# Rare Disease, Real Kid — MVA Hackathon 2026

Code, pre-registrations and reports for the [MVA Hackathon 2026](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026),
organised by Sage Bionetworks with the MVA Society, Hugging Face and BEACON. Team **ciberpty**.

> **No patient sequence data or genotype-scale derivative is present in this repository, and none ever
> will be.** The two diagnostic variants are named with their read depths, as findings, which the
> challenge rules permit; nothing else about this child's genome appears here. Under the hackathon data
> transfer agreement, the proband's VCF, phenotype document and every genotype-scale derivative stay
> on the analysis machine and are deleted within 30 days of the hackathon close. What is published
> here is code, configuration and derived findings, which the terms explicitly permit.
> A `.gitignore` blocks the relevant file types as a second line of defence.

## In one minute

**Track 1 — the variant.** Two orthogonal analyses converge on **BUB1B compound heterozygosity**
(MVA1, OMIM 257300, autosomal recessive). The retrieval is **variant-driven and phenotype-consistent**,
not phenotype-driven, and phase is **not** demonstrated.

| Variant | Consequence | gnomAD | ClinVar |
|---|---|---|---|
| `NM_001211.6:c.2210T>G` p.Leu737Ter (chr15:40209701 T>G) | stop_gained | 9.98×10⁻⁵ (exomes NFE) | 533901, Pathogenic / Likely pathogenic |
| `NM_001211.6:c.3006T>G` p.Asn1002Lys (chr15:40220612 T>G) | missense | 8.99×10⁻⁷ (exomes NFE) | not present (ClinVar holds `c.3006T>A`, a different nucleotide, VUS — does not transfer) |

**Track 2 — the drug question.** Metformin, the candidate the literature points to, fails on
pharmacokinetics for the mechanism proposed for it. Bortezomib survives that filter and then fails a
patient-specific safety filter: **we recommend no drug today.** The proposition we do defend is a
prepared, evidence-backed answer for the case where a new tumour appears, together with the experiment
that could show us we are wrong.

**What we actually contribute** is not a claim, it is seven pre-registrations that constrain the
claim — the DepMap test came back against our mechanism, the mosaicism control came back not conclusive,
and the two power analyses left our own assumptions unsupported. See [`VERIFY.md`](VERIFY.md).

## Results, with what each one does not show

