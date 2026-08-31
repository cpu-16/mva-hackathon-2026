# Cursor (Grok 4.6 xhigh) — ¿esto gana? Puntuación con la rúbrica y qué falta

`agent -p --mode ask`, 30-ago-2026. Mismo brief.

This is a spike: the output is a ranking call and a stop-list, not more analysis. I scored the four packages against the reports, `probando.json`, and the pre-registration — not the narrative.

**No. Not with what exists today.** A hostile mixed panel, after an honest rewrite of all four packages into Track 2, lands around **78–82**. That is a Community/Innovation-award package, not a first-place package. Fifty-two teams already have BUB1B at 100/100. You still recommend no drug, your own test weakened the only drug story, and the new mosaicism headline is a better detector for an architecture this child does not have.

The lead is right to refuse “stop and deliver.” He is not right if “continue” means more of the same Rigor. After one defensive repair, Rigor is close to saturated. The ceiling moves on Impact and Scalability, or it does not move.

---

## 1. Does this win?

**Scoring the four packages as the judges would**, after they are actually in the report (today they are not: Track 2 §5 still says ~14%, Replay is not in Track 2, mosaicism 2.1% is a memo).

| Package | Rigor (35) | Impact (25) | Innovation (25) | Scalability (15) | What a judge actually hears |
|---|---|---|---|---|---|
| **DepMap** | High. Pre-registered, lost, interaction p=0.026, ploidy out. | **Negative.** The tumour-board use-case is a solid tumour. | Modest. Public-data Spearman. | Near zero unless the script is the product. | “They killed their own candidate in the relevant lineage and kept it anyway.” |
| **MVA-Replay** | High, because of the retractions. P-A still open on a biased null, margin 0.025. | Zero for the child. Can hurt Track 1 if tier 2 fails. | Real: planting, the ClinVar counterfactual. | **Latent.** 61 locked runs are a reusable retrieval test. Currently a folder. | “The pipeline retrieves a dominant LoF row and is blind to phase. The analysts supply the recessive diagnosis.” |
| **Phase** | Closed correctly. | Small: “Sanger the parents.” | None. | Small: Exomiser is phase-blind. That is a methods fact. | “Compound het is an interpretation, not an observation.” |
| **Mosaicism** | High *with a hole you already named*, plus two you have not (below). | Only if you cash “no CHIP clone above ~2%” and “bulk cannot see MVA.” Zero if you lead with 6.8×. | The identifiability proof is the real result. The 6.8× is catching up to MoChA/hapLOH (2018), not beating it. | The proof transfers. The window statistic does not, until the noise model is controlled. | “They proved the disease is invisible in bulk, then advertised a 2% detector for clonal trisomy.” |

**Ceiling with what exists, written without the oversell:** roughly

- Rigor **84–88 / 100**
- Impact **68–72** (DepMap can *drop* this if Velcade stays the lead)
- Innovation **80–84**
- Scalability **70–74**

Weighted **~79–82**. Rigor is the closest to a cap. It is not capped yet: the κ hole and the unpowered §6 experiment are still live. After those two, further mosaicism work buys tenths.

**The single addition that raises the ceiling most is not the 1000G control.** That is a defensive repair: it stops a reviewer killing the mosaicism result with one sentence. It is worth doing in hours. It does not take 79 to 88.

What raises the ceiling is **one Impact artefact that changes this child’s next clinical step**, plus **one Scalability artefact another team can run on a different disease**. Those are named in §3. If you can only compute one new number, close κ. If you can only *build* one thing, do not build a better mosaicism detector.

---

## 2. Closing the overdispersion term

The 2.27× is not what you think it is. From `probando.json`:

- Per-site SD of signed BAF is **0.082–0.086 on every autosome**. Binomial at DP ~44 is ~0.075. Site-level κ is **~1.21**, not 2.27.
- Ψ is positive on all 22 chromosomes (3.7×10⁻⁵ to 1.2×10⁻⁴). That is **window-scale correlation**: averaging 125 sites does not reduce variance as 1/W.
- You then set `kappa_efectivo = 2.27` and plugged that into an **iid** beta-binomial Monte Carlo (`06_ventana.py`: independent site noise, then window mean). You stuffed spatial correlation into the iid parameter so that P4 (“if κ>4, reads become necessary”) would not fire.

That is the amendment you did not write.

**You do not need phase for the control.** Under the null, the sign is arbitrary. Unsigned window means of (BAF−0.5) measure the same extra-binomial term. Phasing 1000G samples *against the panel they sit in* would also be invalid: in-panel Beagle phase is nearly perfect, the patient’s is not. Skip it.

### Design, precise

