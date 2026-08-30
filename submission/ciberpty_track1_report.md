# Track 1 — Methods description

**Team: ciberpty** · MVA Hackathon 2026 · Proband PROBAND01
Repository: https://github.com/cpu-16/mva-hackathon-2026

---

## Q3 — Describe your model/approach in detail

We ran two independent analyses and required them to converge before accepting a result.

### Analysis A — genome-wide, phenotype-informed, hypothesis-free (primary)

Exomiser 15.1.0 with the 2602 hg38 and 2602 phenotype data releases. Input was the unmodified proband
VCF — **5,012,204 records, of which 4,740,790 carry the PASS filter** (GRCh38, GATK 4.2.4.0) — together
with the eight HPO terms extracted verbatim from the supplied clinical document:

| HPO | Term |
|---|---|
| HP:0002859 | Rhabdomyosarcoma |
| HP:0000121 | Nephrocalcinosis |
| HP:0004322 | Short stature |
| HP:0001508 | Failure to thrive |
| HP:0003202 | Skeletal muscle atrophy |
| HP:0001622 | Premature birth |
| HP:0001518 | Small for gestational age |
| HP:0200067 | Recurrent spontaneous abortion |

We note that the last term describes the parents' obstetric history rather than a finding in the
child. We kept it because the clinical document states it and because it is informative for the mode
of inheritance, but we flag it explicitly rather than let it pass as a proband phenotype.

No gene panel, no candidate list and no reference to a disease name entered the configuration at any
point. Prioritisation used `hiPhivePrioritiser` (human, mouse, fish and protein-interaction evidence)
and `omimPrioritiser`. Inheritance models covered autosomal dominant, autosomal recessive
(homozygous and compound heterozygous), X-linked and mitochondrial. Frequency sources were UK10K and
gnomAD exomes/genomes across five populations at a 2% maximum; pathogenicity sources were REVEL, MVP,
AlphaMissense and SpliceAI.

Filtering cascade: Exomiser loaded 4,962,047 of those records; 4,702,177 passed the failed-variant
filter → 277,724 after the variant-effect filter → 11,255 after frequency → 9,935 after
inheritance-mode compatibility, distributed across 3,139 genes.

### Result

**BUB1B ranked 2nd of 3,139 genes under the autosomal recessive model, and Exomiser assigned that
ranking to ORPHA:1052, mosaic variegated aneuploidy syndrome** — the correct disease, reached without
being told. Under the recessive model both variants were marked as contributing, so Exomiser
reconstructed the compound heterozygous pair on its own.

The same gene also took rank 1 under the autosomal dominant model, but that entry is an artefact we
report rather than claim: Exomiser attached it to **OMIM:114500, colorectal cancer (somatic)**, and
it wins the top slot because a single truncating allele saturates the variant term of the dominant
model. We originally wrote that the ClinVar whitelist was what short-circuited variant scoring to 1.0;
**we tested that and it is wrong.** Planting an unclassified ClinVar nonsense record in the same gene
(`chr15:40212550 G>T`, no CLNSIG, not whitelisted) gives the identical variant score of 1.0000 — the
`stop_gained` consequence alone saturates it (§ Benchmark, below). A single truncating allele in a
recessive gene is not a dominant colorectal cancer diagnosis. **The result we stand behind is rank 2, not rank 1.** We say so
because the honest reading of our own output matters more than the better-sounding headline.

The combined score gap is real but moderate: 0.5871 (rank 1, AD) and 0.5538 (rank 2, AR) against
0.2137 for the third-ranked gene — **2.59× the third gene for the recessive result we stand behind** (2.75× for the dominant artefact), not an order of magnitude.

### Robustness controls — including one that argues against us

We ran twelve additional Exomiser analyses to test how much of the result comes from the phenotype and
how much from the variant — eleven initially, plus one re-run after we found a flaw in our own control.

