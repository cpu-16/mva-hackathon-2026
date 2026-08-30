Using the brief’s required format. This is a ranked list of things to **compute**, not another write-up and not an implementation plan. I treated the family page, funnel figure, blank worksheet, metformin/bortezomib PK, mosaicism LOD, Exomiser HPO controls, surveillance consensus, and the §6 wet protocol as already done.

---

## Ranking rule

**(weighted points you could actually pick up) / (person-days).** Current Track 2 is ~74–78 because both judges said the same thing: the science is careful and the transferable framework is asserted, but **nothing new was produced that could have come out the other way.** Track 1 is saturated at 100. The remaining room is Innovation and Rigor, then making the five-filter claim an artifact.

Killed on sight (not below): surveillance-calendar PDF, dashboards, another literature pass, ClinicalTrials.gov, wrapping Track 1 in Nextflow, GPU AlphaFold-from-scratch, PGx star-calling (bortezomib has no CPIC pair; a `*1/*1` result is a shrug), un-preregistered “modifier fishing,” re-running Exomiser, re-doing BAF/LOD.

---

## 1. DepMap/PRISM locked test: does the proteasome-inhibitor story survive in solid tumours, and does anyone else become evaluable?

**One sentence.** A pre-registered computational experiment on public cell-line data that can give trametinib (or nobody) a real filter-3 denominator, and that can kill the tumour-board use-case if the Ippolito association is myeloma-only.

**What is actually computed**

- **Inputs (all public, CPU):** latest DepMap release (24Q4 or 25Q2) — `Model.csv`, PRISM Repurposing (AUC / log-fold-change), CRISPR gene effect, RNA-seq, and a published aneuploidy / CIN score already packaged for those lines (Cohen-Sharir or Taylor, whichever the release ships). Drug list locked *before* looking at PI results: bortezomib, carfilzomib, ixazomib, metformin, trametinib, everolimus, plus one negative-control cytotoxic (e.g. paclitaxel) so a global “sick-cell” confound is visible.
- **Method:** for each drug, Spearman ρ of sensitivity vs aneuploidy in (i) all lines, (ii) solid-tumour lines only, (iii) haematological lines only. Lineage as a mixed-effect covariate (`statsmodels`). Secondary, also pre-registered: partial correlation of PI sensitivity vs aneuploidy **after** BUB1B expression; and BUB1B CRISPR dependency vs PI sensitivity. Multiple-testing: 7 drugs × 3 strata, FDR.
- **Outputs a judge can open:** a frozen `hypotheses.yaml`, a `.csv` of ρ / n / p / FDR, one forest plot, and a one-row verdict per drug: `evaluable_filter3` / `not_evaluable` / `association_confined_to_haematological`. No patient genotypes leave the machine.

**What is NEW.** Ippolito’s human signal is myeloma (n = 8 vs 50). You currently have **no number** that speaks to embryonal solid tumours, and you left carfilzomib, ixazomib, and trametinib as “not evaluable” because no CIN-stratified EC50 exists in the papers. This produces that number (or a documented absence) on one matrix, for the drugs you already care about. It does not exist as a table in the literature for this locked set.

**How it is falsified.** Pre-register the signs. Predicted: PI ρ in the sensitive direction in all lines **and** in solid-only; metformin ρ ≈ 0; everolimus not more sensitive (your antagonism is a combo claim, but monotherapy should not look like a PI). **Negative results that matter:** (a) PI association vanishes in solid-only — the tumour-board story for a second ERMS is computationally unsupported; (b) metformin is as aneuploidy-selective as bortezomib in PRISM — the filter-3 kill needs to be rewritten, not defended; (c) trametinib acquires a clean CIN-stratified contrast — you suddenly have a second evaluable candidate (the clinician request the r7 judge already made). A result that cannot change the report is not this proposal.

**Effort.** 4–6 person-days. CPU-only (pandas / scipy / statsmodels). Downloads are large but not GPU.

**Rubric.** Innovation 25% (this is the missing *result*) ~+8–12; Rigor 35% ~+4–6 if the solid-tumour split is honest; Impact 25% ~+3–5 only if a denominator appears or the ERMS use-case is explicitly weakened. Weighted ~4–7 points. Ceiling: a judge can still say “cell lines are not MVA.”

