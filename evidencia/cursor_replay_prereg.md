# Cursor (Grok 4.6 high) — crítica adversarial del pre-registro MVA-Replay (v1)

`agent -p --mode ask`, 30-ago-2026. Mismo brief que Codex.

The design is a methods paper about Exomiser, dressed as a calibration of **your** 0.5871. The headline number is an AD row beating the AR row on a genome that already had the variants. Almost nothing below actually puts that number on a scale.

---

### 1. Where it is rigged in your favour (besides ClinVar circularity)

**1a. The phenotype is the answer key.**  
S1–S4 plant BUB1B / CEP57 / TRIP13 and query them with the patient’s eight MVA HPO terms. hiPhive’s phenotype score for those three genes under those terms is essentially fixed and high. Combined score is then “did the spike-in survive the variant filters?” Rank 1 is the tutorial case Exomiser was built for: right gene, right HPO, ClinVar-strength alleles, depleted competition.

The 18 extra S2 phenotype runs are the actual test. They are labelled “additionally”. They should be primary.

**Fix:** Pre-register a 2×2 as the main result: {MVA gene planted, decoy planted, nothing planted} × {eight real terms, five unrelated terms}. Sensitivity with matching HPO is a positive-control, not a finding.

**1b. Rank is the wrong metric on GIAB, and you lead with it.**  
GIAB v4.2.1 `*_1_22_*` is autosomes, high-confidence regions only. Fewer rare coding variants enter the gene table, so fewer competitors. Rank 1/N_GIAB is easier than rank 1/4565. You declare this as “sensitivity upper bound” and then still make P1/P2/P4/P5 about rank. Metric 7 counting genes ranked does not capture the thing that moves: **who is missing from the competitor set**, not how long the list is.

The planted gene’s **combined score** is mostly a function of (those two alleles + those HPO terms) and is comparable across backgrounds. Rank is not.

**Fix:** Primary endpoints: planted-gene combined score, top-gene combined score, and gap to runner-up. Rank-1 rate is secondary and labelled as an upper bound.

**1c. first / median / last is not the patient’s architecture.**  
S2 is titled “the patient’s own architecture”. It is not. It is some other P/LP and some other VUS, position-sliced. Those P/LP will disproportionately be LoF that the ClinVar whitelist plus pathogenicityFilter will carry; the patient’s hard allele is the missense VUS. You are measuring a easier molecular class and calling it a replay.

**Fix:** One locked pair per gene: the ClinVar records that match the Track 1 calls for BUB1B (public accessions, not patient VCF), and the analogous P/LP+VUS pair for CEP57/TRIP13 only if a VUS with `criteria_provided` exists. first/median/last can stay as a robustness appendix, not the case list.

**1d. Perfect calls.**  
`FILTER=PASS`, `QUAL=100`, `DP=44`, balanced AD, and (if you remember) a passing GQ, forced trans. That is a best-case VAF/GQ/DP draw through `alleleBalanceFilter` (VAF 15–85%, GQ ≥ 20, DP ≥ 10). Honest as a control for the filter; dishonest if you then talk as if you measured retrieval of clinical calls.

**1e. P1 is an escape hatch.**  
“If S1 fails, the benchmark is broken — we debug the spike-in.” That lets you iterate the insertion until the easy stratum works. Any fix that makes S1 work (normalise alleles, drop non-coding, add GQ, change contig prefix) also lifts S2–S4.

**Fix:** Freeze the builder after a **pre-unblinding** smoke test on **one non-MVA gene** (see 4). After that, S1 failure is a result. No debug-and-continue.

**1f. TTN is a straw-man decoy.**  
hiPhive will not confuse TTN with mosaic variegated aneuploidy. P5 is then “a cardiomyopathy gene did not win an MVA query.” Your own Track 1 already named the real distractor: **FANCD2 at 0.2137**.

**Fix:** S5 plants two P/LP in FANCD2 (or whichever gene is hiPhive rank 2 for the eight terms on an empty VCF — that gene, not a size decoy). If that steals rank 1, phenotype is not doing what you think. If it does not, you have a result.

**1g. “Reduced” HPO still contains the fingerprint.**  
HP:0002859 rhabdomyosarcoma + short stature is not a weak query. It still points at BUB1B. The unrelated five-term set is the control; the two-term set will be sold as a dose-response and it is not one.

