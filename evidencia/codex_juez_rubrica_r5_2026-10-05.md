**1. SCORE TABLE**

**85/100: +1 from 84, +3 from 82, +6 from 79, +8 from 77 and +13 from 72. Not a podium entry as submitted.** That is a judgment of submission quality, not a prediction against unseen competitors.

The supplied text controls this review. I also inspected the matching 92-page PDF, its embedded figures and worksheets, the saved earlier scorecards, and selected underlying results. I did not rerun the analyses or verify every citation. Inspected PDF: :codex-file-citation{path="/home/gar16/datos/HACKATHON-MVA-2026/entrega/listo-para-enviar/ciberpty_track2_report.pdf" purpose="source"}.

| Criterion | 72 round | 77 round | 79 round | 82 round | 84 round | Now | Movement from 84 and justification |
|---|---:|---:|---:|---:|---:|---:|---|
| **Scientific Rigor /35** | 27 | 28 | 29 | 30 | 31 | **32** | **+1.** The exposure arithmetic, main DepMap denominators, residual-function qualification and status definitions are improved. However, dependency attribution survives in summaries, the RPE1 stopping rule contradicts itself, and the CEP57 transfer still changes evidentiary standards. |
| **Potential Impact /25** | 15 | 17 | 18 | 19 | 20 | **21** | **+1.** The tumour-stage proposal now supplies treatment arms, an endpoint and numerical planning thresholds. It still defers confidence-bound criteria, replication and exposure implementation. Its decision rule cannot yet be executed without substantive choices. |
| **Innovation /25** | 18 | 19 | 19 | 19 | 19 | **19** | **0.** The DepMap lineage analysis and examination of assay disagreement remain the original Track 2 contributions. Editorial corrections and conventional exposure/safety checks do not add innovation. |
| **Scalability /15** | 12 | 13 | 13 | 14 | 14 | **13** | **−1.** Status definitions improve reuse, but the latest width change physically clips the verdict columns. This is a regression from cramped but contained tables. The gene-transfer example also remains inconsistently scored. |
| **TOTAL** | **72** | **77** | **79** | **82** | **84** | **85** | **Two substantive improvements, offset by a broken deliverable.** |

I am **not deducting for recommending no treatment today**. A conditional research candidate satisfies the organisers’ stated objective. The deductions concern whether the evidence supports the proposed investigation, whether the decision rules mean what the summaries claim, and whether another team can use the delivered artefact.

---

**2. CONTRADICTION HUNT**

The controlling conclusion is consistent across the executive summaries. The claim that every previously identified contradiction was fixed is false.

Quotes below remove extraction line breaks. I distinguish direct contradictions from inconsistent standards and incomplete specifications.

