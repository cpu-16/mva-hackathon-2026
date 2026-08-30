# Cursor (Grok 4.6 xhigh) — qué hacer con los 85 GB de lecturas crudas y la GPU

`agent -p --mode ask --model cursor-grok-4.6-xhigh`, 30-ago-2026. Mismo brief.

This is a spike: a ranked plan, not a build. One of your own files already contradicts the story that the FASTQs were a surprise, and that changes what is worth doing with them.

The official rules already list *“raw sequencing data optionally in BAM/CRAM”* as part of the dataset. `INFORME.md` itemised the eight FASTQs on day one and said mosaic aneuploidy is seen better in reads than in a germline VCF. Track 1 Q11 already tells judges the 85 GB exists and that you chose not to use it. Codex’s review of the phase memo already said empty `PGT`/`PID` is not proof that WhatsHap cannot run. You then wrote *“the challenge distributes a VCF and no alignments.”* That sentence is false as a description of the challenge. It was true only as a description of what you had downloaded.

Do the read-level work. Do not pretend it is a new dataset. Treat it as the dataset you deferred, and run the one statistic that could actually move the mosaicism claim. Almost everything else from those FASTQs is a correction you owe, or busywork.

---

## 1. What the reads unlock

| Analysis | What the VCF cannot do | Verdict |
|---|---|---|
| **Kill-switch pileup at the two BUB1B sites** | Confirm they are real heterozygous SNVs, not mapping artefacts. N1002K is at DP 28 vs a genome near 44. GQ 99 and AD 15,13 look germline; that is not a pileup. | **(a)+(b).** Two hours after CRAM exists. If N1002K is a bad call, Track 1 is wrong and you must know before writing another sentence. |
| **Insert-size distribution + spanning-pair count + WhatsHap on a 20 kb window** | Measure whether any fragment links the two alleles. Geometry: 10,911 bp apart; the only internal het (`chr15:40216470`) is **6,769 bp** from Leu737Ter and **4,142 bp** from Asn1002Lys. NovaSeq PE 149 bp with a typical 350–500 bp insert cannot span that. Codex already told you this. Empty `PGT`/`PID` is what GATK did, not what WhatsHap would do. | **(b) first, then a cheap (a).** You owe the measurement. The likely result (zero spanning pairs, disconnected phase blocks) is not a differentiator. The sentence *“no read-backed phaser can be run at all”* is. |
| **Phased-haplotype BAF (MoChA / hapLOH-style), with a mixing LOD** | Unphased `\|BAF−0.5\|` is almost blind below ~10% at 40× (your own table: 5% trisomy adds **+0.0001**). Signing BAF by statistical phase of *common* SNPs is how Loh and colleagues detect mosaic chromosomal alterations near **1–5%** on arrays. That method needs alignments (or at least BAM-confirmed genotypes) plus a haplotype panel you already have. | **(a). This is the only read-level analysis that can win.** Details in §2. |
| **Read-depth CN with GC-LOESS / mappability** | You reported +2.9% to +7.0% on chr16–22, r(GC, coverage)=0.43, and chr21 (GC-poor) as the largest deviation. That is an unfinished measurement, and you said so. | **(b).** Pre-register: those “gains” vanish after GC+mappability correction. If one remains, that is a finding. Repeating unphased VCF-BAF on the BAM is not a new result. |
| **FANCD2 pileup** | You already called it a mismapped haplotype (AF ≈0.31, three co-phased edits, pseudogenes). The BAM can show MAPQ, secondary hits, and the indel. | **(b), two hours.** Do not build a paper around it. |
| **Diploidy of BUB1B (exon-level depth, split/soft-clipped reads)** | A small deletion under N1002K would change the compound-het reading. | **(a) as QC, not as a hunt.** Hypothesis-driven, 2–4 hours. |
| **Genome-wide SV calling (Manta/Delly/GRIDSS)** | GATK HC does not emit these. | **Busywork** unless BUB1B or a named MVA gene is the query. A genome-wide SV circus on n=1 is how you spend November on incidental findings you must not report. |
| **Re-calling the whole genome (DeepVariant/Clair3/GATK)** | Test whether the organisers’ VCF missed a third BUB1B allele or a splice variant. | **Busywork genome-wide.** Optional and cheap: re-call a 2 Mb window around BUB1B. The two causal sites will still be there. |
| **Genome-wide aggregate of unphased BAF dispersion** | Pool 22 chromosomes so 1–2% effects add. | **Busywork.** Your 5% row already shows the per-chromosome increment is ~0.0001. The SE of the 22-chromosome mean, using your own between-chromosome SD of 0.0035, is `0.0035/√22 ≈ 0.00075`. Signal is below noise before library-chemistry differences versus a public BAM. Simulate it on paper in an hour; do not align 85 GB for it. |
| **ichorCNA / tumor-fraction HMM** | Wrong generative model. It looks for a *clonal* CNA profile at some purity. Variegation averages toward diploid. A null ichorCNA purity will be misread as “no mosaicism.” | **Trap.** |
| **Mitochondria, STRs, de novo assembly, linked-read reconstruction from PE, training a detector on n=1** | — | **Busywork / harmful.** |
| **Premature chromatid separation** | PCS is a metaphase phenomenon. It leaves no trace in extracted DNA. | **Still closed.** The reads do not change this. Keep saying so. |

