# Track 1 — Methods description

**Team: ciberpty** · MVA Hackathon 2026 · Proband PROBAND01
Repository: https://github.com/cpu-16/mva-hackathon-2026
Pitch video: https://youtu.be/QGYHK0Ihs1c

> **This write-up supersedes our earlier Track 1 submissions. The predictions CSV is byte-for-byte
> unchanged** — same two BUB1B variants, same score — so this is a correction to the methods
> description, not to the answer. Four errors in the version we submitted on 30 August are corrected
> here and each is named where it occurred: the unrelated-phenotype control was contaminated and read
> 0.4187 where the clean control reads **0.3965**; a "the phenotype contributes ~24%" figure that is
> **withdrawn** as an invalid conversion; the ranking attributed to the ClinVar whitelist when our own
> counterfactual shows it is worth **0.0128**; and a 30-genome benchmark described as still running
> that has since **finished, 0 of 30**. If more than one of our entries appears on the leaderboard,
> this is the one we ask the panel to read.

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

**BUB1B is the top-ranked gene of the 3,139 in this run, and its recessive row is first of the 2,100
recessive-model rows, mapped by Exomiser to ORPHA:1052, mosaic variegated aneuploidy syndrome** — the correct disease, reached without
being told. Under the recessive model both variants were marked as contributing, so Exomiser
reconstructed the compound heterozygous pair on its own.

The same gene also took rank 1 under the autosomal dominant model, but that entry is an artefact we
report rather than claim: Exomiser attached it to **OMIM:114500, colorectal cancer (somatic)**, and
a single truncating allele saturates the variant term of the dominant model, which is why that row's
score is 0.5871. **It is not why the dominant row outranks the recessive one**: in our benchmark the
dominant row wins whenever exactly one planted allele is truncating — this case (0.5871 dominant
against 0.5538 recessive) and the two-missense construct with no truncating allele at all (0.1120
against 0.0925). Where **both** planted alleles are truncating the recessive row wins instead, in all
three backgrounds (C-hi: 0.9332 recessive against 0.5818 dominant, `replay/out/C_hi_*_real.genes.tsv`).
The ordering tracks whether the recessive row's own variant term also saturates, not the ClinVar
label, and we report that rather than explain it.
We also originally wrote that the ClinVar whitelist was what short-circuited variant scoring to 1.0;
**we tested that and it is wrong.** Planting an unclassified ClinVar nonsense record in the same gene
(`chr15:40212550 G>T`, no CLNSIG, not whitelisted) gives the identical variant score of 1.0000 — the
`stop_gained` consequence alone saturates it (§ Benchmark, below). A single truncating allele in a
recessive gene is not a dominant colorectal cancer diagnosis. **The result we stand behind is rank 2, not rank 1.** We say so
because the honest reading of our own output matters more than the better-sounding headline.

*A note on what "rank 2" counts.* Exomiser's table lists one row per gene × inheritance mode. BUB1B
occupies the first two rows: 0.5871 (dominant) and 0.5538 (recessive). The next row, 0.2137, belongs
to FANCD2 — the **second gene**, not the third. So BUB1B is gene rank 1 of 3,139 and its recessive row
is rank 1 of 2,100 recessive rows; it sits second in the overall row ordering only because its own
dominant row sits first. The combined score gap is real but moderate: **2.59× the next gene for the
recessive result we stand behind** (2.75× for the dominant artefact), not an order of magnitude.

**Stated plainly, because it is the honest reading of our own output.** The pipeline's top-ranked row
for BUB1B is a *dominant* single-allele model, not the recessive compound-heterozygous model the
diagnosis rests on — and our benchmark shows the dominant row wins for BUB1B in every
construct with a single truncating allele, including one with no truncating allele at all — while in
the construct where both planted alleles truncate, the recessive row wins. The compound-heterozygous call is also invariant to
phase: declaring both alleles on the same chromosome changes neither the call, nor the
classification, nor the rank. **The recessive interpretation is supplied by the inheritance model of
the disease and by the two-allele architecture, not by the ranking.** What the retrieval delivers is
the right gene; the diagnosis is an interpretation we make on top of it, and we say so rather than
let the leaderboard number imply otherwise.

