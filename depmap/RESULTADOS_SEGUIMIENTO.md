# Results — pre-registered follow-up of the DepMap analysis (effect sizes, structure, sensitivity)

**Team ciberpty · run 2026-09-07, ~23:43–23:46 EST** (the pre-registration header misstates the date as 8 Sep; the git timestamps govern). Plan fixed in `PREREGISTRO_SEGUIMIENTO.md`
(commit `ee59c9e`) before `05_seguimiento.py` was written. One run; seed 20260908; 2,000 bootstrap
resamples. Outputs: `resultados_seguimiento.csv`, `resultados_seguimiento_lineajes.csv`,
`resultados_seguimiento_loo.csv`, `resultados_seguimiento_rms.csv`, `resultados_seguimiento.json`,
`fig5_seguimiento.png`, `_seguimiento_stdout.txt`. The script was executed a second time only to fix an
axis label on the figure; every number is identical (deterministic seed).

**Headline: all four predictions held. The primary verdict does not change — the solid-stratum drug
association is compatible with zero, and the solid/haematological difference is real under the fitted
model and not driven by any single lineage. Two things the primary report did not say are now on the
record: the ad-hoc interaction numbers reproduce from a committed script, and the child's tumour type is
essentially unrepresented in the drug screen — and the three rhabdomyosarcoma lines that are there sit
among the least sensitive.**

## S1 — effect sizes with 95% bootstrap intervals (ρ < 0 = more aneuploid → more sensitive / dependent)

| Measure | Stratum | n | ρ | 95% CI |
|---|---|---:|---:|---|
| PRISM bortezomib | solid | 444 | −0.075 | −0.168 to +0.017 |
| PRISM carfilzomib | solid | 424 | −0.060 | −0.156 to +0.036 |
| PRISM ixazomib | solid | 438 | +0.028 | −0.059 to +0.116 |
| PRISM metformin | solid | 438 | +0.020 | −0.075 to +0.117 |
| PRISM trametinib | solid | 441 | +0.037 | −0.062 to +0.132 |
| PRISM everolimus | solid | 441 | −0.025 | −0.121 to +0.069 |
| PRISM paclitaxel (control) | solid | 440 | +0.096 | +0.004 to +0.191 |
| CRISPR PSMB5 | all | 946 | −0.198 | −0.260 to −0.133 |
| CRISPR PSMB5 | solid | 833 | −0.077 | −0.149 to −0.009 |
| CRISPR PSMB5 | haematological | 113 | −0.261 | −0.422 to −0.084 |
| CRISPR 20S-core mean | all | 946 | −0.190 | −0.250 to −0.130 |
| CRISPR 20S-core mean | solid | 833 | −0.096 | −0.161 to −0.027 |
| CRISPR 20S-core mean | haematological | 113 | −0.277 | −0.441 to −0.097 |

**P-S1 confirmed:** the bortezomib interval includes zero. Every PRISM proteasome-inhibitor interval
includes zero. Note for honesty in the other direction: the solid-stratum **PSMB5 bootstrap interval
excludes zero narrowly** (−0.149 to −0.009) although the pre-registered FDR test did not pass
(q = 0.118). We keep the pre-registered verdict — a bootstrap interval is descriptive uncertainty, not a
new test — and report both.

## S2 — the interaction as a coefficient (n = 946)

`PSMB5 ~ score + haem + score×haem + ploidy`:

| Term | β | 95% CI (analytic) | p | 95% CI (bootstrap) |
|---|---:|---|---:|---|
| score (solid slope) | −0.00601 | −0.01217 to +0.00016 | 0.056 | — |
| haem | +0.921 | +0.726 to +1.115 | 1×10⁻¹⁹ | — |
| **score × haem** | **−0.01675** | **−0.03144 to −0.00206** | **0.0255** | **−0.03222 to −0.00340** |
| ploidy | +0.007 | −0.053 to +0.068 | 0.82 | — |

Main-effects model `PSMB5 ~ score + haem + ploidy`: score β = −0.00786 (−0.01382 to −0.00190,
p = 0.0098); ploidy β = +0.005 (p = 0.875). **So the three ad-hoc numbers in `RESULTADOS.md` do
reproduce**: "β = −0.0079, p = 0.0098" and "ploidy p = 0.88" are from the main-effects model, and
"interaction p = 0.026" is from the full model. The report now says which is which.

