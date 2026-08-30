# Pre-registration — can bulk WGS see the disease's defining feature? A calibrated test of mosaic aneuploidy in this case

**Team ciberpty · MVA Hackathon 2026 · written 2026-08-30, BEFORE any statistic below was computed.**

Committed to git before `01_*.py` runs. Its timestamp is the evidence that the statistic, the masks,
the nuisance parameters, the confound exclusions, the predictions and the stopping rules were fixed in
advance. Amendments are appended at the bottom with a date; the text above is never edited.

---

## Why

Mosaic variegated aneuploidy is **named after** a cellular phenomenon: more than 25% of cells carrying
different aneuploidies. Our submitted Track 1 report says we looked for it in the bulk WGS, did not
find it, and computed a detection limit of **~14% of cells** for a clonal trisomy against an expected
1–2% per chromosome under variegation.

Two independent reviewers, given the raw-data situation, made the same objection and it is correct:
**that limit belongs to the statistic we used, not to the problem.** We used the mean of
|BAF − 0.5| without phase. At a 5% trisomy that statistic moves by 0.0001. It is close to blind below
about 10%.

The statistic the field actually uses for mosaic chromosomal alterations in this fraction range is
**haplotype-signed BAF**: phase the *common* SNPs against a reference panel, then sign each site's BAF
deviation by which haplotype carries the alternate allele. Deviations that would cancel without phase
now add. This is the basis of MoChA / hapLOH-style detection of mosaic chromosomal alterations at
**1–5% cell fraction**.

**We can run it on the data we have had since day one.** It needs genotypes at common SNPs, per-allele
read depths, and chromosome-scale phase. The proband VCF supplies the first two (2,927,826 autosomal
heterozygous calls, mean DP 44.8, with `AD`); Beagle against the 1000 Genomes 3,202-sample panel
supplies the third. Statistical phasing of *common* SNPs is a different problem from phasing the two
rare BUB1B alleles, which we already showed is not resolvable — that result stands and is not revisited
here.

**This can go against us in two directions and we accept both**: the calibrated limit may turn out no
better than 14%, or the test may return a signal that is a therapy-related clonal artefact rather than
MVA. The exclusion rules for the second are fixed below, before looking.

## The statistic — fixed now

For chromosome *c*, over its retained heterozygous sites *i*:

**φ_c = (1/N_c) · Σ_i s_i · (b_i − 0.5)**

where `b_i = AD_alt / (AD_ref + AD_alt)` and `s_i = +1` if the alternate allele sits on the phased
haplotype arbitrarily labelled 1, `−1` otherwise. The test statistic is **|φ_c|**, two-sided, because
the haplotype labelling is arbitrary per chromosome.

**Expected value under a mosaic gain of one homologue in a cell fraction f**, with phase switch-error
rate ε:

**E[φ_c] = (1 − 2ε) · f / (2·(2 + f))**   ≈ (1 − 2ε) · f/4 for small f.

**Companion statistic (secondary):** per-chromosome mean read depth at the same retained sites,
normalised to the autosomal median, as a dosage check. It is secondary because depth at variant sites
is a biased sampler of the genome; the unbiased version requires the alignments and is deferred to the
read-level stage.

## Site selection — fixed now

A site is retained if **all** hold:

1. autosomal, biallelic SNV;
2. genotype `0/1` in the proband VCF, `FILTER` = PASS;
3. present in the 1000 Genomes 30× GRCh38 phased panel with **MAF ≥ 0.01** (common SNPs only —
   rare sites cannot be phased against a panel, which is the lesson of our own phasing memo);
4. `DP` between **20 and 80** (a window around the mean of 44.8; excludes collapsed repeats above and
   unreliable calls below);
5. `GQ ≥ 30`;
6. outside the excluded regions below.

**Excluded regions, fixed now:** centromeres and the acrocentric short arms of chr13, 14, 15, 21, 22;
the ENCODE blacklist v2; segmental duplications; and any site within 10 kb of a gap in the reference.
Rationale: all four generate BAF and depth artefacts that are chromosome-specific, which is exactly
the axis the test runs along.

## Phasing procedure — fixed now

Beagle 5.5 (27Feb25.75f), `ref` = the 1000 Genomes 30× GRCh38 phased panel (3,202 individuals),
`map` = PLINK GRCh38 genetic map, run per chromosome, `impute=false`, default seed unless stated.
Only sites the panel contains are phased; the retention rule above already restricts to those.

**Switch errors are not corrected.** They attenuate the signal towards zero, so they make the test
conservative, and their magnitude enters the calibration below as a swept parameter rather than an
assumption.

## Calibration — the deliverable, and it uses no patient data

The limit of detection is not asserted; it is measured by injection, and the injection runs on public
data before the proband statistic is computed.

**Substrate:** the seven GIAB genomes (HG001–HG007), site structure and phase as above, with read
depths resampled to the proband's empirical DP distribution so the binomial noise matches 40×.

**Injection:** for a chosen chromosome and a cell fraction *f* ∈ {0.005, 0.01, 0.02, 0.05, 0.10,
0.20}, resample each retained site's alternate count from Binomial(DP, p) with p = (1+f)/(2+f) for
sites whose alternate allele is on the gained haplotype and p = 1/(2+f) otherwise. Repeat 200 times
per (chromosome, f). Also inject monosomy (p mirrored) and the two adversarial architectures below.