**Biggest reason it might not work.** PRISM AUC is not an EC50 in a reversine-isogenic pair. A null in solid tumours may be underpowered (few RMS lines) rather than a real absence — and you will be tempted to over-read it. Pre-commit: if n_RMS < 10, the RMS-only test is descriptive and does not get a p-value.

---

## 2. Proteotoxic-burden scaling: is the §6 fibroblast assay even in the right effect-size regime?

**One sentence.** Turn the §5 / §6 contradiction the judges already named into a number: predicted PI effect size at constitutional mosaic fractions versus Ippolito’s highly aneuploid lines.

**What is actually computed**

- **Inputs:** your already-measured bulk LOD (~14% clonal trisomy; 1–2% per chromosome if 30% of cells are aneuploid and variegated — `MOSAICISMO.md` / report §5); Ippolito Fig. 6o contrast (highly aneuploid vs near-euploid, EC50 < 40 nM as you already bound it); a stoichiometric imbalance model from the aneuploidy-proteotoxic literature (protein excess scales with the copy-number-deviant fraction of the proteome, not with “has MVA: yes/no”).
- **Method:** parameterise predicted proteotoxic load as Σ_chromosomes f_c × proteome_mass_c, with f_c drawn from (i) Ippolito-like whole-chromosome gains in a large fraction of cells, (ii) MVA-like variegation at 1–2% per chromosome, (iii) a sweep of f from 0.5% to 30%. Map load → expected EC50 shift under two models you declare in advance: linear, and a threshold (dependency only above some load). Do **not** fit to Ippolito and then “predict” Ippolito.
- **Outputs:** one plot of predicted EC50 ratio vs mosaic fraction, with two marked points (Ippolito regime, this-child regime), plus a table of “minimum f at which a 72 h fibroblast assay with n = 3 biological replicates has 80% power to see Ippolito’s contrast,” using a simple two-sample t-power calculation on log-EC50.

**What is NEW.** You currently *say* a fibroblast negative is ambiguous. You have not computed whether the assay as written is expected to be blind. That number does not exist.

**How it is falsified.** Linear model predicts a shift below the noise of a 3-replicate 72 h assay at 1–2% per chromosome — that is a **positive finding** (the design is underpowered; §6 must change). The result that kills the proposal is the opposite: even the linear model predicts a detectable shift at 2%, in which case the “ambiguous negative” hedge is unnecessary and should be deleted. Threshold-only models that can fit anything are not allowed as the primary.

**Effort.** 2–3 person-days. CPU-only. Uses work you already did; does not re-derive BAF.

**Rubric.** Rigor 35% ~+6–8 (this is the remaining prize-losing hole in §6). Weighted ~2–3 points. Tiny effort. Does not move Innovation much unless you then **change** the proposed experiment (e.g. require an aneuploidy-high positive control as the actual go-criterion, which you already hint at).

**Biggest reason it might not work.** Proteotoxic stress may be a switch, not a dose. A hostile reviewer will call a linear scaling “an essay with an axis.” Mitigate by leading with the power table (n, σ, detectable ratio), which is ordinary assay statistics, and treating the stoichiometric model as a sensitivity analysis.

---

## 3. Statistical phasing of p.Leu737Ter and p.Asn1002Lys from the singleton VCF

**One sentence.** A local, inspectable P(trans) for the two BUB1B alleles, which the diagnosis currently leaves at 50/50 because there is no BAM and no parents.

**What is actually computed**

- **Inputs:** a **local** slice of the patient VCF, `chr15:40,000,000–40,400,000` (the two sites are `15:40209701` and `15:40220612`, ~11 kb apart). Reference haplotypes: 1000 Genomes 30× GRCh38 or the HGDP+1kGP panel, on disk. **Do not** upload this window anywhere; named variants may be published, the surrounding singleton genotypes may not.
- **Method:** Beagle 5.4 and SHAPEIT5 independently, using only SNPs with DP ≥ 20 and GT = het/hom in the window. Report the phase of the two rare alleles relative to the common haplotype background, with genotype probability / switch quality. Concordance between the two callers is the QC.
- **Outputs:** `phase.json` with P(cis), P(trans), n_hets_in_window, mean switch quality, and a 20 kb haplotype plot (common SNPs only — no rare-allele list for the rest of the genome). A one-line verdict: `trans_supported` / `cis_supported` / `uninformative`.

