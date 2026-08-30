You have reviewed this project three times: the benchmark design, its results, and the corrected
reports. This is a different and bigger question, and the user has asked explicitly for depth over
speed. Take the space you need.

# The situation

Team `ciberpty`, MVA Hackathon 2026 (Sage Bionetworks / Hugging Face / MVA Society). Submission window
closes **24 October 2026** — eight weeks left. Track 1 is submitted and scored 100/100 by the automated
evaluator (BUB1B compound heterozygosity → MVA1, OMIM 257300). Track 2 is written but **not submitted**.

**The problem: 52 other teams already had BUB1B before we started.** The gene is not a differentiator.
Two independent AI judges scored our whole package with the official rubric (Rigor 35 / Impact 25 /
Innovation 25 / Scalability 15) and both said the same thing: *"everything you have is reasoning, you
produced no results."* We have since produced three: a pre-registered DepMap/PRISM test whose result
went against our own hypothesis, a pre-registered benchmark of our own retrieval pipeline, and a
demonstration that the phase of the child's two variants is not resolvable from a VCF.

The user's instruction, verbatim: *"no vamos a publicar el track2 o perder intentos del track 1 sin
tener algo de peso que nos haga ganar... no quiero velocidad quiero calidad."* We will not submit
until we have something with real weight.

# THE NEW FACT — and it invalidates one of our own published claims

We had been working from the 315 MB VCF only. We just enumerated the challenge dataset properly. It is
**85 GB in 11 files**, and the bulk of it is **eight FASTQ files — the raw reads**:

```
WGS_EX2312012_HGWCNDSX7_S16_L00{1,2,3,4}_R{1,2}_001.fastq.gz   ~10.2-11.0 GB each, 84.7 GB total
WGS_EX2312012_HGWCNDSX7.vcf.gz                                  0.32 GB  (the one we used)
Challenge_Clinical_Phenotype_1.docx                             the eight HPO terms
```

Verified by reading a byte-range slice of L001_R1: **NovaSeq 6000 (instrument A01973), flowcell
HGWCNDSX7 (S4), 4 lanes, paired-end, read length exactly 149 bp.** The VCF reports DP 46 and 28 at the
two causal loci, so this is roughly 40-45x WGS.

**This makes a claim we published false.** Our phasing memo and both reports say *"the challenge
distributes a VCF and no alignments, so no read-backed phaser can be run at all."* Wrong: it
distributes the reads, from which alignments are produced. That sentence has to be rewritten whatever
else we decide. (Our geometric argument may still hold — 149 bp reads with a few-hundred-bp insert
cannot span the 10,911 bp between the two BUB1B variants — but now it is a measurement we must make,
not an assertion we can make.)

# Hardware, verified just now

- **CPU:** 32 cores. **RAM:** 31 GB total, ~19 GB free.
- **GPU: NVIDIA RTX 4060 Laptop, 8188 MiB VRAM.** Idle, 44 °C, `torch.cuda.is_available()` is True,
  driver 610.43.03. There was a long-running suspicion that this GPU caused system freezes; that was
  investigated and traced to the **WiFi module (`iwlwifi`)**, not the GPU. The user has now twice and
  explicitly instructed us to use the GPU. Assume 8 GB VRAM is the hard ceiling.
- **Disk:** 131 GB free on the data volume, and the 85 GB download has already started. About 30 GB of
  that is a 1000 Genomes panel we can delete after extracting what we need. So plan for roughly
  **100-120 GB of working space, not more**. A 40x WGS BAM is ~90 GB; the same as CRAM is ~35 GB.
- No aligner installed yet (no bwa, bwa-mem2, minimap2, gatk, whatshap, mosdepth). samtools and
  bcftools are present. We can install anything, including via container.
- Patient data must not leave the machine and must be deleted by 23 November 2026.

# What we have already established, so you do not re-derive it

- **The finding.** BUB1B `chr15:40209701 T>G` p.Leu737Ter (nonsense, ClinVar 533901 P/LP, gnomAD max AF
  1.0e-4) and `chr15:40220612 T>G` p.Asn1002Lys (missense, gnomAD 9.0e-7, not in ClinVar). 10,911 bp
  apart. Both `0/1`, DP 46 and 28, GQ 99, no GATK `PGT`/`PID`.
- **Phase.** In the 10,911 bp interval the child has exactly three heterozygous sites — the two causal
  ones and `chr15:40216470 A>G` — and all three are absent from the 1000 Genomes 3,202-sample phased
  panel. Nearest panel-present hets: 16.8 kb upstream (AF 0.0016) and 809 bp downstream (AF 0.0075).
  Beagle keeps 1,391 of 1,452 window variants and drops all three that matter.