### Robustness controls — including one that argues against us

We ran additional Exomiser analyses to test how much of the result comes from the phenotype and how
much from the variant. We list them by family rather than by a single total, because the total has
been miscounted in earlier drafts: **eight leave-one-HPO-out runs**, **one least-specific-term-alone
run**, **one no-phenotype run**, and the **unrelated-HPO control, which we had to rebuild twice**
(original → r7 → r9). Output files for each are under `tools/results/controles/`.
⚠️ One of those files is misleadingly named and we say so rather than let a reader count it twice:
`hpos_barajados.genes.tsv` ("shuffled") is **not** a shuffled phenotype. `tools/control_hpo.sh` runs it
with the same five unrelated terms as the first version of the unrelated-HPO control, so it is that
control, not a separate family. We ran no shuffled-phenotype control.

⚠️ **Read this section together with the note at the end of it.** The version of this control that
travelled with our submitted entry is r7, and r7 was contaminated. The numbers below are the corrected
r9 analysis. **The submitted prediction CSV is unaffected and unchanged** — it contains the two BUB1B
variants and no control depends on it — so this is a correction to the write-up, not to the answer.

**Leave-one-HPO-out (8 runs).** Removing each HPO term in turn: **BUB1B remained rank 1 in all
eight**, with scores from 0.5447 to 0.7503. Removing the rhabdomyosarcoma term — the one a human
would consider most diagnostic — actually *raised* the score to 0.7503. No single symptom carries the
result.

**Unrelated HPO terms (three versions, each correcting the last).** Our first version of this control
replaced the eight clinical terms with five we described as "clinically unrelated" — seizure
(HP:0001250), hearing impairment (HP:0000365), atrial septal defect (HP:0001631), conjunctivitis
(HP:0000509) and recurrent respiratory infections (HP:0002205). BUB1B came out rank 1, score 0.5506.

**That control was contaminated, and we caught it ourselves.** Querying the HPO annotations for
OMIM:257300 returns 59 terms, and **two of our five are among them**: seizure (HP:0001250, Nervous
System) and atrial septal defect (HP:0001631, Cardiovascular). Congenital heart defects including
septal defects are an established feature of MVA, and BubR1 loss disrupts cardiac development
(PMID 40055864). So the run was not a phenotype-free control at all — it fed the pipeline two genuine
MVA features.

**We re-ran it (r7) with five terms verified as absent from MVA1:** hearing impairment (HP:0000365),
conjunctivitis (HP:0000509), recurrent respiratory infections (HP:0002205), headache (HP:0002315) and
pruritus (HP:0000989). BUB1B came out rank 1, score **0.4187**. **This is the version that travelled
with the submission, and it was contaminated too.**

**The r7 check was against `OMIM:257300` and nothing else, which was not enough.** Hearing impairment
(HP:0000365) is annotated to **OMIM:614114 (MVA2)**, to **ORPHA:1052** (the MVA umbrella term) and
directly to **BUB1B, CEP57 and TRIP13**. Exomiser scores phenotype similarity over the whole ontology
graph, so a term annotated to *any* MVA disease leaks the answer back in. The same class of error,
twice, from an incomplete verification.

**r9 — the clean control.** Five terms checked programmatically against all four MVA identifiers *and*
against the three MVA genes (`hpo/01_verificar.py`, result in `hpo/verificacion.json`): conjunctivitis
(HP:0000509), recurrent respiratory infections (HP:0002205), headache (HP:0002315), pruritus
(HP:0000989) and **skin rash (HP:0000988)**, which replaces hearing impairment. **BUB1B is still rank 1
in the proband's genome, score 0.3965 on the dominant row.** The conclusion survives a clean control;
the score the submitted write-up quoted was inflated by 0.0222.

