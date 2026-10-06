# Pre-registration — operating characteristics of the COMPLETE §6 advancement rule

**Team ciberpty · MVA Hackathon 2026 · written and committed 2026-10-05, after the third and final Track 2
submission, BEFORE `04_regla_completa.py` exists or runs.** This is a post-submission addendum: the
submitted PDF is fixed; this analysis lives in the repository, which the submission links and which is
made public at the start of the final evaluation. Results are appended below the line, dated. Nothing
above the line is edited afterwards.

## Why this exists

Every judge round since 5 October made the same objection: the power figures in §6 (0.167 at n = 3;
about 12 cultures per arm at f = 0.30, 23 at f = 0.20) cover **rejection of equal EC50s only**, not the
complete advancement rule — two control donors, the mixture-table threshold, the ≤ 312 nM condition,
the micronucleus margin and the constitutional-toxicity stop signal. "Detecting a nonzero EC50
difference with 80% power does not give 80% probability of clearing a minimum-effect threshold." We
did not run this before the submission; we run it now, under the rule exactly as the submitted PDF
states it, and we accept whatever it returns. **It cannot improve the submitted score; it can only
make the repository honest about what the design can decide.**

## What already exists (so nothing here is a blind test)

`RESULTADOS_4P.md`: four-parameter Hill fit, shared biological multiplier per culture (CV_bio 0.20),
plate offset (CV 0.05), per-well noise (CV 0.10), grid 0–1,000 nM (11 points), Welch t on log10 EC50:
power 0.167 at the central scenario (f = 0.30, EC50_aneu = 40 nM, r = 4, n = 3), 0.80 first reached at
n = 12 (f = 0.30) and 23 (f = 0.20). `RESULTADOS_2_DOSIS.md`: the 4× selectivity has no empirical
support for a one-chromosome cell. The submitted §6 rule (Part II, "Advancement criteria") is quoted
in the model section below; the code implements it as written, with the choices the PDF left open
fixed here, before the run.

## Model, fixed now (unchanged where the 4P follow-up already fixed it)

- **Truth per culture**: viability(c) = (1 − f)·Hill(c; r·E, m) + f·Hill(c; E, m) for the patient line;
  Hill(c; r·E, m) for each control donor; E = 40 nM, m = 1. Concentrations 0, 5, 10, 25, 50, 75, 100,
  200, 400, 700, 1,000 nM.
- **Variance components**, log-normal multipliers on EC50: **donor level** (CV_donor 0.15, one draw
  per line per experiment — the patient line and each control donor have their own biology),
  **passage level** (CV_pass 0.10; cultures are grouped into passages of 3 — n = 3 is one passage,
  n = 12 is four — so cultures from the same passage are correlated, which is the dependence the PDF
  says will be "modelled, not assumed away"), **culture level** (CV_bio 0.20, as before), plate offset
  on viability (CV 0.05), per-well noise (CV 0.10).
- **Fit**: the four-parameter Hill (bottom, top, log10 EC50, slope) per culture, same bounds and start
  values as `03_potencia_4p.py`; failure rules unchanged (non-convergence, EC50 at a bound, top <
  bottom + 0.2 → that culture's EC50 is missing; an experiment with any missing EC50 in an arm is
  **inconclusive**, never a non-rejection in disguise).