What you have not named, and should: **statistical phasing of common SNPs is a different problem from phasing the two BUB1B alleles.** Beagle dropping Leu737Ter and Asn1002Lys is settled. Beagle/SHAPEIT on the rest of the autosomes is how haplotype BAF works. Do not refuse the mosaic method because the rare-variant phase memo is closed.

---

## 2. Mosaicism: still undetectable for variegation; not yet measured for a preferred chromosome

**Variegated MVA at the diagnostic cell fraction is still not visible in bulk, including with GC-LOESS.** That part of `MOSAICISMO.md` is right, and the reads do not refute it. Gains and losses of the same chromosome cancel in the mean. PCS is invisible. A 30% aneuploid fraction spread over 22 autosomes is ~1–2% per chromosome, and your unphased statistic does not even move at 5%.

GC-LOESS does **not** rescue unphased `\|BAF−0.5\|`. BAF is already a per-site ratio. The 14% LOD is set by between-chromosome systematic bias and by binomial width at 40×, not by the GC sampling you called insufficient. Fixing depth-GC will clean the *dosage* plot (chr16–22). It will not take a 1.4% trisomy over the 0.005 noise floor.

**The honest remaining question is narrower:** does *this* child have a *preferred* chromosome (or a CHIP-like clonal event in post-chemo blood) at a cell fraction haplotype BAF can see?

Back-of-envelope, which you must replace with mixing, not quote as a result:

- At fraction *f*, extra copies of one parental homolog shift haplotype-signed BAF by ~*f*/4. At 2%, that is ~0.005.
- You had 2.27 M het SNVs; ~10⁵ per autosome. Binomial SE of a chromosome mean at DP 44 is ~`0.075/√1e5 ≈ 0.00024`.
- That looks like SNR ≫ 1 at 2%. It is not a detection. Switch errors, reference bias after phasing, overdispersion, and mappability will inflate the SE by several-fold. **1–5% clonal whole-chromosome is the realistic window; 1–2% variegated-per-chromosome is the edge; uniform 1.4% on every chromosome at once is still a no.**

That is why the field uses haplotype BAF (Loh *et al.*, mosaic chromosomal alterations; MoChA/hapLOH), not unphased MAD, for mosaic events in this fraction range.

**Statistic to pre-register (primary):** per-chromosome haplotype-signed BAF after phasing common SNPs (MAF > 1%, DP 20–80) against 1000 Genomes. One number per autosome. Secondary, not primary: GC-LOESS chromosome means. Do not make genome-wide unphased MAD the headline.

**Null, in this order:**

1. **In-silico mixing on a public ~40× BAM (HG002 or a 1000G 30× genome)** at 1, 2, 5, 10, 20% extra copies of one chromosome. This is the LOD. It uses **no patient data**. It is the first result, and it can start while the FASTQ download finishes.
2. **Empirical null from public 30× WGS** (the 30 genomes you are already touching for Replay, or a pre-declared subset): the distribution of the same per-chromosome statistic in people who do not have MVA.
3. **The patient’s other chromosomes** as a within-sample sanity check, not as the sole null. Using only self-chromosomes is how GC-rich autosomes become “mosaic.”

**Confound you must freeze before looking:** this is post-ERMS, likely post-chemo, blood. A 20q deletion, 13q deletion, or loss of X/Y is CHIP / therapy-related, not MVA. Pre-register: those events do not count as support for mosaic variegated aneuploidy. MVA-like evidence would be whole-chromosome *gains* (and maybe losses) of autosomes that are not the CHIP canon.

