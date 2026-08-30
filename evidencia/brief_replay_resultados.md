You reviewed our benchmark PRE-REGISTRATION before it ran and told us it was rigged four ways. We
rewrote it, ran it, and this is what came out. Your job now is to attack the RESULTS and the
conclusions we drew from them — not the design, which you already fixed.

Context you already have: team ciberpty, MVA Hackathon 2026, Track 1 submitted and scored 100/100
(BUB1B compound het, MVA1). Two AI judges said "everything you have is reasoning, you produced no
results". This is the second and third batch of our own results.

What changed after your critique: the random-phenotype null was killed and replaced by healthy
genomes queried with the patient's exact eight HPO terms; TTN was replaced by FANCD2 (the gene that
actually came second in our real run); the "if the easy stratum fails the benchmark is broken" escape
hatch was removed and replaced by a sentinel-gene builder freeze; the case count went from ~150 to 61.
Three dated amendments are at the bottom of the pre-registration — read them, two of them exist
because the mechanisms you demanded caught real defects.

Everything below is verbatim. Do not go looking for files; you have what we have.

=========================== 1. PRE-REGISTRATION v2 (with amendments) ===========================
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

=========================== 2. RESULTS ===========================
# MVA-Replay — results

**Team ciberpty · MVA Hackathon 2026 · started 30-ago-2026.**
Design and predictions were fixed in `PREREGISTRO.md` and committed (`8086dd4`) before any locked case
ran. Amendments 1–3 are dated and appended there. **Experiment A tier 2 (30 × 1000G genomes) is still
running; this file is complete for tiers already finished and says so where it is not.**

---

## 0. An error this benchmark found in our already-submitted Track 1 report

`entrega/methods_track1.md` says, twice:

> "Removing the two contaminating terms drops the score from 0.5506 to 0.4187 — about 24% — **That is
> the size of the phenotype's contribution here**" … "the phenotype contributes **about 24% of the
> score**".

**That is the wrong pair of runs.** Both 0.5506 and 0.4187 are *unrelated-HPO controls*; the first
was the contaminated one, the second the corrected one. The delta between them measures what two
MVA-annotated terms leaking into a control were worth — not what the patient's phenotype is worth.

| Run | HPO set | BUB1B (AD row) |
|---|---|---|
| real | the patient's eight terms | **0.5871** |
| contaminated control | five "unrelated" terms, two annotated to MVA1 | 0.5506 |
| clean control | five verified-unrelated terms | 0.4187 |

The phenotype's contribution is **0.5871 → 0.4187 = 0.1684, i.e. 28.7%**, not 24%.

MVA-Replay reproduces both endpoints exactly, in three unrelated healthy genomes (§2), so the
corrected figure is replicated rather than recomputed from the same single run. The conclusion
("variant-driven, phenotype-consistent") is unchanged; the number attached to it is not.

---

## 1. Experiment A — what a healthy genome scores under the patient's phenotype

Seven GIAB genomes, unspiked, queried with the patient's exact eight HPO terms.

| Genome | Top-ranked gene | Combined score | Genes ranked |
|---|---|---|---|
| HG004 | GJB2 | **0.5619** | 2,495 |
| HG002 | KRT17 | 0.4881 | 2,387 |
| HG005 | RYR2 | 0.4194 | 2,274 |
| HG003 | APOB | 0.4188 | 2,431 |
| HG007 | CLDN24 | 0.2048 | 2,392 |
| HG006 | STIM2 | 0.0599 | 2,276 |
| HG001 | PAH | 0.0578 | 1,872 |

- **P-A holds so far:** our 0.5871 is above all seven. The margin to the highest is **0.025 (4.3%)**.
- **P-A2 holds strongly:** BUB1B does not appear in the ranked table of **any** of the seven.
- **Metric 7:** these genomes rank a median of 2,387 genes against the patient's 4,565. The
  competitor set is roughly half the size, which makes rank easier here than in a clinical WGS and
  biases the null *in our favour*. The score endpoint does not have this problem (§2).

⏳ Tier 2 — 30 unrelated 1000 Genomes 30× individuals, six per superpopulation — is running. With
n = 7 the honest statement is a range, not a percentile.

## 2. Experiment B — the score is a property of two alleles and a phenotype, not of the genome

