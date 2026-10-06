# Track 2 — Methods description

**Team: ciberpty** · MVA Hackathon 2026 · Proband PROBAND01
Repository: https://github.com/cpu-16/mva-hackathon-2026
Full report: `track2/REPORT_track2.pdf`

---

## Q2 — Describe your approach in detail (variant/mechanism → candidate medication)

We went from variant to candidate in five steps; exposure was most often unevaluable, and the direction-of-effect question remains untested for the one candidate not excluded.

**Step 1 — define the working hypothesis.** Two heterozygous BUB1B variants, presumed in *trans* (phase not established; Q9): `c.2210T>G` p.Leu737Ter, a
nonsense allele that, if translated, predicts a 736-residue product lacking residues 737–1050 (314 residues), including the kinase domain (UniProt O60566 annotates it at 766–1050), paired with `c.3006T>G` p.Asn1002Lys inside that domain. Working hypothesis: loss of function, matching
the truncating-plus-missense pattern of viable MVA1 — a truncating allele paired in *trans* with a functionally impaired missense allele, phase and residual function unestablished. Reading the pair as null-plus-hypomorph is our reading of the human truncating-plus-missense pattern (PMID 20516114), which does not state that complete biallelic loss is lethal, and neither do we; the hypothesis that p.Asn1002Lys retains residual function is motivated by the Sieben mouse series (PMID 31738183), not by 20516114, and its rank relative to L1012P is not established.

**Step 2 — follow the mechanism downstream, not at the lesion.** No approved drug restores BubR1.
We therefore asked what the lesion *produces* that is druggable. The chain is: weakened spindle
assembly checkpoint → chromosome mis-segregation → constitutional aneuploidy → stoichiometric
imbalance of protein complexes → proteotoxic stress. The last link is the one with approved drugs
against it.

**Step 3 — five filters instead of the usual two.** Beyond the two questions every exercise asks — is it approved, is the mechanism plausible — we added three:

| # | Filter | Question |
|---|---|---|
| 1 | Regulatory | Approved for marketing? |
| 2 | Mechanistic | Does it address the actual lesion or its consequence? |
| 3 | **Pharmacokinetic** | **Is the achievable exposure excluded by the effective in-vitro concentration? ("not excluded" is the best outcome this screen can return)** |
| 4 | Patient-specific safety | Compatible with *this* child's comorbidities? |
| 5 | **Direction of effect** | Can an increase in mis-segregation among survivors beyond a prespecified margin be excluded? |

**Step 4 — apply them, and report what dies.** Metformin — the candidate the literature points to,
descending from the AICAR hit of Tang et al. (PMID 21315436) — is not evaluable at filter 3: no
published study gives metformin an aneuploidy-selective effective concentration to compare against, and the
complex-I mechanism proposed for it carries a separate objection — therapeutic plasma levels are micromolar
while complex I inhibition requires millimolar (PMID 37343530).
MPS1/TTK
inhibitors and reversine are opposed at filter 2 by construction — they weaken a checkpoint that is already
insufficient — and the quantitative filter-5 margin is untested for them.

**Step 5 — the candidate not excluded, with its stopping condition.** Bortezomib passes filters 1–2, is not
excluded by filter 3 on a total-plasma peak comparison (free exposure and duration at the target unresolved), and fails
filter 4 *for this child*, which is a patient-specific verdict rather than a property of the drug.
We state the condition under which it would become a question for a tumour board — an MVA patient with an active
tumour, where the comparator is cytotoxic chemotherapy rather than nothing; a changed comparator, not an established
benefit — and we propose an
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
Working hypothesis: impaired BUB1B function, with a candidate drug target downstream; phase and the missense allele's functional effect remain unresolved.

The nonsense allele removes the entire C-terminal kinase domain; the missense allele sits inside it.
Cell lines derived from MVA patients with biallelic mutations show "an impaired mitotic checkpoint,
chromosome alignment defects, and low overall BUBR1 abundance" (PMID 20516114), and allele-specific effects — not merely total BubR1 quantity — drive phenotypic
heterogeneity (Sieben 2020, PMID 31738183).

We were explicit about what we could not determine. Phase is not established, and the routes available to us were uninformative: there are no parental samples; the challenge distributes a VCF and raw reads
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
modelled, not every possible MVA genome; it disqualifies the endpoint for that case, and for this child no clinical
negative is reported.