**Fix:** Reduced = terms that are true of the patient **and** common (drop rhabdomyosarcoma), or drop reduced entirely and keep only full vs unrelated.

**1h. Null-B’s depleted genomes make P7 easier.**  
Healthy high-conf GIAB + frequency filters ⇒ weaker coincidental variant scores ⇒ lower top combined scores ⇒ 0.5871 looks more extreme than it would on a clinical WGS. You noted the direction for sensitivity; you did not note that it **helps P7**.

---

### 2. Null-B is not a valid null for the claim you want to make

Claim: “0.5871 is / is not a score a healthy genome routinely produces.”

**Null-B answers a different question:** “What top combined score does Exomiser emit when I throw a random OMIM-coherent 8-term query at these three GIAB slices?”

That can be interesting. It does not calibrate 0.5871.

Why it fails:

- **0.5871 was produced under one phenotype.** The matching null is unspiked genome + **those same eight terms** (Null-A). You already know this; you then buried it as n = 3 and put the 95th-percentile claim on Null-B.
- **hiPhive is VCF-independent.** For a coherent 8-term disease query, the disease gene’s phenotype score is high before any genotype is read. Combined score then depends on whether that gene (or a neighbour) has a passing rare variant in GIAB. So Null-B is mostly a distribution over **phenotype sets**, clustered inside **three genomes**, not a distribution over healthy genomes. Effective n for “a healthy genome” is 3, not 75. Treating the 4th-highest of 75 as a 95th percentile is theatre.
- **When the sampled disease gene has no passing variant, it may not appear at all** (PASS_ONLY). The recorded top score is then the best *other* gene that has both some phenotype similarity and a GIAB rare variant. That is a different generative process from “BUB1B with two real rare alleles and a matching phenotype.”
- **GIAB depletion biases Null-B downward**, so P7 is anti-conservative for the claim you will write in the abstract.
- **`genes_to_phenotype.txt` is gene–HPO, not disease–HPO.** If you sample “an OMIM disease” from that file you are at risk of sampling a gene’s term bag, which makes hiPhive’s match to that gene even tighter. Use a disease–phenotype map (`phenotype.hpoa` / equivalent) or say you are sampling genes.

**What would support the claim:**

Primary scale: **unspiked public genomes, fixed eight HPO terms**, record (i) top combined score, (ii) BUB1B’s combined score and rank (AD and AR rows separately), (iii) runner-up identity. That is Null-A, and n = 3 is too small for a percentile — so **do not claim a percentile**. Report the three numbers next to 0.5871.

To get a real distribution you need more genomes, not more phenotypes. GIAB has more than HG001/002/005 (HG003/004/006/007, etc.). 1000 Genomes 30× GRCh38 is public and can stay on the machine. 53 s/run; 100 genomes is an afternoon. Then a 95th percentile is a statistic.

Null-B, if you keep it, is labelled: “Exomiser’s top-score distribution over random Mendelian queries on GIAB,” and **P7 is withdrawn**. It does not go in the abstract as a calibration of 0.5871.

Your suspicion about hiPhive is right: with n_genome = 3, the top score’s variance is dominated by which phenotype set you drew and whether that gene happens to carry a GIAB rare variant. That is not “what a healthy genome produces.”

---

### 3. P1–P7: unfalsifiable, trivial, or not measured

**P1.** Unfalsifiable as a pipeline claim because you defined failure as a builder bug. As a spike-in-works check it is fine if you freeze the builder first. With matching HPO + ClinVar P/LP + GIAB depletion, rank 1 in 8/9 is close to trivial once insertion works. n = 9 cannot distinguish 70% from 99%.

**P2.** Falsifiable, underpowered, and not a replay of the patient (1c). 7/9 vs 5/9 is noise. Pre-register paired comparisons on the same gene × background, not two floating rates.

**P3.** The inequality `S3 < S2` is almost unfalsifiable in the sense you care about. S3 = 6/9, S2 = 7/9 satisfies it and does **not** show that Track 1 was a ClinVar-whitelist artefact. You need a **magnitude** (e.g. S3 rank-1 rate ≥ 20 pp below S2, or planted-gene score drop on paired cases) and a rule for “S3 ≈ S1 ⇒ rewrite Track 1” with a number, not a vibe. Also S3 can fail because first/median/last VUS are non-coding and `pathogenicityFilter` drops them — that is a pool bug, not a whitelist test. Restrict the pool **now** to consequences the frozen YAML keeps (coding / splice).