Planting the two public ClinVar records of the Track 1 architecture (533901 `chr15:40209701 T>G`
nonsense + 4600147 `chr15:40220612 T>A` VUS) into three unrelated healthy genomes:

| Phenotype | BUB1B rank | BUB1B combined score | Our patient's value |
|---|---|---|---|
| the eight real terms | **1 in 3/3** | **0.5871 in all three** | 0.5871 |
| five verified-unrelated terms | 1 in 2/3 (rank 3 in HG005) | **0.4187 in all three** | 0.4187 |

**Both of our headline numbers reproduce to four decimal places in genomes that are not the
patient's.** Exomiser's gene combined score is fully determined by the planted alleles and the
phenotype query; the rest of the genome contributes nothing to it. What the background changes is the
*rank* — in HG005, whose own top gene reaches 0.8108 under the unrelated terms, BUB1B at 0.4187 falls
to rank 3.

- **P-B1 confirmed** (rank 1 in 3/3 with the real phenotype).
- **P-B2 confirmed** (rank 1 in 2/3 with an unrelated phenotype) — this is the concession we
  pre-committed to publishing, now a rate rather than an anecdote.
- **P-B4 confirmed**: Δ = 0.1684 < 0.20. As a fraction of the score, **28.7%** (see §0).
- **Rank is not a portable endpoint and score is.** Any statement of the form "rank 1 of N" has to
  carry N; the score does not.

### Decoy arm (FANCD2) — **P-B3 is falsified, and in our favour**

FANCD2 is the gene that actually came second in our Track 1 run, so the phenotype already rates it
highly. We predicted that the same P/LP + VUS architecture planted there would take rank 1 in at
least 2 of 3 backgrounds. It did not.

| Phenotype | FANCD2 rank | FANCD2 combined score |
|---|---|---|
| the eight real terms | **1 in 1/3** (only HG001) | 0.1841 in all three |
| five unrelated terms | 0 in 3 | 0.0580 in all three |

**P-B3 falsified**: rank 1 in 1/3, not ≥ 2/3. We predicted the pipeline would fail to discriminate
and it discriminated. Reported as a falsified prediction, not quietly rewritten.

**The mechanism is worth more than the verdict.** In HG002, with the real phenotype:

| Gene | winning MOI row | phenotype score | variant score | OMIM | combined |
|---|---|---|---|---|---|
| **FANCD2** (decoy) | AR | **0.6605** | 0.9226 | 1.0000 | **0.1841** |
| **BUB1B** (planted) | AD | 0.5635 | 1.0000 | 1.0000 | **0.5871** |
| BUB1B | AR | 0.7920 | 0.9615 | 1.0000 | 0.5538 |

The decoy has a **higher** phenotype score than the row that wins for BUB1B, and a comparable variant
score, yet scores 3.2× lower. Two things separate them, and neither is "the phenotype prefers BUB1B":

1. **BUB1B wins on the AD row** — a single ClinVar-pathogenic nonsense under a *dominant* model, with
   the variant term maxed at 1.0000 — not on the recessive row that matches the actual diagnosis.
2. **The combination is steeply non-linear in the phenotype term.** At near-identical variant scores,
   an AR phenotype score of 0.7920 yields 0.5538 while 0.6605 yields 0.1841. A 0.13 difference in
   phenotype score becomes a 3× difference in combined score.

The decoy's alleles were rule-selected and are not matched to BUB1B's for variant strength (its
missense scores 0.8453 against 0.9229). A decoy matched on variant score as well as phenotype would
be a stronger test, and we did not run one.

## 3. Experiment C — how much of the score is ClinVar's classification

Same gene, same phenotype, same three genomes; only the ClinVar class of the two planted alleles
changes.

| Architecture | BUB1B combined score | Rank (HG001 / HG002 / HG005) | Exomiser ACMG |
|---|---|---|---|
| two P/LP alleles | **0.9332** | 1 / 1 / 1 | PATHOGENIC |
| **one P/LP + one VUS — the child's architecture** | **0.5871** | 1 / 1 / 1 | PATHOGENIC |
| two VUS alleles | **0.1120** | 1 / 5 / 3 | UNCERTAIN_SIGNIFICANCE |

