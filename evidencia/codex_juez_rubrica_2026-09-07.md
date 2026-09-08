## 1. SCORES

**Provisional panel score: 72/100 — top third, with a plausible Innovation/Community Award case; not yet a podium contender.** This assessment uses only the supplied report. The repository, cited papers, preregistrations and video have not been independently inspected, and the rubric supplies weights without detailed scoring anchors.

| Criterion | Score | Justification |
|---|---:|---|
| **Scientific Rigor** | **27/35** | §3.5 reports evidence weakening the nominated mechanism, §5 withdraws an uninterpretable patient result, and §6 identifies defects in its own power model: these are substantial strengths. However, conclusions still exceed those qualifications: “the balance inverts” (§4), “with ploidy excluded as a confounder” (executive summary), and “no feasible n rescues it” (§6). The pharmacokinetic filter remains an exposure plausibility screen, while the fibroblast experiment cannot establish the tumour benefit motivating the proposal. |
| **Potential Impact** | **15/25** | The family-facing explanation, patient-specific safety assessment (§4), surveillance discussion and segregation request (§7) offer concrete value. But the principal drug is unsuitable today, the entry’s public-data analysis does not establish the relevant solid-tumour association, and the proposed experiment does not measure tumour selectivity. Consensus surveillance is valuable implementation work, but it is not an original drug-repurposing result. |
| **Innovation** | **18/25** | The strongest originality lies in the prospective challenge to the preferred candidate (§3.5), the balanced-mixture identifiability argument (§5), and the explicit attempt to distinguish dependency from constitutional toxicity (§6). The five-filter framework is useful, but the entry supplies no support for presenting pharmacokinetics and patient safety as unusual additions to repurposing. The drug nomination itself follows the cited literature rather than discovering a new relationship. |
| **Scalability** | **12/15** | The worksheet, gene-specific transfer exercise and documented fresh-clone replay (§9) make reuse more concrete than a generic scalability claim. However, the most operationally demonstrated tool concerns variant retrieval rather than drug repurposing, and the framework’s mis-segregation filter is not literally applicable to “any rare disease.” The supplied text does not demonstrate a comparably complete, portable Track 2 analysis workflow. |

A winning computational entry would not need to manufacture a positive drug result. It would need a sharply defined treatment setting, reliable evidence matched to that setting, reproducible analysis, defensible exposure reasoning, and an explicit explanation of what changes the next decision. This entry has unusually good ingredients for that standard, but its central narrative still tries to preserve a “prepared answer” after its evidence has reduced that answer to a research question.

The likely placement is necessarily qualitative: no competing entries were supplied. The patient-centered framing and reusable negative findings could support the discretionary award, but honesty earns its greatest scientific credit when it changes the conclusion consistently across the report.

## 2. THE FIVE CHANGES WITH THE HIGHEST RETURN

Point estimates below are judgment calls, overlap, and should **not** be added mechanically. All proposed work is editorial or uses public data and CPU compute; none requires patient access or a laboratory before 24 October.

### 1. Reconcile every headline with the actual evidence

**Exactly what to change**

Create a claim ledger with: exact sentence, source/result location, analysis population, evidence status, permissible interpretation, and every place the claim appears. Audit the family page, executive summary, tables, closing note, Appendix B and pitch script against it.

Use one controlling conclusion throughout:

> No disease-modifying drug is supported for use today. Bortezomib remains a conditional research candidate, with an order-of-magnitude total-plasma exposure comparison but no established therapeutic exposure or tumour selectivity in MVA. Our public-data analysis found an attenuated target association in solid tumours and no significant proteasome-inhibitor association in the tested drug screen.

Specific repairs:

- Change “compound heterozygosity” to **presumed compound heterozygosity; phase unconfirmed**, including the title and §1 opening.
- Describe metformin as **not evaluable for aneuploidy-selective activity**, with a separate complex-I exposure objection. Remove “cannot work.”
- Replace “the balance inverts” with **an active malignancy changes the clinical comparator; net benefit remains unestablished**.
- Replace “clears the pharmacology” with **is not excluded by the stated total-plasma peak comparison**.
- Mark filter 5 **untested**, including in the worksheet. “No evidence it increases” is not a pass.
- Resolve §1’s “no predictor was run” against Appendix B’s REVEL and AlphaMissense values: distinguish retrieved scores from locally executed prediction if that is what occurred.
- Resolve the raw-read contradiction: §5 acknowledges distributed FASTQ; §10 and Appendix B claim no read-backed phaser can be run. State what was unavailable in the analysed VCF and what was not attempted; do not promise that alignment would establish phase.
- Separate the access-controlled challenge dataset from public inputs in Appendix B Q6/Q7.