- **Our pipeline is phase-blind.** Exomiser 15.1.0 reads phase into ACMG evidence (trans → PM3,
  cis → BP2) but not into the compound-heterozygous model: two pathogenic nonsense alleles declared in
  *cis* are still called AR_COMP_HET, still PATHOGENIC, still rank 1; absolute score difference 0.0034.
- **Mosaicism, our weakest published result.** MVA is *defined* by mosaic variegated aneuploidy: >25% of
  cells carrying different aneuploidies. We looked for it in the VCF and did not find it, and we
  published a computed detection limit instead of a bare negative: per-chromosome mean |BAF − 0.5| at
  DP 44, with the measured between-chromosome SD of 0.0035 as the noise floor, gives a detection limit
  of ~14% of cells for a clonal trisomy (16% at 2 SD), while variegation leaves each chromosome at
  1-2% of cells — 7-16x below it. **The report says explicitly: "Only the VCF was available, with no
  BAM, so no GC-LOESS normalisation was possible."** That constraint is now gone.
- **Our benchmark.** 61 pre-registered runs on public genomes. Highlights: seven healthy GIAB genomes
  queried with the child's eight HPO terms top out at 0.5619 against our 0.5871 (margin 0.025, on a
  null biased in our favour); planting the two ClinVar alleles into three unrelated healthy genomes
  reproduces 0.5871 and 0.4187 to four decimals; substituting an *unclassified* BUB1B nonsense for the
  ClinVar-whitelisted one leaves the variant term at 1.0000 and moves the combined score only 0.0128.
  A 30-genome 1000 Genomes tier is still running.
- **Track 2** proposes bortezomib as a *conditional* answer for a future tumour, rejects metformin on
  pharmacokinetics (~1000x shortfall), and contributes a five-filter repurposing framework. A
  pre-registered DepMap/PRISM test of our own mechanism came back **against us**: the
  aneuploidy-proteasome link is lineage-restricted and does not reach significance in solid tumours
  (interaction p = 0.026), and this child's tumour was solid. We reported that.

# The question

**Given 85 GB of raw reads, 8 GB of VRAM, 32 cores, ~110 GB of working disk and eight weeks: what is
the analysis that would actually make this submission win, and what is the correct order to do it in?**

Answer these specifically. Rank, cost, and be concrete enough to execute.

1. **What does the raw data unlock that the VCF cannot?** Enumerate honestly, and for each say whether
   it is (a) a real differentiator against 52 teams who all have BUB1B, (b) a correction we owe, or
   (c) busywork. Consider at minimum: mosaic aneuploidy from read depth and BAF with proper GC and
   mappability normalisation; structural and copy-number variants a small-variant VCF cannot contain;
   re-calling with a modern caller to test whether the organisers' VCF missed anything; read-backed
   phasing and the actual insert-size distribution; and anything we have not thought of.

2. **The mosaicism question is the one we think matters most, because it is the disease's defining
   feature and every team will have declared it undetectable.** Is it actually detectable at 40x from
   bulk WGS with proper normalisation, at the cell fractions MVA implies? What is the right statistic
   — per-chromosome, or a genome-wide aggregate of dispersion that pools 22 chromosomes? What is the
   right null: the patient's own chromosomes, public healthy BAMs, or simulated mixtures? **If the
   honest answer is that it is still undetectable, say so and tell us how to prove that convincingly
   rather than assert it, because a rigorous negative with a measured limit is worth more to us than a
   fragile positive.**

3. **Where does an 8 GB GPU genuinely help, and where would we be forcing it?** Parabricks `fq2bam`
   wants 16 GB+ and is presumably out. Be concrete about what fits: DeepVariant or Clair3 inference,
   a trained detector, something else. **Say plainly if the honest answer is that alignment is
   CPU-bound and the GPU's role is small** — we would rather be told that than fake it. But if there is
   a use where the GPU is genuinely decisive rather than decorative, that is what we want.

4. **Feasibility and ordering.** Alignment of 40x WGS on 32 cores: what tool, what wall-clock, what
   disk strategy given we cannot hold 85 GB of FASTQ and a 90 GB BAM at once. Where do we write CRAM
   instead of BAM. What is the minimum viable path to the first real result, and what is the full path.

5. **What would make a judge say this submission deserves to win?** Write the sentence. Then tell us
   which of the analyses above produces it.

6. **What should we NOT do.** We have eight weeks and a working submission. Name the attractive traps.

7. **Is there any reason not to do this at all** — a rule against re-processing the raw data, a risk of
   producing something that contradicts our already-submitted Track 1 in a way we cannot recover from,
   or a cost we are underestimating? The submission rules allow up to 6 Track 1 submissions (2 used)
   and 3 Track 2 submissions (0 used).

Be blunt and specific. Every previous round, the most valuable thing either of you produced was a
claim of ours that contradicted our own data.
