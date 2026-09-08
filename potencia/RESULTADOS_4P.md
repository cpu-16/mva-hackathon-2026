# Results — the four-parameter fit with biological variability (pre-registered follow-up)

**Team ciberpty · run 2026-09-08, 00:23–00:29 EST**, per `PREREGISTRO_4P.md` (commit `fa9eaae`) and its
Amendment 1 (parallel run, per-scenario seeds, committed before any number was seen). Script
`03_potencia_4p.py`; outputs `resultados_4p.json`, `_4p_stdout.txt`. Runtime 397.2 s on 32 cores.

**Headline: under the model we had promised — four free Hill parameters, a shared biological multiplier on
each replicate's EC50 (CV 0.20), a plate offset (CV 0.05) and per-well noise (CV 0.10) — the design's
power at n = 3 per arm is 0.167, not 0.897. Reaching 0.80 needs about 12 independent cultures
per arm at an aneuploid fraction of 0.30, 23 at 0.20, and more than 24 at 0.10. Fitting never failed;
the cost is biology, not the fit.**

## Central scenario (f = 0.30, EC50 = 40 nM, selectivity 4×, slope 1, CV_well 0.10, CV_bio 0.20, n = 3)

| Quantity | Value |
|---|---|
| Power, four-parameter fit | **0.167** |
| Fitting-failure rate | 0.000 |
| Power, the original two-parameter fit on the same simulated data | 0.234 |
| Reference: original two-parameter model without biological variability (`resultados.json`) | 0.897 |

So of the drop from 0.897 to 0.167, most is the added biological and plate variability
(0.897 → 0.234 with the same fitter) and the rest is the four-parameter fit
(0.234 → 0.167).

## Sweeps (one factor at a time from the central scenario; failure rate 0.000 throughout)

| Factor | Values → power |
|---|---|
| aneuploid fraction f | 0.10 → 0.050 · 0.20 → 0.096 · 0.30 → 0.176 · 0.50 → 0.434 |
| selectivity r | 2× → 0.068 · 4× → 0.165 |
| n per arm | 3 → 0.172 · 4 → 0.298 · 6 → 0.515 · 8 → 0.657 |
| CV_bio | 0.10 → 0.234 · 0.20 → 0.170 · 0.30 → 0.122 |
| CV_well | 0.05 → 0.275 · 0.10 → 0.160 · 0.15 → 0.102 |

## n per arm for 0.80 power (600 experiments per n)

| f | n for 0.80 | power at n = 3 / 6 / 12 / 24 |
|---|---|---|
| 0.30 | **12** | 0.20 / 0.52 / 0.85 / 0.99 |
| 0.20 | **23** | 0.07 / 0.26 / 0.47 / 0.82 |
| 0.10 | **> 24** | 0.05 / 0.13 / 0.16 / 0.28 |

## Predictions

| | Outcome |
|---|---|
| P-4P1 central power < 0.80 | **Confirmed** (0.167) |
| P-4P2 fitting-failure rate ≥ 5% | **Falsified** — 0.0% in every scenario; the bounds and start values never produced a rejected fit |
| P-4P3 n ≥ 5 at f = 0.30 and > 24 at f = 0.10 | **Confirmed** (12 and > 24) |
| P-4P4 the two-parameter fit recovers more than half of the loss | **Falsified** — it recovers 0.067 of the 0.730 lost; the biological variability, not the fit, is the larger cost |

## What this forces us to write (per the pre-registered mapping)

- The n = 3 branch is **retired** from the main body of the report; §6 reports n ≈ 12 per arm at
  f = 0.30 and 23 at f = 0.20 under the declared model, with 0.897 kept only as the optimistic
  two-parameter reference.
- The "n = 14 at f = 0.10" branch is **retired**; below f ≈ 0.20 the per-cell endpoint replaces bulk viability.
- *n* counts independent biological replicate cultures per arm; the failure rule is stated and its rate was zero.

## What this does not establish

Nothing about the child's cells. CV_bio = 0.20 is an assumption, not a measurement; the sweep shows
0.10–0.30 moves power at n = 3 between 0.23 and 0.12. The 4× selectivity remains
unsupported and unrefuted (`RESULTADOS_2_DOSIS.md`). A design that needs twelve independent cultures per
arm from one biopsy is heavier than the eight-week assay window implied, and §6 now says so.
