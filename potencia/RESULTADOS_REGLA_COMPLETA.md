# Results — operating characteristics of the complete §6 advancement rule (post-submission addendum)

**Team ciberpty · primary run 2026-10-05, 21:09–21:12 EST**, per `PREREGISTRO_REGLA_COMPLETA.md` (commit
`646a364`) with `04_regla_completa.py` (commit `2cf6596`, before the run). One run, 142.0 s, on the
laptop's RTX 4060 (batched Levenberg–Marquardt in PyTorch); 4,000 simulated experiments per scenario,
seed 20261005. Raw output: `resultados_regla_completa.json` (every frequency, unrounded), `_regla_stdout.txt`.
**Exploratory post-hoc checks** (not pre-registered; run after an adversarial read of the first version of
this file, `evidencia/codex_lectura_regla_completa_2026-10-05.md`): `05_regla_exploratorio.py`,
`resultados_regla_exploratorio.json`, 82.3 s. The first version of this file is in git history
(commit `a3848c6`); the claims it got wrong are listed at the end.

**This analysis was run after the third and final Track 2 submission. The submitted PDF is unchanged;
this file and the dated addenda in `report/` are what the repository adds.**

## Headline

**The 0.80 power of the equal-EC50 test does not carry over to the rule as written.** At the design the
PDF proposes (f = 0.30, 4× within-cell selectivity, 12 cultures per arm, no true micronucleus increase)
the probability that an experiment ends in *advance* is **0.442**; 0.281 end as
*insufficient response* and 0.276 as *inconclusive*. No n in {3, 6, 12, 23} reaches 0.80:
*advance* rises with n (0.012 → 0.127 → 0.459 → 0.622) and so does
*insufficient response* (0.089 → 0.371), while *inconclusive* collapses. The reason is in
check D below: under the fitted-EC50 estimand the model's own expected donor/patient ratio at the
central scenario is **1.469** (noiseless half-viability ratio 1.488), slightly *below* the
mixture-table row of 1.50 that the PDF reads as the threshold. A rule whose threshold sits at or above
the expected effect converges, as precision grows, to *insufficient*, not to *advance*: the row was
derived from the simple mixture formula and is not reachable on average by the four-parameter fit the
design uses. This is the defect the judge round named and we did not test before submitting.

## Fitter acceptance test (run first)

500 simulated curves, GPU fit versus `scipy.optimize.curve_fit`: **99.2 %** within |Δ log10 EC50| ≤ 0.02
(threshold 98 %), identical failure flags on **100 %** (threshold 95 %), no failures by either fitter,
maximum absolute difference 0.039. Passed; no CPU fallback was used (and none is implemented —
see deviations).

## The grid at f = 0.30, δ = 0 (frequencies over 4,000 experiments; all from the grid runs)

| n per arm | r = 1 (null): advance / insufficient / inconclusive | r = 2 | r = 4 |
|---|---|---|---|
| 3 | **0.001** / 0.358 / 0.641 | 0.006 / 0.223 / 0.771 | **0.012** / 0.089 / 0.895 |
| 6 | **0.015** / 0.665 / 0.321 | 0.045 / 0.415 / 0.539 | **0.127** / 0.174 / 0.698 |
| 12 | **0.046** / 0.852 / 0.102 | 0.200 / 0.594 / 0.206 | **0.459** / 0.266 / 0.276 |
| 23 | **0.070** / 0.927 / 0.004 | 0.280 / 0.712 / 0.009 | **0.622** / 0.371 / 0.007 |

*Harm* and *toxicity stop* were ≤ 0.003 in every δ = 0 scenario; the full table below has every value.

## All scenarios (five outcomes per scenario, plus the missing-EC50 rate)

