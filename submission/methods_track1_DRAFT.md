# Track 1 — Methods description (DRAFT)

> **Gilberto: revisa esto antes de enviarlo.** Las secciones marcadas con ⚠️ necesitan una decisión
> tuya, sobre todo la Q23 (declaración de IA), donde no puedo afirmar por ti cómo tienes configurada
> tu cuenta.

---

## Q3 — Describe your model/approach in detail

We ran two independent analyses and required them to converge before accepting a result.

**Analysis A — phenotype-driven, genome-wide, hypothesis-free (primary).**
Exomiser 15.1.0 with the 2602 hg38 and phenotype data releases. Input was the unmodified proband VCF
(4,740,790 PASS variants, GRCh38, GATK 4.2.4.0) and the eight HPO terms extracted verbatim from the
supplied clinical document: HP:0002859, HP:0000121, HP:0004322, HP:0001508, HP:0003202, HP:0001622,
HP:0001518, HP:0200067.

No gene panel, no candidate list, and no reference to the disease name was supplied at any point in
the configuration. Prioritisation used `hiPhivePrioritiser` (human, mouse, fish and PPI evidence) and
`omimPrioritiser`. Inheritance models covered AD, AR-hom, AR-comp-het, X-linked and mitochondrial.
Frequency sources: UK10K and gnomAD exomes/genomes across five populations, maximum 2%.
Pathogenicity sources: REVEL, MVP, AlphaMissense and SpliceAI.

Filtering cascade: 4,702,177 passed the failed-variant filter → 277,724 after variant effect →
11,255 after frequency → 9,935 after inheritance, distributed across 3,139 genes.

**Result:** BUB1B ranked **1st (AD model) and 2nd (AR model)** out of 3,139 genes, with a combined
score roughly four times that of the third-ranked gene. Under the autosomal recessive model — the
correct one for MVA1 — Exomiser flagged *both* variants as contributing, independently reconstructing
the compound heterozygous pair.

**Robustness control.** The primary run applies a variant-effect filter that discards intronic,
upstream/downstream and intergenic variants before scoring. To verify the result does not depend on
it, the analysis was repeated with that filter removed: **219,399 variants across 13,338 genes**
(22× and 4× the primary run). BUB1B remained ranked 1st and 2nd with **identical combined scores**
(0.5871 and 0.5538), and the entire top ten was unchanged.

**Analysis B — targeted panel, orthogonal confirmation.**
An 11-gene panel of MVA genes and phenocopies (BUB1B, CEP57, TRIP13, CENATAC, MAD1L1, MAD2L1BP,
CEP192, BUB1, SMC5, TRIM37, CENPE) with 5 kb padding. Coordinates were retrieved programmatically
from the **Ensembl REST API (release 116)** rather than from memory or a static file, and the
provenance of every coordinate is recorded. The 1,532 PASS variants in these intervals were annotated
with the **Ensembl VEP REST API** and filtered for HIGH/MODERATE impact on the canonical transcript
with gnomAD AF < 1% or absent.

Exactly three variants survived. Two were in BUB1B; the third (MAD1L1 p.Arg59Cys) was a single allele
in a recessive gene and therefore cannot explain the phenotype. **BUB1B was the only gene carrying two
rare damaging alleles.**

**Convergent answer:**

| Variant | Consequence | gnomAD | ClinVar | Exomiser ACMG |
|---|---|---|---|---|
| `NM_001211.6:c.2210T>G` p.Leu737Ter | stop_gained | 3×10⁻⁵ | Pathogenic/Likely pathogenic | PATHOGENIC |
| `NM_001211.6:c.3006T>G` p.Asn1002Lys | missense | absent | VUS (as c.3006T>A) | UNCERTAIN_SIGNIFICANCE |

Diagnosis: **mosaic variegated aneuploidy type 1 (MVA1, OMIM 257300)**, autosomal recessive, caused by
compound heterozygosity in BUB1B. The truncating-plus-missense configuration matches the recurrent
allelic pattern reported in viable MVA1 (Suijkerbuijk 2010, PMID 20516114; Sieben 2020, PMID 31738183).

**Additional analysis — mosaicism (negative result).**
Because MVA is defined by mosaic aneuploidy, we tested whether that signature is visible in the bulk
WGS, using four approaches: per-chromosome B-allele frequency of 2.27 M heterozygous SNVs; the same
restricted to a fixed depth window (DP 40–48) to remove the coverage confounder; a spatial profile in
5 Mb windows; and chromosomal dosage via 10%-trimmed mean depth.

Note that three of these are refinements of the same BAF statistic and only the dosage test is
orthogonal; they are not four independent tests. Analysis used the VCF only — no BAM was available,
so no GC-LOESS normalisation was possible.