**Leave-one-HPO-out (8 runs).** Removing each HPO term in turn: **BUB1B remained rank 1 in all
eight**, with scores from 0.5447 to 0.7503. Removing the rhabdomyosarcoma term — the one a human
would consider most diagnostic — actually *raised* the score to 0.7503. No single symptom carries the
result.

**Unrelated HPO terms (2 runs, one of which corrects the other).** Our first version of this control
replaced the eight clinical terms with five we described as "clinically unrelated" — seizure
(HP:0001250), hearing impairment (HP:0000365), atrial septal defect (HP:0001631), conjunctivitis
(HP:0000509) and recurrent respiratory infections (HP:0002205). BUB1B came out rank 1, score 0.5506.

**That control was contaminated, and we caught it ourselves.** Querying the HPO annotations for
OMIM:257300 returns 59 terms, and **two of our five are among them**: seizure (HP:0001250, Nervous
System) and atrial septal defect (HP:0001631, Cardiovascular). Congenital heart defects including
septal defects are an established feature of MVA, and BubR1 loss disrupts cardiac development
(PMID 40055864). So the run was not a phenotype-free control at all — it fed the pipeline two genuine
MVA features.

**We re-ran it with five terms verified against the same annotation set as absent from MVA1:** hearing
impairment (HP:0000365), conjunctivitis (HP:0000509), recurrent respiratory infections (HP:0002205),
headache (HP:0002315) and pruritus (HP:0000989). **BUB1B still came out top of the ranking, score 0.4187 on
the dominant row.** The conclusion survives a clean control.

*A note on the denominator, because we had this wrong.* An earlier version of this sentence said
"rank 1 of 4,565 genes". 4,565 is the number of gene × inheritance-mode **rows** in that output file,
not genes: the run covers **3,139 genes**, and of those only **257 receive a combined score above
zero** (32 score ≥ 0.01) while the remaining rows are tied at the bottom rank with score 0. The
honest denominator is 3,139 genes, of which 257 were scored at all.

The comparison is informative, but we previously drew the wrong number from it. We wrote that
removing the two contaminating terms drops the score from 0.5506 to 0.4187, "about 24%", and called
that the size of the phenotype's contribution. **Both endpoints of that comparison are unrelated-HPO
controls** — the contaminated one and its correction — so the delta measures what two leaked
MVA-annotated terms were worth, not what the patient's phenotype is worth. **That figure is
withdrawn.**

The right comparison is the real phenotype against the clean control: **0.5871 with the patient's
eight terms, 0.4187 with five verified-unrelated terms, Δ = 0.1684**, and both values reproduce to
four decimal places when the same two alleles are planted into three unrelated healthy genomes
(§ Benchmark). We do **not** convert that delta into a percentage of the score: Exomiser combines
phenotype and variant evidence non-linearly, and 0.4187 is not a phenotype-free baseline, so a share
is not defined. It is a sensitivity of the score to the HPO query. Script and log:
`tools/control_hpo_r7.sh`, `tools/logs/controles_hpo_r7.log`.

**Least-specific term alone (1 run).** With short stature (HP:0004322) as the only input, BUB1B fell
to **rank 4** and HK1 took the top slot.

**No phenotype at all (1 run).** Exomiser terminates with an error; the tool requires at least one
HPO term, so this control could not be run.

**What this forces us to conclude.** We cannot call this a phenotype-driven discovery. The signal
comes from the **variant** — a pathogenic nonsense allele in a constrained gene (LOEUF 0.588) — not
from the phenotype, and not from the database record either: with both ClinVar classifications
stripped, the same molecular architecture still scores 0.5743 and still ranks first (§ Benchmark). The accurate description is **variant-driven and
phenotype-consistent**. What the phenotype does contribute is the choice between competing
interpretations of the same variant: it is the phenotype that makes Exomiser attach the recessive
model to mosaic variegated aneuploidy rather than to somatic colorectal cancer, and the
least-specific-term control shows the effect is real (one vague term is not enough to reach the top).
That is a narrower claim than "our pipeline found it from the symptoms", and it is the one the data
support.