| scenario | f | r | n | δ | advance | insufficient | inconclusive | harm | toxicity stop | missing EC50 |
|---|---|---|---|---|---|---|---|---|---|---|
| `central` | 0.3 | 4 | 12 | 0.0 | 0.442 | 0.281 | 0.276 | 0.000 | 0.000 | 0.000 |
| `sweep:n=3` | 0.3 | 4 | 3 | 0.0 | 0.010 | 0.088 | 0.900 | 0.000 | 0.002 | 0.000 |
| `sweep:n=6` | 0.3 | 4 | 6 | 0.0 | 0.118 | 0.183 | 0.698 | 0.000 | 0.001 | 0.000 |
| `sweep:n=12` | 0.3 | 4 | 12 | 0.0 | 0.466 | 0.261 | 0.274 | 0.000 | 0.000 | 0.000 |
| `sweep:n=23` | 0.3 | 4 | 23 | 0.0 | 0.635 | 0.356 | 0.009 | 0.000 | 0.000 | 0.000 |
| `sweep:f=0.1` | 0.1 | 4 | 12 | 0.0 | 0.112 | 0.252 | 0.635 | 0.000 | 0.000 | 0.000 |
| `sweep:f=0.2` | 0.2 | 4 | 12 | 0.0 | 0.269 | 0.246 | 0.485 | 0.000 | 0.000 | 0.000 |
| `sweep:f=0.3` | 0.3 | 4 | 12 | 0.0 | 0.467 | 0.270 | 0.263 | 0.000 | 0.000 | 0.000 |
| `sweep:f=0.5` | 0.5 | 4 | 12 | 0.0 | 0.596 | 0.278 | 0.126 | 0.000 | 0.000 | 0.000 |
| `sweep:r=1.0` | 0.3 | 1 | 12 | 0.0 | 0.040 | 0.858 | 0.102 | 0.000 | 0.000 | 0.000 |
| `sweep:r=2.0` | 0.3 | 2 | 12 | 0.0 | 0.202 | 0.576 | 0.222 | 0.000 | 0.000 | 0.000 |
| `sweep:r=4.0` | 0.3 | 4 | 12 | 0.0 | 0.446 | 0.281 | 0.273 | 0.000 | 0.000 | 0.000 |
| `sweep:delta=0.0` | 0.3 | 4 | 12 | 0.0 | 0.450 | 0.270 | 0.281 | 0.000 | 0.000 | 0.000 |
| `sweep:delta=0.25` | 0.3 | 4 | 12 | 0.25 | 0.079 | 0.268 | 0.653 | 0.000 | 0.000 | 0.000 |
| `sweep:delta=0.5` | 0.3 | 4 | 12 | 0.5 | 0.002 | 0.273 | 0.722 | 0.003 | 0.000 | 0.000 |
| `sweep:delta=1.0` | 0.3 | 4 | 12 | 1.0 | 0.000 | 0.121 | 0.314 | 0.565 | 0.000 | 0.000 |
| `grid:n=3:r=1.0` | 0.3 | 1 | 3 | 0.0 | 0.001 | 0.358 | 0.641 | 0.000 | 0.000 | 0.000 |
| `grid:n=3:r=2.0` | 0.3 | 2 | 3 | 0.0 | 0.006 | 0.223 | 0.771 | 0.000 | 0.000 | 0.000 |
| `grid:n=3:r=4.0` | 0.3 | 4 | 3 | 0.0 | 0.012 | 0.089 | 0.895 | 0.000 | 0.003 | 0.000 |
| `grid:n=6:r=1.0` | 0.3 | 1 | 6 | 0.0 | 0.015 | 0.665 | 0.321 | 0.000 | 0.000 | 0.000 |
| `grid:n=6:r=2.0` | 0.3 | 2 | 6 | 0.0 | 0.045 | 0.415 | 0.539 | 0.000 | 0.000 | 0.000 |
| `grid:n=6:r=4.0` | 0.3 | 4 | 6 | 0.0 | 0.127 | 0.174 | 0.698 | 0.000 | 0.000 | 0.000 |
| `grid:n=12:r=1.0` | 0.3 | 1 | 12 | 0.0 | 0.046 | 0.852 | 0.102 | 0.000 | 0.000 | 0.000 |
| `grid:n=12:r=2.0` | 0.3 | 2 | 12 | 0.0 | 0.200 | 0.594 | 0.206 | 0.000 | 0.000 | 0.000 |
| `grid:n=12:r=4.0` | 0.3 | 4 | 12 | 0.0 | 0.459 | 0.266 | 0.276 | 0.000 | 0.000 | 0.000 |
| `grid:n=23:r=1.0` | 0.3 | 1 | 23 | 0.0 | 0.070 | 0.927 | 0.004 | 0.000 | 0.000 | 0.000 |
| `grid:n=23:r=2.0` | 0.3 | 2 | 23 | 0.0 | 0.280 | 0.712 | 0.009 | 0.000 | 0.000 | 0.000 |
| `grid:n=23:r=4.0` | 0.3 | 4 | 23 | 0.0 | 0.622 | 0.371 | 0.007 | 0.000 | 0.000 | 0.000 |

## Predictions

