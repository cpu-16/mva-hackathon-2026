# Pre-registered follow-up — effect sizes, lineage structure and sensitivity of the DepMap result

**Team ciberpty · MVA Hackathon 2026 · written 2026-09-08, 00:50, BEFORE `05_seguimiento.py` exists or runs.**

**Status: a follow-up informed by the primary results, not an untouched confirmatory test.** The
primary pre-registration (`PREREGISTRO.md`, commit `4b0b7c2`) and its amendment (`c54e678`) stand
unchanged, and so do their results (`RESULTADOS.md`). Nothing below can turn a null into a positive: no
new hypothesis test is added to the FDR family, and no new drug or gene is added. What is added is what
an expert reader asked for after reading the result (`evidencia/codex_juez_rubrica_2026-09-07.md`,
change #2): **effect sizes with uncertainty, the interaction as a coefficient with an interval, the
lineage structure underneath the pooled "solid" stratum, the representation of the child's tumour
type, the overlap between the two assays, and the sensitivity of the result to the score definition.**

This file is committed and pushed before the script is written. Results are appended below the line,
dated. The text above the line is not edited afterwards.

## What is already known, declared so nothing here can be mistaken for a blind test

- PRISM, 444 solid lines: bortezomib ρ = −0.075 (p = 0.11, q = 0.40); carfilzomib −0.060; ixazomib
  +0.028; metformin +0.020; trametinib +0.037; everolimus −0.025; paclitaxel +0.096 (p = 0.045).
  No test passed FDR 0.05. Haematological lines have no PRISM measurement for these drugs.
- CRISPR, 946 lines: PSMB5 ρ = −0.198 overall (q = 5×10⁻⁸); −0.261 haematological (n = 113);
  −0.077 solid (n = 833, q = 0.12). 0 of 14 20S subunits at FDR 0.05 in solid lines.
- The interaction sentence in `RESULTADOS.md` ("aneuploidy × lineage interaction p = 0.026",
  "ploidy contributes nothing, p = 0.88", "β = −0.0079, p = 0.0098") **has no committed script**. It was
  computed ad hoc on `psmb5_merged.csv`. Re-deriving it today with ordinary least squares on that
  file gives, for the model `PSMB5 ~ score + haem + score×haem + ploidy` (n = 946): score
  β = −0.0060 (p = 0.056), score×haem β = −0.0168 (**p = 0.0255**), ploidy β = +0.007 (**p = 0.82**).
  The 0.026 reproduces; the 0.88 and the −0.0079 do not come from this model and presumably came from
  the main-effects model without the interaction. **Part of this follow-up is to replace those three
  numbers with scripted ones and correct the report wherever they appear.**
- Composition facts checked today without looking at any outcome: 17 rhabdomyosarcoma lines carry an
  aneuploidy score (7 embryonal, 8 alveolar, 1 pleomorphic, 1 unspecified); **3** of them have a PRISM
  bortezomib value and **10** have a CRISPR PSMB5 value. 366 scored models have both a PRISM
  bortezomib value and a CRISPR PSMB5 value.

## Data — unchanged

Same files, same score (`01_aneuploidy_score.py`), same lineage map (`lineage_map.tsv`), same
exclusions. DepMap 24Q4 and PRISM Repurposing 24Q2, public. No patient data.

## Analyses, fixed now — one script, `05_seguimiento.py`, run once

Direction convention, restated: PRISM LFC is more negative when more cells die, so **ρ < 0 means "more
aneuploid → more sensitive"**; CRISPR gene effect is more negative when the gene is more essential, so
**ρ < 0 means "more aneuploid → more dependent"**.

- **S1. Effect sizes with intervals.** For each of the seven locked drugs in the 444 solid PRISM lines,
  and for PSMB5 and the 20S-core mean in each CRISPR stratum: Spearman ρ with a **95% percentile
  bootstrap interval, 2,000 resamples, seed 20260908**. No new p-values; the FDR family stays the
  pre-registered one.
- **S2. The interaction as a coefficient.** OLS `gene_effect ~ score + haem + score×haem + ploidy` for
  PSMB5 (n = 946), reported as coefficients with analytic 95% CIs **and** bootstrap 95% CIs (same
  resampling). Also the main-effects model `gene_effect ~ score + haem + ploidy`, so that the three
  ad-hoc numbers in `RESULTADOS.md` are replaced by scripted ones. Standardised effect: the change in
  PSMB5 gene effect per 10 altered arms, in each stratum.
- **S3. Inside the solid stratum.** For every OncotreeLineage with **n ≥ 20** measured lines (the
  pre-registered power floor), ρ with bootstrap CI for (a) bortezomib LFC and (b) PSMB5 gene effect.
  Lineages with n < 20 are listed with n and ρ but marked *descriptive*, as the primary rule requires.
  One forest plot.
- **S4. Leave-one-lineage-out.** Recompute (a) the solid-stratum bortezomib ρ, (b) the solid-stratum
  PSMB5 ρ and (c) the interaction coefficient, dropping each solid lineage in turn. **Criterion, fixed
  now:** the pooled result is "driven by composition" if removing any single lineage changes the sign
  of (a) or (b), or moves the interaction's analytic 95% CI to include zero. Otherwise it is "not driven
  by any single lineage" — which is all that this test can say.
- **S5. Rhabdomyosarcoma.** The 17 scored RMS lines listed with subtype, score and ploidy; the 3 PRISM
  and 10 CRISPR values shown against the solid-stratum distribution (percentile of each). **No
  statistic is computed on 3 or 10 lines.** This is a named coverage limitation: the child's tumour
  type is essentially unrepresented in the drug screen.
- **S6. Assay overlap.** Among the 366 models with both measurements: ρ between bortezomib LFC and
  PSMB5 gene effect (do the two readouts agree with each other?), and ρ of each with the score in
  that shared set. The two analyses are **different modalities on overlapping models**, and will be
  described as such — never as independent replications.
- **S7. Sensitivity to the score definition, two alternatives fixed now, both reported:**
  (i) **fraction** = altered arms / callable arms; (ii) **ploidy-residualised** score = residual of the
  score on ploidy (linear) within the analysed set. Recompute S1 for bortezomib, carfilzomib and ixazomib
  and S2 for PSMB5 under each. No third definition is tried. Covariates are ploidy and stratum only.

## Predictions, on the record

- **P-S1.** The solid-stratum bortezomib interval includes zero (the null stays a null).
- **P-S2.** The analytic and bootstrap 95% CIs of the score×haem interaction both exclude zero. *If the
  bootstrap CI includes zero, the interaction is reported as fragile and the report's "significantly
  weaker in solid tumours" is downgraded to "weaker, with an interval that reaches zero".*
- **P-S3.** No single solid lineage's removal flips the sign of the solid-stratum PSMB5 ρ or moves the
  interaction CI across zero. *If one does, the report names that lineage and says the pooled result is
  driven by composition.*
- **P-S4.** Within solid lineages with n ≥ 20, the PSMB5 ρ intervals overlap zero in most of them; we
  do not predict which, and we will not single out a lineage that happens to reach significance as a
  finding.
- **P-S5.** Under both alternative score definitions the signs of the bortezomib, carfilzomib and
  ixazomib ρ and of the interaction are unchanged. *A sign change under either alternative is reported as
  a fragility of the primary result.*
- **No prediction is made for rhabdomyosarcoma.** It is a coverage statement.

## What each outcome forces us to write in §3.5

| Outcome | Sentence in the report |
|---|---|
| P-S2 and P-S3 hold | "The attenuation in solid lineages is not an artefact of any single lineage and its interval excludes zero; the solid-stratum association itself remains compatible with zero." |
| P-S2 fails | "The solid/haematological difference is suggestive, not established; its interval reaches zero." |
| P-S3 fails | "The pooled solid result depends on lineage composition; removing *X* changes it." |
| P-S5 fails | "The result depends on how aneuploidy is scored." |
| Any outcome | The RMS coverage limitation, the 366-model overlap, and the corrected interaction numbers. |

## Stopping rules and limits

- One script, one run, outputs `resultados_seguimiento.csv`, `resultados_seguimiento_lineajes.csv`,
  `fig5_seguimiento.png` and `RESULTADOS_SEGUIMIENTO.md`. No specification is added after seeing a
  number. A bug fix is allowed only if the script fails to run, and is recorded.
- Bootstrap intervals are descriptive uncertainty, not new hypothesis tests.
- Cancer cell lines remain cancer cell lines: nothing here speaks to constitutional MVA cells.

---
## Results

*(appended below, dated; the text above is never edited)*

### Results — 2026-09-08, 01:00 (script `05_seguimiento.py`, one analytical run; re-executed once for a figure axis label, numbers identical)

Full write-up: `RESULTADOS_SEGUIMIENTO.md`. Summary against the predictions:

| Prediction | Outcome |
|---|---|
| P-S1 bortezomib solid CI includes zero | **Confirmed** — ρ = −0.075, 95% CI −0.168 to +0.017 |
| P-S2 interaction CIs exclude zero | **Confirmed** — β = −0.01675, analytic −0.0314 to −0.0021, bootstrap −0.0322 to −0.0034 |
| P-S3 not driven by any single lineage | **Confirmed** — no sign flip in 26 leave-one-out fits; interaction CI never crosses zero (p 0.013–0.037) |
| P-S4 within-lineage intervals mostly overlap zero | All 27 do |
| P-S5 signs unchanged under both score definitions | **Confirmed** — but the ploidy-residualised score shrinks bortezomib/carfilzomib ρ from −0.075/−0.060 to −0.028/−0.028 |

Not predicted, reported: the solid-stratum PSMB5 bootstrap interval excludes zero narrowly (−0.149 to
−0.009) while the pre-registered FDR test did not pass (q = 0.118) — the pre-registered verdict stands.
The three ad-hoc numbers in `RESULTADOS.md` reproduce (main-effects model: β = −0.00786, p = 0.0098,
ploidy p = 0.875; full model: interaction p = 0.0255). Rhabdomyosarcoma: 17 scored lines, 3 with a PRISM
value — less killed than 98/91/89% of solid lines at 2.5 µM — and 10 with CRISPR, unremarkable. The two
assays agree with each other at ρ = −0.070 across 365 shared models.