A twelfth run removed the variant-effect filter entirely (219,399 variants across 13,338 genes, 22×
and 4× the primary run) and returned identical scores and an unchanged top ten. We report it as a
technical check that the filter did not manufacture the result, not as evidence of robustness — the
causal variants are coding, so the filter was never going to remove them.

### Analysis B — targeted panel, orthogonal confirmation

An 11-gene panel of MVA genes and phenocopies (BUB1B, CEP57, TRIP13, CENATAC, MAD1L1, MAD2L1BP,
CEP192, BUB1, SMC5, TRIM37, CENPE) with 5 kb padding. Coordinates were retrieved programmatically
from the **Ensembl REST API (release 116)** rather than from memory or a static file, and the
provenance of every coordinate is recorded. The 1,532 PASS variants inside those intervals were
annotated with the **Ensembl VEP REST API** and filtered for HIGH or MODERATE impact on the canonical
transcript at gnomAD AF below 1% or absent.

Exactly three variants survived. Two were in BUB1B; the third (MAD1L1 p.Arg59Cys) was a single allele
in a recessive gene and cannot explain the phenotype. **BUB1B was the only gene carrying two rare
damaging alleles.**

### Convergent answer

| Variant | Consequence | gnomAD (max pop. AF) | ClinVar | Exomiser ACMG (AR model) |
|---|---|---|---|---|
| `NM_001211.6:c.2210T>G` p.Leu737Ter | stop_gained | 9.98×10⁻⁵ (gnomAD exomes NFE) | 533901, Pathogenic/Likely pathogenic, 2★ | PATHOGENIC (PVS1, PM2_Supporting, PP4_Moderate, PP5_Strong) |
| `NM_001211.6:c.3006T>G` p.Asn1002Lys | missense | 8.99×10⁻⁷ (gnomAD exomes NFE) | not present | UNCERTAIN_SIGNIFICANCE (PM2_Supporting, PP4_Moderate, BP1) |

Two notes on this table, both of which correct looser statements we could have made:

- **The two frequency sources disagree for the nonsense variant.** Exomiser's bundled gnomAD gives
  9.98×10⁻⁵ (GNOMAD_E_NFE); the Ensembl VEP REST API returned ≈3×10⁻⁵ for the same variant. We report
  the Exomiser figure because it is the one the ranking was computed from, and we declare the
  discrepancy rather than pick the smaller number. Either way the allele is rare and there are no
  homozygotes.
- **The missense variant is not absent from gnomAD**, as we first wrote. It is present at 8.99×10⁻⁷,
  which is a single-observation-level frequency but not zero. It carries REVEL 0.472, MVP 0.852 and
  AlphaMissense 0.923 — the in-silico predictors disagree with each other, which is why we let it
  stand as a VUS rather than upgrade it.

On ClinVar: **c.3006T>G is not in ClinVar.** ClinVar contains `c.3006T>A`
(VCV004600147, `NC_000015.10:40220611:T:A`), a *different nucleotide substitution at the same
position* producing the same p.Asn1002Lys protein change, classified Uncertain significance —
criteria provided, single submitter, last evaluated 2025-09-19. That classification does **not**
transfer: the two alleles differ in splicing potential and in mutational context, and a VUS
transferred across alleles would in any case add no evidence. We did not use it.

**Interpretation: findings consistent with mosaic variegated aneuploidy type 1 (MVA1, OMIM 257300),
autosomal recessive, through compound heterozygosity in BUB1B (phase not demonstrated; see limitations).** The truncating-plus-missense configuration matches the allelic
pattern described in biallelic MVA patients — "in patients with biallelic mutations, a missense
mutation pairs with a truncating mutation" (Suijkerbuijk 2010, PMID 20516114). Reading that pair as
null-plus-hypomorph is our inference from the same work's observation of absent transcript from
truncating alleles and rapid turnover of missense product; the source does not state that complete
biallelic loss is lethal, and neither do we.

