# Codex (gpt-6-astra) as panel judge of the pitch video v5 (first render) — 2026-09-08 09:41–09:52

Input: two contact sheets (3 moments × 16 scenes of the rendered mp4) + the narration script. Asked for a contradiction hunt against the controlling conclusion, a rubric score of the video alone, three fixes, and a legibility audit. Verdict: **76/100** (Rigor 28, Impact 19, Innovation 18, Scalability 11); the written report had scored 72.

## What was applied before the final render

- S1: «none should be started today» → «no drug should be started for this today» (the report's own sentence).
- S5: «no effective concentration against aneuploid cells has ever been measured» → «no aneuploidy-selective effective concentration has ever been measured for it»; «a thousand times» → «about a thousand times».
- S7: «neuropathy in eighteen percent of children» → «… of children in the paediatric trials»; on screen: 25/140, motor 8 %, regimens with chemotherapy, his own risk is unknown. «has never shrunk a paediatric solid tumour» → «produced no objective responses in paediatric solid tumour trials».
- S6: headline «Bortezomib: a conditional research candidate, not a therapy»; the controlling conclusion as the dominant block (order-of-magnitude comparison; therapeutic margin unestablished; no significant proteasome-inhibitor association; target association weaker in solid tumours; tumour selectivity in MVA unestablished). The free-drug line now shows the 99 nM figure that makes «1–2.5×» arithmetic visible.
- S8: sub-line «A test of cellular response in constitutional cells, not of tumour benefit»; «n = independent cultures, not wells · model-based power» promoted to readable size.
- S9: «Confirm his current age first» promoted to a sub-headline; the past-7 clinical-examination band drawn dashed and labelled «our proposal, not consensus»; «age 10, then reviewed».
- S10: «the measurements that would overturn it» → «the measurements that would change the next decision».
- S2: side labels «variant 1 · phase unknown / variant 2 · phase unknown».
- S4: «Five explicit questions before a drug becomes a candidate»; funnel enlarged.
- Legibility: tiny text 22 → 25 px, provenance 19 → 21 px, repository URL 44 → 60 px.

## Not applied, and why

- S4 funnel text «The proteasome class survives filters 1–3»: it is the report's own figure (fig3_funnel.png, Part I §2). Changing it only in the video would make the video diverge from the report; it goes to the October report round instead.
- S3 «healthy genomes»: the Track 1 report uses exactly that wording for GIAB/1000G («What score does a healthy genome produce»); on screen they are called «unspiked public genomes».
- S9 headline «What changes his prognosis today is surveillance»: Part I §7 says «The intervention that most changes this child's prognosis is surveillance»; the age caveat was promoted instead.
- S8 headline «The experiment that could prove us wrong»: Part I §6 title is «the experiment that could show us we are wrong»; the limitation was added as the sub-line.

---

**A. CONTRADICTION HUNT**

The central conclusion survives, but several headlines and qualifications still need reconciliation. The most consequential problems are in the visuals.

| Scene | Exact wording | Problem and change |
|---|---|---|
| **S1, spoken/on screen** | “Our answer: none should be started today.” | Broader than the disease-modifying question. Replace with **“No disease-modifying drug is supported for use today.”** |
| **S4, funnel** | “The proteasome class survives filters 1–3” | A rough exposure comparison does not establish passage through the exposure filter; evidence for bortezomib also cannot automatically clear a class. Replace with **“Bortezomib remains a conditional research candidate; therapeutic exposure is unestablished.”** |
| **S6, headline** | “Bortezomib is not excluded. So we tested it against ourselves.” | Drops the narration’s restriction to an exposure plausibility check. Replace with **“Bortezomib: conditional research candidate. Public-data tests did not establish selectivity.”** |
| **S6, exposure text** | “on free drug … ≈ 39–53 nM, within 1–2.5× of the bound” | The displayed interval divided by 40 gives approximately **0.98–1.33**, not 1–2.5. More fundamentally, an EC50 upper bound cannot establish an exposure margin, and nominal assay concentration is not necessarily comparable to unbound plasma concentration. Replace with **“Estimated unbound plasma peak: 39–53 nM. Therapeutic margin unestablished.”** |
| **S5, spoken** | “no effective concentration against aneuploid cells has ever been measured” | Broader than absence of an **aneuploidy-selective** effective concentration. Published experiments did expose aneuploid cells to metformin and report effects. Replace with **“We did not identify an aneuploidy-selective effective concentration applicable to MVA.”** [Primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532042/) |
| **S5, spoken** | “needs a thousand times the therapeutic plasma level” | Narration makes the approximate, mechanism-dependent comparison sound exact. Replace with **“The proposed complex I mechanism uses millimolar concentrations, roughly three orders above micromolar plasma levels.”** |
| **S7, spoken** | “neuropathy in eighteen percent of children” | Omits the population and combination regimen, inviting interpretation as this child’s risk from bortezomib alone. The cited FDA review concerns a cohort receiving intensive chemotherapy plus bortezomib. Replace with **“Neuropathy was reported in a chemotherapy-plus-bortezomib cohort; this child’s risk is unknown.”** Retain 18% only with its verified endpoint and denominator displayed. [FDA review](https://www.fda.gov/files/drugs/published/21602-Bortezomib-Clinical-BPCA.pdf) |
| **S7, spoken** | “Alone, it has never shrunk a paediatric solid tumour in a trial.” | “Never shrunk” exceeds “no objective responses” in the cited trial; subthreshold shrinkage is not an objective response. Replace with **“The cited paediatric single-agent trial reported no objective responses.”** |
| **S8, headline; S10, closing** | “The experiment that could prove us wrong”; “the measurements that would overturn it” | In this sequence, fibroblast results appear capable of overturning the clinical conclusion. They cannot establish tumour selectivity or clinical benefit. Replace with **“The experiment that could challenge our research hypothesis”** and **“with the measurements that would guide the next research decision.”** |
| **S9, headline** | “What changes his prognosis today is surveillance.” | Claims an established individual outcome benefit; the footer also says his current age is unknown. Replace with **“The current clinical priority: confirm age-appropriate surveillance.”** The stated ultrasound schedule is supported by consensus; the personalised prognosis claim is not established here. [Consensus recommendations](https://pmc.ncbi.nlm.nih.gov/articles/PMC11705613/) |

Two additional overclaims affect rigor and innovation:

- **S4:** “Five filters, not the usual two” and “Filters three and five are the ones usually skipped” assert an unsupported comparison with other practice. Use **“Five explicit questions before a drug becomes a candidate.”**
- **S3:** “Thirty-seven healthy genomes” asserts a clinical status that reference-dataset membership alone does not establish. Use **“Thirty-seven unspiked public reference genomes.”**

**No apparent spoken/on-screen numerical mismatch** in the 37-background comparison, 444-line analysis, or 17%/80% power figures. S6’s attenuated target association and nonsignificant drug associations agree with the controlling conclusion. Those are distinct findings, correctly kept separate.

**B. RUBRIC SCORE — VIDEO ALONE**

| Criterion | Score | Justification |
|---|---:|---|
| Scientific Rigor | **28/35** | Negative findings, phase uncertainty and failed controls are explicit; exposure language, absolute claims and the fibroblast-to-clinic implication remain weaknesses. |
| Potential Impact | **19/25** | Provides a useful research decision process and surveillance emphasis; patient benefit remains prospective and age applicability unresolved. |
| Innovation | **18/25** | Replay, adversarial testing and stopping rules form a useful workflow; comparative novelty is asserted more than demonstrated. |
| Scalability | **11/15** | A second-gene transfer and reproducible artifacts support portability; broad validation and independent adoption are not demonstrated. |
| **Total** | **76/100** | |

This scores what the video communicates; it does not independently validate the underlying analyses or rescore the report.

**C. THE THREE HIGHEST-RETURN FIXES**

1. **Make S6’s controlling conclusion the dominant visual.** Replace the headline and dense exposure prose with:

   > **Bortezomib remains a conditional research candidate.**  
   > Total-plasma exposure: order-of-magnitude comparison only.  
   > Therapeutic exposure and tumour selectivity in MVA: unestablished.  
   > Tested drug screen: no significant proteasome-inhibitor association.  
   > Target association: weaker in solid tumours.

   Correct S4’s “survives filters 1–3” simultaneously.  
   **Estimated movement: +2–3 Scientific Rigor.**

2. **State precisely what S8 can resolve.** Replace its headline with **“A test of cellular response—not clinical benefit.”** Use this narration:

   > “Patient fibroblasts could test sensitivity and chromosome instability, but cannot establish tumour benefit. Under our model, three independent cultures per arm give 17% power; twelve give 80%. Greater sensitivity could indicate toxicity.”

   Keep **“independent cultures per arm”** and **“model-based power”** readable beside the bars.  
   **Estimated movement: +1–2 Scientific Rigor, +1 Potential Impact.**

3. **Rebuild S9 around applicability and demonstrated transfer.** Use:

   > **Today: confirm age and surveillance plan.**  
   > Consensus: renal ultrasound every three months until age seven.  
   > **Reusable outputs:** eight pre-registrations, five-filter worksheet, replay tool.  
   > **Transfer demonstrated:** TRIP13, three reference backgrounds. Broader validation remains open.

   Remove the proposed extension from the consensus timeline. Enlarge these statements using space recovered from the chapter transitions.  
   **Estimated movement: +1 Potential Impact, +1–2 Scalability.**

These estimates overlap; together, roughly **82–85/100** is plausible after the other wording corrections.

**D. WHAT WORKS**

The video reports contamination, falsification and negative drug-screen results instead of hiding them.  
The safety discussion and survivor-cell endpoint make the proposed research decision concrete.

**E. LEGIBILITY**

- **Systemic:** Main headlines are readable. Citations, caveats, figure labels and several explanatory paragraphs are too small or low-contrast for comfortable viewing at contact-sheet scale. Full-speed readability cannot be established from stills.
- **S2:** The separate “allele 1” and “allele 2” protein tracks visually imply established trans phase despite the headline. Relabel **“Variant A/B; phase unknown”** and identify the tracks as predicted protein consequences.
- **S4:** The funnel is a miniature report figure surrounded by unused space. The right-hand bortezomib annotation appears clipped at the white panel boundary.
- **S6:** The forest plot clips the leftmost portion of the bottom label and the right ends of explanatory axis text. Re-export with sufficient margins; enlarge the plot.
- **S3/S8:** Essential interpretation—retrieval versus diagnostic performance, and independent cultures versus wells—is buried in tiny text. Promote it beside the relevant result.
- **S5:** The concentration graphic has no calibrated axis. Label it **“schematic concentration comparison”** or supply actual ranges on a log axis.
- **S9:** The similarly coloured surveillance bars visually confer comparable authority on consensus guidance and “our extension.” The age-ten endpoint also looks like a recommended cutoff.
- **Title/chapter cards:** Several samples are effectively black. They may represent fades, but the title beat communicates almost nothing in the supplied samples.
- **S1:** The last sampled sentence stops at “would.” This could be an unfinished reveal, not cropping; verify that the complete sentence is held before transition.
- **Closing card:** Enlarge the repository address and hold it at full contrast. No major overlap is apparent in the main slide text.