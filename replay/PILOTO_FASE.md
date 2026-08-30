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
3. **The cost of being on the wrong haplotype is 0.0034 in absolute score** (trans 0.9339, cis 0.9305).
   Being unphased costs 0.0014. We report these as absolute differences: the combined score is a
   non-linear function of its inputs, so a percentage share of it is not defined. Neither changes the call or the rank.

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
