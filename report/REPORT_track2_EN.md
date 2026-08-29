# Track 2 — Drug Repurposing for MVA1 (BUB1B compound heterozygosity)

**Rare Disease, Real Kid: MVA Hackathon 2026**

---

## Executive summary

We will state our conclusion before our argument, because it is not the conclusion this track invites.

**No approved medicine currently has defensible evidence for treating MVA1.** The strongest
preclinical signals in aneuploid cells come from AICAR and 17-AAG, and neither is a marketed drug.
Their approved stand-ins — metformin and hydroxychloroquine — are extrapolations, not findings. Any
report that presents one of them as a treatment for this child is overstating the evidence.

So we changed the question. Instead of asking *"which drug do we give this child?"*, we asked
**"what is missing before that question can be answered at all?"** — and we deliver the three pieces
that are missing:

1. **What is actionable today without any drug.** Structured tumour surveillance and individualised
   chemotherapy planning are the interventions that measurably change this child's prognosis now.
2. **A quantified limit on what the hackathon data can measure.** Every candidate therapy for MVA
   needs *aneuploidy burden* as an endpoint. The correct assays already exist and are standard — we
   do not claim to have invented them. What we contribute is the number: using this child's own
   genome we compute the detection limit of bulk WGS for this purpose (~12–15% clonal), show that
   variegated mosaicism falls 6–14× below it, and demonstrate that **more coverage does not fix
   it**.
3. **An advancement criterion** that disqualifies a whole class of superficially attractive
   candidates: a compound that kills aneuploid cells but raises mis-segregation among the survivors
   makes the disease worse.

The candidate compounds we do rank are explicitly framed as **bench candidates, never as bedside
recommendations**.

---

## 1. Mechanism: what these two alleles break

The proband is compound heterozygous in `BUB1B` (NM_001211.6): **c.2210T>G, p.Leu737Ter** (nonsense;
ClinVar Pathogenic/Likely pathogenic; gnomAD AF 3×10⁻⁵) and **c.3006T>G, p.Asn1002Lys** (missense;
absent from gnomAD). This is MVA1 (OMIM 257300), autosomal recessive.

BubR1 is a core component of the mitotic checkpoint complex (MCC) and of kinetochore–microtubule
attachment control. Its 1,050-residue architecture places the two variants as follows:

```
aa 1                                                                    1050
   | KEN1 |--- N-terminal TPR ---| KEN2/ABBA | GLEBS/Bub3 |-- KARD --|~~| pseudokinase |
     ~26       ~50–204              ~304       ~392–426     ~665–682       ~757–1044
                                                                   ↑            ↑
                                                               Leu737Ter    Asn1002Lys
```

**p.Leu737Ter** truncates in the linker immediately N-terminal to the pseudokinase fold (UniProt/Pfam
place the kinase domain at ~757–1044), removing the entire domain — roughly 313 residues. Note the
schematic above gives approximate literature intervals, not clinical coordinates.

It is worth stating how close this is to a characterised allele: the human `2211insGTTA` allele
produces an unstable X753 truncation, only 16 residues downstream. This is not a "related" model —
it is very nearly the same truncation (PMID 31738183).
The N-terminal MCC-forming region, the GLEBS/Bub3 motif and the KARD motif remain in sequence, but a
truncated protein should not be assumed stable — in that model, allelic combinations produced effects
not explained by protein quantity or aneuploidy rate alone.

*Our inference, not a verified fact:* a premature stop this far upstream of the final exon junction
would typically trigger nonsense-mediated decay. Without patient RNA we cannot say whether the
transcript is degraded or escapes to yield an unstable ~736-residue protein. This must be measured,
not deduced.

**p.Asn1002Lys** falls inside the C-lobe of the pseudokinase domain, outside KEN, TPR, GLEBS and
KARD. It introduces a positive charge and could affect folding, stability or C-terminal interfaces.
**No published functional assay of this substitution exists**, which makes it an experimental
question rather than a characterised allele.

The functional consequence at the cellular level is well documented in MVA patient fibroblasts:
reduced BubR1 levels, a weakened spindle assembly checkpoint, and chromosome alignment defects
(PMID 20516114). The KARD motif recruits PP2A-B56 to antagonise Aurora B and stabilise
kinetochore–microtubule attachments; its disruption causes congression defects
(Xu et al., *Biol Open* 2013, PMID 23789096; Kruse et al., *J Cell Sci* 2013, PMID 23345399).

