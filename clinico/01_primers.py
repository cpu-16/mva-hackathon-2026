#!/usr/bin/env python3
"""Diseña los dos amplicones Sanger para la segregación parental de BUB1B.

Dos reglas, y las dos nacieron de un fallo real, no de la teoría:

1. Ningún primer puede solaparse con un SNP del panel 1000G con AF >= 0.005. Un mismatch
   bajo el primer causa drop-out alélico, que en un test de segregación se lee como
   "este padre no lleva la variante" — el peor error posible aquí.

2. Ningún primer puede caer dentro de un elemento repetido de RepeatMasker. El primer
   par que primer3 devolvió sin esta regla caía en un AluY y tenía ~100 copias exactas
   en GRCh38. El sitio c.2210 está flanqueado por AluY a 272 bp y HAL1 a 600 bp.

La verificación independiente de copia única vive en 02_especificidad.py y es la que manda:
este script propone, aquel dispone.
"""
import json, subprocess, sys

REF = "ref/GRCh38_nochr.fa"
PANEL = "replay/raw/1kgp/chr15.vcf.gz"
FLANK = 1000         # ventana de diseño a cada lado
AF_MIN = 0.005       # umbral de "SNP común" para excluir de las zonas de primer
MARGIN = 80          # nt mínimos entre el fin de cada primer y el sitio causal (lectura Sanger limpia)
MARGIN_MAX = 450     # nt MÁXIMOS: más allá de esto la lectura Sanger ya se degrada y esa dirección
                     # no cubre la variante. Con 80 <= margen <= 450 en ambos lados, las DOS lecturas
                     # la cubren y la secuenciación bidireccional es real, no nominal.

TARGETS = [
    dict(name="BUB1B_c.2210T>G_p.Leu737Ter", pos=40209701, ref="T", alt="G", exon="17/23"),
    dict(name="BUB1B_c.3006T>G_p.Asn1002Lys", pos=40220612, ref="T", alt="G", exon="23/23"),
]


def seq(start, end):
    out = subprocess.run(["samtools", "faidx", REF, f"15:{start}-{end}"],
                         capture_output=True, text=True, check=True).stdout
    return "".join(out.split("\n")[1:]).upper()


def common_snps(start, end):
    out = subprocess.run(
        ["bcftools", "view", "-H", "-r", f"chr15:{start}-{end}", "-v", "snps", PANEL],
        capture_output=True, text=True).stdout
    hits = []
    for line in out.strip().split("\n"):
        if not line:
            continue
        f = line.split("\t")
        af = 0.0
        for kv in f[7].split(";"):
            if kv.startswith("AF="):
                af = max(float(x) for x in kv[3:].split(","))
        if af >= AF_MIN:
            hits.append((int(f[1]), f[3], f[4], af))
    return hits


def repeats(start, end):
    """Intervalos de RepeatMasker (UCSC hg38) que solapan la ventana. Coordenadas 1-based."""
    url = (f"https://api.genome.ucsc.edu/getData/track?genome=hg38;track=rmsk"
           f";chrom=chr15;start={start - 1};end={end}")
    raw = subprocess.run(["curl", "-s", "--max-time", "60", url],
                         capture_output=True, text=True, check=True).stdout
    d = json.loads(raw)
    rows = d.get("rmsk") or d.get("chr15") or []
    assert rows, "UCSC no devolvió repeticiones: sin esa anotación el diseño no es seguro"
    return [(r["genoStart"] + 1, r["genoEnd"], r["repClass"], r["repName"]) for r in rows]


