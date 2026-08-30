# Pre-registration — does the aneuploidy→proteasome dependency hold outside haematological cancers?

**Team ciberpty · MVA Hackathon 2026 · written 2026-08-30, BEFORE any result was computed.**

This file is committed to git before the analysis script is run. Its git timestamp is the evidence
that the hypotheses, the directions of effect and the stopping rules below were fixed in advance.
If we later change any of them, the change and its reason go at the bottom of this file — the
original text is never edited.

---

## Why we are running this

Our Track 2 report proposes bortezomib as a *conditional* answer for an MVA1 patient who develops a
second tumour. The evidence chain is: aneuploid cells over-use protein degradation (Ippolito 2024,
PMID 39247952), and in that paper **aneuploidy level was associated with response of multiple myeloma
patients to proteasome inhibitors**.

Two reviewers independently attacked the same link: *myeloma is a plasma-cell neoplasm with its own
immunoglobulin-driven proteotoxic load, and this child's tumour was an embryonal rhabdomyosarcoma —
a solid tumour.* We have no number that speaks to solid tumours. This analysis produces one, or
documents that it cannot be produced.

**We are testing our own candidate, and this can go against us.** That is the point.

## Data (fixed before analysis)

| Source | File | Version |
|---|---|---|
| Cell line metadata (lineage, primary disease) | `Model.csv` | DepMap 24Q4 (figshare 27993248) |
| Absolute copy-number segments → aneuploidy score | `OmicsAbsoluteCNSegmentsProfile.csv` | DepMap 24Q4 |
| Drug sensitivity | `Repurposing_Public_24Q2_LFC_COLLAPSED.csv` | PRISM Repurposing Public 24Q2 (figshare 25917643) |
| Compound annotation | `Repurposing_Public_24Q2_Treatment_Meta_Data.csv` | same |

No patient data is used anywhere in this analysis. Everything here is public.

## Aneuploidy score — defined before looking at any drug

For each cell line, from absolute CN segments:

1. Map segments to chromosome arms (hg38 centromere positions, fixed table in `arms_hg38.tsv`).
2. Per arm, take the length-weighted median absolute copy number.
3. Estimate the line's ploidy as the length-weighted median absolute CN across all autosomes.
4. Call an arm **gained** if its weighted median CN ≥ ploidy + 0.5, **lost** if ≤ ploidy − 0.5.
5. **Aneuploidy score = number of altered autosomal arms (0–39).** Arms with < 50% segment coverage
   are not called and are excluded from that line's denominator; a line with fewer than 30 callable
   arms is dropped.

This follows the arm-level convention of Taylor 2018 / Cohen-Sharir 2021. We define it here rather
than importing a published score so that the definition cannot be chosen after seeing results.

## Drug list — LOCKED. No drug is added after unblinding.

| Drug | Role in this test | Direction we predict |
|---|---|---|
| **bortezomib** | our candidate | more sensitive with higher aneuploidy |
| **carfilzomib** | proteasome inhibitor, class replication | more sensitive with higher aneuploidy |
| **ixazomib** | proteasome inhibitor, class replication | more sensitive with higher aneuploidy |
| **metformin** | the candidate we rejected | no association |
| **trametinib** | MEK inhibitor, unrelated mechanism | no association predicted |
| **everolimus** | mTOR inhibitor; we predict it *antagonises* PIs | not more sensitive with aneuploidy |
| **paclitaxel** | **negative control**: broadly cytotoxic. If it tracks aneuploidy as strongly as the PIs, the whole signal is a "sick cell" confound, not a proteasome story | no specific association |

## Hypotheses and the exact directions, fixed now

- **H1.** Across all lines, bortezomib sensitivity correlates with aneuploidy score in the sensitive
  direction (more aneuploid → more killed). *Predicted: Spearman ρ significant, sensitive direction.*
- **H2 — the one that matters.** H1 also holds when restricted to **solid-tumour lines only**.
  *Predicted: same direction. If it fails, our tumour-board argument is computationally unsupported
  and we will say so in the report.*
- **H3.** The effect replicates across the proteasome-inhibitor class (carfilzomib, ixazomib), not
  only bortezomib.
- **H4.** Metformin shows no aneuploidy association. *If metformin's association is comparable to
  bortezomib's, our filter-3 rejection needs rewriting, not defending.*
- **H5.** Paclitaxel's association is weaker than the proteasome inhibitors'. *If it is equal or
  stronger, we report the whole comparison as confounded by general cytotoxicity.*

## Statistics, fixed now

- Primary test: **Spearman ρ** between aneuploidy score and drug log-fold-change, per drug, in three
  strata: all lines / solid-tumour lines / haematological lines.
- Multiplicity: **Benjamini–Hochberg across the 7 drugs × 3 strata = 21 tests**; FDR < 0.05 is
  "significant". We report q-values, not raw p, for every test.
- Lineage confounding: a secondary mixed-effects model with lineage as a random intercept
  (`statsmodels`). Reported alongside, not instead of, the primary.
