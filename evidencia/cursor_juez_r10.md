The 1 September work is real, and it moved the score **two points**. That is not the ceiling move those artefacts were commissioned for. A hostile panel still hears an unsubmitted Track 2 whose new files argue with each other.

I scored the markdown package. I could not open a regenerated 34-page PDF: `entrega/listo-para-enviar/` contains only `LEEME.md` and the CSV. Commit `8632b221` in the sister repo claims the PDF refresh; this workspace does not have the file.

---

## 1. Scores

Same method as my previous **74**: each dimension /100, then weighted on the official 35 / 25 / 25 / 15 split. Previous Cursor round-7 pass: Rigor 78, Impact 70, Innovation 75, Scalability 70.

| Package | Rigor /100 | Impact /100 | Innovation /100 | Scalability /100 | Weighted |
|---|---:|---:|---:|---:|---:|
| Parental order | 82 | 78 | 55 | 45 | — |
| §6 power (morning + afternoon) | 62 | 48 | 72 | 40 | — |
| MVA2/MVA3 transfer sheet | 58 | 40 | 60 | 72 | — |
| MVA-Replay CLI | 84 | 20 | 70 | 74 | — |
| **Integrated package (what a judge scores)** | **77** | **76** | **75** | **77** | **76** |

Weighted: `0.35×77 + 0.25×76 + 0.25×75 + 0.15×77 = 76`.

| Dimension | Last time (Cursor 74) | Now | Points moved (weighted) |
|---|---:|---:|---:|
| Scientific rigor (35) | 78 → 27.3 | 77 → 27.0 | **−0.3** |
| Potential impact (25) | 70 → 17.5 | 76 → 19.0 | **+1.5** |
| Innovation (25) | 75 → 18.8 | 75 → 18.8 | **0** |
| Scalability (15) | 70 → 10.5 | 77 → 11.6 | **+1.1** |
| **Total** | **74** | **76** | **+2** |

The artefacts moved Impact and Scalability, as promised. They did not move them much, because each one arrived with a hole a domain-expert judge can quote in one sentence. Rigor did not go up. It went slightly down: the morning power headline is now in tension with an afternoon experiment the report does not mention, and the transfer sheet still contains a sentence the report claims to have withdrawn.

This is still a finalist / community-award package, not a first-place package. Fifty-two other teams have BUB1B. Track 2 is still **0 of 3 submissions**.

---

## 2. The four artefacts

### 2.1 Parental order — artefact, not prose. A lab would still redo the primers.

`clinico/PARENTAL_SEGREGATION_ORDER.md` is what I asked for last round: loci, two amplicons, primers, and an interpretation table written before the result, including the *cis* row that would kill Track 1. The primer pipeline is not theatre. `01_primers.py` excludes 1000G SNVs at AF ≥ 0.005 and RepeatMasker intervals; `02_especificidad.py` counts exact copies across GRCh38; `03_verificar_orden.py` checks the page against `primers_finales.json`, with a `--demo` that mutates a base. Git-side, `aa3143f` is a real pre-registration commit for the *other* artefact; the order itself is dated 2026-09-01 and the JSON matches the sequences on the page.

**Strongest hostile objection.** A diagnostic laboratory will not synthesise these primers. They will genotype two known SNVs with their own validated Sanger or NGS assay. Amplicon 1 is **753 bp** with the variant **574 nt from the reverse primer** (`PARENTAL_SEGREGATION_ORDER.md` lines 75–80). That is a long Sanger product; the reverse read will not cleanly cover the variant if the read is 500–600 nt. Forward Tm is **57.4 °C** against three primers at ~60 °C, and the page still says both amplicons are “compatible in the same run” at 57 °C (lines 82–84). Specificity is **exact-match only**; the page admits that (lines 101–103), which is the right disclaimer and also the reason the sequences are not a deliverable a lab can order. `primers_finales.json` shows `rank_used: 0` and `worst_candidate_copies: 1` for both amplicons: *with* RepeatMasker on, every primer3 candidate was already unique. The AluY “~100 copies” story is a counterfactual of the unconstrained design, not a pair they discarded at the copy-count step.