| | Pre-registered | Outcome |
|---|---|---|
| P-R1 | central *advance* < 0.80 and < 0.60 | **Confirmed** — 0.442 |
| P-R2 | null false-advance ≤ 0.05 at every n; dominant outcome not *harm* | **First clause falsified** — 0.001, 0.015, 0.046, **0.070** at n = 3, 6, 12, 23; second clause holds (*insufficient* or *inconclusive* dominate: at n = 3 *inconclusive* 0.641 > *insufficient* 0.358; the script's automated check only tested "not harm", weaker than the clause) |
| P-R3 | δ = 0.5: *advance* < 0.20, *inconclusive* dominant | **Confirmed** — 0.002 and 0.722 |
| P-R4 | no n reaches 0.80 *advance* at f = 0.30, r = 4 | **Confirmed** — 0.622 at n = 23 |
| P-R5 | f = 0.10: *insufficient* > *advance* for every n | **Confirmed at n = 12 only** (0.252 vs 0.112), the only n the pre-registered design simulated at f = 0.10; the "every n" clause was not testable by that design. Exploratory check C (below) finds it holds at n = 3, 6 and 23 as well — reported as exploratory, not as a pre-registered confirmation |

## Why P-R2 failed — tested, not asserted

The first version of this file blamed the two donor comparisons sharing the patient arm. That cannot be
the mechanism: the intersection of two events each of probability ≤ 0.05 is ≤ 0.05 whatever their
dependence. **Exploratory check B** removes the donor-level variance component (CV_donor = 0) and
leaves everything else: the null false-advance rate falls to 0.001, 0.002, 0.005, 0.002
at n = 3, 6, 12, 23. The inflation is therefore the **donor effect**: each line carries a persistent
random shift that the Welch test — which treats cultures as the independent unit — never sees, so the
interval narrows with n while the between-line difference does not, and the per-comparison error grows
with precision. Multiplicity is not the problem; the unit of inference is. Any real experiment needs a
donor-level random effect (or more control donors) in the analysis, pre-registered before the data.
The pre-registered mapping's sentence stands as written: **the rule as written admits false advancement
above the nominal level under the null (0.070 at n = 23); the threshold — here, the test itself —
must be tightened before use.**

## Exploratory checks (post-hoc, after the adversarial read; not pre-registered)

| Check | Result |
|---|---|
| **A** — micronucleus interval on the *paired* per-culture contrast D_i = T_i − 1.5·V_i (vehicle and treated share the culture multiplier, so the primary's independent-sample interval is too wide) | *advance* at r = 4: 0.024, 0.210, **0.527**, 0.632 at n = 3, 6, 12, 23 (primary: 0.012, 0.127, 0.459, 0.622); null false-advance 0.003, 0.015, 0.054, 0.063. The primary is conservative on the micronucleus side; the conclusion (no n reaches 0.80) does not change |
| **B** — null with CV_donor = 0 | false-advance 0.001, 0.002, 0.005, 0.002: the inflation is the donor effect |
| **C** — f = 0.10 at n = 3, 6, 23 | *insufficient* / *advance*: 0.084 / 0.003; 0.163 / 0.028; 0.348 / 0.227 — P-R5's clause holds at every n tested |
| **D** — effective true ratio, central scenario, n = 23 | mean log10(donor − patient) over fitted EC50s = 0.1671 → ratio **1.469** (SD across experiments 0.082); 54 % of experiments have a point estimate below the 1.50 row; noiseless half-viability ratio of the mixture 1.488 (107.5 vs 160 nM) |

## Deviations and limitations (from the adversarial read; all accepted)

- **Missing-fit precedence.** The pre-registration says any missing EC50 makes the experiment
  *inconclusive*; the code applies *harm* first, so a missing-fit experiment with a harm interval would
  be labelled *harm*. No simulated experiment had a missing EC50 (rate 0.000 everywhere), so no outcome
  was affected. Protocol mismatch, recorded.
- **No convergence criterion in the GPU fitter**: 80 LM iterations, interior finite fits accepted. The
  acceptance test (above) is the only evidence of agreement with the CPU fitter; it does not establish
  convergence for every curve. EC50-at-bound tolerance is 1e-3 (GPU) against 1e-6 (CPU).
- **No CPU fallback is implemented**; the script stops if the acceptance test fails. Unexercised.
- Acceptance agreement is computed among jointly finite fits; with zero failures this equals all 500.
- The variance components are used as **log-scale SDs**; the implied CV of a log-normal multiplier is
  √(e^σ² − 1), i.e. 0.202 for σ = 0.20 — stated for exactness.
- **The micronucleus interval of the primary run ignores the vehicle/treated covariance** of the generated
  data (shared culture multiplier); it is conservative. Check A gives the paired version.
- **Only the patient line decides the micronucleus criterion** — our reading of the PDF's "treated versus
  vehicle cultures of the same line"; the pre-registration did not say it explicitly.
- f is treated as measured without error; the 4× selectivity, the vehicle rate (20 per 1,000) and the
  three variance components are design values, not measurements. Nothing here is about the child's cells.

## What the first version of this file got wrong (corrected above; the old text is in commit `a3848c6`)

"What grows with n is not *advance* but *insufficient response*" (both grow); "the row sits exactly at the
model's expected ratio … about half of the intervals fall wholly below it" (the row sits *above* the
fitted-estimand expectation, 1.469 vs 1.50, and the rule tests the upper bound, not the point estimate);
the n = 23 sentence mixed the grid and the n-sweep realizations; P-R5 was reported as confirmed "for every
n" when only n = 12 had been simulated; and the shared-patient-arm explanation of P-R2 was wrong, as check
B shows.

## What this forces us to write (per the pre-registered mapping)

- P-R1 holds → §6 addendum: *the equal-EC50 power of 0.80 at n = 12 does not carry over to the complete
  rule; the probability of advance at the proposed design is 0.44 and no n in the searched set reaches
  0.80; the design as submitted is a pilot for estimating operating characteristics, not a decisive
  experiment.*
- P-R2 fails → *the rule as written admits false advancement at rate 0.07 under the null at n = 23
  (0.046 at n = 12); the test must account for the donor level before use.*
- Any outcome → the tables above are the record; nothing in the submitted PDF is edited.

Compute: 142.0 s + 82.3 s on one consumer GPU (CUDA), after the owner's instruction to use it; no patient data.
