# Cursor (Grok 4.6 high) — crítica adversarial de los RESULTADOS de MVA-Replay y de la fase

`agent -p --mode ask`, 30-ago-2026. Mismo brief que Codex.

The design critique is closed. What follows is an attack on the write-up of the results, the causal stories attached to them, and the sentences you are about to put in Track 1.

---

## 1. The “24% was the wrong pair” claim

**1.1 Yes, it is an error.** `0.5506 → 0.4187` is the change in the *control* when two MVA-annotated terms are removed from it. That is a contamination audit. It is not a measure of what the patient’s phenotype is worth. Calling it “the size of the phenotype’s contribution” is false. The arithmetic of “about 24%” is `(0.5506−0.4187)/0.5506 = 23.97%`; the formula is fine, the pair is wrong.

**1.2 `28.7%` is the same formula on the right pair, and it is still the wrong kind of number.** `(0.5871−0.4187)/0.5871 = 28.7%` is “what fraction of this particular combined score disappears when we swap these two HPO sets.” That is a finite difference along one axis, at one operating point. It is not a compositional share. Three facts in *your own* results make the share language unsound:

- The combined score is not additive in phenotype and variant. Your FANCD2 table is the proof: a 0.13 phenotype-score gap coexists with a 3× combined-score gap. You cannot convert a delta into “the phenotype is X% of the score” unless the function is linear, which you have already shown it is not.
- `0.4187` is not a phenotype-free baseline. It is a *different* phenotype, still feeding the same non-linear combiner. The residual is not “the variant contribution.”
- `0.5871` is the **AD** row. The diagnosis is AR compound het (`0.5538`). A percentage of the wrong MOI row is not “the phenotype’s contribution to the case.”

**1.3 Experiment C makes the percentage contradictory even as rhetoric.** You cannot write “phenotype is 29% of the score” and “ClinVar is 88% of the score” unless you admit these are incommensurable contrasts (real vs unrelated HPO; two P/LP vs two different VUS). §0 says the conclusion “variant-driven, phenotype-consistent” is unchanged. That sentence is doing work the numbers no longer support. See §6.

**1.4 Do not spend a submission slot to replace 24% with 28.7%.** That is a rounding-error correction of a framing error. Withdraw the percentage.

**Sentence for the report:**

> With the patient’s eight HPO terms the BUB1B combined score is 0.5871; with five terms not annotated to OMIM:257300 it is 0.4187 (Δ = 0.1684). Both values reproduce to four decimals in three unrelated GIAB genomes. The 0.1684 is a local finite difference, not a fraction of the score the phenotype “contributes”: the combiner is non-linear, 0.4187 is not a zero-phenotype baseline, and 0.5871 is the AD row, not the AR compound-heterozygous row that matches the diagnosis. The figure of ~24% previously quoted compared two control runs (0.5506 vs 0.4187) and is withdrawn.

---

## 2. “The combined score is a property of the two alleles and the phenotype, not of the genome”

**2.1 Overstated, and on the verge of being a tautology.** Exomiser scores a gene from that gene’s contributing variants, the HPO query, and gene-level annotation. Plant the same two BUB1B alleles, keep the same HPO set, and the BUB1B combined score *must* repeat unless a background BUB1B allele also enters the contributing set. You already knew it would not: P-A2 says BUB1B is absent from the ranked table of all seven GIAB genomes, and the three spiked backgrounds are a subset of those seven. Reproducing `0.5871` in HG001/HG002/HG005 is the observation “these three genomes have no extra BUB1B allele that Exomiser keeps.” That is worth a sentence. It is not a discovery about “the genome.”

**2.2 What would break it.** A background BUB1B variant that survives `variantEffectFilter` and is marked contributing — a rare missense, a splice variant in the 3–4% of BUB1B that is outside the GIAB high-confidence BED, a second LoF. A scoring rule that is competition-normalised (you have no evidence of one). A 1000G sample; you have not planted into those yet. GIAB v4.2.1 being autosome-only and high-confidence-only makes the tautology easier to satisfy, which you declared.

**2.3 Rank is the thing the genome *does* change, and you used rank as the confirmatory endpoint anyway.** HG005 under unrelated terms: BUB1B stays at `0.4187` and falls to rank 3 because a background gene hits `0.8108`. That is the result. The section title denies it; P-B1 and P-B2 are rank predictions you mark confirmed.

**2.4 HG001 is almost inert as a rank witness.** Unspiked top score `0.0578`. C-lo at `0.1120` takes rank 1 there. FANCD2 at `0.1841` takes rank 1 there. Any planted construct above ~0.06 will take rank 1 in HG001. Every “k of 3” rank result in this file is, at best, a two-background result plus a free win. You do not say that.

