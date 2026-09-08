# Track 2 — Drug Repurposing for MVA1 (BUB1B, presumed compound heterozygosity; phase not established)

**Team: ciberpty** · Rare Disease, Real Kid: MVA Hackathon 2026
Repository: https://github.com/cpu-16/mva-hackathon-2026 · Methods description: Appendix B of this PDF

*This document has two parts. **Part I** (this part, about 24 pages including the reference list) is the decision document: every
conclusion, every number that carries it, and every limitation, at the length a judge can read in one
sitting. **Part II** is the full evidence: the same sections at full length, with derivations, sources
quoted verbatim, the correction history and every pre-registered analysis. Where Part I compresses,
Part II is authoritative for detail; every number in Part I is taken from Part II or from the results files both cite.*

---

## Read this first — one page for the family and the treating team

*Written in plain language for the child's parents and the clinician sitting with them. Every claim is
sourced in the sections that follow.*

**What we looked for.** An existing, approved medicine that could help a child with mosaic variegated
aneuploidy whose presumed cause is two changes in the *BUB1B* gene (one of them still formally uncertain, and whether they sit on opposite copies of the gene is not yet shown; §1, §10). We fixed in advance the tests a candidate had to
pass and put the main candidates through them. It is not an exhaustive screen; §8 lists what we ruled
out and why.

**What we are not recommending.** **No drug should be started for this today.** The honest answer is
more useful than an encouraging one.

- **Metformin**, the medicine most often suggested for this kind of problem, should not be started on
  this reasoning: no one has measured what dose would be needed to act on *this* problem, and the
  best-studied way it might act needs concentrations about a thousand times higher than the blood levels
  the usual doses produce, and whether it could act another way at those levels has never been tested (§3.1).
- **Bortezomib** is an approved cancer medicine that acts on a weakness that cancer cells with extra
  chromosomes have been shown to have. **Nobody has shown that this child's cells have it.** Our own
  analysis of public cancer data found the link weaker in solid tumours as a group, which is the group
  his tumour belongs to, and his tumour type is almost absent from that data. It also causes nerve damage
  in about 18 in 100 children who receive it, and this child already has muscle weakness. **Outside an
  active cancer, that trade is not worth making** (§5).

**What can be done this month.**