**Pilot (2–4 hours, decide whether to continue):** stream chr8 (your lowest, 1.78×) and chr17 (your highest, 3.57×) for 10 samples, 2 per superpopulation. If the patient sits inside that envelope on both, the global 2.27× is technical and the rest is confirmatory. If chr17 is an outlier and chr8 is not, you have a chromosome-specific claim and the reads start to earn their keep.

**Confirmatory:** 30 unrelated (6 AFR / 6 EUR / 6 EAS / 6 SAS / 6 AMR), pre-declared, all 22 autosomes, same site rule as the pre-registration (biallelic SNV, panel MAF ≥ 0.01, GQ ≥ 30, DP window, same masks). Same W=125. Do not use 3,202. Do not download 41 GB.

**Two statistics, both unsigned, both depth-aware:**

1. **σ²_extra = var(b−0.5) − 0.25/DP** per chromosome. Additive technical bias. Comparable across 30× and 44×.
2. **κ_window = var(125-site mean of (b−0.5)) / (0.25/DP/W)**. This is the 2.27× you actually measured.

Report both. The ratio κ **will** make the 44× patient look worse than 30× controls even when the physics is identical: a fixed mapping bias is a larger multiple of binomial SE at higher depth. If you only quote κ, the comparison is invalid. Sensitivity: binomial-thin the patient’s AD to each control’s DP and recompute.

**Matched on:** site list (intersection with the panel), FILTER/PASS-equivalent at common SNPs, superpopulation envelope (you do not know ancestry, so the envelope is the result), DP via thinning. **Not matched on, and you say so:** caller (singleton GATK 4.2.4.0 vs NYGC joint `20201028` GATK), PCR chemistry, aligner. Joint calling is a real confound for rare hets and almost irrelevant at MAF ≥ 0.01, which is all you kept. Restricting to common SNPs is the mitigation, not a hand-wave.

**What distinguishes the two origins**

| | Technical (mapping / reference / library) | Biological (this specimen) |
|---|---|---|
| Patient vs 30 | Inside the DP-matched envelope on σ²_extra and κ_window | Outside, after thinning and after dropping the high-ref-bias / low-mappability tertile |
| Site class | Excess collapses when those tertiles go | Excess remains at unique, well-mapped sites |
| Chromosomes | Same rank order in controls (chr17 high in everyone is GC/mappability) | chr17/6/7/9 high only in the patient |
| Spatial | Correlation length matches mappability / LD / your 200 kb phase segments in controls too | Correlation length matches known mosaic-segment scales and is absent in controls |

**Falsify technical:** patient still outside the envelope after DP-thinning and after dropping the dirty tertile.  
**Falsify biological:** patient inside the envelope on both chromosomes in the pilot. Then you write: the 2.27× is the noise model of GATK AD at common SNPs, and the LOD stands as a second-order limit.

**You already had a cheaper half of this and did not run it.** The pre-registration named seven GIAB genomes as the calibration substrate. You used them for switch rate and for Replay. You never reported Ψ or unsigned κ_window on a healthy genome. If a GIAB GATK VCF with AD is on disk or streamable, that is the first five samples, before 1000G. If GIAB truth VCFs lack AD, 1000G is the right file and you were right to find it.

---

## 3. Impact and Scalability — real work, not prose

You have moved neither. Four packages of self-falsification are Rigor, and identifiability is Innovation. A clinician and a patient advocate still ask the same two questions they asked at 74.

**Impact (25%) — artefact: a one-page parental order, plus a sentence you already computed and did not cash.**

Impact means this child’s next month changes. You cannot start a drug. You cannot get age from a VCF. What you can do:

1. **Parental segregation + PCS, as a lab request, one page.** Two Sanger amplicons at `chr15:40209701` and `40220612`, interpretation table (each parent carries one → trans, diagnosis holds; one parent carries both → cis, Track 1 is wrong; PCS on parental lymphocytes per PMID 42434306). This is the only experiment in the whole project that can confirm the diagnosis, inform a future pregnancy, and explain HP:0200067. Cost: one day of writing. Cost to the family: two blood draws. This is already in §7 as a paragraph. It is not an artefact until it is a page a clinic can send.

2. **Cash the CHIP-negative.** You pre-declared del(5q)/−7/+8/del(13q)/del(20q) as therapy-related, and none is a spike. LOD ~2%. A post-ERMS child with **no detectable therapy-related clonal chromosomal lesion above ~2% of cells in the sequenced specimen** is a clinical sentence. You buried it under “we still cannot see MVA.” Cost: zero compute. Do not oversell it: CHIP is often point mutations, not whole-chromosome events, and tissue is unknown.