- **P-C confirmed, and by a wide margin:** C-hi − C-lo = **0.8212**, against a pre-registered
  threshold of 0.10. The gradient is monotonic and the scores are identical across all three genomes.
- The consequence for our own submission is the uncomfortable one: **had the child's nonsense allele
  not been in ClinVar as Pathogenic, the same two variants in the same gene under the same phenotype
  would have scored 0.1120 and would have lost rank 1 in two of three backgrounds.** Our Track 1
  statement that the ranking is carried by the ClinVar-whitelisted nonsense is not just supported —
  it is the dominant term, worth 88% of the score.

## 4. Pilot, reported separately

`PILOTO_FASE.md` — Exomiser reads phase into ACMG evidence (trans → PM3, cis → BP2) but never into
the compound-heterozygous model; the score penalty for cis is 0.34% and the rank does not move. This
is why the cis/trans stratum was withdrawn and why phase had to be attacked outside the pipeline
(`fase/RESULTADO.md`).

## 5. Predictions scoreboard

| Prediction | Status |
|---|---|
| P-A — 0.5871 above every healthy genome's top score | holds at n = 7 ⏳ n = 37 pending |
| P-A2 — BUB1B absent or < 0.25 in healthy genomes | **confirmed** (absent in 7/7) |
| P-B1 — planted BUB1B rank 1 in 3/3 with real HPO | **confirmed** |
| P-B2 — planted BUB1B rank 1 in ≥ 2/3 with unrelated HPO | **confirmed** (2/3) |
| P-B3 — planted decoy rank 1 in ≥ 2/3 with real HPO | **FALSIFIED** — rank 1 in 1/3 |
| P-B4 — Δ(real − unrelated) < 0.20 | **confirmed** (0.1684) |
| P-C — monotonic gradient, C-hi − C-lo ≥ 0.10 | **confirmed** (0.8212) |

Technical failures: 2 cells (`B_arm2_FANCD2_HG001`, both phenotypes, pre-amendment), superseded by
the amendment-3 re-run and retained in `resultados_todos.tsv`. One prediction of six resolved so far
is falsified (P-B3), and it is falsified in the direction that favours us — which is the direction
that needs saying out loud, because the amendment that produced it was the one that made the decoy
*stronger*.

=========================== 3. PHASE PILOT ===========================
# Pilot result — Exomiser 15.1.0 reads phase for ACMG, but not for the compound-heterozygous call

**Team ciberpty · 30-ago-2026 · run before the MVA-Replay case list was frozen.**

This was a machinery test, not a pre-registered case. Its purpose was to decide whether stratum S6 of
MVA-Replay (cis vs trans vs unphased) measures anything at all. Both external reviewers of our
pre-registration draft warned, independently, that it might not. **It does not measure what we
planned to measure, and the reason is a reportable property of the tool.**

## What was run

Background: GIAB HG002 GRCh38 v4.2.1 benchmark VCF, chr15 only (123,705 variants), `INFO` and the
`ADALL`/`GQ`/`PS` fields stripped for size. Two real ClinVar nonsense variants of BUB1B were inserted
as `FILTER=PASS`, `QUAL=100`, `GT:DP:AD` het at `DP=44`, `AD=22,22`:

- `chr15:40165186 C>T` — ClinVar Pathogenic, `stop_gained`
- `chr15:40218501 A>T` — ClinVar Pathogenic, `stop_gained`

Four encodings of the same two variants, everything else identical:

| Encoding | GT of variant 1 | GT of variant 2 | phase set |
|---|---|---|---|
| **trans** | `0\|1` | `1\|0` | none |
| **cis** | `0\|1` | `0\|1` | none |
| **cis + PS** | `0\|1` | `0\|1` | both `PS=40165186` |
| **unphased** | `0/1` | `0/1` | none |

Pipeline: the frozen Track 1 analysis (`tools/analysis_mva.yml`, Exomiser 15.1.0, data 2602_hg38),
the patient's eight HPO terms, sample id `HG002`, sex MALE. `analysis_mva.yml` contains no
`alleleBalanceFilter`, so the absence of `GQ` on the inserted records cannot affect this result.

## Result

