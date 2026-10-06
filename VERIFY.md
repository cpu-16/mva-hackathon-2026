# How to verify that every pre-registration precedes its result

**Team: ciberpty** · This file exists because a pre-registration is only worth the timestamp behind
it. An external reviewer told us they could not check ours, so here is the check, in one command.

Clone the repository and run:

```bash
git log --format='%h  %cI  %s' --reverse
```

Every design document below was committed **before** the analysis it describes was run, and every
amendment is appended and dated rather than editing the text above it. The pairs:

| Design, committed first | Commit | Committed at (ISO 8601) | Result, committed after | Its first commit |
|---|---|---|---|---|
| `depmap/PREREGISTRO.md` | `4b0b7c2` | 2026-08-30T13:18:33-05:00 | `depmap/RESULTADOS.md` | `38a9d4f` 2026-08-30T13:32:38-05:00 |
| `replay/PREREGISTRO.md` | `8086dd4` | 2026-08-30T14:34:01-05:00 | `replay/RESULTADOS.md` | `d95dbe7` 2026-08-30T15:07:27-05:00 |
| `mosaico/PREREGISTRO.md` | `ed0feae` | 2026-08-30T17:29:35-05:00 | `mosaico/RESULTADOS.md` | `453d20a` 2026-08-30T19:34:16-05:00 |
| `potencia/PREREGISTRO.md` | `aa3143f` | 2026-09-01T16:39:47-05:00 | `potencia/RESULTADOS.md` | `eec870c` 2026-09-01T17:22:44-05:00 |
| `potencia/PREREGISTRO_2_DOSIS.md` | `45c4ed7` | 2026-09-01T17:36:04-05:00 | `potencia/RESULTADOS_2_DOSIS.md` | `8c33031` 2026-09-01T17:43:17-05:00 |
| `depmap/PREREGISTRO_SEGUIMIENTO.md` (follow-up, registered after the first result) | `ee59c9e` | 2026-09-07T23:41:48-05:00 | `depmap/RESULTADOS_SEGUIMIENTO.md` | `612a0f1` 2026-09-07T23:46:51-05:00 |
| `replay/TRANSFER_TRIP13.md` pre-registration | `ee7a050` | 2026-09-07T22:10:02-05:00 | `replay/TRANSFER_TRIP13.md` results + logs | `8956240` 2026-09-07T22:22:51-05:00 |
| `potencia/PREREGISTRO_4P.md` | `fa9eaae` | 2026-09-08T00:09:27-05:00 | `potencia/RESULTADOS_4P.md` (amendment 1 entered with the results; see its provenance note) | `8cee494` 2026-09-08T00:33:46-05:00 |
| `mosaico/PREREGISTRO.md` amendment 4 + analysis code | `6405d9e` 2026-09-01T16:55:40-05:00 → `138a40f` 2026-09-01T18:53:39-05:00 | see left | `mosaico/CONTROL_RESULTADO.md` | `ce94b89` 2026-09-01T21:42:52-05:00 |

**The sixth pair is the one a hostile reviewer should check first, because its result goes against
us** — the external control came back *not conclusive* and left the mosaicism finding withdrawn. It
also needs a caveat we would rather state than have found:

> The commit message on `138a40f` reads *"Write the control analysis before the control data exists"*,
> and that is **imprecise**. The analysis code was committed at 18:53:39, but
> `mosaico/piloto/chr8.tsv.gz` already existed on the analysis machine from 18:39 — the chr8 extraction
> had finished first. The accurate statement, which is the one `CONTROL_RESULTADO.md` makes, is that
> the code was fixed **before the chr17 data existed**. A commit message cannot be edited after the
> fact without breaking the very ordering this file asks you to trust, so we leave it and correct it
> here. Amendment 4 (`6405d9e`, 16:55:40) does precede both extractions, and it is the amendment that
> fixes the windows and the decision rule.

Check any single pair directly:

```bash
git show -s --format='%cI  %s' <design-commit>     # when the design was fixed
git log --diff-filter=A --format='%cI  %s' -- <result-file>   # when the result first appeared
```

## What this does and does not prove

- **It proves ordering of commits within this repository**, and the push history on GitHub gives an
  independent server-side timestamp for when each commit was received. Commit dates are writable by
  the committer; the push timestamps are not, and they are the stronger evidence.
- **It does not prove that nobody had already seen the data.** Nothing in a git history can prove
  that, and we do not claim it. Files land on the analysis machine without touching this repository —
  the sixth pair above is a worked example of exactly that gap. What the history does establish is
  that the hypotheses, parameters, decision rules and the sentences to be written for each outcome
  were fixed and published before the numbers existed in any document we show you.
- **Amendments are appended, never retro-edited.** `git log -p -- <file>` shows this: each amendment
  is an addition at the end of the file, with its own date, and the text above it is untouched.

## The point of the exercise

Several of the pre-registered analyses produced results that **weakened our own argument**, and all of
them are reported:

- the DepMap test found the proteasome dependency does not extend to solid tumours, and this child's
  tumour was solid;
- the mosaicism result was **withdrawn** when the pre-registered statistic fired on 22 of 22
  chromosomes, and the external control designed to rescue or kill it came back **not conclusive**;
- the dose analysis removed the empirical support for the 4× selectivity the power calculation had
  been centred on — without refuting it, which is a distinction we got wrong once and corrected on
  2026-09-06;
- in the retrieval benchmark, the corrected unrelated-phenotype control **falsified** prediction P-B2,
  which the pre-registration had said in advance we expected our own pipeline to fail.

The pre-registration is what makes those reports credible rather than decorative. Corrections made
after a result is known are appended with their date, in the results file, and never applied to the
pre-registration itself.