### Additional analysis — mosaicism (negative result, with a computed detection limit)

Because MVA is defined by mosaic aneuploidy, we tested whether that signature is visible in the bulk
WGS: per-chromosome B-allele frequency across 2.27 M heterozygous SNVs; the same restricted to a
fixed depth window (DP 40–48) to remove the coverage confounder; a spatial profile in 5 Mb windows;
and chromosomal dosage from 10%-trimmed mean depth. Three of these are refinements of the same BAF
statistic and only the dosage test is orthogonal — they are not four independent tests. Only the VCF
was available, with no BAM, so no GC-LOESS normalisation was possible.

**We computed the detection limit instead of asserting a negative, and we state where the threshold
comes from.** Across the 22 autosomes at fixed depth (DP 40–48, 857,435 sites), the measured standard
deviation of mean |BAF − 0.5| between chromosomes is **0.0035**. Our 0.005 noise floor is therefore a
≈1.4-SD criterion. Simulating mean |BAF − 0.5| at DP 44 against it, a clonal trisomy becomes
detectable only when present in **~14% of cells**.

The conclusion does not depend on that choice, and every stricter choice hurts the assay rather than
us: a conventional 2-SD criterion moves the limit to **16%**, and 3-SD to **20%**.

**Read sampling is not what sets that limit.** The simulation subtracts the binomial baseline at
DP 44, so the 0.005 threshold a signal must clear is the *measured dispersion between chromosomes* —
systematic library bias, not counting noise. The read-depth dosage test points the same way by a
separate route: Poisson error when averaging a whole chromosome at 44× is ≈0.03%, orders of magnitude
below the deviations observed. These are two different statistics and we do not conflate them; they
agree on the conclusion that **more sequencing depth would not move the limit**.

Every candidate signal traced to coverage, segmental duplications (22q11, centromeres) or — partially
— GC content. We flag that the GC explanation is incomplete: the measured GC–coverage correlation was
r = 0.43 from a sparse sample, and chr21, the largest deviation, is GC-poor. Where dosage and BAF
disagreed we favoured BAF, which is an internal per-site ratio and cancels coverage bias, and we
report the dosage result as an open question.

**We therefore do not claim the child lacks mosaic aneuploidy — he has it by diagnostic definition.**
We claim this assay cannot resolve it. Variegation spreads the burden across chromosomes: an
aneuploid fraction of ~30% distributed over the autosomes leaves each individual chromosome altered
in roughly **1–2% of cells, which is 7–16× below the 14–16% detection limit**. Bulk averaging erases
variegation by construction, at any depth. Premature chromatid separation, the cytogenetic hallmark of MVA, leaves no trace in DNA
sequence at all. The practical consequence is that **aneuploidy burden is not a measurable endpoint
in these data**, which constrains any Track 2 proposal whose outcome depends on it.

### Additional analysis — a pre-registered benchmark of this pipeline (MVA-Replay)

Our controls above test one genome once. To find out what this pipeline does when the answer is
*not* there, we built a benchmark on public data, **pre-registered it in git before running any case**
(`replay/PREREGISTRO.md`, commit `8086dd4`, with three dated amendments), and sent the design — unrun
— to two independent reviewers first. Their critique cut the design from ~150 runs to 61 and removed
four ways in which it was rigged in our favour. No patient data is used anywhere in it: backgrounds
are GIAB v4.2.1 benchmark genomes and 1000 Genomes 30× individuals; planted alleles are public ClinVar
records; the analysis configuration is the one used above, frozen.

**What score does a healthy genome produce under this phenotype?** Seven GIAB genomes, unspiked,
queried with the patient's exact eight HPO terms, produce top-gene combined scores of 0.0578, 0.0599,
0.2048, 0.4188, 0.4194, 0.4881 and **0.5619**. Our 0.5871 is above all seven, **by 0.025**. BUB1B does
not appear in the ranked table of any of them. We state the direction of the bias: these callsets are
autosome-only and high-confidence-region-only, retaining 6,510–9,486 variants against this patient's
12,431 and ranking 1,872–2,495 genes against 3,139, so the comparison is conservative *in our favour*;
and HG001 plus two trios is three independent units, not seven. A favourable null cleared by 0.025 is
a narrow margin, not a separation.

