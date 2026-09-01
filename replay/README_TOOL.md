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

Already present in this repository: `tools/exomiser-cli-15.1.0` with the 2602 hg38 + phenotype data,
`pipeline/resources/clinvar.vcf.gz` (GRCh38) and `genes_to_phenotype.txt`. On the PATH: `java`,
`bcftools`, `samtools`, `bgzip`, `tabix`, Python 3 (standard library only). About 10 GB RAM per run.
No GPU. No patient data is read or written.

## Usage

```bash
cd replay
./mva_replay.py --self-check          # 20 asserts against the artefacts of the 61-run benchmark, ~3 s

./mva_replay.py --gene BUB1B \
    --allele 533901 \                        # ClinVar variation id …
    --allele chr15:40220612:T:A \            # … or chr:pos:ref:alt, or NC_000015.10:g.40220612T>A
    --hpo HP:0002859 HP:0000121 HP:0004322 HP:0001508 HP:0003202 HP:0001622 HP:0001518 HP:0200067 \
    --background bg/HG002.vcf.gz \
    [--hpo-unrelated HP:... ] [--phase trans|cis|unph] [--sex MALE|FEMALE] [--out DIR] [--dry-run]
```

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
  `genes_to_phenotype.txt` against *every* disease of the gene (OMIM and Orphanet). A hit is a
  warning telling you to pick another term. On BUB1B this fires for `HP:0000365` (hearing
  impairment, ORPHA:1052) — the pre-registration checked only OMIM:257300, so the shipped default
  control set is slightly contaminated for BUB1B and that warning is expected.
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
