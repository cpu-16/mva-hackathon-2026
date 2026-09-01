#!/usr/bin/env python3
"""Elige el par de primers de cada amplicón verificando especificidad en TODO GRCh38.

Por qué existe: el primer par que primer3 devolvió para el amplicón 1 cae dentro de un
elemento Alu y tiene ~100 copias exactas en el genoma. Un primer así no falla en el
diseño, falla en el laboratorio. Se cuentan las coincidencias exactas de cada primer
candidato y de su reverso complementario en un solo pase sobre el FASTA, y se elige el
par mejor rankeado por primer3 en el que AMBOS primers son de copia única.

Criterio: exactamente una copia en los contigs primarios (1-22, X, Y, M). Las copias en
contigs alt/random del mismo cromosoma son la misma región física y se reportan aparte.

# ponytail: coincidencia exacta, no alineamiento con mismatches. Descarta el fallo grosero
# (repeticiones, pseudogenes) por unos centavos de CPU; el laboratorio igual debe correr
# BLAT / in-silico PCR antes de sintetizar, y la orden lo dice.
"""
import json, sys
from collections import defaultdict

REF = "ref/GRCh38_nochr.fa"
PRIMARY = {str(i) for i in range(1, 23)} | {"X", "Y", "M"}
COMP = str.maketrans("ACGTN", "TGCAN")
rc = lambda s: s.translate(COMP)[::-1]

def scan_genome(seqs):
    """Un pase sobre el FASTA. Devuelve {seq: [posiciones]} de coincidencias exactas
    del patrón y de su reverso complementario."""
    needles = {}
    for s in seqs:
        needles.setdefault(s, []).append(("fwd", s))
        needles[s].append(("rev", rc(s)))
    flat = [(s, o, p) for s, v in needles.items() for o, p in v]
    maxlen = max(len(p) for _, _, p in flat)
    hits = defaultdict(list)
    chrom, buf, offset = None, "", 0
    CH = 1 << 24

    def scan(seg, chrom, base):
        for s, orient, pat in flat:
            start = 0
            while True:
                i = seg.find(pat, start)
                if i < 0:
                    break
                hits[s].append((chrom, base + i + 1, orient))
                start = i + 1

    with open(REF) as fh:
        for line in fh:
            if line[0] == ">":
                if buf:
                    scan(buf, chrom, offset)
                chrom, buf, offset = line[1:].split()[0], "", 0
                continue
            buf += line.strip().upper()
            if len(buf) >= CH:
                scan(buf, chrom, offset)
                keep = maxlen - 1
                offset += len(buf) - keep
                buf = buf[-keep:]
        if buf:
            scan(buf, chrom, offset)
    return hits

def main():
    designs = json.load(open("clinico/primers.json"))
    seqs = sorted({p[side] for d in designs for p in d["primers"] for side in ("left", "right")})
    print(f"Escaneando GRCh38 por {len(seqs)} secuencias candidatas…", flush=True)
    hits = scan_genome(seqs)

    def copies(s):
        prim = [h for h in hits[s] if h[0] in PRIMARY]
        alt = [h for h in hits[s] if h[0] not in PRIMARY]
        return prim, alt

    chosen = []
    for d in designs:
        pick = None
        for p in d["primers"]:
            lp, la = copies(p["left"])
            rp, ra = copies(p["right"])
            if len(lp) == 1 and len(rp) == 1 and lp[0][0] == "15" and rp[0][0] == "15":
                pick = dict(p, left_copies=len(lp), right_copies=len(rp),
                            left_alt=len(la), right_alt=len(ra),
                            left_hit=f"{lp[0][0]}:{lp[0][1]}", right_hit=f"{rp[0][0]}:{rp[0][1]}")
                break
        assert pick is not None, f"ningún par de copia única para {d['target']['name']}"
        rejected = d["primers"].index(next(p for p in d["primers"]
                                           if p["left"] == pick["left"] and p["right"] == pick["right"]))
        worst = max(len(copies(p["left"])[0]) for p in d["primers"])
        chosen.append(dict(target=d["target"], window=d["window"],
                           common_snps=d["common_snps"], chosen=pick,
                           rank_used=rejected, worst_candidate_copies=worst))

    json.dump(chosen, open("clinico/primers_finales.json", "w"), indent=2)
    for c in chosen:
        p, t = c["chosen"], c["target"]
        print(f"\n=== {t['name']} — exón {t['exon']} ===")
        print(f"  amplicón {p['amplicon']}  {p['product']} bp   (candidato #{c['rank_used']} de primer3)")
        print(f"  F  {p['left']}   Tm {p['left_tm']}  GC {p['left_gc']}%  copias {p['left_copies']} en {p['left_hit']} (+{p['left_alt']} en contigs alt)")
        print(f"  R  {p['right']}   Tm {p['right_tm']}  GC {p['right_gc']}%  copias {p['right_copies']} en {p['right_hit']} (+{p['right_alt']} en contigs alt)")
        print(f"  margen de lectura: {p['margin_fwd']} nt desde F, {p['margin_rev']} nt desde R")
        print(f"  peor candidato descartado: {c['worst_candidate_copies']} copias exactas del primer izquierdo")
    return 0

if __name__ == "__main__":
    sys.exit(main())