**2.5 The four-decimal match to the patient’s T>G is more interesting than the match across GIAB genomes, and you bury it.** You planted ClinVar `T>A` (4600147), not the child’s `T>G`. Same codon, same protein, different nucleotide, different ClinVar status (VUS record vs absent). Combined score identical to four decimals. That implies the VUS ClinVar record on the missense contributes `0.0000` to the combined score; the planted missense is being scored as a rare protein-altering allele, not as ClinVar 4600147. If that is true, Experiment C’s language about “ClinVar’s whitelist” is almost entirely about the *nonsense* P/LP label, not about “two ClinVar records.” You cannot use the four-decimal reproduction as a finding about genomes and ignore what it says about which annotation is doing the work.

**Trivial-consequence reading, which is the correct one:** this is how a per-gene scorer behaves. The non-trivial residue is “no background BUB1B allele perturbed the three GIAB plants.” Report that. Retire the title.

---

## 3. Experiment C — “ClinVar is 88% of the score”

**3.1 The 88% is the wrong contrast, attached to the wrong architecture, described as if it were the same two variants.**

- C-hi alleles: `40165052` + `40218501` (first/last P/LP by position).
- C-mid alleles: `40209701` + `40220612` (the named Track 1 pair).
- C-lo alleles: `40161221` + `40220755` (first/last VUS by position).

Six loci, not three classifications of one pair. `0.8212 / 0.9332 = 88%` is “how much of the *two-P/LP* score disappears when we plant two *different* VUS.” Your case is C-mid. The analogous arithmetic on your case is `(0.5871−0.1120)/0.5871 = 80.9%`, and it is still the wrong experiment.

The sentence “had the child’s nonsense not been in ClinVar as Pathogenic, the same two variants would have scored 0.1120” is false. You never ran the same two variants with the P/LP label removed. You ran two other VUS, chosen as the positional extremes of a 1,430-record pool.

**3.2 The gradient is confounded with consequence, in silico score, and frequency, exactly as flagged before freeze.** The pairing rule is first/last by genomic position after a consequence filter. P/LP pools are LoF-enriched; VUS pools are missense-enriched. C-hi is very likely two LoF; C-lo is very likely two missense; C-mid is one nonsense + one missense. Variant scores will move with that, ClinVar or not. You already admitted the FANCD2 decoy was unmatched on variant strength (`0.8453` vs `0.9229`). C has the same unmatched-pool problem and you still interpret the entire `0.8212` gap as ClinVar class.

Directionally ClinVar class almost certainly matters: C-mid is ACMG PATHOGENIC, C-lo is UNCERTAIN_SIGNIFICANCE, and Exomiser is ingesting `PP5`. Magnitude “88% of *our* score” is not identified. Rank-loss “in two of three backgrounds” is identified only for the unmatched VUS pair, and one of those three is HG001 (see 2.4).

**3.3 C-lo still taking rank 1 in HG001 is the same background artefact as the decoy, not evidence about ClinVar.** `0.1120 > 0.0578`. That cell cannot support “would have lost rank 1.”

**3.4 What survives the objection.** A monotonic drop C-hi > C-mid > C-lo on *this* pairing rule, identical across three genomes, with ACMG class flipping at C-lo. That is enough to keep the qualitative Track 1 sentence that the P/LP nonsense is doing heavy lifting. It is not enough for 88%, and not enough for the counterfactual about “the same two variants.”

**3.5 The single extra run that settles it.** Plant the C-mid pair (`533901` + `4600147`) into one background (HG002 is enough) with `CLNSIG` rewritten to `Uncertain_significance` (and `CLNREVSTAT` left intact or stripped — pick one and declare it). Same loci, same consequences, same in silico scores, same frequencies, only the whitelist bit flipped. That cell is the actual counterfactual behind your Track 1 sentence. If you have a second cell to spend, do the reverse to the C-lo pair: rewrite both VUS to Pathogenic. You then have a 2×2 of {alleles} × {label} and can see whether class or consequence owns the gap. Everything else is commentary.

Until that run exists, replace the 88% sentence with: the positional P/LP pair scores 0.9332, the child’s architecture 0.5871, the positional VUS pair 0.1120; these are different alleles; the ClinVar-class effect is not isolated.

---

## 4. Phasing — “not computable”

**4.1 The conclusion is almost right. “Airtight” is not.** Two routes are closed as *routes*. One DNA-only check was not done. The Beagle sentence is correct for the mode you used and is not a complete statement of what short-read singleton data can do.

