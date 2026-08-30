#!/usr/bin/env python3
"""Paso 1 — puntuación de aneuploidía por línea celular, EXACTAMENTE como se pre-registró.

Se corre ANTES de tocar los datos de fármacos, a propósito: la definición del score no puede
depender de lo que se vea después. Ver PREREGISTRO.md.

Definición (pre-registrada):
  1. Segmentos de CN absoluto -> brazos cromosómicos (centrómeros hg38, arms_hg38.tsv).
  2. Por brazo: mediana de CN ponderada por longitud.
  3. Ploidía de la línea: mediana ponderada de CN sobre todos los autosomas.
  4. Brazo ganado si >= ploidia+0.5; perdido si <= ploidia-0.5.
  5. Score = nº de brazos autosómicos alterados (0-39).
     Brazos con <50% de cobertura no se llaman. Líneas con <30 brazos llamables se descartan.
"""
import pandas as pd, numpy as np, sys

RAW = "raw/"

def weighted_median(vals, wts):
    o = np.argsort(vals); v, w = np.asarray(vals)[o], np.asarray(wts)[o]
    c = np.cumsum(w)
    if c[-1] == 0: return np.nan
    return v[np.searchsorted(c, c[-1] / 2.0)]

cen = pd.read_csv("arms_hg38.tsv", sep="\t", dtype={"chrom": str}).set_index("chrom")["centromere"]

seg = pd.read_csv(RAW + "OmicsAbsoluteCNSegmentsProfile.csv",
                  usecols=["ProfileID", "Chromosome", "Start", "End", "SegmentAbsoluteCN"],
                  dtype={"Chromosome": str})
seg = seg[seg.Chromosome.isin(cen.index)].dropna(subset=["SegmentAbsoluteCN"]).copy()
print(f"segmentos autosómicos: {len(seg):,} en {seg.ProfileID.nunique():,} perfiles")

# asignar cada segmento a un brazo; los que cruzan el centrómero se parten
cn = seg.Chromosome.map(cen)
p = seg[seg.End <= cn].assign(arm=lambda d: d.Chromosome + "p")
q = seg[seg.Start >= cn].assign(arm=lambda d: d.Chromosome + "q")
x = seg[(seg.Start < cn) & (seg.End > cn)]
xp = x.assign(End=x.Chromosome.map(cen), arm=x.Chromosome + "p")
xq = x.assign(Start=x.Chromosome.map(cen), arm=x.Chromosome + "q")
S = pd.concat([p, q, xp, xq], ignore_index=True)
S["len"] = (S.End - S.Start).clip(lower=0)
S = S[S.len > 0]

# longitud de cada brazo = mayor extensión observada (los datos no traen longitudes de referencia)
armlen = S.groupby("arm").apply(lambda d: d.End.max() - d.Start.min(), include_groups=False)

rows = []
for pid, g in S.groupby("ProfileID"):
    ploidy = weighted_median(g.SegmentAbsoluteCN.values, g.len.values)
    if not np.isfinite(ploidy): continue
    n_alt = n_call = 0
    for arm, ga in g.groupby("arm"):
        cov = ga.len.sum() / armlen[arm]
        if cov < 0.5: continue          # brazo no llamable
        n_call += 1
        m = weighted_median(ga.SegmentAbsoluteCN.values, ga.len.values)
        if m >= ploidy + 0.5 or m <= ploidy - 0.5: n_alt += 1
    if n_call >= 30:                     # umbral pre-registrado
        rows.append((pid, ploidy, n_call, n_alt))

df = pd.DataFrame(rows, columns=["ProfileID", "ploidy", "arms_callable", "aneuploidy_score"])
df.to_csv("aneuploidy_scores.csv", index=False)
print(f"\nlíneas con score: {len(df):,}")
print(df.aneuploidy_score.describe().round(2).to_string())
print(f"\nploidía mediana {df.ploidy.median():.2f} | brazos llamables mediana {df.arms_callable.median():.0f}")