**Screening control terms by eye does not work, and we stopped doing it.** Of thirteen candidate terms
put through the automated check, **four were rejected** — three of them replacements we had proposed
ourselves, because fever, dyspnoea and abdominal pain are each annotated to *TRIP13*.

⚠️ **What the rule still does not guarantee.** It removes terms with a *direct* annotation. It does not
remove terms that merely sit near an MVA term in the ontology graph, and Exomiser's similarity measure
is graph-based. The defensible statement is *"no term in the control set is annotated to any MVA
disease or MVA gene"*, not *"no term is related to MVA"*.

*A note on the denominator, because we had this wrong.* An earlier version of this sentence said
"rank 1 of 4,565 genes". That figure was a row count taken from a control run, and it was wrong in
both the unit and the value. The primary run's output (`tools/results/mva-genome-hpo.genes.tsv`) holds
**4,570 gene × inheritance-mode rows** covering **3,139 unique genes**; **257 genes have at least one
row scoring above zero** and 32 have a row ≥ 0.01. Separately, and in the other unit, **4,262 of the
4,570 rows carry a score of zero** and are tied at the bottom rank. The honest denominator is 3,139 genes, of which 257
were scored at all.

The comparison is informative, but we previously drew the wrong number from it. We wrote that
removing the two contaminating terms drops the score from 0.5506 to 0.4187, "about 24%", and called
that the size of the phenotype's contribution. **Both endpoints of that comparison are unrelated-HPO
controls** — the contaminated one and its correction — so the delta measures what two leaked
MVA-annotated terms were worth, not what the patient's phenotype is worth. **That figure is
withdrawn.**

The right comparison is the real phenotype against the **clean r9** control: **0.5871 with the
patient's eight terms, 0.3965 with five verified-unrelated terms, Δ = 0.1906**, and both values
reproduce to four decimal places when the same two alleles are planted into three unrelated healthy
genomes (§ Benchmark). We do **not** convert that delta into a percentage of the score: Exomiser
combines phenotype and variant evidence non-linearly, and 0.3965 is not a phenotype-free baseline, so
a share is not defined. It is a sensitivity of the score to the HPO query. Script:
`tools/control_hpo_r9.sh`; per-run outputs in `tools/results/controles/`.

**Least-specific term alone (1 run).** With short stature (HP:0004322) as the only input, BUB1B fell
to **rank 4** and HK1 took the top slot.

**No phenotype at all (1 run).** Exomiser terminates with an error; the tool requires at least one
HPO term, so this control could not be run.

**What this forces us to conclude.** We cannot call this a phenotype-driven discovery. The signal
comes from the **variant** — a pathogenic nonsense allele in a constrained gene (LOEUF 0.588) — not
from the phenotype, and not from the database record either: with both ClinVar classifications
stripped, the same molecular architecture still scores 0.5743 and still ranks first (§ Benchmark). The accurate description is **variant-driven and
phenotype-consistent**. **And we removed the last positive role we had attributed to the phenotype, because we tested it and
it was false.** We had written that the phenotype is what makes Exomiser attach the recessive model to
mosaic variegated aneuploidy rather than to somatic colorectal cancer. Re-running the clean
unrelated-HPO control with variant-level output shows the same two mappings — recessive row →
*Mosaic variegated aneuploidy syndrome*, dominant row → *Colorectal cancer, somatic* — under five
clinically unrelated terms. The disease assignment comes from the gene's known inheritance modes via
the OMIM prioritiser, not from the phenotype.