- **Fitter on GPU**: a batched Levenberg–Marquardt in PyTorch on CUDA, fitting all curves of a
  scenario at once (the owner's instruction: use the GPU, it is free). Acceptance test, run first and
  reported: on 500 simulated curves the GPU fit must agree with `scipy.optimize.curve_fit` (the CPU
  fitter of the 4P follow-up) to **|Δ log10 EC50| ≤ 0.02 in at least 98% of curves**, with the same
  failure flags on ≥ 95%. If it does not pass, the run falls back to the CPU fitter in a
  multiprocessing pool and says so; results are not compared across fitters after the fact.

## The rule, as the submitted PDF states it, with the open choices fixed here

Per simulated experiment, with n cultures per arm (patient, control donor A, control donor B):

1. **Response** (criterion 1). For each control donor j, the log10 EC50 ratio donor_j − patient with a
   Welch 95% interval. Let ρ(f) be the mixture-table row at the measured f (1.14, 1.30, 1.50, 2.00 for
   f = 0.10, 0.20, 0.30, 0.50; f is treated as measured without error in this simulation, stated as a
   limitation). *Response met* if, for **both** donors, the interval excludes 0 (ratio 1) and the
   interval is not wholly below log10 ρ(f). *Insufficient response* if, for **either** donor, the
   interval lies wholly below log10 ρ(f). Otherwise *response inconclusive*. The two donors enter
   separately and advancement needs both (the aggregation the PDF left to be fixed: fixed here as
   "both"; no multiplicity adjustment beyond requiring both, stated as such).
2. **Exposure condition** (criterion 2): the patient's pooled EC50 point estimate (geometric mean) is
   ≤ 312 nM.
3. **Micronucleus margin** (criterion 3): per culture, micronuclei per 1,000 binucleated cells in
   vehicle and in treated (at the 100 nM condition, one count per culture). Counts are Poisson with a
   culture-level gamma multiplier (CV 0.25) and the passage correlation above; vehicle rate λ0 = 20
   per 1,000 (a design value, not a measurement), treated rate λ0·(1 + δ). Δ = treated mean − vehicle
   mean, M = 0.5·vehicle mean, and the 95% upper/lower bounds of Δ − M = T − 1.5·V by the delta
   method with Welch degrees of freedom. *Below margin* if the upper bound < 0; *harm* if the lower
   bound > 0; otherwise *inconclusive*.
4. **Toxicity stop** (criterion 4, "markedly more sensitive than both control donors"): fixed here as
   both donor ratios' point estimates exceeding **2 × ρ(f)**, the reading the PDF gives ("a shift more
   than twice the row's prediction").

**Classification, in order of precedence** (the PDF's four outcomes, with harm first):
*harm* (criterion 3 lower bound > 0) › *toxicity stop* (criterion 4) › *advance* (response met, exposure
met, micronucleus below margin) › *insufficient response* › *inconclusive* (everything else, including
any missing EC50). We report all five frequencies; "blocked" = 1 − advance.

## Scenarios, fixed now

- Central: f = 0.30, r = 4, n = 12, δ = 0 (no true micronucleus increase) — the design the PDF proposes.
- Sweeps, one factor at a time from the central: n ∈ {3, 6, 12, 23}; f ∈ {0.10, 0.20, 0.30, 0.50};
  r ∈ {1, 2, 4} (r = 1 is the **null**: false-advancement rate); δ ∈ {0, 0.25, 0.5, 1.0} (δ = 0.5 is a
  true increase exactly at the margin).
- The full n × r grid at f = 0.30, δ = 0: n ∈ {3, 6, 12, 23} × r ∈ {1, 2, 4}.
- 4,000 simulated experiments per scenario; seed 20261005; one random stream per scenario (seed +
  scenario index), as in the 4P follow-up.

## Predictions, on the record

- **P-R1.** At the central scenario the probability of *advance* is **below 0.80** — the 0.80 of the
  equal-EC50 test does not transfer to the complete rule — and below 0.60.
- **P-R2.** Under the null (r = 1) the false-advancement rate is **≤ 0.05** at every n, and the
  dominant outcome is *insufficient response* or *inconclusive*, not *harm*.
- **P-R3.** With a true micronucleus increase at the margin (δ = 0.5) the *advance* probability at the
  central n falls below **0.20**, with *inconclusive* the dominant outcome (the margin test cannot
  resolve an effect exactly at the margin).
- **P-R4.** No n in the searched set reaches 0.80 *advance* at f = 0.30 and r = 4 with δ = 0;
  n = 23 stays below 0.80.
- **P-R5.** At f = 0.10 (ρ = 1.14) the *insufficient response* frequency exceeds the *advance*
  frequency even at r = 4, for every n — the per-cell endpoint, not bulk viability, is the right
  design there (as §6 already says for f < 0.20).

## What each outcome forces us to write (repository only; the PDF is fixed)

| Outcome | Sentence for `REPORT_track2_EN.md` §6 (dated addendum) and the README |
|---|---|
| P-R1 holds | "The equal-EC50 power of 0.80 at n = 12 does **not** carry over to the complete rule: the probability of *advance* at the proposed design is X; the design as submitted is a pilot for estimating operating characteristics, not a decisive experiment." |
| P-R1 fails | "The complete rule reaches X at n = 12; the submitted power figure was conservative." |
| P-R2 fails (false advance > 0.05) | "The rule as written admits false advancement at rate X under the null; the threshold must be tightened before use." |
| Any outcome | The five frequencies per scenario go into a table in the repository, with the fitter acceptance test, and nothing in the submitted PDF is edited. |

## Stopping rules

One script, one run. A bug fix is allowed only if the script fails to execute or the fitter
acceptance test fails, and is recorded as an amendment. No scenario, threshold or classification is
added or changed after seeing a number. This measures the statistical behaviour of a rule under a
declared model; it measures nothing about the child's cells.

---
## Results

*(appended below, dated; the text above is never edited)*

### Results — 2026-10-05, 21:09–21:12 EST (`04_regla_completa.py`, commit `2cf6596`, one GPU run, 142 s)

Full write-up: `RESULTADOS_REGLA_COMPLETA.md`. Fitter acceptance test passed (99.2 % within 0.02;
identical failure flags). Central *advance* **0.44** (P-R1 confirmed); no n reaches 0.80 (P-R4
confirmed; 0.62 at n = 23); δ = 0.5 gives *advance* 0.002 with *inconclusive* 0.72 (P-R3 confirmed);
f = 0.10 gives *insufficient* 0.25 > *advance* 0.11 (P-R5 confirmed). **P-R2 falsified in part:** the
false-advance rate under the null is 0.046 at n = 12 but **0.070 at n = 23**, because the two donor
comparisons share the patient arm; the "both donors" aggregation fixed above is not a sufficient
multiplicity control. Both sentences of the pre-registered mapping go into the `report/` addenda.
