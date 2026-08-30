# Pre-registration v2 — MVA-Replay: putting our Track 1 score on a scale

**Team ciberpty · MVA Hackathon 2026 · written 2026-08-30, BEFORE any locked case was run.**

This file is committed to git before any script in `replay/` other than the phase pilot is executed.
Its git timestamp is the evidence that the case list, the endpoints, the predicted directions and the
stopping rules below were fixed in advance. Changes are appended as dated amendments at the bottom;
the text above the amendment line is never edited.

**Version history is part of the record.** `PREREGISTRO_v1_DRAFT.md` is the draft that was sent,
verbatim and unrun, to two independent reviewers (`evidencia/codex_replay_prereg.md`,
`evidencia/cursor_replay_prereg.md`). Both attacked it hard and largely agreed. This v2 is the
result. Nothing in v1 was ever run; the only thing executed before this file was the phase pilot,
whose result is declared below.

---

## What we already know before running — declared, not hidden

**1. The phase pilot (`PILOTO_FASE.md`, run 30-ago before this file was written).** Both reviewers
warned that our planned cis/trans stratum might measure nothing. We tested it on public data before
freezing anything. Exomiser 15.1.0 reads phase into ACMG evidence (trans → PM3, cis → BP2) but does
**not** apply it to the compound-heterozygous model: two pathogenic nonsense alleles declared on the
*same* chromosome are still called AR_COMP_HET, both still contribute, the classification is still
PATHOGENIC, and the rank is unchanged. The score penalty for cis is 0.34% (0.9339 → 0.9305);
unphased costs 0.15%. Three repeats of the same run gave identical scores, so the pipeline is
deterministic and these differences are signal.

**Consequence, fixed now:** the cis/trans stratum is withdrawn. Phase of the patient's own alleles
must be resolved outside this pipeline, and that work is promoted ahead of the rest of the backlog.

**2. Our Track 1 numbers**, which several predictions below are stated against: BUB1B rank 1 of 4,565
ranked genes, AD row combined score **0.5871** (pheno 0.5635), AR row **0.5538** (pheno 0.7920); the
first non-BUB1B gene was **FANCD2 at 0.2137** (pheno 0.6605). With five clinically unrelated HPO
terms BUB1B still ranked 1 at 0.4187. One run, one genome — that anecdote is what this turns into a
rate.

**3. Reviewer consensus we accepted rather than argued with.** Both reviewers independently said the
v1 design was rigged the same way: *the phenotype names the answer before any variant is read.* Both
said the random-phenotype null could not calibrate 0.5871. Both said the decoy gene (TTN) was a straw
man. Both said the "if S1 fails the benchmark is broken" clause was an escape hatch that licensed
tuning. v2 removes all four. **The case count drops from ~150 runs to 61.**

## Data — all public, no patient data anywhere in this analysis

| Role | Source | Version |
|---|---|---|
| Healthy genomes, tier 1 | GIAB HG001–HG007 GRCh38 benchmark VCFs | NIST v4.2.1 |
| Healthy genomes, tier 2 | 1000 Genomes 30× GRCh38, 3202-sample phased panel, per-sample extraction | 20220422 release |
| Ancestry / relatedness metadata | `integrated_call_samples_v3.20130502.ALL.panel` | 1000G |
| Spike-in alleles | `pipeline/resources/clinvar.vcf.gz` (GRCh38) | the same file Track 1 used |
| Reference bases for REF verification | UCSC hg38 per-chromosome FASTA (chr3, chr5, chr11, chr15) | hg38 |
| High-confidence regions | GIAB `*_v4.2.1_benchmark(_noinconsistent).bed` | NIST v4.2.1 |
| Pipeline under test | Exomiser 15.1.0 + data 2602_hg38, `tools/analysis_mva.yml` | unchanged from Track 1 |

The pipeline is **frozen**. The only fields that may differ between runs are: the VCF path, the
sample id, `hpoIds`, and the output path. No filter, frequency source, pathogenicity source or
inheritance-mode threshold is changed for any reason, including to make a case work.

## The estimand — named precisely, because the obvious name would be wrong

This benchmark measures **conditional retrieval behaviour given a perfect heterozygous call**: what
the pipeline does with an allele it has already been handed cleanly. It does **not** measure
end-to-end diagnostic sensitivity, because we never test detection — every planted call is `PASS`,
balanced and unambiguous. Any sentence in the final report that says "sensitivity" without that
qualifier is a reporting error.

