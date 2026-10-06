## 1. SCORE TABLE

**86/100: +1 from 85, +2 from 84, +4 from 82, +7 from 79, +9 from 77 and +14 from 72. Not a podium entry as submitted.** This is a judgment of submission quality, not a placement prediction against unseen competitors.

The supplied text controls this review. I also inspected the matching 93-page PDF, embedded figures, worksheet geometry, saved scorecards and selected supporting files. I did not rerun the scientific analyses or verify every citation. Inspected PDF: :codex-file-citation{path="/home/gar16/datos/HACKATHON-MVA-2026/entrega/listo-para-enviar/ciberpty_track2_report.pdf" purpose="source"}.

| Criterion | 72 round | 77 | 79 | 82 | 84 | 85 | Now | Movement from 85 and justification |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Scientific Rigor /35** | 27 | 28 | 29 | 30 | 31 | 32 | **32** | **0.** Most exposure, phase, power and DepMap qualifications now agree. However, dependency-transfer claims survive in Part II, and the newly specified tumour rule has an ambiguous or reversed effect sign. Correcting earlier errors while introducing a decision-critical ambiguity does not earn another point. |
| **Potential Impact /25** | 15 | 17 | 18 | 19 | 20 | 21 | **21** | **0.** The tumour-stage proposal now names estimands and confidence-bound requirements. But its sign, overlapping outcome categories, normal comparators and replication rule still require substantive decisions before execution. The constitutional assay remains more developed than the investigation relevant to the nominated tumour setting. |
| **Innovation /25** | 18 | 19 | 19 | 19 | 19 | 19 | **19** | **0.** The original contributions remain the DepMap lineage analysis, assay-disagreement analysis and interrogation of the proposed endpoint. Editorial repair and conventional pharmacology/safety checks do not constitute additional innovation. |
| **Scalability /15** | 12 | 13 | 13 | 14 | 14 | 13 | **14** | **+1.** The worksheets now fit their landscape pages with complete verdict columns. The transfer amendment improves the stated standard, but obsolete operational tables remain in the linked artefact. The corrected DepMap panel title also overlaps its neighbouring title. |
| **TOTAL** | **72** | **77** | **79** | **82** | **84** | **85** | **86** | **The broken worksheet is repaired. The scientific decision rules and supporting package are not fully reconciled.** |

The cumulative improvements since 72 are **+5 Rigor, +6 Impact, +1 Innovation and +2 Scalability**. They come from better uncertainty reporting, separating constitutional vulnerability from tumour benefit, specifying the proposed investigation and making the deliverables reusable.

**No deduction is for declining to recommend treatment.** The organisers permit a conditional research candidate. The deductions concern whether the investigation measures what the document claims and whether another team can apply the delivered rules consistently.

## 2. CONTRADICTION HUNT

**The most consequential remaining defect is the tumour-effect definition.** The primary endpoint is viable-cell recovery, but the parenthetical defines incremental killing as combination minus standard treatment. On recovery, that subtraction has the opposite sign.

For example, recovery of 60% with standard treatment and 30% with the combination means **30 percentage points of additional killing**. The written recovery subtraction gives **−30**, which would fail the positive-benefit threshold.

Quotations below preserve wording with line wrapping normalised. Excerpts are identified. The table distinguishes direct contradictions from ambiguities that prevent a unique decision.

