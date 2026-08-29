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
2. **The biomarker the field does not have.** Every candidate therapy for MVA needs *aneuploidy
   burden* as an endpoint. Using this child's own genome, we show empirically that this endpoint is
   not measurable in bulk sequencing, and we propose a two-tier assay that is.
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
   | KEN1 |--- N-terminal TPR ---| KEN2/ABBA | GLEBS/Bub3 |-- KARD --| pseudokinase |
     ~26       ~50–204              ~304       ~392–426     ~665–682    ~705–1034
                                                                   ↑            ↑
                                                               Leu737Ter    Asn1002Lys
```

**p.Leu737Ter** truncates at the start of the pseudokinase domain, removing roughly 313 residues.
The N-terminal MCC-forming region, the GLEBS/Bub3 motif and the KARD motif remain in sequence, but a
truncated protein should not be assumed stable. In a closely related MVA model, the human
`2211insGTTA` allele produced an unstable X753 truncation, and allelic combinations produced effects
not explained by protein quantity or aneuploidy rate alone (PMID 31738183).

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
kinetochore–microtubule attachments; its disruption causes congression defects in MVA cells
(PMID 23789096, PMID 23345399).

**Genotype–phenotype, honestly stated:** the recurrent pattern in viable MVA1 is one truncating
allele plus one amino-acid substitution, often C-terminal (PMID 20516114). Homozygous `Bub1b`
knockout is embryonic lethal in mouse, while hypomorphs age prematurely and accumulate aneuploidy
(PMID 15208629). But there is **no validated correlation** between these two specific alleles — or
between "truncating + missense" generally — and differential risk of embryonal rhabdomyosarcoma
versus Wilms tumour. The child's rhabdomyosarcoma is consistent with the MVA spectrum
(PMID 16182441, PMID 28553959); it does not by itself establish the function of p.Asn1002Lys.

---

## 2. Piece one — what is actionable today, without a drug

The intervention with the strongest evidence base is not a molecule.

### Tumour surveillance

MVA/BUB1B predisposes principally to early embryonal tumours: embryonal rhabdomyosarcoma, Wilms
tumour, and leukaemia (PMID 16182441, PMID 28553959). UK surveillance recommendations covering
children with mosaic aneuploidy or BUB1B variants propose **renal ultrasound every 3–4 months from
diagnosis until age 5**, because nearly all reported Wilms tumours in those series occurred before
that age (PMID 17652220). Contemporary guidance for genomic instability syndromes emphasises
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

## 3. Piece two — the biomarker the field does not have

**This is our principal contribution.**

Any therapy for MVA needs a measurable endpoint, and the natural one is **aneuploidy burden**. No
candidate can be evaluated without it. So we asked whether that endpoint is measurable in the data
this hackathon provides.

### What we did

Four independent tests on the proband's own 44× WGS, each designed to rule out the artefact of the
previous one:

1. **Per-chromosome B-allele frequency** over 2.27 M heterozygous SNVs. In a diploid chromosome,
   heterozygous sites cluster at 0.50; a trisomy splits them towards 0.33/0.67. Raw signal appeared
   on chr20, 21, 22 and X.
2. **Fixed-depth control** (DP 40–48), removing the coverage confounder. chr21 collapsed to baseline
   — it had been a coverage artefact. chr20 (1.38×) and chr22 (1.28×) survived.
3. **Spatial profile** in 5 Mb windows. A whole-chromosome aneuploidy elevates *every* window; a
   mapping artefact elevates a few. chr20 and chr22 both had **normal medians** (13.1% and 14.0%)
   with two high windows each, falling on the centromere and on **22q11** — the best-known segmental
   duplication region in the genome.
4. **Chromosomal dosage** by 10%-trimmed mean depth. Six chromosomes showed apparent gain (chr16, 17,
   19, 20, 21, 22) — but five of those six are the most GC-rich chromosomes in the genome, the
   signature of GC bias in PCR-based libraries, and the sixth is a small acrocentric. chr18, nearly
   the size of chr17 but GC-poor, showed +0.10%.

**Where tests 1–3 and test 4 disagreed, we resolved in favour of BAF**, which is an internal per-site
ratio and therefore immune to library coverage bias, while dosage compares absolute depths and
inherits every library artefact. A trisomy in 14% of cells (implied by chr21's +7% dosage) would
shift heterozygous BAF to ~0.47/0.53, detectable across 11,463 SNVs — and it is not there. We record
the dosage signal as an open hypothesis, not a finding.

### Why the negative result was predictable — and why it matters

This is not a limitation of the data. It follows from the definition of the disease.

In *variegated* mosaicism, different cells gain or lose **different** chromosomes. The diagnostic
criterion is >25% of metaphases carrying aneuploidies of varied chromosomes. If 30% of lymphocytes
are aneuploid and that burden is distributed across 22 autosomes, **each individual chromosome is
altered in roughly 1.4% of cells** — a dosage shift near 0.7%, far below what 44× bulk sequencing can
resolve. Averaging over millions of cells erases precisely the heterogeneity that defines the
phenotype. This is why MVA is diagnosed by cell-by-cell karyotyping, not by sequencing.

### The proposal

| Candidate endpoint | Resolution | Cost | Verdict |
|---|---|---|---|
| Bulk WGS (BAF or dosage) | insufficient — demonstrated here | already paid | ❌ unusable |
| Metaphase karyotype | diagnostic standard, cell-by-cell | high, manual, slow | reference, not scalable |
| **Low-coverage scDNA-seq** | per cell, genome-wide | medium | ✅ the correct endpoint |
| **Micronucleus frequency** | per-cell proxy for mis-segregation | **low**, microscopy | ✅ cheap screening tier |

We propose the pair **micronucleus frequency (screening) → low-coverage scDNA-seq (confirmation)** as
a standardised endpoint for therapeutic studies in chromosomal instability disorders. Micronuclei are
cheap enough to run across a compound matrix; scDNA-seq confirms the hits. Neither requires the
patient to be dosed with anything.

This proposal is not a literature review conclusion. It falls out of having analysed this specific
child's genome and found the standard approach empirically insufficient.

---

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

- The **11-gene panel and rarity+impact filter** apply to any suspected chromosomal instability
  disorder — MVA by CEP57 (PMID 21552266) or TRIP13 (PMID 28553959), and adjacent phenotypes.
- The **mosaicism artefact controls** (fixed-depth stratification, spatial windowing, GC awareness)
  apply to any attempt to detect mosaic aneuploidy from bulk sequencing, and would have prevented
  three false positives here.
- The **micronucleus → scDNA-seq endpoint** applies to any CIN disorder, including Fanconi anaemia and
  Bloom syndrome.
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
9. Scott RH, et al. Surveillance for Wilms tumour in at-risk children. *Arch Dis Child* 2006. PMID 17652220
10. Yost S, et al. Biallelic *TRIP13* mutations predispose to Wilms tumor and chromosome missegregation. *Nat Genet* 2017. PMID 28553959
11. Snape K, et al. Mutations in *CEP57* cause mosaic variegated aneuploidy syndrome. *Nat Genet* 2011. PMID 21552266
12. Suijkerbuijk SJE, et al. Integration of kinase and phosphatase activities by BUBR1 ensures chromosome segregation fidelity. *Dev Cell* 2012 / related KARD–PP2A-B56 work. PMID 23789096, PMID 23345399
13. Phase Ib metformin + chloroquine in IDH1-mutated solid tumours. PMID 34069550
14. Cancer surveillance recommendations for genomic instability syndromes. DOI 10.1158/1078-0432.CCR-24-1101
