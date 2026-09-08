# 3-minute pitch — script v5 (documentary cut)

Target ≤ 180 s including a silent title beat, four chapter cards and a closing card. Judging: Rigor 35% · Impact 25% · Innovation 25% · Scalability 15%.

**Why v5 (08-Sep-2026).** The v4 video was frozen on 6-Sep, before the report reconciled every headline with its evidence (Codex-as-judge round, 7/8-Sep). It still said *"Bortezomib clears filter three"* and *"If that tumour comes, filter four inverts"*, two sentences the report retired on purpose, and it carried none of the 7/8-Sep results (free-drug margin, DepMap follow-up by lineage, power 0.17 at n = 3, TRIP13 transfer, one-command regeneration). A video more triumphant than the paper is a self-contradiction a judge catches. v5 was drafted from Part I of the submitted document, fact-audited sentence by sentence by Codex (gpt-6-astra) against that text (`evidencia/codex_guion_v5_2026-09-08.md`), and the Track 1 sentences it could not see were verified against `submission/ciberpty_track1_report.md` before they went back in.

Every sentence below maps to a section of the report; the on-screen provenance line of each scene names it.

## S1 — cold open — 44 w

A child survived an embryonal rhabdomyosarcoma. His family shared his genome so that strangers might help. Which approved drug could help him, in mosaic variegated aneuploidy? Our answer: no drug should be started for this today. Here is why, and what would change it.

## S2 — the variant — 39 w

The presumed cause: two BUB1B variants, from two independent analyses. One introduces a stop. The other is a missense of uncertain significance. Whether they sit on opposite copies of the gene is not established. There is no parental sample.

## S3 — the control — 37 w

Our replay tool plants known alleles into public healthy genomes. Thirty-seven unspiked genomes, asked the same symptoms: none scores higher than this case. We caught our own contaminated control, twice. One pre-registered prediction is falsified, and published.

## S4 — five filters — 34 w

Five filters, not the usual two: approval, mechanism, exposure, safety in this child, direction of effect. A plasma peak is only a plausibility check. And among the cells that survive, is mis-segregation made worse?

## S5 — metformin — 37 w

Metformin, the candidate the literature points to: no aneuploidy-selective effective concentration has ever been measured for it, and the complex one mechanism proposed for it needs about a thousand times the therapeutic plasma level. Not disproven. Unevaluable.

## S6 — bortezomib, against ourselves — 51 w

Bortezomib is not excluded by the exposure check; on free drug, the margin is unknown. We tested it, pre-registered, on public cancer data. Across four hundred and forty-four solid tumour lines, no proteasome inhibitor reached significance, and the target association is weaker in solid tumours. His tumour type was barely represented.

## S7 — safety, filter four — 52 w

It fails the safety filter for him: neuropathy in eighteen percent of children in the paediatric trials, on existing muscle atrophy. Alone, it produced no objective responses in paediatric solid tumour trials. If a tumour returns, the comparator becomes chemotherapy, and the question goes to a tumour board, after a laboratory gate.

## S8 — the experiment — 40 w

The experiment that could prove us wrong: his own fibroblasts, a bortezomib dose response, micronuclei among survivors. Under our pre-registered model, three cultures per arm give power of seventeen percent; twelve are needed. Sensitivity alone could mean toxicity, not benefit.

## S9 — what helps today, what scales — 35 w

What helps him today is surveillance, published consensus: renal ultrasound every three months to age seven. What scales: eight pre-registrations, a five-filter worksheet reusable as questions, and a replay tool transferred to a second gene.

## S10 — close — 18 w

Not a prescription. A prepared answer, written down now, with the measurements that would change the next decision.

**Total: 387 narrated words.**

## Build record

Rendered 2026-09-08 from `deck.html` with `render_video.py` (12 Chromium pages in parallel); narration by
Qwen3-TTS 1.7B VoiceDesign on the RTX 4060 (15 s per clip; the first pass of the day ran on CPU at
~60 s per clip), every clip checked against this script by speech recognition (`tts_verify.py`,
whisper base.en; S1, S5 and S7 re-checked with large-v3-turbo because base.en heard «embryonic»,
«effect of» and «and 18%» — the large model confirms the script is spoken as written). Raw clips in
`audio_raw_v5/`; the clips in `audio/` carry `atempo=1.06` so the narration plus the six silent beats
fits under 180 s. Measured total by ffprobe: see the README table.

Two adversarial passes by Codex (gpt-6-astra): the script audit before synthesis
(`evidencia/codex_guion_v5_2026-09-08.md`) and the panel-judge read of the first render
(`evidencia/codex_juez_video_v5_2026-09-08.md`, 76/100), whose fixes are in this cut. S1, S5, S7 and
S10 were re-synthesised after that read.
