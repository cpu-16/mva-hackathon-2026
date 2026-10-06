## 1. SCORE TABLE

**77/100, up from 72. Not a podium entry as submitted.** This is a judgment of submission quality; no competing entries were provided.

The previous criterion scores are preserved in the September 7 review: **27 / 15 / 18 / 12**. I checked the supplied text against selected local results, preregistrations, figure source and verification code. I did not rerun the analyses or independently verify every citation.

| Criterion | Previous | Now | Movement and justification |
|---|---:|---:|---|
| **Scientific Rigor** | 27/35 | **28/35** | **+1.** The DepMap follow-up supplies uncertainty, lineage sensitivity, assay overlap and RMS coverage. The four-parameter power analysis exposes the original design’s weakness. However, the funnel, SC exposure verdict, Appendix B and experimental stopping rules still contradict the qualified conclusions. These are substantive defects, not stylistic ones. |
| **Potential Impact** | 15/25 | **17/25** | **+2.** The experiment’s constitutional-cell interpretation is clearer, and the document identifies concrete next decisions. But fibroblast results remain an unjustified compulsory gate to tumour research; no tumour-selective benefit or comparable therapeutic exposure is established. Surveillance is useful implementation of existing guidance, not a drug-repurposing discovery. |
| **Innovation** | 18/25 | **19/25** | **+1.** The lineage analysis and explicit investigation of assay disagreement strengthen the original computational contribution. The candidate and its mechanism remain literature-derived. Claims that ordinary pharmacology and safety checks distinguish this framework from usual repurposing remain unsupported. |
| **Scalability** | 12/15 | **13/15** | **+1.** The machine-readable worksheet and build process make reuse tangible. But rebuilding PDFs from committed outputs is not full analytical reproduction, and the claim checker does not check “every reported number.” The most developed transfer demonstration still concerns variant retrieval. |
| **TOTAL** | **72/100** | **77/100** | **+5.** More evidence and better packaging, with incomplete reconciliation. |

**The five requested changes were implemented unevenly:** headline reconciliation remains incomplete; the DepMap follow-up is substantially delivered; the exposure table and narrowed experimental interpretation are delivered but contradicted elsewhere; the two-part structure exists; the candidate table exists but encodes inconsistent verdicts.

The organisers do not require a successful treatment. I am deducting for unreliable inference and inconsistent decisions, not for reporting a negative drug result.

## 2. CONTRADICTION HUNT

**The most damaging surviving sentence is Appendix B’s “the balance inverts.”** It converts a possible change in clinical context into a favourable benefit–risk conclusion. The previous review explicitly required its removal.

Page numbers below refer to the supplied PDF pagination. Quotations are exact sentences or identified excerpts; line wrapping is normalised.

