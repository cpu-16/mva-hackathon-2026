# Transferring the five-filter framework to MVA2 (*CEP57*) and MVA3 (*TRIP13*)

**Team: ciberpty** · Rare Disease, Real Kid: MVA Hackathon 2026
Companion to `REPORT_track2_EN.md` — extends §9 (Scalability) and uses the worksheet defined in its
Appendix. No new drug, no new analysis and no new citation is introduced here: every source used
below is already cited in that report.

---

## 0. What this document is, and what it is not

The report's transferable product is the **five-filter worksheet** (§2, Appendix). A framework that
returns the same verdict for every disease it is pointed at is a slogan. This document is the test of
that claim: we take the **same candidate** (bortezomib), hold the filters fixed, and run it against
the two other genetic forms of mosaic variegated aneuploidy.

The answers are different, and they are different *early*:

| | MVA1 — biallelic *BUB1B* | MVA2 — biallelic *CEP57* | MVA3 — biallelic *TRIP13* |
|---|---|---|---|
| Bortezomib verdict | Fails filter 4 for **this** child; conditional for a patient with an active tumour | **Fails filter 4; filters 2–3 not evaluable** | **Conditional — passes 1–3, filters 4–5 undecided** |
| Where it stops | Patient-specific safety, with the inverting condition **demonstrably present** (he has already had an embryonal tumour) | Patient-specific safety, with the inverting condition **never reported** in 15 published individuals — and the mechanism unmeasurable besides | Nothing stops it; nothing licenses it either |

This is a **prospective, desk-based** exercise. Neither worksheet rests on a patient, a sample or an
experiment. No proteasome data of any kind exist for *CEP57*- or *TRIP13*-deficient cells
(REPORT §9), so both sheets contain cells we leave unfilled on purpose. Filling them with a
substitute number is the failure mode the framework exists to prevent (Appendix, *How to fill it in*).

---

## 1. The axes that decide the answer

The framework does not ask "is this an MVA gene?". It asks whether the drug addresses the lesion or a
**direct consequence** of it (filter 2), and — through filter 4 — whether there is a clinical setting
in which the risk is worth taking. On both axes the three genes separate, and the separation is
sourced, not assumed.

| Axis | MVA1 (*BUB1B*) | MVA2 (*CEP57*) | MVA3 (*TRIP13*) |
|---|---|---|---|
| Molecular lesion | Mitotic checkpoint complex / kinetochore–microtubule attachment control (PMID 15475955) | Centrosomal protein "involved in nucleating and stabilizing microtubules" (PMID 21552266) | SAC component; patient cells have "no detectable TRIP13" (PMID 28553959) |
| SAC status in patient cells | Severe impairment — "individuals with biallelic TRIP13 or *BUB1B* mutations … their cells display severe SAC impairment" (PMID 28553959); "impaired mitotic checkpoint, chromosome alignment defects, and low overall BUBR1 abundance" (PMID 20516114) | **"Minimal SAC deficiency"** (PMID 28553959) | **Severe** — "substantial impairment of the spindle assembly checkpoint (SAC), leading to a high rate of chromosome missegregation" (PMID 28553959) |
| Embryonal tumour risk | High (PMID 28553959); E-RMS characterised in a biallelic *BUB1B* MVA case (PMID 16182441) | **"MVA due to biallelic CEP57 mutations … is not associated with embryonal tumors"** (PMID 28553959); "At the time of writing, none of the 15 individuals with MVA2 described in literature developed cancer" (PMID 39264246) | High — **6/6** individuals with biallelic loss-of-function *TRIP13* "all six developed Wilms tumor" (PMID 28553959); a 2026 case adds an orbital embryonal rhabdomyosarcoma at age 12 in the same child (PMID 42595739) |
| Tumour type when it occurs | Solid (Wilms, rhabdomyosarcoma) — and MDS/AML/ALL also reported (PMID 39264246) | None reported | Solid (Wilms; orbital E-RMS) |

Two consequences follow before any worksheet is filled.

**(a) The proteotoxic premise is graded, and *CEP57* sits at the low end of the only comparison that
exists.** The mechanism bortezomib is proposed for is the proteasome dependency of aneuploid cells
(PMID 39247952). The single source that puts the three genotypes on one scale places *CEP57* at
"minimal SAC deficiency" against "severe SAC impairment" for the other two (PMID 28553959).