| Encoding | AR_COMP_HET called | both alleles contributing | ACMG evidence | ACMG class | combined score | rank |
|---|---|---|---|---|---|---|
| trans | yes | yes | PVS1, PM2_Supporting, **PM3**, PP4_Moderate, PP5 | PATHOGENIC | **0.9339** | 1 |
| cis | yes | yes | PVS1, PM2_Supporting, PP4_Moderate, PP5, **BP2** | PATHOGENIC | **0.9305** | 1 |
| cis + PS | yes | yes | identical to cis | PATHOGENIC | **0.9305** | 1 |
| unphased | yes | yes | PVS1, PM2_Supporting, PP4_Moderate, PP5 | PATHOGENIC | **0.9325** | 1 |

The `trans` run was repeated three times and returned 0.9339 every time: the pipeline is
deterministic, so the differences above are signal, not run-to-run noise.

## What this means

1. **Phase is read.** Exomiser correctly converts the genotype encoding into ACMG evidence: `trans`
   earns **PM3** (pathogenic variant seen in trans), `cis` earns **BP2** (seen in cis with a
   pathogenic variant), unphased earns neither. Adding an explicit `PS` phase set changes nothing —
   the pipe character alone is sufficient, and a shared phase set is not required.
2. **Phase does not reach the compound-heterozygous model.** In every encoding, including two
   pathogenic nonsense alleles declared to be on the *same* chromosome, Exomiser still calls
   AUTOSOMAL_RECESSIVE_COMP_HET, still marks both alleles as contributing, still classifies both as
   PATHOGENIC, and still ranks the gene first.
3. **The penalty for being on the wrong haplotype is 0.34%** (0.9339 → 0.9305). Being unphased costs
   0.15%. Neither changes the call or the rank.

## Consequence for our own submission

Our Track 1 and Track 2 reports carry the caveat *"phase not demonstrated"*. This pilot shows the
caveat is **stronger than we stated, not weaker**: our pipeline would have produced the same rank,
the same score to three decimal places, and the same PATHOGENIC classification if the child's two
BUB1B variants sat on the same chromosome — which would not be MVA at all. The tool cannot resolve
the question, so the question has to be resolved outside the tool.

That is why stratum S6 is withdrawn from MVA-Replay (18 runs that would only re-measure this) and why
independent phasing of the patient's own two variants is promoted ahead of it.

## Reproduce

```
replay/smoke/          bg_chr15.vcf.gz, trans/cis/cis_ps/unph.vcf.gz, sample_HG002.yml
replay/smoke/out/      *.genes.tsv, *.variants.tsv, *.log
```

No patient data is used anywhere in this pilot: the background is public GIAB, the two variants are
public ClinVar records.

=========================== 4. PHASING OF THE PATIENT'S OWN VARIANTS ===========================
# The phase of the two BUB1B variants is not resolvable from the data we have — and here is exactly why

**Team ciberpty · MVA Hackathon 2026 · 30-ago-2026.**

Both external reviewers of our benchmark pre-registration independently said the same thing: the
largest unresolved fact in the actual case is whether the child's two BUB1B variants lie in *trans*,
and settling it matters more than any synthetic benchmark. *"If phasing says cis, Track 1 is wrong
regardless of any rank."* This is the result. It is negative, it is definitive, and it took three
queries and one 18-second run rather than the 2–5 days the backlog allocated.

**Answer: with this dataset, phase cannot be determined — not "inconclusively", but *not computable*.
Both routes are closed, each for a specific and measurable reason.**

## The variants

| | Locus (GRCh38) | cDNA | Protein | ClinVar | gnomAD max AF |
|---|---|---|---|---|---|
| Allele 1 | `chr15:40209701 T>G` | c.2210T>G | p.Leu737Ter | 533901, Pathogenic/Likely pathogenic | **1.00 × 10⁻⁴** |
| Allele 2 | `chr15:40220612 T>G` | c.3006T>G | p.Asn1002Lys | absent (4600147 is `T>A`, VUS) | **9.0 × 10⁻⁷** |

Distance between them: **10,911 bp**.

## Route 1 — read-backed phasing: closed by the caller's own output

The patient VCF is a GATK singleton call set with `PGT`/`PID` fields available. Queried directly:

```
40209701  T>G   GT=0/1  PGT=.  PID=.  DP=46  AD=21,25  GQ=99
40220612  T>G   GT=0/1  PGT=.  PID=.  DP=28  AD=15,13  GQ=99
```

