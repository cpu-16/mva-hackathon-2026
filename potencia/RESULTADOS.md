# The §6 assay can be powered, in a regime we have not measured

**Team: ciberpty** · 2026-09-01 · Pre-registered in `potencia/PREREGISTRO.md`, committed as `aa3143f`
**before** any number below existed. Nothing here was chosen after seeing the result.

---

## 1. The pre-committed sentence, applied

Power at the central scenario is **0.897**, which is ≥ 0.80. The pre-registration then obliges us to
write this and nothing else:

> **The §6 assay is in the right effect regime.** The sentence *"a negative result is ambiguous by
> design"* is **withdrawn as it applies to statistical power**. The design as written — 8
> concentrations, 3 biological replicates per arm, 72 h — detects a **4× EC50 selectivity** in a
> culture where **30% of cells carry an aneuploidy**, with 90% power at α = 0.05.
>
> ⚠️ **Read that with its qualifier, which is load-bearing: *powered for a 4× effect, if the treated
> culture is ~30% aneuploid and well-level CV is 10%.*** Neither of those two is measured in these
> cells. At 2× selectivity power is 0.387; at CV 0.15 it is 0.593. And a second pre-registered
> analysis the same day (`RESULTADOS_2_DOSIS.md`) gives us our own reason to doubt that 4× describes
> a cell carrying one extra chromosome. **"The assay is powered" without the qualifier is not a
> statement we can defend.**
>
> The separate caveat is **unaffected and still stands**: dermal fibroblasts are constitutional MVA
> cells, not tumour cells, so a negative does not close the tumour-board question, and a positive is
> as compatible with systemic toxicity as with therapeutic promise. That was never a power argument.

## 2. Why the hedge was wrong: it used the wrong denominator

The report justified the hedge with "variegation leaves each chromosome affected in 1–2% of cells".
That figure is **per chromosome** — 30% of cells divided across 22 autosomes. It is the correct
denominator for §5, which asks whether bulk WGS can see *one specific chromosome*. It is the wrong
one here, because a cell with a gain of chromosome 7 is under proteotoxic load whichever chromosome
it gained.

The sweep contains both readings, and they are not close:

| *f* (fraction of cells with ≥ 1 aneuploidy) | Power at n = 3 | n needed for 0.80 |
|---|---|---|
| **0.02** — the per-chromosome figure, i.e. what §6 implied | **0.063** | > 24 |
| 0.05 | 0.082 | > 24 |
| 0.10 | 0.196 | 14 |
| 0.20 | 0.589 | — |
| **0.30** — the diagnostic order of magnitude, the correct reading | **0.904** | **3** |
| 0.50 | 1.000 | 3 |

A power of 0.063 at α = 0.05 is a test that fires at its own false-positive rate: under the reading
§6 implied, the experiment would have been **blind**, and any negative would have been
uninterpretable. Under the correct reading it is well powered with the n already planned.

**The exercise passes its own falsification test.** The pre-registration said that if power were
≥ 0.80 even at *f* = 0.02, the calculation would not discriminate between the two readings and we
would report it as uninformative. It is 0.063, so it discriminates.

## 3. The finding that changes the protocol: *f* is unmeasured, and the assay is not robust to it

Power collapses between *f* = 0.30 and *f* = 0.10. **Nobody has counted metaphases in these
fibroblasts** — *f* is not a measurement, it is the order of magnitude of a diagnostic criterion, and
the value in a cultured fibroblast line is not the value in the blood that gave the diagnosis.
Culture selection pushes the wrong way: aneuploid cells proliferate more slowly, so *f* at assay time
is likely **lower** than *f* at biopsy.

**Consequence, and it is a change to §6 rather than a caveat added to it:**

> Add a **gating measurement** before the dose–response: a **metaphase count of cells carrying at
> least one numerical chromosome abnormality**, on the expanded fibroblast culture, at the passage
> that will be treated. This is not a new assay — the laboratory doing this work already sets up
> metaphase spreads, because premature chromatid separation scoring is the diagnostic criterion for
> MVA.
>
> ⚠️ **PCS scoring is not the same endpoint and does not substitute for it.** PCS is a
> centromere-cohesion phenotype; *f* is the proportion of cells with an abnormal chromosome *number*.
> The same slides give both, but they must be counted separately. An earlier version of this section
> conflated them. Record the number of abnormal chromosomes **per abnormal cell** at the same time —
> `RESULTADOS_2_DOSIS.md` shows the per-cell burden matters as much as the fraction.
>
> | Measured *f* | What to do |
> |---|---|
> | ≥ 0.25 | Proceed as designed, n = 3 |
> | 0.10 – 0.25 | n = 14 at *f* = 0.10; if that does not fit the window, enrich for aneuploid cells or move to a per-cell endpoint |
> | < 0.10 | **Do not run the bulk viability assay.** It cannot answer the question at any feasible n. Go to a per-cell readout |