**(b) The setting that inverts filter 4 does not arise in MVA2.** In MVA1 and MVA3 the honest
proposition is not "give this drug" but "have an answer ready for a tumour board if a second tumour
appears" (REPORT §4). With no cancer reported in 15 published MVA2 individuals (PMID 39264246), there
is no comparator against which an 18% paediatric neuropathy rate becomes acceptable.

---

## 2. Worksheet A — MVA2, biallelic *CEP57*

*Same columns as the report's Appendix. A candidate must pass all five.*

| Candidate | 1. Approved? | 2. Addresses lesion or a direct consequence? | 3. Cmax ≥ effective concentration? | 4. Safe in *this* patient? | 5. Does not increase mis-segregation among survivors? | Verdict |
|---|---|---|---|---|---|---|
| **Bortezomib** | Yes | **Not evaluable.** It does not touch the lesion (centrosomal microtubule nucleation/stabilisation, PMID 21552266). The consequence route is the aneuploidy-driven proteasome dependency (PMID 39247952) and **no proteasome measurement in *CEP57* cells exists**. *CEP57*-MVA cells show "minimal SAC deficiency" (PMID 28553959), which is a statement about the checkpoint and not about the aneuploid burden the drug exploits — so it is a reason to expect less, not a demonstration of less | **Not evaluable.** No aneuploidy-stratified EC50 in *CEP57*-deficient cells exists (§4 below) | **Fails.** The report's positive case is conditional on an active malignancy, because outside one the 18% paediatric neuropathy rate decides against it (REPORT §4). **No cancer has been reported in the 15 published MVA2 individuals** (PMID 39264246), so the setting that inverts this filter has not been observed to occur | Not reached | **Fails at filter 4, and cannot be evaluated at filters 2–3.** Different from MVA1 in kind: MVA1 also fails filter 4, but there the inverting condition demonstrably exists — this child has already had an embryonal tumour |

**Why filter 2 is "not evaluable" and not "no" — we corrected this after an adversarial review.**
An earlier version of this sheet rejected the candidate *at filter 2*, reasoning from "minimal SAC
deficiency" to "less proteotoxic burden". That step does not hold. "Minimal SAC deficiency" is a
statement about the *checkpoint*, not about the **aneuploid fraction**: biallelic loss-of-function
*CEP57* is a documented cause of "constitutional mosaic aneuploidies" (PMID 21552266), so these cells
*are* aneuploid, and Ippolito's dependency is driven by the stoichiometric imbalance of the aneuploid
**state**, not by the rate at which new errors are made (PMID 39247952). Absence of a measurement is
"not evaluable"; it is not a negative. A per-cell aneuploidy measurement in *CEP57* patient cells
could show a burden comparable to MVA1 — and it still would not make filter 2 a "yes", because no
proteasome data would exist for it.

**The absence of reported cancer was also in the wrong column, and we moved it.** It was being used to
strengthen a *mechanism* verdict. Whether a clinical setting exists in which the risk becomes worth
taking is filter 4, which is where it now sits. It is also weaker than it looks: fifteen reported
individuals is a small denominator, and the same 2024 consensus that records no cancer among them
still recommends surveillance for all MVA conditions (PMID 39264246). We therefore write "has not been
reported to occur", never "does not occur".

What does *not* depend on that inference is the second half of the verdict. The report's positive case
for bortezomib is explicitly conditional on an active malignancy, because outside one the neuropathy
risk decides against it (REPORT §4). In MVA2 that condition has not been reported to occur.

**What would change this verdict.** A first published cancer in an MVA2 individual, or a measurement
showing an aneuploid burden and proteasome dependency in *CEP57* cells comparable to the aneuploidy-high
lines of PMID 39247952. Either one reopens the sheet. Neither exists today.

---

## 3. Worksheet B — MVA3, biallelic *TRIP13*

