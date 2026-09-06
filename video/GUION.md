# 3-minute pitch — script v4

✅ **Rendered 2026-09-06.** `pitch_MVA2026.mp4` narrates this script: 177.87 s by ffprobe, 8 slides
rendered from `deck.html`. 176.08 s by ffprobe.

Target ≤ 180 s. Judging: Rigor 35% · Impact 25% · Innovation 25% · Scalability 15%.

**Why v4 (06-Sep-2026).** v3 spent its time narrating our corrections and showed no result of our own.
The four changes:

- **S3** described "twelve controls" and the version of the unrelated-symptom control that was still
  contaminated. It now gives the corrected number, and the part that goes against us: the score is
  identical across genomes, the *rank* is not.
- **S6** presented bortezomib's mechanism without our own test of it. It now states the DepMap result,
  which weakens our case, because that is the only result in this project that came from our own
  computation on a public dataset.
- **S8** claimed the framework scales without showing anything runnable. It now names MVA-Replay, the
  tool another team can run, and the decision each result would change.
- Throughout: nothing claims a demonstrated benefit of bortezomib in this child or in MVA.

---

## S1 — 38 w

A child survived an embryonal rhabdomyosarcoma. His cells miscount chromosomes when they divide — mosaic variegated aneuploidy. We were asked which approved drug could help him. The honest answer today is none. What we can offer is the evidence behind that no, and what would change it.

## S2 — 58 w

First the variant. Two independent analyses, required to agree: a hypothesis-free genome-wide run driven only by his eight clinical terms, and an eleven-gene panel with coordinates fetched from a versioned database. Both land on BUB1B — one nonsense allele, one missense. We cannot prove the two sit on opposite chromosomes. There are no parental samples, so this is a diagnosis pending segregation.

## S3 — 59 w

Our replay tool plants known alleles into public healthy genomes. We also asked thirty-seven unspiked ones the same symptoms: none scores higher than this case. Then we caught our own contaminated control, twice. Cleaned up, the score is identical in every background — but the rank is not, and one pre-registered prediction is falsified. We said in advance we would publish that.

## S4 — 45 w

For the drug, five filters instead of the usual two. Approval and a plausible mechanism are necessary but not enough. Filter three is pharmacokinetic: does the achievable plasma level reach the concentration that works in a dish? Filter five, rarely applied: does the drug make mis-segregation worse?

## S5 — 41 w

Metformin is the candidate the literature points to. Nobody has measured what concentration it needs against aneuploid cells, so it cannot be evaluated on the mechanism proposed. And that mechanism, inhibiting complex one, needs a thousand times more drug than is safe.

## S6 — 61 w

Bortezomib clears filter three, and then we tested it against ourselves. We pre-registered a question on public cancer data: does the aneuploidy–proteasome link extend to solid tumours? It does not. This child's tumour was solid. So the dependency is established in cancer aneuploidy, not in his cells. We have not shown it transfers.

## S7 — 43 w

Bortezomib also fails filter four for him: motor neuropathy in eight percent of children, on existing muscle atrophy. What changes his prognosis today is not a molecule, it is surveillance, and published consensus says renal ultrasound every three months until he is seven.

## S8 — 55 w

Two things scale. The five-filter worksheet, for any rare disease where someone proposes an approved drug. And the replay tool, which another team can run on their own gene in an afternoon. What we hand over is not a prescription. It is a prepared answer, with the measurement that would overturn it.

---

## Build record

Rendered 2026-09-06 from `deck.html` with `render_video.py`; narration by Qwen3-TTS 1.7B VoiceDesign
on CPU, every clip checked against this script by speech recognition (`tts_verify.py`). Measured total
**176.08 s** (ffprobe), not extrapolated.

S7 was re-synthesised once: the first take dropped the word "to" from *"every three months, to age
seven"*. The line now reads *"until he is seven"*, which the recogniser confirms is spoken in full.