**Genotype–phenotype, honestly stated:** the recurrent pattern in viable MVA1 is one truncating
allele plus one amino-acid substitution, often C-terminal (PMID 20516114). Homozygous `Bub1b`
knockout is embryonic lethal in mouse, while hypomorphs age prematurely and accumulate aneuploidy
(PMID 15208629). But there is **no validated correlation** between these two specific alleles — or
between "truncating + missense" generally — and differential risk of embryonal rhabdomyosarcoma
versus Wilms tumour. The child's rhabdomyosarcoma is consistent with the MVA spectrum
(PMID 16182441); it does not by itself establish the function of p.Asn1002Lys.

---

## 2. Piece one — what is actionable today, without a drug

The intervention with the strongest evidence base is not a molecule.

### Tumour surveillance

MVA/BUB1B predisposes principally to early embryonal tumours: embryonal rhabdomyosarcoma, Wilms
tumour, and leukaemia (PMID 16182441). UK surveillance recommendations covering
children with mosaic aneuploidy or BUB1B variants propose **renal ultrasound every 3–4 months from
diagnosis until age 5**, because nearly all reported Wilms tumours in those series occurred before
that age (PMID 16857697). Contemporary guidance for genomic instability syndromes emphasises
individualised planning, minimising ionising radiation, and management in expert centres
(DOI 10.1158/1078-0432.CCR-24-1101).

Our pragmatic proposal — the extension beyond published guidance is flagged as our inference:

| Period | Surveillance | Frequency and rationale |
|---|---|---|
| Diagnosis → age 7 | Full abdominal ultrasound (both kidneys, liver, retroperitoneum, pelvis) | Every 3 months. We extend cautiously from 5 to 7 years; **this extension is not validated specifically for BUB1B** |
| → age 10 | Full paediatric/oncological examination: abdomen, nodes, head and neck, orbit, skin, genitalia, soft tissues | Every 3 months to age 7, then 6-monthly to 10. Catches superficial or symptomatic ERMS that renal ultrasound cannot |
| Post-ERMS | Relapse follow-up per tumour protocol | Coordinate with the surveillance calendar to avoid duplicate imaging |
| Through childhood | Full blood count with differential | 6-monthly is reasonable given reported leukaemia, but **there is no evidence of benefit** and no validated MVA protocol. Sooner if fever, pallor, bleeding, adenopathy or infection |
| Lifelong | Family education and annual predisposition-clinic review | Urgent review for mass, haematuria, abdominal distension, persistent bone or muscle pain, neurological deficit, bleeding or weight loss |

We do **not** propose serial AFP, repeated CT, PET-CT, or routine whole-body MRI in an asymptomatic
child: no benefit has been demonstrated in MVA, and sedation, false positives, cost and — for CT and
PET — radiation all weigh against it in a cancer-predisposition syndrome.

### Chemotherapy planning: a relative contraindication, precisely stated

Vincristine, taxanes and other spindle poisons depend on a competent mitotic response to arrest cells
with disrupted microtubules. With reduced BubR1 the arrest is less robust: some cells slip through
mitosis, die unpredictably, or generate further aneuploidy. This creates opposing risks — excess
toxicity in vulnerable normal tissue, and altered tumour response.

Direct clinical evidence is sparse but pertinent: an infant with ERMS and PCS/MVA was treated with
**reduced-intensity** chemotherapy (vincristine, dactinomycin, cyclophosphamide) (PMID 31184400).
That is a single case, not a guideline and not a safety estimate.

**The precise formulation matters.** This is a high-level precaution and a *relative*
contraindication, weighed against probability of cure. Writing "vincristine is contraindicated" would
be wrong and potentially harmful: it could deny a child a curative therapy. For any relapse or second
tumour, the correct action is discussion in a cancer-predisposition and clinical-pharmacology
committee, individualised starting doses, escalation by tolerance, close haematological, neurological
and renal monitoring, and preference for local control or non-mitotic agents where oncologically
equivalent.

---

## 3. Piece two — a quantified limit on the hackathon's own data

Any therapy for MVA needs a measurable endpoint, and the natural one is **aneuploidy burden**. So we
asked whether the data this hackathon provides can supply it.

**We are not proposing a new assay.** The correct endpoints already exist and are standard: metaphase
karyotyping with premature chromatid separation scoring is the diagnostic criterion for MVA; the
micronucleus assay is an international standard for mis-segregation (OECD TG 487); and low-coverage
single-cell DNA sequencing has been established for aneuploidy since Knouse et al. 2014
(PMID 25197050), which showed precisely that bulk averaging erases what single cells reveal.