**If it is still undetectable — and that is the likely outcome — prove it like this, not with another assertion:**

- Mixing curve: statistic vs *f*, with the 1000G 95th percentile drawn on the plot.
- This child’s 22 autosomes marked on that plot.
- A one-line LOD: *“clonal whole-chromosome trisomy detectable at f ≥ X% (mixing, 80% power, q < 0.05 vs 1000G); variegation at 1–2% per chromosome sits Y× below that.”*
- The sentence from `MOSAICISMO.md` about bulk averaging, restated as *measured with the reads the challenge distributed*, not as a VCF limitation.

A rigorous negative with a mixing LOD is worth more than a fragile 8% “signal” on chr21 that dies when you exclude acrocentric sequence. Your VCF LOD of ~14% is already the right *genre* of claim. It is the wrong *statistic*, and it was locked to a false data constraint. Replacing 14% unphased with, say, 4% haplotype-phased, and still sitting above 1–2%, is a result. Re-running unphased BAF on a BAM and reprinting 14% is not.

Do not claim you have shown this child lacks mosaicism. You have not, by definition of the disease. You will have shown that **this bulk WGS, analysed with the strongest bulk statistic in routine use, still cannot see the variegated process**, and you will have a number for the clonal exception.

---

## 3. The GPU

Alignment is CPU-bound. An 8 GB 4060 does not change that. Parabricks `fq2bam` is out (16 GB+). Do not wait for a GPU aligner.

Where 8 GB actually fits:

| Job | Fits? | Decisive? |
|---|---|---|
| **Clair3 (or DeepVariant at batch 1–4) on chr15:40.1–40.3 Mb** | Clair3 yes; DeepVariant maybe, likely OOM at default batch | **The only honest GPU sentence in the FASTQ path.** One hour after CRAM. Confirms the two SNVs; looks for a third BUB1B allele. Not a prize on its own. |
| Genome-wide DeepVariant | Unlikely at default; `make_examples` is a CPU day anyway | No. |
| Parabricks, Guppy/Dorado, de novo assembly, training a mosaic CNN | No / wrong data / n=1 | No. |
| AlphaFold from scratch on BUB1B | 8 GB might do a domain with reduced MSA | Theatre. AF-O60566 already exists. Your own gate was pLDDT on 766–1050, FoldX on CPU. |
| **ThermoMPNN / a forward-pass ΔΔG for the VUS calibration** (not FASTQ) | Yes | **This is the GPU’s real job this month if you also do backlog item 5.** It is not a read-level analysis. |
| RAPIDS on 2.27 M SNPs | Yes | Decorative. |

If the methods need a GPU line because you were told to use it: *“Clair3 on the BUB1B window, 8 GB, both alleles confirmed; genome-wide calling remained the organisers’ GATK VCF.”* Do not lead with it. Judges who do genomics will smell a 4060 being walked like a dog.

---

## 4. Feasibility and order

### Disk, first, because the 110 GB figure is already wrong

After 85 GB lands on 131 GB free you have **~46 GB**, not 110. The 1000G bulk (~30 GB) plus lane-wise deletion of FASTQ is not a nicety. It is the only geometry that fits.

Never write a 90 GB BAM. Never keep FASTQ and CRAM together.

Peak that works:

1. Extract from 1000G whatever Replay + haplotype phasing need (common SNPs AF > 1%, plus the chr15 window you already have). Delete the rest. **Do this before or during the FASTQ download, not after.**
2. One lane at a time: FASTQ pair (~21 GB) → CRAM (~8 GB) → **delete that pair**.
3. Merge four CRAMs → one CRAM (~30–40 GB) → delete per-lane CRAMs.
4. End state: ~35 GB CRAM + VCF + a small SNP panel. FASTQ gone.

Sort temps for a *full* 40× BAM will exceed both disk and 31 GB RAM. Lane-wise is required for memory too.

### Tool and wall-clock

**minimap2 `-ax sr`**, not bwa-mem2. 31 GB RAM, ~19 GB free, bwa-mem2’s index wants ~10–12 GB *plus* sort. You will OOM or thrash. Mosaicism, insert size, and two pileups do not need bwa-mem2’s extra fraction of a percent. 16 threads for the aligner, the rest for `samtools sort` at ~500M–1G per thread.

Reference must match the VCF header (GATK 4.2.4.0, DNAnexus, Feb 2025 — almost certainly GRCh38 with decoys). Wrong FASTA and the CRAM is junk.

