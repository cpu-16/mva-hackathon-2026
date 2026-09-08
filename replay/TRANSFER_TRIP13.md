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

### Results — 2026-09-07, 22:10–22:20 local, from clone `ee7a050` (the commit of this file)

Raw outputs (copied from the clone's `replay/out_tool/`): `replay/transfer_trip13/T2_TRIP13_HG00{1,2,5}.json`;
`provision_and_dryrun.sh` and `real_runs.sh` (the exact scripts that ran, including the symlink steps);
`bare_clone.log` (every tool invocation of the operational half with its exit code — the symlink commands
themselves are in the script, not echoed in the log) and `runs.log` (the three real runs, each whole tool
invocation under `/usr/bin/time -v`).

#### Scientific half — all four predictions held

| Background | planted (case HPO) | noclinvar | unrelated HPO | unspiked background | ingested |
|---|---|---|---|---|---|
| HG001 | **0.8332, rank 1**, AR | 0.8332, rank 1 | 0.4240, **rank 1** (AD row) | absent | 2/2 |
| HG002 | **0.8332, rank 1**, AR | 0.8332, rank 1 | 0.4240, rank 2 | 0.0000, rank 212 | 2/2 |
| HG005 | **0.8332, rank 1**, AR | 0.8332, rank 1 | 0.4240, rank 3 | absent | 2/2 |

- **P-T1 confirmed.** Both alleles reached the variants table in 3 of 3, both `CONTRIBUTING`, ACMG
  PATHOGENIC.
- **P-T2 confirmed.** Rank 1 in 3 of 3 with combined score 0.8332 in each — identical to four decimals
  across three backgrounds, the same stability the BUB1B construct showed. Phenotype score 0.6907.
  Runner-up: PAH (HG001), KRT17 (HG002), RYR2 (HG005), all background-native.
- **P-T3 confirmed, at the boundary.** Under the unrelated phenotype TRIP13 is rank 1 in exactly 1 of 3
  (HG001; ranks 2 and 3 in the others), with score 0.4240 in all three. Same pattern as BUB1B
  (rank 1/2/3 at 0.3965). Δ(planted − unrelated) = **0.4092**, larger than BUB1B's 0.1906: the six
  case-report terms, four of which are ophthalmic findings not annotated to TRIP13, still pull the
  score up by more than the eight MVA1 terms did. We report the absolute difference only.
- **P-T4 confirmed.** TRIP13 absent from the ranked table in HG001 and HG005; score 0.0000 at rank 212
  in HG002.
- **Not predicted, reported:** switching the ClinVar whitelist off changed the score by **0.0000** in
  all three backgrounds (whitelist flags went 1→0, score did not move), against 0.0021 for the BUB1B
  construct. For two truncating Likely_pathogenic alleles the whitelist bonus is worth nothing. ClinVar still
  enters through the ACMG route — `acmg_evidence` keeps PP5 with the whitelist off — so this is
  "the whitelist", not "ClinVar", as `README_TOOL.md` already warns.

#### Operational half — three of four predictions failed, and that is the useful part

*Corrected 7-Sep 22:50, after an adversarial read of this section: O-2 was first written up as "confirmed". By its own pre-registered wording ("no second run needed to discover another") it is falsified, and the count is three of four, not two.*

| Finding | Prediction | What happened |
|---|---|---|
| **F1** | O-1: tests pass in a bare clone | **Falsified.** `test_output_reuse.py` failed 9 of 9 sub-tests: `main()` calls `check_resources()` before the dry-run path, and the tests never stubbed it. The README sentence *"runs from a bare checkout"* was untrue at `ee7a050`. Fixed in the **test only** (`check_resources` is now patched like the other resource-touching functions); `mva_replay.py` is unchanged. |
| **F2** | O-2: self-check names every missing resource at once | **Falsified.** The first message did name four resources at once (Exomiser, analysis YAML, ClinVar, HPOA — one message, four paths). But once those were present a second run died with a bare `AssertionError` at the REF check, because the chr15 FASTA (the TRIP13 run needs chr5; the self-check needs chr15) is not among the resources it checks for — exactly the "second run to discover another" the prediction excluded. Documented in `README_TOOL.md`; the check itself is not changed. |
| **F3** | O-3: ≤ 5 manual steps, all in `README_TOOL.md § Requirements` | **Count confirmed — three steps to the first dry-run that exits 0 (`bare_clone.log` STEP 1, 2, 4; it still carries two "no FASTA" warnings), four to a warning-free one (STEP 5); STEP 3 is the diagnostic dry-run that revealed the missing backgrounds — documentation falsified.** Three of the four were not in *Requirements*: the analysis YAML is expected at `tools/analysis_mva.yml` while a checkout carries it at `analysis/analysis_mva.yml`; the FASTA directory `replay/raw/fasta/` was only mentioned under pre-flight checks; the background VCFs and how to prepare them were not in the repository at all. *Requirements* now lists all four steps with sources and commands. |
| **F4** | — | The reuse guard matches case names **by prefix**: `--name T_TRIP13_HG001` refused to run because the dry-run had written `T_TRIP13_HG001_dry4_*`. Documented behaviour, undocumented breadth. The three real runs were re-issued as `T2_*`; no result existed before the refusal, so nothing was re-run. Noted in `README_TOOL.md`. |
| — | O-4: ≤ 120 s per Exomiser call, ≤ 12 GB RSS, ≤ 10 min per background | **Confirmed.** Per-call wall-clock from the run timestamps: HG001 54 / 44 / 47 / 48 s; HG002 49 / 42 / 32 / 33 s; HG005 37 / 30 / 34 / 33 s. Maximum resident set 2.3–2.4 GiB (2,375,524–2,530,632 KiB). Per background, tool start to JSON: 3 min 20 s, 2 min 43 s, 2 min 21 s. Clone: 9.9 s, 12 MB. *Note on method:* `/usr/bin/time -v` wrapped the whole tool invocation (four Exomiser calls), not each call as the design says; per-call figures come from the tool's own timestamped progress lines, and the RSS is the peak over the four. |

**Departures from the pre-registered protocol, declared.** The stopping rule said three dry-runs; there
were five dry-run invocations (three diagnostic ones on HG001 while provisioning, then one per
background), four `--self-check` invocations while provisioning, and one real-run invocation refused by
the name guard (F4). None of them ran Exomiser: the 12 Exomiser runs are exactly the 12 pre-registered.
Two sentences of the pre-registration overstate: "that is what any real MVA3 referral looks like" rests
on one case and should read *a plausible* MVA3 referral; and the abstract says the variant was
"suggesting a diagnosis" of MVA3, not that MVA3 was confirmed, and gives no zygosity. Neither changes a
number.

**What this shows, and no more.** The frozen pipeline retrieves a second MVA gene, planted with two
public Likely_pathogenic alleles and queried with a phenotype transcribed from a published abstract,
at rank 1 in three healthy backgrounds — with the unrelated-phenotype control behaving exactly as it
did for BUB1B. A fresh clone reaches that result in four documented provisioning steps and about
three minutes of compute per background. It also showed that the repository's own claim about its
tests was false and that its requirements list was three items short, both now corrected. It does
not show diagnostic sensitivity, anything about the girl in PMID 42595739, or that the tool runs on a
machine that has never held the resources.
