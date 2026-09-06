# A 4× selectivity has no empirical support for a cell carrying one extra chromosome

**Team: ciberpty** · 2026-09-01 · Pre-registered in `potencia/PREREGISTRO_2_DOSIS.md`, committed as
`45c4ed7` **before** this ran. This analysis was designed to attack our own result from the same day.

> **Clarification of 2026-09-06 (§3).** The first version of §3 read the pre-registered magnitude rule
> onto the haematological stratum and concluded that the 4× scenario was "not defensible" as a
> pre-committed consequence. The rule was written for **solid** lines, and there the exercise is
> uninformative. The corrected reading is in §3; the title of this file was changed with it. The
> pre-registration itself has not been edited.

---

## 1. The pre-committed outcome, applied

The pre-registration fixed the decision on the **solid** stratum, because that is the lineage relevant
to this child. The rule that fires is the falsification clause:

> **The slope does not differ from zero in solid lines**, so this analysis cannot constrain the
> selectivity. It is reported as **uninformative** for that stratum, not as evidence of a small
> effect.

| Solid lines (n = 833) | |
|---|---|
| Slope of PSMB5 dependency per altered arm | **−0.0056** |
| 95% confidence interval | **[−0.0118, +0.0006]** — covers zero |
| p | 0.076 |

That is the outcome we said was likely: our own DepMap package had already found PSMB5 dependency
non-significant in solid lines (ρ = −0.077, q = 0.118). We pre-committed to reporting it as a null and
we are doing so.

## 2. The secondary stratum is informative, and it goes against this morning's result

The pre-registration set no decision rule for the haematological stratum, so **everything in this
section is secondary and is labelled as such.** It is reported because it is the only place where the
dependency exists at all, and therefore the only place the question can be asked.

| Haematological lines (n = 113) | |
|---|---|
| Slope per altered arm | **−0.0284** |
| 95% confidence interval | **[−0.0499, −0.0068]** — excludes zero |
| p | **0.010** |
| Residual SD of PSMB5 effect | 0.607 |
| Predicted change at **2 arms** (one chromosome — the MVA cell) | −0.057 = **0.09 residual SD** |
| Predicted change at **18 arms** (a highly aneuploid line) | −0.510 = **0.84 residual SD** |

**Where the dependency is real, it is carried by the high end of the range.** One whole chromosome
moves PSMB5 dependency by about a tenth of a standard deviation; eighteen altered arms move it by
most of one. The relationship is not a switch that flips when a cell becomes aneuploid — it is a dose,
and an MVA cell sits at the flat end of it.

**Robustness without the linear model (post-hoc, not pre-registered).** Comparing lines directly
rather than fitting a slope gives the same picture, so the conclusion does not depend on assuming
linearity:

| Stratum | ≤ 4 arms | ≥ 16 arms | Cohen's d | p (Mann–Whitney) |
|---|---|---|---|---|
| Solid | −1.751 (n = 57) | −1.810 (n = 603) | 0.10 | 0.30 |
| Haematological | −0.779 (n = 41) | −1.175 (n = 28) | **0.63** | **0.005** |

The quadratic term is not significant in either stratum (p = 0.20 and p = 0.92), so we have no
evidence of curvature — which is not the same as evidence of linearity, as the pre-registration said.

## 3. What this does to this morning's power result

`potencia/RESULTADOS.md` centred its power calculation on a **4× EC50 selectivity**, taken from
Ippolito's < 40 nM in **highly aneuploid** cancer lines. This analysis says that number is measured at
the far end of a dose relationship from where MVA cells sit.