---

# Experiment A — the scale for 0.5871 (primary)

Every healthy genome, **unspiked**, run against the patient's exact eight HPO terms
(HP:0002859, HP:0000121, HP:0004322, HP:0001508, HP:0003202, HP:0001622, HP:0001518, HP:0200067).
The phenotype query is frozen: this is the null for *our* number under *our* question, which the
withdrawn random-phenotype null was not.

**Genomes.** All seven GIAB samples (HG001–HG007) plus **30 unrelated 1000 Genomes individuals**,
selected by a rule fixed here: from the 2,504-sample unrelated panel, sort sample ids
lexicographically within each of the five superpopulations (AFR, AMR, EAS, EUR, SAS) and take the
first six of each. n = 37. HG002–HG004 and HG005–HG007 are two trios; HG001 is also in 1000G as
NA12878 and is excluded from the 1000G draw if it appears. **Effective independence is reported as
~33 unrelated individuals plus two trios, never as 37 independent draws.**

**Recorded per genome:** top-ranked gene, its MOI row and combined score; the runner-up and the gap;
BUB1B's own combined score and rank in each MOI row, or its absence; and the burden table below.

**Burden table, per genome** — because "number of genes ranked" is too weak a comparability check:
variants read, variants retained after the frozen filters, rare variants, protein-altering variants,
genes with ≥ 1 retained variant, genes with ≥ 2 qualifying heterozygous variants, chromosomes
present. GIAB v4.2.1 benchmark VCFs are autosome-only and high-confidence-region-only; the 1000G
panel is a site-filtered joint call. **Neither is a clinical WGS**, and the two tiers are reported
separately, never pooled into one percentile.

**P-A (on the record).** The patient's 0.5871 exceeds the **maximum** top-gene combined score
observed across all 37 healthy genomes. *If it does not, we report its percentile plainly and state
in the abstract that our headline score is inside the range a healthy genome produces under the same
phenotype query. That would be the most important negative result of Track 1 and it is not going in
a footnote.*

**P-A2.** In healthy genomes, BUB1B either does not appear in the ranked table or scores below 0.25.
*If BUB1B routinely scores high in healthy genomes under this phenotype, the phenotype alone is
carrying the answer.*

---

# Experiment B — variant contribution vs phenotype contribution, with a decoy the phenotype likes

The failure of v1 was that the planted gene and the queried phenotype pointed at each other. B breaks
that by planting the **same allele architecture** into a gene the phenotype *also* likes, and by
crossing every cell with a phenotype that likes nothing.

**Arm 1 — MVA gene.** Two real, public ClinVar records reproducing the Track 1 architecture in BUB1B:

| Allele | Record | ClinVar | Class | Consequence |
|---|---|---|---|---|
| 1 | `chr15:40209701 T>G` | 533901 | Pathogenic/Likely_pathogenic | nonsense (p.Leu737Ter) |
| 2 | `chr15:40220612 T>A` | 4600147 | Uncertain_significance | missense (p.Asn1002Lys) |

**Declared substitution:** the child carries `chr15:40220612 T>G`, which is *not* in ClinVar. We plant
the ClinVar record at the same position and codon, `T>A`, which produces the same protein change and
is the record our Track 1 report already discusses. One nucleotide differs. We use the public record
so that nothing patient-derived enters a public benchmark.

**Arm 2 — matched decoy.** The same architecture in **FANCD2** (chr3:10,026,370–10,101,937, Ensembl
ENSG00000144554, retrieved from Ensembl REST 30-ago-2026): one ClinVar P/LP allele + one ClinVar VUS
allele, picked by the pairing rule below. FANCD2 is the decoy because it is the gene that actually
came second in our Track 1 run under this exact phenotype (pheno score 0.6605) — it is a distractor
the phenotype already rates highly, not a size-mismatched straw man.

**Design.** 3 GIAB backgrounds (HG001, HG002, HG005 — one per ancestry) × 2 arms × 2 phenotype sets
= **12 spiked runs**, paired against the same three genomes unspiked under both phenotype sets
(6 runs, shared with Experiment A). Phenotype sets: the eight real terms, and the five verified as
not annotated to OMIM:257300 in round 7 (HP:0000365, HP:0000509, HP:0002205, HP:0002315, HP:0000989).

