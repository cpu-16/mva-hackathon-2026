## 1. SCORE TABLE

**84/100: +2 from 82, +5 from 79, +7 from 77, +12 from 72. Not a podium entry as submitted.** This is an assessment of submission quality, not a prediction against unseen competitors.

The supplied text controls this review. I also inspected the matching local 90-page PDF’s embedded funnels and worksheet layout, and checked selected underlying results. I did not rerun the analyses or independently verify every citation. Inspected PDF: :codex-file-citation{path="/home/gar16/datos/HACKATHON-MVA-2026/entrega/listo-para-enviar/ciberpty_track2_report.pdf" purpose="source"}.

| Criterion | 72 round | 77 round | 79 round | 82 round | Now | Movement from 82 and justification |
|---|---:|---:|---:|---:|---:|---|
| **Scientific Rigor /35** | 27 | 28 | 29 | 30 | **31** | **+1.** Residual-function inference, exposure arithmetic, neuropathy context and constitutional-versus-tumour interpretation are substantially repaired. However, “true Cmax / EC50 ratio” survives, filter statuses remain internally inconsistent, and several summaries still exceed the operational experiment. |
| **Potential Impact /25** | 15 | 17 | 18 | 19 | **20** | **+1.** The tumour-stage specification now names relevant material, standard treatment, incremental benefit and matched exposure. That is a substantive improvement. Its decisive effect/selectivity criterion is still deferred, however, and the fibroblast programme remains more developed than the investigation that could actually support the nominated tumour-stage candidate. |
| **Innovation /25** | 18 | 19 | 19 | 19 | **19** | **0.** The lineage analysis and interrogation of assay disagreement remain the original Track 2 contributions. Correcting interpretation adds rigor, not another discovery. “Five filters instead of the usual two” still overstates methodological novelty. |
| **Scalability /15** | 12 | 13 | 13 | 14 | **14** | **0.** Generated worksheets, bounded verification coverage and documented rebuild modes remain useful. Landscape pagination is real, but the tables retain approximately portrait-width content. The status vocabulary is listed rather than operationally defined, and its progression rule contradicts the research workflow. |
| **TOTAL** | **72** | **77** | **79** | **82** | **84** | **The repairs earn two points. The claim that every listed defect was removed is false.** |

I am **not** deducting because the document recommends no treatment today. Candidate nomination for further investigation satisfies the organisers’ stated objective. The remaining deductions concern evidence consistency, comparative prioritisation and whether the proposed research can make the decision claimed for it.

The earlier September requests are substantially fulfilled. Of the latest three requests, reconciliation remains incomplete; §6 is more honest but not fully operational; the tumour-stage specification is present but stops immediately before defining its decisive threshold.

## 2. CONTRADICTION HUNT

The controlling conclusion is now consistent across the two executive summaries. The surviving defects are concentrated in subordinate summaries, filter semantics and protocol language.

Quoted text below preserves the wording while removing extraction line breaks. Not every row is a numerical contradiction: where the problem is an inconsistent standard or scope, that is identified explicitly.