**Is the score a property of the patient's genome?** Planting the two public ClinVar records that
reproduce this case's architecture (533901 `chr15:40209701 T>G` nonsense, 4600147 `chr15:40220612 T>A`
VUS missense) into three unrelated healthy genomes returns **0.5871 with the real phenotype and
0.4187 with five unrelated terms, identical to four decimal places in all three**. The gene reached
the top position in 3/3 with the real phenotype and 2/3 with the unrelated one. The rank, not the
score, is what the background changes.

**How much of the score is the ClinVar record?** This is the result that went against what we had
written. Holding gene, consequence, partner allele and phenotype fixed and changing only the ClinVar
status:

| Construct | Nonsense allele | Missense allele | Combined score |
|---|---|---|---|
| this case's architecture | ClinVar P/LP, whitelisted | ClinVar VUS | 0.5871 |
| with the child's **real** missense (absent from ClinVar) | ClinVar P/LP | not in ClinVar | **0.5871** |
| with an **unclassified** ClinVar nonsense | no CLNSIG, not whitelisted | ClinVar VUS | **0.5743** |
| **with no ClinVar classification on either allele** | no CLNSIG | not in ClinVar | **0.5743** |

Individual variant scores are identical in every row (1.0000 for the nonsense, 0.9229 for the
missense). **Removing ClinVar entirely costs 0.0128 — 2.2% of the combined score — and does not
change the top position in either background tested.** The whitelist adds `PP5_Strong` to the ACMG
evidence; it is not what saturates the variant term, the `stop_gained` consequence is. An earlier
draft of this report credited the ranking to the ClinVar whitelist; that attribution is corrected
here. The finding is more robust than we had claimed: it would have been reached for a nonsense
allele that no database had ever seen.

**What the benchmark does not establish.** Every planted call is `PASS`, balanced and unambiguous, so
this measures retrieval *given a perfect heterozygous call*, not end-to-end diagnostic sensitivity.
Three case genes and one decoy are a replay of this case, not a general rare-disease benchmark. One
of seven pre-registered predictions was contrary to its predicted direction and is reported as such
in `replay/RESULTADOS.md`, together with the three conclusions of ours that the reviewers refuted.

## Q4 — Automated output or manual review?

Automated output with documented manual review. The submitted CSV is the direct result of the
convergence between the two analyses, but two decisions were made by hand — confirming the
compound-heterozygous pair and adjudicating the secondary candidates — and reporting the submission
as purely automated would be inaccurate.

## Q5 — Describe the manual review

Manual review was limited to two decisions, both documented:

1. **Confirming the compound-heterozygous pair.** Both analyses proposed the pair automatically; we
   verified the genotypes (0/1 for both), read depths (46× and 28×) and allelic balance
   (21,25 and 15,13) directly in the VCF.
2. **Adjudicating two secondary candidates** (see Q10).

No variant was added, removed or re-ranked on intuition.

## Q6 / Q7 — Data sources

Public data only. No proprietary data sources were used.

- Ensembl REST API release 116 (gene coordinates)
- Ensembl VEP REST API (functional consequence, canonical transcript, gnomAD frequencies)
- Exomiser 15.1.0 with data releases 2602_hg38 and 2602_phenotype
- gnomAD v4 (via Exomiser and VEP)
- ClinVar, GRCh38 (NCBI FTP snapshot and E-utilities)
- Human Phenotype Ontology (`hp.obo`, `genes_to_phenotype.txt`)
- REVEL, MVP, AlphaMissense and SpliceAI (via the Exomiser bundle)
- OMIM and Orphanet identifiers via the Exomiser `omimPrioritiser`
- Published literature (PubMed / Europe PMC), cited by PMID

