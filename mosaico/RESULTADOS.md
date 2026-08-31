# Can bulk WGS see the disease's defining feature? — results

> ⚠️ **STATUS: the proband conclusion in §5 is WITHDRAWN pending an external control.** Two reviewers
> found that we calibrated one test and applied another: the pre-registered rule fires on 22 of 22
> autosomes, and the negative we reported came from an uncalibrated post-hoc statistic. See
> Amendment 3 in `PREREGISTRO.md`. §1–§4 (the wrong-statistic diagnosis, the measured switch rate,
> the calibration arithmetic and the identifiability result) are unaffected.

**Team ciberpty · MVA Hackathon 2026 · 30-ago-2026.**
Design, statistic, masks, confound exclusions and predictions were fixed in `PREREGISTRO.md` and
committed (`ed0feae`) before anything below was computed. The calibration was completed and committed
(`55b4594`) **before the proband statistic was computed**. Two amendments are dated in that file.

---

## The short version

| | |
|---|---|
| What our submitted report claims | mosaic aneuploidy detectable only above **~14%** of cells |
| What the right statistic achieves, **measured** | **~2.1%** (1.46–2.95% over the overdispersion range) |
| What the proband shows | **no chromosome-specific mosaic imbalance**; no chromosome reaches \|z\| = 3 |
| What no statistic can ever achieve | **balanced variegation is non-identifiable** — invisible at any cell fraction and any depth |

---

## 1. Why the published limit was the wrong number

Our Track 1 report puts a ~14% detection limit on mosaic aneuploidy and presents it as the limit of
bulk WGS. It is the limit of the *statistic we chose*: the mean of |BAF − 0.5| without phase, which
moves by 0.0001 at a 5% trisomy.

The statistic used in the field for mosaic chromosomal alterations at 1–5% cell fraction is
**haplotype-signed BAF**: phase the common SNPs against a reference panel, then sign each site's BAF
deviation by which haplotype carries the alternate allele, so deviations that cancel without phase
instead add. Reference bias, which lowers every b_i equally, cancels in the signed mean because the
sign is independent of which allele is reference.

**It needs no raw reads.** The proband VCF supplies 2,927,826 autosomal heterozygous calls at mean
DP 44.8 with per-allele depths; Beagle against the 1000 Genomes 3,202-sample panel supplies
chromosome-scale phase for the common sites. Retained after the pre-registered filters: **2,059,000
sites**, 27,510–171,120 per chromosome.

## 2. The switch-error rate, measured against a trio rather than assumed

Statistical phasing makes segmental errors: one mistake inverts the haplotype assignment for a whole
run of sites. We measured ours instead of assuming it, using the GIAB Ashkenazi trio — HG002 phased by
Beagle against the panel, compared to Mendelian phase from HG003 and HG004 at **48,027
trio-informative sites** on chr15:

- **switch-error rate: 0.810%** per consecutive heterozygous site pair
- **377 phase segments**, median 22 sites and 40 kb, mean 123 sites and 201 kb

**This falsified our own pre-registered statistic before it was ever applied to the proband.** The
chromosome-wide signed mean is diluted by a realised factor of 27 by those segments; its limit of
detection is **25–58%**, *worse than the 14% our submitted report already claims*. Amendment 1
replaced it with the orientation-invariant Ψ = Σ_s w_s (φ_s² − v_s), in which each segment contributes
Δ² regardless of how it is oriented.

Amendment 2 fixed the window at **125 sites** by minimising the calibrated limit on public data. The
sweep has a clean minimum and it lands on the analytic optimum 1/(switch rate) = 123 — an agreement
that is how a coding error in an earlier version of the sweep was caught, in which the attenuation
cancelled itself and made ever-larger windows look monotonically better.

## 3. The calibrated limit of detection

Monte Carlo on GPU, 40,000 null replicates per cell, with the measured switch process and the
empirical segment-size distribution. The null of Ψ is a weighted sum of chi-squares with very unequal
weights, where the normal approximation is unreliable in the tail.

| Overdispersion κ | LOD (fraction of cells) |
|---|---|
| 1 | 1.46% |
| **2 (central)** | **2.07%** |
| 4 | 2.95% |

Against the 14% we published, that is a **6.8-fold improvement**, and it places the achievable limit
at the upper edge of the 1–2% per chromosome that variegation implies.

## 4. The result that does not depend on any of that

A perfectly balanced variegated mixture — a fraction *g* of cells gaining homologue A, an equal
fraction gaining B, matched losses of each — has mean copy number **exactly 2** and mean allele
fraction **exactly 0.5**, by symmetry. Simulated under identical conditions:

| Architecture | f = 2% | f = 5% | f = 10% | f = 20% | f = 40% |
|---|---|---|---|---|---|
| Directional gain of one homologue | 100% | 100% | 100% | 100% | 100% |
| **Balanced variegation** | **0.1%** | **0.1%** | **0.1%** | **0.1%** | **0.2%** |

