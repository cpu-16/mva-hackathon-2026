#!/usr/bin/env python3
"""Mide el error de fase REAL de nuestro procedimiento (Beagle vs panel 1000G),
contra la fase mendeliana del trío GIAB (HG002 hijo, HG003 padre, HG004 madre).
Solo datos públicos. Es el insumo que decide si el estadístico por cromosoma sirve."""
import subprocess, sys, os, gzip, bisect, json
from collections import defaultdict

P = "/home/gar16/datos/HACKATHON-MVA-2026"
CROM = sys.argv[1] if len(sys.argv) > 1 else "chr15"

def calls(sample, crom):
    """pos -> GT normalizado, desde el VCF de referencia GIAB."""
    r = subprocess.run(["bcftools","query","-r",crom,"-f","%POS\t%REF\t%ALT\t[%GT]\n",
                        f"{P}/replay/raw/{sample}.vcf.gz"], capture_output=True, text=True)
    d = {}
    for line in r.stdout.splitlines():
        pos, ref, alt, gt = line.split("\t")
        if "," in alt or len(ref) != 1 or len(alt) != 1: continue   # solo SNV bialélicos
        g = gt.replace("|","/")
        d[int(pos)] = (ref, alt, g)
    return d

def bed(sample, crom):
    ini, fin = [], []
    with open(f"{P}/replay/raw/{sample}_highconf.bed") as f:
        for line in f:
            p = line.split("\t")
            if p[0] == crom: ini.append(int(p[1])); fin.append(int(p[2]))
    return ini, fin

def dentro(ini, fin, pos):
    i = bisect.bisect_right(ini, pos-1) - 1
    return i >= 0 and pos-1 < fin[i]

def gt_de(d, ini, fin, pos):
    """GT del padre/madre: llamada explícita, o 0/0 si el sitio está en su región de confianza."""
    if pos in d: return d[pos][2]
    return "0/0" if dentro(ini, fin, pos) else None

if __name__ == "__main__":
    print(f"cromosoma: {CROM}")
    hijo  = calls("HG002", CROM); padre = calls("HG003", CROM); madre = calls("HG004", CROM)
    bi_p, bf_p = bed("HG003", CROM); bi_m, bf_m = bed("HG004", CROM)
    bi_h, bf_h = bed("HG002", CROM)
    print(f"  llamadas: hijo {len(hijo)}  padre {len(padre)}  madre {len(madre)}")

    verdad = {}   # pos -> '0|1' (ref paterno) o '1|0' (alt paterno)
    razones = defaultdict(int)
    for pos, (ref, alt, g) in hijo.items():
        if g != "0/1": continue
        if not dentro(bi_h, bf_h, pos): razones["fuera_conf_hijo"] += 1; continue
        gp = gt_de(padre, bi_p, bf_p, pos); gm = gt_de(madre, bi_m, bf_m, pos)
        if gp is None or gm is None: razones["fuera_conf_padres"] += 1; continue
        # informativo si al menos un progenitor es homocigoto
        if   gp == "0/0": verdad[pos] = "0|1"          # el ALT vino de la madre
        elif gp == "1/1": verdad[pos] = "1|0"          # el ALT vino del padre
        elif gm == "0/0": verdad[pos] = "1|0"
        elif gm == "1/1": verdad[pos] = "0|1"
        else: razones["ambos_het"] += 1
    print(f"  sitios het del hijo con fase de trío: {len(verdad)}   descartados: {dict(razones)}")
    with gzip.open(f"verdad_trio_{CROM}.tsv.gz","wt") as f:
        for pos in sorted(verdad): f.write(f"{pos}\t{verdad[pos]}\n")
    print(f"  -> verdad_trio_{CROM}.tsv.gz")