We ran the calibrated statistic on the proband and **withdrew the result**: the pre-registered
threshold fires on all 22 autosomes, which indicates a null model that does not fit these data, and the
pre-registered external control came back **not conclusive** because the control genomes were called
differently from the proband. We report no clinical negative for this child.

## Q10 — Time and effort

Approximately 30 hours of analyst time over the first two days (28–29 August 2026), of which the large majority
went to literature verification and adversarial review rather than to computation; the later pre-registered rounds
(30 August to 5 October) added several working days of analysis, verification and adversarial review, not logged to the hour. Compute was
negligible: the genome-wide prioritisation ran in 53 seconds on a commodity workstation with no GPU,
and the robustness controls in about ten minutes. Later rounds added the pre-registered analyses, on public inputs and, for the mosaicism work, the controlled-access proband VCF: eight in total — DepMap and its
follow-up, MVA-Replay, mosaicism, power and its four-parameter follow-up, dose–response, and the TRIP13 transfer
(`VERIFY.md` lists each pre-registration with its result file and amendments). The phase pilot is **not** one of
them — it ran before any pre-registration and we do not count it. All of this is CPU-only except the mosaicism null calibration,
which used one consumer GPU.

## Q11 — Method abstract (≤500 words)
No approved drug restores BubR1 function. We followed the lesion
downstream — weakened spindle assembly checkpoint, mis-segregation, constitutional aneuploidy,
stoichiometric protein imbalance, proteotoxic stress — and asked which approved agent acts on the
last link.

We applied five explicit filters. Beyond "is it approved" and "is the mechanism
plausible", we added a pharmacokinetic filter (is achievable exposure excluded by the effective in-vitro
concentration?), a patient-specific safety filter, and a direction-of-effect filter (can an increase beyond a prespecified
micronucleus harm margin among survivors be excluded?).

Metformin, the candidate the literature points to, is not evaluable on filter three: no aneuploidy-selective
effective concentration exists, and its complex-I mechanism needs millimolar levels against micromolar plasma (PMID 37343530). Bortezomib passes filters one and two (mechanism plausible in cancer aneuploidy; our own pre-registered test on public solid-tumour lines did not establish it there) and is not excluded by three. Aneuploidy level was associated with multiple myeloma patients' response to proteasome inhibitors
(Ippolito 2024, PMID 39247952), on cohorts small enough (8 complete responders vs 50 progressive) that
we treat it as motivation, not prediction. Label Cmax 231–312 nM (1.3 mg/m² IV) over a 40 nM reference bound read from a figure gives
5.8–7.8× on **total plasma** drug — Cmax/40, not Cmax/EC50; free peak ≈ 39–53 nM — not a therapeutic margin.

It then fails filter four for this child: peripheral neuropathy in 18% (motor 8%) of patients in a paediatric trial with combination chemotherapy, on top of
existing skeletal muscle atrophy. But filter four is patient-specific. For an MVA patient with an
active malignancy — where the comparator is cytotoxic chemotherapy — the comparator changes, though
benefit remains unestablished; biallelic BUB1B disease carries a high risk of embryonal tumours (phase not established here). Our deliverable is a conditional tumour-stage research comparison, with unresolved exposure and selectivity
requirements, plus a separate constitutional-cell vulnerability assay.

Strengths. Every candidate carries a stated status against a stated criterion, including our own; filter five stays untested; §8 lists what we
excluded. We report a predicted antagonism: reducing translation protects CIN cells from proteasome
inhibition (PMID 31530568), so mTOR inhibitors would antagonise, not synergise. The
questions apply to any rare disease; re-run on MVA2 and MVA3 — a transfer inside the MVA group, not a general demonstration — they return different verdicts.

Limitations. The proteasome dependency is established in cancer aneuploidy, not constitutional
mosaicism; §6 measures response and constitutional-cell vulnerability, not mechanism. Our
own pre-registered DepMap analysis found the association attenuated in solid lineages, the lineage of
this child's tumour. Under the pre-registered four-parameter model (f = 0.30, 4× selectivity, CV 0.20) the equal-EC50 test has simulated
power 0.17 at n = 3 and first exceeds 0.80 at n = 12; the full advancement rule is not powered. Phase is not established; parental genotyping is the cheapest
informative experiment. No disease-modifying drug can be recommended from these data today; the clearest action
supported by guidance is surveillance, not a molecule.

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
