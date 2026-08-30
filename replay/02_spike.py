#!/usr/bin/env python3
"""Constructor de casos de MVA-Replay. Reglas congeladas en PREREGISTRO.md §Experimento C.
Selecciona alelos de ClinVar por regla (no a mano), verifica REF contra el FASTA hg38,
exige region de alta confianza del fondo y ausencia de solapamiento, e inserta.
"""
import subprocess, os, sys, csv, json

ROOT  = "/home/gar16/datos/HACKATHON-MVA-2026"
REP   = f"{ROOT}/replay"
CLIN  = f"{ROOT}/pipeline/resources/clinvar.vcf.gz"
FASTA = f"{REP}/raw/fasta"          # chrN.fa.bgz
BEDS  = f"{REP}/raw"                # HGxxx_highconf.bed
BG    = f"{REP}/bg"                 # HGxxx.vcf.gz (sin INFO)
POOLS = f"{REP}/pools"
CASES = f"{REP}/cases"

# Ensembl REST, recuperado 30-ago-2026 (mismo metodo que pipeline/mva_panel.provenance.tsv)
GENES = {
    "BUB1B": ("chr15", 40155983, 40226137),
    "CEP57": ("chr11", 95784964, 95842070),
    "TRIP13":("chr5",    887848,  924357),
    "FANCD2":("chr3",  10021370, 10106937),   # 10026370-10101937 +/-5kb
    "SMC5":  ("chr9",  70253269, 70359874),   # centinela: valida el builder, no es caso
}
# consecuencias que analysis_mva.yml CONSERVA (variantEffectFilter borra intronicas/up/down)
KEEP_MC = ("missense", "nonsense", "frameshift", "splice_acceptor", "splice_donor")

def clnsig_atoms(s):
    out = []
    for a in s.replace("|", "/").split("/"):
        out.append(a.strip("_ "))
    return out

def pool(gene, klass):
    """Pool ClinVar por la regla del pre-registro. klass in {'PLP','VUS'}."""
    chrom, start, end = GENES[gene]
    reg = f"{chrom.replace('chr','')}:{start}-{end}"
    q = subprocess.run(["bcftools","query","-r",reg,
        "-f","%POS\t%REF\t%ALT\t%ID\t%INFO/CLNSIG\t%INFO/CLNREVSTAT\t%INFO/MC\n", CLIN],
        capture_output=True, text=True)
    rows = []
    for line in q.stdout.splitlines():
        pos, ref, alt, vid, sig, rev, mc = line.split("\t")
        # ENMIENDA 1 (30-ago): la regla escrita decia "contiene criteria_provided", que
        # tambien acepta no_assertion_criteria_provided (0 estrellas). Se exige >=1 estrella.
        if not (rev.startswith("criteria_provided")
                or rev in ("reviewed_by_expert_panel","practice_guideline")): continue
        if "," in alt or len(ref) > 50 or len(alt) > 50: continue
        atoms = clnsig_atoms(sig)
        if klass == "PLP":
            if not any(a in ("Pathogenic","Likely_pathogenic") for a in atoms): continue
        else:
            if sig != "Uncertain_significance": continue
        if not any(k in mc for k in KEEP_MC): continue
        rows.append({"chrom":chrom,"pos":int(pos),"ref":ref,"alt":alt,
                     "clinvar_id":vid,"clnsig":sig,"clnrevstat":rev,"mc":mc})
    rows.sort(key=lambda r: r["pos"])
    return rows

def ref_ok(chrom, pos, ref):
    fa = f"{FASTA}/{chrom}.fa.bgz"
    if not os.path.exists(fa): return None
    r = subprocess.run(["samtools","faidx",fa,f"{chrom}:{pos}-{pos+len(ref)-1}"],
                       capture_output=True, text=True)
    seq = "".join(r.stdout.split("\n")[1:]).upper()
    return seq == ref.upper()

def en_alta_confianza(sample, chrom, pos):
    bed = f"{BEDS}/{sample}_highconf.bed"
    if not os.path.exists(bed): return None
    with open(bed) as f:
        for line in f:
            c, s, e = line.split("\t")[:3]
            if c == chrom and int(s) <= pos-1 < int(e): return True
    return False

