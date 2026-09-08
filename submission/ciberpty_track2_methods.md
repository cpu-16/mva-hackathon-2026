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
experiment — an eight-week assay window, 12–16 weeks from a fresh biopsy because establishing the fibroblast line takes 4–8 weeks on its own, more if twelve cultures per arm must be expanded — that could fail to support the dependency in this child's own cells. It would not, on its own, close the tumour-board question, and we say so where we describe it.

## Q3 — Generative AI declaration

Commercially-available generative AI was used. Provider, plan and relevant setting for each:

- **Anthropic**, Claude Opus and Claude Fable 5.1 via Claude Code, **Max** subscription plan, model-improvement data
  sharing disabled in account privacy settings.
- **OpenAI**, Codex (gpt-5.6), **Plus** plan, "Improve the model for everyone" disabled.
- **xAI Grok 4.6 via Cursor**, **Pro** plan, **Privacy Mode enabled** (zero data retention at Cursor
  and at the underlying model providers).
- **Qwen3-TTS 1.7B VoiceDesign** — open-weights, run locally on CPU with no cloud service and no API
  key. Used only to narrate the pitch video; not a commercial service, listed for completeness. Each
  clip was transcribed by a local recogniser and diffed against the written script before assembly,
  because this class of model can alter a word silently.

**No block of the VCF and no genotype table was ever sent to a language model.** Genomic work ran on
local tools (`bcftools`, Exomiser) and on annotation APIs — Ensembl VEP and ClinVar — which return
public annotation for submitted coordinates and acquire no rights over the input. The policy does not
name these services; we read them as satisfying the two conditions it does set, namely no training on
inputs or outputs and limited retention.

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

Publicly available drug, target and literature sources only; no proprietary data. The one controlled-access
input is the challenge dataset itself (the proband's VCF and clinical document), used under the data
transfer agreement described under *Data availability* and deleted within 30 days of the close.

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
establishable from these data: there are no parental samples; the challenge distributes a VCF and raw reads
but no alignments, we did not align them, and short reads could not phase two variants whose only intervening
heterozygous site lies 6.8 and 4.1 kb away; and the two variants lie 10,911 bp apart with no GATK
phase tag on either — a limit visible in the data itself, since GATK did phase three variants 5 bp
apart elsewhere in the same VCF. Reference-panel phasing fails separately: all three heterozygous
sites inside the interval are absent from the 1000 Genomes 3,202-sample phased panel, and Beagle 5.5
drops all three. Our retrieval pipeline is insensitive to phase in any case: two pathogenic nonsense
alleles declared in cis are still called compound heterozygous, still PATHOGENIC and still ranked
first, at an absolute score difference of 0.0034. Nonsense-mediated decay of the truncated
transcript is unmeasured and we do not assert it either way without patient RNA. p.Asn1002Lys has
no published functional assay, and its in-silico predictors disagree (REVEL 0.472, AlphaMissense
0.923), which is why we let it stand as a VUS.

We also asked whether aneuploidy burden could serve as a trial endpoint in these data, and computed
that it cannot. A first-order calculation — mean |BAF − 0.5| at DP 44 against a measured
between-chromosome SD of 0.0035 — puts the detection limit at ~14% of cells for a clonal trisomy (16%
under a stricter 2-SD criterion). A later calibrated simulation (Ψ over 125-site windows, Monte Carlo
null) improves that to **2.07% at an overdispersion κ = 2**; that is a *simulated* limit conditional on
κ, not a measured sensitivity, and it places variegation's 1–2% per chromosome at the edge of what is
achievable rather than far below it. The argument that does not depend on any limit is
**non-identifiability**: for a perfectly balanced variegated mixture, mean copy number is exactly 2 and
mean allele fraction exactly 0.5 by symmetry, and simulated detection stays at the 0.1–0.2%
false-positive rate even with 40% of cells aneuploid. That proof covers the balanced mixture we
modelled, not every possible MVA genome, and it is enough to disqualify the endpoint.

We ran the calibrated statistic on the proband and **withdrew the result**: the pre-registered
threshold fires on all 22 autosomes, which indicates a null model that does not fit these data, and the
pre-registered external control came back **not conclusive** because the control genomes were called
differently from the proband. We report no clinical negative for this child.

## Q10 — Time and effort

Approximately 30 hours of analyst time over two days (28–29 August 2026), of which the large majority
went to literature verification and adversarial review rather than to computation. Compute was
negligible: the genome-wide prioritisation ran in 53 seconds on a commodity workstation with no GPU,
and the robustness controls in about ten minutes. Later rounds added the pre-registered DepMap,
benchmark, power and mosaicism-control analyses, all on public data. The phase pilot is **not** one of
the pre-registered five — it ran before that pre-registration and we do not count it as one
(`VERIFY.md` lists the five pairs). All of this is CPU-only except the mosaicism null calibration,
which used one consumer GPU.

## Q11 — Method abstract (≤500 words)
No approved drug restores BubR1 function, so we did not look for one. We followed the lesion
downstream — weakened spindle assembly checkpoint, mis-segregation, constitutional aneuploidy,
stoichiometric protein imbalance, proteotoxic stress — and asked which approved agent acts on the
last link.

We applied five filters instead of the usual two. Beyond "is it approved" and "is the mechanism
plausible", we added a pharmacokinetic filter (does the achievable Cmax reach the concentration
effective in vitro?), a patient-specific safety filter, and a direction-of-effect filter (does the drug
increase mis-segregation among survivors?).