| Location | Exact sentence or excerpt | What it contradicts | Fix |
|---|---|---|---|
| **Funnel, pp. 7 and 32; confirmed in figure source** | “The proteasome class survives filters 1–3 and is held as a conditional answer for a future active tumour (§4, §6)” | Carfilzomib and ixazomib are **not evaluable** at filter 3. Bortezomib IV is merely **not excluded** by one comparison. The statement improperly upgrades both the evidence and the entire class. | “Bortezomib IV is not excluded by the total-plasma peak comparison; therapeutic exposure remains unresolved. Other proteasome inhibitors lack an evaluable denominator.” |
| **I §3.2, p. 9; II §3.2, p. 37; summaries and worksheet** | “On total drug the IV ratio is 5.8–7.8; on free drug the peak (≈ 39–53 nM, or ≈ 99 nM on the 223 ng/mL figure) is within one- to 2.5-fold of the < 40 nM bound” | **40 nM is the comparison value; “<40 nM” is not a denominator.** The actual EC50 could be substantially lower. The quoted range also combines different clinical cohorts. | Report the ratios to **40 nM explicitly**, separately by cohort, and say that neither is a free-drug exposure margin. See arithmetic below. |
| **II §3.2, p. 38; both worksheets** | “A margin of 1.33 does not survive any plausible free-fraction correction.” | The same section says culture binding is unknown and rejects correcting only one side. SC total Cmax exceeds the stated EC50 upper bound, and equivalent AUC is acknowledged. These facts do not establish SC failure. | Replace SC filter 3 **fail** with **exposure unresolved**; retain the descriptive lower peak and equivalent-AUC information. |
| **II §3.1, p. 33; Appendix B Q11, p. 81** | “It fails filter 3 decisively.” / “Metformin, the candidate the literature points to, dies on filter three” | The worksheet and qualified conclusion say **not evaluable**, with no aneuploidy-selective EC50. The complex-I comparison does not disprove every proposed mechanism. | “Metformin cannot be evaluated for aneuploidy-selective exposure; the complex-I rationale also has a separate concentration mismatch.” |
| **Appendix B Q11, p. 82** | “For an MVA patient with an active malignancy — where the comparator is cytotoxic chemotherapy — the balance inverts” | I §5 and II §4 say the balance **can** invert and remains a tumour-board judgment. Active cancer alone establishes neither benefit nor acceptable toxicity. | “Active malignancy changes the comparator; whether adding bortezomib improves benefit–risk remains unestablished.” |
| **Appendix B Q2, p. 76** | “Step 1 — establish the lesion. Compound heterozygosity in BUB1B” | The title, both limitations sections and Q9 explicitly say phase is unestablished. “Establish” also overstates the uncharacterised missense allele. | “Step 1 — define the working hypothesis: two heterozygous BUB1B variants, presumed in trans; phase and missense function remain unresolved.” |
| **II §6, p. 61; family page and safety sections** | “We treat the fibroblast arm as the gate that decides whether that second stage is worth building” | The same section says a negative fibroblast result **does not close the tumour question**. Yet “Failing any of 1–3 … stops the programme.” | Give the constitutional-cell and tumour-material programmes separate decisions. Fibroblast failure stops the constitutional hypothesis, not automatically tumour investigation. |
| **I §6, p. 16; II §6, p. 60** | “the 95% confidence interval of the treated-minus-vehicle difference must exclude a relative increase of 50% of the vehicle rate” | **Excluding a threshold is directionally ambiguous.** An interval wholly above the harmful threshold also excludes it. | Require the **upper confidence bound** to be below the prespecified harm margin. Specify how uncertainty in the vehicle rate enters the calculation. |
| **II §6, p. 61** | “If bortezomib raises micronucleus frequency among survivors, that does falsify the proposal outright: it fails filter 5 regardless of how well it kills.” | The preceding operational rule tolerates increases below a 50% margin; it also requires attribution to mis-segregation. “Any increase” is a different rule. | Use one rule throughout: unacceptable harm, inconclusive safety and evidence below the chosen margin must be distinguished. |
| **Family page, p. 2; summaries, safety tables** | “It also causes nerve damage in about 18 in 100 children who receive it” | The cited **25/140** is an observed rate in a specific combination-treatment safety population, not an attributable bortezomib risk in children generally. | Identify AALL07P1, combination chemotherapy and the population; state that this child’s incremental risk is unknown. |
| **I summary, p. 4; II summary, p. 27; Appendix B Q10, p. 81** | “Eight pre-registrations were committed to git before their analyses ran” versus “The phase pilot is not one of the pre-registered five” | The supplied list totals **eight**, but Q10 retains the old count and “five pairs.” | Replace both counts with one numbered inventory of eight plans, their result files and amendments. |
| **I §4, p. 12; II §3.5, p. 44** | “all four predictions held” | The referenced local follow-up preregistration contains **P-S1 through P-S5: five predictions**, with five corresponding outcomes. | “All five listed predictions held,” with a mapping to P-S1–P-S5. Do not confuse prediction counts with preregistration counts. |
| **II §3.5, p. 45** | “Under a fraction-of-arms score the numbers are unchanged” | The follow-up table changes bortezomib from −0.075 to −0.077, carfilzomib from −0.060 to −0.054 and ixazomib from +0.028 to +0.032. | “The fraction-of-arms score produces similar estimates with unchanged signs and interpretation.” |
| **II §3.5, p. 46** | “Two measurements on overlapping models agree: the link our bortezomib argument rests on is detectable where myeloma sits and attenuated in solid tumours.” | PRISM contains **no relevant haematological drug measurements**. Only CRISPR estimates the stratum difference. The paired modalities correlate at −0.070 with a CI crossing zero. | “CRISPR supports a stratum difference; PRISM supplies a separate, non-significant solid-line drug association.” |
| **I §4, p. 11; II summary, p. 26** | “ploidy adds nothing (p = 0.88)” | Its proximity to the interaction result makes it appear to describe that model. The follow-up gives **p = 0.875 in the main-effects model**, but **p = 0.82 in the interaction model**. | Name both models and their p-values; replace “adds nothing” with “was not statistically significant.” |
| **Part II introduction, p. 25** | “Section numbers match Part I.” | They do not: II §3.5 maps to I §4; II §4 maps to I §5; II §5 is compressed into I §6. The shared funnel’s §4 safety reference is wrong in Part I. | Provide an explicit crosswalk and part-qualified links; use named sections in shared figures. |
| **I §7, p. 17; II §7, p. 63** | “The consensus asks for clinical assessment without setting an end date” / “continuing past 7 is our extension” | Continuing an open-ended recommendation is not an extension beyond a stated stopping age. The renal-ultrasound endpoint is being transferred to a different surveillance modality. | Describe the proposed **frequency and age-10 review point** as local suggestions; do not claim to extend an age limit absent from the clinical-assessment recommendation. |
| **I §9, pp. 19–20; II §9, p. 68** | “checks every reported number against the results files” | The inspected checker uses selected regex anchors. It does not comprehensively cover Part I, embedded figure text, every table or every numerical claim. | “Checks a specified subset of numerical claims”; publish coverage and extend it before claiming completeness. |