| Candidate | 1. Approved? | 2. Addresses lesion or a direct consequence? | 3. Cmax ≥ effective concentration? | 4. Safe in *this* patient? | 5. Does not increase mis-segregation among survivors? | Verdict |
|---|---|---|---|---|---|---|
| **Bortezomib** | Yes | **Yes — on the same footing as MVA1.** Not the lesion (nothing restores TRIP13), but the best-characterised consequence: severe SAC impairment and "a high rate of chromosome missegregation" (PMID 28553959) feeding the proteasome dependency of aneuploid cells (PMID 39247952) | **Yes on total drug, with the same denominator as MVA1 and the same weakness:** 231–312 nM Cmax (IV, 1.3 mg/m², FDA label NDA 021602 s040 §12.3) vs EC50 < 40 nM in highly aneuploid lines (PMID 39247952) = **5.8–7.8×**. IV only; the subcutaneous route (53.1 nM) does not pass. The EC50 is from aneuploidy-stratified **cancer** lines, not *TRIP13* cells | **Not evaluable — no patient.** The generic burden transfers unchanged: peripheral neuropathy in 18% of paediatric patients, motor in 8% (FDA BPCA Clinical Review, NDA 021602, 2015). Whether it is acceptable is a statement about one child at one moment | **No evidence it increases mis-segregation; untested — and the stake is higher here.** With no detectable TRIP13 and severe SAC impairment (PMID 28553959), a survivor population selected for instability is a more serious failure mode than in a checkpoint-competent tissue. Endpoint: micronucleus assay, OECD TG 487 | **Conditional, not approved. Same standing as MVA1 minus this child's specific contraindication: a question for a tumour board in an MVA3 patient with an active tumour, gated on the ex-vivo test of REPORT §6** |

**Three constraints we carry across with the candidate, not just the favourable half.**

1. **Our own pre-registered result cuts against it here too.** The DepMap test (REPORT §3.5) found the
   aneuploidy–proteasome link attenuated in solid tumours: PSMB5 dependency ρ = −0.077, q = 0.118 in
   833 solid lines versus ρ = −0.261, q = 0.042 in 113 haematological lines, aneuploidy × lineage
   interaction **p = 0.026**, ploidy excluded (p = 0.88). The MVA3 tumours on record are **solid**
   (Wilms in 6/6, PMID 28553959; orbital E-RMS, PMID 42595739). The transfer therefore inherits the
   weakness, not a fresh start.
2. **The mTOR antagonism prediction transfers unchanged.** Everolimus or sirolimus would be expected
   to *protect* aneuploid cells from proteasome inhibition rather than synergise (PMID 31530568,
   imported as an inference from its mechanism — that paper did not test rapalogues).
3. **The gate is the same experiment.** REPORT §6 is written for *BUB1B* fibroblasts; run on *TRIP13*
   patient fibroblasts it answers the same question with the same advancement criteria, including the
   stop signal (patient cells markedly more sensitive than controls *without* the aneuploidy-high
   positive control shifting further ⇒ constitutional toxicity, not selectivity). **It inherits the
   gate too**: the aneuploid cell fraction must be measured on the culture before treatment, and the
   replicate count follows from it (REPORT §6, `potencia/RESULTADOS.md`).

---

## 4. What we would need to fill filter 3 for these — and do not have

Filter 3 needs a **real denominator**: an effective concentration measured in a model stratified for
the disease mechanism. The report rejected metformin because no such number exists for it at all
(REPORT §3.1, Appendix). The gap here is a *different* one, and conflating the two would be dishonest,
so we state both:

| | Metformin, MVA1 (report §3.1) | Bortezomib, MVA2/MVA3 (here) |
|---|---|---|
| Is there an aneuploidy-selective effective concentration? | **No — none exists for metformin in any model** | **Yes, generic:** EC50 < 40 nM in highly aneuploid cancer lines (PMID 39247952) |
| Is there a genotype-specific one? | No | **No — no proteasome data exist for *CEP57* or *TRIP13* cells** (REPORT §9) |
| Consequence | Not evaluable on the proposed mechanism | Filter 3 is passed on the **generic** denominator only, and the ratio is on total, not free, drug |