Metformin, the candidate the literature points to, dies on filter three: therapeutic plasma levels are
micromolar while complex I inhibition requires millimolar (PMID 37343530). AICAR's selectivity does
reproduce in human cells (PMID 22890317), but that paper does not test metformin, and AICAR is not
approved.

Bortezomib survives filters one to three. Aneuploid cells depend on increased protein degradation, and
aneuploidy level was associated with multiple myeloma patients' response to proteasome inhibitors
(Ippolito 2024, PMID 39247952), on cohorts small enough (8 complete responders vs 50 progressive) that
we treat it as motivation, not prediction. An EC50 below 40 nM in highly aneuploid lines against a
label Cmax of 89–120 ng/mL (231–312 nM) at 1.3 mg/m² IV gives a margin of 5.8–7.8× on **total plasma**
drug at a peak — not free or intratumoral drug, and 312 nM is the top of a label interval, not a
validated clinical threshold.

It then fails filter four for this child: motor neuropathy in 8% of paediatric patients, on top of
existing skeletal muscle atrophy. But filter four is patient-specific. For an MVA patient with an
active malignancy — where the comparator is cytotoxic chemotherapy — the balance
inverts, and biallelic BUB1B carries a high risk of embryonal tumours. Our deliverable is that answer
prepared in advance, with its margin and its stopping rule.

Strengths. Every candidate is killed or kept by a stated criterion, including our own; this is not an
exhaustive screen, and §8 of the report lists what we excluded. We report an antagonism a
combination-minded team could walk into: reducing translation protects CIN cells from proteasome
inhibition (PMID 31530568), so mTOR inhibitors would be predicted to antagonise, not synergise. The
framework transfers to any rare disease; applied to MVA2 and MVA3 it returns different verdicts.

Limitations. The proteasome dependency is established in cancer aneuploidy, not constitutional
mosaicism; whether it transfers is what our proposed experiment tests. Our
own pre-registered DepMap analysis found the association attenuated in solid lineages, the lineage of
this child's tumour. Under the pre-registered four-parameter model with biological variability the assay
has power 0.17 at n = 3 and needs about 12 cultures per arm. The EC50 is a conservative bound read from a figure
panel. Phase is unproven and unobservable in these data; parental genotyping is the cheapest
informative experiment. No disease-modifying drug can be recommended from these data today — what most
changes his prognosis now is surveillance, not a molecule.

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