| Analysis | Result | What it does **not** establish |
|---|---|---|
| [`depmap/`](depmap/RESULTADOS.md) | Aneuploidy scoring of 2,420 DepMap 24Q4 lines against PRISM drug response and CRISPR dependency. The aneuploidy–proteasome link is **significantly weaker in solid lineages** (interaction p = 0.026); ploidy adds nothing (p = 0.88). A pre-registered follow-up ([`RESULTADOS_SEGUIMIENTO.md`](depmap/RESULTADOS_SEGUIMIENTO.md)) gives the intervals, shows the attenuation is not driven by any single lineage, and finds this child's tumour type essentially absent from the drug screen. This child's tumour was solid. | That bortezomib does or does not work in MVA. It weakens our own argument, which is why it is here. |
| [`replay/`](replay/RESULTADOS.md) | MVA-Replay plants public alleles into public genomes. The two alleles score **0.5871** with the real phenotype in three unrelated backgrounds, to four decimals. Across **7 GIAB + 30 1000 Genomes** healthy genomes, the highest top-gene score is **0.5619** and **0.5207** respectively — **0 of 37 exceed 0.5871**. **Transferred to a second gene from a fresh clone** ([`TRANSFER_TRIP13.md`](replay/TRANSFER_TRIP13.md)): two public *TRIP13* alleles score 0.8332, rank 1 in 3 of 3 backgrounds; absent or 0 unspiked. | Diagnostic sensitivity. Every planted call is perfect and unambiguous; this measures retrieval given a clean heterozygous call, on a null biased in our favour. |
| [`hpo/`](hpo/RESULTADOS.md) | The unrelated-phenotype control, rebuilt twice. With a term set verified against **all** MVA diseases and genes, BUB1B still ranks 1 in the proband's genome at **0.3965** (Δ = 0.1906 from the real phenotype) — but in planted healthy backgrounds its rank is **1, 2 and 3**. | That the ranking is background-independent. It is not, and the version quoted in our submitted Track 1 write-up (0.4187) was contaminated. |
| [`mosaico/`](mosaico/RESULTADOS.md) | Bulk WGS cannot serve as an aneuploidy-burden endpoint. A calibrated simulation reaches a **2.07% detection limit at κ = 2**; more importantly, a perfectly balanced variegated mixture is **non-identifiable** — detection stays at the 0.1–0.2% false-positive rate even at 40% aneuploid cells. | Anything about this child. The patient-level result is **withdrawn**, and the pre-registered external control came back **not conclusive** ([`CONTROL_RESULTADO.md`](mosaico/CONTROL_RESULTADO.md)). We report no clinical negative. |
| [`potencia/RESULTADOS_REGLA_COMPLETA.md`](potencia/RESULTADOS_REGLA_COMPLETA.md) (**post-submission, 5 Oct**) | Operating characteristics of the **complete** §6 rule (two control donors, mixture-table threshold, ≤ 312 nM, micronucleus margin, toxicity stop), pre-registered after the final submission and run on a GPU: at the proposed design (f = 0.30, 4×, n = 12) the probability of *advance* is **0.44**, never 0.80 at any n ≤ 23; false advance under the null **0.07 at n = 23** because the two donor comparisons share the patient arm. The design is a pilot, not a decisive experiment. | Anything about the child's cells; the 4× selectivity and the variance components are scenario values. The submitted PDF predates this and is not edited. |
| [`potencia/`](potencia/RESULTADOS.md) | Power for the proposed fibroblast assay was **0.897** under a two-parameter fit with no biological variability (assumed 4× selectivity, 30% aneuploid culture, 10% well CV) — and **0.063** under the per-chromosome reading our report had implied. The pre-registered follow-up with the promised four-parameter fit and biological variability ([`RESULTADOS_4P.md`](potencia/RESULTADOS_4P.md)) gives **0.167 at n = 3** and needs **12 cultures per arm** at f = 0.30; the small-n branches are retired. A gating measurement is part of the protocol. | A validated power estimate. None of the three inputs is measured in these cells, the Hill fit uses two parameters where the design promised four, and the noise model has no biological-replicate term. [`RESULTADOS_2_DOSIS.md`](potencia/RESULTADOS_2_DOSIS.md) removes the empirical support for the 4× without refuting it. |
| [`fase/`](fase/RESULTADO.md) | Phase is not merely unresolved, it is **not resolvable from the evidence this challenge provides**: all three relevant variants are absent from the 1000 Genomes phased panel, and the challenge distributed a VCF and raw reads rather than alignments, so no read-backed phaser was run. | — |
| [`vus/`](vus/RESULTADOS.md) | The calibration set for a BUB1B missense predictor **does not exist**: of 1,497 submitted missense records, one is P/LP and 1,426 are VUS, while 82 of 94 truncating records are P/LP. | A prior probability that this child's missense is causal. That number describes the database, not the biology. |
| [`clinico/`](clinico/PARENTAL_SEGREGATION_ORDER.md) | A one-page laboratory request a clinician can adapt and sign: both loci, two Sanger amplicons with primers verified as single-copy across GRCh38, and an interpretation table written **before** the result covering all five outcomes — including the one that would refute our own Track 1 call. | That segregation classifies the missense. A *trans* result supports the compound-heterozygous model and contributes PM3-type evidence; it does not make a VUS pathogenic. |

## Layout

```
pipeline/    Gene panel with provenance, chromosome maps, bcftools triage
analysis/    Exomiser configuration: analysis specs, run scripts, HPO control scripts
report/      Track 2 report: PART1_decision_document.md (the ~20-page reading version), REPORT_track2_EN.md (full evidence),
             the PDF that binds both, candidates.tsv (machine-readable five-filter table), figures and their source
submission/  Track 1 CSV, Track 1 report (md + PDF), Track 2 methods, methods form
video/       3-minute pitch (mp4), narration script and slide source
depmap/      Pre-registered DepMap aneuploidy × drug/dependency analysis
replay/      MVA-Replay: the packaged tool, its pre-registration, benchmark results and tests
hpo/         Automated verification of control HPO terms against all MVA diseases and genes
mosaico/     Mosaicism detection limit, non-identifiability proof, external control
potencia/    Pre-registered power and dose-response analyses for the proposed assay
fase/        Phasing attempt and why phase is not resolvable here
vus/         ClinVar census and AlphaFold structural context for p.Asn1002Lys
clinico/     Parental segregation laboratory request and primer design
evidencia/   Adversarial review rounds, verbatim source abstracts, challenge rules snapshots
VERIFY.md    How to check that every pre-registration precedes its result
```

`evidencia/` is a historical archive, not a source of truth: several statements in it were refuted in
later rounds.

## Reproducing