What the phenotype measurably does in this case is move the combined score by 0.1906 without changing
the top position in the proband's genome. The least-specific-term control shows it is not nothing (short stature alone drops
BUB1B to rank 4), but it does not select the interpretation, it does not choose the disease mapping,
and it does not decide the answer.
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
(VCV004600147, canonical SPDI `NC_000015.10:40220611:T:A`, 0-based, corresponding to VCF position 40220612), a *different nucleotide substitution at the same
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
WGS: per-chromosome B-allele frequency across 2.27 M heterozygous SNVs (biallelic, PASS, autosomes — the
2.93 M in `mosaico/RESULTADOS.md` counts every heterozygous call, not only biallelic SNVs); the same restricted to a
fixed depth window (DP 40–48) to remove the coverage confounder; a spatial profile in 5 Mb windows;
and chromosomal dosage from 10%-trimmed mean depth. Three of these are refinements of the same BAF
statistic and only the dosage test is orthogonal — they are not four independent tests. We worked from
the VCF and did no GC-LOESS normalisation. **That was our choice of input, not a limit of the
challenge:** the organisers do distribute the raw reads (84.7 GB of FASTQ), and the analysis that
decided the question did not need them (`mosaico/RESULTADOS.md`).

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

**A later analysis replaced that first-order limit, and it does not help us.** Calibrating the null —
Ψ over 125-site windows, the measured switch process, the empirical segment-size distribution and
40,000 Monte Carlo replicates per cell — gives **2.07% of cells at an overdispersion κ = 2** (1.46% at
κ = 1, 2.95% at κ = 4; `mosaico/ventana.json` at the chosen window W = 125). That is a *simulated*
limit under a fitted null, conditional on κ, not a measured sensitivity.

**We therefore do not claim the child lacks mosaic aneuploidy — he has it by diagnostic definition.**
We claim this assay cannot resolve it. Variegation spreads the burden across chromosomes: an
aneuploid fraction of ~30% — the order of magnitude of the diagnostic criterion, not a figure from
this patient — distributed over the autosomes leaves each chromosome altered in roughly **1–2% of
cells**. Against the first-order 14–16% floor that is 7–16× below it; **against the calibrated 2.07%
limit it sits at the boundary**, which is a worse position for the assay, not a better one. The
conclusion survives either way, but not *because of* any limit. The argument that depends on no limit
is this: **a perfectly balanced variegated mixture is not identifiable from bulk allele fractions** —
equal gains of either homologue and matched losses give mean copy number exactly 2 and mean allele
fraction exactly 0.5 by symmetry, and simulated detection stays at the **0.1–0.2% false-positive rate
from 2% up to 40% aneuploid cells** (`mosaico/RESULTADOS.md` §4). That proof is about the balanced
mixture we modelled, not about every MVA genome.

**What we do not claim about this child.** The patient-level mosaicism result is **withdrawn**. The
pre-registered external control (10 healthy 1000 Genomes individuals) came back **not conclusive**:
the proband sits *below* the control envelope on both statistics and both chromosomes, an outcome the
amendment did not foresee, and the controls carry no GQ filter and a different caller, a mismatch
declared in advance with that same direction (`mosaico/CONTROL_RESULTADO.md`). **We report no clinical
negative at any percentage.** Bulk averaging erases variegation by construction, at any depth. Premature chromatid separation, the cytogenetic hallmark of MVA, leaves no trace in DNA
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
autosome-only and high-confidence-region-only, retaining **5,079–6,912 unique variants against this
patient's 8,939** and ranking 1,872–2,495 genes against 3,139, so the comparison is conservative *in
our favour*;
and HG001 plus two trios is three independent units, not seven. A favourable null cleared by 0.025 is
a narrow margin, not a separation.

**Is the score a property of the patient's genome?** Planting this case's own two alleles — the public
ClinVar nonsense (533901, `chr15:40209701 T>G`) and the child's missense (`chr15:40220612 T>G`, absent
from ClinVar; the ClinVar record at that position, 4600147, is a different substitution, `T>A`) — into
three unrelated healthy genomes returns **0.5871 with the real phenotype and
0.3965 with the five clean r9 unrelated terms, identical to four decimal places in all three**. The narrow
statement is the one `replay/RESULTADOS.md` §2 makes: under this frozen pipeline, and given that none
of the three backgrounds carries a retained BUB1B variant of its own, the planted gene's combined score
does not move with the background while its rank does. That is stability of the score across the
backgrounds we tested — one deterministic computation run three times — not a demonstration that the
score is independent of the genome in general. A background carrying its own BUB1B variant (the
1000 Genomes tier shows one, HG00101) was not tested with planted alleles, and our phase pilot already
shows the score is not fully determined by the two alleles (0.9339 *trans* vs 0.9305 *cis*, § Phase).