## Q9 — Can the approach output compound heterozygous pairs?

Yes, and it did so without being told to. Exomiser's `AUTOSOMAL_RECESSIVE_COMP_HET` mode flagged both
BUB1B variants as contributing under the recessive model. The targeted analysis independently
selected any gene carrying two rare damaging alleles, which returned BUB1B alone.

**Neither method can establish phase, and we went and measured why rather than asserting it.**

*Read-backed phasing is closed by what the challenge distributes.* There is no parental sample, and
the dataset is a VCF with no BAM or CRAM, so no read-backed phaser (WhatsHap, HapCUT2) can be run at
all. What the VCF shows is consistent: GATK emitted no `PGT`/`PID` tags for either BUB1B variant,
which sit **10,911 bp** apart, while it *did* phase three FANCD2 variants spanning 5 bp into a single
haplotype (`PID=10046720_C_T`) elsewhere in the same file. Physical phasing worked where the distance
allowed it and was silent where it did not.

*Reference-panel phasing is closed by the panel.* Inside the 10,911 bp interval the patient carries
exactly three heterozygous sites — the two causal variants and `chr15:40216470 A>G` — and **all three
are absent from the 1000 Genomes 30× GRCh38 phased panel (3,202 individuals, 6,404 haplotypes)**. The
nearest panel-present heterozygous markers are 16.8 kb upstream (AF 0.0016) and 809 bp downstream
(AF 0.0075), with nothing in between that could link the two alleles. Beagle 5.5 run against that
panel confirms it operationally: 1,391 of the patient's 1,452 window variants survive, and all three
of the sites that matter are dropped, because a reference-panel phaser emits the panel's markers. The
absence is what the frequencies predict — expected copy counts in 6,404 haplotypes are 0.64 for the
nonsense (gnomAD max AF 1.0 × 10⁻⁴) and **0.006** for the missense (9.0 × 10⁻⁷); reaching a 95%
chance of observing the missense would need on the order of 3 × 10⁶ haplotypes.

*And our own pipeline would not have used phase if we had it.* In a controlled test on public data,
Exomiser reads phase into its ACMG evidence (trans → PM3, cis → BP2) but not into the
compound-heterozygous model: two pathogenic nonsense alleles declared on the **same** chromosome are
still called AR_COMP_HET, both still marked contributing, still classified PATHOGENIC, and still
ranked first — at a combined-score penalty of **0.34%** (0.9339 → 0.9305).

The compound-heterozygous interpretation therefore rests on allele rarity, the known recessive
inheritance of MVA1, the phenotype match, and the absence of homozygotes in gnomAD — not on a
demonstrated *trans* configuration, which is not observable in these data. **Parental genotyping at
the two loci is the single highest-value follow-up for this case**; long-read or linked-read
sequencing of the child, or allele-specific analysis of the BUB1B transcript, would also settle it.
All three require new laboratory work.

## Q10 — Secondary / incidental findings

**None reported.** The Exomiser output contains 12,431 variant-by-inheritance-model rows, 5,348 of
which carry an ACMG classification. **Three unique variants** reached pathogenic or likely pathogenic
(four rows — the BUB1B nonsense appears twice, once under the AD model and once under the AR model).
Two of the three lie outside BUB1B, and both were adjudicated as non-reportable:

**FANCD2 chr3:10046723 `AG>A` — `ENST00000675286.1:c.1278+1del`, Exomiser ACMG PATHOGENIC.** Three
independent reasons not to report it, in order of weight:

