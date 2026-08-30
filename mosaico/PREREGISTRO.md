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

### Amendment 1 — 2026-08-30, before the proband statistic was computed

**The pre-registered statistic is the wrong one for this noise, and we caught it in the calibration.**

The analytic calibration above treats phase switch errors as independent per site, entering only as
the attenuation factor (1 − 2ε). **They are not independent.** A switch error from a reference-panel
phaser inverts the haplotype assignment for an entire *run* of consecutive sites, until the next
switch. Under a mosaic gain the true per-site deviation is +Δ throughout, so an inverted run
contributes −Δ, and the chromosome-wide signed mean becomes

  φ_c = Δ · (1 − 2q),  where q is the *fraction of sites lying in inverted runs*.

If a chromosome carries S phase segments of roughly random orientation, |1 − 2q| has magnitude ≈ 1/√S.
At a plausible S ≈ 300 segments per chromosome that is a **~17× dilution**, which would move the limit
of detection from the 0.30–0.67% computed above to roughly 5%. This is exactly why the published
methods in this area (MoChA, hapLOH) run a hidden Markov model over the phased B-allele frequency
rather than averaging it: the model absorbs the unknown orientation of each segment.

**The primary statistic is therefore replaced, before any proband value was computed, by an
orientation-invariant form:**

  **Ψ_c = Σ_s w_s · ( φ_s² − v_s )**,  where the sum runs over phase segments *s* of chromosome *c*,
  φ_s is the signed mean within segment *s*, v_s is its variance under the null, and w_s = N_s / N_c.

Each segment contributes Δ² under the alternative regardless of its orientation, so segmental switch
errors no longer cancel the signal. Under the null Ψ_c is a weighted sum of centred chi-square terms
and its distribution is obtained by the same Monte Carlo procedure already declared.

**The chromosome-wide signed mean φ_c is retained as a secondary statistic**, reported alongside, both
because it is what was originally pre-registered and because it remains the more powerful test in the
limit of near-perfect phase.

**Segments are defined by the measured switch positions, not assumed.** Before either statistic is
applied to the proband we measure the actual switch-error rate and segment-length distribution of our
own phasing procedure, using the GIAB Ashkenazi trio: HG002 phased by Beagle against the 1000 Genomes
panel, compared against Mendelian phase derived from HG003 and HG004 at trio-informative sites. That
measurement is public data only, it is the input to the calibration, and it is reported whatever it
says. **If the measured switch rate makes even Ψ_c underpowered below 2%, the honest conclusion is a
measured limit rather than a detection, and that is what we will report.**

The three-line summary of the analytic calibration that prompted this amendment is kept for the
record: with independent switch errors, N = 158,612 sites on chr1 and mean depth 42.5, the limit of
detection was 0.30% (ε = 0, κ = 1) to 0.67% (ε = 0.05, κ = 4), against the 14% our submitted report
attributes to bulk WGS. **Prediction P2 — that the limit would remain worse than 1% — is falsified in
that idealised model.** Whether it survives realistic segmental phasing is what the measurement above
decides.

### Amendment 2 — 2026-08-30, window size chosen on public data before unblinding

Amendment 1 replaced the chromosome-wide signed mean with the orientation-invariant Ψ. Computing Ψ
needs segment boundaries, and **in the proband we do not know where the switches are** — that
information exists only for the GIAB trio, where Mendelian phase gives ground truth. Ψ is therefore
computed over **fixed windows of W consecutive retained sites**, and a switch falling inside a window
attenuates that window's φ_s rather than being absorbed by a boundary.

W is a tuning parameter and it is chosen **on public data, before any proband value is computed**, by
minimising the calibrated limit of detection under the measured switch process (0.810% per site) at
the central overdispersion κ = 2. Monte Carlo, 40,000 null replicates per cell, on GPU:

| W (sites) | windows | LOD κ=1 | LOD κ=2 | LOD κ=4 |
|---|---|---|---|---|
| 20 | 7,402 | 1.81% | 2.57% | 3.65% |
| 50 | 2,960 | 1.56% | 2.21% | 3.15% |
| 100 | 1,480 | 1.49% | 2.11% | 2.99% |
| **125** | **1,184** | **1.46%** | **2.07%** | **2.95%** |
| 150 | 986 | 1.47% | 2.09% | 2.96% |
| 200 | 740 | 1.51% | 2.15% | 3.05% |
| 300 | 493 | 1.60% | 2.26% | 3.22% |
| 500 | 296 | 1.75% | 2.48% | 3.52% |

**W = 125 sites is fixed from here.** The curve is a clean minimum and it lands on the analytic
optimum of 1/(switch rate) = 123 sites, which is an independent check that the simulation is modelling
the attenuation correctly. That check matters: an earlier version of this sweep contained a coding
error in which the switch attenuation cancelled itself (the assumed sign multiplied the true sign, and
their product is identically one), which made ever-larger windows look monotonically better. It was
caught because the answer disagreed with the analytic optimum. The corrected sweep is the one above.

**The two limits of detection are reported separately and must not be conflated:**

- **1.12–2.26%** — Ψ with *known* segment boundaries. This is what a method with perfect switch
  detection would achieve, and it is an upper bound on performance, not our result.
- **1.46–2.95%, central estimate 2.07%** — Ψ over fixed windows, which is what we can actually run on
  the proband. **This is the number that goes in the report.**

Against the 14% our submitted report attributes to bulk WGS, that is a **6.8-fold improvement**, and
it places the achievable limit at the upper edge of the 1–2% per chromosome that variegation implies.