**Wrong, not just weak.** Nothing in the sequences or coordinates is wrong against the JSON. Test B (parental PCS, lines 105–113) is labelled a two-family hypothesis; that is honest. What is wrong is the Impact *framing*: this is a template a treating clinician might adapt, written by a team with no access to the patient (lines 13–16). That is still the highest-Impact object in the repo. It is not a signed order, and it does not change Monday unless someone who can sign it receives the Track 2 submission.

---

### 2.2 Power calculation — real arithmetic, rhetorical correction, and then a buried second experiment.

The morning package is a real calculation. `aa3143f` (“Pre-register the power calculation… before computing it”) precedes `eec870c` (the results). Seeded code, 2,000 simulations, failed fits counted as non-rejections, sweeps that include the reading they wanted to kill. `resultados.json` matches `RESULTADOS.md` to Monte Carlo noise (`power_central` 0.8975 vs sweep `f=0.3` 0.9045).

**The 0.02 vs 0.30 distinction is a real arithmetic correction, and it is also rhetorical.**

It is real for the question “what fraction of cells is aneuploid?” Thirty percent of cells with one error, spread over 22 autosomes, is ~1.4% per chromosome. That *is* the right denominator for §5 (can bulk WGS see a given chromosome). It is the wrong denominator for “is *a cell* aneuploid.” Report §6 now says that (`REPORT_track2_EN.md` lines 532–543). So far, fine.

It is rhetorical because proteotoxic load is not a switch. Ippolito’s EC50 is from *highly* aneuploid cancer lines. An MVA cell with one extra chromosome is not that object. The morning mixture assigns every aneuploid cell `E_aneu = 40 nM`, i.e. the Ippolito extreme, then reports power 0.897 for “4× EC50 selectivity in a culture where 30% of cells carry an aneuploidy.” That sentence hides the number in their own JSON:

```38:40:potencia/resultados.json
    "0.3": {
      "max_abs_viability_gap": 0.09890109890109888,
      "ec50_ratio": 1.4979956796914413
```

At the central scenario the bulk patient-vs-control EC50 ratio is **1.50×**, not 4×. The 4× lives only in the 30% subpopulation. The go criterion in the report is not “detect 1.5×.” It is:

```571:574:track2/REPORT_track2_EN.md
1. **A dependency signal, not merely a sensitivity difference:** an EC50 shift between patient and control fibroblasts whose 95% confidence interval excludes 1, of a magnitude at least equal to the near-euploid-versus-highly-aneuploid contrast in Ippolito Fig. 6o. A shift smaller than that is not
   the effect we predicted.
```

Ippolito 6o is a contrast between two *homogeneous* populations. Under the team’s own mixture, a 30% mosaic cannot produce that bulk contrast. They powered a *t*-test that will fire on 1.5×, then set a go bar the generative model cannot reach. Power 0.897 is for a different decision than §6’s advancement rule.

Further, the noise model has no biological-replicate variance: `n=3` “biological” curves differ only by per-well lognormal CV 0.10 (`01_potencia.py` lines 56–62). At well CV 0.15, their own sweep drops power to 0.593 (`RESULTADOS.md` line 92). The preregistration says “four-parameter Hill” (`PREREGISTRO.md` lines 74–76); the code fits two parameters with top fixed at 1 and bottom at 0 (`01_potencia.py` lines 37–49). That is a mismatch, not a quibble.

**They already knew the dose objection by the afternoon, ran it, and did not put it in the report.** `PREREGISTRO_2_DOSIS.md` (commit `45c4ed72`, after the morning result) states the hostile reviewer’s point in their own words: mean altered chromosomes per aneuploid cell ≈ 1.0, so the mixture is “binary where the biology is graded” (lines 15–24). Pre-committed rule: if `|Δ₂|/σ < 0.10` in solids, the 4× central scenario “is then not defensible” and they “must say” so in `RESULTADOS.md` and Track 2 §6 (lines 61–65). If the solid slope’s CI covers 0, call the exercise uninformative (lines 69–73), and they noted that outcome was *likely*.

`dosis.json`: solid slope −0.0056/arm, CI **[−0.0118, +0.0006]** (covers 0), `|Δ₂|/σ = 0.020`. They took the uninformative hatch. The magnitude they pre-registered as fatal is 0.020, five times below the 0.10 kill line. Haematological `|Δ₂|/σ = 0.093` is also under 0.10, in the lineage where the dependency *exists*. The unregistered post-hoc in solids, ≤4 vs ≥16 arms, is p = 0.30 (`dosis.json` lines 45–51). None of this is in `potencia/RESULTADOS.md` or Track 2 §6. The morning headline still stands: “the §6 assay is in the right effect regime.”

