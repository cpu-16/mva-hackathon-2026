# Codex (gpt-6-astra) as script doctor for the pitch v5 — 2026-09-08 08:47–08:55

Prompt: the draft v5 (472 w), the v4 script with the retired sentences marked, and Part I of the submitted Track 2 document verbatim as the only source of truth. Asked for a sentence-level fact audit, a ≤380-word rewrite, visual beats and three remaining attack points.

What was taken: the audit verdicts and the precision fixes ("not excluded", "margin unknown", "barely represented", "after a laboratory gate", "reusable as questions", "under our pre-registered model"). What was NOT taken: the Track 1 sentences Codex marked *not in excerpt* (two independent analyses, 37 unspiked genomes, the contaminated control caught twice, P-B2 falsified, no parental sample) — those are in `submission/ciberpty_track1_report.md` and were verified there before going back in; and the removal of the n = 3 / n = 12 power numbers, which are in Part I §6 and are kept with their condition ("under our pre-registered model").

---

# A. FACT AUDIT TABLE

Each row covers one draft sentence or standalone fragment. “Not in excerpt” means unsupported by the supplied text, not necessarily false. The family-consent sentence is retained under your explicit exception.

| Draft sentence | Verdict | Exact excerpt phrase | Fix applied |
|---|---|---|---|
| A child survived an embryonal rhabdomyosarcoma. | supported | “this child's tumour was an embryonal rhabdomyosarcoma”; “our proband is alive” | Retained. |
| His cells miscount chromosomes when they divide: mosaic variegated aneuploidy. | supported | “a child with mosaic variegated aneuploidy”; “a checkpoint that is already insufficient” | Removed for space. |
| His family shared his genome so that strangers might help. | not in excerpt | None. Explicitly permitted by your instruction about documented family consent. | Retained under that exception. |
| We were asked which approved drug could help him. | supported | “An existing, approved medicine that could help a child” | Removed for space. |
| Today, the honest answer is none. | overstated | “No drug should be started for this today.” | Scoped to disease modification, avoiding a claim that no medicine could help him for any indication. |
| This is the evidence behind that no, and what would change it. | supported | “What would change the answer.” | Replaced with the concrete conclusion; reconsideration remains in the close. |
| Two independent analyses, required to agree: a hypothesis-free genome-wide run on his eight clinical terms, and an eleven-gene panel. | not in excerpt | None establishes these two analyses, their independence, term count or agreement requirement. | Removed. |
| Both land on BUB1B: one nonsense allele, one missense of uncertain significance. | not in excerpt | “two heterozygous `BUB1B` variants”; “stop_gained”; “UNCERTAIN_SIGNIFICANCE” | Retained the variant findings; removed the unsupported convergence claim. |
| Whether they sit on opposite copies of the gene is not established. | supported | “whether they sit on opposite copies of the gene is not yet shown” | Retained. |
| There are no parental samples. | not in excerpt | “Ask about testing and counselling for both parents” does not establish sample availability. | Removed. |
| Our replay tool plants known alleles into public healthy genomes. | supported | “plants two alleles into a public genome”; “three healthy GIAB genomes” | Shortened; added its retrieval-only limitation. |
| Thirty-seven unspiked genomes, asked the same symptoms: none scores higher than this case. | not in excerpt | None reports this thirty-seven-genome comparison. | Removed. |
| We caught our own contaminated control, twice. | not in excerpt | None documents two contaminated replay controls. | Removed. |
| Cleaned up, the score holds in every background; the rank does not. | not in excerpt | “The same pattern as BUB1B (rank 1/2/3 under an unrelated phenotype)” does not establish the cleanup claim or its scope. | Replaced with the documented second-gene transfer result. |
| One pre-registered prediction is falsified, and published. | not in excerpt | None identifies this replay prediction and its falsification. | Removed; retained the documented preregistrations elsewhere. |
| For the drug, five filters instead of the usual two. | supported | “We applied five filters to candidate drugs rather than the usual two” | Named the five filters; removed the unnecessary comparison. |
| Approval and mechanism are necessary, not sufficient. | supported | “Regulatory”; “Mechanistic”; “Pharmacokinetic”; “Patient-specific safety”; “Direction of effect” | Incorporated into the filter list. |
| Filter three: does the achievable plasma level reach the concentration that works in a dish? | overstated | “a possibility check on total plasma drug at a peak, not a demonstration of efficacy” | Explicitly described a plasma peak as an exposure plausibility check. |
| Filter five: among the cells that survive, is mis-segregation made worse? | supported | “among the cells that survive the drug, is the defect made worse?” | Retained in simpler spoken language. |
| Metformin is the candidate the literature points to. | supported | “Metformin, the candidate the literature points to” | Replaced with its decision-relevant verdict. |
| No one has measured the concentration it needs against aneuploid cells, and the route proposed for it needs a thousand times the plasma level. | overstated | “no study reports a metformin aneuploidy-selective effective concentration”; “a gap of roughly a thousandfold in concentration ranges, not a dosing calculation” | Specified selective activity, the complex one mechanism and an approximate concentration comparison. |
| Not disproven. | supported | “unevaluable, not as disproven” | Expressed through the remaining untested possibility. |
| Unevaluable. | supported | “not evaluable for aneuploidy-selective activity” | Retained with that scope. |
| Bortezomib is not excluded by filter three: on free drug, its peak sits within one to two-and-a-half fold of the effective concentration. | overstated | “within one- to 2.5-fold of the < 40 nM bound”; “the true free-drug margin is unknown”; “the two sides are not on the same footing” | Removed the ratio shorthand. Preserved non-exclusion and the limits on free exposure and duration. |
| So we tested it against ourselves, pre-registered, on public cancer data. | supported | “drug list, directions, statistic, correction and stopping rules committed… before the analysis ran” | Replaced rhetorical wording with the actual public-data findings. |
| Across four hundred and forty-four solid-tumour lines, no proteasome inhibitor reached significance. | supported | “Result 1 — drugs (444 solid lines). No proteasome inhibitor reached FDR < 0.05.” | Specified that the null concerns an association in the tested screen. |
| The dependency is weaker in solid tumours, and his tumour type is almost absent from the screen. | overstated | “genetic dependency on bortezomib's target is significantly weaker”; “solid-stratum association itself remains compatible with zero”; “his tumour type is essentially absent from the drug screen” | Specified an attenuated target association; retained the coverage limitation. |
| It also fails filter four for him: neuropathy in eighteen percent of children, on existing muscle atrophy. | supported | “neuropathy in 18% of children, on pre-existing muscle atrophy” | Retained as an observed paediatric-recipient rate and a current patient-specific objection. |
| In paediatric trials, bortezomib alone has never shrunk a solid tumour. | supported | “Single-agent bortezomib has not shrunk a paediatric solid tumour in a trial.” | Matched the report’s formulation. |
| If a tumour returns, the comparator changes from nothing to chemotherapy, and the question goes to a tumour board. | supported | “the comparator becomes chemotherapy rather than nothing”; “after the ex-vivo gate”; “possible addition to standard treatment, never a replacement” | Added laboratory testing and adjunctive-only framing. No automatic safety reversal. |
| The experiment that could prove us wrong: his own fibroblasts, a bortezomib dose–response, micronuclei among the survivors. | supported | “Patient dermal fibroblasts”; “a bortezomib dose–response”; “a micronucleus assay… on survivors” | Retained the experiment and added that sensitivity could indicate systemic toxicity. |
| Sized honestly, it needs twelve cultures per arm, not three; at three, power is seventeen percent. | overstated | “12 independent cultures per arm at f = 0.30, 23 at f = 0.20”; “None of the inputs is measured in these cells” | Removed. The unconditional count conceals model assumptions, including unsupported selectivity. |
| What changes his prognosis today is surveillance: renal ultrasound every three months to age seven, published consensus. | overstated | “The intervention that most changes this child's prognosis is surveillance”; “current age… must be confirmed first”; “regular clinical assessment” | Added age confirmation, birth-to-seven scope and clinical assessment. Removed the implied immediate eligibility. |
| Eight analyses pre-registered in git; where they came back against us, we report it. | supported | “eight pre-registrations that constrain the claim”; “the DepMap test came back against our mechanism” | Shortened to eight preregistrations constraining the claims. |
| What scales: the five-filter worksheet, for any rare disease where someone proposes an approved drug; and the replay tool, transferred to a second MVA gene from a fresh clone: rank one in all three genomes, three operational promises broken, and fixed. | overstated | “applies as questions”; “three of which the requirements list did not include”; “regression tests… did not. Both fixed” | Qualified worksheet transfer as questions. Replaced the inaccurate count of “promises” with provisioning and test failures. |
| What we hand over is not a prescription. | supported | “No drug should be started for this today”; “a prepared, evidence-bounded answer” | Retained in the close. |
| It is a prepared answer, written down now so nobody assembles it in a hurry, with the measurement that would overturn it. | overstated | “We have written that answer down now so nobody has to assemble it in a hurry”; “A negative fails to support transfer without closing the tumour-board question” | Replaced a single decisive measurement with measurements needed for reconsideration. |