| Background | Real HPO, rank | Clean unrelated HPO, rank | Top gene under unrelated HPO |
|---|---|---|---|
| HG001 | 1 | **1** | BUB1B 0.3965 |
| HG002 | 1 | **2** | KRT17 0.5766 |
| HG005 | 1 | **3** | TNF 0.7436 |

So with the real phenotype BUB1B is first in 3 of 3; with a clean unrelated phenotype it is first in
**1 of 3**. Under the contaminated r7 set the same cells read 1 / 1 / 3, so the correction moves
exactly one background, HG002. Neither KRT17 nor TNF is directly annotated to any of the five control
terms — we checked `genes_to_phenotype.txt` — so the displacement is Exomiser's graph-based semantic
similarity, and the replacement term "skin rash" sits near KRT17's cutaneous disease terms. In the
proband's own genome BUB1B remains rank 1 under the clean control.

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
missense). **The combined score falls by 0.0128 and the top position does not change in either background
tested; Exomiser's own call moves from PATHOGENIC to LIKELY_PATHOGENIC.** We do not express 0.0128 as
a percentage of the score, for the same reason we withdrew the phenotype percentage above: the
combination is non-linear and a share is not defined.

**What this does and does not establish.** We could not delete ClinVar's record for the child's own
allele, so the last two rows substitute a *different* `stop_gained` at `chr15:40212550` — a ClinVar
record carrying no classification and no whitelist flag. Gene, consequence class, partner allele and
phenotype are held fixed; the locus is not. It therefore refutes our earlier claim that ClinVar
whitelisting is what saturates the variant term — an unclassified nonsense reaches the same 1.0000 —
and it shows the top position survives without any ClinVar classification in these two backgrounds. It
does **not** show that an allele no database had ever recorded would rank identically, and it is not a
deletion of ClinVar from this case's own variant.

**The principal null experiment has now finished.** The pre-registered design calls for 37 healthy
genomes. The seven GIAB genomes are above; the **30 unrelated 1000 Genomes genomes are complete**, with
a maximum top-gene combined score of **0.5207 (CDH1, HG01885)** and **0 of 30 exceeding 0.5871**. The
prediction was stated against the maximum, so a single exceedance would have falsified it, and the
sentence published for this outcome was frozen before any of those runs finished
(`replay/RESULTADOS.md` §8). Effective independence is roughly 33 unrelated individuals plus two trios,
not 37 draws, and both callsets carry a lower rare-variant burden than clinical WGS, which lowers
healthy top scores and biases the comparison *in our favour*.

⚠️ One qualifier: *"BUB1B does not appear in the ranked table"* holds for the seven GIAB genomes. In
the 1000 Genomes tier BUB1B does appear once, in HG00101, at rank 138 with a score of 0.0002. P-A2 was
stated as "absent or below 0.25", so it holds — but the stronger wording does not.

**Pre-registered predictions, re-scored against each definition.** The corrected control changes one
of them, and it changes it against us, which is the outcome we pre-committed to publishing:

| Prediction, as locked | Status |
|---|---|
| P-A — 0.5871 above every healthy genome's top score | **confirmed** (0 of 7 GIAB and 0 of 30 1000G exceed it) |
| P-A2 — BUB1B absent or < 0.25 in healthy genomes | **confirmed** (absent in 7/7 GIAB; 0.0002 in one 1000G genome) |
| P-B1 — planted BUB1B rank 1 in 3/3 with real HPO | **confirmed** |
| P-B2 — planted BUB1B rank 1 in ≥ 2/3 with unrelated HPO | **falsified** with the clean control (1/3). It read confirmed (2/3) only with the contaminated set |
| P-B3 — planted decoy rank 1 in ≥ 2/3 with real HPO | **not evaluable as locked** — a pool defect our own ingestion check caught; the corrected construct ran contrary to the predicted direction |
| P-B4 — Δ(real − unrelated) < 0.20 | **confirmed** (0.1906 with the clean control, against 0.1684 with the contaminated one); the percentage form is withdrawn |
| P-C — monotonic gradient, C-hi − C-lo ≥ 0.10 | **confirmed** (0.8212) — **our causal reading of it is retracted** |

