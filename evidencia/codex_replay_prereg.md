# Codex — crítica adversarial del pre-registro MVA-Replay (v1)

`codex exec` (GPT-5.x), 30-ago-2026. Brief: `brief_replay_prereg.md`. Sin acceso a red: se le dio todo el contexto verbatim.

## 1. Where the benchmark is rigged in your favour

1.1. **The phenotype names the answer before the variants are examined.** BUB1B, CEP57, and TRIP13 are the three canonical MVA genes, and every positive case uses an MVA phenotype. hiPhive should already place those genes near the top on phenotype evidence alone. This is not a general sensitivity test; it is a test of whether Exomiser retrieves famous, phenotype-perfect genes after you add favorable variants.

**Fix:** Add phenotype-matched negative controls: run the same MVA HPO set after planting the same variant architectures in genes matched to BUB1B/CEP57/TRIP13 for coding length, constraint, inheritance mode, and ClinVar density but unrelated to MVA. TTN alone is not matched and is too obvious.

1.2. **All nine observations within a stratum are pseudoreplicates.** The apparent denominator is nine, but there are only three causal genes and apparently one variant pair per gene, copied into three backgrounds. Background changes do not create independent tests of variant interpretation. A single highly recognizable allele pair can produce three successes.

Report the experimental unit honestly:

- variant construct: likely \(n=3\);
- background perturbations per construct: \(n=3\);
- never present 9/9 as nine independent causal cases.

**Fix:** Use three independently selected allele pairs per gene, or report results by construct and background without binomial sensitivity language.

1.3. **The selection rule does not actually specify the allele pairs.** “First, median and last record” yields three records per gene/class, but S1 and S3 each require two alleles and S2 requires one from each of two pools. The preregistration never says which two records form each case. This leaves a major post hoc degree of freedom.

**Fix:** Append, before running anything, an explicit deterministic pairing rule—for example:

- S1: first and last P/LP;
- S2: median P/LP and median VUS;
- S3: first and last VUS;
- S4: the same P/LP used in S2.

Also specify what happens if records coincide, overlap, share an allele, or a pool has fewer than two eligible variants.

1.4. **“Inside the gene span” is not equivalent to “a variant in the gene.”** Long introns, overlapping genes, regulatory records, and transcript-specific consequences can enter the pool. TTN is particularly vulnerable because of its enormous span.

**Fix:** Require an Exomiser-recognized protein-coding consequence on a canonical or explicitly named transcript of the target gene. Freeze transcript IDs before seeing rankings.

1.5. **Your spike-ins may be outside the GIAB high-confidence regions.** You are manufacturing perfect calls at loci where the corresponding GIAB sample may not be callable. That removes exactly the sequencing and calling difficulty faced by a clinical pipeline.

**Fix:** Restrict eligible loci to the intersection of the three GIAB v4.2.1 high-confidence BEDs, or at minimum require membership in the relevant sample’s confident region and report how many pool records are excluded.

1.6. **The synthetic calls are unrealistically immaculate.** Every planted variant is `PASS`, `QUAL=100`, depth 44, balanced 22:22, with no strand bias, mapping ambiguity, local haplotype complexity, or caller uncertainty. This tests prioritization after perfect detection, not end-to-end operating characteristics.

That is acceptable only if you rename the estimand: **conditional retrieval sensitivity given a perfect heterozygous call**. Do not call it pipeline sensitivity without that qualifier.

1.7. **Background target-gene variants are uncontrolled.** Dropping only an exact-position collision is insufficient. A background could already carry another rare target-gene allele, converting S4 into a possible biallelic case or changing S2/S3 interpretation.

**Fix:** Before insertion, inventory every Exomiser-retained variant in the planted gene. Either exclude contaminated gene–background combinations by a predeclared rule or retain and flag them as such.

1.8. **The three genes are not a representative disease benchmark.** They were selected because they are exactly the genes relevant to your submitted diagnosis. The result can support “replay performance for known MVA genes,” not general rare-disease performance.

---

## 2. Is Null-B valid?

2.1. **No—not for the stated claim.** Null-B estimates:

> The top score produced by a healthy GIAB genome under a randomly selected OMIM phenotype.

Your claim concerns:

> The top score produced by a healthy genome under this patient’s eight HPO terms.

Those are different distributions. The valid direct null is Null-A, but \(n=3\) is far too small to support “routinely” or a 95th-percentile claim.

2.2. **hiPhive makes the mismatch especially serious.** The top gene and top combined score can be dominated by how specific, internally coherent, well-annotated, and genetically distinctive the phenotype set is. Eight terms for a well-characterized syndrome are not exchangeable with eight terms from another OMIM disease.

Thus the 75 observations are primarily 25 phenotype-set experiments repeated over three correlated genomes—not 75 independent draws from one null distribution. The effective replication for phenotype variation is closer to 25, while the replication for healthy-genome variation remains three.

2.3. **The random-set construction is underspecified and likely biased.** What happens when an OMIM disease has fewer than eight annotations? Are ancestors included? Are redundant parent–child HPO terms allowed? Are diseases sampled uniformly, causing rare and richly annotated diseases to have the same weight as broad syndromes? Does `genes_to_phenotype.txt` represent disease-level annotation faithfully? These choices can shift the top-score distribution substantially.

2.4. **The correct null is many healthy genomes queried with the exact patient HPO set.** Spend the 75 Null-B runs on approximately 25 independent public genomes × three runs only if three technical representations are meaningful, or preferably 75 independent genomes × the single frozen query. Use the closest available clinical-WGS-like callsets and one consistent preprocessing pipeline.

If you cannot acquire more genomes, your honest conclusion is limited to:

> In the three GIAB backgrounds, the top scores under the patient phenotype were X, Y, and Z.

You cannot estimate a 95th percentile from three genomes.

2.5. Null-B is still useful for a different question:

> How much does the maximum Exomiser score vary across phenotype definitions in healthy genomes?

Keep it as an exploratory calibration, but do not use its percentile to validate 0.5871.

2.6. **Even a larger healthy null must match variant burden.** Comparing the patient’s clinical WGS score against reduced GIAB benchmark VCFs confounds disease signal with callset construction. Ideally, healthy and patient VCFs should come from comparable sequencing, calling, filtering, chromosome coverage, and representation.

---

## 3. Problems with P1–P7

3.1. **P1’s number is falsifiable; its interpretation is not.** With nine cases, “≥90%” means exactly 9/9 because 8/9 is 88.9%. The sentence “if it fails, the benchmark is broken, not the pipeline” pre-assigns every negative result to implementation failure. That is an escape hatch.

Replace it with technical validity criteria established before rankings are viewed. If the inserted genotypes are present, parsed, retained, and annotated correctly, an S1 miss is a pipeline result.

3.2. **P2 is measurable but overstates replication.** Seven of nine passes the threshold, but the meaningful units are three genes/variant constructs. A failure across all three backgrounds for one gene is one construct-level failure, not three independent failures.

3.3. **P3 is not adequately specified.** “S3 < S2” could mean 6/9 versus 7/9, which is one case and essentially noise. “S3 ≈ S1” has no declared equivalence margin. Further, S3 does not fully break ClinVar circularity: its variants still come from ClinVar, and Exomiser may ingest their VUS annotations or recognize them through other sources.

Specify a quantitative contrast, such as rank-1 difference and median score difference, with uncertainty, while acknowledging it is descriptive at this sample size.

3.4. **P3 does not isolate “ClinVar whitelist” from variant severity.** P/LP and VUS pools likely differ in molecular consequence, allele frequency, computational pathogenicity, review history, and transcript position. An S2→S3 drop cannot be attributed specifically to ClinVar classification.

3.5. **P4 is falsifiable but is not a false-positive rate.** A carrier gene ranked highly under a phenotype that names that gene is a prioritization result, not a false diagnosis unless the pipeline actually outputs a diagnostic call. Separate:

- gene rank;
- compatible inheritance call;
- reportable diagnosis.

Otherwise you risk accusing the pipeline of a failure it was not designed to avoid at the ranking stage.