| | Action | Why |
|---|---|---|
| 1 | **Confirm the child's current age** with the care team | Every schedule below depends on it, and we do not have it |
| 2 | **Renal ultrasound every 3 months, birth to age 7** | Published consensus for all forms of MVA (PMID 39264246: the SIOP-Europe host-genome group's schedule, endorsed by the AACR workshop). Not our idea; how it applies to this child is the treating team's decision |
| 3 | **Regular full clinical examination**, including the orbit, skin and soft tissues | Rhabdomyosarcoma is not a kidney tumour; a 2026 case of the related MVA3 had a second tumour behind the eye at age 12 (PMID 42595739) |
| 4 | **Avoid unnecessary radiation; keep HPV vaccination up to date** | Consensus guidance (PMID 39264246) |
| 5 | **Ask about testing and counselling for both parents** — a ready-to-adapt laboratory request is included (`clinico/PARENTAL_SEGREGATION_ORDER.md`) | The clinical notes mention repeated miscarriages; a 2026 study linked that pattern to carriers of *BUB1B* changes (PMID 42434306). A hypothesis, not a diagnosis, and a simple test (§7) |

**What would change the answer.** If a new tumour appears, the question changes from "should he take a
medicine" to "which medicines belong in the treatment plan", and bortezomib becomes worth putting to a
tumour board, after the laboratory test in §6 — as a possible *addition* to standard treatment, never a replacement. In children with
other solid tumours it has been given at known doses — with real side effects — and has not shrunk tumours on its own (§5).
We have written that answer down now so nobody has to assemble it in a hurry.

**What we are not certain about.** The strongest evidence comes from cancer patients, not from
children with MVA. Whether the same weakness exists in this child's cells is genuinely unknown; §6
describes the experiment that could show us we are wrong.

---

## Executive summary

We applied five filters to candidate drugs rather than the usual two (§2). **Metformin**, the candidate
the literature points to, is not evaluable for aneuploidy-selective activity — no effective concentration
has ever been measured — and the complex I mechanism proposed for it needs millimolar concentrations
against micromolar plasma levels (§3.1). **Bortezomib** survives: aneuploid cancer cells depend on the
proteasome (Ippolito 2024, PMID 39247952), its total-plasma peak at the approved IV dose is 5.8–7.8 times
the EC50 of highly aneuploid lines, and aneuploidy level tracked response in myeloma patients (§3.2).
That comparison is an exposure plausibility screen on total drug against an upper bound on the EC50, not a
therapeutic threshold: on free drug (83% protein-bound) the peak is within one- to 2.5-fold of that bound,
not the six- to eightfold the total-drug ratio suggests.

**We then tested the part of that argument that public data can test, pre-registered, and it did not
survive** (§4): across 444 solid-tumour cell lines no proteasome inhibitor reached significance, and the
genetic dependency on bortezomib's target is significantly weaker in solid tumours than in haematological
ones (interaction p = 0.026, interval excluding zero, not driven by any single lineage). This child's
tumour was solid, and his tumour type is essentially absent from the drug screen.

Bortezomib then **fails the patient-specific safety filter**: neuropathy in 18% of children, on
pre-existing muscle atrophy. **Not for this child, not now** (§5). What remains is a prepared, evidence-
bounded answer for the setting of an active tumour, an experiment that could refute the premise in this
child's own cells (§6), and the actions that change his prognosis today without any drug (§7).

**What we contribute** is seven pre-registrations that constrain the claim — DepMap and its follow-up, MVA-Replay, mosaicism, power, dose–response and the TRIP13 transfer; the DepMap test came back against our mechanism, the mosaicism control came back not conclusive, the power analysis found the assay feasible only under unmeasured inputs, and the dose–response analysis left our 4× assumption unsupported — a reusable five-filter worksheet, and a retrieval-benchmark tool transferred to a
second MVA gene from a fresh clone of our repository (§9).

---

## 1. The variants

The proband carries two heterozygous `BUB1B` variants (NM_001211.6, MANE), read here as compound
heterozygous **on presumption: phase is not established** (§10).

| Variant | Consequence | Exomiser ACMG | ClinVar | gnomAD (Exomiser snapshot, exomes NFE; VEP: 3×10⁻⁵ and no record) |
|---|---|---|---|---|
| `c.2210T>G` p.(Leu737Ter) | stop_gained | PATHOGENIC | 533901, Pathogenic/Likely pathogenic | 9.98×10⁻⁵ |
| `c.3006T>G` p.(Asn1002Lys) | missense | UNCERTAIN_SIGNIFICANCE | **not present** (ClinVar holds `c.3006T>A`, a different nucleotide, VUS — does not transfer) | 9.0×10⁻⁷ |

**p.Leu737Ter** removes the C-terminal kinase fold entirely (UniProt annotates it at 766–1050), 16
residues from BUBR1^X753, a characterised truncating MVA allele (PMID 31738183). **p.Asn1002Lys** has no
published functional assay. On the AlphaFold model (pLDDT 91.1 at the residue) Asn1002 is buried (relative
solvent accessibility 0.162) in a hydrophobic pocket, and the substitution inserts a longer, charged side
chain — evidence about the substitution, not a classification: no ΔΔG was computed, and the retrieved
predictors disagree (REVEL 0.472, AlphaMissense 0.923). No calibration set exists to score it against: in
ClinVar (2026-08-28 release) *BUB1B* carries 1,497 missense records of which one is Likely pathogenic — one star, single submitter — against 82 of 94
truncating records P/LP — a property of the database, not a prior about this allele. The mouse model
pairing the nearby missense L1012P with a truncation died prematurely (PMID 31738183); our proband is
alive, so if that transfers, p.Asn1002Lys must retain more function than L1012P — a falsifiable
prediction §6 tests. Full detail: Part II §1.

---

## 2. Five filters, not two

| # | Filter | Question | What it eliminates here |
|---|---|---|---|
| 1 | Regulatory | Approved for marketing? | AICAR, 17-AAG, reversine, apcin, proTAME, DCZ0415 |
| 2 | Mechanistic | Does it address the lesion or a direct consequence of it? | Agents on uninvolved pathways |
| 3 | **Pharmacokinetic** | **Is Cmax ≥ the effective in-vitro concentration?** | **Metformin** |
| 4 | Patient-specific safety | Compatible with *this* child's comorbidities? | **Bortezomib, at present** |
| 5 | Direction of effect | Does it avoid increasing mis-segregation in survivors? | Untested for the candidates that reach it; §6 is where it would be measured |

![The five-filter funnel](fig3_funnel.png)

Filter 3 is a possibility check on total plasma drug at a peak, not a demonstration of efficacy: it
ignores protein binding, exposure duration and tissue penetration. Filter 5 asks the question
repurposing exercises forget: among the cells that survive the drug, is the defect made worse?

---

## 3. Applying the filters

### 3.1 Metformin: not evaluable on the mechanism proposed for it

Tang et al. found aneuploidy-selective sensitivity to **AICAR** (PMID 21315436); AICAR is not approved,
and metformin is the marketed stand-in that activates AMPK through complex I inhibition. Therapeutic
metformin plasma concentrations are **micromolar**, while complex I inhibition requires **millimolar**
(PMID 37343530) — a gap of roughly a thousandfold in concentration ranges, not a dosing calculation.
Therapeutic metformin does activate AMPK in patients; what the gap rules out is the complex I route at
plasma concentrations. An AMPK-mediated aneuploidy-selective effect at those concentrations is not
excluded — it is **untested**: no study reports a metformin aneuploidy-selective effective concentration,
the one paper reproducing AICAR's selectivity in human cells attributes it to EGFR degradation and does not
test metformin (PMID 22890317), and Tang's instability models were never given metformin. In children,
dose-normalised exposure varies 3.3-fold and clearance is renal (PMID 42399684); this child has
nephrocalcinosis. **Verdict: rejected at filter 3 as unevaluable, not as disproven.** Part II §3.1.

### 3.2 Bortezomib: passes filters 1–2; not excluded by filter 3

Aneuploid cells carry a stoichiometric protein imbalance and compensate by increasing degradation, which
makes them dependent on the proteasome; Ippolito et al. showed this across diploid-versus-aneuploid
models and hundreds of cancer lines, and found aneuploidy level associated with myeloma patients'
response to proteasome inhibitors (PMID 39247952). That human signal rests on small cohorts and one-tailed tests (single agent: 8 complete responders vs 50 progressors, p = 0.014; with chemotherapy and dexamethasone: 13 complete vs 14 minimal responders per the figure legend, p = 0.038) — enough to justify an experiment, not to
predict a patient. A 2026 paired-CRISPR preprint independently nominates proteasome subunits and UBE2H
as aneuploid-specific dependencies (PMID 42094535; not peer-reviewed, weighted as corroboration).

| | Value | Source |
|---|---|---|
| EC50, highly aneuploid lines (72 h) | **< 40 nM**, conservative bound read from Fig. 6o | PMID 39247952 |
| Cmax, 1.3 mg/m² IV, repeated dosing | **89–120 ng/mL = 231–312 nM** (the twice-weekly range the label reports; the same label gives 223 ng/mL in its IV-vs-SC cohort) | FDA label NDA 021602 |
| Ratio, IV | **5.8–7.8**, on total drug | — |
| Subcutaneous | 53.1 nM; ratio 1.33 — does not survive any plausible free-fraction correction | same |

Read the ratio as an order of magnitude on *total* plasma drug at a peak. **The exposure evidence, laid out
rather than reduced to a pass:**

| Quantity | Value | What it does and does not support |
|---|---|---|
| Effective concentration | EC50 < 40 nM at 72 h in 5 highly aneuploid cancer lines, read from Fig. 6o (PMID 39247952); no tabulated value; medium and serum binding unstated | A bound on total drug in culture, not a threshold for MVA cells |
| Plasma binding | 83% bound to human plasma proteins over 100–1,000 ng/mL (label §12.3) | Free fraction ≈ 17%, applied below 100 ng/mL as an approximation |
| Cmax, IV 1.3 mg/m² | 112 ng/mL first dose; 89–120 ng/mL twice weekly; 223 ng/mL in the IV-vs-SC comparison cohort (label §12.3) | Total drug at a peak; **free peak ≈ 39–53 nM** (or ≈ 99 nM from 223 ng/mL) |
| Cmax, SC 1.3 mg/m² | 20.4 ng/mL, with AUC equivalent to IV (label §12.3) | Free peak ≈ 9 nM |
| Pharmacodynamics | Maximal 20S inhibition 73–83% in whole blood at 5 min (label §12.2); elimination half-life 76–108 h on multiple dosing, with plasma falling steeply after infusion | Duration at the target is not established by any number here |

On total drug the IV ratio is 5.8–7.8; **on free drug the peak (≈ 39–53 nM, or ≈ 99 nM on the 223 ng/mL
figure) is within one- to 2.5-fold of the < 40 nM bound** — and since that bound is an upper bound on the
EC50, the true free-drug margin is unknown; the culture value is itself partly free drug in serum-containing
medium, so the two sides are not on the same footing. What filter 3 supports is that the IV route is **not excluded**; it does not support
comparable free exposure or duration at the target, and we do not correct one side for binding while
leaving the other unexplained. The culture-side EC50 carries its own unstated medium and binding conditions. Myeloma is a plasma-cell neoplasm with its own proteotoxic load and
clonal, not variegated, aneuploidy; MVA1 is a different setting in which the same dependency is plausible
and **untested**. Part II §3.2.

### 3.3 Everything else: not evaluable

| Drug | Verdict | Why |
|---|---|---|
| Carfilzomib, ixazomib | Not evaluable | No IC50 in an aneuploidy-stratified model; Cmax known, no valid denominator |
| Hydroxychloroquine | Not evaluable, mechanistically weakened | Tang's hit was chloroquine, which did *not* differentially inhibit the human CIN lines |
| Everolimus / sirolimus | Not evaluable, possibly counterproductive | §3.4 |
| Trametinib | Not evaluable — the gap most worth closing | Aneuploid RPE1 clones are MEK-inhibitor-sensitive (PMID 39251587) but only relative IC50s were recoverable; Cmax 36.1 nM at 2 mg/day; approved from age 1 with dabrafenib for BRAF V600E low-grade glioma; filters 2 and 5 untested; null in our DepMap test |

We leave cells empty rather than manufacture ratios from unstratified models.

### 3.4 The antagonism nobody should walk into

Aneuploid cells are vulnerable to proteasome inhibition *because* of translational burden; ovarian
carcinoma spheroids acquired resistance to proteasome inhibitors by suppressing mTORC1, and PTEN loss
resensitised them (PMID 31530568). That paper did not test rapalogues; the antagonism is our inference from its mechanism. **Prediction, falsifiable:** everolimus or sirolimus would antagonise
bortezomib in aneuploid cells; §6 tests the combination. The same paper notes bortezomib's poor clinical
response in advanced ovarian cancer — a solid-tumour failure any honest reading carries. A tension we flag:
mTORC1 hyperactivity correlates with sarcopenia in *monoallelic* BubR1 mice (PMID 31738183), a
muscle-directed rationale that points the other way and must not be read as support for the combination.

---

## 4. We tested our own candidate on public data, and pre-registered it first

The objection to §3.2 is that the human signal is myeloma and this child's tumour was an embryonal
rhabdomyosarcoma. We had no number for solid tumours, so we produced one — drug list, directions,
statistic, correction and stopping rules committed to `depmap/PREREGISTRO.md` before the analysis ran (the commit history documents the record, not our conduct; deviations are listed in `VERIFY.md`, and one untestable hypothesis was recorded as a dated amendment).

**Method.** An arm-level aneuploidy score for 2,420 DepMap 24Q4 lines (validated: stable MSI lines average
5.0 altered arms, CIN lines 16.5), correlated with PRISM Repurposing drug sensitivity and DepMap CRISPR
gene effect. The pipeline is not blind: across 6,790 compounds 1.1% reach p < 0.001 against 0.1% expected.

**Result 1 — drugs (444 solid lines).** No proteasome inhibitor reached FDR < 0.05. Bortezomib
ρ = −0.075 (95% bootstrap CI −0.168 to +0.017), carfilzomib −0.060, ixazomib +0.028; metformin null as
predicted; paclitaxel, the cytotoxic control, ran the other way (+0.096), which argues against — without
excluding — a "sick cells die more" confound. Haematological lines have no PRISM value for these drugs (0 of 98 for bortezomib).

**Result 2 — the target (946 lines).** PSMB5 dependency tracks aneuploidy overall (ρ = −0.198,
q = 5×10⁻⁸) but splits by lineage: **haematological ρ = −0.261 (−0.422 to −0.084); solid ρ = −0.077
(−0.149 to −0.009), q = 0.12** — the interval excludes zero narrowly while the pre-registered FDR test
did not pass, and the pre-registered verdict stands. The **aneuploidy × lineage interaction is
β = −0.017 (95% CI −0.031 to −0.002, p = 0.026)**; per ten additional altered arms PSMB5 dependency moves
−0.06 in solid lines and −0.23 in haematological lines; ploidy adds nothing (p = 0.88), which does not exclude other confounding. These model statistics were first computed ad hoc and are now reproduced by the follow-up script.

![Follow-up: effect sizes with 95% bootstrap intervals; the solid stratum by lineage](fig5_seguimiento.png)

**Follow-up, pre-registered after the result (`depmap/PREREGISTRO_SEGUIMIENTO.md`), all four predictions
held.** Dropping each of 26 solid lineages never flips a sign or moves the interaction interval across
zero (p 0.013–0.037); all 27 within-lineage intervals overlap zero; a fraction-of-arms score changes
nothing, a ploidy-residualised score shrinks the small drug correlations by more than half (−0.075 → −0.028) without
changing signs. The two assays share 365 solid models and agree with each other only at ρ = −0.070 (−0.176 to +0.033): they
are different modalities on overlapping models, not independent replications. **Rhabdomyosarcoma:** 17
scored lines, **3** with a drug value — less killed at 2.5 µM than 98%, 91% and 89% of solid lines —
and 10 with a CRISPR value, unremarkable. No statistic is computed on them; it is a coverage limitation
for exactly the tumour type this child had.

**What it costs us.** The link our bortezomib argument rests on is detectable where myeloma sits and
attenuated in solid tumours: *the attenuation is not an artefact of any single lineage and its interval
excludes zero; the solid-stratum association itself remains compatible with zero.* Ippolito's own
bortezomib screen (Fig. 6p, reversine-induced aneuploidy, p < 0.0001) is positive; ours carries the same
sign and fails significance, and an induced-aneuploidy design is the more sensitive of the two — so our
null is weaker evidence against the link than theirs is for it. Ippolito also report associations in pancreatic and paediatric PDX models (their Suppl. Fig. 8o–r), which say nothing about MVA. What we add is the lineage split. PRISM
is a single-dose viability screen, not an EC50, and cancer lines are not constitutional MVA. Part II §3.5
and `depmap/RESULTADOS*.md`.

---

## 5. Filter 4 — safety in *this* child, where the candidate stops

Bortezomib is not excluded by the total-plasma comparison. It does not clear this patient today.

| Concern | Data | Relevance here |
|---|---|---|
| **Peripheral neuropathy** | 25/140 (18%) of paediatric patients, motor 11/140 (8%) (FDA BPCA review, 2015); adults grade ≥ 2 in 39% by the IV route (FDA NDA 206927 s002, 2022) | **Skeletal muscle atrophy** (HP:0003202): the decisive objection |
| Cytopenias, infection | FDA label | Prior chemotherapy; marrow reserve unknown |
| GI toxicity, hypotension | FDA label | **Failure to thrive** (HP:0001508) |
| Renal | PK not clinically altered by renal impairment, per label | **Nephrocalcinosis** (HP:0000121): function, hydration and electrolytes first |

**Bortezomib is not proposed as prophylaxis or chronic therapy for this child.** Filter 4 is
patient-specific: for an MVA patient with an active malignancy, the comparator becomes chemotherapy rather
than nothing and the balance *can* invert — a judgement for the treating team and a tumour board, off
label or under an n-of-1 protocol with its own ethics approval and stopping rules, after the ex-vivo gate of §6, not a result of this report.

**What is already known about bortezomib in the tumour he had, and in children — none of it in our
favour.** RMS cell lines are killed at 13–26 nM, sparing primary myoblasts, and bortezomib reduced the growth of an RMS xenograft
(PMID 18342500). But across the Pediatric Preclinical Testing Program, in-vivo activity against
solid-tumour xenografts was limited while leukaemia xenografts responded (PMID 17420992). The COG phase I
ADVL0015 set 1.2 mg/m² twice weekly for two of every three weeks as the paediatric dose, with dose-limiting thrombocytopenia at
1.6 mg/m² and **no objective responses** in 15 children with refractory solid tumours (PMID 15570082);
ADVL0916 with vorinostat likewise saw none, with a sensory neuropathy progressing to grade 4 as a DLT
(PMID 22887890); an adult sarcoma phase II found minimal single-agent activity in soft-tissue sarcoma and closed its osteosarcoma/Ewing/rhabdomyosarcoma arm for low
accrual (PMID 15739208). **Single-agent bortezomib has not shrunk a paediatric solid tumour in a trial.**
If it is ever reached for, it would be as part of a combination, and the aneuploidy argument is a reason
to ask whether MVA-driven tumours are the exception, not evidence that they are.

Spindle poisons depend on a competent checkpoint; a reduced-intensity regimen for an RMS in PCS/MVA is
on record as a single case (PMID 31184400). That is a mechanistic caution to weigh against probability of
cure, not a contraindication, and never a reason to withhold curative therapy.

---

## 6. Endpoints, and the experiment that could show us we are wrong

**Bulk sequencing cannot serve as the aneuploidy-burden endpoint** (Part II §5). From the proband's VCF
we computed a first-order detection limit of ~14% of cells for a clonal trisomy, then a calibrated
simulated limit of **2.07% at overdispersion κ = 2** (1.46% at κ = 1, 2.95% at κ = 4) — a simulated limit
under a fitted null, not a measured sensitivity. If ~30% of cells were aneuploid spread across 22 autosomes — an illustrative bound, not a patient measurement — each chromosome would be affected in 1–2% of cells, which sits at
that edge, and the argument that needs no limit is this: **a perfectly balanced variegated mixture is not
identifiable from bulk allele fractions** — detection stays at the 0.1–0.2% false-positive rate from 2% to
40% of cells. Real variegation need not be balanced, so this disqualifies the endpoint without saying bulk
WGS can never see MVA. **We ran the calibrated statistic on the proband and withdrew the result**: the
null did not describe the data (22 of 22 autosomes exceeded the threshold), the z-score we had reported was chosen after seeing the data and never calibrated, the residual overdispersion
(≈2.3×) is uncontrolled, and the pre-registered external control of ten 1000 Genomes individuals came back
*not conclusive*: the proband fell below the control envelope, an outcome the amendment had not listed, with the controls' different calling explaining their inflated dispersion. **No clinical negative is reported.**
Any screen must measure mis-segregation per cell: metaphase counts, micronuclei (OECD TG 487), or
single-cell DNA.

**The experiment (Part II §6).** Patient dermal fibroblasts against two matched controls and a
reversine-treated RPE1 positive control; allele-fate assays; a bortezomib dose–response 0–1,000 nM at 72 h
(spanning the 312 nM Cmax); a bortezomib + everolimus arm for the predicted antagonism; a micronucleus
assay with FISH for 3–5 chromosomes on survivors of every condition, with proliferation recorded because a change in division rate alone moves the count. Eight weeks of assay after 4–8 weeks to establish the line: a planning figure of **12–16 weeks**
from biopsy (MVA1 fibroblasts may grow slower), after consent, assent and ethics approval whose timing is not ours to control.

**What it decides, and what it cannot.** Fibroblasts are constitutional MVA cells, not tumour cells: a
sensitivity difference measures whether the dependency transfers to constitutional aneuploidy and is, on
its own, as compatible with systemic toxicity as with promise. A negative fails to support transfer
without closing the tumour-board question, which needs aneuploidy-high tumour material this design does
not sample.

| Reading | Consequence |
|---|---|
| Aneuploid-cell fraction *f* measured first, on the culture and passage to be treated (cells with ≥ 1 numerical abnormality, plus abnormal chromosomes per abnormal cell; PCS scored separately) | Gate: the bulk EC50 ratio to expect at an assumed 4× selectivity is 1.14× at f = 0.10, 1.30× at 0.20, 1.50× at 0.30, 2.00× at 0.50 — a pre-specified reading rule, not a validated threshold, recomputed if selectivity is ever estimated; indicative n = 3 at f ≥ 0.25, n = 14 at 0.10, and below f ≈ 0.10 use a per-cell endpoint instead of bulk viability |
| EC50 shift at the row for the measured *f*, 95% CI excluding 1, at ≤ 312 nM | Dependency signal: build the tumour-material stage. A shift materially *above* the row is not a better result — suspect the mixture model or systemic toxicity |
| Patient cells markedly more sensitive **without** the positive control shifting more | **Stop**: the most likely reading is constitutional toxicity, the outcome most easily mistaken for success |
| Micronuclei increase among survivors | **Stop**: fails filter 5 regardless of killing |
| No shift | Fails to support transfer in these cells; tumour question stays open |

Power: 0.897 in an idealised simulation (n = 3, α = 0.05, assumed 4× selectivity, 30% aneuploid culture, 10% CV, a two-
parameter Hill fit where four were pre-registered, no biological-replicate term) and 0.387 at 2×; none of the inputs is measured in these
cells, and our own dose–response analysis leaves the 4× unsupported and unrefuted (`potencia/`).

---

## 7. Actionable now, without any drug

**The intervention that most changes this child's prognosis is surveillance, and there is an MVA-specific
consensus** (PMID 39264246, verified against the full text): renal ultrasound every 3 months from birth to
age 7 for all MVA conditions, regular clinical assessment for rhabdomyosarcoma and other malignancies,
avoidance of radiation, HPV vaccination. Cancers in MVA1 are predominantly Wilms tumour and
rhabdomyosarcoma, with MDS, AML and ALL reported. **The gap that matters for this child:** the window
closes at seven, and a 2026 MVA3 case had an orbital embryonal rhabdomyosarcoma at twelve (PMID 42595739),
at a site renal ultrasound does not image. The consensus asks for clinical assessment without setting an end date; for a child who has already had an RMS we propose that the
clinical-examination arm continue past seven, and we mark it as our extension.

| Period | Surveillance | Frequency |
|---|---|---|
| Birth to 7 | Renal ultrasound (we suggest widening the field to liver, retroperitoneum, pelvis) | 3-monthly — **consensus**; the wider field is ours |
| To 10, then reviewed | Full paediatric and oncological examination: abdomen, nodes, head and neck, **orbit**, skin, genitalia, soft tissues | 3-monthly to 7, then 6-monthly — continuing past 7 is **our extension** |
| Post-ERMS | Relapse follow-up per tumour protocol | Avoid duplicate imaging |
| Through childhood | Full blood count with differential | 6-monthly is reasonable; **no evidence of benefit exists** |
| Lifelong | Family education; annual predisposition clinic | Urgent review for mass, haematuria, pain, deficit, bleeding, weight loss |

The child's current age is not in the dataset and must be confirmed first. No serial AFP, CT, PET-CT or
routine whole-body MRI while asymptomatic. If the child is past seven, missed scans should not be "caught
up"; a baseline assessment and an individualised decision by the predisposition team is the right course. The whole table is a discussion framework for an expert predisposition clinic.

**For the parents.** The clinical document records recurrent spontaneous abortion (HP:0200067). If the
variants are in *trans* — the interpretation adopted here, not demonstrated — each parent would be expected to carry one;
segregation testing establishes that and must precede any carrier-specific interpretation. A 2026 study of
two families with recurrent pregnancy loss found heterozygous *BUB1B* variants (classified VUS) with elevated
premature chromatid separation in the carriers' lymphocytes (PMID 42434306): a hypothesis, cheap to act on.
A PCS assay on parental lymphocytes would test whether the parents show that cellular phenotype — not that it
caused the losses — and would inform any future pregnancy. **The laboratory request is written**
(`clinico/PARENTAL_SEGREGATION_ORDER.md`): both loci, two Sanger amplicons with primers verified as
single-copy across GRCh38 (the first design returned sat in an *AluY* with ~100 copies; RepeatMasker
exclusion caught it), and an interpretation table written before the result covering all five outcomes —
including *cis*, which would refute our own Track 1 interpretation. A *trans* result contributes PM3-type
evidence; **it does not by itself reclassify the missense.**

---

## 8. What we do not propose

MPS1/TTK inhibitors and reversine (not approved; they weaken a checkpoint that is already insufficient);
apcin and proTAME (APC/C tool compounds, not marketed); DCZ0415 (a TRIP13 inhibitor: wrong gene, not approved); AICAR and 17-AAG (screen hits, not marketed;
positive controls only); metformin (§3.1); senolytics (the BubR1 evidence rests on genetic clearance of
p16⁺ cells, PMID 22048312, and senescence is an anti-tumour barrier worth keeping here); mTOR inhibitors with
proteasome inhibition (§3.4); bortezomib for this child today (§5).

---

## 9. Scalability

- **The five-filter worksheet** (one page, below) applies *as questions* to any repurposing exercise in a
  rare disease — filter 3 as an exposure plausibility screen, filter 5 as the MVA instance of "does treatment
  worsen the disease-relevant defect or select for it?" — and it is the transferable product.
- **The MVA genes are not interchangeable.** Transferred prospectively (`report/TRANSFER_MVA2_MVA3.md`)
  the worksheet returns different verdicts: for **MVA2** (*CEP57*) bortezomib fails filter 4 and cannot be
  evaluated at 2–3 — no proteasome data, and an active malignancy has not been reported in the 15
  published individuals (PMID 39264246; a statement about the literature, not of zero risk); for **MVA3**
  (*TRIP13*), which shares the embryonal-tumour risk and severe checkpoint failure (PMID 28553959), it
  stays conditional. That shows the worksheet responds to the evidence available for each gene, not that
  the drug behaves differently in them. UBE2H is the target to watch (PMID 42094535); it has no approved
  inhibitor.
- **The retrieval benchmark is a tool, and we tested the claim.** `replay/mva_replay.py` plants two
  alleles into a public genome and returns score, rank, a ClinVar-whitelist-off counterfactual and an
  unrelated-phenotype control. Pre-registered and pushed before the run, from a **fresh clone** of the
  repository, it planted two public Likely-pathogenic *TRIP13* alleles — chosen by the frozen pool rule, not by us — into three healthy GIAB genomes,
  queried with six HPO terms transcribed from the abstract of PMID 42595739:

| Background | Planted, case phenotype | Unrelated phenotype | Unspiked |
|---|---|---|---|
| HG001 | **0.8332, rank 1** | 0.4240, rank 1 | absent |
| HG002 | **0.8332, rank 1** | 0.4240, rank 2 | 0.0, rank 212 |
| HG005 | **0.8332, rank 1** | 0.4240, rank 3 | absent |

  The same pattern as BUB1B (rank 1/2/3 under an unrelated phenotype). Each background took under 3½
  minutes and about 2.4 GiB. The operational half was the useful one: four provisioning steps, three of
  which the requirements list did not include, and regression tests the README said ran from a bare
  checkout did not. Both fixed; the provisioning script and every tool invocation with its exit code are
  committed (`replay/TRANSFER_TRIP13.md`). It measures retrieval given a perfect call, not diagnostic
  sensitivity.
- **One command regenerates the Track 2 package.** `analysis/make_track2.sh` re-runs the DepMap follow-up
  (figure and tables) when the public downloads are present, renders the worksheet from `candidates.tsv`,
  checks every reported number against the results files and builds the PDFs. Run from a fresh checkout of
  the repository it finished in 8 s and 179 MB, naming the one missing input (the ~700 MB DepMap/PRISM
  downloads, which it does not bundle) and building both PDFs from the committed copies
  (`evidencia/make_track2_fresh_checkout_2026-09-08.log`).
- The gene panel and artefact controls transfer to any MVA or PCS workup; the micronucleus → scDNA-seq
  endpoint applies to mitotic CIN disorders, **not** to Fanconi anaemia or Bloom syndrome.

---

## 10. Limitations

- **Phase is not established, and cannot be from these data.** No parental samples; the challenge
  distributes a VCF and raw reads but no alignments, we did not align the reads, and short reads could not
  phase two variants whose only intervening heterozygous site lies 6.8 and 4.1 kb away; all three sites are
  absent from the 1000 Genomes phased panel (expected copies 0.64 and 0.006 in 6,404 haplotypes). Nothing in
  the data weighs *cis* over *trans*; what supports *trans* is that the child is affected, MVA1 is recessive,
  truncating-plus-missense is the recurrent pattern, and the phenotype matches. **A diagnosis pending
  segregation.** The retrieval pipeline itself is insensitive to phase: two nonsense alleles declared in *cis*
  are still called compound heterozygous and ranked first (score difference 0.0034).
- **p.Asn1002Lys has no functional assay**, and its apparent ClinVar entry is a different nucleotide.
- **The bortezomib EC50 is a bound read from a figure; the Cmax is a label interval; the ratio is on
  total drug** and says nothing about free drug, tissue or duration. No effective concentration has been
  measured in constitutional MVA cells.
- **Ippolito studied cancer aneuploidy.** Whether the dependency transfers is exactly what §6 tests; we have
  not assumed it. Our public-data test weakens the solid-tumour case and cannot speak to MVA cells.
- **The power estimate is idealised** (two-parameter fit, no biological-replicate term, unmeasured inputs).
- **The mosaicism control was not conclusive**; the patient-level result is withdrawn; no clinical negative.
- **No trial specific to MVA1** was found in ClinicalTrials.gov, Open Targets, ChEMBL or CMap/LINCS; absence of an interface result is not proof of absence.
- **The child's current age is unknown to us.**

---

## A closing note

The family published their son's genome so that strangers might help. The honest answer to "what drug
should he take today" is none. What we can leave them is a mechanism that matches his disease, an approved
drug whose plasma levels are not excluded by the concentrations at which cancer cells respond, the
condition under which it would be worth asking about, the experiment that could fail to support it in his
own cells, and the surveillance that changes his prognosis now. That is not a cure. It is a prepared
answer to a question this family may unfortunately have to ask.

---

## The five-filter worksheet (reusable)

*Rendered from `report/candidates.tsv` by `report/render_candidates.py`; the table below and the machine-readable file are the same object. Statuses only here; the model context and reason behind every cell are in the Part II worksheet and in the file. Every candidate this report evaluated is a row; add yours.*

| Candidate | 1. Approved? | 2. Lesion or direct consequence? | 3. Cmax vs effective concentration | 4. Safe in *this* patient? | 5. No increase in mis-segregation? | Verdict |
|---|---|---|---|---|---|---|
| **metformin** | pass | pass | not evaluable | not reached | not reached | **rejected at filter 3 unevaluable** |
| **bortezomib IV** | pass | pass | not excluded | **fail** | untested | **fails filter 4 for this child; conditional for active tumour** |
| **bortezomib SC** | pass | pass | **fail** | **fail** | untested | **fails filter 3 and 4** |
| **carfilzomib** | pass | pass | not evaluable | not reached | not reached | **not evaluable** |
| **ixazomib** | pass | pass | not evaluable | not reached | not reached | **not evaluable** |
| **hydroxychloroquine** | pass | **fail** | not evaluable | not reached | not reached | **not evaluable mechanistically weakened** |
| **everolimus sirolimus** | pass | **fail** | not evaluable | not reached | not reached | **not evaluable possibly counterproductive** |
| **trametinib** | pass | untested | not evaluable | not reached | not reached | **not evaluable gap most worth closing** |
| **AICAR** | **fail** | pass | not reached | not reached | not reached | **fails filter 1** |
| **17-AAG HSP90i** | **fail** | pass | not reached | not reached | not reached | **fails filter 1** |
| **reversine MPS1 TTK inhibitors** | **fail** | **fail** | not reached | not reached | **fail** | **fails filter 1 and 5** |
| **apcin proTAME** | **fail** | untested | not reached | not reached | not reached | **fails filter 1** |
| **DCZ0415** | **fail** | **fail** | not reached | not reached | not reached | **fails filter 1 and 2** |
| **senolytics** | **fail** | untested | not reached | not reached | untested | **not proposed** |
| **UBE2H inhibitor** | **fail** | pass | not reached | not reached | not reached | **target to watch** |
| *(your candidate)* | | | | | | |

**How to fill it in.** Filter 3 needs a real denominator measured in a model stratified for the disease
mechanism; if none exists, write *not evaluable* rather than substitute an IC50 from an unrelated model.
Filter 4 is a statement about one person and one moment, not about the drug. Filter 5 is the question
repurposing exercises forget. A machine-readable version with status vocabulary (pass / fail / untested /
not evaluable), source and reason is `report/candidates.tsv`.

---

## References

1. Hanks S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in *BUB1B*. *Nat Genet* 2004. PMID 15475955
2. Suijkerbuijk SJE, et al. Molecular causes for BUBR1 dysfunction in mosaic variegated aneuploidy. *Cancer Res* 2010. PMID 20516114
3. Hanks S, et al. Comparative genomic hybridization and BUB1B mutation analyses in childhood cancers associated with MVA. *Cancer Lett* 2006. PMID 16182441
4. Tang YC, et al. Identification of aneuploidy-selective antiproliferation compounds. *Cell* 2011. PMID 21315436
5. Ippolito MR, et al. Increased RNA and Protein Degradation Is Required for Counteracting Transcriptional Burden and Proteotoxic Stress in Human Aneuploid Cells. *Cancer Discov* 2024. PMID 39247952
6. Sakellakis M. Why Metformin Should Not Be Used as an Oxidative Phosphorylation Inhibitor in Cancer Patients. 2023. PMID 37343530
7. Fontaine E. Metformin-Induced Mitochondrial Complex I Inhibition: Facts, Uncertainties, and Consequences. 2018. PMID 30619086
8. Ailabouni AS, et al. Interindividual variability in metformin pharmacokinetics in pediatric patients. 2026. PMID 42399684
9. Chui MH, et al. Chromosomal Instability and mTORC1 Activation through PTEN Loss Contribute to Proteotoxic Stress in Ovarian Carcinoma. *Cancer Res* 2019. PMID 31530568
10. Knouse KA, et al. Single cell sequencing reveals low levels of aneuploidy across mammalian tissues. *PNAS* 2014. PMID 25197050
11. Baker DJ, et al. BubR1 insufficiency causes early onset of aging-associated phenotypes. *Nat Genet* 2004. PMID 15208629
12. Baker DJ, et al. Clearance of p16^Ink4a-positive senescent cells delays ageing-associated disorders. *Nature* 2011. PMID 22048312
13. Sieben CJ, et al. BubR1 allelic effects drive phenotypic heterogeneity in mosaic variegated aneuploidy. *J Clin Invest* 2020. PMID 31738183
14. Nishitani-Isa M, et al. ERMS with PCS/MVA treated with reduced-intensity chemotherapy. *Pediatr Int* 2019. PMID 31184400
15. Scott RH, et al. Surveillance for Wilms tumour in at-risk children: pragmatic recommendations. *Arch Dis Child* 2006. PMID 16857697
16. Xu P, et al. BUBR1 recruits PP2A via the B56 family to promote chromosome congression. *Biol Open* 2013. PMID 23789096
17. Kruse T, et al. Direct binding between BubR1 and B56-PP2A regulates mitotic progression. *J Cell Sci* 2013. PMID 23345399
18. Snape K, et al. Mutations in *CEP57* cause mosaic variegated aneuploidy syndrome. *Nat Genet* 2011. PMID 21552266
19. Yost S, et al. Biallelic *TRIP13* mutations predispose to Wilms tumor and chromosome missegregation. *Nat Genet* 2017. PMID 28553959
20. FDA label, VELCADE (bortezomib), NDA 021602 s040, §12.3
21. FDA BPCA Clinical Review, bortezomib paediatric safety, NDA 021602, 2015
22. Aneuploid human colonic epithelial cells are sensitive to AICAR-induced growth inhibition through EGFR degradation. 2013. PMID 22890317
23. Nakano Y, Kuiper RP, et al. Update on Recommendations for Cancer Screening and Surveillance in Children with Genomic Instability Disorders. *Clin Cancer Res* 2024. PMID 39264246
24. Schukken KM, et al. Paired CRISPR screens identify mitochondrial metabolism and UBE2H as aneuploid-specific dependencies in human cancer cell lines. *bioRxiv* 2026 (preprint). PMID 42094535
25. Vempuluru VS, et al. Sequential presentation of Wilms' tumor and orbital rhabdomyosarcoma in a child with mosaic variegated aneuploidy syndrome 3. *Orbit* 2026. PMID 42595739
26. Wei TY, et al. Functional and clinical evidence for two novel heterozygous *BUB1B* variants and their value in precision genetic counseling for recurrent pregnancy loss. *Front Endocrinol* 2026. PMID 42434306
27. Escalante LE, Hose J, et al. Chromosome duplication causes premature aging via defects in ribosome quality control. *PLoS Biol* 2025. PMID 41248159
28. Bersani F, Taulli R, et al. Bortezomib-mediated proteasome inhibition as a potential strategy for the treatment of rhabdomyosarcoma. *Eur J Cancer* 2008. PMID 18342500
29. Houghton PJ, Morton CL, et al. Initial testing (stage 1) of the proteasome inhibitor bortezomib by the pediatric preclinical testing program. *Pediatr Blood Cancer* 2008. PMID 17420992
30. Blaney SM, Bernstein M, et al. Phase I study of the proteasome inhibitor bortezomib in pediatric patients with refractory solid tumors: a Children's Oncology Group study (ADVL0015). *J Clin Oncol* 2004. PMID 15570082
31. Muscal JA, Thompson PA, et al. A phase I trial of vorinostat and bortezomib in children with refractory or recurrent solid tumors: a Children's Oncology Group phase I consortium study (ADVL0916). *Pediatr Blood Cancer* 2013. PMID 22887890
32. Maki RG, Kraft AS, et al. A multicenter Phase II study of bortezomib in recurrent or metastatic sarcomas. *Cancer* 2005. PMID 15739208
33. Human aneuploid cells depend on the RAF/MEK/ERK pathway for overcoming increased DNA damage. *Nat Commun* 2024. PMID 39251587

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with
the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium
for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and
their family who generously contributed their data and their story to advance research into this rare
disease. We acknowledge their trust in making this Hackathon possible.

## Data availability

The individual-level data analysed here is the Hackathon dataset (`SageBio/mva-hackathon-2026-data`),
accessed under the challenge data transfer agreement accepted by Hugging Face account `cpu-16` on
2026-08-28, and cited as directed on the Hackathon Synapse page. No patient sequence data or
genotype-scale derivative is included in this document or in our public repository, and every copy
we hold will be deleted by 2026-11-23 with written confirmation to the organisers. The two diagnostic
variants are named, as findings, which the challenge rules permit. All other inputs are public:
Exomiser 15.1.0 with data release 2602, ClinVar, gnomAD v4, the Human Phenotype Ontology, Ensembl and
VEP, the 1000 Genomes and GIAB genomes, DepMap 24Q4, AlphaFold and the literature cited by PMID.
Analysis code, pre-registrations and results: https://github.com/cpu-16/mva-hackathon-2026