**Neither variant carries a phase group.** GATK physically phases only variants it can place on the
same read or read pair; at 10,911 bp apart with short-read WGS this is impossible, and the caller
says so by leaving both fields empty. The only phased genotypes anywhere in the 20 kb window are two
homozygous indels 2 bp apart (`40216568`, `40216570`, `PID=40216568_TA_T`), and homozygous sites
carry no phase information.

## Route 2 — statistical phasing: closed by the reference panel

Statistical phasing needs heterozygous markers that exist in the reference panel *between* the two
variants, so that a haplotype can be traced from one to the other. We counted them.

In the patient's 20 kb window there are exactly **four heterozygous sites**: the two causal variants,
`40216470 A>G`, and `40221421 G>C`. Checked against the 1000 Genomes 30× GRCh38 phased panel
(3,202 individuals, 6,404 haplotypes):

| Site | Inside the 10,911 bp interval? | In the 1000G panel? |
|---|---|---|
| `40209701 T>G` (allele 1) | boundary | **no** |
| `40216470 A>G` | **yes** | **no** |
| `40220612 T>G` (allele 2) | boundary | **no** |
| `40221421 G>C` | no — 809 bp beyond allele 2 | yes, AF 0.0075 |

**Inside the interval there is not one panel-present heterozygous marker.** Widening to ±100 kb, the
patient has 124 heterozygous sites, 118 of which are in the panel — but the nearest one before
allele 1 is `40192892` (16,809 bp upstream, AF 0.0016) and the nearest after allele 2 is `40221421`
(809 bp downstream, AF 0.0075). The 10.9 kb that has to be spanned is empty.

**Empirical confirmation.** Beagle 5.5 (27Feb25.75f), reference = the 1000G panel above, genetic map
= PLINK GRCh38, target = the patient's chr15:39.65–40.73 Mb (1,452 variants). The run completes in
18 seconds and outputs 26,194 phased markers. Of the patient's 1,452 input variants, 1,391 survive:

| Site | In Beagle's output |
|---|---|
| `40209701` (allele 1) | **dropped** |
| `40216470` | **dropped** |
| `40220612` (allele 2) | **dropped** |
| `40221421` | present, phased `0\|1` |

**The phasing tool discards both causal variants**, because a reference-panel phaser can only place a
variant that exists in the panel. There is no posterior to report, no seed instability to measure,
and no "probably trans" to write down.

## Why a bigger panel would not fix this

The absence is exactly what the allele frequencies predict. In 6,404 panel haplotypes, the expected
copy count is:

- allele 1, gnomAD AF 1.0 × 10⁻⁴ → **0.64 expected copies**;
- allele 2, gnomAD AF 9.0 × 10⁻⁷ → **0.006 expected copies**.

To have even one expected copy of allele 2, a reference panel would need on the order of **10⁶
haplotypes**. No public phased panel is within two orders of magnitude of that, and sending patient
genotypes to a remote imputation server is not an option for this dataset.

## What this changes in our submission

Our Track 1 and Track 2 reports carry the caveat *"phase not demonstrated"*, phrased as an
unfinished piece of work. It is not unfinished; it is **undoable with this dataset**, and the
sentence should say so with these numbers. Combined with the phase pilot (`replay/PILOTO_FASE.md`),
which showed that our pipeline would have returned the same rank, the same score to three decimals
and the same PATHOGENIC classification even if both variants sat on the same chromosome, the honest
statement is:

> The compound-heterozygous interpretation rests on the inheritance model and the phenotype, not on
> observed phase. Phase could not be observed: the two variants are 10,911 bp apart, so the caller
> produced no read-backed phase group for either; and neither variant, nor the only other
> heterozygous site between them, exists in the 1000 Genomes 3,202-sample reference panel, so a
> reference-panel phaser discards all three. Our ranking pipeline is itself phase-blind, so it could
> not have flagged the difference.

## What would resolve it, in order of cost

1. **Genotype the parents at the two loci.** Two targeted Sanger reactions per parent. If each parent
   carries one variant, phase is settled. Cheapest by a wide margin and the standard clinical answer.
