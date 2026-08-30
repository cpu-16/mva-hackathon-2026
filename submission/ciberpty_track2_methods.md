# Track 2 — Methods description

**Team: ciberpty** · MVA Hackathon 2026 · Proband PROBAND01
Repository: https://github.com/cpu-16/mva-hackathon-2026
Full report: `track2/REPORT_track2.pdf`

---

## Q2 — Describe your approach in detail (variant/mechanism → candidate medication)

We went from variant to candidate in five steps, and the third and fifth are where most candidates die.

**Step 1 — establish the lesion.** Compound heterozygosity in BUB1B: `c.2210T>G` p.Leu737Ter, a
nonsense allele that removes the C-terminal 313 residues, including the kinase domain (UniProt O60566 annotates it at 766–1050), paired with `c.3006T>G` p.Asn1002Lys inside that domain. Loss of function, matching
the truncating-plus-missense pattern of viable MVA1: a null allele with a hypomorphic one. Reading the pair as null-plus-hypomorph is our reading of the human truncating-plus-missense pattern (PMID 20516114), which does not state that complete biallelic loss is lethal, and neither do we; the separate prediction that p.Asn1002Lys retains more residual function than L1012P comes from the Sieben mouse series (PMID 31738183), not from 20516114.

**Step 2 — follow the mechanism downstream, not at the lesion.** No approved drug restores BubR1.
We therefore asked what the lesion *produces* that is druggable. The chain is: weakened spindle
assembly checkpoint → chromosome mis-segregation → constitutional aneuploidy → stoichiometric
imbalance of protein complexes → proteotoxic stress. The last link is the one with approved drugs
against it.

**Step 3 — five filters instead of the usual two.** Repurposing exercises typically ask only whether
a drug is approved and whether its mechanism is plausible. We added three:

| # | Filter | Question |
|---|---|---|
| 1 | Regulatory | Approved for marketing? |
| 2 | Mechanistic | Does it address the actual lesion or its consequence? |
| 3 | **Pharmacokinetic** | **Is Cmax ≥ the effective in vitro concentration?** |
| 4 | Patient-specific safety | Compatible with *this* child's comorbidities? |
| 5 | **Direction of effect** | Does it avoid increasing mis-segregation in survivors? |

**Step 4 — apply them, and report what dies.** Metformin — the candidate the literature points to,
descending from the AICAR hit of Tang et al. (PMID 21315436) — fails filter 3: therapeutic plasma
levels are micromolar while complex I inhibition requires millimolar (PMID 37343530), and no
published study gives metformin an aneuploidy-selective effective concentration to compare against.
MPS1/TTK
inhibitors and reversine fail filter 5 by construction: they weaken a checkpoint that is already
insufficient.

**Step 5 — the survivor, with its stopping condition.** Bortezomib passes filters 1–3 and fails
filter 4 *for this child*, which is a patient-specific verdict rather than a property of the drug.
We state the condition under which it would become appropriate — an MVA patient with an active
tumour, where the comparator is cytotoxic chemotherapy rather than nothing — and we propose an
experiment — an eight-week assay window, about twelve weeks from a fresh biopsy — that could fail to support the dependency in this child's own cells. It would not, on its own, close the tumour-board question, and we say so where we describe it.

## Q3 — Generative AI declaration

Commercially-available generative AI was used. Provider, plan and relevant setting for each:

- **Anthropic**, Claude Opus via Claude Code, **Max** subscription plan, model-improvement data
  sharing disabled in account privacy settings.
- **OpenAI**, Codex (gpt-5.6), **Plus** plan, "Improve the model for everyone" disabled.
- **xAI Grok 4.6 via Cursor**, **Pro** plan, **Privacy Mode enabled** (zero data retention at Cursor
  and at the underlying model providers).
- **Piper TTS** (`en_US-ryan-high`) — open-source, run locally with no cloud service and no API key.
  Used only to narrate the pitch video; not a commercial service, listed for completeness.

**No block of the VCF and no genotype table was ever sent to a language model.** Genomic work ran on
local tools (`bcftools`, Exomiser) and on annotation APIs — Ensembl VEP and ClinVar — that the
hackathon policy names as acceptable.