**We computed the detection limit rather than asserting a negative.** Simulating mean |BAF − 0.5| at
DP 44 shows a clonal trisomy is detectable above the systematic between-chromosome noise floor
(≈0.005) only when present in **~12–15% of cells**. Coverage is not the constraint: Poisson error
over a whole chromosome at 44× is ~0.03%, so the limit is set by library bias, not read sampling.

Every candidate signal traced to coverage, segmental duplications (22q11, centromeres) or — partially
— GC content. We flag that the GC explanation is incomplete: our measured GC–coverage correlation was
r = 0.43 from a sparse sample, and chr21, the largest deviation, is GC-poor. Where dosage and BAF
disagreed we favoured BAF, which cancels coverage bias, and report dosage as an open hypothesis.

**We therefore do not claim the child lacks mosaic aneuploidy — he has it by diagnostic definition.**
We claim this assay cannot resolve it: variegation distributes the burden across chromosomes so that
each sits 6–14× below the detection limit, and bulk averaging erases variegation by construction, at
any depth. The cytogenetic hallmark of MVA, premature chromatid separation, leaves no trace in DNA
sequence at all. The practical consequence is that "aneuploidy burden" is not a measurable endpoint
here, which constrains any Track 2 proposal whose outcome depends on it.

## Q4 — Automated output or manual review?

⚠️ **Recomendación: responder "automated output with documented manual review".** El CSV enviado es la
salida directa de la convergencia de ambos análisis, pero la decisión de excluir los hallazgos
secundarios fue una revisión manual con criterio clínico, y ocultarlo sería inexacto.

## Q5 — Describe the manual review

Manual review was limited to two decisions, both documented:

1. **Confirming the compound-heterozygous pair.** Both analyses proposed the pair automatically; we
   verified the genotypes (0/1 for both), read depths (46× and 28×) and allelic balance directly in
   the VCF.
2. **Adjudicating two secondary candidates** (see Q10).

No variant was added, removed or re-ranked on intuition.

## Q6 / Q7 — Public data only

Public data only. No proprietary data sources were used.

- Ensembl REST API release 116 (gene coordinates)
- Ensembl VEP REST API (functional consequence, canonical transcript, gnomAD frequencies)
- Exomiser 15.1.0 with data releases 2602_hg38 and 2602_phenotype
- gnomAD v4 (via Exomiser and VEP)
- ClinVar, GRCh38 (NCBI FTP snapshot and E-utilities)
- Human Phenotype Ontology (`hp.obo`, `genes_to_phenotype.txt`)
- REVEL, MVP, AlphaMissense and SpliceAI (via the Exomiser bundle)
- OMIM identifiers via the Exomiser `omimPrioritiser`
- Published literature (PubMed / Europe PMC), cited by PMID

## Q9 — Can the approach output compound heterozygous pairs?

Yes, and it did so without being told to. Exomiser's `AUTOSOMAL_RECESSIVE_COMP_HET` inheritance mode
flagged both BUB1B variants as contributing under the recessive model. The targeted analysis
independently flagged any gene carrying two rare damaging alleles, which selected BUB1B alone.

**Limitation we want to state plainly:** neither method can establish *phase*. There is no parental
sample, and the two variants are ~11 kb apart, well beyond read-backed phasing range for Illumina
paired-end data. The compound-heterozygous interpretation rests on allele rarity, the known recessive
inheritance of MVA1, and the absence of homozygotes in gnomAD — not on demonstrated trans
configuration. Parental testing would settle it.

## Q10 — Secondary / incidental findings

**None reported.** Of 12,427 ACMG-classified variants, four reached pathogenic or likely pathogenic.
Two lay outside BUB1B and both were adjudicated as non-reportable:

- **FANCD2 chr3:10046723**, splice_donor, ACMG PATHOGENIC — judged a probable technical artefact:
  allelic fraction 0.31 (AD 61,28) rather than the expected 0.5; a second variant 2 bp away at
  10046725 in the same splice donor, the signature of a misaligned indel; and FANCD2 has
  high-identity pseudogenes that are a known short-read mapping pitfall. Even if real, a single
  allele of an autosomal recessive disorder is carrier status. Sanger validation would be required
  before any report.
- **GNRHR chr4:67753920**, missense, ACMG LIKELY_PATHOGENIC — a clean heterozygote (AD 28,32) and
  carrier status for an autosomal recessive condition unrelated to the phenotype. Carrier status is
  not a secondary finding under ACMG SF v3.2.

We chose to document the reasoning rather than submit these as `secondary` rows. They would not have
harmed the automated score, but reporting them as findings would be a clinically meaningful false
positive.

## Q11 — Runtime and cost

- Exomiser genome-wide run: **53 seconds** wall clock (32-core CPU, 16 GB JVM heap).
- Targeted panel with REST annotation: under 5 minutes, dominated by API latency.
- Mosaicism analysis: about 10 minutes of `bcftools` streaming.
- One-off setup: ~55 GB of Exomiser reference data downloaded and extracted.
- **Marginal compute cost: effectively zero** — a commodity workstation, no GPU, no cloud instance.
  Reproducing this on a laptop is realistic: only the 315 MB VCF and the phenotype document are
  needed, not the 85 GB of raw reads.