**Nuisance parameters swept, declared now:** phase switch-error rate ε ∈ {0, 0.01, 0.02, 0.05}; BAF
overdispersion κ ∈ {1, 2, 4} applied as a beta-binomial. κ is also **estimated empirically from the
proband's own autosomes**, which is legitimate because it is a nuisance parameter of the noise model,
not the quantity under test.

**Output:** a power curve — detection probability against *f*, per architecture, at a fixed
false-positive rate — and a single **LOD** defined as the smallest *f* detected in ≥ 80% of injections
at a genome-wide false-positive rate of 5% across 22 chromosomes.

## The identifiability result — stated before the data, because it does not depend on them

Bulk DNA observes mean copy number and mean allele fraction. It does not observe cell-to-cell
variance. Consider a mixture in which, for chromosome *c*, a fraction *g* of cells gains homologue A,
a fraction *g* gains homologue B, a fraction *l* loses A and a fraction *l* loses B. Then:

- mean copy number = 2 + 2g − 2l, which equals **exactly 2** when g = l;
- mean allele fraction at every heterozygous site = **exactly 0.5**, for any g and l, by symmetry.

**So a perfectly balanced variegated mixture is invisible in bulk at any sequencing depth.** This is
not low power; it is non-identifiability — two biologically distinct cell populations produce the same
observable distribution. We will state and demonstrate this, and it bounds what any bulk method,
including ours, can claim. **We predict it is the correct explanation of our negative result, if the
result is negative.**

## Confounds excluded in advance — this is post-chemotherapy blood

The specimen is from a child treated for embryonal rhabdomyosarcoma. Clonal haematopoiesis and
therapy-related clonal events are expected and are **not** evidence of mosaic variegated aneuploidy.
Fixed now, before looking:

- **del(20q), del(13q), del(5q), del(7q)/−7, +8, and loss of Y** are the canonical CHIP /
  therapy-related lesions. If any of these appears, it is reported as a clonal haematopoietic event
  and **does not count** as support for MVA.
- MVA-consistent evidence would be whole-chromosome **gains** (and losses) of autosomes outside that
  canon, and ideally more than one chromosome.
- Any segmental (sub-chromosomal) event is by definition not whole-chromosome aneuploidy and is
  reported separately.

**Tissue caveat, fixed now:** we do not know which tissue was sequenced. Every negative statement in
the report will read *"not detectable in the sequenced specimen"*, never *"absent in the child"*.
Mosaicism in MVA varies by tissue and by selection.

## Predictions on the record

- **P1.** The calibrated LOD for a clonal whole-chromosome trisomy is **better than 14%** — i.e. the
  haplotype-signed statistic beats the unphased one we published. *If it is not better, our current
  report needs no change on this point and we say so.*
- **P2.** The LOD is **worse than 1%**, so uniform variegation at 1–2% per chromosome remains below it.
  *We expect our own negative to survive.*
- **P3.** No autosome in the proband exceeds the genome-wide threshold. *If one does and it is outside
  the CHIP canon, that is a positive finding and the most important result of the project. If one does
  and it is inside the CHIP canon, it is reported as a therapy-related clonal event, not as MVA.*
- **P4.** The empirically estimated overdispersion κ of the proband's autosomes is between 1 and 4.
  *If κ > 4, the AD values in the provided VCF are noisier than a binomial model allows and the
  read-level stage becomes necessary rather than confirmatory.*
- **P5.** The balanced-variegation injection is **not detected at any f**, including f = 0.20,
  confirming the identifiability argument numerically.

## Stopping rules

- The statistic, the site filters, the masks, the injection grid and the thresholds above are fixed.
  Nothing is re-tuned after seeing the proband's φ values.
- **The calibration runs and is committed before the proband statistic is computed.** The order is not
  negotiable: public data first, patient last.
- If a chromosome exceeds threshold, the pre-declared confirmations are: reproducibility across
  independent sequencing lanes (requires the read-level stage), consistency between the BAF and depth
  statistics, robustness to the masks, and absence from the CHIP canon. A signal failing any of these
  is reported as unconfirmed.
- No metric is redefined after unblinding. A metric that proves unmeasurable is declared so in a dated
  amendment, as three already have been in `replay/PREREGISTRO.md`.

## Limitations declared in advance

- **The `AD` values come from the organisers' GATK 4.2.4.0 call set**, not from a pileup we control.
  Reference bias, realignment and filtering therefore enter the noise in ways we cannot fully model
  from the VCF. The read-level stage exists to bound this, and until it runs the LOD is a
  *first-order* limit.
- **Depth at variant sites is a biased sampler.** The unbiased dosage analysis with GC and mappability
  correction needs the alignments and is deferred.
- **Statistical phasing of common SNPs carries switch errors** that attenuate the statistic. Swept, not
  assumed.
- **One specimen, one tissue, one time point.**
- **This measures aggregate dosage imbalance, not cellular heterogeneity.** A number from this test can
  never be reported as "percentage of aneuploid cells" without a model of how aneuploidies are
  distributed across cells and chromosomes, which bulk data cannot supply.

---
## Amendments

*(none yet)*