**Correction of 2026-09-06: the pre-registered magnitude rule did not fire, and we withdraw the claim
that it did.** §4 of `PREREGISTRO_2_DOSIS.md` defines Δ₂ and σ explicitly **in solid lines**, "the
stratum relevant to this child". In solid lines the slope's 95% interval covers zero
(`dosis.json`: −0.0118 … +0.0006, p = 0.076), so the falsification clause is what applies and the
exercise is **uninformative for the stratum the rule was written about**. The 0.093 is the
**haematological** ratio (`dosis.json`, `ratio_2` = 0.0935), and the pre-registration set no decision
rule for that stratum. An earlier version of this section applied the < 0.10 threshold to it and
reported "the 4× central scenario is not defensible" as a pre-committed consequence. That transferred
a rule to a different stratum after seeing the result, which is the failure mode this whole
pre-registration exists to prevent. It is withdrawn.

What survives the correction, stated at the strength the data support:

> **The 4× selectivity has no empirical support in these cells, and it never had any.** It is an
> assumption imported from highly aneuploid cancer lines, and this analysis gives an independent
> reason to doubt it: where the dependency exists at all, two altered arms move it 0.09 residual SD
> against 0.84 at eighteen. That is descriptive, secondary and outside the pre-registered decision.
>
> **The 4× has equally not been refuted as an EC50 ratio.** The stratum where the rule could have
> fired returned a null, and CRISPR gene effect does not convert to EC50 in any case. "Unsupported"
> and "refuted" are different states and we report the first.
>
> What replaces it is not a smaller number. It is a **conditional design**: the selectivity is an
> unknown the experiment measures, the assay is powered at an assumed 4× (0.897) and underpowered at
> an assumed 2× (0.387), and the advancement threshold is read off the measured aneuploid fraction
> rather than assumed. `potencia/RESULTADOS.md` and Track 2 §6 are worded that way.

**We are not converting this into an EC50 ratio, and the pre-registration said we would not.** CRISPR
gene effect is complete permanent loss; a drug is partial reversible inhibition. There is no
calibration that licenses the conversion. What transfers is the *shape* of the argument — the
dependency is graded and MVA cells are at the low end — not a number for *r*.

## 4. Why this makes the §6 gate more important, not less

This morning's gate measured the **cell fraction**. This analysis says the **per-cell burden** matters
too, and in the same direction: an MVA fibroblast culture is a small fraction of cells each carrying a
small perturbation. Both terms push the expected effect down.

The gating measurement should therefore record **both**: the proportion of cells with at least one
numerical abnormality *and* the number of abnormal chromosomes per abnormal cell. A standard metaphase
count returns both from the same slides at no extra cost.

**A correction to how we described that gate.** `potencia/RESULTADOS.md` §3 said metaphase counting
"with premature chromatid separation scoring" measures the aneuploid fraction directly. **PCS and
aneuploidy are different endpoints** — PCS is the cytogenetic hallmark used to diagnose MVA, not a
count of cells with an abnormal chromosome number. The protocol must count **cells with ≥ 1 numerical
chromosome abnormality**; PCS scoring is a useful companion, not the measurement the model needs.

## 5. Limits

- **Solid lines gave a null**, and that is the lineage of this child's tumour. The informative
  estimate comes from haematological lines, which is the stratum our own DepMap result says behaves
  differently. Using it to reason about a solid-lineage question is exactly the extrapolation we
  criticised in §3.5 of the report; here it is used only to bound an *effect size*, and it is the
  conservative direction.
- **Two arms is the low edge of the observed range**: only 4.7% of solid lines and 18.6% of
  haematological lines carry ≤ 2 altered arms. The estimate there is an extrapolation from a
  regression dominated by the middle of the range.
- **Arms are counted, not identified.** Two arms of chromosome 21 are not two arms of chromosome 1.
- **Cancer lines are not constitutional fibroblasts**, the same open extrapolation the whole Track 2
  argument rests on.

## 6. Reproduce

    potencia/PREREGISTRO_2_DOSIS.md   design, committed as 45c4ed7 before the run
    potencia/02_dosis.py              regression, curvature check and the post-hoc contrast
    potencia/dosis.json               every number
    depmap/psmb5_merged.csv           input, from the pre-registered DepMap package

CPU only, no patient data, no new download.