We do **not** use a "reduced" phenotype set. A two-term set containing rhabdomyosarcoma still names
BUB1B; presenting it as a dose–response would be a claim we cannot support.

**Endpoints, paired within genome:** planted-gene combined score in each MOI row; rank; whether both
planted alleles appear as contributing variants; ACMG classification and evidence codes; and
Δ(real − unrelated) combined score. **Combined score is the primary endpoint and rank is secondary**,
because rank depends on how many competitors the background callset happens to contain and these
backgrounds have fewer than a clinical WGS.

**Predictions on the record:**

- **P-B1.** With the real phenotype, planted BUB1B reaches rank 1 in 3 of 3 backgrounds.
- **P-B2.** With the unrelated phenotype, planted BUB1B still reaches rank 1 in ≥ 2 of 3. *We expect
  our own pipeline to fail this. It is the round-7 control generalised, and confirming it is a
  concession we are pre-committing to publish, not a win.*
- **P-B3.** With the real phenotype, planted **FANCD2** also reaches rank 1 in ≥ 2 of 3 backgrounds.
  *If a phenotypically plausible decoy carrying the same allele architecture wins just as easily, the
  answer is carried by the variants and the phenotype only orders the shortlist. We predict this, and
  it is an argument against our own submission's framing.*
- **P-B4.** Δ(real − unrelated) combined score for the planted gene is < 0.20 in every cell — i.e.
  the phenotype is worth less than a fifth of the score. *Our current report quotes a single ~24%
  figure from one run; this replaces it with a distribution or contradicts it.*

---

# Experiment C — how much of the score is ClinVar's whitelist?

BUB1B only, the same three backgrounds, real phenotype, three allele architectures:

| Architecture | Alleles |
|---|---|
| **C-hi** | two ClinVar P/LP |
| **C-mid** | one P/LP + one VUS *(this is Arm 1 of Experiment B — not re-run)* |
| **C-lo** | two ClinVar VUS |

= **6 new runs**.

**Pool and pairing rule, fixed now.** For gene G and class K, the pool is every ClinVar GRCh38 record
inside G's Ensembl span (±5 kb) satisfying **all** of:

1. `CLNREVSTAT` contains `criteria_provided`;
2. `CLNSIG`, after splitting on `|` and `/`, has an atom in {`Pathogenic`, `Likely_pathogenic`} for
   K = P/LP, or is exactly `Uncertain_significance` for K = VUS;
3. a single ALT allele, REF and ALT ≤ 50 bp;
4. `MC` contains a consequence the frozen `analysis_mva.yml` **keeps**: missense, nonsense,
   frameshift, splice acceptor or splice donor. Intronic, upstream, downstream and intergenic records
   are excluded here, in advance, because `variantEffectFilter` deletes them and a case built on one
   would fail as a pool bug that looks like a pipeline miss;
5. the locus lies inside the background genome's GIAB high-confidence BED (measured coverage of the
   target spans: BUB1B 96.1–97.2%, CEP57 98.1–98.3%, TRIP13 85.0–87.2%, per background);
6. no background record overlaps the locus — overlap, not just an exact POS match;
7. REF matches the hg38 reference FASTA at that position.

The surviving pool is sorted by position. **Pairing: allele 1 = the first record, allele 2 = the last
record.** For C-mid the pair is the two named records in Experiment B Arm 1. If a pool has fewer than
two survivors the case is declared unbuildable in the results, not patched. Pools are written to
`replay/pools/` before any locked run so the rule can be audited against its output.

**P-C.** Planted-gene combined score falls monotonically C-hi > C-mid > C-lo, and C-hi − C-lo ≥ 0.10.
*If C-lo scores the same as C-hi, Exomiser is not leaning on ClinVar the way our Track 1 report
claims, and the sentence "the signal comes from a ClinVar-whitelisted nonsense" has to be rewritten.*

---

## Builder validation, and the escape hatch we are closing

The v1 draft said that if the easy stratum failed, "the benchmark is broken, not the pipeline". Both
reviewers flagged that as a licence to tune the builder until the pipeline wins. It is removed.

The spike-in builder is validated **once**, before any locked case is run, on a **sentinel gene that
appears in no experiment above** (`SMC5`, from the MVA panel but not a case gene), against three
assertions:

1. both planted alleles appear in the Exomiser variants TSV for that run;
2. each planted REF matches the hg38 FASTA at that position;
3. no background record overlaps either locus.

Assertions 1–3 concern **ingestion only**. None of them refers to a rank, a score or a gene position
in the output. Once they pass, the builder is frozen. After the freeze:

- a planted allele that does not reach the variants TSV is a **`technical_failure`**, counted and
  reported, never silently dropped and never a false negative;
- a planted gene that ranks poorly is a **result**. It is not debugged.

## Stopping rules

- The case list above is complete: 37 (A) + 12 (B) + 6 (C) = **55 spiked-or-null runs**, plus the
  6 unspiked GIAB × 2 phenotype-set runs shared between A and B = **61 Exomiser runs**.
- Nothing is added after the first result is seen.
- No endpoint is redefined after unblinding. An endpoint that turns out unmeasurable is declared so
  in a dated amendment with its reason, as the cis/trans stratum already was.
- Results are reported **per construct and per background**. Three backgrounds carrying the same
  allele pair are three perturbations of one construct, not three independent cases, and no binomial
  rate is computed over them.

## Limitations declared in advance

- **The backgrounds are not clinical WGS.** GIAB v4.2.1 is autosome-only and high-confidence-region
  only; the 1000G panel is a site-filtered joint call. Both carry a different rare-variant burden
  from a clinical singleton, which makes ranks easier and the null in Experiment A conservative in a
  direction that *helps* P-A. The burden table quantifies it; the report must state the direction.
- **The planted calls are immaculate.** `PASS`, `QUAL=100`, `DP=44`, `AD=22,22`, `GQ=99`. Detection
  difficulty is not tested at all. Hence the estimand name above.
- **The spike-ins come from ClinVar, which Exomiser consults.** Experiment C exists to measure the
  size of that dependence rather than to deny it. Even C-lo alleles are ClinVar records, so C
  measures a gradient inside ClinVar, not ClinVar versus no-ClinVar.
- **Three case genes and one decoy.** This is a replay of *our* case, not a general rare-disease
  benchmark, and no sentence in the report may generalise it to one.
- **Planting variants is not simulating disease.** Nothing here validates the clinical
  interpretation. It measures retrieval only.
- **A trio is not three individuals.** HG002–HG004 and HG005–HG007 are reported as families.

---
## Amendments

*(none yet — amendments are appended below with a date, never edited into the text above)*

### Amendment 1 — 2026-08-30, before any locked case was run

**The pool rule as written admits 0-star records.** Criterion 1 of the pool rule says *"`CLNREVSTAT`
contains `criteria_provided`"*. ClinVar's 0-star review status is the string
`no_assertion_criteria_provided`, which **contains** that substring. The rule as written therefore
admits exactly the records it was meant to exclude.

This was caught by the sentinel validation, not by reading the code: the builder selected ClinVar
2443708 (`no_assertion_criteria_provided`) as the second sentinel allele.

**Criterion 1 is tightened to:** `CLNREVSTAT` starts with `criteria_provided`, or equals
`reviewed_by_expert_panel` or `practice_guideline`.

Effect on the pools, all of which were rebuilt and re-written to `replay/pools/`:

| Gene | P/LP before → after | VUS before → after |
|---|---|---|
| BUB1B | 82 → **78** | 1434 → **1430** |
| CEP57 | 38 → **34** | 664 → **663** |
| TRIP13 | 9 → **5** | 96 → **95** |
| FANCD2 | 273 → **263** | 707 → **704** |
| SMC5 (sentinel) | 4 → **2** | 119 → **118** |

**No locked case had been run when this was found.** Nothing else in the rule changes.

### Amendment 2 — 2026-08-30, same session

**`GQ` must be declared in the background header.** The pre-registered spike-in FORMAT is
`GT:DP:AD:GQ`, but the background preparation strips `FORMAT/GQ`, so `bcftools concat` refused the
insertion ("Tag not defined in header"). A `##FORMAT=<ID=GQ,Number=1,Type=Integer>` line is added to
each background header with `bcftools reheader`. **No record data changes.** The frozen
`analysis_mva.yml` contains no genotype-quality or allele-balance filter, so the seven Experiment A
runs already completed before this change remain valid and are not re-run.

### Builder validation — 2026-08-30, PASSED, builder now frozen