3.6. **P5 is close to trivially true.** TTN is a phenotype-incompatible, extreme-length decoy under an MVA query. If hiPhive contributes meaningfully at all, TTN should lose. It does not quantify phenotype contribution under a difficult alternative.

Use matched decoys with plausible overlapping phenotypes or similar phenotype scores.

3.7. **P6 may not be measured at all.** It is valid only if Exomiser 15.1.0 consumes cross-record phase information in precisely the way you encode it and exposes an auditable AR_COMP_HET decision. If it ignores `PS`, treats phased heterozygotes as ordinary heterozygotes, or performs gene-level compound-het assignment without phase exclusion, S6 is merely documenting software behavior—not validating your patient caveat.

3.8. **P7 is not supported by the proposed null.** Its reference distribution changes both genome and phenotype, is clustered, and is not comparable to the clinical WGS. Therefore “above the 95th percentile” would be numerically calculable but scientifically mislabelled.

---

## 4. Technical traps

4.1. **Do not assume `PS` semantics. Verify them before unblinding.** The three required encodings are:

- cis: `0|1` and `0|1`, same phase set;
- trans: `0|1` and `1|0`, same phase set;
- unphased: `0/1` and `0/1`, with no `PS`.

Using `0|1` for both “trans” records would actually encode cis. Using different `PS` values does not encode trans; it says their relative phase is unknown.

4.2. **A parser recognizing `|` does not prove it uses `PS`.** Establish a technical acceptance test with an unrelated sentinel gene before benchmark runs:

- confirm both variants appear in Exomiser’s variant output;
- confirm the parsed genotypes remain phased;
- confirm cis, trans, and unphased produce the expected inheritance annotations;
- inspect the exact field on which `AR_COMP_HET called` will be scored.

Pre-register the expected observable. If no output field distinguishes them, declare S6 unmeasurable before running the locked cases.

4.3. **Do not “debug until P1 passes.”** Technical validation may check VCF ingestion and annotation, but it must not require a desired rank. Otherwise P1 explicitly licenses tuning against the benchmark.

4.4. **Allele balance may not be determined solely by `DP` and `AD`.** Confirm the exact Exomiser filter reads `AD` for this VCF path and how it handles absent `GQ`, `PL`, or caller-specific fields. A balanced `AD=22,22` should ordinarily pass, but “matching patient depth” does not establish matching filter behavior.

Also make the VCF internally consistent:

- `DP=44`;
- `AD=22,22`;
- if retained, `ADALL` consistent with `AD`;
- valid `GQ` if the analysis filters on genotype quality;
- `GT` first in `FORMAT`.

4.5. **Your inserted `FORMAT` differs from the surrounding records.** That is legal if the header definitions exist, but verify that the sample column contains exactly the number of fields declared and that no code assumes the original `GT:PS:DP:ADALL:AD:GQ` layout. Prefer preserving the original format schema and filling unused fields with `.`.

4.6. **PASS_ONLY can create asymmetric comparison.** The inserted calls always pass, while the source file has already been restricted to benchmark PASS calls. This removes the noisy and borderline calls present in clinical WGS. Confirm whether `PASS_ONLY` operates on input `FILTER`, Exomiser’s internal filters, or both; report both pre-filter and retained variant counts.

4.7. **Exact-coordinate collision detection is inadequate.** Overlapping indels or differently represented variants can conflict without sharing the same POS. Without a reference FASTA, you cannot reliably left-normalize or validate arbitrary indels.

Safest fix: restrict spike-ins to SNVs whose REF matches an existing trusted GRCh38 source and reject any overlapping background record. If you keep indels, obtain the exact GRCh38 FASTA and normalize both inputs.

4.8. **ClinVar allele-specific fields are easy to misparse.** “Single ALT” avoids some complexity but not all. `CLNSIG`, `CLNREVSTAT`, conflicting submissions, multiple conditions, and `_` versus spaces/pipes require explicit parsing. Save the raw source record and parsed eligibility fields for every selected allele.

4.9. **Chromosome and sample-header consistency must be checked.** Verify:

- one and only one sample;
- expected sample identifier;
- `chr` contigs accepted by the frozen Exomiser assembly configuration;
- sorted records after insertion;
- no duplicate coordinates/alleles;
- correct bgzip and tabix/CSI index;
- REF allele agrees with GRCh38;
- every spike-in is visible via a round-trip VCF query.

4.10. **Metric 7 does not measure the important comparability gap.** “Number of ranked genes” is a weak proxy. Two VCFs can rank the same number of genes while differing drastically in rare damaging variant burden and top-score distribution.

At minimum report per genome:

- total variants read and retained;
- rare variants;
- protein-altering variants;
- genes with at least one retained variant;
- genes with two qualifying heterozygous variants;
- callable coding bases per target gene;
- chromosome coverage, especially the absence of X/MT;
- distribution of variant and phenotype component scores.

4.11. **A high-confidence benchmark VCF is not simply a cleaner clinical WGS.** It conditions on benchmarkability and omits difficult genomic contexts. Sensitivity is not automatically an upper bound for variants that would lie outside those regions, while ranking sensitivity conditional on an inserted perfect call may be higher. Likewise, the false-positive rate is not merely lower; it is for a different observation process.

4.12. **Case dropping can become informative missingness.** Variants colliding with background calls are likely enriched at polymorphic loci. Dropping them preferentially removes certain allele classes. Report the eligible pool, selected records, collision status, and denominator fixed before results. Do not replace dropped cases, but do not calculate sensitivity with a quietly reduced denominator either.

---

## 5. What a judge could write

> “This benchmark repeatedly inserts perfect ClinVar variants into three unusually sparse reference callsets, queries them with phenotypes that already identify the three target genes, and treats replicated variant pairs as independent cases; its random-phenotype null does not calibrate the patient’s score under the patient’s phenotype, so the reported sensitivity and 95th percentile do not support the claimed operating characteristics.”

That is the dismissal you need to design against.

---

## 6. The single smallest high-value change

**Replace Null-B with many independent healthy genomes queried using the exact same eight patient HPO terms.**

This directly addresses your motivating claim, removes phenotype-set variation as the dominant confounder, and gives “0.5871” a defensible reference distribution. Even 20–30 reasonably comparable public genomes would be more relevant than 75 runs formed from only three genomes and 25 unrelated phenotypes.

If you need to recover compute, cut **S6’s unphased arm** first. Unphased is already the patient-like default and tells you little unless Exomiser’s phase handling has first passed a tiny technical sentinel test. Retain trans versus cis only after that validation.

---

## 7. A cheaper or stronger experiment

7.1. **For the Track 1 clinical claim, statistical phasing is more valuable than the benchmark as currently designed.** It addresses the largest unresolved fact in the actual case: whether the two BUB1B variants plausibly lie in trans. Run Beagle/SHAPEIT locally with an appropriate reference panel, but state clearly that reference-panel phasing of rare variants is probabilistic and is not equivalent to parental or read-backed phase. Report posterior certainty or concordance, not simply “trans.”

7.2. **For pipeline validation, a stronger experiment is a blinded replay of many public solved cases.** Use public cases with frozen VCF/phenotype/causal-gene truth, remove any case whose truth was used to tune the analysis, and measure causal-gene rank. That tests real background burden, real call quality, heterogeneous genes, and imperfect phenotypes. It is substantially stronger than perfect ClinVar spike-ins, though acquiring harmonized public WGS cases may be the bottleneck.

7.3. Of your remaining backlog, my priority would be:

1. Statistical/read-backed phasing of the BUB1B pair.
2. Rewrite this benchmark’s null around the exact patient phenotype and more healthy genomes.
3. Power analysis before committing to fibroblast work.
4. Executable drug-filter engine if it produces auditable Track 2 outputs.
5. ΔΔG calibration last; it is unlikely to rescue or refute pathogenicity convincingly by itself.

The central flaw is not S1’s ClinVar circularity. It is that both sides of the ranking are favorable: **the variants point to the target genes, and the phenotype independently names the same target genes.** Combined with only three causal constructs and an invalid percentile null, the current design can produce an impressive-looking success rate without demonstrating the operating characteristics you say it measures.