Without that gate, a negative result from this experiment cannot be told apart from an underpowered
one — which is precisely the failure mode a reviewer would use to dismiss §4 and §6 together.

## 4. A second, smaller design correction

Power is not monotonic in the selectivity *r*: it rises to **0.955 at r = 6** and falls back to
**0.885 at r = 10**. That is not biology, it is the concentration range. At r = 10 the control's EC50
is 400 nM, which is the top of the planned 0–400 nM series, so it is estimated at the edge of the
data: the standard deviation of log₁₀(EC50) doubles from 0.049 to 0.098 and the estimate is biased
upward (413 nM against a true 400 nM). Curve fits do not fail — 0 of 200 — the estimate simply
becomes imprecise.

**Extend the series to ~1,000 nM.** The extra points cost nothing and they bracket the control's
EC50 even under high selectivity. The clinically relevant region is unchanged: Cmax is 231–312 nM.

## 5. The rest of the sweeps

| Swept | Values | Power |
|---|---|---|
| EC50 in aneuploid cells | 20, 40 nM | 0.903, 0.907 — insensitive |
| Selectivity *r* | 2, 3, 4, 6, 10 | 0.387, 0.763, 0.905, 0.955, 0.885 |
| Hill slope *m* | 1.0, 1.5, 2.0 | 0.894, 0.972, 0.981 — m = 1 is conservative, as declared |
| Well CV | 0.05, 0.10, 0.15 | 1.000, 0.904, 0.593 |
| Replicates *n* | 3, 4, 6, 8 | 0.897, 0.982, 1.000, 1.000 |

Two of these are worth acting on. A **selectivity of only 2×** gives power 0.387, so the experiment
is not powered to detect a weak effect — and the honest framing is that it is powered to detect the
effect size that would matter clinically, not any effect. And **assay noise matters more than
replicate count**: going from CV 0.10 to 0.15 costs more power (0.904 → 0.593) than dropping from
n = 4 to n = 3 (0.982 → 0.897). Tighten the plating and the readout before adding replicates.

## 5b. Two places where the implementation is weaker than the pre-registration said

Found by adversarial review of this document, and recorded rather than quietly fixed:

- **The pre-registration says "four-parameter Hill curve"; the code fits two parameters.**
  `01_potencia.py` fits EC50 and slope with the top fixed at 1 and the bottom at 0. That is the right
  model for a normalised viability readout, but it is *not* what the pre-registration wrote, and a
  four-parameter fit on 8 points with n = 3 would be noticeably less stable. The reported power is
  therefore **optimistic relative to the declared model**, and the declared model is the one we
  committed to. We report the discrepancy; we do not re-run and claim the new number was the plan.
- **The noise model has no shared replicate term.** Each concentration gets independent log-normal
  error, with no donor, plate or batch effect. Real dose–response curves are correlated within a
  plate, which makes fitted EC50s noisier than simulated ones. This too pushes the reported power
  **upward**. The CV sweep (0.05 / 0.10 / 0.15) is the only handle on it, and CV 0.15 already costs
  more power than dropping a replicate.

Both errors point the same way: **0.897 is an upper bound on the power of this design, not an
estimate of it.**

## 6. What this does not establish

- **It is a power calculation, not evidence that the dependency transfers.** DepMap already told us
  the aneuploidy–proteasome association attenuates in solid lineages (interaction p = 0.026, §3.5).
  This says the experiment could see the effect if it is there; it says nothing about whether it is.
- ***r* is the unknown being measured**, not an input. The 4× central value is the effect size the
  design is powered for. No fibroblast selectivity measurement for bortezomib in constitutional
  aneuploidy exists.
- **The mixture model is the load-bearing assumption**: cell-autonomous dependency, and a
  drug-sensitive subpopulation showing up in bulk viability in proportion to its size. It ignores
  paracrine effects and differential proliferation. Both were declared in the pre-registration
  before the numbers were computed.
- **A significant EC50 shift in fibroblasts is not a reason to treat this child.** Filter 4 still
  fails (§4).

## 7. Reproduce

    potencia/PREREGISTRO.md    the design, committed as aa3143f before any run
    potencia/01_potencia.py    seeded simulation, 2,000 experiments per scenario
    potencia/resultados.json   every number above

CPU only, no patient data, no GPU. Runtime ~30 minutes.
