# Pre-registration — MVA-Replay: what are the operating characteristics of our Track 1 pipeline?

**Team ciberpty · MVA Hackathon 2026 · written 2026-08-30, BEFORE any replay case was run.**

This file is committed to git before `01_*.py` is executed for the first time. Its git timestamp is
the evidence that the case list, the metrics, the predicted directions and the stopping rules below
were fixed in advance. If any of them changes, the change and its reason are appended at the bottom
as a dated amendment — the original text is never edited.

---

## Why we are running this

Our Track 1 submission reports a single number: BUB1B ranks 1 of 4,565 genes, combined score 0.5871.
Both reviewers said the same thing about the whole project — *"everything you have is reasoning, you
produced no results"*. The DepMap pre-registration answered that for Track 2. This answers it for
Track 1, and it answers a question we cannot currently answer at all:

**We have never measured what our pipeline does when the answer is not there.** One patient, one
run, one hit. We do not know its sensitivity, we do not know its false-positive rate, and we do not
know what score a *healthy* genome produces under the same phenotype query. Without that, "rank 1 of
4,565" is a number without a scale.

Our own HPO control already exposed the weak point: unrelated phenotype terms still put BUB1B at
rank 1, which forced us to relabel the finding *variant-driven, phenotype-consistent*. That control
was one run on one genome. MVA-Replay turns it into a rate.

**This can go against us.** If a healthy GIAB genome routinely produces a top-ranked gene scoring
above 0.5871, our headline number is unremarkable and we will report it as such.

## Data — all public, no patient data anywhere in this analysis

| Role | Source | Version |
|---|---|---|
| Background genome 1 (CEU) | GIAB `HG001_GRCh38_1_22_v4.2.1_benchmark.vcf.gz` | NIST v4.2.1 |
| Background genome 2 (AJ) | GIAB `HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz` | NIST v4.2.1 |
| Background genome 3 (Han Chinese) | GIAB `HG005_GRCh38_1_22_v4.2.1_benchmark.vcf.gz` | NIST v4.2.1 |
| Spike-in allele source | `pipeline/resources/clinvar.vcf.gz` (GRCh38) | the same file the Track 1 triage used |
| Pipeline under test | Exomiser 15.1.0 + data 2602_hg38, `tools/analysis_mva.yml` | unchanged from Track 1 |

The pipeline is **frozen**. No parameter, filter, frequency source or pathogenicity source is changed
for this benchmark. If we tune anything after seeing a result, the benchmark stops being a benchmark.

## Spike-in construction — rule-selected, not hand-picked

The obvious failure mode of a synthetic benchmark is that the planted variants are chosen so that the
pipeline finds them. We remove the choice:

For a target gene G and a ClinVar class C, the candidate pool is every ClinVar GRCh38 record inside
the gene's Ensembl span (`pipeline/mva_panel.hg38.bed`) with:

- `CLNSIG` matching class C exactly — `Pathogenic` / `Likely_pathogenic` for class **P/LP**,
  `Uncertain_significance` for class **VUS**;
- `CLNREVSTAT` containing `criteria_provided` (≥1 star);
- a single ALT allele, REF and ALT ≤ 50 bp.

The pool is sorted by position and we take the **first, the median and the last** record. No other
selection is applied and no variant is replaced after a run. The exact `bcftools` command that builds
each pool is in `01_build_cases.py` and its output pools are written to `replay/pools/` before any
Exomiser run, so the pools can be audited against this rule.

A spike-in is written into the background VCF as a new record with `FILTER=PASS`, `QUAL=100` and
`GT:DP:AD` = the chosen genotype with `DP=44` and a balanced AD, matching the depth of the patient's
own WGS so that `alleleBalanceFilter` behaves the same way it did in Track 1. Records are inserted in
coordinate order and the file is re-indexed. If a spike-in position already carries a background
call, that case is **dropped and reported as dropped**, not moved.

## Case list — LOCKED. No case is added, removed or re-run after unblinding.

Genes: **BUB1B** (MVA1, OMIM 257300), **CEP57** (MVA2), **TRIP13** (MVA3). Decoy gene: **TTN**
(large, variant-rich, no MVA phenotype).

| Stratum | Architecture | Cases | Ground truth | Direction we predict |
|---|---|---|---|---|
| **S1** | two ClinVar **P/LP** alleles, in trans | 3 genes × 3 backgrounds = 9 | planted gene | easiest; rank 1 in ≥ 90% |
| **S2** | one **P/LP** + one **VUS**, in trans — *the patient's own architecture* | 3 × 3 = 9 | planted gene | rank 1 in ≥ 70% |
| **S3** | two **VUS** alleles, in trans | 3 × 3 = 9 | planted gene | **worse than S2**; this is the stratum that tells us how much of our result is ClinVar's whitelist rather than our pipeline |
| **S4** | one **P/LP** allele only, heterozygous — a **carrier**, not a patient | 3 × 3 = 9 | **no diagnosis** | we predict the gene still reaches rank ≤ 3 in ≥ 50% of cases. If so, that is a limitation of ours to report: rank 1 does not mean biallelic |
| **S5** | two P/LP alleles in the **decoy** gene | 1 × 3 = 3 | **not rank 1 under the MVA phenotype** | if the decoy takes rank 1, the phenotype contributes nothing |
| **S6** | the S2 architecture planted **in cis** (`0\|1` + `0\|1`, same phase set) and **unphased** (`0/1` + `0/1`), against the S2 trans case | 3 genes × 3 backgrounds × 2 = 18 | comp-het call should be **lost in cis** | if Exomiser calls AR_COMP_HET in cis, phase adds nothing and our "phase not demonstrated" caveat is weaker than we claimed |