**What is NEW.** No published phase exists for this pair. Read-backed phasing is impossible (you already checked: no `PGT`/`PID` on either site; GATK *did* phase FANCD2 in the same file). A probability that is not 0.5 is a new fact about this child.

**How it is falsified.** Parental segregation (the real test). Computationally: P(trans) ∈ (0.3, 0.7) or the two callers disagree → **uninformative**, and you report that as the result, not as a failed project. A confident **cis** call would undermine the compound-het interpretation and would have to go in the report as a problem, not a footnote.

**Effort.** 2–3 person-days. CPU-only. Beagle on a 400 kb window is minutes.

**Rubric.** Rigor 35% ~+6–10 if |P−0.5| is large and both callers agree; ~+1 if uninformative. Impact small. Weighted EV ~1.5–3 points. Kept this high because the brief asked for patient-specific claims and the effort is small enough that an uninformative outcome is cheap.

**Biggest reason it might not work.** Both alleles are ultra-rare. Reference panels phase *common* haplotypes; two private variants can sit on the background with essentially no information. Then you have computed a precise 0.5, which a judge will not reward. Stop after QC; do not “interpret” a coin flip.

---

## 4. Calibrated computational assay of p.Asn1002Lys (and NMD fate of p.Leu737Ter)

**One sentence.** Put this VUS on a number line next to every published BUB1B missense that already has a ClinVar or functional label, and state whether it is milder than L1012P — the prediction you already made from Sieben and have not tested.

**What is actually computed**

- **Inputs:** AlphaFold DB `AF-O60566` (no GPU folding); the human BUB1B missense set from ClinVar + the MVA literature (including **L1012P**, the Sieben allele ten residues away); MANE transcript `ENST00000287598.11` for NMD geometry.
- **Method (CPU):** FoldX `RepairPDB` + `BuildModel` (or ThermoMPNN if you want a second, independent ΔΔG; it is a forward pass, not training). Same pipeline on the whole calibration set *before* looking at N1002K. Primary metric: ΔΔG vs L1012P, not vs wild type alone. Secondary: NMDEscPredictor / 50-nt rule for L737X (last exon-exon junction on MANE). Optional cheap orthogonal: Ensembl VEP REST **for the two named variants only** (SpliceAI lookup) — they are already publishable.
- **Outputs:** ROC of ΔΔG for P/LP vs B/LB in the calibration set; a strip plot with N1002K and L1012P marked; NMD call with the junction distance in bp; a one-line verdict that is only allowed if calibration AUROC ≥ 0.7.

**What is NEW.** You state in §1 and §10 that **no functional assay of p.Asn1002Lys exists.** A calibrated ΔΔG and an NMD geometry number are not in any paper about this allele. The Sieben inference (“must retain more residual function than L1012P or the child would not be alive with a truncating allele”) becomes a quantitative claim.

**How it is falsified.** Two different failures, both publishable: (1) calibration AUROC < 0.7 → you **do not interpret** N1002K; the result is “this method cannot rank BUB1B missenses,” which is a result. (2) N1002K is predicted **more** destabilising than L1012P → your hypomorph story is in trouble (or FoldX is wrong; you only get to pick that if calibration failed). NMD: if L737X is predicted to escape NMD, the “truncation removes the kinase domain” cartoon has to live with a possible dominant-negative peptide; if NMD is predicted, the protein-level kinase-domain figure is a map of what is *lost*, not of what is *present*. Wet falsification remains §6 allele-fate (RT-PCR ± NMD inhibitor), which you already designed.

**Effort.** 5–7 person-days (most of it is the calibration set and not fooling yourself). CPU-only. FoldX on one domain is hours, not days.

**Rubric.** Rigor 35% ~+5–8 if calibration works; Innovation 25% ~+3. Weighted ~3–4 points. If calibration fails and you still quote a ΔΔG, this becomes a net loss.

