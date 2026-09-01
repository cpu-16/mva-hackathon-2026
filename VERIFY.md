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

Check any single pair directly:

```bash
git show -s --format='%cI  %s' <design-commit>     # when the design was fixed
git log --diff-filter=A --format='%cI  %s' -- <result-file>   # when the result first appeared
```

## What this does and does not prove

- **It proves ordering within this repository**, and the push history on GitHub gives an
  independent server-side timestamp for when each commit was received.
- **It does not prove the analysis had not been run before the design was committed.** Nothing in a
  git history can prove that. What it does establish is that the hypotheses, parameters, decision
  rules and the sentences to be written for each outcome were fixed and published before the
  numbers existed in any document we show you.
- **Amendments are appended, never retro-edited.** `git log -p -- <file>` shows this: each amendment
  is an addition at the end of the file, with its own date, and the text above it is untouched.

## The point of the exercise

Three of the five pre-registered analyses produced results that **weakened our own argument**, and
all three are reported: the DepMap test found the proteasome dependency does not extend to solid
tumours (the child's tumour was solid); the mosaicism result was **withdrawn** when the
pre-registered statistic fired on 22 of 22 chromosomes; and the dose analysis undercut the power
result we had published hours earlier the same day. The pre-registration is what makes those
reports credible rather than decorative.