Wall-clock, 32 cores, first time, including mistakes: **one overnight to a merged, duplicate-marked, indexed CRAM** (roughly 8–16 h of compute, 24–48 h of calendar if the reference, RG tags, or CRAM reference hashes fight you). Then:

- Pileup + insert size + WhatsHap window: **2–4 h**
- mosdepth + GC-LOESS: **half a day**
- Phase common SNPs + haplotype BAF + 1000G null: **1–3 days**
- Mixing LOD on a public BAM: **1–2 days**, and it should already be done

### Minimum viable path to the first real result

**The first result does not use the patient’s reads.** Mixing LOD on HG002/1000G, pre-registered, committed before you open a patient FASTQ. That is the DepMap move again: a test that can come out against you, on public data, with a git timestamp.

Second result, from the patient CRAM, in this order:

1. Kill-switch pileup (both BUB1B sites + BUB1B exon depth).
2. Insert size, spanning-pair count, WhatsHap blocks — rewrite the false sentence.
3. GC-LOESS dosage vs the chr16–22 claim.
4. Haplotype BAF vs mixing LOD and 1000G null.

### Full path (and what is not on it)

Minimum path, plus FANCD2 pileup, optional Clair3 on the BUB1B window, then **one** Track 1 resubmit and the **first** Track 2 submit. Not on the path: genome-wide re-calling, SV circus, ichorCNA, de novo assembly, a GPU aligner, a five-filter engine (DepMap did not give you a second filter-3 denominator in solid tumours).

### Order against the rest of the eight weeks

| When | What | Why this position |
|---|---|---|
| **Now, while FASTQ downloads** | Finish Replay tier 2 (already running). Pre-register the read-level experiment. Mixing LOD on public BAM. Extract 1000G SNPs, delete the bulk. Download a matching GRCh38, index for minimap2. §6 fibroblast power calculation (2–3 days, no FASTQ) — still the cheapest Track 2 hole. | You cannot align yet. You can produce a result today. |
| **Day the FASTQ is complete** | Lane-wise CRAM. Delete FASTQ as you go. | Disk. |
| **Next calendar day** | Kill-switch, insert size, WhatsHap. | If N1002K dies, stop and rethink Track 1. |
| **Following 3–5 days** | GC-LOESS + haplotype BAF + apply mixing LOD. | The prize analysis. |
| **Then, one writing pass** | Rewrite mosaicism § and phase § in both reports. Fix the three Replay-found errors in Track 1 if they are not already in the submitted PDF. | One Track 1 submit, not two. |
| **Only if pLDDT gate passes** | VUS calibration on CPU, ThermoMPNN on GPU. | Independent of FASTQ. Abort if pLDDT < 70. |
| **Do not start** | Five-filter CLI, genome-wide DeepVariant, PGx, another literature pass. | Already killed, still dead. |

Do not drip-feed Track 1 submits. You have 4 left. Spend **one** on the combined correction (Replay errors + “we had the reads” + measured LOD + 1000G Replay outcome). Keep three in reserve.

---

## 5. The sentence a judge should be able to say

**“They are the team that pre-registered a test of the disease’s defining feature on the reads the challenge actually distributed, using the statistic that can see 1–5% clonal aneuploidy, calibrated it on public 40× genomes, applied it to this child, and reported a number — including when that number went against the idea that bulk WGS could serve as an MVA endpoint.”**

That sentence is produced by **§2’s haplotype-BAF experiment plus the mixing LOD**, sitting on top of the three results you already have (DepMap against the proteasome story in solid tumours, Replay, phase not resolvable). Alignment, WhatsHap, GC-LOESS, and Clair3 are what make that sentence true rather than asserted. They are not themselves the sentence.

A judge will not say you deserve to win because you ran bwa. Fifty-two teams have BUB1B because they opened the VCF. The ones who also open the FASTQ and run ichorCNA will either claim a GC artefact or write “undetectable” without a mixing curve. The curve is the artefact.

---

## 6. What not to do