That is **five confirmed, one falsified and one not evaluable**. The falsification is P-B2, and the
pre-registration said in advance that we *expected our own pipeline to fail this one* and pre-committed
to publishing it if it did (`replay/PREREGISTRO.md`). We are not presenting it as a victory; we are
presenting it because we said we would.

**What the benchmark does not establish.** Every planted call is `PASS`, balanced and unambiguous, so
this measures retrieval *given a perfect heterozygous call*, not end-to-end diagnostic sensitivity.
Three case genes and one decoy are a replay of this case, not a general rare-disease benchmark. Thirty
seven healthy genomes are not a validation cohort, and the GIAB and 1000 Genomes callsets share biases
of their own. All of this, and the three conclusions of ours that the reviewers refuted, is in
`replay/RESULTADOS.md`.

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

No variant was added, removed or re-scored, and no gene was moved in the ranking. There is one
interpretive judgement, made in the open: Exomiser emitted both a dominant and a recessive row for
BUB1B and scored the dominant one higher, and we report the recessive one as the result because the
dominant row is attached to somatic colorectal cancer and a single truncating allele in a recessive
gene is not that diagnosis. That is a judgement about which of the tool's own outputs to stand
behind, not a re-ranking.

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
which sit **10,911 bp** apart, while it *did* phase four FANCD2 variants spanning 18 bp into a single
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
ranked first. The combined score moves by **0.0034 in absolute terms** (trans 0.9339, cis 0.9305,
unphased 0.9325) — an absolute difference, not a share.

The compound-heterozygous interpretation therefore rests on allele rarity, the known recessive
inheritance of MVA1, the phenotype match, and the absence of homozygotes in gnomAD — not on a
demonstrated *trans* configuration, which is not observable in these data. **Parental genotyping at
the two loci is the single highest-value follow-up for this case**; long-read or linked-read
sequencing of the child, or allele-specific analysis of the BUB1B transcript, would also settle it.
All three require new laboratory work.

⚠️ **Settling phase would not settle the missense.** A confirmed *trans* configuration supports the
compound-heterozygous model and contributes PM3-type evidence; it does **not** on its own reclassify
p.Asn1002Lys from uncertain significance. Function is a separate question and would need a functional
assay. The *cis* result is the decisive one in the other direction: it would refute this
interpretation.

## Q10 — Secondary / incidental findings

**None reported.** The Exomiser output contains 12,431 variant-by-inheritance-model rows, 5,348 of
which carry an ACMG classification. **Three unique variants** reached pathogenic or likely pathogenic
(four rows — the BUB1B nonsense appears twice, once under the AD model and once under the AR model).
Two of the three lie outside BUB1B, and both were adjudicated as non-reportable:

**FANCD2 chr3:10046723 `AG>A` — `ENST00000675286.1:c.1278+1del`, Exomiser ACMG PATHOGENIC.** Three
independent reasons not to report it, in order of weight:

