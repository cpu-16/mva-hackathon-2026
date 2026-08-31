Fourth round. You have reviewed the benchmark design, its results, the corrected reports, and the
raw-data strategy. The team lead has pushed back on me and he is right, so I am putting his question
to you unfiltered.

His words: *"¿ya estás seguro de todo? ¿con lo que tienes ganamos? te dije mil veces hay que seguir
insistiendo hasta lograr algo bueno, por eso te dije que te apoyes de codex y cursor."*

I had just recommended stopping the analysis and moving to delivery. He rejected that. He is right
that I overcorrected: your earlier warnings about scope creep were about unfocused expansion, not
about finishing what we started. So: **we are continuing, and the question is what to continue with.**

# Where we actually are, today

Closing date 24 October 2026. Track 1 submitted twice, scored 100/100 by the automated evaluator
(the evaluator scores the CSV, not the report). Track 2 written, **zero of three submissions used**.
Two AI judges scored the package 72→78 and 65→74 on the official rubric
(Rigor 35 / Impact 25 / Innovation 25 / Scalability 15). 52 other teams already had BUB1B.

**Four pre-registered result packages now exist, each committed to git before it ran:**

1. **DepMap/PRISM.** The aneuploidy–proteasome dependency our Track 2 candidate rests on is
   lineage-restricted: no proteasome inhibitor reaches FDR<0.05 in solid lines, PSMB5 CRISPR
   dependency ρ=−0.077 q=0.118 in solids vs ρ=−0.261 q=0.042 in haematological, interaction p=0.026.
   This child's tumour was solid. **Went against us; reported.**

2. **MVA-Replay**, 61 runs on public genomes. Seven healthy GIAB genomes queried with the child's
   eight HPO terms top out at 0.5619 against our 0.5871 — margin 0.025 on a null we declare is biased
   in our favour. Planting the two ClinVar alleles into three unrelated healthy genomes reproduces
   0.5871 and 0.4187 to four decimals. Stripping both ClinVar classifications costs only 0.0128 and
   does not lose the top position — **refuting our own published claim** that the ClinVar whitelist
   carried the ranking. A 30-genome tier is still running; that prediction is open.

3. **Phase.** Not resolvable: no alignments were downloaded at the time, no GATK phase tag, 10,911 bp
   apart, and all three heterozygous sites inside the interval are absent from the 1000 Genomes
   3,202-sample panel, so Beagle drops them. Also: Exomiser reads phase into ACMG evidence but not
   into the compound-het model, so cis and trans give the same call, class and rank.

4. **Mosaicism — the newest and, I think, the best.** Our submitted report claims bulk WGS can only
   see mosaic aneuploidy above ~14% of cells. That is the limit of the statistic we chose (unphased
   mean |BAF−0.5|), not of the problem. We re-did it with haplotype-signed BAF:
   - measured our own phase switch rate against the GIAB trio: **0.810%/site**, 377 segments on chr15;
   - that **falsified our own pre-registered statistic before we used it** — the chromosome-wide
     signed mean is diluted 27× and its LOD is 25–58%, worse than the 14% we published. Amendment.
   - orientation-invariant statistic, window fixed at 125 sites on public data: **calibrated
     LOD 1.46–2.95%, central 2.07%** — 6.8× tighter than published.
   - **balanced variegation is non-identifiable**: mean copy number exactly 2, mean allele fraction
     exactly 0.5 by symmetry; simulated detection is 0.1% at f=2% and 0.2% at f=40%, which is exactly
     the false-positive rate. Invisible at any depth, by any statistic.
   - the proband: **no chromosome-specific imbalance**. Excess over binomial 1.78×–3.57× across all 22
     autosomes, median 2.27×; highest robust z is chr17 at +2.88, below |z|=3, followed immediately by
     chr6 +2.72, chr7 +2.64, chr9 +2.60 — a continuous gradient, not a spike. None of the
     pre-declared therapy-related clonal lesions is elevated.

# The one hole in it, and a discovery that may close it cheaply

The median 2.27× excess is **uncontrolled**. It is correlated at the ~200 kb window scale and from the
VCF alone we cannot say whether it is technical (mapping and reference bias) or biological. A reviewer
kills the result with one sentence: *"your limit is first-order and your negative may be your own
noise model."*

**What I just found:** the 1000 Genomes high-coverage **raw GATK callset**
(`20201028_3202_raw_GT_with_annot`) carries `GT:AD:DP:GQ:PGT:PID:PL:SB` for 3,202 healthy individuals
at 30×. Same data type, same caller family, as the proband's GATK 4.2.4.0 VCF. And it streams: I
pulled 2 Mb for 5 samples in **6 seconds** with a remote range request, no download of the 41 GB file.

So a matched healthy control for the overdispersion looks reachable in hours, not days.

# Hardware and time

32 cores, 31 GB RAM, RTX 4060 with 8 GB VRAM (used so far for the Monte Carlo null of a weighted
chi-square mixture, which is a real use, not decoration). ~125 GB free disk. The 85 GB of raw reads is
2/8 downloaded; minimap2 installed; the reference is byte-identical to the challenge's (2,580 contigs,
same names and lengths, verified). Eight weeks.

# What I want from you

Be brutal. He asked whether this wins, and I do not think it does yet.

1. **Does this win?** Score the four packages against the rubric as the judges would. Where is the
   ceiling with what exists today, and what single addition raises it most? If your answer is that
   Rigor is already saturated and the marginal return is elsewhere, say that.

2. **Closing the overdispersion term.** Given the 1000G raw callset with AD, design the control
   precisely: how many individuals, which chromosomes, matched on what, and what exactly distinguishes
   a technical from a biological origin of a window-scale correlated excess. What would falsify each?
   Is there a confound in comparing a 44× GATK 4.2.4 call set to a 30× GATK 3.5/4 call set that would
   invalidate the comparison, and how do we handle depth mismatch?

3. **We have moved nothing on Impact (25%) and Scalability (15%) — 40% of the rubric.** Everything we
   built is Rigor and some Innovation. What is *real work*, not prose, that moves those two? Impact
   means something that changes this child's prognosis or care; Scalability means something another
   team can take to another disease. Name the concrete artefact for each and what it costs.

4. **What are we still missing that would change a judge's ranking**, that neither of you nor I have
   named yet? Assume there is something.

5. **The read-level stage.** With the overdispersion possibly closable from VCFs, does aligning the
   85 GB still earn its cost? What specifically justifies it now: the pileup kill-switch on the two
   BUB1B variants (N1002K sits at DP 28 against a genome at 44), the insert-size measurement, the
   unbiased depth companion, or nothing? If the honest answer is that it is now optional, say so.

6. **What would you stop doing.** We have eight weeks and a working submission we have not sent.

Every previous round the most valuable thing either of you produced was a claim of ours contradicting
our own data. Assume there is one in the four packages above and find it.