# B. FINAL SCRIPT v5

Counts use whitespace-separated words; “forty-four” counts as one. Headings and count annotations are not narrated. Estimated narration is **161.92 seconds**, or **171.92 seconds** including the reserved ten seconds.

## S1

A child survived an embryonal rhabdomyosarcoma. His family shared his genome so that strangers might help. No disease modifying drug is supported for use today.

(25 words)

## S2

The presumed cause is two BUB1B variants. One introduces a stop. The other is a missense variant of uncertain significance. Whether they sit on opposite copies of the gene is not established.

(32 words)

## S3

Our replay tool plants alleles into public genomes. It measures retrieval given a perfect call, not diagnostic sensitivity. Transferred to a second MVA gene, it returned rank one in three backgrounds.

(31 words)

## S4

Five filters ask about approval, mechanism, exposure, patient safety, and direction of effect. A plasma peak is only an exposure plausibility check. Among surviving cells, does treatment worsen chromosome segregation?

(30 words)

## S5

Metformin remains unevaluable for aneuploidy selective activity. No effective concentration has been measured. Its proposed complex one mechanism needs concentrations roughly a thousand times therapeutic plasma levels. Other activity at those levels remains untested.

(34 words)

## S6

Bortezomib remains a conditional research candidate, with no established therapeutic exposure or tumour selectivity in MVA. The total plasma peak comparison does not exclude it, but establishes neither comparable free exposure nor duration at the target. Our public data analysis found an attenuated target association in solid tumours and no significant proteasome inhibitor association in the tested drug screen. That screen covered four hundred and forty-four solid tumour lines. His tumour type was barely represented.