1. **The variant is not isolated: four co-phased changes in one splice region.** GATK phased it
   onto a single haplotype (`PID=10046720_C_T`) with three neighbours within 18 bp — chr3:10046720
   `C>T`, chr3:10046723 `AG>A`, chr3:10046725 `TAAG>T` (`c.1278+3_1278+5del`) and chr3:10046738
   `C>T`. All four sit at an allelic fraction of 0.30–0.32 (AD 65,31 / 61,28 / 66,28 / 58,27) rather
   than the ≈0.5 expected of a germline heterozygote. Four clustered, co-phased changes at a
   consistent sub-heterozygous fraction is the
   signature of a divergent or mismapped haplotype, not of four independent events. (An earlier
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
**autosomal recessive** condition, so a single allele is carrier status regardless of frequency. Its
maximum population frequency is **0.033%** (gnomAD genomes, Latino/Admixed American — Exomiser reports
`MAX_FREQ` as a percentage, 0.0327, the same convention under which the BUB1B nonsense reads 0.00998),
and GNRHR does not appear on the ACMG SF v3.2 secondary findings gene list (statement:
PMID 37347242; gene table as reproduced by NCBI ClinVar, checked directly). Carrier status is not a reportable secondary finding, and the condition is unrelated
to this child's phenotype.

We chose to document the reasoning rather than submit these as `secondary` rows. They would not have
harmed the automated score, but reporting them as findings would be a clinically meaningful false
positive.

## Q11 — Runtime and cost

- Exomiser genome-wide run: **53 seconds** wall clock (32-core CPU, 16 GB JVM heap).
- Robustness controls (the families listed under *Robustness controls* above, one Exomiser run each): about
  a minute per run, roughly 11 minutes in total.
- Targeted panel with REST annotation: under 5 minutes, dominated by API latency.
- Mosaicism first-order BAF scan: about 10 minutes of `bcftools` streaming.
- Mosaicism null calibration (40,000 Monte Carlo replicates per cell, eight window sizes): run with
  PyTorch on one consumer GPU (`mosaico/05_mc_gpu.py`; `lod_montecarlo.json` records `"dispositivo":
  "cuda"`). The script falls back to CPU when no CUDA device is present, and this is the **only** GPU
  use anywhere in the work — the genome-wide Exomiser run above needs none.
- One-off setup: ≈55 GB of Exomiser reference data downloaded and extracted.
- **Marginal compute cost is effectively zero** — a commodity workstation, no cloud instance and no
  specialised hardware.
  Reproducing this on a laptop is realistic: only the 315 MB VCF and the phenotype document are
  needed, not the 84.7 GB of raw reads.

## Q12 — Method abstract (≤500 words)
We used two independent analyses and required them to converge.

The primary analysis was hypothesis-free: Exomiser 15.1.0 (data 2602, hg38) on the complete proband
VCF — 4,740,790 PASS variants — driven only by the eight HPO terms taken verbatim from the clinic. No
gene panel, candidate list or disease name entered the configuration. **BUB1B is the top-ranked gene
of 3,139, and its recessive row is first among the 2,100 recessive-model rows, mapped by Exomiser to
mosaic variegated aneuploidy syndrome (ORPHA:1052)**, both variants contributing. Its *dominant* row
scores higher (0.5871 vs 0.5538) but is attached to somatic colorectal cancer; **we report the
recessive row and call the dominant one an artefact.**

The confirmatory analysis was orthogonal: an 11-gene MVA panel from Ensembl, annotated through VEP,
filtered for HIGH/MODERATE impact below 1% gnomAD AF. Of 1,532 variants three survived, two of them in
BUB1B, the only gene with two rare damaging alleles.

Both routes converge on **NM_001211.6:c.2210T>G p.Leu737Ter** (nonsense; ClinVar 533901
Pathogenic/Likely pathogenic; gnomAD 9.98×10⁻⁵) and **c.3006T>G p.Asn1002Lys** (missense; gnomAD
8.99×10⁻⁷; not in ClinVar) — the truncating-plus-missense pattern of viable MVA1.

**Robustness controls; the phenotype comes out weaker than we claimed.** Leave-one-HPO-out keeps
BUB1B on top in all eight runs; five verified-unrelated HPO terms also return it there in the proband's
genome (**0.3965 against 0.5871**). The finding is **variant-driven and phenotype-consistent**: the phenotype moves the score by
**0.1906** and changes nothing else. The unrelated-HPO control had to be rebuilt twice; the version quoted in our submitted
entry (0.4187) was contaminated by a term annotated to MVA2.

**We then measured what this pipeline does when the answer is absent**, in a benchmark pre-registered
in git before any case ran. Seven healthy GIAB genomes queried with the same eight terms top out at
**0.5619 against our 0.5871** — a margin of 0.025 on a null biased in our favour. The pre-registered
30-genome 1000 Genomes tier has since finished: maximum **0.5207 (CDH1, HG01885)**, **0 of 30** above
0.5871. Planting the same two public ClinVar alleles into three unrelated healthy genomes reproduces
0.5871 and 0.3965 to four decimals — stability across the backgrounds tested, not independence from
the genome — while the *rank* under the unrelated phenotype holds in only one of the three, which
falsifies a pre-registered prediction we said we expected to fail. Substituting an **unclassified**
BUB1B nonsense for the whitelisted one moves the combined score only 0.0128 without losing the top
position: the truncating consequence, not the database record, saturates the variant term.

**Limitations.** Phase is not observable here: no parental sample, no alignments (the challenge
distributed a VCF and raw reads, not a BAM, and we did not realign), 10,911 bp between the variants
with no phase tag, and none of the relevant sites is in the 1000 Genomes panel. Our pipeline is
insensitive to phase regardless. p.Asn1002Lys is functionally unproven and its predictors disagree
(REVEL 0.472, AlphaMissense 0.923). The genome-wide run took 53 seconds without a GPU.

## Q23 — Generative AI declaration

Commercially-available generative AI was used. Provider, plan and relevant setting for each:

- **Anthropic**, Claude Opus and Claude Fable 5.1 via Claude Code, **Max** subscription plan, model-improvement data
  sharing disabled in account privacy settings.
- **OpenAI**, Codex (gpt-5.6), **Plus** plan, "Improve the model for everyone" disabled.
- **xAI Grok 4.6 via Cursor**, **Pro** plan, **Privacy Mode enabled** (zero data retention at Cursor
  and at the underlying model providers).
- **Qwen3-TTS 1.7B VoiceDesign** — open-weights, run entirely on local hardware (CPU) with no cloud
  service and no API key. Used only to narrate the pitch video. Listed for completeness; it is not a
  commercial service. Every generated clip was transcribed by a local speech recogniser and diffed
  against the written script before the video was assembled (`video/tts_verify.py`), because a
  speech model of this kind can drop or alter a word silently — it did so once, and the affected
  line was rewritten and re-generated.

**How these tools were used, and how they were not.** The language models were used for literature
retrieval and citation checking, for adversarial review of our own drafts, and for writing. They were
also used against us on purpose: two independent models were asked to attack our reports, and the
corrections they produced — including a claim of ours that contradicted our own data file — are
recorded in the repository under `evidencia/`.

**No block of the VCF and no genotype table was ever sent to a language model.** All genomic work ran
on local tools (`bcftools`, Exomiser 15.1.0) and on annotation APIs — Ensembl VEP and ClinVar — which
return public annotation for submitted coordinates and acquire no rights over the input. The policy
does not name these services; we read them as satisfying the two conditions it does set, namely no
training on inputs or outputs and limited retention. What the models saw were named variants, HPO
terms and reasoning: exactly the category the policy classifies as a "finding" and permits retaining.

---

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with
the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for
Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their
family who generously contributed their data and their story to advance research into this rare
disease. We acknowledge their trust in making this Hackathon possible.

## Data availability

The individual-level data analysed here is the Hackathon dataset (`SageBio/mva-hackathon-2026-data`),
accessed under the challenge data transfer agreement accepted by Hugging Face account `cpu-16` on
2026-08-28, and cited as directed on the Hackathon Synapse page. **No patient sequence data or
genotype-scale derivative is included in this document or in our public repository**, and every copy
we hold will be deleted by 2026-11-23 with written confirmation to the organisers. The two diagnostic
variants are named, as findings, which the challenge rules permit. All other inputs are public:
Exomiser 15.1.0 with data release 2602, ClinVar, gnomAD v4, the Human Phenotype Ontology, Ensembl and
VEP, the 1000 Genomes and GIAB genomes, DepMap 24Q4, AlphaFold and the literature cited by PMID.
Analysis code, pre-registrations and results: https://github.com/cpu-16/mva-hackathon-2026