**What is missing, concretely.** A dose–response in *CEP57*- and in *TRIP13*-deficient patient cells
against matched controls and an aneuploidy-high positive control, with per-cell aneuploidy measured on
the same population — i.e. the design of REPORT §6, run twice more. There is a reason to want the
per-cell number specifically, and it is **not** the "1–2% of cells" argument, which is a
per-chromosome figure and the wrong denominator for this question (`potencia/RESULTADOS.md` §2).
The right reason is a dose one: proteotoxic load scales with how much of the genome is unbalanced,
and an MVA cell carries **about one** altered chromosome, two arms, while eighteen arms is the point
at which we evaluated the dose response (`potencia/dosis.json`, `arms_high`). **We have not counted
arms in the specific lines that gave the < 40 nM EC50**, and no such count exists in any of our files.
In DepMap, within the lineage where the
aneuploidy–proteasome dependency is real at all, the PSMB5 dependency changes by **0.028 gene-effect
units per arm** — so two arms move it 0.09 residual standard deviations while eighteen move it 0.84
(`potencia/RESULTADOS_2_DOSIS.md`). The generic denominator is therefore *evaluated* at the far end of
the range from where these three genotypes sit — a statement about our dose-response contrast, not a
measurement of the lines the EC50 came from. That applies to MVA2 and MVA3 exactly as it applies to
MVA1, and it is why a genotype-specific EC50 is not a formality.

**We do not manufacture the missing cells.** Substituting the generic aneuploid-line EC50 as if it
were a *CEP57* or *TRIP13* value would produce a ratio with no meaning, which is the error the
worksheet's instructions name.

---

## 5. Why this matters

A framework that returns the same answer for three diseases is a slogan. One that **stops the
candidate at filter 4 in MVA2, with filters 2–3 not evaluable, and leaves it conditional in MVA3** is a
demonstration — because the
two verdicts were produced by the same five questions, in the same order, from published evidence,
without adjusting the questions to reach them.

Three properties are visible only because the answers diverged:

- **The filters bind at different points.** MVA1 stops at filter 4 for a reason that is a fact about
  one child; MVA2 also stops at filter 4, but for a reason that is a fact about the gene — the setting
  that would invert that filter, an active malignancy, has not been reported in MVA2 — with filters 2–3
  not evaluable there for want of any proteasome measurement in *CEP57* cells; MVA3 stops at nothing — it stops only for want of data. A framework in
  which every candidate fails at the same place is not discriminating; it is expressing a prior.
- **"Same syndrome" is not a licence to transfer a drug.** All three are mosaic variegated aneuploidy,
  and biallelic *BUBR1*, *CEP57* and *TRIP13* are the three recognised causes (PMID 31738183). A
  mechanism-blind repurposing exercise would carry a proteasome inhibitor to all three on the shared
  diagnosis. The evidence separates them: the same source that grants the mechanism to *TRIP13* denies
  the tumour association to *CEP57* (PMID 28553959).
- **Empty cells are the output, not a defect.** Filter 3 stays unfilled for both genotypes, and the
  report's own DepMap test argues *against* the candidate in the lineage that matters (REPORT §3.5).
  A framework that could not record those is one that cannot be wrong.

The practical use is small and real: a clinician handed an MVA2 diagnosis can be told, with the
sources, why the proteasome-inhibitor idea circulating for MVA does not carry to that gene — and a
clinician handed an MVA3 diagnosis can be told the opposite, together with the experiment that would
have to run first.

---

## 6. What transfers to MVA2 and MVA3 regardless of the drug verdict

The drug verdict is the part that changes. Most of the report does not:

- **Surveillance.** The 2024 consensus is explicit that renal ultrasound every 3 months from birth to
  age 7 is recommended "for all MVA conditions including those with an unknown genetic cause"
  (PMID 39264246). That includes MVA2, where no cancer has been reported in the 15 published
  individuals — a tension that belongs to the consensus, not to us, and we do not resolve it. The
  report's own **extension** — continuing clinical examination past age 7, including the orbit — was
  prompted by an **MVA3** case (Wilms at 3, orbital E-RMS at 12; PMID 42595739), so it applies to MVA3
  at least as strongly as to MVA1.
- **The endpoint.** Per-cell mis-segregation (micronucleus assay, OECD TG 487; single-cell copy number,
  PMID 25197050) is required for any of the three, for the reason computed in REPORT §5: bulk
  sequencing cannot see variegation at any depth.
- **The gene panel** (BUB1B, CEP57, TRIP13, CENATAC, MAD1L1, MAD2L1BP, CEP192, BUB1, SMC5, TRIM37,
  CENPE) is the same workup.
- **What we do not propose** (REPORT §8) is unchanged, and one entry is worth repeating for MVA3
  specifically: **DCZ0415**, an experimental TRIP13 inhibitor, remains rejected at filter 1 — it is not
  approved — and in a genotype whose cells have "no detectable TRIP13" (PMID 28553959) there is, on the
  face of it, no target left for it to inhibit — an inference of ours, not a tested result.