| Location | Exact sentence or wording | What it contradicts | Fix |
|---|---|---|---|
| **II §3.1, p.38** | “For bortezomib, filter 3 is a true Cmax / EC50 ratio against an EC50 measured in an aneuploidy-stratified model.” | I §3.2 and II §3.2 explicitly say the denominator is a **40 nM reference upper bound read from a figure**, not a measured EC50 point estimate. This previously flagged sentence survives verbatim. | “For bortezomib, filter 3 compares total-plasma Cmax with a 40 nM reference upper bound read from an aneuploidy-stratified experiment.” |
| **II §3.5, p.47** | “In 444 solid-tumour lines, no proteasome inhibitor reached FDR < 0.05.” | I §4 supplies **444 bortezomib, 424 carfilzomib and 438 ixazomib**. The sentence assigns one denominator to three tests. | “Across 424–444 evaluable solid-tumour lines, depending on the inhibitor, none reached FDR < 0.05.” |
| **II worksheet introduction, p.78** | “Status vocabulary: pass · fail · untested · not evaluable · not reached · not excluded · exposure unresolved — only pass and not excluded permit further assessment.” | The same paragraph permits research assessment on unresolved evidence. The worksheet also assesses SC safety after “exposure unresolved,” and the report proposes closing trametinib’s unresolved gaps. | Delete the progression restriction. Define clinical exclusion separately from permission to investigate missing evidence. |
| **Embedded funnels, pp.7 and 36** | “anything selecting for unstable clones” | II §2, p.36 explicitly says **longer-term clonal selection remains untested**. A short micronucleus endpoint does not exclude selection of unstable clones. | “Increase in the measured micronucleus endpoint beyond the prespecified margin; long-term clonal selection remains unresolved.” |
| **I §6, p.17** | “A sensitivity difference measures whether the dependency transfers to constitutional aneuploidy and is, on its own, as compatible with systemic toxicity as with promise.” | II §6, p.59 correctly says it measures a response difference between sampled lines and requires mechanistic follow-up before attribution to dependency. | “A sensitivity difference measures differential response in the sampled constitutional lines; it does not by itself identify a proteotoxic dependency.” |
| **Appendix B Q11, p.88** | “a direction-of-effect filter (does the drug increase mis-segregation among survivors?).” | The operational rule permits an increase below a **provisional 50% margin**. It does not test exclusion of any increase. The same shorthand survives in the worksheet instructions on p.82. | “a direction-of-effect filter testing whether the micronucleus increase exceeds a prespecified harm margin.” |
| **Family summary, p.2** | “nerve damage was recorded in about 18 in 100 children” | The safety tables correctly identify a population aged **1.0–26.8 years**. The percentage is not a children-only estimate. The funnels repeat “18% of children.” | “Peripheral neuropathy was recorded in 25 of 140 children and young adults receiving the combination regimen.” |
| **II §6, pp.60–62** | “A second pre-registered analysis the same day gives us our own reason to doubt the 4×.” | The preceding analysis is dated **8 September**, but the dose-analysis correction is dated **6 September**. The underlying registration/result chronology places the dose analysis on **1 September**. | “An earlier dose–response analysis, pre-registered on 1 September, gives us a separate reason to question the 4× assumption.” |
| **II §6 timetable, p.64** | “expanded into twelve replicate cultures per arm … before week 4 — an expansion the eight-week assay window does not contain.” | This activity occupies weeks 1–3 of the eight-week table while being declared outside that window. The later timeline says expansion precedes the assay programme. | Add an explicit **pre-assay establishment and expansion phase**, outside weeks 1–8; make week 1 begin after cultures are available. |
| **II §3.5, p.51** | “What our analysis does add, and theirs does not address, is the lineage split: the association is carried by haematological lines and attenuated in solid ones (interaction p = 0.026)” | The preceding comparison concerns **drug response**, whereas this interaction is **CRISPR PSMB5 dependency**. I §4 says there are no evaluable haematological PRISM measurements for these drugs. This is a modality ambiguity, not an incorrect p-value. | “Separately, our CRISPR analysis identifies a lineage interaction in PSMB5 dependency; PRISM cannot estimate the corresponding haematological drug-response association.” |
| **I §3.3 / II §3.3 / worksheets** | “filters 2 and 5 are untested for it” — trametinib | **Inconsistent filter-2 standard:** aneuploidy-selective MEK evidence is described, but trametinib receives “untested,” while metformin receives “pass” despite no demonstrated metformin selectivity. “Mechanistic plausibility” and “demonstrated transfer to MVA” are being mixed. | Define filter 2 once, then apply it to every candidate. Under a plausibility standard, explain why trametinib does or does not meet that standard; reserve MVA validation for a separate evidence field. |
| **II §9, p.74** | “no proteasome measurement exists in CEP57 cells for filter 3” | **Inconsistent exposure-evidence standard:** no constitutional BUB1B measurement exists either, yet cancer-model potency permits an MVA1 comparison. CEP57 may have weaker transfer evidence, but absence of a CEP57-specific assay is not a consistently applied filter-3 rule. | Separate generic cancer-model exposure plausibility from gene-specific biological transfer. Mark the latter unresolved for both, with different supporting evidence. |

