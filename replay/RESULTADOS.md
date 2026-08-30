# MVA-Replay — results

**Team ciberpty · MVA Hackathon 2026 · started 30-ago-2026.**
Design and predictions were fixed in `PREREGISTRO.md` and committed (`8086dd4`) before any locked case
ran. Amendments 1–3 are dated and appended there. **Experiment A tier 2 (30 × 1000G genomes) is still
running; this file is complete for tiers already finished and says so where it is not.**

---

## 0. An error this benchmark found in our already-submitted Track 1 report

`entrega/methods_track1.md` says, twice:

> "Removing the two contaminating terms drops the score from 0.5506 to 0.4187 — about 24% — **That is
> the size of the phenotype's contribution here**" … "the phenotype contributes **about 24% of the
> score**".

**That is the wrong pair of runs.** Both 0.5506 and 0.4187 are *unrelated-HPO controls*; the first
was the contaminated one, the second the corrected one. The delta between them measures what two
MVA-annotated terms leaking into a control were worth — not what the patient's phenotype is worth.

| Run | HPO set | BUB1B (AD row) |
|---|---|---|
| real | the patient's eight terms | **0.5871** |
| contaminated control | five "unrelated" terms, two annotated to MVA1 | 0.5506 |
| clean control | five verified-unrelated terms | 0.4187 |

The phenotype's contribution is **0.5871 → 0.4187 = 0.1684, i.e. 28.7%**, not 24%.

MVA-Replay reproduces both endpoints exactly, in three unrelated healthy genomes (§2), so the
corrected figure is replicated rather than recomputed from the same single run. The conclusion
("variant-driven, phenotype-consistent") is unchanged; the number attached to it is not.

---

## 1. Experiment A — what a healthy genome scores under the patient's phenotype

Seven GIAB genomes, unspiked, queried with the patient's exact eight HPO terms.

| Genome | Top-ranked gene | Combined score | Genes ranked |
|---|---|---|---|
| HG004 | GJB2 | **0.5619** | 2,495 |
| HG002 | KRT17 | 0.4881 | 2,387 |
| HG005 | RYR2 | 0.4194 | 2,274 |
| HG003 | APOB | 0.4188 | 2,431 |
| HG007 | CLDN24 | 0.2048 | 2,392 |
| HG006 | STIM2 | 0.0599 | 2,276 |
| HG001 | PAH | 0.0578 | 1,872 |

- **P-A holds so far:** our 0.5871 is above all seven. The margin to the highest is **0.025 (4.3%)**.
- **P-A2 holds strongly:** BUB1B does not appear in the ranked table of **any** of the seven.
- **Metric 7:** these genomes rank a median of 2,387 genes against the patient's 4,565. The
  competitor set is roughly half the size, which makes rank easier here than in a clinical WGS and
  biases the null *in our favour*. The score endpoint does not have this problem (§2).

⏳ Tier 2 — 30 unrelated 1000 Genomes 30× individuals, six per superpopulation — is running. With
n = 7 the honest statement is a range, not a percentile.

## 2. Experiment B — the score is a property of two alleles and a phenotype, not of the genome

Planting the two public ClinVar records of the Track 1 architecture (533901 `chr15:40209701 T>G`
nonsense + 4600147 `chr15:40220612 T>A` VUS) into three unrelated healthy genomes:

| Phenotype | BUB1B rank | BUB1B combined score | Our patient's value |
|---|---|---|---|
| the eight real terms | **1 in 3/3** | **0.5871 in all three** | 0.5871 |
| five verified-unrelated terms | 1 in 2/3 (rank 3 in HG005) | **0.4187 in all three** | 0.4187 |

**Both of our headline numbers reproduce to four decimal places in genomes that are not the
patient's.** Exomiser's gene combined score is fully determined by the planted alleles and the
phenotype query; the rest of the genome contributes nothing to it. What the background changes is the
*rank* — in HG005, whose own top gene reaches 0.8108 under the unrelated terms, BUB1B at 0.4187 falls
to rank 3.

- **P-B1 confirmed** (rank 1 in 3/3 with the real phenotype).
- **P-B2 confirmed** (rank 1 in 2/3 with an unrelated phenotype) — this is the concession we
  pre-committed to publishing, now a rate rather than an anecdote.
- **P-B4 confirmed**: Δ = 0.1684 < 0.20. As a fraction of the score, **28.7%** (see §0).
- **Rank is not a portable endpoint and score is.** Any statement of the form "rank 1 of N" has to
  carry N; the score does not.

**Decoy arm (FANCD2, the gene that actually came second in our Track 1 run).** ⏳ Re-running under
amendment 3. First cell: with the corrected allele the decoy reaches **rank 1, score 0.1841** in
HG001 — where the background's own best gene scores only 0.0578. Pre-amendment cells, built on a
pool defect the ingestion assertion caught, are reported as technical failures and are superseded.

## 3. Experiment C — how much of the score is ClinVar's classification

Same gene, same phenotype, same three genomes; only the ClinVar class of the two planted alleles
changes.

| Architecture | BUB1B combined score | Rank (HG001 / HG002 / HG005) | Exomiser ACMG |
|---|---|---|---|
| two P/LP alleles | **0.9332** | 1 / 1 / 1 | PATHOGENIC |
| **one P/LP + one VUS — the child's architecture** | **0.5871** | 1 / 1 / 1 | PATHOGENIC |
| two VUS alleles | **0.1120** | 1 / 5 / 3 | UNCERTAIN_SIGNIFICANCE |

- **P-C confirmed, and by a wide margin:** C-hi − C-lo = **0.8212**, against a pre-registered
  threshold of 0.10. The gradient is monotonic and the scores are identical across all three genomes.
- The consequence for our own submission is the uncomfortable one: **had the child's nonsense allele
  not been in ClinVar as Pathogenic, the same two variants in the same gene under the same phenotype
  would have scored 0.1120 and would have lost rank 1 in two of three backgrounds.** Our Track 1
  statement that the ranking is carried by the ClinVar-whitelisted nonsense is not just supported —
  it is the dominant term, worth 88% of the score.

## 4. Pilot, reported separately

`PILOTO_FASE.md` — Exomiser reads phase into ACMG evidence (trans → PM3, cis → BP2) but never into
the compound-heterozygous model; the score penalty for cis is 0.34% and the rank does not move. This
is why the cis/trans stratum was withdrawn and why phase had to be attacked outside the pipeline
(`fase/RESULTADO.md`).

## 5. Predictions scoreboard

| Prediction | Status |
|---|---|
| P-A — 0.5871 above every healthy genome's top score | holds at n = 7 ⏳ n = 37 pending |
| P-A2 — BUB1B absent or < 0.25 in healthy genomes | **confirmed** (absent in 7/7) |
| P-B1 — planted BUB1B rank 1 in 3/3 with real HPO | **confirmed** |
| P-B2 — planted BUB1B rank 1 in ≥ 2/3 with unrelated HPO | **confirmed** (2/3) |
| P-B3 — planted decoy rank 1 in ≥ 2/3 with real HPO | ⏳ re-running (1/1 so far) |
| P-B4 — Δ(real − unrelated) < 0.20 | **confirmed** (0.1684) |
| P-C — monotonic gradient, C-hi − C-lo ≥ 0.10 | **confirmed** (0.8212) |

Technical failures so far: 2 cells (`B_arm2_FANCD2_HG001`, both phenotypes, pre-amendment),
superseded by the amendment-3 re-run and retained in `resultados_todos.tsv`.
