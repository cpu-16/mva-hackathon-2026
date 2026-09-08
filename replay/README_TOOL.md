# mva_replay.py — replay the MVA-Replay benchmark for your own gene

One file, one command, four Exomiser runs. Give it a candidate gene, two alleles, the patient's
HPO terms and a healthy background genome; it plants the alleles, runs the **frozen** Track 1
pipeline (Exomiser 15.1.0, data 2602_hg38, `tools/analysis_mva.yml`, unchanged) and reports what
the pipeline does with them under four conditions:

| condition | VCF | HPO | ClinVar whitelist | what it answers |
|---|---|---|---|---|
| `planted` | background + your two alleles | yours | on | the headline: planted score and rank |
| `noclinvar` | same | yours | **off** (`-Dexomiser.hg38.use-clinvar-whitelist=false`) | how much the ClinVar label is worth, in absolute score |
| `unrelated` | same | five clinically unrelated terms | on | how much the phenotype is worth, in absolute score |
| `background` | background only | yours | on | does the gene score at all without the plant? (the "given" of RESULTADOS.md §2) |

It is the tool form of `replay/01_run.py … 05_posthoc_clinvar.py`, which ran the 61 pre-registered
cases in `PREREGISTRO.md`; the functions are copied from there, not rewritten.

## Requirements

A code checkout is 12 MB and contains none of the resources below. **Measured on a fresh clone
(`TRANSFER_TRIP13.md`, 7-Sep-2026): four provisioning steps separate the clone from a working
`--dry-run`.** Each is listed with where it comes from; `mva_replay.py` stops and names whichever is
missing.

1. **Exomiser 15.1.0 and its data** at `tools/exomiser-cli-15.1.0/` — the CLI release plus the
   `2602_hg38` and `2602_phenotype` bundles (~55 GB, public, from the Exomiser download site), with
   `application.properties` pointing `exomiser.data-directory` at the extracted bundles. **And the
   frozen analysis at `tools/analysis_mva.yml`:** in a checkout it lives at `analysis/analysis_mva.yml`;
   copy it there (`mkdir -p tools && cp analysis/analysis_mva.yml tools/`).
2. **ClinVar and HPOA** at `pipeline/resources/`: `clinvar.vcf.gz` + `.tbi` (GRCh38, the release
   Track 1 used) and `genes_to_phenotype.txt` (HPOA). `hp.obo` is optional, for resolving term names.
3. **hg38 FASTA for the REF check** at `replay/raw/fasta/chrN.fa.bgz` (+ `.fai`, `.gzi`): UCSC
   `goldenPath/hg38/chromosomes/chrN.fa.gz`, recompressed with `bgzip` and indexed with
   `samtools faidx`. Without it the REF check degrades to a warning, not a failure. `--self-check`
   needs `chr15`.
4. **A background genome** — a single-sample, bgzip-compressed, tabix-indexed GRCh38 VCF. The seven
   GIAB genomes used here are the NIST v4.2.1 GRCh38 benchmark VCFs
   (`ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/.../NISTv4.2.1/GRCh38/HG00N_GRCh38_1_22_v4.2.1_benchmark.vcf.gz`),
   prepared as `bcftools annotate -x INFO,FORMAT/ADALL,FORMAT/GQ in.vcf.gz -Oz -o replay/bg/HG00N.vcf.gz && bcftools index -t replay/bg/HG00N.vcf.gz`.
   Any other single-sample VCF works; the script declares `GT/DP/AD/GQ` in the header if they are missing (Amendment 2).

On the PATH: `java` (17+), `bcftools`, `samtools`, `bgzip`, `tabix`, Python 3 (standard library only).
About 10 GB RAM per run. No GPU. No patient data is read or written.

## Usage

```bash
cd replay
./mva_replay.py --self-check          # 21 assertions when the local benchmark artefacts (replay/out, replay/cases, chr15 FASTA) are present; 12 without them

./mva_replay.py --gene BUB1B \
    --allele 533901 \
    --allele chr15:40220612:T:A \
    --hpo HP:0002859 HP:0000121 HP:0004322 HP:0001508 HP:0003202 HP:0001622 HP:0001518 HP:0200067 \
    --background bg/HG002.vcf.gz
```

Optional flags include `--hpo-unrelated`, `--phase trans|cis|unph`, `--sex MALE|FEMALE`,
`--out DIR`, `--name NAME` and `--dry-run`. Alleles may be ClinVar variation IDs,
`chr:pos:ref:alt`, or supported genomic HGVS strings.

