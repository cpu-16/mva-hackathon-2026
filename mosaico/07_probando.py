#!/usr/bin/env python3
"""Estadístico del probando. Se corre DESPUÉS de commitear la calibración.
Fasa con Beagle contra el panel 1000G, cruza la fase con los AD del VCF, y calcula
Psi (invariante a orientación, ventana W elegida en datos públicos) y phi (secundario)."""
import subprocess, os, sys, gzip, json, glob, numpy as np
REP = os.path.dirname(os.path.abspath(__file__))
P = "/home/gar16/datos/HACKATHON-MVA-2026"
W = json.load(open(f"{REP}/ventana.json"))["W_elegida"]

def fasar(c):
    """Beagle sobre el cromosoma c del probando contra el panel."""
    salida = f"{REP}/fase/probando_chr{c}"
    if os.path.exists(salida + ".vcf.gz"): return salida + ".vcf.gz"
    os.makedirs(f"{REP}/fase", exist_ok=True)
    ent = f"{REP}/fase/_in_chr{c}.vcf.gz"
    if not os.path.exists(ent):
        with open("/tmp/_ren.txt", "w") as f: f.write(f"{c}\tchr{c}\n")
        subprocess.run(f"bcftools view -r {c} -v snps -m2 -M2 -f PASS "
                       f"{P}/data/WGS_EX2312012_HGWCNDSX7.vcf.gz 2>/dev/null "
                       f"| bcftools annotate --rename-chrs /tmp/_ren.txt -Oz -o {ent}",
                       shell=True, check=True)
        subprocess.run(["bcftools","index","-t",ent], check=True)
    panel = f"{P}/replay/raw/1kgp/chr{c}.vcf.gz"
    mapa  = f"{REP}/fase/plink.chr{c}.GRCh38.map"
    if not os.path.exists(mapa):
        subprocess.run(f"unzip -o -q -j {P}/fase/mapa_chr15.zip 'chr_in_chrom_field/plink.chrchr{c}.GRCh38.map' -d {REP}/fase "
                       f"&& mv {REP}/fase/plink.chrchr{c}.GRCh38.map {mapa}", shell=True)
    subprocess.run(["java","-Xmx10g","-jar",f"{P}/fase/beagle.jar",
                    f"gt={ent}", f"ref={panel}", f"map={mapa}",
                    f"out={salida}", "nthreads=8", "seed=2026"],
                   stdout=open(f"{REP}/fase/_beagle_chr{c}.log","w"), stderr=subprocess.STDOUT)
    subprocess.run(["tabix","-f","-p","vcf",salida+".vcf.gz"])
    os.remove(ent); os.remove(ent+".tbi")
    return salida + ".vcf.gz"

def estadistico(c):
    sitios = {}
    with gzip.open(f"{REP}/sitios/chr{c}.tsv.gz","rt") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 5: continue
            ad = p[4].split(",")
            if len(ad) != 2: continue
            r_, a_ = int(ad[0]), int(ad[1])
            if r_ + a_ < 10: continue
            sitios[int(p[0])] = (r_, a_)
    v = fasar(c)
    r = subprocess.run(["bcftools","query","-f","%POS\t[%GT]\n", v], capture_output=True, text=True)
    pos, s, b = [], [], []
    for line in r.stdout.splitlines():
        pp, gt = line.split("\t")
        pp = int(pp)
        if pp not in sitios or gt not in ("0|1","1|0"): continue
        ref, alt = sitios[pp]
        pos.append(pp); s.append(1.0 if gt == "1|0" else -1.0)   # +1 si el ALT va en el haplotipo 1
        b.append(alt / (ref + alt))
    if len(pos) < 5000: return None
    s = np.array(s); b = np.array(b); dev = s * (b - 0.5)
    n = len(dev); S = n // W
    win = dev[:S*W].reshape(S, W)
    phi_s = win.mean(axis=1)
    v_s = np.var(dev, ddof=1) / W           # varianza nula estimada de los propios datos
    Psi = np.mean(phi_s**2 - v_s)
    return {"crom": c, "n_sitios": n, "n_ventanas": int(S), "phi": float(dev.mean()),
            "Psi": float(Psi), "sd_sitio": float(np.std(dev, ddof=1))}

if __name__ == "__main__":
    croms = sorted(int(os.path.basename(f)[3:].split(".")[0])
                   for f in glob.glob(f"{REP}/sitios/chr*.tsv.gz"))
    print(f"ventana elegida en datos públicos: W = {W} sitios")
    print(f"cromosomas: {croms}\n")
    out = []
    for c in croms:
        d = estadistico(c)
        if d:
            out.append(d)
            print(f"  chr{c:<2}  n={d['n_sitios']:>7}  ventanas={d['n_ventanas']:>4}  "
                  f"phi={d['phi']:+.6f}  Psi={d['Psi']:+.3e}", flush=True)
    json.dump(out, open(f"{REP}/probando.json","w"), indent=1)
    print("\n-> probando.json")