**4.2 (a) Beagle dropping target-only variants is documented behaviour, not a misconfiguration, given `ref=`.** With a reference panel, Beagle 5.x imputes and emits panel markers; markers present only in the target are ignored. That is why `40209701`, `40216470`, and `40220612` vanish and `40221421` survives. You ran an imputer. You did not run a cohort phaser. Saying “a reference-panel phaser can only place a variant that exists in the panel” is correct for this tool in this mode. It would be incorrect as a universal statement about Beagle: `gt=` without `ref=` phases the target cohort and can keep private variants. With *n* = 1 that mode has nothing to phase with, so it would not have saved you. The configuration matches the route you were testing. Do not claim you “tested statistical phasing” in general; you tested reference-panel imputation of two alleles that are not in the panel, which was guaranteed to drop them. The empty-interval argument (no panel-present het between the two sites) is the real result. The Beagle table is a consistency check, not independent evidence.

**4.3 (b) Short-read singleton methods you did not exhaust.**

Closed, and you can say so:

- GATK `PGT`/`PID` empty at both causal sites: they are not in one HaplotypeCaller active region. At 10,911 bp that is expected.
- PE-WGS read-backed phasing of the pair: insert sizes ~300–500 bp cannot span 10.9 kb.
- Bridging via the one intervening patient het (`40216470`): 6,769 bp and 4,142 bp. Still far beyond PE-WGS.
- Reference-free statistical phasing: one sample, four hets in 20 kb. There is no cohort LD to use.
- Allele balance: occupancy, not haplotype.
- ASE / transcript phasing: RNA, not this dataset.

Not closed, and this is the hole:

- **Read-backed phasing of allele 2 against `40221421`, 809 bp downstream, which *is* in the panel and which Beagle *did* phase.** GATK did not emit a phase set, which is suggestive, not exhaustive. WhatsHap/HapCUT2 on the BAM will use overlapping reads more greedily than HC’s `PGT`. A long-insert tail can cover 809 bp. You inferred “read-backed is closed” from the VCF. Physical phasing lives in the BAM. Until someone runs WhatsHap on `chr15:40209000–40222000` (or even `samtools view` for any read/pair covering both `40220612` and `40221421`), “not computable from this dataset” overreaches. The honest statement is: not computable from the VCF plus a 1000G panel; the only remaining short-read test is BAM-backed phasing of the 809 bp pair, which cannot by itself phase allele 1, and which you have not run.

No other singleton short-read trick gets you cis vs trans of a 10.9 kb rare/rare pair. Parents, long reads, or RNA remain the real answers. You already ranked those correctly.

**4.4 (c) Expected copy-count is the right argument for route 2, written one notch too coarse.** `AF × 6,404` is the right expected-count check for “will this allele exist in this panel.” Allele 2: `9×10⁻⁷ × 6404 ≈ 0.006`; ~10⁶ haplotypes for one expected copy. No public panel is near that. Allele 1: `1×10⁻⁴ × 6404 ≈ 0.64` is *not* hopeless for a larger panel — gnomAD-WGS scale is a few expected copies. So “a bigger panel would not fix this” is false of allele 1 and true of the *pair*. Rewrite: panel phasing of cis vs trans requires both alleles (or a het chain connecting them) to be placeable; allele 2’s frequency makes the pair unplaceable at any public panel size; a larger panel could at best sit allele 1 on a local haplotype, which does not answer the question.

**4.5 The Track 1 sentence you drafted is usable after two edits:** (i) replace “Our ranking pipeline is itself phase-blind” with the more precise pilot result — it *reads* phase into ACMG (`PM3`/`BP2`) and does not apply it to the compound-het model, penalty 0.34%, rank unchanged; (ii) add that BAM-backed phasing of the 809 bp neighbour was not done, if it still has not been done by the time you submit.

---

## 5. P-B3 falsified — mechanism vs story

**5.1 The verdict “falsified, 1/3 not ≥2/3” is correctly reported.** The mechanism paragraph is a story about two runs that never competed, plus a non-linearity claim that the BUB1B cells contradict.

**5.2 These are not a head-to-head.** Arm 2 plants FANCD2. Arm 1 plants BUB1B. The HG002 table that puts FANCD2 `0.1841` next to BUB1B `0.5871` concatenates two experiments. In the decoy runs BUB1B is not planted and, per P-A2, is not in the table. The pipeline did not “prefer BUB1B to FANCD2.” It assigned FANCD2 a combined score of `0.1841`, which beats HG001’s background (`0.0578`) and loses to HG002/HG005 backgrounds (`0.4881`, `0.4194`). That is a score-versus-background result. You do not even publish the HG002/HG005 decoy *ranks* — only “1 in 1/3 (only HG001).” If those ranks are 2 vs 40, the story changes. Missing numbers.