What we contribute is **the number**: how far short the bulk shortcut falls, computed on this
patient's genome.

### Method and its limits, stated first

Analysis used **the VCF only** — no BAM or FASTQ were available to us, so no GC-LOESS normalisation
or read-level dosage was possible. Four analyses were run, of which **three are refinements of the
same B-allele-frequency statistic and one (depth-based dosage) is orthogonal**. They are not four
independent tests.

In a trisomy, heterozygous sites split symmetrically towards `1/(2+f)` and `(1+f)/(2+f)`, so **the
mean BAF does not move** — the dispersion does. The correct statistic is therefore the mean
|BAF − 0.5|.

### The detection limit

Simulating mean |BAF − 0.5| at DP = 44 across 40,000 sites per condition:

| Cells carrying a trisomy | Mean deviation | Effect over baseline |
|---|---|---|
| 0% | 0.0601 | — |
| 5% | 0.0603 | +0.0001 |
| 10% | 0.0629 | +0.0027 |
| **14%** | 0.0656 | **+0.0055** |
| 20% | 0.0704 | +0.0103 |
| 30% | 0.0808 | +0.0206 |

The noise floor is not statistical but **systematic between chromosomes**: in these data the measured
deviation at fixed depth (DP 40–48) ranges 0.0532–0.0581 across chromosomes, a spread of ≈0.005
attributable to GC content, mappability and segmental duplications.

**Practical detection limit of this VCF: a clonal whole-chromosome trisomy present in ~12–15% of
cells.**

One point deserves emphasis because it is counter-intuitive: **coverage is not the bottleneck.**
Poisson error when averaging an entire chromosome at 44× is on the order of 0.03%. Sequencing at 200×
would barely move the limit, because what constrains it is library bias, not read sampling.

### Why variegation falls below that limit

As an **illustrative bound, not a measurement of this child**: if 30% of cells were aneuploid — the
order of magnitude of the classical diagnostic criterion, not a figure from this patient — and each
cell altered a different chromosome across 22 autosomes, each chromosome would be affected in ~1.4%
of cells. With *k* altered chromosomes per aneuploid cell that becomes `0.30 × k / 22`, and gains and
losses of the same chromosome **cancel in bulk**. Even on favourable assumptions the per-chromosome
burden sits **6–14× below the ~12–15% limit**.

And no technical improvement resolves this: **averaging over millions of cells erases variegation by
construction.** Better chemistry raises sensitivity for a *clonal* aneuploidy, not a *variegated* one.

**A further limitation that no sequencing depth addresses:** the cytogenetic hallmark of MVA is
**premature chromatid separation**, a metaphase phenomenon that leaves no trace whatsoever in
extracted DNA sequence. Additionally, blood from a patient treated for ERMS may carry a very
different aneuploidy burden than a metaphase lymphocyte culture.

### What we actually observed

| Analysis | Result |
|---|---|
| BAF per chromosome (2.27 M het SNVs) | Apparent signal on chr20, 21, 22, X |
| Same, at fixed depth (DP 40–48) | chr21 **disappears** — a coverage artefact (mean DP 50.7). chr20 and chr22 persist |
| Spatial profile, 5 Mb windows | chr20 and chr22 have **normal medians** (13.1%, 14.0%); the high windows fall on the centromere and on **22q11**, the best-characterised segmental duplication region in the genome |
| Depth-based dosage | Apparent gain of +2.9% to +7.0% on chr16, 17, 19, 20, 21, 22 |

**On the dosage signal we are deliberately incomplete.** GC bias explains chr19, 22, 17 and 16, which
are among the most GC-rich chromosomes. It does **not** explain chr21 — the largest deviation (+7.0%)
and one of the most GC-poor chromosomes — nor chr20; acrocentric and low-complexity mapping is the
more plausible cause there. Our measured GC–coverage correlation was **r = 0.43** (n = 22), estimated
from only 2–3 windows of 200 kb per chromosome: too sparse to characterise a chromosome. **This is an
insufficient measurement, not an established explanation.** Resolving it would require GC-LOESS
normalisation on BAMs we do not have.

What does hold: the dosage signal is **not corroborated by the more robust indicator**. BAF is an
internal per-site ratio that cancels coverage bias; dosage compares absolute depths and inherits
every library artefact. Where they disagree, the burden of proof lies with dosage.

### The consequence for Track 2

