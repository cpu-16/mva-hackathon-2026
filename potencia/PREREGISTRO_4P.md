# Pre-registered follow-up — the four-parameter fit, biological variability and fitting failures

**Team ciberpty · MVA Hackathon 2026 · committed 2026-09-08 before `03_potencia_4p.py` exists or runs.**

**Status: a follow-up to `PREREGISTRO.md` (commit before `01_potencia.py`), informed by its results and
by two adversarial reads.** `RESULTADOS.md` §5b records that the implementation fitted **two** Hill
parameters where the pre-registration promised **four**, and that the noise model had **no shared
replicate term**; both push the reported power (0.897 at the central scenario) upward. The judge round
(`evidencia/codex_juez_rubrica_2026-09-07.md`, change #3) asked for exactly this: *"either implement
the promised four-parameter model with biological variability and fitting failures, or retire the
numerical sample-size branches from the main body. Specify what n counts."* We implement it. The
original results stand as the optimistic reference and are not edited.

Results are appended below the line, dated. Nothing above the line is edited afterwards.

## What already exists, so nothing here can be mistaken for a blind test

- Two-parameter fit (EC50, slope; top fixed at 1, bottom at 0), per-well log-normal noise, 8
  concentrations 0–400 nM, n = 3 per arm, two-sided t on log10 EC50: **power 0.897** at f = 0.30,
  EC50_aneu = 40 nM, selectivity r = 4, slope m = 1, CV 0.10; **0.387** at r = 2; 0.589 at f = 0.20,
  0.196 at f = 0.10; n for 0.80 at f = 0.10 is 14 (`resultados.json`).
- The §6 design was since extended to **0–1,000 nM** with dense sampling below 100 nM
  (`RESULTADOS.md` §4), which the original script did not use.

## What *n* counts — fixed now

*n* is the number of **independent biological replicate cultures per arm** — separate cultures from
independent passages, seeded on separate plates — each yielding one fitted dose–response curve and one
EC50. Technical wells within a curve are not *n*. The test compares the *n* patient EC50s against the
*n* control EC50s.

## Model, fixed now

- **Truth**, unchanged: viability = (1 − f)·Hill(c; r·E, m) + f·Hill(c; E, m) for the patient culture
  and Hill(c; r·E, m) for the control, with E = EC50 of aneuploid cells (40 nM), r = within-cell
  selectivity, m = slope.
- **Concentrations**, the current design: 0, 5, 10, 25, 50, 75, 100, 200, 400, 700, 1,000 nM
  (11 points; six at or below 100 nM).
- **Biological variability**, new: each replicate culture draws a shared multiplier on its EC50,
  log-normal with coefficient of variation **CV_bio ∈ {0.10, 0.20, 0.30}** (central 0.20), applied to
  the whole curve; and a plate-level multiplicative offset on viability, log-normal with CV 0.05.
  Per-well noise stays log-normal with CV 0.10 (sweep 0.05 / 0.15 retained).
- **Fit**, the promised four-parameter Hill: bottom b, top t, EC50, slope m, all free, fitted per
  replicate curve by least squares with bounds b ∈ [0, 0.5], t ∈ [0.5, 1.5], log10 EC50 ∈ [0, 4],
  m ∈ [0.2, 6]; start values b = 0, t = 1, EC50 = 80 nM, m = 1.
- **Fitting failure**, counted and reported: non-convergence, or an EC50 estimate at either bound of
  its interval, or a fitted top below the fitted bottom + 0.2. A failed fit in any replicate makes that
  simulated experiment a **non-rejection** (the pre-registered rule), and the failure rate is reported
  separately so a reader can see how much of the lost power is fitting rather than biology.
- **Statistic**: two-sided Welch t on log10 EC50 between arms, α = 0.05. (The original used the
  equal-variance t; Welch is stated here because the patient arm has an extra variance component.)
- **Simulation**: 2,000 experiments per scenario, seed 20260908; n for 0.80 power searched with 600
  experiments per n from 3 to 24.

## Scenarios, fixed now

Central: f = 0.30, E = 40 nM, r = 4, m = 1, CV_well 0.10, CV_bio 0.20, n = 3. Sweeps, one factor at a
time: f ∈ {0.10, 0.20, 0.30, 0.50}; r ∈ {2, 4}; n ∈ {3, 4, 6, 8}; CV_bio ∈ {0.10, 0.20, 0.30};
CV_well ∈ {0.05, 0.10, 0.15}. Also the two-parameter fit re-run on the **same** simulated data at the
central scenario, so the cost of the four-parameter fit is separated from the cost of the added
variability.

## Predictions, on the record

- **P-4P1.** At the central scenario the four-parameter power is **below 0.80** (against 0.897 before).
- **P-4P2.** The fitting-failure rate at n = 3 is **at least 5%** of simulated experiments.
- **P-4P3.** The n needed for 0.80 power at f = 0.30, r = 4, CV_bio 0.20 is **at least 5**, and at
  f = 0.10 it exceeds 24 (not reachable within the searched range).
- **P-4P4.** Re-running the two-parameter fit on the same data recovers more than half of the power
  lost relative to 0.897 — i.e., the four-parameter fit itself, not the biological variability, is the
  larger cost at n = 3.

## What each outcome forces us to write in §6 (both parts)

| Outcome | Sentence |
|---|---|
| P-4P1 holds | The n = 3 branch is **retired** from the main body; §6 reports the n the four-parameter model needs, with the fitting-failure rate, and keeps 0.897 only as the optimistic two-parameter reference. |
| P-4P1 fails (power ≥ 0.80) | The n = 3 branch stays, now under the declared model, with the failure rate stated. |
| P-4P3: n at f = 0.10 exceeds 24 | The "n = 14 at f = 0.10" branch is retired; below f ≈ 0.20 the per-cell endpoint replaces bulk viability. |
| Any outcome | *n* is defined as independent biological replicate cultures; the failure rule is stated; every number in `RESULTADOS.md` is left as the optimistic reference. |

## Stopping rules

One script, one run. A bug fix is allowed only if the script fails to execute, and is recorded. No
scenario is added after seeing a number. This measures the design's statistical behaviour under a
declared model; it measures nothing about the child's cells.

---
## Results

*(appended below, dated; the text above is never edited)*

### Amendment 1 — 2026-09-08, 00:22, before any result was seen

The first execution ran single-threaded and was stopped after 12 minutes at the owner's request to
finish sooner; its standard output was still buffered and `resultados_4p.json` had not been written, so
**no number from it was observed**. The script is re-run with the scenarios distributed over CPU cores
(`multiprocessing`), which changes one thing only: each scenario now draws from its own random stream
seeded from the master seed (20260908 plus the scenario index) instead of one sequential stream. Model,
scenarios, simulation counts, predictions and decision rules are unchanged. No GPU is used.

### Results — 2026-09-08, 00:29 EST (`03_potencia_4p.py`, one parallel run, 397.2 s)

Full write-up: `RESULTADOS_4P.md`. Central power **0.167** (0.897 before), fitting failures 0.000,
two-parameter fit on the same data 0.234; n for 0.80: **12** at f = 0.30, **23** at f = 0.20,
**> 24** at f = 0.10. P-4P1 and P-4P3 confirmed; P-4P2 (failures ≥ 5%) and P-4P4 (the fit is the larger
cost) **falsified** — the cost is the biological variability. The n = 3 and n = 14 branches are retired from
the main body per the pre-registered mapping.
