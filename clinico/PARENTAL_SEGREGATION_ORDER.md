# Laboratory request — parental segregation of two *BUB1B* variants

**Prepared by: team ciberpty** · Rare Disease, Real Kid: MVA Hackathon 2026 · 2026-09-01
Companion to `entrega/methods_track1.md` (Track 1) and `track2/REPORT_track2_EN.md` (Track 2).

---

> **What this document is.** A one-page request that a treating clinician can adapt, sign and send to
> a diagnostic laboratory. It carries the exact loci, verified primer sequences and a pre-written
> interpretation table, so that the decision does not have to be reconstructed by whoever reads the
> genome report next.
>
> **What it is not.** It is **not a signed clinical order and not medical advice.** It was written by
> an analysis team with no access to the patient, no knowledge of the child's current age, and no
> role in his care. Every element below is a proposal to a clinical genetics service, which owns the
> decision, the consent process and the interpretation.

---

## 1. The question

The proband is heterozygous for two rare *BUB1B* variants (NM_001211.6, MANE transcript
ENST00000287598.11). **Whether they sit on opposite chromosomes is not known, and it cannot be
determined from the data available.**

| | Variant | Consequence | Position (GRCh38) | Exon |
|---|---|---|---|---|
| **A** | `c.2210T>G` p.(Leu737Ter) | stop_gained | chr15:40,209,701 T>G | 17 / 23 |
| **B** | `c.3006T>G` p.(Asn1002Lys) | missense, VUS | chr15:40,220,612 T>G | 23 / 23 |

The MVA1 diagnosis requires them to be **in *trans*** — one on each parental chromosome. In *cis*,
one *BUB1B* copy remains intact and the recessive diagnosis does not hold.

**Why this cannot be answered from the existing genome.** We measured it rather than assuming it.
The two variants are **10,911 bp apart** and the caller emitted no phase tag for either. Inside that
interval the child carries exactly three heterozygous sites — the two above plus chr15:40,216,470 —
and **all three are absent from the 1000 Genomes 30× reference panel** (3,202 individuals), so
statistical phasing has no marker to link them; a Beagle 5.5 run keeps 1,391 of 1,452 window variants
and drops precisely those three. Expected copy counts in 6,404 haplotypes are 0.64 and **0.006**, so
a larger panel does not fix it: roughly 10⁶ haplotypes would be needed. Two heterozygous variants in
a singleton are a priori 50/50 *cis* or *trans*, and rarity does not phase them.

**Testing the parents is the cheapest experiment in the entire project, and the only one that can
confirm the diagnosis.**

## 2. Why it matters — three consequences, not one

1. **It confirms or refutes the diagnosis.** A *cis* result means the reported compound
   heterozygosity is wrong and the search must reopen — a second hit could be a deletion, a deep
   intronic variant or uniparental disomy, none of which the current analysis would have seen.
2. **It informs any future pregnancy.** If both parents are carriers, recurrence risk is 25% and
   prenatal or preimplantation testing becomes available to them. That is a decision they cannot
   make without this result.
3. **It addresses a finding already in the clinical record.** The referral lists recurrent
   spontaneous abortion (HP:0200067) as parental history. A 2026 study of two unrelated families
   with unexplained recurrent pregnancy loss found novel heterozygous *BUB1B* variants with
   **significantly elevated premature chromatid separation in the carriers' lymphocytes**
   (PMID 42434306). Those variants were classified VUS and the cohort is two families, so this is a
   hypothesis and not a finding about this family — but it is cheap to test and it is squarely in
   the parents' own interest.

## 3. What is requested

### Test A — targeted Sanger sequencing of both parents, both loci

Bidirectional Sanger sequencing of two amplicons in **each** parent, plus the proband as a positive
control on the same run. Sanger rather than a repeat trio genome: it answers exactly this question,
in days rather than weeks, at a fraction of the cost, and it is the format a diagnostic laboratory
can report clinically.

| | Amplicon 1 — variant A | Amplicon 2 — variant B |
|---|---|---|
| Target | `c.2210T>G` p.(Leu737Ter), exon 17 | `c.3006T>G` p.(Asn1002Lys), exon 23 |
| Amplicon (GRCh38) | chr15:40,209,523–40,210,275 | chr15:40,220,394–40,220,743 |
| Product size | 753 bp | 350 bp |
| Forward primer | `AGTGCTGACTGTGTAATCTTGA` | `TGTAGTTCTTCCCTGGGCTTTC` |
| Tm / GC | 57.4 °C / 40.9% | 60.0 °C / 50.0% |
| Reverse primer | `GGACAGTTATTGCTCCAATCCG` | `GCCCCAGGACTAGTTAACTTCC` |
| Tm / GC | 59.4 °C / 50.0% | 60.1 °C / 54.5% |
| Read margin to the variant | 156 nt from F, 574 nt from R | 196 nt from F, 131 nt from R |

