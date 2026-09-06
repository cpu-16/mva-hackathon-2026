# Rare Disease, Real Kid — MVA Hackathon 2026

Code, pre-registrations and reports for the [MVA Hackathon 2026](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026),
organised by Sage Bionetworks with the MVA Society, Hugging Face and BEACON. Team **ciberpty**.

> **No patient data is present in this repository, and none ever will be.** Under the hackathon data
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

**What we actually contribute** is not a claim, it is five pre-registered analyses that constrain the
claim — including four that came back against us. See [`VERIFY.md`](VERIFY.md).

## Results, with what each one does not show

| Analysis | Result | What it does **not** establish |
|---|---|---|
| [`depmap/`](depmap/RESULTADOS.md) | Aneuploidy scoring of 2,420 DepMap 24Q4 lines against PRISM drug response and CRISPR dependency. The aneuploidy–proteasome link is **significantly weaker in solid lineages** (interaction p = 0.026); ploidy excluded as a confounder (p = 0.88). This child's tumour was solid. | That bortezomib does or does not work in MVA. It weakens our own argument, which is why it is here. |
| [`replay/`](replay/RESULTADOS.md) | MVA-Replay plants public alleles into public genomes. The two alleles score **0.5871** with the real phenotype in three unrelated backgrounds, to four decimals. Across **7 GIAB + 30 1000 Genomes** healthy genomes, the highest top-gene score is **0.5619** and **0.5207** respectively — **0 of 37 exceed 0.5871**. | Diagnostic sensitivity. Every planted call is perfect and unambiguous; this measures retrieval given a clean heterozygous call, on a null biased in our favour. |
| [`hpo/`](hpo/RESULTADOS.md) | The unrelated-phenotype control, rebuilt twice. With a term set verified against **all** MVA diseases and genes, BUB1B still ranks 1 in the proband's genome at **0.3965** (Δ = 0.1906 from the real phenotype) — but in planted healthy backgrounds its rank is **1, 2 and 3**. | That the ranking is background-independent. It is not, and the version quoted in our submitted Track 1 write-up (0.4187) was contaminated. |
| [`mosaico/`](mosaico/RESULTADOS.md) | Bulk WGS cannot serve as an aneuploidy-burden endpoint. A calibrated simulation reaches a **2.07% detection limit at κ = 2**; more importantly, a perfectly balanced variegated mixture is **non-identifiable** — detection stays at the 0.1–0.2% false-positive rate even at 40% aneuploid cells. | Anything about this child. The patient-level result is **withdrawn**, and the pre-registered external control came back **not conclusive** ([`CONTROL_RESULTADO.md`](mosaico/CONTROL_RESULTADO.md)). We report no clinical negative. |
| [`potencia/`](potencia/RESULTADOS.md) | Power for the proposed fibroblast assay is **0.897** under an assumed 4× selectivity, a 30% aneuploid culture and 10% well CV — and **0.063** under the per-chromosome reading our report had implied. A gating measurement is now part of the protocol. | A validated power estimate. None of the three inputs is measured in these cells, the Hill fit uses two parameters where the design promised four, and the noise model has no biological-replicate term. [`RESULTADOS_2_DOSIS.md`](potencia/RESULTADOS_2_DOSIS.md) removes the empirical support for the 4× without refuting it. |
| [`fase/`](fase/RESULTADO.md) | Phase is not merely unresolved, it is **not computable** from this dataset: all three relevant variants are absent from the 1000 Genomes phased panel, and no read-backed phaser can run on a VCF. | — |
| [`vus/`](vus/RESULTADOS.md) | The calibration set for a BUB1B missense predictor **does not exist**: of 1,497 submitted missense records, one is P/LP and 1,426 are VUS, while 82 of 94 truncating records are P/LP. | A prior probability that this child's missense is causal. That number describes the database, not the biology. |
| [`clinico/`](clinico/PARENTAL_SEGREGATION_ORDER.md) | A one-page laboratory request a clinician can adapt and sign: both loci, two Sanger amplicons with primers verified as single-copy across GRCh38, and an interpretation table written **before** the result covering all five outcomes — including the one that would refute our own Track 1 call. | That segregation classifies the missense. A *trans* result supports the compound-heterozygous model and contributes PM3-type evidence; it does not make a VUS pathogenic. |

## Layout

```
pipeline/    Gene panel with provenance, chromosome maps, bcftools triage
analysis/    Exomiser configuration: analysis specs, run scripts, HPO control scripts
report/      Track 2 report (md + PDF), figures and figure source, working documents
submission/  Track 1 CSV, Track 1 report (md + PDF), Track 2 methods, methods form
video/       3-minute pitch (mp4), narration script and slide source
depmap/      Pre-registered DepMap aneuploidy × drug/dependency analysis
replay/      MVA-Replay: the packaged tool, its pre-registration, benchmark results and tests
hpo/         Automated verification of control HPO terms against all MVA diseases and genes
mosaico/     Mosaicism detection limit, non-identifiability proof, external control
potencia/    Pre-registered power and dose-response analyses for the proposed assay
fase/        Phasing attempt and why it is not computable here
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
replay/mva_replay.py --self-check          # 21 assertions, includes a positive and a negative control
python3 replay/test_output_reuse.py        # regression tests for output-collision handling
```

Running a real replay additionally needs Exomiser 15.1.0 with its hg38 2602 data bundles (~55 GB,
public), a GRCh38 FASTA and a background VCF. See [`replay/README_TOOL.md`](replay/README_TOOL.md) for
the arguments and for the two failure modes it deliberately refuses to work around.

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

- **Phase is not established, and is not computable from these data.** No parental samples; the two
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
  that is conditional, and the experiment in §6 of the Track 2 report exists to test it.
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