**Neuropathy source check.** The FDA review describes AALL07P1 as a single-arm study in paediatric and young-adult patients with relapsed lymphoid malignancies receiving bortezomib with intensive reinduction chemotherapy, including vincristine. The 18% figure must retain that context; it cannot be interpreted as the drug’s incremental risk. The safety concern remains legitimate. [FDA BPCA clinical review](https://www.fda.gov/files/drugs/published/21602-Bortezomib-Clinical-BPCA.pdf)

**Required numerical checks**

| Check | Finding |
|---|---|
| **Free-drug arithmetic** | Using the rounded figures: **39/40 = 0.975; 53/40 = 1.325; 99/40 = 2.475**. Write **approximately 0.98–1.33 times 40 nM**, or **2.48 times 40 nM in the separate cohort**. These are not measured free-plasma/free-medium EC50 ratios. |
| **Total-drug arithmetic** | **231/40 = 5.775; 312/40 = 7.8.** The calculations are correct against 40 nM. Because the EC50 is stated as **<40**, these are conservative reference-denominator comparisons, not an estimated interval for the actual Cmax/EC50 ratio. |
| **Power** | **0.167**, rounded to **0.17**, agrees across the current text and results. **12 cultures at f = 0.30**, **23 at f = 0.20**, and **>24 at f = 0.10** also agree. |
| **Retired power labels** | **0.897** and **0.387** are explicitly identified as original two-parameter scenarios, not current estimates. The current 2× scenario is **0.068 at n = 3**. Their continued appearance as historical results is not itself a contradiction. |
| **Eight preregistrations** | Correct arithmetic: DepMap **2**, Replay **1**, mosaicism **1**, power **2**, dose–response **1**, TRIP13 transfer **1** = **8**. Q10 is stale. This count does not establish that every amendment was prospectively committed. |
| **DepMap drug sample sizes** | **444 applies to bortezomib**, not a common complete-case set for every drug. The follow-up lists carfilzomib **424**, ixazomib **438**, metformin **438**, trametinib **441**, everolimus **441**, paclitaxel **440**. Report drug-specific n. |
| **DepMap principal estimates** | Bortezomib **ρ = −0.075**, **p = 0.11**, CI **−0.168 to +0.017**; PSMB5 overall **n = 946**, **ρ = −0.198**, **q = 5.2×10⁻⁸**. The Part I rounding to **5×10⁻⁸** is acceptable. |
| **Stratum estimates** | Haematological **n = 113**, **ρ = −0.261**, **q = 0.042**; solid **n = 833**, **ρ = −0.077**, **q = 0.118**. Totals reconcile. |
| **Interaction** | **β = −0.01675**, rounded to **−0.017**; **p = 0.0255**, rounded to **0.026**. The quoted confidence interval and ten-arm slopes reconcile. This was originally exploratory, not converted into independent confirmation by later scripting. |
| **Solid-stratum uncertainty** | The marginal Spearman bootstrap interval excludes zero, the FDR result fails, and the adjusted regression slope interval includes zero. These can coexist. “The association remains compatible with zero” must identify the **adjusted slope**, rather than blur three inferential objects. |
| **Assay overlap and RMS** | **365 shared solid models** agrees with the follow-up. RMS coverage agrees: **17 scored**, **3 drug**, **10 CRISPR**, with the stated percentiles. These are RMS collectively, not necessarily three embryonal RMS drug models. |
| **Ippolito cohorts** | The two parts consistently report **8 versus 50, p = 0.014**, and **13 versus 14, p = 0.038**, with one-tailed tests. Part II explicitly preserves the source’s comparator-label discrepancy. This is internal consistency, not independent resolution of that discrepancy. |
| **Raw reads and phase** | The former “no raw reads” contradiction is repaired: all detailed accounts acknowledge FASTQ availability and that alignment was not attempted. The remaining errors are categorical phase/causality language in Q2 and overbroad claims that phase is intrinsically unobservable. |

Two presentation defects also remain: the “one page” family introduction occupies three pages, and the extracted worksheets repeatedly truncate verdict text. The latter requires visual PDF inspection before declaring the delivered tables readable.

## 3. ATTACKABLE SENTENCES

These are additional attacks, beyond the explicit contradictions above.

| Location and sentence | Why an expert attacks it | Defensible replacement |
|---|---|---|
| **II §6, p. 55:** “What n counts: independent biological replicate cultures per arm, from separate passages on separate plates, each yielding one fitted EC50” | Separate passages and plates do not establish independence. One patient donor remains one donor; related cultures can share lineage, passage and batch effects. | “The simulations assume independent culture-level errors. Experimental cultures remain nested within donor and culture lineage; passages and plates will be recorded and modelled, and inference will be limited to the sampled lines.” |
| **II §6, p. 55:** “Power reaches 0.80 at n = 12 independent cultures per arm” | This is scenario-specific simulated power, not a validated sample size. The search used 600 simulated experiments per n, and the implemented test does not reproduce every advancement condition. | “Under the stated independent-culture scenario, the simulation first crossed estimated 80% power at n = 12; this does not establish power for the complete advancement rule.” |
| **II §6, p. 60:** “Read the criterion off this table once f is measured, and treat a shift materially below the corresponding row as a negative.” | An unsupported 4× assumption has become an efficacy threshold. “Materially” is undefined. A smaller real effect could be misclassified as absent. | “Use the table for planning sensitivity analyses only; estimate the observed shift and uncertainty without treating assumed 4× selectivity as the biological success threshold.” |
| **II §6, p. 61:** “the most likely reading is constitutional toxicity … rather than selective killing of aneuploid cells” | Cross-line sensitivity does not identify the mechanism. Constitutional toxicity and selective killing of constitutional aneuploid cells are not mutually exclusive. RPE1 is not an isogenic comparator. | “This result raises concern about constitutional-cell toxicity; the proposed comparisons cannot determine its mechanism or establish tumour selectivity.” |
| **II §6, p. 59:** “FISH separates whole-chromosome loss from breakage” | FISH for 3–5 chromosomes does not universally classify all micronuclei. Probe type and the interpretation of negative signals matter. | “Use a specified centromere/kinetochore assay to support micronucleus classification; chromosome-specific FISH provides additional information only for the chromosomes probed.” |
| **I §1, p. 6:** “our proband is alive, so if that transfers, p.Asn1002Lys must retain more function than L1012P” | Survival across species and allele combinations does not order residual function without comparable ages, backgrounds and expression. “Died prematurely” does not mean never viable. | “The mouse result motivates testing residual function of p.Asn1002Lys but does not establish its functional rank relative to L1012P.” |
| **II §1, p. 31:** “the allele-fate arm of the experiment in §6 tests it directly” | RNA fate and protein abundance do not directly test checkpoint function or compare the two missense alleles. | “The allele-fate arm tests transcript and protein stability; comparative residual function would require a checkpoint assay with an appropriate L1012P comparator.” |
| **II §3.5, p. 44:** “this is not whole-genome doubling in disguise” | A non-significant ploidy coefficient does not exclude confounding, and ploidy is not a complete measure of whole-genome-doubling history. | “The association persists after adjustment for measured ploidy in this model; residual confounding and whole-genome-doubling history remain unresolved.” |
| **II §3.5, p. 46:** “An induced-aneuploidy design is the more sensitive of the two” | No comparative power analysis establishes this. The designs estimate different effects; reversine perturbation is not interchangeable with constitutional aneuploidy. | “The within-line perturbation and cross-line observational designs address different estimands; their p-values do not establish which design provides stronger evidence for MVA.” |
| **I §4, p. 11:** “The pipeline is not blind: across 6,790 compounds 1.1% reach p < 0.001 against 0.1% expected.” | Excess small p-values can reflect real associations, confounding or calibration problems. It does not validate sensitivity for this candidate. | “The screen contains an excess of small p-values; this alone does not establish calibration or sensitivity for the prespecified proteasome-inhibitor tests.” |
| **II §5, p. 52:** “And bulk averaging erases variegation by construction, at any depth.” | The preceding paragraph expressly allows detectable asymmetric mixtures. Bulk measurements lose cellular resolution, not every aggregate signal. | “Bulk averaging loses cellular resolution and cannot identify the balanced mixture modelled here, although asymmetric mixtures may remain detectable.” |
| **I §5, p. 14; II §4, p. 49:** “Single-agent bortezomib has not shrunk a paediatric solid tumour in a trial.” | No objective responses in the cited studies is narrower than no shrinkage, and a universal claim needs an exhaustive review. | “ADVL0015 reported no objective responses in 15 children with refractory solid tumours; the cited combination study also reported none.” |
| **II §9, p. 67:** “For MVA2 bortezomib fails filter 4” | A patient-specific filter cannot be assigned from a gene label and absence of reported malignancy alone. No individual MVA2 patient is specified. | “No favourable treatment setting is established for MVA2 in this review; individual safety is not evaluable without a patient and indication.” |
| **Worksheet, pp. 74–75:** “No agent approved with a senolytic indication” | Filter 1 asks whether a drug is marketed, not whether the proposed repurposed indication is approved. A class-level failure applies a different rule. | “Assess named senolytic candidates individually for marketing approval; the cited genetic-clearance experiment does not itself nominate a validated drug.” |
| **I §7, p. 17:** “The intervention that most changes this child’s prognosis is surveillance” | The report supplies neither a patient-specific prognosis estimate nor a comparison proving this superlative. | “The clearest current clinical action supported by the cited guidance is age-appropriate cancer surveillance, reviewed by the treating team.” |

For the micronucleus assay, the distinction between fragments and whole chromosomes is fundamental to the guideline; specify the actual discrimination method rather than relying on “FISH” as a sufficient description. [OECD Test Guideline 487](https://www.oecd.org/en/publications/test-no-487-in-vitro-mammalian-cell-micronucleus-test_9789264264861-en.html)

## 4. THE THREE CHANGES WITH THE HIGHEST RETURN

The estimated movements below overlap and should not be added mechanically.

### 1. Replace the competing conclusions with one controlled conclusion

**Expected movement: Scientific Rigor +2–3; Potential Impact +0–1. Editorial effort: roughly one working day.**

Use this paragraph in both summaries, Appendix B Q2/Q11 and the closing note:

> No disease-modifying drug is supported for use in this child today. Bortezomib is a conditional research candidate: the stated IV total-plasma peak comparison does not exclude it, but comparable free exposure, duration and tumour selectivity in MVA remain unestablished. PRISM did not detect a significant proteasome-inhibitor association in the tested solid lines; CRISPR showed a weaker aneuploidy–PSMB5 association in solid than haematological lines. Active malignancy would change the clinical comparator, not establish a favourable benefit–risk balance.

Then make the associated changes everywhere:

- Remove the **class-wide filter 3 pass**, including embedded figure text.
- Replace SC **fail** with **exposure unresolved**.
- Keep metformin **not evaluable**, separating the complex-I objection.
- Replace the “1–2.5× free-drug margin” with the explicit reference-denominator arithmetic.
- Qualify phase, neuropathy population and the status of the missense.
- Preserve **filter 5 untested**.

The controlling conclusion must govern the artwork and form answers, not merely the limitations section.

### 2. Rewrite §6 as two research questions, with executable decision rules

**Expected movement: Scientific Rigor +1–2; Potential Impact +1. Effort: one editorial day, with optional CPU sensitivity analysis.**

Replace the compulsory fibroblast gate with:

> The constitutional-cell study measures drug response and potential normal-tissue vulnerability in the sampled lines. It cannot establish tumour benefit, and a negative result does not automatically stop tumour-specific investigation. Any tumour-directed proposal requires a separate comparison using relevant tumour material and normal-cell comparators.

Replace the filter 5 criterion with:

> Let Δ be the treated-minus-vehicle micronucleus rate and M the prespecified harm margin. Evidence below the margin requires the upper confidence bound for Δ − M to be below zero. An interval crossing zero is inconclusive; an interval wholly above zero indicates harm exceeding the margin.

Specify estimation of the vehicle-dependent margin, culture-level replication, proliferation and micronucleus classification.

Finally:

- Rename the 4× table **planning scenarios**, not advancement thresholds.
- State that 12 cultures is conditional simulated planning, not a validated requirement.
- Define culture ancestry, donor nesting, plate allocation and the intended unit of inference.
- If CPU work is used, add a prespecified sensitivity analysis for correlated cultures and report power for the **actual proposed decision**, not just rejection of equal EC50s. Do not claim assumed correlations are measured.

This closes the largest remaining gap between “an experiment that can fail” and an experiment whose outcomes have defensible interpretations.

### 3. Build and audit one canonical claim inventory through the final PDF

**Expected movement: Scalability +1; Scientific Rigor +0–1. Effort: one working day, no new biological analysis.**

Replace “checks every reported number” with an accurate coverage statement, then extend the checker to cover:

- Part I, Part II, Appendix B, candidate TSV and figure labels.
- Drug-specific n, effect estimates, uncertainty, correction families and model names.
- Eight preregistrations, five DepMap follow-up predictions and amendment provenance.
- Both current and explicitly retired power scenarios.
- An explicit vocabulary including **not excluded**, **not reached** and **exposure unresolved**, or a documented mapping to the chosen schema.

Change the build description to:

> Without public downloads, this command rebuilds the document from committed results. With the required inputs, it reruns the specified analyses. The log identifies which mode ran and which claims were checked.

For final acceptance, inspect the rendered funnel and every worksheet page. Resolve the truncated verdict columns, repair cross-references, and make the family page actually one page. These are defects in the delivered artifact, not matters a repository link can repair.

## 5. ONE-LINE VERDICT

**Do not ship without a unified exposure/clinical verdict and a corrected §6 decision rule; the current PDF still contradicts its own evidence at the points that determine action.**