| Location | Exact sentence or wording | What it contradicts | Fix |
|---|---|---|---|
| **I §10, p.23; repeated in II §10, p.80, and Q11, p.92** | “Whether the dependency transfers is exactly what §6 tests; we have not assumed it.” | I §6 and II §6 correctly say that a sensitivity difference **does not establish a proteotoxic dependency**. The proposed assay measures response and constitutional-cell vulnerability. | “Section 6 measures differential drug response and constitutional-cell vulnerability; attributing either to proteotoxic dependency requires additional mechanistic experiments.” Apply everywhere. |
| **II §4, p.54** | “Whether that dependency transfers to constitutional MVA is exactly what §6 proposes to measure…” | Same contradiction, inside the clinical rationale itself. | Replace with the same response-versus-mechanism distinction above. |
| **II §6, criterion 4, p.69; I §6 table, p.18** | “if patient fibroblasts are markedly more sensitive than controls without the aneuploidy-high positive control showing a larger shift still…” | The same paragraph says: “patient-cell toxicity is interpreted on its own, without requiring a particular ordering across cell types.” Those are incompatible decision rules. | Delete the cross-cell-type ranking condition. Define the constitutional-toxicity flag independently; RPE1 establishes assay responsiveness only. |
| **I §6 table, p.18** | “a pre-specified reading rule, not a validated threshold, recomputed if selectivity is ever estimated.” | II §6, p.68: “The primary threshold stays fixed”; recalibration using this experiment is exploratory and requires another experiment. | “The primary table remains fixed for this experiment; any recalibration is exploratory and requires prospective evaluation.” |
| **II §6, pp.68–70** | “treat a shift whose 95% interval lies below the corresponding row as a negative.” / “Each result is classified as advance, demonstrated harm or inconclusive” | A sufficiently precise result below the required response threshold is an **insufficient-benefit result**, not demonstrated harm and not necessarily inconclusive. The classification omits an outcome the preceding rule explicitly creates. | Add “insufficient response” as a distinct outcome, or explicitly nest it under “no advance” without calling it harm or uncertainty. |
| **I §5, p.16; II §4, p.56** | “each with prespecified confidence-bound criteria and replication in independently initiated culture experiments; otherwise classify the result as negative or inconclusive.” | This is presented as the specified tumour-stage decision, but the confidence criteria and replication requirement remain unspecified. It also gives no explicit harm classification when normal-cell toxicity exceeds its margin. **Specification gap, not a wrong result.** | State the estimands, confidence bounds, replication unit and advance/harm/insufficient-benefit/inconclusive mapping now. |
| **I §9, p.21; II §9, p.77** | “the aneuploidy-burden premise that carries filter 2 for MVA1 is not established for CEP57” | Filter 2 is declared to mean **mechanistic plausibility**, with disease-specific activity unestablished for every candidate. CEP57-associated mosaic aneuploidy is established; absence of proteotoxic measurements is shared with constitutional MVA1. | Apply the same plausibility standard, or name a specific additional criterion and apply it to MVA1 too. Do not substitute checkpoint severity for aneuploid burden. |
| **II §9, p.77** | “no proteasome measurement exists in CEP57 cells for filter 3” | MVA1 passes the report’s narrow plausibility screen using **generic aneuploid cancer cells**, not BUB1B-deficient cells. Requiring genotype-specific potency only for CEP57 changes the filter. | Separate the generic exposure comparison from disease-specific potency. Apply the same generic comparison to all three genes, with transfer unestablished, or require disease-specific potency for all three. |
| **I §9, p.21; II §9, p.77** | “For MVA2 bortezomib fails filter 4…” | The worksheet says filter 4 concerns **one person at one moment**. The transfer exercise provides no MVA2 patient. No reported cancers among 15 individuals does not supply a patient-specific safety assessment. | “Patient-specific filter 4 is not evaluable without a patient; the cited literature supplies no established tumour-treatment setting for this proposal.” |
| **Embedded DepMap figure, II §3.5, p.48** | “A · PRISM: 6,790 compounds, 444 solid-tumour lines” | The corrected prose gives 444 bortezomib, 424 carfilzomib and 438 ixazomib. The panel still presents a common denominator without qualification. | “PRISM: 6,790 compounds; evaluable n varies by compound.” Identify the three candidate denominators in the legend. |
| **I executive summary, p.5** | “peripheral neuropathy in 18% (25/140) of children in a trial…” | Both safety tables specify a population aged **1.0–26.8 years**. The family page now correctly says “patients”; this summary still does not. | “Peripheral neuropathy in 25/140 patients aged 1.0–26.8 years receiving bortezomib with intensive combination chemotherapy…” |
| **II §6 timeline, p.67** | “The range spans the 312 nM clinical Cmax so the advancement threshold falls inside the data.” | The controlling conclusion and exposure section explicitly deny that 312 nM is a validated clinical threshold. Criterion 2 calls it only a provisional nominal-concentration ceiling. | “The grid includes 312 nM, the provisional nominal-concentration ceiling used for this assay; this does not establish clinical exposure equivalence.” |
| **II §6 timeline, p.66** | “expanded into twelve replicate cultures per arm…” | The immediately preceding sample-size rule requires approximately **23** at f≈0.20. Expansion is written as fixed before the gating measurement that determines it. | “Establish the cultures, measure f, then select and expand the applicable provisional replication design.” Put establishment before week 1 rather than inside the “1–3” row. |
| **Appendix B Q2, p.86; worksheets** | “MPS1/TTK inhibitors and reversine fail filter 5 by construction” | Filter 5 now means excluding a **quantified increase beyond a 50% margin**, with confidence bounds. Mechanistic concern alone does not establish that quantitative outcome. | Record mechanistic opposition under filter 2; write “quantitative filter-5 margin untested” unless a separate precautionary exclusion category is defined. |
| **Q11, p.91** | “does the micronucleus increase among survivors exceed a prespecified harm margin?” | The operational requirement is to **exclude** an increase exceeding the margin. Failure to demonstrate excess harm is not evidence below the margin. | “Can an increase beyond the prespecified micronucleus harm margin be excluded?” |
| **Worksheet introduction, pp.24 and 81** | “the table below and the machine-readable file are the same object.” | They share a source, but the rendered PDF hides substantial verdict text. Pages **25, 82 and 83** run beyond the right page boundary. This is visible in the PDF, not merely an extraction artefact. | Fix the page-content origin and table width, regenerate, then inspect every worksheet page. Source identity does not establish delivery fidelity. |