**Rubric movement:** Scientific Rigor **+3–5**; Potential Impact **+0–1** through clearer decisions.

**Effort:** **8–12 hours.**

**Risk:** The submission sounds less triumphant. That is preferable to giving a judge another sentence contradicted by the entry itself. This change has value regardless of any new analysis result.

### 2. Strengthen §3.5 around a precise, clinically relevant question

**Exactly what to change**

Make this the main original Track 2 result. Before additional analysis, freeze a dated plan explicitly described as a **follow-up informed by the existing results**, not an untouched confirmatory test.

Using the existing public-data pipeline:

1. Report the actual matched sample size, effect estimate and uncertainty for each nominated drug. Define the response direction and each FDR correction family.
2. Report the interaction coefficient and confidence interval, not just interaction \(p=0.026\).
3. Examine within-solid-lineage associations where sample sizes permit, then assess whether the pooled result is driven by lineage composition. Include a leave-one-lineage-out sensitivity analysis.
4. Inventory rhabdomyosarcoma representation and annotation quality. If sufficient material does not exist, make that a named coverage limitation rather than treating all solid cancers as the patient’s lineage.
5. Check whether the drug and CRISPR analyses share models or copy-number inputs. Call them **different assay modalities**, not statistically independent replications without justification.
6. Show sensitivity to a small, prespecified set of reasonable aneuploidy-score choices and available covariates. Do not search specifications until a drug becomes significant.

Deliver one figure with effect sizes and intervals, one compact results table, and an explicit decision statement. If the relevant stratum remains weak or uninformative, the nomination stays exploratory.

**Rubric movement:** Scientific Rigor **+2–4**; Innovation **+1–2**.

**Effort:** **14–22 hours**, assuming the reported pipeline runs.

**Risk:** Small subgroup sizes, missing annotations and correlated predictors may prevent a sharper conclusion. Report that outcome; a rigorously delimited negative result is more useful than a rescued \(p\)-value.

### 3. Replace the binary PK “pass” with an exposure evidence table, and narrow the experiment’s decision

**Exactly what to change**

For bortezomib, tabulate:

- Assay model, medium, exposure duration and how the figure-derived EC50 bound was obtained.
- Label population, route, dosing context and total-plasma peak interval.
- Available protein-binding and pharmacodynamic information, with missing quantities explicitly marked.
- Which comparisons are supported and which cannot establish comparable free exposure or duration at the target.

Do not “correct” only the clinical concentration for binding while leaving the culture concentration unexplained. Do not infer subcutaneous failure from peak concentration alone while acknowledging persistent pharmacodynamic inhibition for IV dosing.

Then edit §6 as a **future research protocol**, with separate decisions:

- Constitutional fibroblasts: dependency transfer and potential normal-tissue vulnerability.
- Tumour-derived material: the unsatisfied requirement for a tumour-treatment claim.

A fibroblast result cannot be a compulsory gate to the tumour programme while a negative fibroblast result explicitly does not close the tumour question.

For the CPU power analysis, either implement the promised four-parameter model with biological variability and fitting failures, or retire the numerical sample-size branches from the main body. Specify what \(n\) counts. Preserve the existing optimistic results and deviations in the appendix.

Keep 4× selectivity as a scenario, not the biological threshold for success. Replace “no increase in micronuclei” with a future decision criterion that acknowledges uncertainty and an interpretable assay response; the current wording does not say how an increase would be excluded.

**Rubric movement:** Scientific Rigor **+2–3**; Potential Impact **+1–2**.

**Effort:** **12–18 hours.**

**Risk:** Public information may not establish comparable exposure. The correct output could be “exposure plausibility unresolved.” That is more defensible than retaining a clinical-looking pass/fail threshold.

### 4. Deliver a 14-page decision document and a consistent three-minute pitch

**Exactly what to change**

Use the structure below. Put §3.5 by page 5, §7 by page 9 and §9 by page 10. The current “one page” family summary occupies four extracted pages; make it an actual page.

Reduce repeated correction narratives in the main body to the corrected conclusion plus an appendix pointer. Preserve the full correction history, withdrawn findings and failed controls in an indexed appendix.

Allocate the pitch approximately as follows:

- **25 seconds:** clinical question and no-drug-today conclusion.
- **40 seconds:** candidate evidence and exposure boundary.
- **50 seconds:** the original public-data result that weakens the candidate.
- **40 seconds:** patient safety and what remains unresolved.
- **25 seconds:** transferable deliverable and next research decision.