- **The spindle-poison caution** (REPORT §4) transfers on the same weak footing: severe SAC impairment
  is documented for *TRIP13* (PMID 28553959), and the only clinical record cited is a single case of
  rhabdomyosarcoma with PCS/MVA treated with reduced-intensity chemotherapy (PMID 31184400 — a title
  with no abstract in PubMed, not a guideline, and no gene specified in it). It is a relative
  consideration for a tumour board, never a reason to withhold curative therapy.

---

## 7. Limitations of this transfer

- **Neither sheet has a patient.** Filter 4 is patient-specific by construction, so both worksheets
  leave it undecided for want of a patient (in MVA2 it is the filter the candidate stops at, but on a
  published-cohort argument rather than one child's comorbidities; MVA3 cannot answer it in the
  abstract). A completed sheet
  requires a named child, their comorbidities and their current age.
- **The MVA2 "not evaluable at filter 2" reading rests partly on an inference**, flagged in §2 above: "minimal SAC
  deficiency" (PMID 28553959) is a checkpoint measurement, and the step to "smaller proteotoxic burden"
  is ours, not the source's. We record it as the weakest joint in this document.
- **Absence of reported cancer is not absence of risk.** Fifteen published individuals (PMID 39264246)
  is a small denominator, and the same consensus still recommends surveillance for MVA2.
- **The MVA3 filter-3 pass is inherited, not independent.** Its denominator is the generic
  aneuploidy-stratified EC50 of PMID 39247952, computed on total rather than free drug, read from a
  figure panel as a conservative upper bound — every caveat the report attaches to the MVA1 ratio
  (§3.2, §10) applies here unchanged.
- **Our own pre-registered result weakens the MVA3 case** (REPORT §3.5), and the MVA3 tumours are solid.
- **No new evidence was gathered for this document.** Every PMID above already appears in
  `REPORT_track2_EN.md` or `evidencia/fuentes_verbatim.md`. Where evidence was missing we wrote *not
  evaluable*, *not reached* or *no data* rather than searching for a substitute.

---

## Sources used (all already cited in `REPORT_track2_EN.md`)

- PMID 15475955 — Hanks S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in *BUB1B*. *Nat Genet* 2004
- PMID 16182441 — Hanks S, et al. CGH and *BUB1B* mutation analyses in childhood cancers associated with MVA. *Cancer Lett* 2006
- PMID 20516114 — Suijkerbuijk SJE, et al. Molecular causes for BUBR1 dysfunction in MVA. *Cancer Res* 2010
- PMID 21552266 — Snape K, et al. Mutations in *CEP57* cause mosaic variegated aneuploidy syndrome. *Nat Genet* 2011
- PMID 25197050 — Knouse KA, et al. Single cell sequencing reveals low levels of aneuploidy across mammalian tissues. *PNAS* 2014
- PMID 28553959 — Yost S, et al. Biallelic *TRIP13* mutations predispose to Wilms tumor and chromosome missegregation. *Nat Genet* 2017
- PMID 31184400 — Nishitani-Isa M, et al. ERMS with PCS/MVA treated with reduced-intensity chemotherapy. *Pediatr Int* 2019 (no abstract in PubMed)
- PMID 31530568 — Chui MH, et al. Chromosomal instability and mTORC1 activation through PTEN loss. *Cancer Res* 2019
- PMID 31738183 — Sieben CJ, et al. BubR1 allelic effects drive phenotypic heterogeneity in MVA. *J Clin Invest* 2020
- PMID 39247952 — Ippolito MR, et al. Increased RNA and protein degradation … in human aneuploid cells. *Cancer Discov* 2024
- PMID 39264246 — Nakano Y, Kuiper RP, et al. Update on recommendations for cancer screening and surveillance in children with genomic instability disorders. *Clin Cancer Res* 2024
- PMID 42595739 — Vempuluru VS, et al. Sequential Wilms' tumor and orbital rhabdomyosarcoma in a child with MVA3. *Orbit* 2026
- FDA label, VELCADE (bortezomib), NDA 021602 s040, §12.3
- FDA BPCA Clinical Review, bortezomib paediatric safety, NDA 021602, 2015
