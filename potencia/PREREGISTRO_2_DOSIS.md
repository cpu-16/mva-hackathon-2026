# Pre-registration 2 — is a 4× selectivity plausible for a cell with ONE extra chromosome?

**Team: ciberpty** · written and committed BEFORE the analysis ran. The git timestamp is the claim.

---

## 1. Why this exists: it attacks our own result from this morning

`potencia/RESULTADOS.md` concluded that the §6 fibroblast assay is powered (0.897) at a central
scenario of **4× EC50 selectivity** between aneuploid and euploid cells. That selectivity was taken
from Ippolito et al. (PMID 39247952), whose EC50 of < 40 nM was measured in **highly aneuploid cancer
lines**.

**A hostile reviewer with domain knowledge would attack exactly there, and they would be right to.**
Proteotoxic load is not a switch, it is a dose: a cell carrying sixteen altered arms is not the same
as a cell carrying two. And in MVA the aneuploid cells carry **about one extra or missing chromosome
each**, not sixteen. That follows from the report's own numbers: if ~30% of cells are aneuploid and
each chromosome is affected in ~1.4% of cells, then the mean number of altered chromosomes per
aneuploid cell is 22 × 0.014 / 0.30 ≈ **1.0**.

So the mixture model in `potencia/01_potencia.py` is **binary where the biology is graded**, and it
assigns to a one-chromosome MVA cell the sensitivity measured in a sixteen-arm cancer line. If that
assignment is wrong, this morning's power result is optimistic and the correction we published today
is itself in need of a correction.

**We can test it with data we already hold**, from our own pre-registered DepMap package
(`depmap/RESULTADOS.md`): arm-level aneuploidy scores for 2,420 lines and CRISPR gene-effect values
for PSMB5, bortezomib's own target.

## 2. Question

Across DepMap cell lines, how much does the genetic dependency on **PSMB5** change **per altered
chromosome arm** — and is the change expected for **two arms** (one whole chromosome, the MVA case)
large or small relative to the residual spread between lines?

## 3. Model and statistic, fixed now

Ordinary least squares of PSMB5 CRISPR gene effect on the arm-level aneuploidy score, **fitted
separately within each lineage stratum** (solid, haematological) because our own DepMap result found
a significant interaction (p = 0.026), and adjusted for ploidy, which we already excluded as a
confounder (p = 0.88) and therefore keep as a covariate rather than a hypothesis.

    PSMB5_effect ~ b0 + b1 · arms_altered + b2 · ploidy      (within stratum)

Reported: **b1** and its 95% confidence interval, in gene-effect units per arm; the predicted
difference for **2 arms** and for **18 arms**; and both expressed as a fraction of the **residual
standard deviation** of PSMB5 effect within the stratum.

The residual SD is the comparator on purpose. It is the natural scale of "how different is this line
from another line of the same type", and it is the scale on which an experiment has to separate two
cultures.

## 4. Pre-committed outcomes

Let **Δ₂** be the predicted change in PSMB5 effect for 2 altered arms, and **σ** the residual SD in
solid lines — the stratum relevant to this child.

- **|Δ₂| / σ ≥ 0.25** → a one-chromosome cell sits an appreciable fraction of a standard deviation
  away from euploid. The 4× central selectivity is not implausible, this morning's power result
  stands as written, and we say so.
- **|Δ₂| / σ < 0.10** → the effect of one chromosome is negligible on the scale that separates cell
  lines. **This morning's central scenario is then not defensible**, and we must say in
  `potencia/RESULTADOS.md` and in Track 2 §6 that the assay is powered for an effect size we have no
  reason to expect in these cells, and re-centre the calculation on the selectivity that the DepMap
  slope actually implies.
- **0.10 ≤ |Δ₂| / σ < 0.25** → we report the ratio and re-run the power calculation at the implied
  selectivity, replacing the 4× central value rather than keeping both.

**Falsification of the exercise.** If **b1 does not differ from zero** in solid lines (its 95%
confidence interval covers 0), then this analysis cannot constrain the selectivity at all and we
report it as uninformative rather than reading a null as evidence of a small effect. Note we already
know PSMB5 dependency is **not significant** in solids (ρ = −0.077, q = 0.118), so this outcome is
likely and we are pre-committing to reporting it as a null.

## 5. What this cannot do, stated before the result

- **Gene effect is not drug EC50.** A CRISPR knockout is a complete, permanent loss; a drug is a
  partial, reversible inhibition. We will report the slope in gene-effect units and **will not convert
  it into an EC50 ratio** — there is no calibration that would license that conversion. The
  conclusion is about whether the dose–response *has an appreciable slope at the low end*, not about
  the numeric value of *r*.
- **Cancer lines are not constitutional fibroblasts.** This is the same extrapolation the whole
  Track 2 argument rests on, and it is not resolved by this analysis.
- **The aneuploidy score counts arms, not the identity of the arm.** Two arms of chromosome 21 are
  not two arms of chromosome 1. The model treats them as equivalent; the biology does not.
- **Linearity is an assumption.** If the true relationship is threshold-like, a linear slope
  underestimates the effect at high burden and overestimates it at low burden — which is the region
  we care about. We will check for curvature by adding a quadratic term and reporting whether it
  changes the sign of the conclusion, but a null curvature test does not establish linearity.

## 6. Reproduce

    potencia/02_dosis.py        the regression, seeded where randomness is used
    potencia/dosis.json         every number
    depmap/psmb5_merged.csv     input, produced by the pre-registered DepMap package

CPU only, no patient data, no GPU, no new download.