The CEP57 objection is substantive. The cited original study reports numerical chromosome abnormalities in approximately **25–50% of examined cells**. That establishes an aneuploidy premise, although it does not establish proteasome dependency. The report must not conflate those two claims. [Snape et al., original CEP57 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3508359/)

**Requested checks that do reconcile—or require a narrower qualification**

| Check | Finding |
|---|---|
| **(a) Funnel: “the proteasome class survives filters 1–3”** | **Fixed in the inspected PDF.** The embedded figure now singles out bortezomib IV as not excluded by the total-plasma comparison and labels other proteasome inhibitors not evaluable. Do not resurrect this old criticism. |
| **(b) “1–2.5×” arithmetic** | **Fixed as reference-value arithmetic.** 231–312 nM ×0.17 gives 39.3–53.0 nM; division by 40 gives 0.98–1.33. The higher cohort gives approximately 99 nM, or 2.5×40 nM. These are not free-plasma/free-medium therapeutic margins. An EC50 upper bound is not a measured EC50. The current detailed wording acknowledges both limitations. |
| **(c) Power** | **Numerically consistent.** 0.167 rounds to 0.17; approximately 12 cultures at f=0.30 and 23 at f=0.20 agree with the cited simulation. The 0.897 and 0.387 values are explicitly historical two-parameter results. The remaining problem is decision coverage: these calculations power rejection of equal EC50s, not the full advancement rule. |
| **(d) Neuropathy** | 25/140=17.86%; 11/140=7.86%. Total and motor endpoints now reconcile. Combination treatment, vincristine and unknown attributable risk are correctly stated in the safety tables. “Children” on p.5 remains inaccurate for the full age range. |
| **(e) Eight pre-registrations** | **The list contains eight:** DepMap; DepMap follow-up; MVA-Replay; mosaicism; original power; four-parameter power; dose–response; TRIP13 transfer. The phase pilot is correctly excluded. This count does not establish that every amendment preceded its analysis: the local four-parameter results explicitly disclose one amendment committed with the results. Preserve that provenance qualification. |
| **(f) Phase and raw reads** | The title, variant sections and Q9 consistently qualify presumed trans phase. The document now correctly acknowledges distributed raw reads and that they were not aligned. However, “short reads could not have phased…in any case” exceeds an assessment of the **called markers** and ordinary fragments. Write that those evaluated routes did not establish phase. |
| **(g) DepMap** | The prose reconciles: PRISM n=444/424/438; CRISPR 946=833+113; PSMB5 overall ρ=−0.198; solid −0.077; haematological −0.261; q=5×10⁻⁸ versus 5.2×10⁻⁸ and q=0.12 versus 0.118 are rounding. Interaction β≈−0.017, p=0.026 matches the result file. Shared models=365, cross-assay ρ=−0.070. RMS=17 scored, 3 drug, 10 CRISPR. The remaining denominator defect is the embedded figure. |
| **Other numerical checks** | The 314-residue loss and predicted 736-residue translated product agree. The 14% versus 2.07% detection limits are now distinguished by statistic and assumptions. The adjusted solid slope’s interval crossing zero does not contradict the marginal Spearman interval excluding zero or the failed FDR test. |
| **References and form length** | The Part I/II section map is coherent. Q11 is approximately **499 whitespace-delimited words**, leaving essentially no room for added qualifications without cuts. The “Figure 1” reference in II §5 would be clearer if its caption actually carried that number. |