1. **The variant is not isolated: three co-phased changes in one splice region.** GATK phased it
   onto a single haplotype (`PID=10046720_C_T`) with two neighbours within 6 bp — chr3:10046720
   `C>T`, chr3:10046723 `AG>A` and chr3:10046725 `TAAG>T` (`c.1278+3_1278+5del`). All three sit at an
   allelic fraction of ≈0.31 (AD 65,31 / 61,28 / 66,28) rather than the ≈0.5 expected of a germline
   heterozygote. Three clustered, co-phased changes at a consistent sub-heterozygous fraction is the
   signature of a divergent or mismapped haplotype, not of three independent events. (An earlier
   draft described the second variant as an SNV 2 bp away; it is in fact a 3 bp deletion, which
   strengthens the mismapping reading rather than weakening it.)
2. **FANCD2 is a known short-read mapping pitfall.** The gene has high-identity pseudogenes, and
   the Fanconi anaemia sequencing literature documents that "database errors and in particular
   pseudogenes impose obstacles that may prevent correct data perception and interpretation"
   (PMID 23285130).
3. **ClinVar disagrees with Exomiser, though we weight this last.** ClinVar VariationID 3059927
   classifies the deletion **Benign**, while Exomiser calls it PATHOGENIC because its PVS1 rule fires
   on any canonical splice-donor deletion with no ClinVar downgrade applied. We put this third rather
   than first because the ClinVar record is weak evidence in its own right: **0 stars, no assertion
   criteria provided, a single submitter** (PreventionGenetics, SCV004798965.2). The neighbouring
   deletion (ClinVar 518343, Benign/Likely benign) carries the same limitation. A 0-star benign call
   does not by itself refute a pathogenic prediction — it is the co-phased haplotype and the
   allelic fraction that do the work here.

Even if the deletion were real, a single allele of an autosomal recessive disorder is carrier status.
Sanger sequencing or long reads would be needed before any clinical report.

**GNRHR chr4:67753920 `C>T` — `c.416G>A` p.Arg139His, Exomiser ACMG LIKELY_PATHOGENIC.** A clean
heterozygote (AD 28,32, DP 60) and ClinVar Pathogenic (VariationID 16030, multiple submitters, no
conflicts) for hypogonadotropic hypogonadism 7 with or without anosmia (OMIM 146110) — an
**autosomal recessive** condition, so a single allele is carrier status. The allele reaches 3.3% in
gnomAD Latino/Admixed American, consistent with a recessive carrier allele rather than a dominant
finding, and GNRHR does not appear on the ACMG SF v3.2 secondary findings gene list (statement:
PMID 37347242; gene table as reproduced by NCBI ClinVar, checked directly). Carrier status is not a reportable secondary finding, and the condition is unrelated
to this child's phenotype.

We chose to document the reasoning rather than submit these as `secondary` rows. They would not have
harmed the automated score, but reporting them as findings would be a clinically meaningful false
positive.

## Q11 — Runtime and cost

- Exomiser genome-wide run: **53 seconds** wall clock (32-core CPU, 16 GB JVM heap).
- Twelve robustness controls: about 11 minutes total.
- Targeted panel with REST annotation: under 5 minutes, dominated by API latency.
- Mosaicism analysis: about 10 minutes of `bcftools` streaming.
- One-off setup: ≈55 GB of Exomiser reference data downloaded and extracted.
- **Marginal compute cost is effectively zero** — a commodity workstation, no GPU, no cloud instance.
  Reproducing this on a laptop is realistic: only the 315 MB VCF and the phenotype document are
  needed, not the 85 GB of raw reads.

## Q12 — Method abstract (≤500 words)
We identified the causal variants through two independent analyses required to converge.

The primary analysis was hypothesis-free: Exomiser 15.1.0 (data 2602, hg38) on the complete proband
VCF — 4,740,790 PASS variants — driven only by the eight HPO terms taken verbatim from the clinical
document. No gene panel, no candidate list and no disease name entered the configuration.
**BUB1B ranked 2nd of 3,139 genes under the recessive model, mapped by Exomiser to mosaic variegated
aneuploidy syndrome (ORPHA:1052)**, both variants flagged as contributing. The same gene took rank 1
under the dominant model but attached to somatic colorectal cancer; we report that as an artefact of
a single truncating allele saturating the dominant model's variant term, not as a result.