Use the same approved sentences from the claim ledger in the pitch. There is no live Q&A to repair a misleading shorthand.

**Rubric movement:** Potential Impact **+1–2**; Innovation/Scalability **+0–1 each**, by making existing contributions assessable. This is communication credit, not new biological evidence.

**Effort:** **8–12 hours.**

**Risk:** Excess compression could hide the limitations. Counter it with a visible limitation beside every main result, not a blanket disclaimer at the end.

### 5. Make the scalable product demonstrably Track 2-specific

**Exactly what to change**

Package the drug evidence worksheet and §3.5 analysis as the primary reusable product:

- A machine-readable candidate table with **pass / fail / untested / not evaluable**, model context, source locator and reason.
- A CPU command that regenerates the principal public-data figure and table.
- A fresh-environment run recording dependencies, runtime, memory, missing inputs and failures.
- A rendered report generated from the same evidence table used in the PDF.

Keep the MVA2/MVA3 transfer exercise, but distinguish **different evidence availability** from evidence that the drug works differently. Reframe filter 5 generically as **does treatment worsen the disease-relevant defect or create harmful selection?**, with mis-segregation as the MVA implementation.

Move the Exomiser replay to a secondary appendix: it is useful, but it does not demonstrate portability of drug evaluation.

Add a precise data-handling inventory matching the supplied rules: challenge-derived data in every environment, deletion within 30 days of actual close, and confirmation by email. Do not present public repository persistence as permission to retain patient-derived intermediate datasets. The supplied embargo clause is incomplete, so do not invent its remaining conditions.

**Rubric movement:** Scalability **+1–2**; Innovation **+0–1**.

**Effort:** **10–16 hours.**

**Risk:** Packaging can reveal missing dependencies or unavailable redistribution rights. Record those restrictions and provide acquisition instructions rather than bundling data indiscriminately.

## 3. A PROPOSED STRUCTURE

**Target: 14 pages, approximately 4,300–4,800 words including table text.** Retain the current section numbers for traceability, but use more informative headings.

“Verbatim appendix” should mean a clearly dated historical record. Known errors must not reappear as current instructions simply because they were moved unchanged. Place a correction notice immediately before affected archived material.

| Pages | Current material | Main-body treatment | Appendix or cut |
|---|---|---|---|
| **1** | Family summary | **Stay; 350 words.** No drug today, why, care-team discussion points, unknown age, and what remains uncertain. | Move the current version verbatim to the dated submission archive. |
| **2** | Executive summary; §§1–2 | Executive summary **200 words**; §1 **180 words**; §2 **170 words** plus compact filter table. State unconfirmed phase and VUS immediately. | Move full structural analysis, ClinVar census and mouse comparison verbatim to a variant-evidence appendix, with current interpretations flagged. |
| **3–4** | §§3.1–3.4; §8 | §3.1 **220 words**; §3.2 **330**; §3.3 **180** plus candidate table; §3.4 **150**; §8 **100**. Preserve every exclusion and every “not evaluable” result. | Move full literature discussions and detailed source extracts verbatim. Cut repeated rhetorical claims about competing teams and usual practice. |
| **5–6** | §3.5 | **Stay prominently; 600 words**, one figure and one results table. Include sample sizes, correction scope, lineage interaction, null drug results, assay differences and limitations. | Move the present §3.5 verbatim into the dated analysis record; add follow-up methods and outputs separately. |
| **7** | §4 | **Stay; 300 words** plus safety table. Define current non-use and the still-unresolved active-tumour setting. | Archive full current text verbatim. Remove unsupported clinical contraindication language from the current account. |
| **8** | §§5–6 | §5 **200 words**; §6 **320 words** plus a small decision diagram. Preserve non-identifiability, withdrawn patient result, failed external control, model assumptions, toxicity ambiguity and timeline/ethics dependencies. | Move both existing sections verbatim to dedicated appendices, with a front-page correction/status index. Keep every simulation result, protocol deviation and stop condition accessible there. |
| **9** | §7 | **Stay; 430 words.** Separate consensus, treating-team discussion proposals and unvalidated additions. Preserve unknown age, phase limits, two-family evidence and the distinction between segregation and pathogenicity. | Move surveillance derivation, full primer narrative and laboratory request details to a clinical-discussion appendix. |
| **10** | §9 | **Stay; 320 words** plus transfer table. Lead with the actual Track 2 package and distinct MVA-gene uncertainties. | Move replay implementation and TRIP13 benchmark narrative verbatim to a Track 1 transfer appendix. |
| **11** | §10; closing note | §10 **350 words**, organized as unresolved questions and their consequences. Closing note **60 words**, retaining family respect without claiming a prepared treatment answer. | Preserve full current limitations and closing text in the historical archive. |
| **12** | Five-filter worksheet | **Stay as a one-page usable artifact**, with status vocabulary and corrected worked examples. | Archive original worksheet verbatim. |
| **13–14** | References; acknowledgement; data availability | Retain all references needed by the main text; concise acknowledgement and explicit data-handling statement. | Put extended source verification and duplicate acknowledgements in the archive. |