def merge(intervals):
    """Une intervalos solapados. [(a,b)] -> [(a,b)] sin solapes, ordenados."""
    out = []
    for a, b in sorted(intervals):
        if out and a <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def main():
    import primer3
    results = []
    for t in TARGETS:
        start, end = t["pos"] - FLANK, t["pos"] + FLANK
        template = seq(start, end)
        assert len(template) == 2 * FLANK + 1, len(template)
        off = t["pos"] - start
        assert template[off] == t["ref"], f"referencia no coincide: {template[off]} != {t['ref']}"

        snps = common_snps(start, end)
        reps = repeats(start, end)

        excl = [(p, p) for p, _, _, _ in snps if p != t["pos"]]
        excl += [(max(a, start), min(b, end)) for a, b, _, _ in reps]
        merged = merge(excl)
        # a coordenadas del template, 0-based, formato [inicio, longitud]
        excluded = [[a - start, b - a + 1] for a, b in merged]

        design = primer3.bindings.design_primers(
            {"SEQUENCE_ID": t["name"], "SEQUENCE_TEMPLATE": template,
             "SEQUENCE_TARGET": [off - MARGIN, 2 * MARGIN + 1],
             "SEQUENCE_EXCLUDED_REGION": excluded},
            {"PRIMER_TASK": "generic", "PRIMER_PICK_LEFT_PRIMER": 1,
             "PRIMER_PICK_RIGHT_PRIMER": 1, "PRIMER_NUM_RETURN": 20,
             "PRIMER_OPT_SIZE": 22, "PRIMER_MIN_SIZE": 19, "PRIMER_MAX_SIZE": 26,
             "PRIMER_OPT_TM": 60.0, "PRIMER_MIN_TM": 57.0, "PRIMER_MAX_TM": 63.0,
             "PRIMER_PAIR_MAX_DIFF_TM": 2.0,
             "PRIMER_MIN_GC": 35.0, "PRIMER_MAX_GC": 65.0,
             "PRIMER_MAX_POLY_X": 4, "PRIMER_MAX_SELF_ANY_TH": 45.0,
             "PRIMER_MAX_HAIRPIN_TH": 40.0, "PRIMER_PAIR_MAX_COMPL_ANY_TH": 45.0,
             "PRIMER_PRODUCT_SIZE_RANGE": [[300, 2 * MARGIN_MAX]]})

        n = design["PRIMER_PAIR_NUM_RETURNED"]
        assert n > 0, (f"primer3 no devolvió pares para {t['name']} — la ventana libre de "
                       f"repeticiones puede ser demasiado corta")
        picks = []
        for i in range(n):
            lpos, llen = design[f"PRIMER_LEFT_{i}"]
            rpos, rlen = design[f"PRIMER_RIGHT_{i}"]
            amp_start, amp_end = start + lpos, start + rpos
            picks.append(dict(
                rank=i,
                left=design[f"PRIMER_LEFT_{i}_SEQUENCE"], right=design[f"PRIMER_RIGHT_{i}_SEQUENCE"],
                left_tm=round(design[f"PRIMER_LEFT_{i}_TM"], 1),
                right_tm=round(design[f"PRIMER_RIGHT_{i}_TM"], 1),
                left_gc=round(design[f"PRIMER_LEFT_{i}_GC_PERCENT"], 1),
                right_gc=round(design[f"PRIMER_RIGHT_{i}_GC_PERCENT"], 1),
                product=design[f"PRIMER_PAIR_{i}_PRODUCT_SIZE"],
                amplicon=f"chr15:{amp_start}-{amp_end}",
                margin_fwd=t["pos"] - (amp_start + llen),
                margin_rev=amp_end - t["pos"]))
        # descartar los pares en que alguna dirección no alcanza la variante con lectura limpia
        picks = [q for q in picks if q["margin_fwd"] <= MARGIN_MAX and q["margin_rev"] <= MARGIN_MAX]
        assert picks, (f"{t['name']}: ningún par deja la variante dentro de {MARGIN_MAX} nt de AMBOS "
                       f"primers — la ventana libre de repeticiones no lo permite")
        results.append(dict(
            target=t, window=f"chr15:{start}-{end}",
            common_snps=[dict(pos=p, change=f"{r}>{a}", af=round(af, 4)) for p, r, a, af in snps],
            repeats=[dict(start=a, end=b, cls=c, name=nm) for a, b, c, nm in reps],
            excluded_bp=sum(b - a + 1 for a, b in merged), primers=picks))

    json.dump(results, open("clinico/primers.json", "w"), indent=2)
    for r in results:
        t = r["target"]
        print(f"\n=== {t['name']}  ({r['window']}) ===")
        print(f"  {len(r['common_snps'])} SNPs comunes · {len(r['repeats'])} repeticiones · "
              f"{r['excluded_bp']} bp excluidos de {2 * FLANK + 1}")
        print(f"  repeticiones: " + ", ".join(f"{x['name']}({x['start']}-{x['end']})" for x in r["repeats"]))
        print(f"  {len(r['primers'])} pares candidatos; el primero:")
        p = r["primers"][0]
        print(f"    {p['amplicon']}  {p['product']} bp   F {p['left']}  R {p['right']}"
              f"   márgenes {p['margin_fwd']}/{p['margin_rev']} nt")


if __name__ == "__main__":
    main()