- **Do not treat “we aligned 85 GB on a 4060” as Innovation.** It is logistics.
- **Do not re-run unphased VCF-BAF on the BAM and reprint 14%.** That is the item CONTINUAR-AQUI already killed. Stay killed. The new work is a different statistic.
- **Do not submit Track 2 until §5 of that report is rewritten.** As it stands it says there was no BAM. You now know that is false. Submitting it is sending a paragraph you can already falsify. You have three Track 2 attempts; the first one should contain the mixing LOD.
- **Do not burn a Track 1 submit on “analysis pending.”** Wait for the measurement.
- **Do not keep FASTQ and CRAM. Do not put CRAM, pileups-with-reads, or a genome-wide BAF table on GitHub or into a model.** Named variants and per-chromosome summaries are findings; the CRAM is the child. Deletion date is still 23 November 2026, and the rules explicitly include *derived* datasets.
- **Do not call CHIP events MVA.**
- **Do not genome-wide SV-call, de novo assemble, train a classifier, run Parabricks, or fish for modifiers.**
- **Do not starve Replay tier 2.** P-A is open. A 0.025 margin on a biased null, with 30 genomes still running, is an unfinished result you already promised sentences for.
- **Do not skip the N1002K pileup because “GQ 99.”** That is the only FASTQ outcome that can actually break Track 1.
- **Do not write “phase is now resolved.”** It will not be. Measure the blocks, then keep parental Sanger as the cheapest experiment in the report.
- **Do not use the GPU as a plot.** If it does not run Clair3 on a window or ThermoMPNN, it does not belong in the methods.

---

## 7. Is there a reason not to do this at all?

**No rule against it.** The rules describe raw data as part of the provision. Using it is completing the intended dataset. Reprocessing is not a second submission type; it is analysis.

**Track 1 contradiction risk is real in one place and fake in the others.**

- Fake: mosaicism remaining undetectable does not touch BUB1B. It *strengthens* Track 2 §5.
- Fake: WhatsHap failing to link 10.9 kb does not touch BUB1B. You already do not claim observed phase.
- **Real: N1002K (or Leu737Ter) looking like an artefact in the BAM.** Probability is low; cost of not checking is the whole Track 1. If it happens, you still have four submits to recover, and you would rather find it than have a judge find it.
- Real but recoverable: a third BUB1B allele, or a deletion, would change the allelic architecture sentence, not necessarily the gene.

**Cost you are underestimating:** not GPU, not core-hours. (1) **46 GB free after the download**, so destructive lane-wise CRAM is mandatory. (2) **31 GB RAM**, so minimap2 not bwa-mem2. (3) **Calendar**, not compute: first WGS on a laptop is an overnight of CPUs and two days of headers and CRAM reference hashes. (4) **Opportunity cost** if this expands into a calling pipeline. Scoped as mixing → CRAM → kill-switch → haplotype BAF, it is a week of work and compatible with §6 power and Replay. Unscoped, it eats the eight weeks.

**The actual reason to hesitate** is not legal or strategic. It is this: if you open the FASTQs and then run the *same* unphased statistic, you will have spent a week to confirm a claim you already published, while Q11 currently *brags* that the 85 GB was unnecessary. That would look worse than leaving the FASTQs closed. The condition that makes this worth doing is the mixing-calibrated haplotype BAF. If you are not willing to pre-register that and accept a negative, do not download.

---

## What this contradicts in your own corpus

You asked for these.

1. *“The challenge distributes a VCF and no alignments.”* The challenge distributes eight FASTQs and, in the rules, names BAM/CRAM as the raw form. You distributed a VCF to yourselves.
2. *“FASTQs would not change the mosaicism conclusion”* (`HALLAZGOS.md`, `RESUMEN-NOCHE.md`). True for unphased BAF and for fully variegated cancelling. False as a reason not to measure haplotype BAF and GC-LOESS, both of which you said required a BAM.
3. *“More depth would not move the limit.”* True for *your* statistic, because you subtract the binomial and compare to between-chromosome SD. Not generally true for haplotype-signed BAF, where averaging ~10⁵ independent hets is the whole point. Do not carry that sentence over unchanged.
4. Track 1 Q11: reproducibility without the 85 GB is a feature of *retrieval*, not of the mosaicism section you also submitted. Those two claims cannot share a report once you know what the 85 GB is.
5. CONTINUAR-AQUI still says do not use the GPU and lists BAF mosaicism as killed. The GPU instruction has been superseded twice. The killed item is VCF-BAF. Do not use the handover to refuse the reads.

**Start with the mixing LOD on a public BAM, committed before a patient read is aligned.** That is the move that made DepMap valuable. The CRAM is plumbing. The prize is whether mosaic variegated aneuploidy, at the fractions the diagnosis implies, is a number you can read out of the file the organisers actually gave you. You should expect the answer to be no, with a tighter LOD than 14%, and you should want that in writing before 24 October.