| Location | Exact sentence or excerpt | What it contradicts | Fix |
|---|---|---|---|
| **I §5, p.16; II §4, p.56** | “Δ_T the incremental tumour killing (standard regimen plus bortezomib minus standard regimen, on vehicle-normalised viable-cell recovery)” *(excerpt)* | Lower recovery means greater killing. Combination-minus-standard **recovery** therefore reverses the intended benefit sign. If the subtraction is intended to operate on a transformed killing endpoint, that transformation is missing. | Define recovery \(R\), killing \(K=100(1-R)\), and \(\Delta_m=K_{m,S+B}-K_{m,S}=100(R_{m,S}-R_{m,S+B})\). |
| **Same tumour-stage paragraphs** | “a normal-comparator lower bound above 10 points is harm, a tumour upper bound below 20 points is insufficient benefit, anything else is inconclusive.” *(excerpt)* | Both conditions can hold simultaneously. The purported classification is not mutually exclusive. Technical invalidity and disagreement between the two experiments are also unmapped. | Give an explicit hierarchy: demonstrated harm overrides insufficient benefit; advancement requires valid, concordant experiments; otherwise apply insufficient-benefit or inconclusive rules. |
| **II §10, p.80; II §9, p.76** | “Whether the proteotoxic dependency transfers is precisely what the proposed experiment tests; we have not assumed it.” / “The proteotoxic vulnerability, if §6 shows it transfers” *(second quotation is an excerpt)* | I §6, II §6 and Q11 correctly state that the assay measures differential response and constitutional-cell vulnerability, **not mechanistic attribution**. | “Section 6 measures differential drug response and constitutional-cell vulnerability; attributing these to proteotoxic dependency requires separate mechanistic experiments.” Replace the p.29 “designed to break” formulation as well. |
| **I §6, p.18** | “No shift” → “Fails to support transfer in these cells; stops the constitutional-cell hypothesis” *(table excerpts)* | II §6, p.70 distinguishes a precise insufficient response from an inconclusive estimate requiring redesign. “No shift” does not distinguish either from simple non-significance. | Split the row: **precisely below the response threshold → insufficient response**; **interval too wide to decide → inconclusive**. Both block advancement, but only the former supports the stated negative conclusion. |
| **II §6 timeline, p.66** | Week “1–3” contains establishment and expansion described as “a pre-assay phase of 4–8 weeks that precedes week 1 and sits outside the eight-week window.” *(excerpts)* | The same work is simultaneously assigned to weeks 1–3 and to before week 1. The prose correction did not repair the schedule. | Add a separate **pre-assay establishment, gating and expansion** row, with duration contingent on growth and replication requirements. Reserve weeks 1–8 for work performed after readiness. |
| **I §5, p.15; II §4, p.55** | “no objective responses in 15 children with refractory solid tumours” / “no objective responses among 15 children with refractory solid tumours” *(excerpts)* | Later sentences give **15 enrolled, 11 assessable**. These earlier formulations retain a denominator ambiguity; they should not be read as an established 0/15 response estimate. | Use “15 enrolled, 11 assessable; no objective responses reported” at every occurrence. The enrolment/assessability distinction is explicit in the [ADVL0015 abstract](https://pubmed.ncbi.nlm.nih.gov/15570082/). |
| **Appendix B Q5, p.87** | “we withdrew that use and kept the paper only for the BUB1B/TRIP13 embryonal-tumour sentence its abstract actually states” *(excerpt)* | II §9 still uses PMID 28553959 for CEP57 tumour association and checkpoint severity, as well as BUB1B/TRIP13 checkpoint impairment. The citation-use history is inaccurate. | “We withdrew the inference from checkpoint severity to proteotoxic burden; we retain the paper for its reported tumour associations and checkpoint findings.” |
| **Linked transfer artefact, §§2–3 and amendment** | MVA2: “Fails at filter 4, and cannot be evaluated at filters 2–3.” MVA3: “Yes on total drug” *(table excerpts)* | The amendment changes MVA2 to F2 plausibility pass, the shared generic F3 comparison and F4 not evaluable without a patient. The main report says F3 cannot return a pass. Appending a correction does not make the working tables usable. | Publish corrected current tables. Preserve the old tables only in a clearly marked historical section. Remove “Everything else stands” where it preserves incompatible conclusions. |
| **Transfer artefact §5 versus II §9, p.77** | “A framework that returns the same answer for three diseases is a slogan.” | The report correctly says: “A valid framework can return the same verdict for three diseases”. These statements directly conflict. | “Transfer tests whether the same evidence standards can be applied across genes; identical statuses are permissible.” |
| **Transfer artefact §3 versus I §5 / II §6** | “a question for a tumour board in an MVA3 patient with an active tumour, gated on the ex-vivo test of REPORT §6” *(excerpt)* | The current report expressly says fibroblast failure does not decide tumour-directed investigation. | “The constitutional assay informs normal-cell vulnerability; tumour-directed investigation requires its own tumour/normal comparison.” |
| **Transfer artefact §6 versus II §5, p.59** | “bulk sequencing cannot see variegation at any depth.” *(excerpt)* | The report restricts non-identifiability to the balanced mixture and acknowledges detectable asymmetric mixtures. | “Bulk measurements cannot identify the balanced mixture modelled here or recover the cell-level distribution; asymmetric mixtures may remain detectable.” |
| **Transfer artefact §6 versus I/II §7** | “The report’s own extension — continuing clinical examination past age 7, including the orbit” *(excerpt)* | Both report parts now state that consensus clinical assessment has **no specified end date**. | “Our additions are the proposed examination frequency, orbit emphasis and age-10 review point.” |
| **Appendix B Q10, p.90, versus linked VERIFY.md** | “VERIFY.md lists each pre-registration with its result file and amendments” *(excerpt)* | The inspected repository file lists five original analysis registrations plus a mosaicism-control amendment. It does **not** list the DepMap follow-up, four-parameter follow-up and TRIP13 transfer as the claimed eight-registration manifest. | Add those three registrations and their result/commit pairs. Count the mosaicism amendment separately from the eight analyses. |
| **Linked `potencia/RESULTADOS_2_DOSIS.md`, §3** | “the assay is powered at an assumed 4× (0.897) and underpowered at an assumed 2× (0.387)” *(excerpt)* | The PDF correctly retires those as current design-power estimates. This supporting file still states them as the operative assay interpretation. | Mark the paragraph historical and superseded by the four-parameter analysis; link the current 0.167/0.068 scenarios and their assumptions. |

The transfer findings above concern the inspected repository’s actual `report/TRANSFER_MVA2_MVA3.md`, not merely a stale backup in the analysis directory.

**The requested numerical and factual checks:**

| Check | Finding |
|---|---|
| **(a) Funnel: “proteasome class survives filters 1–3”** | **Fixed in the current embedded figure.** It now names bortezomib IV’s total-plasma comparison and says other proteasome inhibitors are not evaluable. Do not resurrect this old criticism. |
| **(b) Free-drug arithmetic** | **Fixed.** \(0.17\times231–312=39.27–53.04\) nM; divided by **40 nM**, this is **0.98–1.33**. The separate 223 ng/mL cohort gives approximately **99 nM**, or **2.5×40 nM**. These are reference ratios, not measured free-plasma/free-medium margins. An EC50 bound of **<40** cannot establish an upper bound of 1–2.5 on a true exposure ratio. |
| **(c) Power** | **Consistent in the PDF:** 0.167 rounds to 0.17; n≈12 at f=0.30, n≈23 at f=0.20 and >24 at f=0.10 refer to the declared equal-EC50 test. The PDF labels 0.897 and 0.387 historical. The supporting dose-analysis file still needs the correction identified above. Different Monte Carlo sweeps need not reproduce the central estimate exactly. |
| **(d) Neuropathy** | **The principal report passages are repaired.** 25/140=17.86%, rounded to 18%; 11/140=7.86%, rounded to 8%. The stated setting is relapsed lymphoid malignancy with intensive combination chemotherapy, including vincristine, and ages 1.0–26.8—not bortezomib-attributable risk in this child. The age range and study context agree with the [FDA BPCA review](https://www.fda.gov/files/drugs/published/21602-Bortezomib-Clinical-BPCA.pdf). Standalone worksheet wording should retain the mixed paediatric/young-adult population. |
| **(e) Eight registrations** | **The list counts to eight:** DepMap; DepMap follow-up; MVA-Replay; mosaicism; power; four-parameter power follow-up; dose–response; TRIP13 transfer. The count is correct. The claimed verification manifest is incomplete. Commit order also remains distinct from proof of when results were first seen. |
| **(f) Phase, compound heterozygosity and reads** | The title and main interpretation consistently identify **presumed trans configuration, phase unestablished**. Raw reads are correctly acknowledged as distributed but unaligned. The categorical “short reads could not phase” language in I §10/Q9 remains stronger than the actual assessment; use II §10’s qualified ordinary-fragment wording. The L1012P functional-ranking inference is repaired. |
| **(g) DepMap** | The principal numbers agree: PRISM bortezomib **ρ=−0.075, n=444, p≈0.11**; carfilzomib **−0.060, n=424**; ixazomib **+0.028, n=438**. CRISPR PSMB5: **946=833+113**, overall **ρ=−0.198, q≈5.2×10⁻⁸**; solid **ρ=−0.077, q=0.118**; haematological **ρ=−0.261, q=0.042**. Interaction **β≈−0.017, p=0.026**. Shared models **365**, cross-assay **ρ=−0.070**. RMS **17 scored/3 drug/10 CRISPR**. The marginal interval, FDR result and adjusted-slope interval are now distinguished correctly. |

Two additional qualifications on DepMap:

- **p=0.076 in the dose analysis and p=0.056 in the interaction analysis are different fitted analyses**, not automatically a numerical contradiction. Label the model beside each occurrence.
- The panel-A “444” wording has been corrected, but **the longer replacement title overlaps panel B’s title**. The figure’s overarching “it did not hold up” headline remains broader than the qualified result.

The worksheet clipping is genuinely fixed: all seven columns are within the landscape page bounds. Q11 is approximately **490 words after removing PDF headers and footers**; I do not find a demonstrated 500-word-limit violation.

## 3. ATTACKABLE SENTENCES

These are additional weaknesses or overstatements. They should not all be mislabelled as direct contradictions.

| Location and wording | Why a domain expert attacks it | Defensible replacement |
|---|---|---|
| **II summary, p.29:** “It cannot inhibit complex I at therapeutic plasma concentrations.” | An isolated-mitochondria concentration comparison does not resolve intracellular exposure, duration and the mechanistic uncertainty your own review describes. | “The cited concentration comparison does not support complex-I inhibition as the proposed mechanism at therapeutic plasma exposure.” |
| **I §3.2, p.9:** “Aneuploid cells carry a stoichiometric protein imbalance and compensate by increasing degradation, which makes them dependent on the proteasome” *(excerpt)* | This universalises findings from particular experimental models to all aneuploid cells. | “In the cited aneuploid cancer models, altered protein homeostasis was associated with increased vulnerability to proteasome inhibition.” |
| **DepMap figure, p.48:** “and it did not hold up in solid tumours” *(excerpt)* | It can be read as candidate or mechanism falsification, whereas the drug association has the predicted sign and fails its significance criterion. | “No significant PRISM proteasome-inhibitor association; weaker CRISPR PSMB5 association in solid lines.” |
| **II §3.5, p.49:** “The pipeline is not blind: across all 6,790 compounds 1.1% reach p < 0.001 against 0.1% expected by chance.” | An excess of small p-values does not establish calibration or power for these candidate tests. Part I already explains this better. | “The screen contains an excess of small p-values, but this does not establish calibration or sensitivity for the proteasome-inhibitor comparisons.” |
| **I §5, p.14:** “Skeletal muscle atrophy … the decisive objection” *(table excerpt)* | Atrophy supplies a vulnerability concern, not a measured incremental neuropathy risk or automatic drug contraindication. | “Existing muscle atrophy increases concern about neuromuscular toxicity; absent demonstrated benefit, prophylactic or chronic use is not supported.” |
| **II §4, p.55:** “the in-vitro sensitivity of RMS at concentrations below the paediatric Cmax is real” *(excerpt)* | The document’s displayed PK comparison uses a 1.3 mg/m² label dataset, while ADVL0015 recommends 1.2 mg/m². No matched paediatric exposure comparison is presented here. | “RMS sensitivity was reported at 13–26 nM in the cited cultures; equivalent paediatric tumour exposure has not been established here.” |
| **I §5 / II §4:** “If it is ever reached for, it would be as part of a combination” | Failure of monotherapy does not establish a useful combination or justify clinical use of one. | “Any combination hypothesis requires separate evidence of incremental benefit over the standard regimen.” |
| **II §4, p.54:** “the best-characterised downstream consequence of aneuploidy” *(excerpt)* | “Best” requires a comparative assessment not supplied by this candidate-centred review. | “A downstream vulnerability characterised in the cited aneuploid cancer models.” |
| **I/II tumour-stage specification:** “with culture-level resampling and replication in two independently initiated experiments” *(excerpt)* | No confidence level, simultaneous-inference method, resampling structure or rule for combining the two experiments is specified. | “Before sampling, freeze the joint confidence procedure, culture and batch resampling hierarchy, and whether both independent experiments must satisfy every advancement condition.” |
| **II §6, p.69:** “if patient fibroblasts are markedly more sensitive than both control donors” *(excerpt)* | “Markedly” is undefined and overlaps the desired differential-response outcome. Different investigators could classify the same result differently. | “Define the excessive-response stop threshold numerically before sampling, separately from the minimum response threshold; interpret it as a constitutional-toxicity concern, not proof of mechanism.” |
| **I §6, p.18:** “the design needs about 12 independent cultures per arm” *(excerpt)* | The simulation sizes an equal-EC50 comparison, not the two-control, minimum-effect, micronucleus and stopping-rule programme. Q11 correctly acknowledges this. | “The equal-EC50 simulation first exceeds 80% power at about 12 cultures per arm under these assumptions; the complete advancement rule has not been sized.” |
| **II §6, p.61:** “A cell is under proteotoxic load whichever chromosome it gained” *(excerpt)* | Chromosome identity, dosage and adaptation are not shown to be interchangeable. The design counts numerical abnormalities, including losses, while this sentence concerns gains. | “The mixture model uses the fraction of numerically abnormal cells; chromosome identity, gains versus losses and per-cell burden may also affect response.” |
| **I §6, p.17:** “Any screen must measure mis-segregation per cell: metaphase counts, micronuclei … or single-cell DNA.” *(excerpt)* | Karyotype and single-cell copy number measure chromosome state; micronuclei are a conditional proxy. These are not interchangeable direct measurements of an error rate. | “Use cell-resolved chromosome-state measurements and a separately defined mis-segregation proxy; report their distinct estimands.” |
| **II §1, p.34:** “no in-silico classification of this allele can be anchored to same-gene truth” *(excerpt)* | The ClinVar census establishes that this snapshot is insufficient for same-gene calibration, not that all functional or independently curated evidence is unavailable. | “This ClinVar snapshot is insufficient for reliable BUB1B-specific calibration of predictor performance.” |
| **I §10 / Appendix B Q9:** “short reads could not phase two variants” *(excerpt)* | The reads were not aligned or inspected. Ordinary fragment bridging is implausible with the evaluated markers; that is narrower than an exhaustive impossibility claim. | “The evaluated VCF markers do not support ordinary short-fragment bridging; we did not assess the raw reads.” |
| **II §7, p.74:** “it is cheap to act on and it is squarely in the family’s interest” *(excerpt)* | Cost, availability and incremental counselling value are unmeasured; the paragraph later admits unknown cost and turnaround. | “Parental segregation and possible PCS testing are questions for clinical genetics; availability, cost and additional counselling value require local assessment.” |
| **Appendix B Q2, p.85:** “five filters instead of the usual two” | No review establishes that drug-repurposing practice ordinarily omits pharmacokinetics, safety or disease worsening. | “We organised the assessment into five explicit evidence questions.” |
| **Appendix B Q11, p.91:** “mTOR inhibitors would antagonise, not synergise.” *(excerpt)* | The cited study did not test rapalogues, and the report correctly labels the proposed interaction an inference elsewhere. | “We predict rapalogue antagonism from the cited mechanism; the combination remains untested in the proposed models.” |
| **II §9, p.77:** “The framework was transferred prospectively … and it gives different answers.” *(excerpt)* | The current uniform standard may produce the same research status for patient-free MVA2 and MVA3 assessments. Different background annotations are not necessarily different candidate verdicts. | “The framework was applied across genes using common standards; gene-specific evidence changes annotations, while several filter statuses remain identical.” |
| **Closing notes, pp.24 and 80:** “The honest answer to ‘what drug should he take today’ is none.” | Read literally, this exceeds a review of disease-modifying candidates and could encompass necessary supportive or unrelated medication. | “This assessment supports no disease-modifying drug for MVA to start today.” |

## 4. THE THREE CHANGES WITH THE HIGHEST RETURN

**1. Make both experimental decision rules executable, then simulate the rules actually proposed.**

**Expected movement: Rigor +1; Impact +1, conditional on a coherent result.**

Replace the tumour-stage paragraph in **I §5 and II §4** with an explicit definition:

> Let \(R_{m,a}\) be viable-cell recovery relative to vehicle in material \(m\), treatment arm \(a\), at the prespecified post-washout endpoint. Define incremental killing in percentage points as  
> \[
> \Delta_m=100(R_{m,S}-R_{m,S+B}),
> \qquad D_j=\Delta_T-\Delta_{N_j}.
> \]
> Positive \(\Delta_m\) means that adding bortezomib reduces recovery.

Then freeze:

- The identities and limitations of both normal comparators.
- The endpoint time and exposure-schedule qualification.
- A specified simultaneous confidence procedure and confidence level.
- Culture/batch resampling units and the requirement across two independent experiments.
- An outcome hierarchy that handles harm plus insufficient benefit, invalid assays and discordant experiments.

A defensible classification starts:

> Demonstrated normal-cell harm blocks advancement regardless of tumour response. Otherwise, advance to further preclinical investigation only when every prespecified benefit and normal-cell constraint is satisfied in both valid experiments. Precisely insufficient tumour benefit is classified separately; unresolved, discordant or invalid results are inconclusive.

Keep the 20/10/10 thresholds explicitly provisional. **Do not represent a preclinical “advance” as a treatment recommendation.**

For the constitutional assay, define the EC50-ratio direction, the numerical “markedly sensitive” stop threshold and exactly how the measured-fraction threshold is applied. Simulate the complete classification across both control comparisons, culture dependence and micronucleus uncertainty.

Report **advance / harm / insufficient response / inconclusive frequencies**, not merely rejection of equal EC50s. Include effects below, at and above the chosen thresholds. If this cannot be finished, retain the existing simulation but consistently state that **the full protocol is unsized**.

**2. Replace amendment-dependent operational documents with a single current version.**

**Expected movement: Rigor +1; protects or potentially improves Scalability.**

The principal failure is now distributed across files. Another paragraph appended to the transfer sheet will not solve it.

Create one authoritative current claim/status table and use it to reconcile:

- I §6, II summary/§9/§10 and Q11 on response versus mechanism.
- All ADVL0015 denominators.
- The pre-assay timeline.
- MVA2/MVA3 operational worksheets.
- The linked dose-analysis interpretation.
- The eight-registration manifest in `VERIFY.md`.

The current gene-transfer sheet should state, for bortezomib IV:

> F2: mechanistic plausibility supported; disease-specific activity unestablished.  
> F3: not excluded by the shared generic total-plasma comparison; free exposure and disease-specific transfer unresolved.  
> F4: patient-specific; not evaluable without a patient.  
> F5: untested.

Retain gene-specific tumour and checkpoint evidence as annotations. Do not force different verdicts to demonstrate that the framework works.

Move obsolete interpretations into a visibly historical section. Extend the existing claim checker to flag retired phrases in **current** deliverables, including figure text. Repair the overlapping DepMap titles and inspect the embedded PDF figure—not only the plotting source.

**3. Make the decision document prioritise the next investigation instead of recounting the repair history.**

**Expected movement: Impact up to +1; limited additional Innovation.**

Replace the repeated §3.3/§5/§6 narrative with a short comparative research-decision table:

| Candidate/question | Evidence already available | Missing evidence that changes the decision | What the present report can rank |
|---|---|---|---|
| Bortezomib, tumour-stage addition | Cancer-model rationale, nominal potency comparison, clinical toxicity and limited solid-tumour activity | Exposure-qualified incremental tumour effect and normal-cell separation | A documented candidate, not a demonstrated priority |
| Trametinib | Aneuploid-model rationale and marketed formulation | Absolute potency under specified assay conditions, exposure comparison and relevant normal-cell effects | A defined evidence gap |
| Metformin | Marketed drug; indirect rationale | Direct aneuploidy-selective activity at justified exposure | Currently unevaluable |
| Constitutional fibroblast assay | Proposed response and micronucleus measurements | Measured fraction, variability and interpretable response/safety estimates | Normal-cell vulnerability investigation; not a tumour-efficacy gate |

Replace “the gap most worth closing” and “best-characterised consequence” with that explicit comparison. State which evidence-retrieval task could change prioritisation before laboratory work and which uncertainty requires material.

Keep correction history in Part II or the repository. A judge should be able to identify the candidate, comparator, missing evidence and next decision without reading multiple accounts of earlier mistakes.

## 5. ONE-LINE VERDICT

**Ship after fixes in (2), especially the tumour-effect sign, dependency-transfer claims and obsolete operational transfer tables; the current package is not ready for the final submission.**