3. **§6 power, 2–3 days, no FASTQ.** This is still item 4 on your own board and still not done. If proteotoxic load scales with the aneuploid fraction, a 1–2% per-chromosome fibroblast culture is not Ippolito’s highly aneuploid lines. Either the linear model says the 72 h assay is blind — then you *change* the go-criterion, you do not hedge it — or it says a shift is expected, and you delete the “ambiguous negative” sentence. Until that number exists, §4+§6 is an Impact claim with an unpowered test. DepMap already predicts the solid-lineage attenuation; an underpowered fibroblast assay is how you launder that.

What does **not** move Impact: a better LOD, Replay tier 2, 1000G κ, aligning 85 GB, a ΔΔG on the VUS, another literature paragraph on surveillance.

**Scalability (15%) — artefact: Replay as a runnable spike test, plus two filled worksheets that disagree.**

The appendix table is not Scalability. It is a screenshot of a claim.

1. **MVA-Replay, packaged.** Input: a candidate gene, two alleles, an HPO set, a background VCF. Output: planted score, rank, the ClinVar-stripped counterfactual, the unrelated-HPO control. You have already run this 61 times. Another team with a different rare disease can spike *their* gene into HG002 in an afternoon. Cost: 3–5 days of wrapping what exists. This is the only computational artefact you have that another disease can use without this child’s data.

2. **Fill the five-filter sheet for MVA2 (CEP57) and MVA3 (TRIP13) as prospective transfers.** You already know the answers will differ: CEP57 has no embryonal-tumour risk (you cited this), so bortezomib’s tumour-board use-case dies at filter 2/4; TRIP13 should look like BUB1B. A framework that gives the *same* answer for three diseases is a slogan. A framework that kills the candidate in MVA2 and keeps it conditional in MVA3 is a demonstration. Cost: 2 days, papers you already have. No new compute.

Do not build the “five-filter engine.” DepMap did not give you a second filter-3 denominator in solid tumours. An engine with one evaluable row is theatre.

---

## 4. What neither of us has named

**The index tumour was never characterised.** Track 2’s prepared answer is for a *future* solid tumour. This child already had an embryonal rhabdomyosarcoma. Ippolito’s human signal is *tumour* aneuploidy versus proteasome-inhibitor response. You ran germline WGS and cell-line DepMap, and never asked what was known about the tumour that existed: karyotype, CMA, ploidy, histology report. If the challenge phenotype packet has it, you missed the only patient-tumour denominator in the project. If it does not, the honest Impact sentence is: *the prepared answer has no measurement from the tumour this child actually had.* That is a worse hole than uncontrolled κ, and it is sitting in the clinical document.

Second, quieter: **you are sitting on 0/3 Track 2 submissions with a working package and a video that only needs a URL.** Continuing analysis and burning the quota are not opposites. Submit this week with current honesty (video v3, not v1). Keep two shots for the rewrite. Eight weeks of “not until it’s good” is how a 24 October close date meets 0/3.

---

## 5. Do the 85 GB still earn their cost?

**Optional for mosaicism. Not optional for one pileup, and only after CRAM exists for another reason.**

The overdispersion question is a VCF-vs-VCF question. Unsigned κ_window on streamed 1000G AD closes it without a single read. The identifiability proof does not use reads. The CHIP-negative does not use reads. GC-LOESS would clean the *old* dosage plot in `MOSAICISMO.md` (+2.9% to +7% on chr16–22). That is a correction you owe the published 14% section, not a prize.

What still justifies alignment, in order:

| | Justifies 85 GB? |
|---|---|
| **N1002K pileup (DP 28 vs genome ~44)** | **Yes, as a kill-switch, cheap once CRAM exists.** GQ 99 and AD 15,13 are not a pileup. If this call is a mapping artefact, Track 1 is wrong and every package downstream is decoration. Two hours after CRAM. Not a reason to *start* a 48-hour align if the 1000G control is the live experiment. |
| **Insert-size + spanning pairs at 10,911 bp** | You owe the measurement because you published “no alignments.” Geometry already says zero spanning pairs. A histogram is a sentence, not a differentiator. |
| **Unbiased depth / GC-LOESS** | Companion. Pre-register that the chr16–22 “gains” vanish. If one remains, that is a finding. It does not take variegation over 2%. |
| **WhatsHap on the BUB1B window** | Same as insert size. Allele 2 is 809 bp from `40221421`; allele 1 is 10.9 kb away. It cannot answer cis/trans. |
| **Haplotype BAF from the BAM rather than the VCF** | No. You already ran the VCF version. Re-running it on a pileup you control is a methods footnote unless the 1000G control says the GATK AD is the problem *and* the patient is still an outlier. |

