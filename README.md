# Rare Disease, Real Kid — MVA Hackathon 2026

Submission code and reports for the [MVA Hackathon 2026](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026),
organised by Sage Bionetworks with the MVA Society, Hugging Face and BEACON.

> **No patient data is present in this repository, and none ever will be.** Under the hackathon data
> transfer agreement, the proband's VCF, phenotype document and every genotype-scale derivative stay
> on the analysis machine and are deleted within 30 days of the hackathon close. What is published
> here is code, configuration, and named findings — which the terms explicitly permit to survive.
> A `.gitignore` blocks the relevant file types as a second line of defence.

## Result

**BUB1B compound heterozygosity** → mosaic variegated aneuploidy type 1 (MVA1, OMIM 257300),
autosomal recessive.

| Variant | Consequence | gnomAD | ClinVar |
|---|---|---|---|
| `NM_001211.6:c.2210T>G` p.Leu737Ter (chr15:40209701 T>G) | stop_gained | 3×10⁻⁵ | Pathogenic / Likely pathogenic |
| `NM_001211.6:c.3006T>G` p.Asn1002Lys (chr15:40220612 T>G) | missense | absent | VUS |

## Approach: two orthogonal analyses, required to converge

The point of running two is that one of them cheats and the other does not.

**A — Phenotype-driven, genome-wide, hypothesis-free (primary).** Exomiser 15.1.0 on the complete
VCF (4,740,790 PASS variants) driven only by the eight HPO terms from the clinical document. No gene
panel, no candidate list, and the disease name never appears in any configuration file. **BUB1B
ranked 1st and 2nd of 3,139 genes**, at ~4× the score of the third gene, and under the recessive
model Exomiser flagged both variants as contributing — reconstructing the compound heterozygous pair
on its own. Runtime: 53 seconds.

**B — Targeted panel, confirmation.** 11 MVA genes and phenocopies, coordinates fetched from the
Ensembl REST API at run time (never hard-coded — see `pipeline/mva_panel.provenance.tsv`), annotated
via Ensembl VEP REST, filtered for HIGH/MODERATE impact at gnomAD AF < 1%. Of 1,532 variants, three
survived; **BUB1B was the only gene carrying two rare damaging alleles**.

**Robustness control.** Repeating analysis A with the variant-effect filter removed — 219,399
variants across 13,338 genes, 22× and 4× the primary run — left the ranking and the scores
*identical*. The answer does not depend on that filter.

## The negative result that matters

MVA is defined by mosaic aneuploidy, so we tested whether that signature is visible in the bulk WGS.
Four approaches — per-chromosome B-allele frequency, the same at fixed read depth, a 5 Mb spatial
profile, and chromosomal dosage — found no robust evidence. Every candidate signal traced to
coverage, segmental duplications (22q11, centromeres) or GC content.

Rather than assert a negative, we computed the **detection limit**: simulation of mean |BAF − 0.5| at
DP 44 against the systematic between-chromosome noise floor gives **~12–15% of cells for a clonal
trisomy**. Variegation distributes the burden so each chromosome sits 6–14× below that — and coverage
is not the constraint (Poisson error over a whole chromosome at 44× is ~0.03%; library bias sets the
floor). Bulk averaging erases variegation by construction, at any depth.

**We do not claim the child lacks mosaic aneuploidy** — he has it by diagnostic definition. We claim
this assay cannot resolve it. The correct endpoints already exist and are standard (metaphase
karyotype with PCS scoring, micronucleus assay per OECD TG 487, low-coverage scDNA-seq since
[Knouse 2014](https://pubmed.ncbi.nlm.nih.gov/25197050/)); our contribution is quantifying how far
the bulk shortcut falls short. Details in [`report/MOSAICISMO.md`](report/MOSAICISMO.md).

## Layout

```
pipeline/    Gene panel with provenance, ClinVar/HPO resource fetch, bcftools triage
analysis/    Exomiser configuration: phenopacket, analysis specs, run scripts
report/      Findings, mosaicism analysis, Track 2 report
submission/  Track 1 CSV and methods description
```

## Reproducing

Requires the gated hackathon dataset (access via the Space), plus `bcftools` and Java 17+.
Only the VCF and the phenotype document are needed — **not** the 85 GB of raw reads.

```bash
# 1. Panel triage (fast sanity check)
pipeline/triage.sh /path/to/proband.vcf.gz

# 2. Genome-wide, phenotype-driven (the primary analysis)
#    Edit the absolute paths in analysis/run_now.sh for your machine first.
analysis/run_now.sh
```

Exomiser needs its 2602 hg38 and phenotype data bundles (~55 GB, public) — see
[the Exomiser docs](https://exomiser.readthedocs.io/).

## Declared limitations

- **Phase is not established.** No parental samples, and the two variants lie ~11 kb apart — beyond
  read-backed phasing for short reads. The compound-heterozygous call rests on allele rarity and the
  known recessive inheritance of MVA1, not on demonstrated *trans* configuration.
- **p.Asn1002Lys has no published functional assay.** Its hypomorphic character is a hypothesis.
- **REMM and CADD were not used.** Evaluated and dropped: 15.2 GB of download for scores that only
  affect non-coding variants, while the causal variant is coding and SpliceAI (included) covers the
  clinically relevant non-coding class.
- **No secondary findings are reported.** Two ACMG pathogenic/likely-pathogenic calls outside BUB1B
  were adjudicated as a probable mapping artefact (FANCD2) and carrier status (GNRHR). Reasoning in
  [`report/HALLAZGOS.md`](report/HALLAZGOS.md).

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with
the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium
for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and
their family who generously contributed their data and their story to advance research into this rare
disease. We acknowledge their trust in making this Hackathon possible.