def solapa(sample, chrom, pos, ref):
    r = subprocess.run(["bcftools","view","-H","-r",
                        f"{chrom}:{max(1,pos-60)}-{pos+len(ref)+60}", f"{BG}/{sample}.vcf.gz"],
                       capture_output=True, text=True)
    for line in r.stdout.splitlines():
        f = line.split("\t")
        p, rf = int(f[1]), f[3]
        if p <= pos + len(ref) - 1 and pos <= p + len(rf) - 1:
            return True
    return False

def elegir_par(gene, klass_a, klass_b, sample, fijos=None):
    """Devuelve (alelo1, alelo2) por la regla: primero y ultimo del pool que sobrevivan
    a REF / alta confianza / no solapamiento. `fijos` fuerza registros nombrados."""
    if fijos: cand_a = cand_b = None
    pa = [r for r in pool(gene, klass_a)]
    pb = pa if klass_a == klass_b else [r for r in pool(gene, klass_b)]
    def valido(r):
        return (ref_ok(r["chrom"], r["pos"], r["ref"]) is True
                and en_alta_confianza(sample, r["chrom"], r["pos"]) is True
                and not solapa(sample, r["chrom"], r["pos"], r["ref"]))
    a = next((r for r in pa if valido(r)), None)
    b = next((r for r in reversed(pb) if valido(r) and (a is None or r["pos"] != a["pos"])), None)
    return a, b

def construir(caso, sample, alelos, fase="trans"):
    """alelos = lista de dicts con chrom/pos/ref/alt. Inserta en el fondo."""
    os.makedirs(CASES, exist_ok=True)
    bg = f"{BG}/{sample}.vcf.gz"
    hdr = subprocess.run(["bcftools","view","-h",bg], capture_output=True, text=True).stdout
    spk = f"{CASES}/{caso}.spike.vcf"
    gts = {"trans":["0|1","1|0"], "cis":["0|1","0|1"], "unph":["0/1","0/1"]}[fase]
    with open(spk,"w") as f:
        f.write(hdr)
        for i, a in enumerate(sorted(alelos, key=lambda x:(x["chrom"], x["pos"]))):
            f.write(f'{a["chrom"]}\t{a["pos"]}\t.\t{a["ref"]}\t{a["alt"]}\t100\tPASS\t.\t'
                    f'GT:DP:AD:GQ\t{gts[i%2]}:44:22,22:99\n')
    subprocess.run(["bgzip","-f",spk], check=True)
    subprocess.run(["tabix","-f","-p","vcf",spk+".gz"], check=True)
    out = f"{CASES}/{caso}.vcf.gz"
    subprocess.run(["bcftools","concat","-a","-Oz","-o",out,bg,spk+".gz"],
                   check=True, capture_output=True)
    subprocess.run(["tabix","-f","-p","vcf",out], check=True)
    return out

def verificar_insercion(caso, alelos):
    """Assert 1 del pre-registro: los alelos plantados estan en el VCF construido."""
    out = f"{CASES}/{caso}.vcf.gz"
    ok = []
    for a in alelos:
        r = subprocess.run(["bcftools","view","-H","-r",f'{a["chrom"]}:{a["pos"]}-{a["pos"]}',out],
                           capture_output=True, text=True)
        ok.append(any(l.split("\t")[3]==a["ref"] and l.split("\t")[4]==a["alt"]
                      for l in r.stdout.splitlines()))
    return all(ok)

if __name__ == "__main__":
    os.makedirs(POOLS, exist_ok=True)
    for g in GENES:
        for k in ("PLP","VUS"):
            rows = pool(g, k)
            with open(f"{POOLS}/{g}_{k}.tsv","w",newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else
                                   ["chrom","pos","ref","alt","clinvar_id","clnsig","clnrevstat","mc"],
                                   delimiter="\t")
                w.writeheader(); w.writerows(rows)
            print(f"{g:8s} {k:4s} pool={len(rows)}")