That is the new hole of 1 September. Not a missing artefact. An artefact that cut against them, then did not enter the deliverable.

---

### 2.3 Transfer sheet — a filled worksheet, with the filters moved.

`TRANSFER_MVA2_MVA3.md` is not prose pretending to be a table. Two worksheets, same candidate, different verdicts, empty cells left empty, the CEP57 inference flagged before a reviewer does it (lines 67–75). That is the demonstration I asked for.

**Strongest hostile objection.** The filters were not held fixed. Filter 2 in the report is:

```191:191:track2/REPORT_track2_EN.md
| 2 | Mechanistic | Does it address the actual lesion or a direct consequence of it? | Agents acting on uninvolved pathways |
```

The appendix scores MVA1 bortezomib filter 2 as **“Yes — proteasome dependency of aneuploid cells”** (`REPORT_track2_EN.md` line 809). Biallelic *CEP57* causes “constitutional mosaic aneuploidies” (they quote PMID 21552266 at line 69 of the transfer sheet). If filter 2 is the aneuploid *state*, MVA2 is Yes or not-evaluable, not No. They failed it by importing SAC *severity* and the absence of published cancer — the latter is filter 4’s inversion condition. Line 65 of the transfer sheet says so in one cell: “Rejected at filter 2 … **and** no clinical setting in which filter 4 could invert.” Report §9 repeats the conflation (lines 726–729) while claiming “the filters held fixed” (line 726). A framework that kills the candidate in MVA2 only after changing what filter 2 means is still a slogan, just with two extra rows.

**Wrong.** Line 107–108 still says a negative §6 result is “ambiguous by the same design.” Report §6 withdrew that sentence the same day (lines 532–543). That is a false statement in a file §9 tells the judge to open.

---

### 2.4 MVA-Replay CLI — a real tool. “An afternoon” is false.

`replay/mva_replay.py` is one file. `--self-check` exists and is built to fire: it asserts that `HP:0000365` is annotated to BUB1B and that the new default set is not (`mva_replay.py` lines 296–298). The default control was updated (lines 31–37). The r9 JSONs exist and match `hpo/RESULTADOS.md` §6: 0.3965 in all three backgrounds, ranks 1 / 2 / 3 (`replay/out_r9/BUB1B_HG00{1,2,5}_r9.json`).

**Strongest hostile objection.** Another team cannot spike a gene “in an afternoon” (`REPORT_track2_EN.md` lines 732–736; `README_TOOL.md` lines 20–23). The script hard-requires this repo’s Exomiser 15.1.0, the 2602 hg38 data (~55 GB), `tools/analysis_mva.yml`, a ClinVar VCF and `genes_to_phenotype.txt`. Without that stack it is a wrapper with no engine. One gene, two alleles, sequential Java. The ClinVar “counterfactual” only drops the whitelist (`README_TOOL.md` lines 83–89); they already know the honest counterfactual is a different unclassified allele. Scalability of a frozen local pipeline is real for *this* disease and thin for “any rare disease.”

**Wrong.** Nothing in the CLI contract is false. The overclaim is the afternoon.

---

## 3. Re-submit Track 1?

**For.** The submitted report still says the unrelated control was “verified against the same annotation set as absent from MVA1” and scores **0.4187** (`entrega/methods_track1.md` lines 104–107). That sentence is now known to be false: HP:0000365 is annotated to MVA2, ORPHA:1052, BUB1B, CEP57 and TRIP13 (`hpo/RESULTADOS.md` lines 15–16; `hpo/verificacion.json`). The team’s brand is catching its own errors. Leaving a known false number, after already re-submitting once for the identical class of contamination, is the thing a write-up judge is trained to notice. The CSV does not change. Quota is 4 of 6 left.