### Appendix map

- **Appendix A — Evidence and claim ledger:** current authoritative wording, sources, result paths and correction index.
- **Appendix B — Required methods form:** retain Q2–Q11, correcting contradictions before submission. Preserve the supplied version verbatim in the historical appendix; the official current form must agree with the report.
- **Appendix C — Variant and phase evidence:** full §1 detail, phase limitations and segregation design.
- **Appendix D — Drug evidence:** full §§3.1–3.4, exclusion rationale, exposure arithmetic and source extraction.
- **Appendix E — Public-data analysis:** §3.5, original preregistration/amendments, current follow-up plan and all results.
- **Appendix F — Mosaicism:** full §5, both detection-limit approaches, failed calibration, failed control and withdrawal.
- **Appendix G — Future protocol and power:** full §6, every assumption, deviation, scenario and correction.
- **Appendix H — Clinical discussion material:** full §7 and the clinician-adaptable segregation request.
- **Appendix I — Transfer and operational reproducibility:** full §9 detail, including Exomiser replay.
- **Appendix J — Dated submitted-text archive:** the supplied version verbatim, explicitly superseded where corrected.

**Cut from the current narrative:** repeated “before a reviewer does” framing, speculative claims about competitors, unsupported novelty slogans, duplicate acknowledgements, and repeated explanations of the same historical correction. **Cut no unique limitation or negative result.**

## 4. WHAT NOT TO TOUCH

- **“No drug should be started for this today.”** Keep it prominent. It is the clearest patient-facing conclusion.
- **The negative §3.5 results.** Keep the null drug screen, ixazomib’s opposite direction, weak solid-tumour association and interaction result visible. Do not replace them with percentile enthusiasm.
- **The withdrawal in §5.** “Our attempt to measure it did not produce an interpretable answer” is stronger science than an invalid clinical negative.
- **The distinction between constitutional sensitivity and therapeutic selectivity.** §6’s admission that fibroblast sensitivity could indicate systemic toxicity is essential.
- **The missing denominators.** Preserve “not evaluable” for candidates without a suitable concentration measurement. Empty cells are a legitimate result.
- **The genetic boundaries.** Unconfirmed phase, the different ClinVar nucleotide substitution, unknown allele fate and the fact that trans does not establish pathogenicity must remain.
- **The gene-specific caution.** Keep MVA2 distinct from MVA1/MVA3 and preserve the limitation that the published MVA2 observations do not establish zero cancer risk.
- **The provenance trail.** Preserve amendments, deviations, failed primer design and provisioning failures. Edit their placement, not their existence.
- **The family-first tone.** Preserve directness and respect. Remove promises of readiness, not the reason the team cared enough to do the work.

## 5. STATEMENTS A HOSTILE JUDGE WOULD ATTACK

These are attacks on what the supplied text establishes, not externally verified corrections to its cited literature.

