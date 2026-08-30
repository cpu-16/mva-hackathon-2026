#!/usr/bin/env python3
"""Compara la fase de Beagle contra la verdad del trío. Devuelve tasa de switch,
distribución de longitudes de segmento y la dilución que sufriría la media con signo."""
import subprocess, gzip, sys, json, numpy as np
CROM = sys.argv[1] if len(sys.argv) > 1 else "chr15"

verdad = {}
with gzip.open(f"verdad_trio_{CROM}.tsv.gz","rt") as f:
    for line in f:
        p, g = line.split()
        verdad[int(p)] = g

r = subprocess.run(["bcftools","query","-f","%POS\t[%GT]\n", f"hg002_{CROM}_fasado.vcf.gz"],
                   capture_output=True, text=True)
bea = {}
for line in r.stdout.splitlines():
    pos, gt = line.split("\t")
    if gt in ("0|1","1|0"): bea[int(pos)] = gt

com = sorted(set(verdad) & set(bea))
print(f"sitios het con fase de trío: {len(verdad)}")
print(f"sitios het fasados por Beagle: {len(bea)}")
print(f"comunes (los que se pueden comparar): {len(com)}")
if not com: sys.exit("sin solapamiento")

# orientación: +1 si Beagle coincide con el trío, -1 si está invertido
ori = np.array([1 if bea[p] == verdad[p] else -1 for p in com])
pos = np.array(com)
cambios = np.flatnonzero(np.diff(ori) != 0)
n_switch = len(cambios)
tasa = n_switch / (len(ori) - 1)
print(f"\n  switches observados: {n_switch}")
print(f"  tasa de switch por par de sitios consecutivos: {tasa*100:.3f}%")

bordes = np.concatenate(([0], cambios + 1, [len(ori)]))
tam = np.diff(bordes)
print(f"  segmentos de fase: {len(tam)}")
print(f"  tamaño de segmento (sitios): mediana {int(np.median(tam))}  media {tam.mean():.0f}  máx {tam.max()}")
largos_bp = [pos[bordes[i+1]-1] - pos[bordes[i]] for i in range(len(tam))]
print(f"  tamaño de segmento (bp):     mediana {int(np.median(largos_bp)):,}  media {np.mean(largos_bp):,.0f}")

# dilución de la media con signo: |sum(w_s * o_s)| con o_s la orientación del segmento
w = tam / tam.sum()
o = np.array([ori[bordes[i]] for i in range(len(tam))])
dilucion_real = abs((w * o).sum())
dilucion_esperada = np.sqrt((w**2).sum())     # si la orientación fuera aleatoria
print(f"\n  DILUCIÓN de la media con signo por cromosoma:")
print(f"    factor realizado en este cromosoma: {dilucion_real:.4f}  ({1/dilucion_real:.0f}x de pérdida)" if dilucion_real>0 else "    ~0")
print(f"    escala esperada con orientación aleatoria: {dilucion_esperada:.4f}  ({1/dilucion_esperada:.0f}x)")
print(f"    -> el estadístico invariante a orientación (enmienda 1) NO sufre esta pérdida")
json.dump({"crom":CROM,"n_comparables":len(com),"n_switch":n_switch,"tasa_switch":tasa,
           "n_segmentos":int(len(tam)),"seg_sitios_mediana":int(np.median(tam)),
           "seg_bp_mediana":int(np.median(largos_bp)),
           "dilucion_realizada":float(dilucion_real),"dilucion_esperada":float(dilucion_esperada)},
          open(f"switch_{CROM}.json","w"), indent=1)
