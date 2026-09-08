# Pre-registration — transferring MVA-Replay to a second gene, from a fresh clone

**Team ciberpty · MVA Hackathon 2026 · written 2026-09-07, BEFORE any run.**

This file is committed and pushed before `mva_replay.py` is invoked on TRIP13. Its git timestamp is
the evidence that the case, the alleles, the phenotype, the predictions and the stopping rules were
fixed in advance. Results are appended below the amendment line, dated; nothing above it is edited.

## Why this exists

The Track 2 report (§9) says the retrieval benchmark is *"packaged as a tool, not described as one"*
and that *"a team working on a different rare disease can spike their own gene into a public genome in
an afternoon."* Every run behind that sentence so far was made on this machine, in the analysis
directory, by the people who wrote the tool. The 6-Sep review named this as the gap with the highest
return: **demonstrate transfer, do not assert it.** Two things are measured here, and they are kept
apart:

1. **Scientific:** what the frozen Track 1 pipeline does with a *different* MVA gene, given a phenotype
   taken from a published case rather than from our own patient.
2. **Operational:** what a person who clones the public repository actually has to do before the tool
   returns an interpretable result, with the failures they hit, the wall-clock and the memory.

## The case — public, and not ours

PMID **42595739** (abstract on file: `evidencia/pubmed_auditoria_2026-09-06.xml`): a 12-year-old girl
with a left Wilms tumour at three years (nephrectomy and chemotherapy) and an orbital embryonal
rhabdomyosarcoma at twelve, presenting with proptosis, ptosis, visual acuity 20/160, chemosis and
corneal exposure. Exome sequencing found a likely pathogenic null variant in *TRIP13*
(c.998_999delCT, p.Ser333Leufs*30), diagnosis MVA3 (OMIM 617598). The abstract does not state
zygosity, and the report's own allele is **not** used here (see below). Nothing about this child
beyond the abstract is used.

**Phenotype, six HPO terms read off the abstract before any run**, resolved against the bundled
`hp.obo`:

| Term | Id | Sentence in the abstract |
|---|---|---|
| Nephroblastoma | HP:0002667 | "history of left Wilms' tumor" |
| Embryonal rhabdomyosarcoma | HP:0006743 | "histopathology was consistent with embryonal rhabdomyosarcoma" |
| Proptosis | HP:0000520 | "massive left proptosis" |
| Ptosis | HP:0000508 | "ptosis" |
| Reduced visual acuity | HP:0007663 | "visual acuity of 20/160" |
| Chemosis | HP:0012375 | "conjunctival chemosis" |

**Declared in advance:** Nephroblastoma is annotated to TRIP13 in HPOA (OMIM:617598, 6/6 cases), so
this phenotype *does* point at the gene. That is what any real MVA3 referral looks like, and the tool
reports it in `hpo_annotated_to_gene` rather than hiding it. The unrelated-phenotype control below is
what separates "the alleles carry it" from "the phenotype carries it".

## Alleles — the frozen pool rule, applied without looking

`replay/pools/TRIP13_PLP.tsv` was built on 2026-08-30 by the pool rule of `PREREGISTRO.md`
(Amendments 1 and 3 applied) and has five records. **Pairing rule, unchanged:** allele 1 = first record
by position, allele 2 = last.

| Allele | Locus (GRCh38) | ClinVar | Class | Review status | Consequence |
|---|---|---|---|---|---|
| 1 | `chr5:900524 T>TA` | 3910602 | Likely_pathogenic | criteria_provided, single submitter | frameshift |
| 2 | `chr5:914464 G>C` | 4070948 | Likely_pathogenic (MVA3) | criteria_provided, single submitter | splice acceptor |

The case report's own c.998_999delCT is not planted: it is not verified in the local ClinVar release,
and the pool rule is frozen. Two truncating alleles is the **C-hi architecture** of Experiment C, so
the BUB1B C-hi cells (AR combined score 0.9332 in all three backgrounds) are the comparison this
result is read against.

## Design

- **Tool:** `replay/mva_replay.py` as committed at the time of this file, unmodified. The Exomiser
  analysis (`analysis_mva.yml`), Exomiser 15.1.0 and the 2602 hg38 data are the frozen Track 1 pipeline.