2. **Long-read or linked-read sequencing of the child** (ONT / PacBio HiFi / 10x-style). A single
   read spanning 10.9 kb resolves it directly; PacBio HiFi reads average 15–20 kb.
3. **Allele-specific analysis of BUB1B transcript** (RNA from a cultured fibroblast or lymphoblast
   line, cDNA cloning or long-read cDNA). Also answers whether the nonsense allele escapes
   nonsense-mediated decay — relevant to the §6 experiment.

All three require new laboratory work. None can be done from the data in this challenge.

## Reproduce

```
fase/paciente_chr15_win.vcf.gz   ventana chr15:39,650,000-40,730,000 del paciente (renombrada a chr15)
fase/panel_chr15.vcf.gz          1000G 30x GRCh38 phased panel, chr15
fase/plink.chr15.GRCh38.map      mapa genético GRCh38
fase/prueba.vcf.gz               salida de Beagle
java -Xmx10g -jar beagle.jar gt=paciente_chr15_win.vcf.gz ref=panel_chr15.vcf.gz \
     map=plink.chr15.GRCh38.map chrom=chr15:39650000-40730000 out=prueba seed=1 nthreads=6
```

Nothing in this analysis leaves the machine. The panel and the map are public; the patient window is
local and covered by `data/BORRAR-AL-TERMINAR.md`.

=========================== WHAT WE WANT FROM YOU ===========================

Number every finding. Be blunt and specific; "consider adding more controls" is worthless.

1. **The claimed error in our already-submitted Track 1 report (§0 of the results).** We are saying
   the report's "the phenotype contributes about 24% of the score" cites the wrong pair of runs,
   because 0.5506 and 0.4187 are both unrelated-HPO controls. Before we spend one of our four
   remaining Track 1 submission slots on this: is it actually an error? Is 28.7% the right
   replacement, or is the whole framing of "the phenotype contributes X% of the score" unsound
   because the combination is non-linear (see the FANCD2 mechanism table)? Give us the sentence you
   would put in the report.

2. **"The combined score is a property of the two alleles and the phenotype, not of the genome."**
   We claim this because 0.5871 and 0.4187 reproduce to four decimals in three unrelated genomes.
   Is that claim over-stated? What would break it? Is there a reading in which this is a trivial
   consequence of how Exomiser computes the score, and therefore not a finding at all?

3. **Experiment C (0.9332 / 0.5871 / 0.1120).** We conclude ClinVar's classification is worth 88% of
   our score, and that without the Pathogenic call on the nonsense the same variants would have
   scored 0.1120 and lost rank 1 in two of three backgrounds. Attack that. In particular: the P/LP
   and VUS pools differ in more than ClinVar class (consequence type, frequency, REVEL/AlphaMissense
   scores), which one of you already warned about. Does the gradient survive that objection, and what
   single extra run would settle it?

4. **The phasing result.** We are claiming the phase is not merely undetermined but *not computable*,
   and we plan to put that in the report. Is the argument airtight? Specifically: (a) is "Beagle
   drops variants absent from the reference panel" a correct and complete statement of the tool's
   behaviour, or did we misconfigure it; (b) is there any phasing approach we have not considered
   that works with short-read singleton WGS — population-based, LD-based, allele-balance-based,
   anything; (c) is the expected-copy-count argument (0.64 and 0.006 copies in 6,404 haplotypes) the
   right way to say a bigger panel would not help?

5. **P-B3 falsified.** We predicted the FANCD2 decoy would take rank 1 in >=2/3 and it took 1/3. We
   report that as falsified and in our favour. Is our stated mechanism right — that BUB1B wins on its
   AD row and that the combination is steeply non-linear in the phenotype term — or are we telling a
   story about two numbers? What is the alternative explanation?

6. **What in these results contradicts something else we have written?** Every previous round of this
   project, the most valuable finding was one of our own claims contradicting our own data. Assume
   one is here and find it.

7. **P-A is the one still open** (7 healthy GIAB genomes so far, top scores 0.0578-0.5619, our 0.5871
   clears all seven by 0.025; 30 unrelated 1000 Genomes individuals are downloading). Given the
   margin is 4.3%, what should we pre-commit to saying if one or two of the 30 exceed 0.5871? Write
   the sentence for each case now, before we see the data.