We have **not** shown this child lacks mosaic aneuploidy — he has it by diagnostic definition. We have
shown that **this assay cannot resolve it at the level the disease produces it**.

Therefore: **no therapeutic proposal whose endpoint is "reduced aneuploidy burden" can be evaluated
with the hackathon data**, and any compound screen must measure per-cell mis-segregation rather than
substitute bulk sequencing for it. That is the constraint the next section turns into a filter.

## 4. Piece three — the advancement criterion

A candidate advances only if it satisfies all of the following:

1. **≥3-fold window** between compound effect on aneuploid and corrected/WT cells, in **≥2 isogenic
   backgrounds**.
2. **Reproduced in the patient's own fibroblasts**, not only in engineered lines.
3. **Does not increase micronuclei or mis-segregation among surviving cells.**
4. Effective at **clinically achievable exposures**.
5. For mTOR inhibitors additionally: elevated baseline mTORC1 and demonstrated reversal of that
   biomarker.
6. Replication by an independent laboratory before any animal model.

**Criterion 3 is the one that matters most, and the one most easily missed.** A compound that
preferentially kills aneuploid cells while raising chromosome mis-segregation in the survivors is not
a therapy — it is a selection pressure that worsens the underlying defect. Any screen that measures
only viability will score such a compound as a hit. Publishing this as a hard filter is, in our view,
more useful to the field than any of the individual candidates below.

---

## 5. Candidate compounds, ranked by evidence strength

"Approved" means the active substance holds at least one marketing authorisation. **None is approved
for MVA1 or for preventing its tumours.** All uses discussed would be off-label and experimental.

| Compound | Hypothesis | Evidence | Paediatric context | Risks specific to this child | Strength |
|---|---|---|---|---|---|
| **Metformin** | Complex I inhibition raises AMP/activates AMPK, lowering mTORC1; an imperfect marketed stand-in for AICAR to exploit the energetic stress of aneuploid cells | AICAR was aneuploidy-selective (PMID 21315436). **No direct metformin evidence in MVA** | Labelled from age 10 in T2DM | Nephrocalcinosis and possible renal compromise raise lactic-acidosis concern; failure to thrive makes an energy-restricting agent unattractive | **Low–moderate, preclinical only** |
| **Hydroxychloroquine** | Lysosomal/autophagy inhibition; extrapolated from chloroquine, which sensitised trisomic MEFs alongside AICAR | The screen hit was **chloroquine**, not HCQ, and the differential was modest (PMID 21315436). A metformin+chloroquine phase Ib in IDH1-mutant tumours showed frequent progression and toxicity dropouts (PMID 34069550) | Extensive paediatric use in its licensed indications | Myopathy is especially undesirable alongside skeletal muscle atrophy; also retinopathy, QT effects | **Low, extrapolative** |
| **Everolimus** | mTORC1 inhibition; could modulate the mTORC1 hyperactivity associated with BubR1 allelic sarcopenia | Allelic model association only (PMID 31738183). No demonstrated intervention in human MVA | Clearest paediatric regulatory basis (TSC) and a paediatric formulation | Immunosuppression in a cancer survivor; stomatitis, pneumonitis, cytopenia; uncertain long-term growth effects | **Low, indirect** |
| **Sirolimus** | Same rationale, less paediatric support | Same indirect association | FDA paediatric transplant use from age 13 | As above, with less paediatric evidence in young children | **Very low–low** |

### Why metformin is the most defensible bench candidate — and still not a therapy

Tang et al. screened isogenic trisomic MEFs and found selective sensitivity to **AICAR**, 17-AAG and
chloroquine; AICAR induced p53-dependent apoptosis, and AICAR+17-AAG was more effective in CIN lines
than in near-euploid lines (PMID 21315436). **AICAR is not an approved medicine**, so it fails the
rules of this track.

Metformin is a marketed agent that also produces AMPK-mediated energetic stress, but it does not
reproduce AICAR cleanly — AICAR is additionally converted to ZMP and perturbs nucleotide metabolism.
We found no primary evidence that metformin reduces constitutional aneuploidy, restores BubR1
checkpoint function, or prevents ERMS or Wilms tumour. It therefore belongs in the *in vitro* panel
and nowhere else.

---

## 6. What we do not propose, and why

- **MPS1/TTK inhibitors, including reversine** — experimental tool compounds, not approved, and they
  directly weaken a checkpoint that is already insufficient. Expected to increase CIN.