**Use a fresh case name or output directory for every invocation.** Existing files for the same
case cause an error before analysis starts — and the match is by prefix, so `--name T_HG001` also
collides with an earlier `T_HG001_dry` in the same `--out` (finding F4 of `TRANSFER_TRIP13.md`). A gene/background name alone cannot establish that
alleles, phenotypes, phase and resources match a previous run. Automatic reuse is therefore disabled.
This also applies after `--dry-run`, which writes sample YAML files: choose a different `--name`
for the actual run. No old result is deleted or overwritten by this check.

`--dry-run` resolves the alleles, runs every pre-flight check and prints the spike records and the
four exact Exomiser command lines as JSON, without running Java. A full run on a GIAB background
takes about 4 minutes (≈ 55 s per Exomiser call); outputs land in `--out` (default `replay/out_tool/`)
as `NAME_{planted,noclinvar,unrelated,background}.{genes,variants}.tsv` plus `NAME.json`.

**Background genome.** A single-sample, bgzip-compressed, tabix-indexed GRCh38 VCF. The seven GIAB
genomes in `replay/bg/` and thirty 1000 Genomes individuals in `replay/bg1k/` are ready to use
(`_prep_bg.sh` shows how they were made: `bcftools annotate -x INFO`). Any other VCF works if it has
one sample; the script declares `GT/DP/AD/GQ` in the header if they are missing (Amendment 2).

## What the pre-flight checks do (and what happens if they fire)

- **REF vs hg38** (`samtools faidx`): a mismatch aborts. Only chr3/5/11/15 FASTAs are in
  `replay/raw/fasta/`; pass `--fasta` for another chromosome or you get a warning, not a check.
- **Overlap with the background** (`bcftools view -r`, ±60 bp): a warning. The planted record still
  goes in, but the reported score is then a property of both alleles together.
- **Unrelated HPO terms annotated to the gene**: each `--hpo-unrelated` term is looked up in HPOA's
  `genes_to_phenotype.txt` against *every* disease of the gene (OMIM and Orphanet). A hit stops
  the run unless `--allow-contaminated-control` is explicitly supplied. On BUB1B this fires for
  `HP:0000365` (hearing impairment, ORPHA:1052). The current default replaces that term with
  `HP:0000988`; the historical pre-registered set is retained for the positive self-check.
- **Ingestion** (pre-registration assertion 1): after the run, both planted alleles must appear in
  Exomiser's variants table annotated to `--gene`. If not, `technical_failure: true` is set and the
  score is reported anyway — never silently dropped, never called a miss.

## Reading the output

`NAME.json` holds, per condition: `score` (best MOI row's combined score), `gene_rank` (among unique
genes — not gene×MOI rows, see RESULTADOS.md §0.2(c)), `row_rank`, `moi`, `pheno_score`,
`n_genes`, `n_genes_score_gt0`, `top_gene`/`top_score`, `runner_up`, `acmg`, `acmg_evidence`,
`whitelist_flags`, `functional_class`, `variant_scores`, `alleles_ingested`. Two summary numbers:

- `delta_clinvar_abs` = planted − noclinvar
- `delta_phenotype_abs` = planted − unrelated

Both are **absolute differences**. Do not divide them by the score: Exomiser combines phenotype and
variant evidence non-linearly, so "X % of the score" is undefined (this project withdrew two such
figures; RESULTADOS.md §0.2 and §4b).

## Ceilings, marked `# ponytail:` in the code

- One gene, exactly two alleles per call. A panel is a shell loop.
- Allele input is genomic: `chr:pos:ref:alt`, genomic HGVS (`NC_…:g.` SNV/MNV) or a ClinVar id.
  Transcript (`c.`) or protein (`p.`) HGVS must be resolved to one of those first.
- `noclinvar` switches off Exomiser's ClinVar **whitelist** only (the log then says
  `Loaded 0 whitelist variants`; `WHITELIST_VARIANT` goes to 0 and the nonsense's variant score from
  1.0000 to 0.9986). ClinVar still feeds the ACMG evidence (`PP5_Strong` stays), so on the BUB1B
  reference case this delta is **0.0021**, smaller than the **0.0128** measured when the nonsense was
  replaced by an unclassified one of the same consequence (`05_posthoc_clinvar.py`, X2/X3,
  RESULTADOS.md §3.2). Read `delta_clinvar_abs` as "the whitelist", not "ClinVar"; for the full
  counterfactual plant an unclassified allele of the same consequence.
- The GIAB high-confidence-BED criterion of the pool rule is not applied: you choose the alleles, so
  the ingestion check is the gate.
- Runs are sequential. Four calls, ≈ 4 minutes on a GIAB background.