**P4.** Trivially true, and **you already measured it.** Track 1: BUB1B AD 0.5871, AR 0.5538, rank 1 is the **heterozygous** row. A ClinVar P/LP het in BUB1B under MVA HPO will produce a high AD row. Rank ≤ 3 in ≥ 50% of S4 is not a brave prediction; it is the Track 1 table. Measuring “AR_COMP_HET absent, AD row present, AD score still high” would be a metric. Rank ≤ 3 is not.

**P5.** Not a test of “phenotype contributes nothing.” TTN + MVA HPO is stacked to pass. n = 3, bar = 2. Replace the gene or drop the prediction.

**P6.** Not measured by the stated endpoint. Exomiser’s public behaviour: phased VCF is used for **ACMG PM3 / BP2**, not clearly for whether AR_COMP_HET is a compatible MOI. Two hets in one gene will likely still be **called** AR_COMP_HET in cis; cis may add BP2 and trans PM3 and the combined score may move. If you count “AR_COMP_HET called / not called,” S6 can come back 18/18 called and you will write “phase adds nothing,” which may be a wrong reading of a wrong endpoint. Endpoint must be: PM3 vs BP2 vs neither, Δcombined score, Δrank, and whether both alleles are contributing_variant. And only after a smoke test (4).

**P7.** Falsifiable on Null-B, but Null-B is the wrong distribution (2), so the prediction is not a test of the claim. 95th percentile of 75 clustered runs is also not a 95th percentile.

---

### 4. Technical traps that silently corrupt results

**4a. S6 / phase — this will waste 18 runs if you do not smoke-test.**  
Do this **once**, before the locked list, on a non-MVA gene: three tiny VCFs, same two P/LP, trans `0|1`+`1|0` same `PS`, cis `0|1`+`0|1` same `PS`, unphased `0/1`+`0/1`. Read the gene TSV and the ACMG evidence. If AR_COMP_HET is present in all three and only PM3/BP2 change, P6’s binary endpoint is void — amend it before unblinding, not after. If all three are identical, Exomiser is ignoring phase for ranking **and** ACMG, and S6 is 18 empty runs.

GIAB already has `PS` on some records. Spike-ins must share a **new** phase-set id, not join a neighbouring GIAB block. `|` without a shared `PS` may not count as one haplotype. Mixing `GT:DP:AD` into a `GT:PS:DP:ADALL:AD:GQ` file is legal per record; dropping `PS` on the spike-ins while cis/trans depends on `PS` is how you get “Exomiser ignored phase” as an artefact of your FORMAT line.

**4b. `alleleBalanceFilter` and your FORMAT.**  
You write `GT:DP:AD`, no **GQ**. The filter wants GQ ≥ 20. Missing GQ is an untested branch: either every spike-in is dropped (S1 collapses, you “debug”) or GQ is skipped and they all sail through. Write `GT:DP:AD:GQ` = het, `DP=44`, `AD=22,22`, `GQ=99`. Do not discover this on case 40.

**4c. PASS_ONLY hides the failure mode.**  
`analysisMode: PASS_ONLY` keeps only variants that pass **Exomiser** filters (not the VCF FILTER column; that is `failedVariantFilter`). A planted allele that fails frequency / pathogenicity / allele balance **never appears**. That looks like “planted gene not rank 1” (sensitivity miss) rather than “allele never entered the model” (technical failure).

**Fix:** For every case, assert both planted alleles are in the variants TSV with their filter/contributing flags. Absence = `technical_failures`, not a false negative. One FULL-mode dump on the smoke-test VCF to see reject reasons.

**4d. Insertion into GIAB is not “add a row and index.”**