**5.3 HG001 again.** Rank 1 in 1/3 is rank 1 in the one background whose unspiked top is `0.0578`. P-B3 did not fail because the pipeline discriminated an MVA gene from a phenotypically plausible decoy. It failed because `0.1841` is a weak combined score relative to incidental GIAB tops. Amendment 3 making the decoy “stronger” (rank 58/69 → rank 1 in HG001) is still a score of `0.1841`. Stronger than a one-allele technical failure; not matched to BUB1B.

**5.4 The AD-row point is real, and it is not in your favour.** BUB1B’s headline `0.5871` is AD, variant term `1.0000`, one ClinVar-pathogenic nonsense. The AR row that matches MVA1 is `0.5538`. If you are celebrating P-B3 as “the pipeline discriminated,” you are celebrating a *dominant LoF* win in an AR disease gene. That is a known Exomiser behaviour (one P/LP LoF maxes the AD variant term). It is an argument that your Track 1 top row is the wrong inheritance model, not that the tool can tell BUB1B from FANCD2 under a compound-het architecture.

**5.5 “Steeply non-linear in the phenotype term” is not identified.** You compare FANCD2 AR (`pheno 0.6605`, `var 0.9226`, combined `0.1841`) to BUB1B AR (`pheno 0.7920`, `var 0.9615`, combined `0.5538`). Gene, phenotype score, *and* variant score all move. The missense in silico gap is admitted in the next paragraph. The comparison that *does* hold variant architecture fixed is P-B4: BUB1B `0.5871 → 0.4187` when only HPO changes. That is a 29% relative drop, not a 3× drop. If phenotype-term non-linearity were as steep as the FANCD2 paragraph claims, P-B4 would have been huge. It wasn’t. The 3× gap is mostly “different gene, weaker variants, different MOI-row winner,” not a measured phenotype elasticity.

**5.6 Alternative explanation, which fits every number you published:** the first/last FANCD2 pair is a weaker variant package than the named BUB1B pair, so its combined score is `0.1841` in every background. Rank 1 then occurs only when the background is as empty as HG001. You predicted a rank rate for an unmatched decoy. You falsified the rank rate. That does not demonstrate discrimination of gene identity, and it is not a win for the Track 1 framing.

**5.7 You predicted P-B3 as an argument *against* your submission.** Falsifying it in a way that depends on unmatched variant strength and on HG001’s empty background does not become evidence *for* the submission. Report the falsification. Do not cash it.

---

## 6. Where these results contradict you

Assuming, as requested, that the valuable finding is an own-goal. Several are.

**6.1 §0 vs §3: “variant-driven” vs ClinVar-driven.** §0 keeps “variant-driven, phenotype-consistent.” §3 says without the Pathogenic ClinVar call the score would be `0.1120` and would lose rank 1 in two of three backgrounds, “the dominant term, worth 88%.” Those cannot both stand. A molecular variant that needs a database gold star to score is not variant-driven. It is whitelist-driven. P-B2 (rank 1 with unrelated HPO in 2/3) already said the phenotype is not doing retrieval. P-A2 said the phenotype is not sufficient. Together: phenotype is neither necessary nor sufficient; ClinVar P/LP on a LoF is. The Track 1 slogan to retire is “variant-driven, phenotype-consistent.” The slogan the data support is “ClinVar-P/LP-LoF-driven, phenotype-modulated, inheritance-model-wrong.”

**6.2 The number you treat as “our Track 1 score” is the wrong MOI row.** You freeze `0.5871` as the estimand, reproduce it, test P-A against it, and then write in the decoy section that BUB1B wins on AD, “not on the recessive row that matches the actual diagnosis.” You cannot use `0.5871` as the case headline and treat the AD/AR split as a mechanism footnote. If the diagnosis is compound het, the number that belongs in the abstract is `0.5538`, or both rows, with AD-first named as a pipeline bias. As written, Track 1 is a 100/100 for retrieving the gene under the inheritance model the disease does not have.

**6.3 Phase: the caveat you already published is weaker than the result you now have, and the 100/100 does not survive it.** Pilot: cis vs trans does not change rank, combined score to three decimals, AR_COMP_HET call, contributing-variant flags, or PATHOGENIC. Phasing memo: cis/trans is not observable in this dataset. Joint implication: the compound-het interpretation is an analyst overlay. Exomiser would have given you the same Track 1 artefact if both alleles were cis, which is not MVA. “Phase not demonstrated” as unfinished work is false; “phase not observable, and the tool would not have used it” is the result. A leaderboard score for a compound-het call that is invariant to cis and that ranks AD above AR is not a compound-het result.