**Against.** Track 1 does not differentiate: 52 of 53 teams already had the answer, the evaluator scores the CSV, and 100/100 is already in. A correction that only patches 0.4187 → 0.3965 while keeping “variant-driven, still rank 1 under unrelated HPO” would be a new framing error, because the clean set loses rank in two of three GIAB backgrounds (`hpo/RESULTADOS.md` lines 89–109). Publishing that softening in Track 1 advertises four prior errors (the retired 24%, ClinVar, 4,565 rows, now this) that a judge who never opened HPOA would not have found. This team’s distinctive failure mode is transcription while “fixing.” A fifth resubmit is another chance to mint a fifth error. The podium is the Track 2 write-up, which is not in the queue.

**Recommendation: do not resubmit Track 1 until Track 2 has used a submission.** If Track 2 is in and quota remains, one honesty patch is worth it, and only if the *claim* is rewritten to the sentence already in `hpo/RESULTADOS.md` lines 105–109, not just the number. Resubmitting now, at 0/3 on Track 2, is editing the document that does not decide the podium.

---

## 4. Contradictions

**§5 “1–2% of cells” vs `potencia/RESULTADOS.md`.** Not a contradiction if you read §6. §5 uses 1–2% for bulk WGS of *one chromosome* (`REPORT_track2_EN.md` lines 498–503). That is the right denominator. The morning power note explains why §6 had been using it for the wrong question (lines 535–538).

**`TRANSFER_MVA2_MVA3.md` vs §6.** Yes. Transfer lines 128–131 still use the per-chromosome 1–2% as the reason a fibroblast culture “may simply not be aneuploid enough,” and lines 107–108 keep “a negative result is ambiguous by the same design.” That is the hedge §6 withdrew.

**`TRANSFER` vs §9.** Verdicts agree (filter-2 kill in MVA2, conditional in MVA3). Both files claim the filters were held fixed; both smuggle filter 4 into filter 2. That is agreement in the error, not a cross-file clash. §3.5’s solid-lineage attenuation is carried into the MVA3 sheet (TRANSFER lines 95–100); that part is consistent.

**`hpo/RESULTADOS.md` §2 vs §6.** They do not formally contradict: §2 has a warning box pointing at §6 (lines 43–46). A skimmer who stops at §2 (“the finding is variant-driven,” line 38) is being sold a sentence §6 narrows. **§6 is wrong on a different point.** It says that with the contaminated r7 set, BUB1B “came first under unrelated phenotypes in every background” (lines 100–101). The team’s own benchmark already reported r7 ranks **1 / 1 / 3** (`replay/RESULTADOS.md` lines 88–99; submitted Track 1 lines 270–272). The clean set changed HG002 from 1 to 2. It did not change “won everywhere” into “not everywhere.” That was already not everywhere. Inflating the r7 baseline makes the r9 wound look bigger than it is.

**New, and not in the four named files: afternoon vs morning power.** `PREREGISTRO_2_DOSIS.md` obligated a recant or an uninformative report in `potencia/RESULTADOS.md` and §6. `dosis.json` exists. The report still leads with power 0.897 at 4×. That is the same class of error as every previous round: the report contradicts the team’s own material.

---

## 5. Highest-return remaining

**Stop analysing. Ship Track 2 this week.**

Not a fifth artefact. The discontinuous payoff is a judge reading this package. Right now they cannot. The only hard blocker is a YouTube/Vimeo URL for **video v3**, not the old one (`CONTINUAR-AQUI.md` lines 84–85, 171–175). Quota is 3; sitting on 0 of 3 with eight weeks left is how a 76 loses to a noisier but submitted 70.

Shipping work, concretely, in one afternoon:

1. Upload `video/pitch_MVA2026.mp4` (v3). Confirm the public URL.
2. Two-hour consistency pass, because a judge who opens the companions will quote them: delete TRANSFER lines 107–108 and 128–131 (the withdrawn hedge and the 1–2% proteotoxicity reuse); add one paragraph to §6 stating that the afternoon DepMap-slope attack was uninformative in solids and that `|Δ₂|/σ = 0.020` would have failed the pre-registered 0.10 bar; fix `hpo/RESULTADOS.md` line 100 (“every background” → “2 of 3, already lost on HG005”).
3. Put the URL in the Track 2 form and submit `ciberpty_track2_report.pdf`. Keep two shots.

Do not wait for the mosaicism 1000G pilot. Do not resubmit Track 1 first. Do not build a fifth analysis. The 1 September work bought two points. The remaining points are in the inbox of a judge who has not been sent the file.