The neuropathy denominator and age range are supported by the [FDA BPCA clinical review](https://www.fda.gov/files/drugs/published/21602-Bortezomib-Clinical-BPCA.pdf). The report now appropriately distinguishes observed combination-regimen events from this child’s unknown incremental risk.

**Results of the specifically requested checks:**

| Check | Finding |
|---|---|
| **(a) “The proteasome class survives filters 1–3”** | **Removed from the matching PDF’s embedded funnels.** They now name bortezomib IV, qualify the total-plasma comparison and call other proteasome inhibitors not evaluable. Do not deduct for the removed sentence. The separate clonal-selection overclaim remains. |
| **(b) Free-drug arithmetic** | **Correct as reference arithmetic:** \(231×0.17=39.27\), \(312×0.17=53.04\) nM; dividing by 40 gives **0.982–1.326**. Approximately 99/40 gives **2.48**. These are not measured free-drug margins. Because EC50 is **<40 nM**, treating 40 as an exact EC50 would also be wrong. The revised prose mostly makes both distinctions correctly. |
| **(c) Power** | **0.167 at n=3**, approximately **12 cultures/arm at f=0.30**, **23 at f=0.20**, and **>24 at f=0.10** match the stated four-parameter results. **0.897 and 0.387 are clearly historical**, not surviving false current labels. Different Monte Carlo sweeps need not return identical estimates at the same scenario. The unresolved issue is power for the **complete decision rule**, explicitly acknowledged in Q11. |
| **(d) Neuropathy** | **25/140 = 17.9%; 11/140 = 7.9%.** The main safety tables now carry disease, combination therapy, vincristine and age context. “Children” remains inaccurate shorthand in the family summary and funnel. |
| **(e) Eight pre-registrations** | **The list counts to eight:** DepMap; DepMap follow-up; MVA-Replay; mosaicism; original power; four-parameter power; dose–response; TRIP13 transfer. The phase pilot is correctly excluded. Counting eight does not independently establish prospective execution or turn follow-up predictions into external validation. |
| **(f) Phase, compound heterozygosity and reads** | The working diagnosis is consistently labelled **presumed**, phase unestablished, and the missense remains a VUS. Raw reads are correctly acknowledged; lack of alignment is identified as the team’s choice. The categorical claim that phase is impossible “from these data” remains stronger than the demonstrated limitations of the called-marker configuration and tested panel. |
| **(g) DepMap** | The principal numbers reconcile: **946 = 833 solid + 113 haematological**; pooled ρ **−0.198**, q **5.2×10⁻⁸**; solid ρ **−0.077**, q **0.118**; haematological ρ **−0.261**, q **0.042**. Interaction β approximately **−0.01675**, p **0.0255 → 0.026**. **365 shared models**, assay correlation **−0.070**, and RMS coverage **17 scored / 3 PRISM / 10 CRISPR** agree. The surviving denominator sentence and modality ambiguity are identified above. |
| **Intervals versus significance** | The report now separates the solid Spearman interval excluding zero, the FDR test failing, and the adjusted slope interval including zero. **These are not contradictory results.** |
| **Variant length and residual function** | **736 retained residues; 737–1050 removed = 314 residues.** The survival-based functional ranking relative to L1012P is withdrawn. These repairs hold. |
| **References and page presentation** | The Part I/II section mapping is usable. “Figure 1” on p.55 lacks an equally explicit numbered caption. Worksheets are landscape and the inspected candidate rows are intact, but narrow columns still break names and status words. |
| **Q11 word limit** | Approximately **494 whitespace-delimited words**, excluding running headers/page numbers. It appears within 500; replacements should preserve that limit. |

**Visual finding:** landscape orientation alone did not fix the worksheet. On pp.79–81, the table content occupies approximately **424 points of an 842-point-wide page**. Drug names and the filter-5 header still break into fragments. This is a layout defect visible in the PDF, not merely a `pdftotext` artefact.

## 3. ATTACKABLE SENTENCES

These are additional or deeper vulnerabilities. They should not be counted as independent numerical contradictions where they merely restate an issue above.

| # | Location and wording | Why an expert attacks it | Defensible replacement |
|---:|---|---|---|
| 1 | **II executive summary, p.31:** “it is the one worth having ready as a question” | Implies comparative priority, while the new tumour-stage paragraph explicitly disclaims a basis for ranking it above trametinib. | “It is one conditional research candidate worth documenting; this assessment does not establish priority over unresolved alternatives.” |
| 2 | **II §3.1, p.38:** “We reject it with a number” | The candidate’s stated exclusion is missing selective potency; the thousandfold number concerns a different mechanistic comparison. | “We cannot evaluate aneuploidy-selective exposure; a separate concentration comparison weakens the proposed complex-I rationale.” |
| 3 | **I §3.1, p.8:** “what the gap rules out is the complex I route at plasma concentrations” | A plasma-versus-isolated-system comparison does not establish intracellular target exposure or universally settle the mechanism. | “The cited concentration comparison does not support complex-I inhibition at therapeutic plasma levels; it does not establish intracellular exposure.” |
| 4 | **II §3.5, p.47:** “tracks aneuploidy strongly overall” | A correlation of −0.198 is modest; small q is not large effect size. | “PSMB5 dependency has a modest overall association with aneuploidy (ρ = −0.198), with strong statistical evidence under the stated test.” |
| 5 | **II §3.5, p.51:** “which removes between-line confounding by construction” | Within-line contrasts reduce between-line differences but do not isolate aneuploidy from every effect of reversine or treatment interaction. | “The within-line contrast controls stable between-line differences, while attribution specifically to induced aneuploidy remains dependent on the perturbation design.” |
| 6 | **I §6, p.19:** “the cost is biology” | The rerun changed biological variability, plate effects, grid and statistical test. The report itself says their contributions were not separated. | “Most of the reduction is associated with changes beyond the curve fitter; their individual contributions were not isolated.” |
| 7 | **II §6, p.66:** “treat a shift whose 95% interval lies below the corresponding row as a negative” | That rejects the assumed **4× scenario**, not every response difference or dependency. It also leaves partially overlapping intervals without a clear decision. | “An interval wholly below the row fails the prespecified 4× mixture scenario; overlap is inconclusive, and neither outcome excludes smaller differential responses.” |
| 8 | **II §6, p.66:** “If the experiment ever returns a selectivity estimate, the table is recomputed rather than defended.” | Re-estimating the advancement threshold from the same outcome data makes the purported fixed decision rule adaptive. | “Keep the primary threshold fixed; any table recalibrated from these data is exploratory and must be evaluated in a subsequent experiment.” |
| 9 | **II §6, p.67:** “without the aneuploidy-high positive control showing a larger shift still” | RPE1 and patient fibroblasts are not isogenic or the same cell type. Their ordering is not a validated safety discriminator. | “Use RPE1 to assess assay responsiveness; interpret patient-cell toxicity independently, without requiring a particular ordering across cell types.” |
| 10 | **II §6, p.67:** “Failing any of 1–3 … stops the constitutional-cell programme” | An inconclusive confidence interval and demonstrated harm are scientifically different outcomes. Stopping an uninformative experiment need not reject its hypothesis. | “Classify each result as advance, demonstrated harm, or inconclusive; an inconclusive result permits no advancement claim and requires redesign before further testing.” |
| 11 | **I §6, p.17:** “Patient dermal fibroblasts against two matched controls” | The power analysis describes a two-arm comparison. The report does not specify two separate comparisons, pooled controls, donor weighting or multiplicity. | “Estimate the patient-versus-control effect separately for each control donor; specify aggregation and multiplicity before sampling, and simulate that exact rule.” |
| 12 | **II §6, p.61:** “an MVA cell carries about one altered chromosome” | Converts an illustrative burden assumption into a generic biological measurement. The report later insists that the actual burden must be counted. | “For an illustrative low-burden scenario, we model one altered chromosome per abnormal cell; the treated culture’s distribution is unknown.” |
| 13 | **II §9, p.73:** “Less mis-segregation should mean less proteotoxic burden” | Less checkpoint impairment is not a measurement of mis-segregation, persistent aneuploid burden or proteotoxic stress. | “The cited checkpoint findings do not establish a proteotoxic burden in CEP57 cells; that transfer remains unmeasured.” |
| 14 | **II §10, p.76:** “we measured that it is not establishable from these data” | No raw-read alignment was performed. The analysis establishes failure of particular available phasing routes, not a universal impossibility theorem. | “We did not establish phase: the called heterozygous markers do not support ordinary short-fragment bridging, and the tested reference-panel route was uninformative.” |
| 15 | **Appendix B Q2, p.82:** “Loss of function … a null allele with a hypomorphic one.” | The leading declaration outruns its following caveat: the missense’s function and phase are unresolved. | “Working hypothesis: a truncating allele paired in trans with a functionally impaired missense allele; phase and residual function remain unestablished.” |
| 16 | **II §7 table, p.70:** “Catches superficial ERMS that renal ultrasound cannot” | Claims demonstrated surveillance detection performance from an examination proposal. | “Examines sites outside the renal-ultrasound field; detection performance and clinical benefit for this schedule are unquantified.” |
| 17 | **I/II §7 tables:** “6-monthly is reasonable; no evidence of benefit exists” | An unsupported frequency is still a clinical proposal. Calling it reasonable adds no evidence, and the surrounding consensus material can lend it borrowed authority. | “Routine blood-count surveillance has no demonstrated benefit here; its use and frequency require an individual clinic decision.” |
| 18 | **II worksheet, p.78:** “A candidate must pass all five to be clinically supported” | These five questions are neither a validated clinical decision rule nor universally necessary criteria for every useful treatment. | “These five questions organise this candidate assessment; satisfying them would not establish clinical benefit or authorise treatment.” |
| 19 | **Funnel / II worksheet:** “Filters 3 and 5 are the two most often skipped” | No survey or benchmark establishes this frequency claim. | “This assessment makes exposure plausibility and disease-worsening risk explicit.” |
| 20 | **I §5 / II §4:** “advance … only if an effect and selectivity criterion fixed before the material is obtained is met” | Promises that somebody will specify the decisive criterion later. That is a protocol requirement, not the promised concrete specification. | “The current specification defines the comparison but not an executable advancement threshold; effect, selectivity, uncertainty and reproducibility criteria remain to be fixed.” |

## 4. THE THREE CHANGES WITH THE HIGHEST RETURN

### 1. Complete reconciliation and replace the contradictory status rule

**Expected movement: Scientific Rigor +1–2; protects Scalability. Editorial work, no new biological analysis.**

Make every correction in section 2 in the source, generated tables, figures and methods form. In particular, remove the two surviving previously flagged sentences on pp.38 and 47.

Replace the p.78 progression rule with:

> “Statuses describe evidence, not permission to investigate. ‘Pass’ means the stated criterion is supported in the named setting; ‘fail’ means evidence opposes it in that setting; ‘untested’ means no direct test was performed; ‘not evaluable’ means a required input is missing; ‘not reached’ means it was not assessed. ‘Not excluded’ denotes only the specified total-plasma comparison. ‘Exposure unresolved’ means available pharmacokinetic information does not settle exposure plausibility. Unresolved evidence can motivate research but cannot establish clinical suitability.”

Also define filter 2 as either **mechanistic plausibility** or **demonstrated disease-specific activity**. The current candidate table alternates between them.

Verify the **final PDF**, including embedded images, rather than only the Markdown. The existing regex checks demonstrably do not prevent the surviving contradictions.

### 2. Make the tumour-stage comparison executable, and separate statistical power from advancement

**Expected movement: Potential Impact +1–2; Scientific Rigor +0–1. One editorial day plus at most two days of CPU simulation.**

Replace the deferred criterion in I §5 and II §4 with a short, explicitly provisional operational specification. For example:

> “Compare vehicle, bortezomib, the relevant standard regimen, and standard regimen plus bortezomib in tumour-derived material and patient constitutional non-malignant comparators. Use a prespecified pulse/washout schedule justified from clinical pharmacokinetic and pharmacodynamic evidence. The primary endpoint is viable-cell recovery at a fixed post-washout time. Define incremental killing as the reduction in vehicle-normalised viability from adding bortezomib to the standard regimen. For planning, require at least 20 percentage points of incremental tumour killing, at least 10 percentage points of tumour–normal separation, and no more than 10 percentage points of incremental killing in either normal comparator. These are provisional research thresholds, not clinically validated margins. Advancement requires prespecified confidence-bound criteria and replication in independently initiated culture experiments; otherwise classify the result as negative or inconclusive.”

Those particular thresholds are **design choices**, not findings. The value is making choices explicit and testable.

Then:

- Specify how the two control donors enter the analysis.
- Freeze the rule before estimating selectivity from the experiment.
- Simulate the complete rule across plausible effect sizes, variances and culture dependence.
- Report **go / harm / inconclusive probabilities**, not merely rejection of equal EC50s.
- Keep the fibroblast programme’s decision separate from the tumour-stage decision.

Do not manufacture a tumour-model power estimate from the fibroblast simulation. If the complete rule cannot be supported within feasible replication, say that the protocol remains a pilot for estimating operating characteristics.

### 3. Fix the actual reading artifact and align the methods abstract with the research deliverable

**Expected movement: Scalability +1; possible Potential Impact benefit. Half to one editorial day.**

The worksheets need a width correction, not another orientation change. Let them use the landscape page’s available width. Replace long column headers with **F1–F5 plus a readable legend**, preserve whole drug names and status phrases, and inspect pp.25 and 79–81 after regeneration.

Move revision-history passages—“we got this wrong once,” retired branches and repeated explanations of previous versions—into a compact correction log in Part II. Keep their scientific consequences in the decision document.

Finally, replace Q11’s generic priority claim:

> “Our deliverable is that question prepared in advance, with its exposure comparison and its stopping rule.”

with:

> “Our deliverable is a conditional tumour-stage research comparison, with unresolved exposure and selectivity requirements, plus a separate constitutional-cell vulnerability assay.”

Keep the abstract below 500 words. Do not describe a deferred stopping rule as already delivered.

## 5. ONE-LINE VERDICT

**Ship after fixes in (2); the current version still contradicts its own exposure evidence, sample counts and research-progression rules.**