Sentinel gene **SMC5** (in the MVA panel, in no experiment above), background HG002, two ClinVar
Likely_pathogenic alleles selected by the frozen rule:

| Allele | Locus | ClinVar | Review status | Consequence |
|---|---|---|---|---|
| 1 | `chr9:70267944 G>T` | 4856047 | criteria_provided, single submitter | nonsense |
| 2 | `chr9:70315463 CTTAT>C` | 4845894 | criteria_provided, single submitter | frameshift |

| Assertion | Result |
|---|---|
| 1. both planted alleles reach Exomiser's variants TSV | **PASS** — both present, both `CONTRIBUTING_VARIANT=1` under AR, annotated `stop_gained` and `frameshift_truncation`, both LIKELY_PATHOGENIC |
| 2. each planted REF matches the hg38 FASTA | **PASS** |
| 3. no background record overlaps either locus | **PASS** |

None of the three assertions refers to a rank or a score. **The builder is frozen as of this line.**
From here, a planted allele that does not reach the variants TSV is a `technical_failure`; a planted
gene that ranks poorly is a result and is not debugged.

*(Recorded for context, not as an assertion: SMC5 reached rank 2 with combined score 0.4476, behind
the background's own top gene KRT17 at 0.4881.)*

### Amendment 3 — 2026-08-30, triggered by the pre-registered ingestion assertion

**"Inside the gene's Ensembl span (±5 kb)" is not the same as "a variant in the gene."** The pool rule
placed no requirement on which gene ClinVar actually annotates a record to.

This was caught by the mechanism the pre-registration put in place, not by inspection: the ingestion
check on `B_arm2_FANCD2_HG001` reported **1 of 2 planted alleles reaching Exomiser's variants TSV**.
The missing allele was ClinVar **2312080**, whose `GENEINFO` is **`FANCD2OS:115795`** — a different
gene on the opposite strand — sitting 2,827 bp beyond the end of FANCD2 inside the ±5 kb padding.
Exomiser annotated it correctly to FANCD2OS, so it never appeared as a FANCD2 variant. Reviewer 1
predicted exactly this failure mode (`evidencia/codex_replay_prereg.md`, point 1.4).

**Two criteria are added to the pool rule:**

8. `INFO/GENEINFO` must name the target gene (symbol match before the `:` in any `|`-separated entry);
9. the record must lie inside the gene body **excluding** the ±5 kb padding.

Effect on the pools: BUB1B **unchanged** (78 P/LP, 1430 VUS), CEP57 34→**17** / 663→**590**,
TRIP13 5→**5** / 95→**72**, FANCD2 263→**263** / 704→**679**, SMC5 unchanged.

**Which cases are affected.** The BUB1B first/last picks are identical before and after
(C-hi `40165052`+`40218501`, C-lo `40161221`+`40220755`), so **Experiments B arm 1 and C are not
re-run**. Only the FANCD2 decoy arm changes (second allele `10104764` → `10101244`, ClinVar 1224522)
and its six cells are rebuilt and re-run. The affected pre-amendment cells are reported as
`technical_failure` in the results, as the stopping rules require, and are not deleted.

**Direction of the fix, stated for the record:** correcting this makes the decoy arm **stronger**, not
weaker. In the pre-amendment run the decoy reached rank 58 and 69; in the first re-run cell it reaches
**rank 1**. The amendment therefore works against prediction P-B3's failure and against our own
framing — it is not a fix in our favour.


### Amendment 4 — 2026-08-30, arithmetic correction to the declared pilot result

The phase pilot summarised at the top of this file reports the cis penalty as "0.34%". That is the
**absolute** difference (0.9339 − 0.9305 = 0.0034) written as if it were a percentage; expressed as a
share of the score it would be 0.36%. Both reviewers caught it independently in the round-8
verification.

**We are not restating it as a share at all.** The combined score is a non-linear function of its
inputs, which is exactly the reason we withdrew the phenotype percentage from the Track 1 report, and
the same objection applies here and to the 0.0128 ClinVar difference. All three are reported as
absolute differences from here on: **cis costs 0.0034, unphased costs 0.0014, and removing ClinVar
costs 0.0128.** The pilot's conclusion — that phase does not reach the compound-heterozygous model —
is unaffected, since it never depended on the size of the difference.

The original text above is left as written, per this file's own rule.
