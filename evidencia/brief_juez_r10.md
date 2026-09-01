# Round 10 — judge the package again, after the Impact and Scalability work

You have judged this package before. Your last two scores were **78** (Codex) and **74** (Cursor) on
the official rubric — **Rigor 35 / Impact 25 / Innovation 25 / Scalability 15** — and you both said
the same thing: Rigor is near saturated, and the ceiling sits in **Impact (25) and Scalability (15),
which were at zero**. You both named the specific artefacts that would move them.

**Those artefacts now exist.** This round asks whether they actually moved the score, and whether
anything built on 1 September introduced a new hole.

Competition: "Rare Disease, Real Kid" (Sage Bionetworks + Hugging Face). Closes **24 October 2026**.
Single podium across both tracks, not one per track. Track 1 is submitted and scored 100/100 by the
automated evaluator (which scores the CSV, not the report). 52 of 53 teams already had the same
answer, so Track 1 does not differentiate. Track 2 is written but **not submitted** — 0 of 3
submissions used — blocked only on a video URL the team lead must supply.

---

## Read these, in this order

Everything is under `/home/gar16/datos/HACKATHON-MVA-2026`.

**The four new artefacts (1 September):**

1. `clinico/PARENTAL_SEGREGATION_ORDER.md` — the Impact artefact. A one-page laboratory request for
   parental segregation testing: two Sanger amplicons, primers designed against GRCh38 with common
   1000G SNVs and RepeatMasker intervals excluded, then verified single-copy across the entire
   assembly. Interpretation table written before the result, covering five outcomes including two
   that would refute the team's own Track 1 answer.
   Code: `clinico/01_primers.py`, `clinico/02_especificidad.py`, `clinico/03_verificar_orden.py`.

2. `potencia/PREREGISTRO.md` → `potencia/RESULTADOS.md` — a power calculation for the §6 go/no-go
   experiment, pre-registered and committed as `aa3143f` **before** it ran. Claims the report's own
   hedge ("a negative result is ambiguous by design") rested on an arithmetic error: the "1–2% of
   cells" figure is **per chromosome**, and the quantity the assay depends on is the fraction of
   cells with *at least one* aneuploidy. Power 0.897 under the correct reading, 0.063 under the
   implied one. Code: `potencia/01_potencia.py`, raw output `potencia/resultados.json`.

3. `track2/TRANSFER_MVA2_MVA3.md` — the Scalability artefact. The five-filter worksheet filled
   prospectively for MVA2 (*CEP57*) and MVA3 (*TRIP13*) with the same candidate, filters held fixed.
   Claims different verdicts: bortezomib rejected at filter 2 for MVA2, conditional for MVA3.

4. `replay/mva_replay.py` + `replay/README_TOOL.md` — MVA-Replay packaged as a one-file CLI. Takes a
   gene, two alleles, an HPO set and a background VCF; returns planted score, rank, the
   ClinVar-stripped counterfactual and an unrelated-HPO control. Has `--self-check`.

**The finding that came out of building them:**

5. `hpo/RESULTADOS.md` — **read this one carefully, it cuts both ways.** The packaged tool's own
   warning fired on the team's own control set: `HP:0000365` (hearing impairment), one of the five
   "unrelated" control terms **in the Track 1 report that is already submitted**, is annotated to
   MVA2 (OMIM:614114), to ORPHA:1052 and directly to *BUB1B*, *CEP57* and *TRIP13*. The round-7 fix
   had checked MVA1 only. Re-run clean: BUB1B still rank 1 in the proband but score **0.3965**, not
   the submitted 0.4187. **And §6 of that file reports a second consequence that goes against the
   team**: with the clean set on three GIAB backgrounds the score is invariant (0.3965 in all three)
   but the rank is 1, 2 and 3 — BUB1B is displaced in two of three.
   Code: `hpo/01_verificar.py`, `tools/control_hpo_r9.sh`, runs in `replay/out_r9/`.

**How they were folded into the deliverable:**

6. `track2/REPORT_track2_EN.md` — §6 (rewritten around the power result and a new gating
   measurement), §7 (points at the clinical order), §9 (points at the transfer sheet and the tool),
   and the "Read this first" page. PDF regenerated at 34 pages.

**Context you may need:** `CONTINUAR-AQUI.md` (state and the map of which file wins when two
contradict), `mosaico/PREREGISTRO.md` amendments 3 and 4, `depmap/RESULTADOS.md`,
`replay/RESULTADOS.md`, `fase/RESULTADO.md`.

---

## What I want from you

Be brutal. Do not be encouraging. The team lead asked directly whether this is going well or whether
it can be improved, and a comfortable answer is useless to him.

1. **Score it now, package by package and overall, against the official rubric.** Give a number per
   dimension, not a vibe. Compare against your own previous 78 / 74 and say explicitly **how many
   points, if any, the 1 September work actually moved** — and in which dimension. If it moved
   nothing, say that.

2. **Attack the new artefacts.** For each of the four:
   - Is it what it claims to be, or is it prose dressed as an artefact?
   - What is the single strongest objection a hostile judge with domain expertise raises?
   - Is there anything in it that is *wrong*, as opposed to merely weak?
   Pay particular attention to the power calculation: its mixture model, its parameter choices, and
   whether the "0.02 vs 0.30" framing is a real correction or a rhetorical one. And to the primer
   design: would a diagnostic laboratory actually use that page, or would they redo it?

3. **The self-inflicted wound.** The clean HPO control weakens the "variant-driven" claim in a report
   that is **already submitted**, and the team has 4 of 6 re-submissions left. Given that Track 1
   does not differentiate anyway and the podium is decided on the write-up: **is re-submitting worth
   it, or does it just draw a judge's attention to four errors they would never have found?** Argue
   both sides, then give a recommendation.

4. **Contradiction hunt — this is the one that has mattered most in every previous round.** In every
   round, the worst error was a statement in a report that contradicted the team's own material, not
   a misquoted external fact. Cross-check the new files against each other and against the reports.
   Specifically: does `potencia/RESULTADOS.md` contradict §5 of the Track 2 report, which still uses
   "1–2% of cells" for a different purpose? Does `hpo/RESULTADOS.md` §2 contradict its own §6? Does
   anything in `TRANSFER_MVA2_MVA3.md` contradict §9 or §3.5 of the report?

5. **With eight weeks left: what is the highest-return thing remaining?** One answer, not a list. If
   your answer is "stop analysing and ship", say so plainly — but then say what the *shipping* work
   is, concretely. If the answer is a fifth artefact, name it and estimate the days.

Output: a scored table first, then the objections, then one recommendation. Cite file and line for
every criticism so it can be checked. If you cannot open a file, say so rather than guessing.