## Q4 — Automated or manual candidate identification?

**Primarily manual literature review and expert curation, with LLM-assisted retrieval.** No
drug-target database query produced the candidate. Interface queries against ClinicalTrials.gov, Open
Targets, ChEMBL and CMap/LINCS returned no MVA1-specific drug pairing, which we report as a negative
result rather than omit.

## Q5 — Describe the manual review and curation

Three activities, all documented in the repository:

1. **Citation verification.** Every PMID was checked against PubMed or Europe PMC before use. This
   was not ceremonial: **three citation problems were caught, of three different kinds** —
   one wrong paper (a study of acromegaly cited as Wilms surveillance, PMID 17652220, replaced by
   16857697); one merged attribution (two KARD papers under a single citation, separated into
   PMID 23789096 and 23345399); and one over-extension (PMID 28553959 was being used to carry the
   proteotoxic rationale to CEP57, which that same source contradicts — we withdrew that use and kept
   the paper only for the BUB1B/TRIP13 embryonal-tumour sentence its abstract actually states).
2. **Adversarial review by independent models.** Two different language models were asked to attack
   our own drafts. They found, among others, a claim of ours that contradicted **our own data file**:
   the report stated that Tang et al. used only stable trisomies, when our extraction record shows
   Figure 6 of that paper tests *Bub1b*^H/H hypomorphic MEFs. Corrected. All review rounds are in
   `evidencia/`.
3. **Pharmacokinetic arithmetic, redone by hand.** Each Cmax was converted from ng/mL to molar using
   the molecular weight, against the FDA label section cited. This surfaced that our own margin used
   the ceiling of a label interval (89–120 ng/mL) rather than the interval; corrected to 5.8–7.8×.

## Q6 / Q7 — Data sources

Publicly available sources only. No proprietary data.

- **Literature:** PubMed / Europe PMC, cited by PMID throughout.
- **Regulatory labels:** FDA labels and reviews — VELCADE (NDA 021602 s040; BPCA Clinical Review
  2015), NDA 206927 s002, Kyprolis (NDA 202714 s010), Ninlaro (NDA 208462), Rapamune, Afinitor,
  Mekinist.
- **Variant and gene resources:** ClinVar, gnomAD v4, Ensembl REST and VEP, UniProt (O60566), OMIM
  and Orphanet identifiers, Human Phenotype Ontology.
- **Drug/target interfaces queried (all negative for MVA1):** ClinicalTrials.gov, Open Targets,
  ChEMBL, CMap/LINCS.
- **Pathway and model resources:** Reactome (R-HSA-69618), KEGG (hsa04110), MGI (MGI:1333889).
- **Assay standards:** OECD Test Guideline 487 (micronucleus assay).

## Q8 — Proprietary data

None.

## Q9 — How did you characterize the variant's mechanism?
Loss of function, with the druggable target displaced downstream of the lesion.

The nonsense allele removes the entire C-terminal kinase domain; the missense allele sits inside it.
Cell lines derived from MVA patients with biallelic mutations show "an impaired mitotic checkpoint,
chromosome alignment defects, and low overall BUBR1 abundance" (PMID 20516114), and allele-specific effects — not merely total BubR1 quantity — drive phenotypic
heterogeneity (Sieben 2020, PMID 31738183).

We were explicit about what we could not determine. Phase is not established, and we measured that it is not
establishable from these data: there are no parental samples, the challenge distributes a VCF with no
alignments so no read-backed phaser can be run, and the two variants lie 10,911 bp apart with no GATK
phase tag on either — a limit visible in the data itself, since GATK did phase three variants 5 bp
apart elsewhere in the same VCF. Reference-panel phasing fails separately: all three heterozygous
sites inside the interval are absent from the 1000 Genomes 3,202-sample phased panel, and Beagle 5.5
drops all three. Our retrieval pipeline is insensitive to phase in any case: two pathogenic nonsense
alleles declared in cis are still called compound heterozygous, still PATHOGENIC and still ranked
first, at a 0.34% score penalty. Nonsense-mediated decay of the truncated
transcript is unmeasured and we do not assert it either way without patient RNA. p.Asn1002Lys has
no published functional assay, and its in-silico predictors disagree (REVEL 0.472, AlphaMissense
0.923), which is why we let it stand as a VUS.

