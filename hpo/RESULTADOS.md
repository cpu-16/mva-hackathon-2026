# The unrelated-HPO control was contaminated a second time

**Team: ciberpty** · 2026-09-01 · Found by our own tool, not by a reviewer.

---

## 1. What happened

The Track 1 report rests on a control that answers the question *"does this pipeline put BUB1B first
even when the phenotype is wrong?"*. It has now been contaminated twice, for the same reason both
times: **the term set was checked against MVA1 only.**

| Round | Control terms | Problem |
|---|---|---|
| Original | seizures, hearing impairment, atrial septal defect, conjunctivitis, recurrent respiratory infections | Two terms (HP:0001250, HP:0001631) are annotated to **MVA1** (OMIM:257300). Found before the second submission; the report was re-submitted corrected |
| r7 — **the version currently submitted** | **hearing impairment**, conjunctivitis, recurrent respiratory infections, headache, pruritus | **HP:0000365 (hearing impairment) is annotated to OMIM:614114 (MVA2), to ORPHA:1052 (Mosaic variegated aneuploidy syndrome, the umbrella term) and directly to the genes BUB1B, CEP57 and TRIP13** |
| r9 — this run | conjunctivitis, recurrent respiratory infections, headache, pruritus, **skin rash** | Every term checked against all four MVA identifiers *and* against the three MVA genes |

The r7 fix verified the replacement terms against `OMIM:257300` and nothing else. Exomiser scores
phenotype similarity over the whole ontology graph, so a term annotated to **any** MVA disease — or
to *BUB1B* through any disease — leaks the answer back into the control. MVA2 and the ORPHA umbrella
term were never queried.

It was caught by the packaged MVA-Replay tool, which emits a warning when a term supplied as an
"unrelated" control is annotated to the gene being planted. The check existed because the first
contamination taught us to write it; it fired on the second one.

## 2. The corrected number

Exomiser 15.1.0, identical analysis (`tools/analysis_mva.yml`), same VCF, only the HPO set changes.

| Run | HPO set | BUB1B rank | BUB1B score |
|---|---|---|---|
| Real phenotype | the child's 8 terms | 1 | **0.5871** |
| Control r7 (**as submitted**) | 5 terms, one annotated to MVA2/ORPHA | 1 | 0.4187 |
| **Control r9 (clean)** | **5 verified terms** | **1** | **0.3965** |

**The conclusion is unchanged and slightly strengthened: the finding is variant-driven.** BUB1B is
ranked first even with a phenotype that has nothing to do with the disease, on the cleanest control
we have been able to construct. What changes is the number: the submitted report's 0.4187 was
inflated by 0.0222 by the contaminating term.

## 3. What has to change in the submitted report

The Track 1 report currently states the unrelated-HPO control score as **0.4187**. That figure
should read **0.3965**, and the control terms should be listed as the r9 set. This is the **fourth**
correction to the submitted report, joining the three already recorded (the retired "about 24%"
phenotype contribution, the ClinVar attribution, and the 4,565 rows-versus-genes denominator).

The re-submission quota stands at 2 of 6 used.

## 4. Verification, and its limits

`hpo/01_verificar.py` queries `ontology.jax.org` for every candidate term and rejects it if it is
annotated to **OMIM:257300** (MVA1), **OMIM:614114** (MVA2), **OMIM:617598** (MVA3), **ORPHA:1052**
(the umbrella term), to any disease whose name contains "aneuploid", or to any of **BUB1B**,
**CEP57**, **TRIP13**.

Of thirteen terms tested, **four were rejected**, and three of those rejections were replacements we
had proposed: fever, dyspnoea and abdominal pain are each annotated to *TRIP13*. Screening candidate
control terms by eye does not work; this is the third round in which it failed.

**What this still does not guarantee.** The rule removes terms with a *direct* annotation. It does
not remove terms that are close to an MVA term in the ontology graph without being annotated to it,
and Exomiser's similarity measure is graph-based. A term with zero annotations to MVA can still sit
near one. The honest statement is therefore *"no term in the control set is annotated to any MVA
disease or MVA gene"*, which is what we now write, and **not** *"the control set is phenotypically
independent of MVA"*, which we cannot demonstrate with this method.

## 5. Reproduce

    hpo/01_verificar.py          checks each term against all MVA diseases and genes
    hpo/verificacion.json        the result, per term
    tools/control_hpo_r9.sh      the two Exomiser runs above
