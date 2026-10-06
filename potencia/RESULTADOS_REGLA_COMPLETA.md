# Results — operating characteristics of the complete §6 advancement rule (post-submission addendum)

**Team ciberpty · run 2026-10-05, 21:09–21:12 EST**, per `PREREGISTRO_REGLA_COMPLETA.md` (commit
`646a364`) with `04_regla_completa.py` (commit `2cf6596`, before the run). One run, 142 s, on the
laptop's RTX 4060 (batched Levenberg–Marquardt in PyTorch); 4,000 simulated experiments per scenario,
seed 20261005. Raw output: `resultados_regla_completa.json`, `_regla_stdout.txt`.

**This analysis was run after the third and final Track 2 submission. The submitted PDF is unchanged;
this file and the dated addenda in `report/` are what the repository adds.**

## Headline

**The 0.80 power of the equal-EC50 test does not carry over to the rule as written.** At the design the
PDF proposes (f = 0.30, 4× within-cell selectivity, 12 cultures per arm, no true micronucleus increase)
the probability that an experiment ends in *advance* is **0.44**; 0.28 end as *insufficient response*
and 0.28 as *inconclusive*. No n in the searched set reaches 0.80: at n = 23 it is 0.62, and what grows
with n is not *advance* but *insufficient response* (0.36 at n = 23), because the mixture-table row
(1.50× at f = 0.30) sits **exactly at** the model's own expected bulk ratio — with a precise estimate,
about half of the intervals fall wholly below the row. The threshold the PDF reads off the table is a
coin flip against its own model, which is the defect the judge round named and we did not test before
submitting.

## Fitter acceptance test (run first)

500 simulated curves, GPU fit versus `scipy.optimize.curve_fit`: **99.2 %** within |Δ log10 EC50| ≤ 0.02
(threshold 98 %), identical failure flags on **100 %** (threshold 95 %), no failures by either fitter,
maximum absolute difference 0.039. Passed; no CPU fallback was used.

## The grid at f = 0.30, δ = 0 (frequencies over 4,000 experiments)

| n per arm | r = 1 (null) advance / insufficient / inconclusive | r = 2 | r = 4 |
|---|---|---|---|
| 3 | **0.001** / 0.36 / 0.64 | 0.006 / 0.22 / 0.77 | **0.01** / 0.09 / 0.90 |
| 6 | **0.015** / 0.67 / 0.32 | 0.045 / 0.42 / 0.54 | **0.13** / 0.17 / 0.70 |
| 12 | **0.046** / 0.85 / 0.10 | 0.20 / 0.59 / 0.21 | **0.46** / 0.27 / 0.28 |
| 23 | **0.070** / 0.93 / 0.004 | 0.28 / 0.71 / 0.009 | **0.62** / 0.37 / 0.007 |

*Harm* and *toxicity stop* were 0.000–0.003 throughout the δ = 0 scenarios (no true micronucleus
increase, no cross-line toxicity in the model).

## Sweeps from the central scenario (n = 12, r = 4, δ = 0 unless varied)

| Scenario | advance | insufficient | inconclusive | harm |
|---|---|---|---|---|
| f = 0.10 (ρ = 1.14) | 0.11 | 0.25 | 0.64 | 0 |
| f = 0.20 (ρ = 1.30) | 0.27 | 0.25 | 0.49 | 0 |
| f = 0.30 (ρ = 1.50) | 0.47 | 0.27 | 0.26 | 0 |
| f = 0.50 (ρ = 2.00) | 0.60 | 0.28 | 0.13 | 0 |
| δ = 0.25 (true micronucleus increase below the margin) | 0.08 | 0.27 | 0.65 | 0 |
| δ = 0.50 (true increase exactly at the margin) | 0.002 | 0.27 | 0.72 | 0.003 |
| δ = 1.00 (true increase at twice the margin) | 0.000 | 0.12 | 0.31 | **0.57** |

## Predictions

| | Pre-registered | Outcome |
|---|---|---|
| P-R1 | central *advance* < 0.80 and < 0.60 | **Confirmed** — 0.44 |
| P-R2 | null false-advance ≤ 0.05 at every n; dominant outcome not *harm* | **Falsified on the first half** — 0.046 at n = 12 but **0.070 at n = 23** (0.001 at n = 3, 0.015 at n = 6); the second half holds (*insufficient* dominates the null) |
| P-R3 | δ = 0.5: *advance* < 0.20, *inconclusive* dominant | **Confirmed** — 0.002 and 0.72 |
| P-R4 | no n reaches 0.80 *advance* at f = 0.30, r = 4 | **Confirmed** — 0.62 at n = 23 |
| P-R5 | f = 0.10: *insufficient* > *advance* | **Confirmed** — 0.25 vs 0.11 |

**Why P-R2 fails, and why it matters.** The two donor comparisons share the patient arm. A patient arm
whose cultures happen to fit low drives *both* ratios up at once, so requiring "both donors" does not
give the protection two independent tests would, and the false-advance rate grows with precision
(0.07 at n = 23) rather than staying at the nominal level. The aggregation the PDF left open — and we
fixed as "both donors, no further adjustment" — is not enough on its own; a joint test on the pooled
control arm with a donor random effect, or a Bonferroni-type bound, would need to be pre-registered
before any real experiment.

## What this forces us to write (per the pre-registered mapping)

- P-R1 holds → the §6 addendum says: *"The equal-EC50 power of 0.80 at n = 12 does not carry over to
  the complete rule: the probability of advance at the proposed design is 0.44, and no n in the searched
  set reaches 0.80; the design as submitted is a pilot for estimating operating characteristics, not a
  decisive experiment."*
- P-R2 fails → *"The rule as written admits false advancement at rate 0.07 under the null at n = 23
  (0.05 at n = 12); the two-donor aggregation must be replaced by a joint test before use."*
- Any outcome → the tables above are the record; nothing in the submitted PDF is edited.

## What this does not establish

The model is the pre-registered one, not the child's cells: f is treated as measured without error, the
4× selectivity is the scenario the dose–response analysis already found unsupported, the micronucleus
vehicle rate (20 per 1,000) and its dispersion are design values, and the three variance components
(donor, passage, culture) are assumptions. A rule can only be as good as the threshold it reads: the
mixture-table row is the expected value under the model, so an experiment whose truth is exactly that
value cannot clear it reliably at any n. That is a property of the rule, now measured, and the reason
the next design should state a minimum effect *below* the model's expectation or replace the bulk-EC50
criterion with a per-cell endpoint, as §6 already proposes for f < 0.20.

Compute: 142 s on one consumer GPU (CUDA), after the owner's instruction to use it; no patient data.