Effect in units a reader can picture: **per 10 additional altered arms, PSMB5 gene effect moves by
−0.06 in solid lines and −0.23 in haematological lines** (more negative = more essential).

**P-S2 confirmed:** both intervals of the interaction exclude zero.

## S3 — inside the solid stratum, by lineage

Seventeen solid lineages reach the pre-registered floor of n ≥ 20 for CRISPR PSMB5 and ten for PRISM
bortezomib. **Every within-lineage interval overlaps zero** — all 27 of them — for both readouts (table in
`resultados_seguimiento_lineajes.csv`; figure `fig5_seguimiento.png`, right panel). Point estimates
scatter on both sides of zero (PSMB5: 12 negative, 5 positive among the 17; bortezomib: 5 and 5). No
lineage is singled out, as pre-committed (P-S4).

## S4 — leave-one-lineage-out

Dropping each of the 26 solid lineages in turn: bortezomib ρ stays within −0.100 to −0.053; PSMB5 ρ
within −0.091 to −0.067; the interaction β within −0.0182 to −0.0159 with p from 0.013 to 0.037, and
its analytic 95% CI never crosses zero. **P-S3 confirmed: not driven by any single lineage** (the
pre-registered criterion). That is all this test can say — it does not establish a clinically meaningful
solid-tumour effect, and the solid slope itself (β = −0.006, p = 0.056) remains compatible with zero.

## S5 — rhabdomyosarcoma: a coverage statement, not a result

Seventeen scored RMS lines (7 embryonal, 8 alveolar, 1 pleomorphic, 1 unspecified; scores 0–27, ploidy
2–4). **Three** have a PRISM bortezomib value and **ten** have a CRISPR PSMB5 value. No statistic is
computed on them. Descriptively: at PRISM's single 2.5 µM dose, the three RMS lines (LFC −1.73, −2.51,
−2.65) are **less killed than 98%, 91% and 89% of the 444 solid lines** (solid median LFC −4.20,
IQR −5.09 to −3.40). The ten CRISPR values sit between the 24th and 84th percentile of the solid
PSMB5 distribution — unremarkable. **The child's tumour type is essentially absent from the drug screen,
and the little that is there does not favour bortezomib.** This is a different assay from the 13–26 nM
in-vitro sensitivity reported for RMS lines (PMID 18342500, cited in the report's §4), and it is
consistent with the limited in-vivo activity the PPTP reported for solid-tumour xenografts.

## S6 — the two assays on the same models

365 solid models carry both measurements. In that set, bortezomib LFC and PSMB5 gene effect correlate
at ρ = −0.070 (−0.176 to +0.033): **the two readouts barely agree with each other**. Their correlations
with the score in the shared set are −0.087 (−0.186 to +0.018) and −0.029 (−0.131 to +0.068). They are
different modalities on overlapping models, not independent replications, and the report now says so.

## S7 — sensitivity to the score definition

| Score | bortezomib ρ | carfilzomib ρ | ixazomib ρ | interaction β (p) |
|---|---:|---:|---:|---|
| altered arms (primary) | −0.075 | −0.060 | +0.028 | −0.0168 (0.026) |
| fraction of callable arms | −0.077 | −0.054 | +0.032 | −0.685 (0.024) |
| ploidy-residualised | −0.028 | −0.028 | +0.018 | −0.0234 (0.029) |

**P-S5 confirmed — no sign changes.** But the residualised score shrinks the bortezomib and carfilzomib
correlations by more than half (−0.075 → −0.028): part of the small drug-sensitivity signal travels
with ploidy-correlated aneuploidy. The interaction is unaffected by the definition.

## What this forces us to write in §3.5

Per the pre-registered mapping (P-S2 and P-S3 hold): *"The attenuation in solid lineages is not an
artefact of any single lineage and its interval excludes zero; the solid-stratum association itself
remains compatible with zero."* Plus, for any outcome: the RMS coverage limitation, the 365-model overlap
and the near-zero agreement between the readouts, and the corrected attribution of the interaction
numbers.

## Limitations

Cancer cell lines, single-dose viability, an arm-count score of our own definition, and no
constitutional MVA cells anywhere. Bootstrap intervals are descriptive. Leave-one-lineage-out tests
composition, not confounding by lineage-correlated biology.