**57 spiked cases.** Every case is run once with the patient's eight HPO terms.

Additionally, the nine **S2** cases are re-run with two more phenotype sets, to turn our one-off HPO
control into a rate: **reduced** (2 terms: HP:0002859 rhabdomyosarcoma, HP:0004322 short stature) and
**unrelated** (the five terms verified as not annotated to OMIM:257300 in round 7: HP:0000365,
HP:0000509, HP:0002205, HP:0002315, HP:0000989). 18 extra runs.

## The null distribution — the number that gives "rank 1 of 4,565" a scale

- **Null-A (n = 3).** Each unmodified background, queried with the patient's eight HPO terms. Records
  the top-ranked gene and its combined score. Small n, reported as n = 3, not dressed up.
- **Null-B (n = 75).** Each unmodified background × **25 random phenotype sets** of eight HPO terms.
  Each set is drawn, with a fixed seed (`seed=2026`, written here before drawing), from the terms
  annotated to a randomly chosen OMIM disease in `pipeline/resources/genes_to_phenotype.txt`, so the
  sets are clinically coherent rather than random noise. Records the top-ranked combined score of
  each run. This is the distribution of "what does the best gene in a genome *without* the causal
  variant score, for a real phenotype?"

The seed and the drawing rule are fixed now. The drawn sets are written to `replay/pheno_sets.tsv`
before any null run.

## Metrics, fixed now

1. **Sensitivity** per stratum: fraction of cases where the planted gene is at rank 1; also ≤ 5, ≤ 10.
2. **Displacement**: in positive cases, which gene beats the planted gene when one does, and by how
   much.
3. **Null percentile of our own result**: where 0.5871 falls in Null-B, and the three Null-A values.
4. **Carrier rate** (S4): fraction of carrier-only cases that reach rank ≤ 3.
5. **Phase effect** (S6): AR_COMP_HET called / not called, and Δrank, for cis vs trans vs unphased.
6. **Phenotype contribution**: Δ(combined score) between correct, reduced and unrelated HPO across
   the nine S2 cases, reported as a distribution, not the single 24% figure we currently quote.
7. **Background comparability**: number of genes ranked in a GIAB run vs the 4,565 of the patient's
   WGS. GIAB benchmark VCFs cover only high-confidence regions, so this benchmark's backgrounds carry
   *fewer* rare variants than a real clinical genome. We quantify the gap rather than hand-wave it.

## Predictions we are on the record for

- **P1.** S1 ≥ 90% rank 1. *If S1 fails, the benchmark is broken, not the pipeline — we debug the
  spike-in machinery and say so.*
- **P2.** S2 ≥ 70% rank 1.
- **P3.** S3 < S2. *If S3 ≈ S1, our claim that the finding is driven by a ClinVar-whitelisted
  nonsense is wrong and the Track 1 report needs rewriting.*
- **P4.** S4 reaches rank ≤ 3 in ≥ 50% of cases. *We expect our pipeline to fail this. It is the
  honest version of the "variant-driven" concession, with a number.*
- **P5.** S5 decoy is not rank 1 in ≥ 2 of 3 backgrounds.
- **P6.** cis loses the AR_COMP_HET call in ≥ 2 of 3 backgrounds per gene.
- **P7.** 0.5871 is above the 95th percentile of Null-B. *If it is not, we report that our headline
  number is inside the range a healthy genome produces for an arbitrary phenotype. That would be the
  most important negative result in the project and it goes in the abstract, not a footnote.*

## Stopping rules

- The case list above is complete. Nothing is added after the first result is seen.
- A run that fails technically (Exomiser error, timeout, dropped spike-in) is reported in a
  `technical_failures` count. It is never silently excluded.
- No metric is redefined after unblinding. If a metric turns out to be unmeasurable, it is declared
  unmeasurable in an amendment with the reason, exactly as H2 was in the DepMap pre-registration.
- We do not tune the Exomiser analysis in response to any result.

## Limitations declared in advance

- **GIAB benchmark VCFs are high-confidence-region only.** They carry a lower rare-variant burden
  than clinical WGS, so sensitivity here is an *upper bound* and the false-positive rate a *lower
  bound*. Metric 7 measures the size of that gap.
- **Spike-ins come from ClinVar,** the same database Exomiser consults. S1 is therefore partly
  circular by construction; S3 exists to break that circularity, and the S1→S3 gradient is the
  interesting quantity, not S1 alone.
- **Three backgrounds only.** Null-A has n = 3 and will be reported as such.
- **Single ancestry per background.** The frequency filters are ancestry-sensitive; hiPhive is not.
- **Synthetic biallelic architecture is not a synthetic patient.** We plant variants, not disease.
  Nothing here validates the *clinical* interpretation, only the *retrieval* behaviour.

---

## Amendments

*(none yet — amendments are appended below with a date, never edited into the text above)*