- **Sample name.** Frozen `analysis_mva.yml` almost certainly names the patient’s sample. HG001/HG002/HG005 are different sample IDs. Wrong sample ⇒ empty or wrong analysis. The freeze must list the only fields allowed to change: VCF path, sample, `hpoIds`, output path.
- **Contigs.** GIAB is `chr`-prefixed. If `clinvar.vcf.gz` is not, you insert `15` into a `chr15` file and Exomiser never sees it.
- **CLNSIG exact match drops the real class.** ClinVar’s modal pathogenic bin is `Pathogenic/Likely_pathogenic`, not `Pathogenic`. Your pool rule as written can exclude the canonical alleles. Lock a parse rule now: P/LP = any CLNSIG atom in `{Pathogenic, Likely_pathogenic}` after splitting on `|` and `/`.
- **Exact POS drop is too narrow.** Overlapping deletion / different normalisation of the same indel / MNVs will not match POS and will create an illegal haplotype. Drop on any overlapping record, after left-normalising both to the same FASTA. “No hg38 FASTA” is a self-inflicted silent-miss generator; `chr15`/`chr11`/`chr5`/`chr2` FASTA is small. Without it you cannot prove REF.
- **first/median/last can be intronic.** Genome YAML often uses `pathogenicityFilter: {keepNonPathogenic: false}`. Those records vanish (4c). Restrict the pool to kept consequences **before** slicing, in this file, now.

**4e. What metric 7 does not capture**

- Autosomes only: no chrX/Y/MT competitors (filename is `_1_22_`).
- High-conf absence is not a filter tag; those variants **do not exist**, including rare variants **inside** BUB1B/FANCD2/TTN. TTN in particular is repeat-rich and depleted — another reason S5 is empty.
- Rank percentile vs a shorter list is not the same as “would still be rank 1 on 4565 genes.”
- Frequency databases know HG001 (NA12878 / 1000G CEU). Residual GIAB variants are a weird subset: common enough to be called, rare enough to pass your YAML. That is not a clinical singleton’s rare-variant burden.

---

### 5. The sentence a judge writes

*“They inserted ClinVar pathogenic alleles of the three known MVA genes into high-confidence GIAB autosome slices, queried them with the MVA phenotype, and Exomiser ranked those genes first. That is the software demo. It does not tell us whether 0.5871 is unusual, because the score was never placed on a null with the same HPO terms and a realistic competitor set — and their own Track 1 table already showed rank 1 was the AD row.”*

---

### 6. The single smallest change

**Kill Null-B as the scale for 0.5871. Make the primary locked experiment: the exact two Track 1 BUB1B ClinVar alleles, planted into the three GIAB genomes, each run with (a) the eight real terms and (b) the five unrelated terms, plus the three unspiked GIAB + eight terms (Null-A). Report AD and AR scores separately, and whether the planted alleles are contributing.**

That is 3 × 2 + 3 = 9 runs that actually put 0.5871 and the HPO-control anecdote on a rate. Everything else (S1, TTN, 25 random HPO sets, cis/trans until the smoke test) is appendix.

If you insist on one stratum to cut for costing nothing useful: **cut S1** (P1 already admits it is a builder check) **and S5-as-TTN**. Do not cut the unrelated-HPO S2 runs.

---

### 7. A cheaper, stronger experiment

Runtime is not your constraint. 150 × 53 s is a couple of hours. The constraint is **what a judge can be forced to believe**.

**Stronger than S6, and on your backlog:** statistical phasing of the **patient’s** two BUB1B variants locally (Beagle/SHAPEIT + 1000G/HRC panel, nothing leaves the machine). S6 tests whether Exomiser reads `PS`. The published caveat is that **this child’s** alleles have not been shown in trans. If the local phasing says cis, Track 1 is wrong regardless of any GIAB rank. If it says trans with a documented posterior, “phase not demonstrated” shrinks. That is a result about the case, which is what Track 1 is.

**Do not instead:** a fibroblast power analysis (a plan, which is what they already dinged) or the drug-filter engine (Track 2). ΔΔG on p.Asn1002Lys is a single number you can run in a day as a supplement; it does not scale 0.5871.

**Do this week, in order:**

1. Phase smoke test (4a) — 3 runs. Amend P6 or delete S6.  
2. Exact-allele slim replay (section 6) — 9 runs.  
3. Local phasing of the real BUB1B pair.  
4. Only then, if you still need a rate: more unspiked genomes × **fixed** eight HPO terms, not 25 random diseases.

The contradiction with your own data is P4 / rank-1-as-diagnosis: you already reported the AD interpretation winning. A 57-case matrix that rediscovers “Exomiser ranks a phenotypically matching gene with a ClinVar P/LP het near the top” is the seventh round of the same unmeasured claim.