Two things are reproducible without any access to the patient data, and one is not.

**MVA-Replay (no gated data needed).** The packaged tool plants public alleles into public genomic
backgrounds. It is a single file with no new dependencies.

```bash
python3 replay/test_output_reuse.py        # regression tests for output-collision handling; runs from a bare checkout (verified 7-Sep, after fixing the test that did not)
replay/mva_replay.py --self-check          # 22 assertions, with a positive and a negative control; names missing resources instead of failing
```

**`--self-check` needs the local analysis resources and will stop with their names if they are
absent** — it verifies real ClinVar records and real benchmark outputs, so a bare checkout cannot run
it. Those resources, and a real replay, need Exomiser 15.1.0 with its hg38 2602 data bundles (~55 GB,
public), a GRCh38 FASTA and a background VCF. See [`replay/README_TOOL.md`](replay/README_TOOL.md) for
the arguments and for the two failure modes it deliberately refuses to work around.

**We measured that path instead of describing it.** [`replay/TRANSFER_TRIP13.md`](replay/TRANSFER_TRIP13.md)
pre-registers, and then reports, a run of the tool on a second gene (*TRIP13*, two public ClinVar
alleles, a phenotype transcribed from a published case) **from a fresh clone of this repository**: four
provisioning steps, about three minutes per background, rank 1 in 3 of 3. It also found that the
regression tests did not run from a bare checkout and that the requirements list was three items
short; both are fixed, and the log that found them is committed.

**The whole Track 2 package, one command.** `bash analysis/make_track2.sh` regenerates the DepMap follow-up figure
and tables (when `depmap/raw/` is present), renders the five-filter worksheet from `report/candidates.tsv`, runs the
claim verifier and builds both PDFs; from a fresh checkout it takes about 8 s and names what is missing
(`evidencia/make_track2_fresh_checkout_2026-09-08.log`).

**The pre-registered public-data analyses.** `depmap/`, `vus/` and `potencia/` use only public data
and CPU. Each directory holds its scripts numbered in run order and the JSON/CSV every reported number
comes from. `depmap/` needs the DepMap 24Q4 and PRISM 24Q2 downloads (figshare 27993248 and 25917643,
~700 MB, gitignored).

**The primary case analysis is not reproducible without the gated dataset.** It requires the
hackathon VCF (access through the Space) plus `bcftools` and Java 17+; the 85 GB of raw reads are not
needed.

```bash
pipeline/triage.sh /path/to/proband.vcf.gz   # panel triage, fast sanity check
analysis/run_now.sh                          # genome-wide Exomiser run; edit the absolute paths first
```

## Declared limitations

- **Phase is not established, and is not resolvable from these data.** No parental samples; the two
  variants lie ~11 kb apart with nothing phaseable between them; all three relevant variants are absent
  from the 1000 Genomes panel. The compound-heterozygous call rests on allele rarity, the recessive
  inheritance of MVA1 and the phenotype match — not on a demonstrated *trans* configuration.
- **p.Asn1002Lys has no published functional assay.** Its hypomorphic character is a hypothesis, and no
  same-gene calibration set exists to score it against.
- **The rank of BUB1B under an unrelated phenotype is background-dependent** (1 / 2 / 3 across three
  healthy genomes). Only the score held, and only across those three backgrounds — one deterministic
  computation run three times, not evidence that the score is independent of the genome in general.
- **The bortezomib margin is computed on total plasma Cmax**, not free or intratumoral drug, and says
  nothing about duration of exposure.
- **No proteasome dependency has been demonstrated in this child's cells.** Everything downstream of
  that is conditional; the experiment in §6 of the Track 2 report measures differential drug response and
  constitutional-cell vulnerability in his own cells, not the mechanism itself.
- **REMM and CADD were not used.** Evaluated and dropped: 15.2 GB of download for scores that only
  affect non-coding variants, while the causal variant is coding and SpliceAI (included) covers the
  clinically relevant non-coding class.
- **No secondary findings are reported.** Two ACMG pathogenic/likely-pathogenic calls outside BUB1B
  were adjudicated as a probable mapping artefact (FANCD2) and carrier status (GNRHR).

**Nothing here is medical advice.** The reports are a methods write-up and a reasoned proposal for a
panel of judges, written by people with no access to the patient. The laboratory request in `clinico/`
is a draft for a clinical genetics service to adapt, review and decide on.

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with
the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium
for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and
their family who generously contributed their data and their story to advance research into this rare
disease. We acknowledge their trust in making this Hackathon possible.