**Biggest reason it might not work.** BubR1’s C-terminal fold is a contested kinase; AlphaFold confidence in that region may be poor (check pLDDT *before* FoldX). ΔΔG on a low-pLDDT segment is theatre. Pre-commit: if mean pLDDT in 766–1050 < 70, abort the stability arm and ship only the NMD geometry.

---

## 5. A runnable five-filter engine whose first real output is a census, not a worksheet

**One sentence.** The artifact you already claimed in §9: a CLI that fills the five filters under the same “do not invent a denominator” rule you used by hand, run once on a locked list of approved drugs so a judge can re-run it.

**What is actually computed**

- **Inputs:** `candidates.yaml` (locked list: all FDA-approved proteasome inhibitors, AMPK-related diabetes drugs, MEK inhibitors, mTOR inhibitors, HSP90 agents — the union of Tang / Ippolito / Schukken neighbourhoods that actually have a marketed molecule); `cmax_table.tsv` **hand-curated** from the FDA labels you already extracted (do not NLP-parse DailyMed; that is how you invent a numerator); `patient_flags.yaml` derived from this child’s HPOs (muscle atrophy, FTT, nephrocalcinosis, prior embryonal tumour) as coded contraindications; optional `denominators.csv` from proposal 1.
- **Method:** ChEMBL REST (and nothing else) for assays whose description / tissue / cell line matches a **pre-registered** keyword list (`aneuploid`, `CIN`, `trisom`, `reversine`, plus Ippolito/Tang assay IDs if present). If zero hits → `filter3 = not_evaluable`. Never fall back to a myeloma IC50. Filter 1 = openFDA marketing status. Filter 4 = overlap of `patient_flags` with a small, hand-mapped AE table (neuropathy, cardiotoxicity, nephrotoxicity, immunosuppression) — boolean, not an LLM. Filter 5 = `unknown` unless a pre-registered literature flag exists (you do not have a computational mis-segregation assay from a VCF).
- **Outputs:** `filled_worksheet.csv` + `verdict.json`; a pytest fixture that **must** reproduce your current rows (metformin `not_evaluable` at 3, bortezomib pass 3 / fail 4) from frozen inputs; a census line: `N candidates, K evaluable at filter 3, M pass 1–3`. MIT-licensed script in the public repo, with no patient VCF inside.

**What is NEW.** The blank appendix is not runnable. A census of “how many approved drugs in this mechanism neighbourhood even have a legal denominator” does not exist. If ChEMBL has a CIN-stratified carfilzomib EC50 you missed by hand, that is a new evaluable row. If it has none, the absence is now a query a rival can re-run, not a paragraph.

**How it is falsified.** The frozen regression test fails against your own published rows → the engine is wrong. A CIN-keyword hit that on inspection is a junk assay → you tightened the keyword list too loosely (report the false-positive rate on a labelled sample of 50 ChEMBL rows). The result that would change the science: K > 1 at filter 3 (someone other than bortezomib is evaluable) or K = 0 (then your bortezomib row is also not machine-justified, and you have a problem).

**Effort.** 7–10 person-days. CPU-only. Most of the time is the denominator rule and tests, not the CLI.

**Rubric.** Scalability 15% ~+8–12 (this is the only proposal that moves the criterion you are currently faking with a worksheet); Innovation ~+3–5. Weighted ~2–3 points. Lowest ratio of the five; kept because the brief asked for the framework as an artifact and a clinician can run it on the next child without reading 29 pages.

**Biggest reason it might not work.** ChEMBL will not contain Ippolito’s figure-read <40 nM. If the engine cannot ingest a **manual, cited** denominator as an explicit override (with a `source=figure_read` flag), it will mark bortezomib not evaluable and contradict the report. Build that override first, or this tool attacks you.

---

## What to actually do in 8 weeks

Do **1 and 2 in parallel in the first 10 days.** They are the only items that can change what the Track 2 document *says* (solid-tumour PI association; §6 underpowered; metformin unexpectedly selective; trametinib evaluable). Then 3, because it is two days and uses the patient’s VCF. Then 4 only if AlphaFold pLDDT clears the gate. Then 5, feeding denominators from 1, if and only if 1 produced at least one machine-readable contrast — otherwise you are wrapping the current worksheet and the judges will see it.

If only one thing gets built: **proposal 1.** It is the first result in this project that could come out against you in public, on a dataset anyone can download.