---

**3. ATTACKABLE SENTENCES**

These are additional vulnerabilities in inference, execution or presentation. Some overlap the contradictions because those are the sentences an expert will actually quote.

| # | Location and wording | Why a domain expert attacks it | Defensible replacement |
|---|---|---|---|
| **1** | **I §2 / II §2:** “Five filters, not two”; “The first two are the ones every exercise asks…” | Exposure, toxicity and disease-worsening checks are not methodological inventions. The comparison caricatures ordinary repurposing practice. | “We organise this assessment around five explicit evidence questions.” |
| **2** | **II executive summary, p.29:** “It fails on pharmacokinetics…” | This headline collapses missing aneuploidy-selective potency into demonstrated pharmacokinetic failure. | “Its aneuploidy-selective exposure cannot be evaluated; a separate concentration mismatch weakens the proposed complex-I mechanism.” |
| **3** | **I §3.1 / II §3.1:** “What the micromolar-versus-millimolar gap rules out is the complex I route at plasma concentrations.” | The report itself cites an unresolved mechanistic literature. A plasma-versus-isolated-mitochondria comparison does not settle every tissue or intracellular mechanism. | “This comparison does not support the proposed complex-I mechanism at therapeutic plasma concentrations; it is not a complete intracellular exposure model.” |
| **4** | **II §3.3, pp.45–46:** “It was pre-blocked…as a mechanism-unrelated comparator…” | Trametinib is now classified as mechanistically plausible. The historical designation needs an explicit admission that the biological interpretation changed. | “Trametinib was prespecified as a comparator; subsequent literature review made its ‘mechanism-unrelated’ label inappropriate. We retain its original analysis and report the revised rationale.” |
| **5** | **I §3.3 / II §3.3:** “the gap most worth closing” | No comparative analysis establishes that priority, while the tumour-stage section disclaims a basis for ranking candidates. | “An unresolved candidate for which an absolute potency estimate would permit the next exposure comparison.” |
| **6** | **II §3.5, p.49:** “The pipeline is not blind…” | An excess of small p-values can reflect genuine associations, confounding or miscalibration. It does not validate these particular tests. Part I already says this better. | “The screen detects associations overall; this does not establish calibration or sensitivity for the prespecified proteasome-inhibitor tests.” |
| **7** | **II §3.5, p.49:** “validated against lines whose biology is independently known” | Separation between MSI and CIN groups is a plausibility check, not full validation of the score. | “The score showed the expected group-level difference between the selected MSI and CIN controls.” |
| **8** | **I §4 / II §3.5:** paclitaxel “argues against…a ‘sick cells die more’ confound.” | One drug’s opposite association does not control shared confounding across drugs and lineages. | “Paclitaxel showed an opposite association; this is a descriptive comparator, not a general confounding control.” |
| **9** | **II §3.5, p.52:** “the association is carried by haematological lines” | The solid point estimate is also negative; its marginal interval excludes zero. “Carried by” overstates exclusivity. | “The association is stronger in haematological lines under the interaction model; evidence within solid lines depends on the estimand and inferential procedure.” |
| **10** | **II §4, p.54:** “a proteasome inhibitor is not an exotic addition” | Approval in other indications does not make addition to an MVA tumour regimen clinically routine. | “Approval in other indications supplies pharmacology and toxicity information, but does not establish benefit in this combination or disease.” |
| **11** | **I §5 / II §4:** “ADVL0015: 0 of 15” | The abstract reports 15 enrolled and 11 assessable. It does not justify silently treating 15 as a response-evaluable denominator. | “ADVL0015 enrolled 15 patients and reported no objective responses; the abstract identifies 11 assessable patients.” |
| **12** | **II §4, p.55:** “concentrations below the paediatric Cmax… the paediatric dose and toxicity profile are established” | The report’s main quantitative exposure comparison is the adult label at 1.3 mg/m²; the cited solid-tumour phase I dose is 1.2 mg/m². The bridge needs a paediatric PK source and bounded language. | “RMS cultures showed nanomolar sensitivity; a small paediatric phase I trial identified a recommended dose and observed toxicities. Exposure equivalence for the proposed schedule remains unresolved.” |
| **13** | **II §6, p.61:** “A cell is under proteotoxic load whichever chromosome it gained…” | Chromosome identity, gain versus loss, dosage compensation and adaptation can matter. The subsequent dose analysis itself says burden matters. | “The mixture model treats aneuploid cells as a sensitive subpopulation; chromosome identity, direction and burden remain unmodelled sources of heterogeneity.” |
| **14** | **II §6, p.64:** “the required n grows past what a biopsy-derived culture can supply” | The simulation did not establish a biological maximum culture yield. | “Under the current model, replication exceeds the proposed practical limit; below this fraction we would redesign around a per-cell endpoint.” |
| **15** | **II §6, p.67:** “Micronucleus assay…on survivors of every condition” | Highly cytotoxic or strongly cytostatic conditions may not yield an interpretable assay. Recording proliferation alone does not supply acceptance criteria. | “Score micronuclei only under prespecified proliferation, cytotoxicity and assay-validity criteria; classify unevaluable conditions as inconclusive.” |
| **16** | **II §6, p.69:** “among survivors” as the safety population | Survivor conditioning can hide damage in cells that died or failed to divide. This endpoint does not establish overall normal-tissue safety. | “The endpoint estimates micronucleus frequency among evaluable dividing survivors and cannot exclude injury in lost or non-dividing cells.” |
| **17** | **II §7, p.74:** “It is cheap, it can be done this month…” | Cost, access, consent, laboratory validation and scheduling were not established. | “Parental segregation and, where available, PCS testing are proposed for discussion with clinical genetics; local cost and turnaround are unknown.” |
| **18** | **II §10 / Q9:** “nothing in the sequence data weighs one over the other” | Raw reads were not examined and phasing alternatives were not exhaustively assessed. | “The evaluated VCF markers and reference-panel analysis did not establish cis or trans phase.” |
| **19** | **Q11, p.91:** “mTOR inhibitors would antagonise, not synergise” | The cited study did not test rapalogues; the full report properly labels this an inference. | “We predict antagonism from the cited mechanism; the rapalogue combination remains untested.” |
| **20** | **Q11, p.88:** “Loss of function, with the druggable target displaced downstream of the lesion.” | This unqualified opening precedes unresolved phase and an uncharacterised missense VUS. | “Working hypothesis: impaired BUB1B function, with a candidate drug target downstream; phase and the missense allele’s functional effect remain unresolved.” |