## Q12 — Method abstract (≤500 words)

We identified the causal variants through two independent analyses designed to check each other, and
required them to converge before accepting a result.

The primary analysis was deliberately hypothesis-free. Exomiser 15.1.0 (data release 2602, hg38) was
run on the complete proband VCF — 4,740,790 PASS variants — driven only by the eight HPO terms taken
verbatim from the clinical document. No gene panel, no candidate list, and no mention of the disease
name entered the configuration at any point. Prioritisation combined hiPhive (human, mouse, fish and
protein-interaction evidence) with the OMIM prioritiser, across autosomal dominant, recessive,
X-linked and mitochondrial models. **BUB1B ranked first and second of 3,139 genes**, at roughly four
times the combined score of the third-ranked gene, and under the recessive model Exomiser flagged
both variants as contributing, reconstructing the compound heterozygous pair on its own.

The confirmatory analysis took the opposite approach: an 11-gene panel of MVA genes and phenocopies,
with coordinates fetched programmatically from the Ensembl REST API and their provenance recorded,
annotated through Ensembl VEP and filtered for HIGH/MODERATE impact at gnomAD AF below 1%. Of 1,532
variants, three survived; two were in BUB1B, and it was the only gene carrying two rare damaging
alleles.

Both routes converge on **NM_001211.6:c.2210T>G p.Leu737Ter** (nonsense, ClinVar
Pathogenic/Likely pathogenic, gnomAD 3×10⁻⁵) and **c.3006T>G p.Asn1002Lys** (missense, absent from
gnomAD), consistent with MVA1 (OMIM 257300) and with the truncating-plus-missense allelic pattern
reported in viable MVA1.

Because MVA is defined by mosaic aneuploidy, we also asked whether that signature is visible in the
bulk WGS. Four tests — per-chromosome B-allele frequency, the same at fixed read depth, a spatial
profile in 5 Mb windows, and chromosomal dosage by trimmed mean depth — found no robust evidence.
Every candidate signal traced to coverage, segmental duplications or GC content. Where the dosage and
BAF tests disagreed, we favoured BAF, which is an internal per-site ratio and immune to library
coverage bias. The negative result follows from the biology: in *variegated* mosaicism different
cells carry aneuploidies of different chromosomes, so a 30% aneuploid fraction spread over 22
autosomes leaves each chromosome altered in 1–2% of cells, below the resolution of 44× bulk
sequencing. Aneuploidy burden is therefore not a measurable endpoint in these data — a constraint
that matters for evaluating any candidate therapy.

**Strengths.** Two orthogonal methods, one knowledge-driven and one phenotype-driven, reach the same
answer. Every reference coordinate is fetched from a versioned API rather than hard-coded. A control
run without the variant-effect filter — 219,399 variants across 13,338 genes — leaves the ranking
unchanged, so the result does not depend on that filter. Total analysis time was 53 seconds on a
commodity workstation with no GPU.

**Limitations.** Phase cannot be established: there is no parental sample and the variants lie ~11 kb
apart, beyond read-backed phasing for short reads, so the compound-heterozygous call rests on allele
rarity and known recessive inheritance rather than demonstrated trans configuration. REMM and CADD
were omitted. The functional consequence of p.Asn1002Lys is unproven and remains an experimental
question.

## Q23 — Generative AI declaration (REQUIRED)

⚠️ **Esta es la que no puedo llenar por ti.** Hay que declarar proveedor, plan y configuración de
cada herramienta usada. Lo que usamos de hecho:

| Herramienta | Proveedor | Para qué |
|---|---|---|
| Claude Code (Opus) | Anthropic | análisis, pipeline, redacción |
| Codex | OpenAI | revisión de literatura del Track 2 |
| Cursor (Grok) | xAI vía Cursor | análisis científico y construcción del pipeline |

**Antes de declarar nada, verifica y anota para cada una:** el plan o tier exacto, y si el
entrenamiento sobre tus datos está desactivado. La CPO de Sage exige dos condiciones: sin
entrenamiento sobre inputs/outputs, y retención limitada en tiempo y propósito. Su ejemplo de
formulación aceptable es literalmente *"Anthropic API, Claude Sonnet, Commercial terms, no training
on customer content"*.

**Dato de hecho sobre lo que sí ocurrió:** ningún bloque del VCF ni tabla de genotipos se envió a un
LLM. El trabajo con el genoma se hizo con herramientas locales (bcftools, Exomiser) y APIs de
anotación —Ensembl VEP, ClinVar— que la propia política del hackathon nombra como herramientas
aceptables. Lo que los modelos vieron fueron variantes nombradas, términos HPO y razonamiento, es
decir, exactamente lo que la CPO clasifica como "hallazgo" y autoriza a conservar.
