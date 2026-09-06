# 3-minute pitch — script v4

⛔ **NOT RENDERED.** `pitch_MVA2026.mp4` still narrates **v3** (archived in `GUION_v3.md`). The v4
narration has not been synthesised, the slides listed below have been edited in `slides.html` but
**not re-rendered to PNG**, and the video has not been reassembled. Nothing here is ready to upload.
See "What is blocking this" at the bottom.

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

## S3 — 60 w

To test the retrieval we built a tool that plants known alleles into public healthy genomes. Across thirty-seven of them, none scores higher than this case. Then we caught our own contaminated control, twice. Cleaned up, the score is identical in every background — but the rank is not, and one pre-registered prediction is falsified. We said in advance we would publish that.

## S4 — 45 w

For the drug, five filters instead of the usual two. Approval and a plausible mechanism are necessary but not enough. Filter three is pharmacokinetic: does the achievable plasma level reach the concentration that works in a dish? Filter five, rarely applied: does the drug make mis-segregation worse?

## S5 — 41 w

Metformin is the candidate the literature points to. Nobody has measured what concentration it needs against aneuploid cells, so it cannot be evaluated on the mechanism proposed. And that mechanism, inhibiting complex one, needs a thousand times more drug than is safe.

## S6 — 61 w

Bortezomib clears filter three, and then we tested it against ourselves. We pre-registered a question on public cancer data: does the aneuploidy–proteasome link extend to solid tumours? It does not. This child's tumour was solid. So the dependency is established in cancer aneuploidy, not in his cells. We have not shown it transfers.

## S7 — 42 w

Bortezomib also fails filter four for him: motor neuropathy in eight percent of children, on existing muscle atrophy. What changes his prognosis today is not a molecule, it is surveillance, and published consensus says renal ultrasound every three months, to age seven.

## S8 — 55 w

Two things scale. The five-filter worksheet, for any rare disease where someone proposes an approved drug. And the replay tool, which another team can run on their own gene in an afternoon. What we hand over is not a prescription. It is a prepared answer, with the measurement that would overturn it.

---

## What is blocking this

Nothing scientific. The session that wrote v4 could not execute Piper, ffmpeg or the slide renderer,
so:

1. `audio/S1..S8.wav` still hold the **v3** narration.
2. `slide01..08.png` still hold the **pre-v4** slides, even though `slides.html` has been updated.
3. `pitch_MVA2026.mp4` is therefore **the v3 video**, unchanged, 2:59.0.

To finish, in order: `python3 render.py` (slides → PNG), re-synthesise S1–S8 with Piper at
**`--length-scale 1.415`**, then reassemble with the `-t $A` recipe in `README.md`. **Measure the
total; the word counts above are estimates, not timings.** v3 was **411 narration words for 179.0 s**;
v4 is **408**, which extrapolates to about **177.7 s** at the same speaking rate. That is an
extrapolation, not a measurement, and it has to be confirmed with `ffprobe` before anyone calls this a
three-minute video. If it exceeds 180 s, cut script — do not speed up the voice.

Recount the narration at any time with:

```bash
grep -h "^A child survived\|^First the variant\|^To test the retrieval\|^For the drug\|^Metformin is the\|^Bortezomib clears\|^Bortezomib also\|^Two things scale" GUION.md | wc -w
```