**6.4 Rank is declared non-portable, then used to confirm four of six predictions.** P-B1, P-B2, P-B3, and the C-lo rank-loss claim are rank endpoints. The one place rank actually moved with a fixed score (HG005 unrelated, rank 3) is the concession you pre-committed to. You cannot simultaneously teach the reader that rank is not portable and put rank on the scoreboard as confirmation.

**6.5 P-A “holds” on a test you declared biased in your favour, at a 0.025 margin, with effective *n* ≈ 3, with the burden table missing.** Pre-registration: GIAB is not clinical WGS; lower rare-variant burden *helps* P-A; report the burden table; never pool tiers; never call 7 samples 37 independent draws. Results: no burden table in the document you pasted, “P-A holds so far,” margin `0.025` (`4.3%`) against HG004 GJB2 `0.5619`. HG001 + two trios is three independent units, not seven. The score endpoint is *not* rescued by “rank is easier here”; you said that yourselves. What helps P-A is depressed healthy top scores. HG004 GJB2 is a real pathogenic incidental in a “healthy” genome and it already got within `0.025`. That is a near-miss against a biased null, not a confirmation. Putting “holds” on the scoreboard before tier 2, and before the burden table, contradicts the stopping/reporting rules you froze.

**6.6 P-B3 was pre-registered as an argument against you; the write-up spends its energy explaining why losing it is a win.** Combined with unmatched variant strength, Amendment 3, and HG001, this is the same class of error as v1’s escape hatch, just in the discussion section: a result that does not support the submission is being spent as if it did.

**6.7 The four-decimal identity of patient T>G and planted T>A contradicts any implication that the missense’s ClinVar record matters.** If you keep Experiment C as “ClinVar’s whitelist,” restrict it to the nonsense. The missense is a rare protein change. Your own plant shows the VUS accession is inert.

---

## 7. P-A — sentences to freeze now

The margin is `0.025` against a GJB2 incidental, on a null that you said is conservative in your favour, with two trios in the seven. Treat P-A as not yet a result. Freeze the following. Do not edit them after seeing the 30.

**If 0 of 30 exceed 0.5871:**

> P-A holds as pre-registered: 0.5871 is above every top-gene combined score in 7 GIAB genomes (max 0.5619, GJB2 in HG004) and in 30 unrelated 1000G genomes (max M, gene G, sample S). GIAB and 1000G are not pooled. Effective independence is ~33 unrelated individuals plus two trios, not 37 draws. Both callsets carry a lower rare-variant burden than clinical WGS, which lowers healthy top scores and biases this comparison in our favour; the margin over the GIAB maximum is 0.025. A biased null that we clear by 0.025 is not evidence that 0.5871 is diagnostic. It is evidence that it sat above this particular set of public genomes.

**If 1 of 30 exceeds 0.5871:**

> P-A failed. 0.5871 is below the maximum top-gene combined score observed in healthy genomes under the patient’s eight HPO terms (exceeded by 1 of 30 unrelated 1000G samples: gene G, score X, sample S; GIAB maximum remains 0.5619 in HG004 GJB2). The headline Track 1 number is inside the range this frozen pipeline produces from an unspiked public genome asked the same question. That is a negative result for Track 1. It goes in the abstract, not a footnote. We do not report a pooled GIAB+1000G percentile.

**If 2 or more of 30 exceed 0.5871:**

> P-A failed. 0.5871 is inside the healthy-genome range (exceeded by k of 30 unrelated 1000G samples; maximum M at gene G). A combined score that multiple unspiked public genomes also clear, under the same phenotype query, cannot be presented as a case-level result. Abstract: our headline score is not larger than every healthy genome’s top score.

**Also freeze, because you will be tempted:** if all 30 are below 0.5871 but any one of them lands in `(0.5619, 0.5871]` — i.e. closer than HG004 already got — you will not write “comfortably above the null.” You will write that two independent public genomes produce top scores within 5% of the case, and that the remaining gap is smaller than the phenotype finite difference you are no longer converting into a percentage.

---

**If you only change three sentences in Track 1:** withdraw the 24%/28.7% share; stop calling `0.5871` the compound-het result (it is the AD row, phase-invariant, ClinVar-P/LP-on-LoF-dominated); and do not describe P-B3 as a result in your favour. The extra cell that is actually worth running is C-mid with `CLNSIG` flipped to VUS, not another healthy genome.