We also asked whether aneuploidy burden could serve as a trial endpoint in these data, and computed
that it cannot: simulating mean |BAF − 0.5| at DP 44 puts the detection limit at ~14% of cells for a
clonal trisomy (16% under a stricter 2-SD criterion, against a measured between-chromosome SD of
0.0035), while variegation leaves each chromosome at 1–2% — 7–16× below it. That constrains
any proposal whose outcome depends on measuring aneuploidy from bulk sequencing.

## Q10 — Time and effort

Approximately 30 hours of analyst time over two days (28–29 August 2026), of which the large majority
went to literature verification and adversarial review rather than to computation. Compute was
negligible: the genome-wide prioritisation ran in 53 seconds on a commodity workstation with no GPU,
and the eleven robustness controls in about ten minutes.

## Q11 — Method abstract (≤500 words)
No approved drug restores BubR1 function, so we did not look for one. We followed the lesion
downstream — weakened spindle assembly checkpoint, mis-segregation, constitutional aneuploidy,
stoichiometric protein imbalance, proteotoxic stress — and asked which approved agent acts on the
last link.

We then applied five filters instead of the usual two. Beyond "is it approved" and "is the
mechanism plausible", we added a pharmacokinetic filter (does the achievable Cmax reach the
concentration effective in vitro?), a patient-specific safety filter, and a direction-of-effect
filter (does the drug increase mis-segregation among survivors?). Filters three and five are rarely
applied and eliminate the most candidates.

Metformin, the candidate the literature points to, dies on filter three. Therapeutic plasma
levels are micromolar while complex I inhibition requires millimolar (PMID 37343530) — roughly a
thousand-fold gap. We state what kind of number that is: for metformin no aneuploidy-selective EC50
exists, so this is a comparison between concentration ranges, not the same quantity as a measured
Cmax/EC50 ratio. We note what cuts the other way: AICAR's selectivity does reproduce in human cells
(PMID 22890317), but that paper does not test metformin, and AICAR is not approved.

Bortezomib survives filters one to three. Aneuploid cells mitigate proteotoxic stress by
increasing protein degradation and are correspondingly sensitive to proteasome inhibition; aneuploidy
level was significantly associated with multiple myeloma patients' response to proteasome inhibitors
(Ippolito 2024, PMID 39247952), on cohorts small enough (8 complete responders vs 50 progressive)
that we treat it as motivation, not prediction. The concentration reaches: EC50
below 40 nM in highly aneuploid lines against a label Cmax of 89–120 ng/mL (231–312 nM) at
1.3 mg/m² IV — a margin of 5.8–7.8× on total drug. The subcutaneous route does not pass once protein binding
is considered, and we say so.

It then fails filter four for this child: motor neuropathy in 8% of paediatric patients, on top of
existing skeletal muscle atrophy. But filter four is patient-specific.
For an MVA patient with an active malignancy — where the comparator is cytotoxic chemotherapy rather
than nothing — the balance inverts, and biallelic BUB1B carries a high risk of embryonal tumours. Our
deliverable is that answer prepared in advance, with its margin and its stopping rule.

Strengths. Every candidate is killed or kept by a stated criterion, including our own. We report an antagonism a combination-minded team could walk into: reducing translation protects
CIN cells from proteasome inhibition (PMID 31530568), so mTOR inhibitors would be predicted to
antagonise rather than synergise. The framework transfers to any rare disease.

Limitations. The proteasome dependency is established in cancer aneuploidy, not constitutional
mosaicism; whether it transfers is precisely what our eight-week experiment tests, and we
have not assumed it. The EC50 is a conservative bound read from a figure panel. Phase is unproven and, we show, unobservable in these data; parental genotyping is the cheapest experiment here.
And no disease-modifying drug can be recommended from these data today — what most changes his
prognosis now is surveillance, not a molecule.
