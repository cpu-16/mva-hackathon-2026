# Results — pre-registered test of the aneuploidy→proteasome dependency outside myeloma

**Team ciberpty · run 2026-08-30.** Hypotheses, drug list, statistics and stopping rules were fixed in
`PREREGISTRO.md` (git commit `4b0b7c2`) **before** any of this was computed; the amendment declaring
the CRISPR extension is commit `c54e678`, also before that extension was run.

**Headline: our own candidate did not hold up in solid tumours, and we report it.**

## What we did

We built an arm-level aneuploidy score for 2,420 cancer cell lines from DepMap 24Q4 absolute
copy-number segments, then asked whether it predicts (A) sensitivity to seven pre-locked drugs in the
PRISM Repurposing screen and (B) genetic dependency on proteasome subunits in DepMap CRISPR.

**Score validation (positive/negative control).** Chromosomally stable, MSI colorectal lines score low
(DLD1 = 0, RKO = 10; mean 5.0); CIN lines score high (HT29 = 21, SW620 = 12; mean 16.5). The score
discriminates in the expected direction on lines whose biology is known independently.

**Pipeline validation.** Across all 6,790 PRISM compounds in 444 solid-tumour lines, 1.1% reach
p < 0.001 against 0.1% expected by chance — an 11-fold enrichment. The machinery detects associations
when they exist, so the nulls below are not an artefact of a broken pipeline.

## A — Drug sensitivity (PRISM Repurposing, 444 solid-tumour lines)

| Drug | ρ | p | q (BH) | Predicted | Result |
|---|---|---|---|---|---|
| Bortezomib | **−0.075** | 0.11 | 0.40 | sensitive | direction right, **not significant** |
| Carfilzomib | −0.060 | 0.22 | 0.51 | sensitive | direction right, not significant |
| Ixazomib | +0.028 | 0.55 | 0.68 | sensitive | **wrong direction** |
| Metformin | +0.020 | 0.68 | 0.68 | null | null, as predicted |
| Trametinib | +0.037 | 0.44 | 0.68 | null | null |
| Everolimus | −0.025 | 0.59 | 0.68 | not sensitive | null |
| Paclitaxel (control) | +0.096 | 0.045 | 0.31 | null | opposite direction |

**No test passed FDR < 0.05.** Bortezomib and carfilzomib sit in the 4th and 8th percentile of all
6,790 compounds by direction — suggestive, and no more than that. Paclitaxel goes the other way, so
this is not a generic "sick cells die more" confound.

**H2 could not be tested.** The seven drugs exist only in the `REP.PRIMARY` screen, which used an
adherent-only cell-line collection: of 98 haematological lines with an aneuploidy score, **zero** have
a bortezomib measurement. The solid-versus-haematological contrast is not computable from PRISM. We
discovered this only after downloading, and recorded it in the amendment.

## B — Genetic dependency (DepMap CRISPR, 946 lines, both strata)

| Stratum | n | PSMB5 ρ | q (BH) | 20S core mean ρ | Core subunits at FDR<0.05 |
|---|---|---|---|---|---|
| All | 946 | **−0.198** | **5.2×10⁻⁸** | −0.062 | 5 / 14 |
| **Haematological** | 113 | **−0.261** | **0.042** | −0.104 | 1 / 14 |
| **Solid tumour** | 833 | −0.077 | 0.118 | −0.031 | **0 / 14** |

`PSMD9`, the pre-declared negative control, is null everywhere (q ≥ 0.46). Against a background of 200
random genes, the 20S core in solid lines separates by **z = −0.51** — indistinguishable from noise.

**Confounders, checked.** Adjusting for ploidy and lineage stratum, aneuploidy still predicts PSMB5
dependency overall (β = −0.0079, p = 0.0098), and **ploidy itself contributes nothing** (p = 0.88), so
this is not whole-genome doubling in disguise. Within solid lines alone the association does not reach
significance (β = −0.0056, p = 0.077). The formal test of the question we asked — the
**aneuploidy × lineage interaction — is significant (p = 0.026)**: the association is genuinely weaker
in solid tumours, not merely underpowered there. Note that solid lines are the *larger* stratum
(833 vs 113), so this is not a sample-size artefact. Haematological lines are also markedly *less*
aneuploid (mean 9.3 vs 18.7 altered arms, p = 6×10⁻²⁴), which makes the stronger association within
them more striking, not less.

## What this forces us to write

Two independent measurements — drug sensitivity and genetic dependency — point the same way:

> **The aneuploidy→proteasome-dependency link that our bortezomib argument rests on is detectable in
> haematological lineages, where myeloma sits, and is significantly attenuated in solid tumours.**

This child's tumour was an embryonal rhabdomyosarcoma — a solid tumour. Our §4 "prepared answer for a
second tumour" therefore rests on evidence that **we ourselves could not extend to the relevant
lineage**. We are not withdrawing the proposal: the direction of effect is preserved for two of three
proteasome inhibitors, the mechanism is unchanged, and a null in heterogeneous cancer lines is not a
null in constitutional MVA. But the claim is now explicitly weaker than it was before we ran this, and
the report says so.

## Limitations we state ourselves

- PRISM Repurposing primary is a **single-dose (2.5 µM) viability screen**, not an EC50, and not the
  isogenic diploid-versus-aneuploid comparison Ippolito used. This is not a replication attempt of
  Ippolito and we do not describe it as one.
- Cancer cell lines are not constitutional mosaic aneuploidy. A null here does not refute the
  mechanism in MVA; it removes a supporting argument we had been leaning on.
- The arm-level score is our own definition (pre-registered), not an imported published score. It
  validates on known lines, but a different definition could give different magnitudes.
- CRISPR gene effect measures dependency on the target, not response to the drug. They are related,
  not identical.

## Reproducing this

```bash
cd depmap
python3 01_aneuploidy_score.py     # score de aneuploidía por línea
python3 02_prereg_test.py          # prueba pre-registrada (PRISM)
python3 03_crispr_extension.py     # extensión declarada (CRISPR)
python3 04_figura.py               # figura 4
```
All inputs are public (DepMap 24Q4 figshare 27993248; PRISM Repurposing 24Q2 figshare 25917643).
No patient data is used anywhere in this analysis.


---
**Note added 2026-09-08.** The three numbers in *Confounders, checked* (β = −0.0079, p = 0.0098; ploidy
p = 0.88; interaction p = 0.026) were computed ad hoc when this file was written. They are now
reproduced by `05_seguimiento.py`: the first two come from the main-effects model, the third from the
model with the interaction term. Effect sizes with intervals, the lineage structure, the assay overlap,
the score-definition sensitivity and the rhabdomyosarcoma coverage are in `RESULTADOS_SEGUIMIENTO.md`
(pre-registered in `PREREGISTRO_SEGUIMIENTO.md`, commit `ee59c9e`). The phrase "two independent
measurements" above overstates: the assays share 365 solid models and agree with each other only at
ρ = −0.070.
