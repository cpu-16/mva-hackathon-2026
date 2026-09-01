# The VUS cannot be resolved from databases, and we can say by how much

**Team: ciberpty** · 2026-09-01 · ClinVar snapshot of 2026-08-28, AlphaFold AF-O60566-F1-v6.

**This is a census and a structural measurement, not a hypothesis test.** It carries no
pre-registration because there is no decision rule to fix in advance — it counts what a database
holds on a given date and measures a property of a published structure. What it carries instead is
the exact snapshot, the region and the command, so that anyone can reproduce or refute the counts.

---

## 1. Why we ran it, and what we did *not* do

The Track 1 answer rests on two alleles: a nonsense that ClinVar calls pathogenic, and
**p.Asn1002Lys, a missense with no ClinVar record and no functional assay**. That second allele is
the weakest link in the diagnosis, and the obvious move is to throw a pathogenicity predictor at it.

Two reviewers had already killed that move: *"isolated AlphaMissense/SIFT/PolyPhen prediction without
calibration"* was on the do-not-do list. The right version is to **calibrate the predictor against
variants of the same gene that are already classified**, and then place ours on that calibrated
scale. That is what gene-specific evidence calibration is for.

**We went to build that calibration set and it does not exist.** That absence is the result.

## 2. The census: BUB1B missense are 95% unresolved, and the gene has one classified positive

`bcftools view -r 15:40160000-40280000` on the ClinVar 2026-08-28 release, restricted to
`GENEINFO=BUB1B`:

| | count |
|---|---:|
| ClinVar records at the locus | 2,471 |
| **Missense** | **1,497** |
|   — Pathogenic or Likely pathogenic | **1** |
|   — Benign or Likely benign | 35 |
|   — **Uncertain significance** | **1,426 (95.3%)** |
| Loss of function (nonsense, frameshift, splice) | 94 |
|   — Pathogenic or Likely pathogenic | **82** |

The single missense P/LP is ClinVar `2503511`, Likely pathogenic, submitted by **one** submitter at
one star.

**A predictor cannot be calibrated on one positive.** Any threshold, any ROC, any likelihood ratio
for this gene would rest on a single one-star record. So the honest output is not a calibrated score
for our variant — it is the statement that **the calibration set does not exist**, with the number
attached.

**And the contrast is the interesting part.** This gene's clinical evidence is built almost entirely
on loss of function: 82 P/LP truncating variants against 1 P/LP missense, a ratio of 82:1. That is
consistent with the mechanism — MVA1 is a recessive loss-of-function disease — and it explains why
the child's nonsense allele classifies cleanly while the missense does not. **It also means the base
rate for a BUB1B missense reaching P/LP in ClinVar is 1 in 1,497, or 0.07%.** Waiting for the
database to resolve this allele is waiting for an event that has happened once in the gene's history.

## 3. The structure, which does say something

The AlphaFold model is high confidence exactly where the variant sits, so the criterion we had set
in advance for abandoning structural work — *mean pLDDT below 70 across 766–1050* — is not met:

| Region | mean pLDDT |
|---|---:|
| Kinase domain, 766–1050 | **81.9** |
| Neighbourhood 992–1012 | **91.5** |
| **Asn1002 itself** | **91.1** |
| Whole protein | 63.6 |

Measured on that model with Shrake–Rupley solvent accessibility (Tien 2013 maxima):

- **Asn1002 is buried.** Relative solvent accessibility **0.162**, below the conventional 0.25 cutoff.
- **Its environment is hydrophobic.** Ten residues lie within 5 Å; the closest are **Leu1001,
  Ala1003, Trp978, Val998, Ile1000, Phe977**.
- The substitution is **Asn → Lys**: a longer side chain carrying a **positive charge**, placed in a
  buried hydrophobic pocket.
- For comparison, **Leu737** — where the nonsense truncates — has RSA 0.084 and the truncation
  removes **313 residues**, which matches the figure already in the report.

**What that is worth, stated precisely.** Burying a charge in a hydrophobic pocket is a recognised
destabilising substitution class. This is **evidence about the substitution, not a classification**:
we did not compute a ΔΔG, we did not run a predictor, and we are not assigning ACMG PP3. A buried
charged residue can be tolerated, and a single structure cannot tell us whether this one is.

## 4. What this changes

1. **It justifies the parental segregation request with a number.** The clinical order in
   `clinico/PARENTAL_SEGREGATION_ORDER.md` argues that segregation is the cheapest route to
   resolving this variant. The census says it is also the *only practical* route: the database path
   has a 0.07% base rate in this gene, and there is no calibration set to build a computational one.
2. **It explains the asymmetry in our own Track 1 evidence.** The nonsense carries the diagnosis
   because loss-of-function is the only variant class this gene resolves. That is a property of the
   evidence base, not of our pipeline.
3. **It closes item 5 of the project backlog** — "calibrate the VUS" — with a negative that is
   informative, rather than leaving it open or producing an uncalibrated score.

## 5. Limits, and one that matters more than the others

- **A census measures the database, not the biology.** ClinVar contains what has been submitted.
  Missense variants in BUB1B may be under-tested, under-submitted, or classified in laboratories that
  do not deposit. **Absence of classified positives is not evidence that pathogenic missense variants
  are rare in this gene.**
- **The literature disagrees with the database, and that is the point.** Sieben et al. modelled the
  human MVA missense **BUBR1^L1012P** in mice (PMID 31738183) — a missense allele causal enough to
  build a disease model on. We could not locate it in this ClinVar snapshot; our search by protein
  annotation returned nothing because this VCF does not carry `p.` notation in its INFO field, so we
  report that as **not found by our query**, not as absent. Either way, characterised missense
  alleles exist in the literature that the database does not classify.
- **Consequence annotation is transcript-dependent.** Records in the same window are labelled
  `missense_variant` or `intron_variant` depending on the transcript; we counted a record as missense
  if any transcript called it so.
- **Solvent accessibility comes from a predicted model**, not a crystal structure, and from a single
  conformation of a protein that is part of a dynamic complex.
- **One structure is not a stability calculation.** The honest ceiling of §3 is "this substitution is
  of a class that is often destabilising, in a position the model resolves confidently".

## 6. Reproduce

    vus/01_censo.py                    the census and the structural measurement
    vus/censo.json                     every number
    vus/AF-O60566-F1-model_v6.pdb      the structure, from alphafold.ebi.ac.uk
    pipeline/resources/clinvar.vcf.gz  ClinVar, 2026-08-28 snapshot

CPU only, no patient data, no GPU.