(75 words)

## S7

Bortezomib fails his current safety filter. Neuropathy affected eighteen percent of paediatric recipients; he already has muscle atrophy. Alone, it has not shrunk a paediatric solid tumour in a trial. A new tumour warrants discussion at a tumour board only after laboratory testing, as a possible addition to standard treatment.

(50 words)

## S8

The proposed experiment tests his fibroblasts with bortezomib and measures micronuclei among survivors. Sensitivity could signal systemic toxicity, not tumour benefit. Surveillance is actionable now. Confirm his age first. Consensus recommends renal ultrasound every three months from birth to seven, alongside regular clinical assessment.

(44 words)

## S9

Eight preregistrations constrain the claims. The transferable product is the five filter worksheet, reusable as questions. The replay transfer exposed provisioning and test failures, since fixed.

(26 words)

## S10

This is a prepared answer, not a prescription. We have written down the uncertainty, and the measurements needed to reconsider it.

(21 words)

TOTAL: 368 words

# C. VISUAL BEATS

- **S1:** Typographic cold open: “No disease modifying drug is supported for use today.”
- **S2:** `fig2_domains.png`, highlight both variants with “Missense uncertain” and “Phase not established.”
- **S3:** Typographic: “Retrieval given a perfect call.” Avoid imagery implying validated diagnostic accuracy.
- **S4:** `fig3_funnel.png`, reveal the five filters sequentially; exposure must read as plausibility, with no bortezomib “pass” badge.
- **S5:** Typographic: “Unevaluable for aneuploidy selective activity.”
- **S6:** `fig4_depmap.png`, then `fig5_seguimiento.png`; retain confidence intervals and distinguish drug response from target association.
- **S7:** Typographic: “Bortezomib fails his current safety filter.”
- **S8:** Typographic cards, sequentially: “Sensitivity could signal systemic toxicity.” Then “Confirm his age first.”
- **S9:** Reuse `fig3_funnel.png` as a worksheet overview, captioned “Reusable as questions.”
- **S10:** Typographic: “A prepared answer, not a prescription.”

# D. THREE REMAINING JUDGE ATTACKS

1. **“Bortezomib remains a conditional research candidate, with no established therapeutic exposure or tumour selectivity in MVA.”**  
   Why prioritize it after the safety objection and weak solid-tumour evidence? The script honestly bounds the candidate, but cannot establish that it deserves priority over unresolved alternatives.

2. **“The proposed experiment tests his fibroblasts with bortezomib and measures micronuclei among survivors.”**  
   Feasibility remains unspoken: independent culture requirements depend on unmeasured assumptions, and fibroblasts cannot establish tumour selectivity. The toxicity warning helps, but does not resolve either limitation.

3. **“Eight preregistrations constrain the claims.”**  
   A count is not proof of prospective rigor. The excerpt acknowledges deviations, ad hoc statistics and a follow-up registered after the initial result. Judges can still ask exactly what was fixed before each analysis.