**Suggested conditions.** Annealing 57 °C, standard hot-start polymerase, both amplicons compatible
in the same run. Sequence in both directions; the margins above put the variant inside the clean
window of at least one read in either direction.

**How these primers were constrained, because two of the constraints are the failure modes of this
particular test:**

- **No primer overlaps a common SNP.** Every 1000 Genomes SNV with AF ≥ 0.005 in a 2 kb window was
  excluded from the primer regions (6 in window 1, 7 in window 2). A mismatch under a primer causes
  allele drop-out, and in a segregation test allele drop-out reads as *"this parent does not carry
  it"* — a false negative that would be reported as a result.
- **No primer falls in a repeat.** The *c.2210* locus is flanked by an **AluY 272 bp upstream and a
  HAL1 LINE 600 bp downstream**. The first primer pair the design software returned sat inside that
  AluY and has ~100 exact copies in GRCh38. RepeatMasker intervals were excluded and every candidate
  re-checked.
- **Single-copy verified, not assumed.** All four primers were counted against the **entire GRCh38
  assembly** including alt and random contigs: each occurs **exactly once**, at the expected chr15
  position, with zero copies elsewhere.

**The laboratory should still run its own in-silico PCR and BLAT before ordering synthesis.** Our
check counts *exact* matches; a primer unique by exact match can still have paralogues at one or two
mismatches, which only an alignment-based check will find.

### Test B — premature chromatid separation in parental lymphocytes

Metaphase spreads from peripheral blood of both parents, PCS scored by G-banding, with centromere
FISH if available — the assay used in PMID 42434306. Requested **alongside** genetic counselling,
not instead of it. It tests whether the miscarriage history is itself part of a carrier phenotype.

**This is a hypothesis-generating test on a two-family basis and should be consented as such.** A
normal PCS rate does not exclude carrier status, and an elevated rate in a heterozygote is not a
diagnosis.

## 4. Interpretation — written before the result

| Result | Phase | What it means | What follows |
|---|---|---|---|
| One parent carries **A**, the other carries **B** | ***trans*** | **The MVA1 diagnosis is confirmed.** Both parents are carriers | Recurrence risk 25%; offer counselling and reproductive options; the Track 2 report's premise holds |
| One parent carries **both** A and B | ***cis*** | **The compound-heterozygous interpretation is wrong.** One *BUB1B* copy is intact | Reopen the search: CNV/deletion analysis, deep intronic variants, uniparental disomy of 15q. The Track 1 answer must be revised |
| One parent carries one variant; **neither** carries the other | Not resolved | The second variant is *de novo* **or** the parent is a germline mosaic. Segregation alone cannot place a *de novo* allele on either chromosome | Long-read sequencing of the child, or allele-specific RT-PCR on patient RNA, is then the only route to phase |
| **Neither** parent carries **either** variant | Not resolved | Both *de novo* — rare — or a parental relationship different from the one recorded | Handle per laboratory policy; this possibility must be covered in consent **before** samples are taken |
| A parent shows a low-level or mixed trace | Possible mosaicism | Sanger has limited sensitivity for mosaicism | Deep amplicon sequencing of that parent before any recurrence-risk figure is quoted |

**Note on the second row, because it is the one that would hurt.** Our own retrieval pipeline is
blind to phase: in a controlled test, two pathogenic nonsense alleles declared on the *same*
chromosome were still called compound heterozygous, still classified pathogenic and still ranked
first, at a score difference of 0.0034. **Nothing in the computational analysis would have flagged a
*cis* configuration.** The recessive interpretation was supplied by the analysts, not demonstrated
by the software. That is precisely why this test is worth running.

## 5. What is deliberately **not** requested

- **A repeat trio whole genome.** It answers the same question more slowly and more expensively, and
  it would return incidental findings that require their own consent process.
- **Long-read sequencing, for now.** It is the right answer *only* if the third or fourth row above
  occurs. Requesting it first spends the budget before knowing whether it is needed.
- **Any drug, and any change to treatment.** No medicine is proposed for this child today; see
  Track 2 §4. This request changes a diagnosis and a recurrence risk, not a prescription.
- **Testing of the child's siblings, if any.** That is a separate decision with its own consent
  considerations, and it should follow the parental result rather than precede it.

## 6. Provenance

Primer design: `clinico/01_primers.py` (primer3, GRCh38, 1000 Genomes 30× panel, UCSC RepeatMasker).
Single-copy verification: `clinico/02_especificidad.py` (exhaustive exact-match count over GRCh38).
Phasing analysis: `fase/RESULTADO.md`. Phase-blindness of the pipeline: `replay/PILOTO_FASE.md`.

**Source cited above:** Wei TY, et al. Functional and clinical evidence for two novel heterozygous
*BUB1B* variants and their value in precision genetic counseling for recurrent pregnancy loss.
*Front Endocrinol* 2026. PMID 42434306.