- **Backgrounds:** GIAB HG001, HG002, HG005, the three of Experiment B.
- **Sex:** FEMALE (the case). Phase: `trans`. Everything else at the tool's defaults.
- **Unrelated control:** the tool's default five terms (HP:0000509, HP:0002205, HP:0002315,
  HP:0000989, HP:0000988), each checked today against `genes_to_phenotype.txt`: **none is annotated
  to TRIP13.** If the tool nevertheless refuses at run time, the refusal is a result and is reported; the
  reserve terms, in order, are HP:0001369, HP:0002099, HP:0003326, HP:0002014 (also checked, none
  annotated to TRIP13), and the substitution is recorded in an amendment.
- **Runs:** 3 backgrounds × 4 conditions (planted, noclinvar, unrelated, background) = **12 Exomiser
  runs.** Nothing is added after the first result is seen.

## Where it runs — the operational half

1. `git clone` of `github.com/cpu-16/mva-hackathon-2026` into an empty directory on this machine
   (the repository is private until the final evaluation, so the clone is authenticated; that is the
   only difference from what a judge will do).
2. In the bare clone, `python3 replay/test_output_reuse.py` and `replay/mva_replay.py --self-check`
   are run **before any resource is provided.** The self-check is expected to stop and name what is
   missing; that message is the first thing a judge sees and is recorded verbatim.
3. Resources are then made available **by symlink from the analysis machine**, one step at a time,
   each step recorded: the Exomiser installation and data, the ClinVar VCF and HPOA file, the hg38
   chr5 FASTA, the background VCFs. **Download time is not measured** (55 GB of Exomiser data were
   already on disk); the number of distinct manual steps is.
4. `--dry-run` once per background, then the real run, each Exomiser call wrapped in `/usr/bin/time -v`
   for wall-clock and maximum resident set size.

Every failure met on the way — a missing file, a wrong path, a refusal — is reported as a numbered
finding. The only permitted fix is to **documentation** (`README_TOOL.md`, the repository README) or
to a path the tool resolves. The analysis YAML, the spike-in builder and the scoring are not touched.

## Predictions, on the record

- **P-T1 (gate).** Both planted alleles reach Exomiser's variants table annotated to TRIP13, in 3 of 3
  backgrounds. *A failure is a `technical_failure`, reported and not debugged.*
- **P-T2.** With the six case-report terms, planted TRIP13 is gene rank 1 in **3 of 3** backgrounds with
  a combined score **≥ 0.80** in each. *If any background misses rank 1, the sentence in §9 about
  spiking "your own gene" acquires that exception, in the report, with the number.*
- **P-T3.** With the unrelated phenotype, planted TRIP13 is rank 1 in **at most 1 of 3** backgrounds.
  *The BUB1B analogue (one P/LP + one VUS) gave 1 of 3. Two truncating alleles may carry more: if
  TRIP13 stays rank 1 in ≥ 2 of 3, that is reported as "the architecture carries the answer without the
  phenotype", which weakens the phenotype-driven framing of Track 1 and is published as such.*
- **P-T4.** In the unspiked backgrounds, TRIP13 is absent from the ranked table or scores **< 0.25**
  under the case phenotype, in 3 of 3.
- **O-1.** From the bare clone, `test_output_reuse.py` passes with no resources present.
- **O-2.** From the bare clone, `--self-check` exits non-zero and its message names every missing
  resource in one go (no second run needed to discover another).
- **O-3.** The number of manual steps between the bare clone and a successful `--dry-run` is **≤ 5**,
  and every one of them is already described in `README_TOOL.md § Requirements`. *If a step is not
  described there, that is a documentation defect and is listed as such.*
- **O-4.** Each Exomiser call finishes in **≤ 120 s** wall-clock and **≤ 12 GB** maximum RSS on this
  machine (32 cores, 31 GB RAM, OpenJDK 25); one background, four conditions, in **≤ 10 min**.

## Stopping rules and what this does not show

- 12 Exomiser runs, three dry-runs, two bare-clone commands. Nothing else. No re-run to improve a
  number; a run that fails is reported as failed.
- This measures **conditional retrieval given a perfect heterozygous call** (the estimand of
  `PREREGISTRO.md`). It is not diagnostic sensitivity, not clinical validation, and not evidence about
  the girl in PMID 42595739.
- The operational half measures the tool on the machine it was written on, with resources symlinked
  rather than downloaded. It measures whether the **documentation** is complete and the tool's failure
  modes are informative, not whether a stranger's machine will run it.
- One gene, one architecture, three backgrounds. "The tool transfers" means exactly that and no more.

---
## Amendments and results

*(appended below with a date; the text above is never edited)*
