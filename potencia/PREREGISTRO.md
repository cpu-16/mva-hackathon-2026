# Pre-registration — Is the §6 fibroblast assay in the right effect regime?

**Team: ciberpty** · Rare Disease, Real Kid: MVA Hackathon 2026
**Written and committed BEFORE any number was computed.** The git timestamp of this file is the
claim. Amendments are appended at the end, dated, and never edit the text above them.

---

## 1. Why this exists

Track 2 §6 proposes an eight-week go/no-go experiment: bortezomib dose–response at 72 h on the
child's dermal fibroblasts against matched controls, and asks whether the proteasome dependency that
Ippolito et al. measured in highly aneuploid cancer lines (PMID 39247952) transfers to constitutional
MVA. The report then hedges it:

> "variegation leaves each chromosome affected in 1–2% of cells, so a fibroblast population may
> simply not be aneuploid enough to express a dependency … **A negative result is therefore ambiguous
> by design**"

**That hedge has never been computed.** Both external reviewers named it: §4 plus §6 is currently an
Impact claim resting on a test of unknown power, and an underpowered assay is how a predicted
solid-lineage attenuation gets laundered into an "ambiguous negative".

There is also a specific reason to suspect the hedge is wrong, and it is an arithmetic point rather
than a biological one. The "1–2% of cells" figure is **per chromosome**: it is 30% of cells carrying
an aneuploidy, divided across 22 autosomes (§5, and `MOSAICISMO.md`). It is the correct denominator
for asking whether **bulk WGS can see a specific chromosome**, which is what §5 uses it for. It is
the **wrong** denominator for asking whether a **cell** is under proteotoxic load, because a cell with
a gain of chromosome 7 is aneuploid whichever chromosome it was. The quantity the assay depends on is
the fraction of cells carrying *at least one* aneuploidy, and §6 has silently substituted one for the
other.

We compute the power. The result can go either way and we commit to both outcomes below.

## 2. Question

Given the mosaic architecture of MVA, does the dose–response design in §6 have adequate statistical
power to detect the predicted differential sensitivity between patient and control fibroblasts — and
if not, what changes?

## 3. Model, fixed now

A fibroblast culture from this child is a **mixture**: a fraction *f* of cells carries at least one
aneuploidy and is assumed to bear the proteotoxic dependency; the remainder is karyotypically normal
and is assumed to behave like control fibroblasts. Population viability at bortezomib concentration
*c* is therefore

    V(c) = (1 − f) · H(c; E_dip, m) + f · H(c; E_aneu, m)

with `H(c; E, m) = 1 / (1 + (c/E)^m)`, the standard Hill form. The control culture is `f = 0`.

**This mixture model is itself the main assumption and we state it plainly.** It assumes the
dependency is cell-autonomous and that a drug-sensitive subpopulation shows up in a bulk viability
readout in proportion to its size. It ignores paracrine effects, selection during culture expansion,
and any difference in proliferation rate between aneuploid and euploid fibroblasts. Culture selection
in particular runs *against* us — aneuploid cells proliferate more slowly, so *f* at assay time is
likely lower than *f* at biopsy. We do not model that; we note it as a bias with a known sign and we
handle it by sweeping *f* down to 0.02.

## 4. Parameters, declared before computing

| Parameter | Central value | Swept over | Where it comes from |
|---|---|---|---|
| *f*, fraction of cells with ≥1 aneuploidy | **0.30** | 0.02, 0.05, 0.10, 0.20, 0.30, 0.50 | The order of magnitude of the MVA diagnostic criterion (§5). **0.02 is included on purpose**: it is the per-chromosome figure, i.e. what §6 currently implies, so the sweep contains the reading we suspect is wrong |
| *E_aneu*, EC50 in aneuploid cells | **40 nM** | 20, 40 nM | Conservative upper bound read from a figure panel in PMID 39247952, exactly as declared in Track 2 §3.2. Not a tabulated value |
| *r = E_dip / E_aneu*, the selectivity being tested | **4×** | 2, 3, 4, 6, 10 | **No published value exists for fibroblasts.** This is the effect size the experiment is powered *for*, not a measurement, and it is reported as a sweep for that reason |
| *m*, Hill slope | **1.0** | 1.0, 1.5, 2.0 | Default; steeper slopes make mixtures easier to separate, so 1.0 is the conservative choice |
| CV of a viability well | **0.10** | 0.05, 0.10, 0.15 | Typical for a luminescent viability readout. Applied multiplicatively on a log scale |
| *n*, biological replicates per arm | **3** | 3, 4, 6, 8 | The §6 design as written |
| Concentrations | 8 points, 0–400 nM, denser below 100 nM | fixed | The §6 design as written |

## 5. Statistic and decision rule, fixed now

For each simulated experiment: fit the four-parameter Hill curve to patient and to control by
non-linear least squares, take `log10(EC50)` from each, and compare the two arms with a two-sided
Student *t* test at **α = 0.05**, *n* per arm. Power is the fraction of **2,000** simulated
experiments that reject. Fits that fail to converge count as **non-rejections**, never as discards —
discarding them would inflate power.

**Pre-committed outcomes.** We write the three sentences now so that we cannot choose one after
seeing the number:

- **Power ≥ 0.80 at the central scenario** → the §6 assay is in the right regime. We **delete** the
  sentence "a negative result is ambiguous by design" *as it applies to power*, state the powered
  effect size explicitly, and keep the separate — and unaffected — caveat that fibroblasts are not
  tumour cells so a negative does not close the tumour-board question.
- **Power < 0.50 at the central scenario** → the assay as designed is blind. We **change the go
  criterion**, we do not hedge it: the experiment must either enrich for aneuploid cells before
  treatment or move to a per-cell endpoint. A bulk 72 h viability readout would be dropped as the
  primary.
- **0.50 ≤ power < 0.80** → we report the *n* that reaches 0.80 at the central scenario and amend the
  §6 design to that *n*, or state that it is not attainable in the eight-week window.

**Falsification of the exercise itself.** If power is ≥ 0.80 even at *f* = 0.02 — the per-chromosome
reading — then the calculation does not discriminate between the two readings of *f*, the argument in
§1 carries no weight, and we report that the exercise was uninformative rather than quietly keeping
the favourable half.

## 6. What this cannot do

- It cannot tell us *f* for this child. Nobody has karyotyped these fibroblasts; **the value is
  unmeasured and we sweep it rather than assume it.** A metaphase count with PCS scoring would
  measure it, and that is the cheapest way to make this calculation binding rather than indicative.
- It cannot tell us *r*. There is no fibroblast selectivity measurement for bortezomib in
  constitutional aneuploidy; that is the point of running the experiment.
- It says nothing about whether the dependency transfers at all. That is biology, and DepMap already
  told us the association attenuates in solid lineages (§3.5).
- The power it reports is for the **statistical comparison**, not for the clinical decision. A
  significant EC50 shift in fibroblasts is not evidence that bortezomib helps this child.

## 7. Reproduction

    potencia/01_potencia.py     simulation and sweeps, seeded
    potencia/RESULTADOS.md      written after, with the pre-committed sentence applied

No patient data, no GPU, public parameters only.