- **Apcin, proTAME** — APC/C tool compounds, not marketed, no paediatric safety data.
- **DCZ0415** — experimental TRIP13 inhibitor; not approved and does not address BUB1B deficiency.
- **AICAR** — a genuine hit in the Tang screen, but not an approved medicine. Useful as an *in vitro*
  positive control, not as a candidate (PMID 21315436).
- **17-AAG / tanespimycin** — solid preclinical proteotoxic-stress rationale, but it never achieved
  marketing authorisation. Excluded by the rules.
- **Senolytics (dasatinib+quercetin, navitoclax, fisetin)** — the BubR1 senescence evidence comes from
  *genetic* clearance of p16^Ink4a+ cells via the INK-ATTAC transgene (PMID 22048312), which is not a
  transferable drug. No agent is approved with a senolytic indication. More importantly, **senescence
  is an anti-tumour barrier**: removing it in a cancer-predisposition syndrome could do harm.
- **Aurora B or PLK1 inhibitors** — may kill CIN tumours but aggravate the fundamental defect.
- **Any of the ranked candidates administered to the patient outside a trial** — approval for another
  indication does not bridge the gap between cell culture and a child. There is no validated
  biomarker, no MVA dose, and no demonstrated clinical benefit.

---

## 7. Proposed validation experiment

**Primary question:** does p.Leu737Ter reduce transcript and protein through NMD, and is
p.Asn1002Lys a C-terminal hypomorph that lowers BubR1/PP2A-B56 stability, weakening the checkpoint
and raising mis-segregation?

**Secondary, pharmacological:** are the resulting aneuploid cells selectively vulnerable to
energetic/autophagic stress, and does everolimus help only where mTORC1 is hyperactive?

**Design:**

1. **Material.** Early-passage patient dermal fibroblasts; two matched healthy controls; a known
   BUB1B/MVA control if obtainable. In parallel, CRISPR-engineer an isogenic diploid line to carry
   WT, Leu737Ter/+, Asn1002Lys/+ and the compound genotype; and separately correct each allele in
   patient cells. Use ≥3 independent clones plus an edited pool to guard against clonal artefacts.
2. **Allele fate.** Long-read RNA-seq or allele-specific RT-PCR to quantify mutant:WT ratio. Treat one
   replicate with an NMD inhibitor as an experimental reagent to test for transcript rescue.
   Quantitative western blot with N- and C-terminal antibodies: an N+/C− band supports truncation;
   loss of both supports NMD or instability.
3. **Molecular function.** Co-IP of BubR1–Bub3 and BubR1–B56; kinetochore immunofluorescence;
   p-S6 and p-4EBP1 for mTORC1. Under low-dose nocodazole, live imaging (H2B-mCherry/tubulin-GFP) for
   NEBD-to-anaphase timing and arrest maintenance; quantify misaligned chromosomes.
4. **Chromosomal fidelity.** 200 mitoses per condition scored for lagging chromosomes, bridges and
   micronuclei; FISH for 3–5 chromosomes; low-coverage scDNA-seq at baseline and after 20 passages.
5. **Causal rescue.** Reintroduce BUB1B-WT at near-endogenous expression — a weak promoter or safe
   knock-in, **not** massive overexpression. Correcting Asn1002Lys should restore stability and
   PP2A-B56 recruitment; correcting Leu737Ter should raise total protein. Convergent rescue
   establishes causality.
6. **Mini-screen of approved compounds.** Metformin, HCQ and everolimus at clinically achievable
   exposures, alone and as metformin+HCQ; 72 hours and 14 days. Read out viability, apoptosis,
   proliferation, SA-β-gal/p16/p21/SASP, p-AMPK/p-S6, and — critically — **mis-segregation rate**.
   Include chloroquine, AICAR and 17-AAG only as mechanistic controls, never as candidates.

**Falsifying result:** if correcting Asn1002Lys fails to rescue BubR1 or checkpoint function, or the
edited compound genotype is indistinguishable from WT, the specific hypomorph hypothesis is weakened.
If metformin or HCQ kills patient and control cells equally, or increases residual CIN, those
candidates are eliminated. This design is built to be able to fail, which is the point.

---

## 8. Scalability

None of the above is specific to this child:

- The **gene panel and rarity+impact filter** (BUB1B, CEP57, TRIP13, CENATAC, MAD1L1, MAD2L1BP,
  CEP192, BUB1, SMC5, TRIM37, CENPE) apply to any suspected MVA or PCS phenotype — MVA by CEP57
  (PMID 21552266) or TRIP13 (PMID 28553959).