Honest answer: **do not make alignment the main path.** Finish the 1000G pilot this week. If the patient is inside the envelope, alignment drops to “N1002K kill-switch when disk and time allow,” not “the thing we continue with.” If the patient is a clean outlier on well-mapped sites after DP-thinning, then the BAM is how you show the extra variance is not a caller artefact — and only then.

You already have 2/8 FASTQs. Read the headers for library chemistry (PCR vs PCR-free) before you design the 1000G match. That is ten minutes. It is the confound that actually matters, and it does not need minimap2.

---

## 6. What I would stop

Stop treating the 6.8× as the mosaicism headline. Stop stuffing window correlation into iid κ. Stop expanding Replay (let the 30-genome tier finish; it is a loaded falsification; do not add arms). Stop re-phasing the two BUB1B alleles. Stop the ΔΔG/AlphaFold path unless the pLDDT abort fires, in which case stop anyway. Stop the five-filter engine. Stop genome-wide SV, re-calling, ichorCNA, and anything that needs the 4060 to look used. Stop writing “the recessive interpretation is supplied by the inheritance model **and the phenotype**” — Replay §4b already killed the phenotype’s role and §5 still says it. Stop sitting on 0/3.

**Do, in this order, and then rewrite and submit:**

1. **Submit Track 2 this week** with what you have, video v3. Quota is a tool.
2. **Unsigned κ pilot on 1000G** (chr8 vs chr17, 10 samples). Hours.
3. **§6 power calculation.** 2–3 days. Then change §6 or delete the hedge.
4. **Let Replay tier 2 finish.** Write the pre-committed sentence. If P-A fails, it goes in the Track 1 abstract, not a footnote.
5. **Parental-order page + CHIP-negative sentence + MVA2/MVA3 worksheets + Replay wrap.** That is Impact and Scalability. Days, not weeks.
6. **N1002K pileup** only if you align; alignment only if (2) says the patient is an outlier, or if you need the kill-switch for sleep.

Eight weeks of (2)–(5) is “insisting until something good.” Eight weeks of a better mosaicism statistic is the scope creep you were warned about, just wearing a pre-registration.

---

## The claim that contradicts your own data

You asked for one. It is in mosaicism, and it is worse than the uncontrolled-κ sentence you already wrote.

**“The excess is global, and it cannot be mosaicism.”**

Three facts in your files, together, make that sentence false as written.

**First: you converted a variance into a mean shift.** Median 2.27× → “~3.1% directional imbalance on every autosome.” That 3.1% is `4 × sqrt(excess × binomial/W)`: the cell fraction that would produce this much Ψ *if Ψ were a squared mean shift*. Ψ is `mean(φ_s² − v_s)`. Extra window variance and a directional clone both raise it. You cannot interpret the former as the latter and then call the latter absurd. That is the category error a reviewer needs one sentence for.

**Second: the decision rule cannot see the alternative you named.** Robust z of 22 chromosomes against *each other*, threshold |z|=3. A global process — technical *or* mosaic — is absorbed into the centre by construction. chr17 at +2.88 is “not a spike” because you residualized the spike out. The LOD calibration used a Monte Carlo null at genome-wide FPR 5%. The proband was called with a different test. The test you applied is blind to “every autosome a bit elevated,” which is what you then said the 2.27× would have to be in order to count, which is why you said it cannot be mosaicism.

**Third: chromosome-wide φ on chr17 is +0.00181.** If that were directional mosaicism, f ≈ 0.73%, far below your LOD. The high Ψ on chr17/6/7/9 is window variance, not a preferred homologue. Your own secondary statistic (the one you originally pre-registered) already says there is no directional clone. You did not need the 3.1% conversion, and using it overclaims what Ψ can rule out.

Separately, and this one is in Replay, still live in the text: **§5 says the recessive interpretation is supplied by “the inheritance model and the phenotype” after §4b showed the phenotype does not select the disease mapping.** The winning row is still AD, 0.5871 against the AR compound-het 0.5538. Combined with the phase pilot (cis and trans: same call, same class, same rank, Δ = 0.0034), Track 1 is a dominant LoF retrieval that you interpret as recessive MVA. That is not a scandal if you say it. It is a contradiction if §5 still credits the phenotype.

DepMap is the clean one: it went against you and you reported it. The unclean move is keeping Velcade as the prepared answer for a second **solid** tumour after you could not extend the dependency to solid lines, while §6 remains an assay you have not shown is in the right effect-size regime. That is not a number contradicting a number. It is the lead of Track 2 contradicting §3.5.

---

So: the lead asked if you are sure, and if this wins. You should not be sure, and it does not win yet. What you started and have not finished is the noise model, the power of the experiment you are still proposing, the parental artefact, and packaging Replay so someone else can use it. What you started and should not continue is a third mosaicism statistic and 85 GB as a personality test.