| Quoted statement | Likely attack |
|---|---|
| **“The proband is compound heterozygous in BUB1B”** (§1) | Your own §10 says phase is unestablished. Why is the foundational genotype presented as demonstrated in the opening? |
| **“the one route proposed for it”** (family summary) | §3.1 explicitly discusses a separate, untested AMPK-mediated possibility. The family summary removes a distinction the scientific text says is decisive. |
| **“roughly a thousand times more drug than a person can safely take”** (family summary) | Your calculation compares concentration ranges in different settings; it is not a dose-escalation or maximum-safe-dose calculation. You have translated a concentration objection into an unsupported dosing claim. |
| **“the link weakest in the kind of tumour he had”** (family summary) | You report a pooled solid-versus-haematological comparison, not an embryonal-rhabdomyosarcoma-specific ranking. “Weakest” and “the kind” imply more specificity than the analysis supplies. |
| **“We then tested that leap ourselves, and it did not survive.”** (executive summary) | The preceding leap is from cancer to constitutional MVA. You analysed cancer cell lines, so you did not test that transfer directly; you tested part of the cancer-context generalization. |
| **“with ploidy excluded as a confounder”** (executive summary) | An adjusted association and a nonsignificant ploidy coefficient do not exclude confounding, measurement error or model misspecification. |
| **“Bortezomib clears the pharmacology.”** (§4) | You acknowledge unknown free exposure, tissue exposure and relevant duration. Your own definition supports only a limited peak-concentration plausibility comparison. |
| **“The subcutaneous route does not pass”** (§3.2) | Why does a total-peak filter become binding-adjusted here but remain total-drug for IV? Where is the matched culture-exposure correction, and how does persistent inhibition enter either decision? |
| **“the balance inverts”** (§4; Appendix B) | Active cancer changes the comparator; it does not establish net benefit. What evidence supports benefit for this tumour, with this toxicity profile, in addition to or instead of which regimen? |
| **“This is a relative contraindication”** (§4, spindle poisons) | You have escalated a mechanistic concern and a case title into clinical contraindication language. The report supplies no clinical evidence sufficient for that designation. |
| **“its git timestamp is the evidence”** (§3.5) | A repository timestamp documents a record but does not alone prove hypotheses preceded access to outcomes. Show the public chronology, frozen inputs, analysis history and deviations without claiming more than those records demonstrate. |
| **“Paclitaxel … runs opposite, so this is not a ‘sick cells die more’ confound.”** (§3.5) | One drug with different biology does not exclude general fitness, lineage composition or other response confounding across the nominated compounds. |
| **“Solid lines are the larger stratum, so this is attenuation, not low power.”** (§3.5) | Sample size alone cannot establish adequate power. The interaction supports a difference under the fitted model; it does not establish precise absence of a clinically meaningful solid-tumour effect. |
| **“which is a worse position for the assay than the 14% figure suggested, not a better one”** (§5) | A lower detection limit improves nominal sensitivity under its assumptions. This sentence reverses the comparison and undermines confidence in the surrounding interpretation. |
| **“so his value is not anomalous in size”** (§5) | You have just established that the controls are not comparable. Being below an invalid comparison envelope does not establish normality, even if you subsequently disclaim a clinical negative. |
| **“below 0.10 … no feasible n rescues it”** (§6) | You have not defined feasibility or demonstrated that claim across effect sizes and biological variability. Your reported model supports scenario-specific loss of power, not this universal boundary. |
| **“A shift materially above it is not a better result”** (§6) | The table assumes unmeasured 4× selectivity. A larger shift could reflect stronger selectivity as well as toxicity or model failure; your assumed effect cannot adjudicate those explanations. |
| **“N+/C− band implies truncation; loss of both implies NMD”** (§6) | Those protein-band patterns alone do not uniquely identify transcript fate. Your proposed RNA arm may help, but the readout column promises a diagnostic inference that the protein result itself cannot provide. |
| **“Mis-segregation rate — filter 5”** (§6, micronucleus readout) | You equate the assay readout with a specific mechanism without describing how other sources of micronuclei or treatment-related proliferation changes would be distinguished. |
| **“Two heterozygous variants in a singleton are a priori 50/50 cis or trans”** (§10) | Two possible configurations do not automatically have equal prior probabilities. You have not specified a model that justifies 50/50. |
| **“a PCS assay on parental lymphocytes … would test whether the miscarriage history is itself part of the carrier phenotype”** (§7) | It could test a cellular phenotype in the parents. It would not establish that their pregnancy losses were caused by it, especially given the two-family, VUS-based evidence described here. |
| **“applies to any repurposing exercise in any rare disease”** (§9) | Mis-segregation is disease-specific, and Cmax-versus-EC50 is not a universal exposure criterion. Show the generalized questions and their limits instead of claiming universality. |
| **“one that kills the candidate in MVA2 and holds it conditional in MVA3 is a demonstration”** (§9) | This demonstrates different worksheet outputs under different evidence availability. It does not validate differential drug suitability, and 15 published cancer-free individuals do not eliminate future malignancy. |
| **“Publicly available sources only.”** (Appendix B Q6/Q7) | Your data-availability statement identifies a challenge dataset accessed under an agreement with deletion requirements. Distinguish controlled-access challenge data from the public reference inputs. |
| **“we show why the obvious candidate cannot work”** (closing note) | §3.1 expressly says metformin is unevaluable, “not as disproven.” The final impression contradicts the careful analysis. |
| **“an approved drug that reaches the required concentration”** (closing note) | No required effective concentration has been measured in constitutional MVA, and the report disclaims comparable free or intratumoral exposure. This closing claim restores precisely the certainty your limitations remove. |

The highest-priority edits are the first-page and closing claims. They currently tell a more confident story than the strongest parts of the report support.