For item 11, the enrolment/assessability distinction comes directly from the [ADVL0015 abstract](https://pubmed.ncbi.nlm.nih.gov/15570082/). For items 15–16, the proposed acceptance rules should be reconciled with the actual [OECD TG 487 requirements](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/test-no-487-in-vitro-mammalian-cell-micronucleus-test_g1g6fb2a/9789264264861-en.pdf), including proliferation and cytotoxicity constraints.

---

**4. THE THREE CHANGES WITH THE HIGHEST RETURN**

**1. Reconcile the decision claims and apply one evidence standard across genes.**

**Expected movement: Scientific Rigor +1–2; protects Scalability. Editorial work.**

Make these exact replacements across Part I, Part II, Appendix B, figures and the linked transfer worksheet:

- Replace every “§6 tests whether dependency transfers” sentence with:  
  **“Section 6 measures differential drug response and constitutional-cell vulnerability; mechanistic attribution and tumour selectivity require separate experiments.”**
- Delete the RPE1 response-ranking condition from both stopping-rule versions.
- Make the primary mixture threshold fixed; make recalibration exploratory.
- Replace the Q11 filter-5 question with the exclusion-of-harm formulation.
- Separate **generic exposure plausibility**, **disease-specific activity**, and **patient-specific suitability** in the MVA transfer.

For the transfer, the defensible result may be that several filters have the **same status** across genes. That is acceptable. Do not manufacture different verdicts by requiring CEP57-specific evidence that you waive for BUB1B and TRIP13.

Also update the linked transfer artefact itself. The inspected local copy still contains older “passes 1–3”, “inverting condition” and blanket bulk-sequencing claims. Label any historical version as historical; a report cannot claim a corrected transferable product while pointing to an incompatible one.

**2. Finish the tumour-stage decision rule and simulate the actual constitutional advancement rule.**

**Expected movement: Potential Impact +1–2; Scientific Rigor +0–1. One editorial day plus bounded CPU work.**

Replace the current deferred “prespecified confidence-bound criteria” sentence in **I §5 / II §4** with an operational definition.

For example, define:

- \(K_{m,a}\): vehicle-normalised loss of viable-cell recovery in material \(m\), treatment arm \(a\), at one fixed washout endpoint.
- \(\Delta_m=K_{m,\text{standard+bortezomib}}-K_{m,\text{standard}}\).
- \(D_j=\Delta_T-\Delta_{N_j}\), for each normal comparator.

Then state:

> “Advance to further preclinical investigation only if the simultaneous lower confidence bound for \(\Delta_T\) exceeds 20 percentage points, both lower bounds for \(D_j\) exceed 10 points, and both upper bounds for \(\Delta_{N_j}\) remain below 10 points. A normal-comparator lower bound exceeding 10 points is a harm result. A tumour-effect upper bound below 20 points is insufficient benefit. Remaining or technically invalid outcomes are inconclusive. These are provisional design thresholds, not clinical decision thresholds.”

Specify the confidence procedure, culture-level resampling unit, actual replication requirement, endpoint time and exposure-schedule qualification. If incremental tumour–normal separation is used, acknowledge that the separation threshold partly duplicates the tumour-benefit and normal-harm constraints.

For **§6**, simulate the complete advancement event, including two control comparisons, the mixture threshold, correlated culture effects and the micronucleus criterion. Report advance, harm, insufficient-response and inconclusive frequencies.

The crucial issue is mathematical: **detecting a nonzero EC50 difference with 80% power does not give 80% probability of clearing a minimum-effect threshold**. At a true effect exactly equal to that threshold, increasing n does not make threshold-crossing likely enough merely by improving precision. The present n≈12 calculation cannot support the complete rule.

If that simulation cannot be completed, retain the equal-EC50 calculation but remove any implication that it sizes the full protocol.

**3. Repair the actual PDF geometry and make the final document shorter to audit.**

**Expected movement: Scalability +1; protects the other scores. Half a day.**

The worksheet content starts roughly **205 points from the left edge** of an approximately **842-point-wide** landscape page and runs off the right edge. This is a positioning-and-width error. Another orientation change will not fix it.

Required output:

- All seven columns visible on pp.25 and 82–83, with complete verdicts.
- Landscape-specific margins and a table width constrained to the available content area.
- Repeated headers and intact candidate rows.
- F1–F5 with a concise legend; detailed rationale can follow as keyed notes if necessary.
- Figure text inspected at ordinary reading size.
- The DepMap panel’s common “444” denominator corrected.

Use the regained editorial space to remove repeated accounts of prior mistakes from Part I. Keep the correction history in Part II or the repository. The decision document currently spends too much of its length describing how the team repaired earlier drafts.

---

**5. ONE-LINE VERDICT**

**Ship after fixes in (2), including the clipped worksheets and contradictory decision rules; the current PDF is not ready for the final submission.**