The confirmatory analysis was orthogonal: an 11-gene MVA panel, coordinates from the Ensembl REST API,
annotated through VEP, filtered for HIGH/MODERATE impact below 1% gnomAD AF. Of 1,532 variants three
survived; two were in BUB1B, the only gene with two rare damaging alleles.

Both routes converge on **NM_001211.6:c.2210T>G p.Leu737Ter** (nonsense; ClinVar 533901
Pathogenic/Likely pathogenic; gnomAD 9.98×10⁻⁵) and **c.3006T>G p.Asn1002Lys** (missense; gnomAD
8.99×10⁻⁷; not in ClinVar) — the truncating-plus-missense allelic pattern of viable MVA1.

**Twelve robustness controls, one of which argues against us.** Leave-one-HPO-out keeps BUB1B on top
in all eight runs, but five verified-unrelated HPO terms also return it there (0.4187 against 0.5871).
The finding is **variant-driven and phenotype-consistent**: the loss-of-function consequence carries
the ranking; the phenotype selects the recessive MVA interpretation over the dominant artefact.

**We then measured what this pipeline does when the answer is absent.** A benchmark pre-registered in
git before any case ran — 61 runs, public data only, design critiqued by two independent reviewers —
shows three things. Seven healthy GIAB genomes queried with the same eight terms produce top-gene
scores of 0.058–0.562 against our 0.587, a margin of 0.025 on a null biased in our favour. Planting
the same two public ClinVar alleles into three unrelated healthy genomes reproduces 0.5871 and 0.4187
to four decimals — the score follows the alleles and the query, not the genome. And stripping both
ClinVar classifications costs **0.0128, 2.2% of the score**, without changing the top position: the
database record is not what drives the result, the truncating consequence is.

Mosaic aneuploidy is not visible in the bulk WGS and we computed why: at DP 44 the detection limit is
~14% of cells while variegation leaves each chromosome at 1–2%, 7–16× below it.

**Limitations.** Phase is not observable here: no parental sample, no alignments (a VCF was
distributed, so no read-backed phaser can run), 10,911 bp between the variants with no GATK phase tag,
and neither they nor the only heterozygous site between them is in the 1000 Genomes 3,202-sample
panel, so reference-panel phasing discards all three. Our pipeline is insensitive to phase in any
case. The functional consequence of p.Asn1002Lys is unproven and its predictors disagree (REVEL 0.472,
AlphaMissense 0.923). REMM and CADD were omitted. The genome-wide run took 53 seconds without a GPU.

## Q23 — Generative AI declaration

Commercially-available generative AI was used. Provider, plan and relevant setting for each:

- **Anthropic**, Claude Opus via Claude Code, **Max** subscription plan, model-improvement data
  sharing disabled in account privacy settings.
- **OpenAI**, Codex (gpt-5.6), **Plus** plan, "Improve the model for everyone" disabled.
- **xAI Grok 4.6 via Cursor**, **Pro** plan, **Privacy Mode enabled** (zero data retention at Cursor
  and at the underlying model providers).
- **Piper TTS** (`en_US-ryan-high`) — open-source, run entirely on local hardware with no cloud
  service and no API key. Used only to narrate the pitch video. Listed for completeness; it is not a
  commercial service.

**How these tools were used, and how they were not.** The language models were used for literature
retrieval and citation checking, for adversarial review of our own drafts, and for writing. They were
also used against us on purpose: two independent models were asked to attack our reports, and the
corrections they produced — including a claim of ours that contradicted our own data file — are
recorded in the repository under `evidencia/`.

**No block of the VCF and no genotype table was ever sent to a language model.** All genomic work ran
on local tools (`bcftools`, Exomiser 15.1.0) and on annotation APIs — Ensembl VEP and ClinVar — that
the hackathon policy names explicitly as acceptable. What the models saw were named variants, HPO
terms and reasoning: exactly the category the policy classifies as a "finding" and permits retaining.