- **Power floor: any stratum with n < 20 lines is reported as descriptive only and gets no p-value.**
  We state n for every cell of the table.
- Solid vs haematological is assigned from `Model.csv` `OncotreeLineage`, using a mapping written
  before unblinding (`lineage_map.tsv`); "Lymphoid", "Myeloid" and plasma-cell lineages are
  haematological, everything else is solid.

## What each outcome would force us to write

| Outcome | What goes in the report |
|---|---|
| H2 holds | The PI rationale is not myeloma-specific; the tumour-board argument gains support that did not exist before. |
| H2 fails, H1 holds | The association we rely on is **confined to haematological lines** in this dataset. The tumour-board argument is weakened and we say so in §4 and in the abstract. |
| H4 fails (metformin tracks aneuploidy) | Our filter-3 rejection of metformin is rewritten, not defended. |
| H5 fails (paclitaxel ≥ PIs) | The entire comparison is reported as confounded; no drug conclusion is drawn from it. |
| Everything null | We report a null. PRISM LFC is not an EC50 in an isogenic pair, and a null here does not vindicate or refute Ippolito — it means this dataset cannot resolve it. |

## Known limitations, acknowledged in advance

- PRISM log-fold-change at a single dose is **not** an EC50, and not the isogenic
  diploid-vs-aneuploid comparison Ippolito used. This is an association across heterogeneous cancer
  lines, and we will not describe it as a replication of Ippolito.
- Cancer cell lines are not constitutional mosaic aneuploidy. A positive result does not transfer to
  MVA by itself; it only removes the "myeloma-only" objection.
- Embryonal rhabdomyosarcoma lines are few. If n < 20 we do not test that lineage separately.

---

# Amendment 1 — 2026-08-30, written after running the primary test and BEFORE running the extension

The original text above is unedited, as promised. This amendment records what we found that we could
not have anticipated, and what we are adding because of it.

## What forced the amendment

**H2 is not testable in this dataset.** The seven locked drugs exist only in the `REP.PRIMARY`
PRISM screen, and that screen used the PR500A collection, which is adherent-only. Of the 98
haematological lines that have both an aneuploidy score and a PRISM entry, **zero have a non-null
bortezomib measurement**. The solid-versus-haematological contrast — the entire reason we ran this —
cannot be computed from PRISM Repurposing. The "all lines" and "solid lines" strata are therefore
the same 444 lines, and we report them as one.

This is a property of the data, not a result. We did not know it before downloading.

## What we are adding, with its direction fixed now

We will test the same mechanism with a different measurement that *does* cover both strata:
**CRISPR gene-effect scores for proteasome subunits** (DepMap 24Q4 `CRISPRGeneEffect.csv`, ~1,100
lines including haematological). Genetic dependency on the proteasome is the mechanism Ippolito
proposed and the one the 2026 paired CRISPR screens (PMID 42094535, preprint) nominate.

- **Gene set, locked now:** the 14 constitutive 20S subunits `PSMA1-PSMA7`, `PSMB1-PSMB7`, plus
  `PSMB5` singled out because it is bortezomib's binding target. We will also report the 19S
  ATPases `PSMC1-PSMC6` as a secondary set. No gene is added after seeing results.
- **Statistic:** Spearman ρ between aneuploidy score and CRISPR gene effect (more negative gene
  effect = more essential), per gene, in the three strata. BH-FDR across all genes × strata.
- **Predicted direction (H6):** more aneuploid lines are *more* dependent on proteasome subunits, so
  **ρ negative**.
- **Negative control, locked now:** `PSMD9` is a proteasome-assembly chaperone that is not part of
  the 20S core, plus a random set of 200 genes to give the null distribution of ρ. If the core
  subunits do not separate from the random background, we report no effect.
- **H7 — the contrast we actually wanted:** the association, if present, is **not confined to
  haematological lines**. If it holds in solid lines, the myeloma-only objection to our report is
  answered by genetic data even though the drug data could not answer it.

## What each outcome forces us to write

| Outcome | Report |
|---|---|
| ρ negative and significant in solid lines | The proteasome dependency of aneuploid cells is present in solid-tumour lines at the genetic level. The myeloma-only objection is weakened. |
| Significant only in haematological lines | The objection stands, and we say the drug argument is lineage-restricted. |
| No separation from the random background | We report that neither PRISM nor CRISPR in DepMap supports the dependency at the resolution we can measure, and the report's §3.2 is softened accordingly. |

## Result of the primary test, recorded here before the extension is run

For the record, so that the extension cannot be presented as if it were the primary analysis:
bortezomib ρ = −0.075 (n = 444 solid lines, p = 0.11, q = 0.40 — **not significant**); carfilzomib
ρ = −0.060 (q = 0.51); ixazomib ρ = +0.028; metformin ρ = +0.020; paclitaxel ρ = +0.096.
**No test passed FDR < 0.05.** Pipeline positive control: across all 6,790 compounds, 1.1% reach
p < 0.001 against 0.1% expected by chance, so the machinery detects associations when they exist.