- The **mosaicism artefact controls** (fixed-depth stratification, spatial windowing, GC awareness)
  apply to any attempt to detect mosaic aneuploidy from bulk sequencing, and would have prevented
  three false positives here.
- The **micronucleus → scDNA-seq endpoint** applies to mitotic CIN disorders — MVA and PCS
  syndromes. It does **not** transfer to Fanconi anaemia or Bloom syndrome, whose diagnostic assays
  are chromosome breakage under DEB/MMC and sister-chromatid exchange respectively; those measure a
  different lesion and should not be substituted.
- The **advancement criterion**, especially the mis-segregation clause, applies to any compound screen
  in a chromosomal instability background.

---

## 9. Limitations and open questions

- **Phase is not established.** No parental samples; the two variants lie ~11 kb apart, beyond
  read-backed phasing for short reads. The compound-heterozygous interpretation rests on allele
  rarity and known recessive inheritance. Parental testing would settle it.
- **p.Asn1002Lys has no published functional assay.** Its hypomorphic character is a hypothesis and
  the primary target of the proposed experiment.
- **No allele–tumour correlation exists** for these variants, and none should be inferred.
- **The GC-bias explanation for the dosage signal was verified only partially** (r = 0.43 across 22
  chromosomes), on a GC estimate sampled from 2–3 windows per chromosome — too sparse to characterise
  a whole chromosome. It is an insufficient measurement, not a refutation, and we report it as such.
- **Our surveillance extension from 5 to 7 years is a cautious proposal**, not validated consensus for
  BUB1B.
- **No searched database** (Open Targets, ChEMBL, CMap/LINCS, ClinicalTrials.gov) returned a
  therapeutic trial specific to MVA1. Absence of an interface result is not proof of absence.

---

## A closing note

The family of this child chose to publish their son's genome so that strangers might help. They will
read what comes back.

Promising a molecule without evidence would be the worst possible outcome of this hackathon: it would
not help the child, and it would erode exactly the trust that made the data available. Our candidates
go on the bench, not in the medicine cabinet. What we offer instead is the thing that has to exist
before any candidate can be honestly evaluated — a measurable endpoint, a filter that rejects
compounds which would make the disease worse, and a surveillance plan that helps this child now.

---

## References

1. Hanks S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in *BUB1B*. *Nat Genet* 2004. PMID 15475955
2. Suijkerbuijk SJE, et al. Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Res* 2010. PMID 20516114
3. Hanks S, et al. Childhood cancer predisposition in mosaic variegated aneuploidy. *Cancer Lett* 2006. PMID 16182441
4. Tang YC, et al. Identification of aneuploidy-selective antiproliferation compounds. *Cell* 2011. PMID 21315436 · DOI 10.1016/j.cell.2011.01.017
5. Baker DJ, et al. BubR1 insufficiency causes early onset of aging-associated phenotypes. *Nat Genet* 2004. PMID 15208629
6. Baker DJ, et al. Clearance of p16^Ink4a-positive senescent cells delays ageing-associated disorders. *Nature* 2011. PMID 22048312 · DOI 10.1038/nature10600
7. Sieben CJ, et al. BubR1 allelic effects drive phenotypic heterogeneity in mosaic variegated aneuploidy. *J Clin Invest* 2020. PMID 31738183 · DOI 10.1172/JCI126863
8. Nishitani-Isa M, et al. Embryonal rhabdomyosarcoma with PCS/MVA treated with reduced-intensity chemotherapy. *Pediatr Int* 2019. PMID 31184400 · DOI 10.1111/ped.13849
9. Scott RH, et al. Surveillance for Wilms tumour in at-risk children. *Arch Dis Child* 2006. PMID 16857697
10. Yost S, et al. Biallelic *TRIP13* mutations predispose to Wilms tumor and chromosome missegregation. *Nat Genet* 2017. PMID 28553959
11. Snape K, et al. Mutations in *CEP57* cause mosaic variegated aneuploidy syndrome. *Nat Genet* 2011. PMID 21552266
12. Suijkerbuijk SJE, et al. Integration of kinase and phosphatase activities by BUBR1 ensures chromosome segregation fidelity. *Dev Cell* 2012 / related KARD–PP2A-B56 work. PMID 23789096, PMID 23345399
13. Phase Ib metformin + chloroquine in IDH1-mutated solid tumours. PMID 34069550
14. Cancer surveillance recommendations for genomic instability syndromes. DOI 10.1158/1078-0432.CCR-24-1101