**0.1–0.2% is the false-positive rate.** With 40% of cells aneuploid, the signal is exactly zero. This
is not low power; it is **non-identifiability** — two biologically distinct cell populations produce
the same observable distribution. No depth and no statistic can separate them from bulk DNA.

## 5. The proband

Ψ over 125-site windows, all 22 autosomes, expressed as the excess over the binomial expectation.

| | |
|---|---|
| Excess over binomial, median | **2.27×** — i.e. the empirically measured overdispersion is κ ≈ 2.3 |
| Range across chromosomes | 1.78× (chr8) to 3.57× (chr17) |
| Highest robust z-score | **chr17, z = +2.88** — below the |z| = 3 threshold |
| Next four | chr6 (+2.72), chr7 (+2.64), chr9 (+2.60), chr2 (+2.29) |

**No chromosome is separated from the others.** The values form a continuous gradient, which is what a
global nuisance term looks like, not what a mosaic trisomy of one chromosome looks like — that would
put a single chromosome far above a tight cluster.

**⚠️ We wrote "the excess is global, and it cannot be mosaicism". That is withdrawn.** It converts a
variance into a mean shift: Ψ is raised both by a directional clone and by extra window-scale
variance, and we back-solved the excess as though only the first were possible. What the *secondary*
statistic supports, and this stands, is narrower: the chromosome-wide signed mean reaches at most
+0.0018 (chr17), so there is no evidence of a **directional** preferred-homologue clone.

**And the pre-registered test fires on all 22 autosomes** at every overdispersion setting (thresholds
5.58e-6, 1.12e-5, 2.23e-5 for κ = 1, 2, 4). That is not 22 mosaic events; it is a null model that does
not describe these data. Until the external control says what a healthy genome does under the same
pipeline, no detection or non-detection can be claimed.

**The pre-declared confound exclusions did not have to be invoked.** None of the therapy-related
clonal lesions is elevated: chr5 (1.92×), chr7 (3.46×), chr8 (1.78×), chr13 (2.27×), chr20 (1.89×).
chr7 is high but does not stand out from chr17, chr6 and chr9, which are not in the canon.

**Conclusion, in the form it goes in the report:**

> In the sequenced specimen, no chromosome-specific mosaic whole-chromosome imbalance is detected at a
> calibrated limit of **~2.2% of cells** (κ = 2.3 measured in these data), against the ~14% our earlier
> analysis could reach. The residual signal is a global overdispersion of 2.3× the binomial
> expectation, shared by all 22 autosomes, which is not interpretable as aneuploidy. And for the
> architecture that defines the disease — variegated gains and losses balanced across cells and
> homologues — bulk sequencing is not merely insensitive but **non-identifiable**: the expected
> observation is exactly that of a disomic genome, at any cell fraction and any depth.

## 6. What this changes in the submitted reports

- The mosaicism section's "~14%" is replaced by the measured **2.1%** limit and its calibration.
- The claim that bulk WGS cannot see MVA is **strengthened and given a proof**, not merely a limit.
- The sentence "only the VCF was available, with no BAM, so no GC-LOESS normalisation was possible" is
  wrong twice over: the challenge distributes the raw reads, and the analysis that mattered did not
  need them.

## 7. Limitations, stated plainly

- **The global 2.3× overdispersion is uncontrolled.** It is correlated at the ~200 kb window scale and
  we cannot say from the VCF alone whether it is technical (mapping and reference bias) or biological.
  Separating it requires a healthy genome processed identically from reads, which is the read-level
  stage now in progress. Until then the limit above is a *first-order* limit.
- **The AD values come from the organisers' GATK 4.2.4.0 call set**, not from a pileup we control.
- **Depth at variant sites was not used** as a dosage companion; the unbiased version needs alignments.
- **One specimen, one tissue, one time point.** Every negative statement reads *"not detectable in the
  sequenced specimen"* and never *"absent in the child"*: mosaicism in MVA varies by tissue.
- **Ψ measures aggregate dosage imbalance, not cellular heterogeneity.** No number from it can be
  reported as a percentage of aneuploid cells.

## 8. A data-integrity failure worth recording

Two panel files, chr17 and chr19, downloaded truncated (417 of 862 MB, 256 of 718 MB) while competing
for bandwidth. **They produced no error** — Beagle silently phased against a partial panel. chr17
yielded 25,829 sites instead of 57,063 and chr19 16,052 instead of 48,558. Found by checking every
file against its remote size, not by any tool complaining. All 22 are now byte-complete and both
chromosomes were re-derived and re-phased.

## Reproduce

```
mosaico/PREREGISTRO.md     diseño, enmiendas 1 y 2
mosaico/00_sitios.sh       sitios retenidos por la regla pre-registrada
mosaico/02_switch.py       fase verdadera del trío GIAB
mosaico/03_medir_switch.py tasa de switch medida
mosaico/04_lod.py          LOD analítico
mosaico/05_mc_gpu.py       LOD por Monte Carlo en GPU
mosaico/06_ventana.py      elección de la ventana en datos públicos
mosaico/07_probando.py     estadístico del probando
```
