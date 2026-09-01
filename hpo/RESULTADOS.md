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

**In the proband's genome the conclusion holds: the finding is variant-driven.** BUB1B is still
ranked first with a phenotype that has nothing to do with the disease, on the cleanest control we
have been able to construct. What changes is the number: the submitted report's 0.4187 was inflated
by 0.0222 by the contaminating term.

⚠️ **The same clean set, run on unrelated healthy backgrounds, slightly weakens a second claim — see
§6.** BUB1B's score is unchanged across genomes; its *rank* is displaced in two of three GIAB
backgrounds under the clean control, against one of three under the contaminated one. Read §2 and §6
together; §2 alone overstates what the control shows.

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

---

## 6. Re-running the benchmark with the clean set gives a *less* favourable result, and we report it

The clean term set was also run through the packaged tool on the three GIAB backgrounds used in
`replay/RESULTADOS.md`, spiking the child's two alleles into each. The score behaves exactly as
before; **the rank does not.**

| Background | Planted score, real HPO | Unrelated-HPO score | Unrelated-HPO **rank** | Top gene under unrelated HPO |
|---|---|---|---|---|
| HG001 | 0.5871 | 0.3965 | **1** (r7: 1) | BUB1B 0.3965 |
| HG002 | 0.5871 | 0.3965 | **2** (r7: **1**) | KRT17 0.5766 |
| HG005 | 0.5871 | 0.3965 | **3** (r7: 3) | TNF 0.7436 |

**The invariance result stands and is if anything cleaner.** BUB1B's score is **0.3965 to four
decimal places in all three genomes**, as 0.5871 is under the real phenotype. The score does not
depend on the background; only the rank does, which is what `replay/RESULTADOS.md` already concluded
and the reason it named the score, not the rank, as the portable endpoint.

**One claim has to be softened — and our first draft of this section overstated by how much.**

⚠️ We wrote that with the contaminated r7 set BUB1B "came first in every background". **That is false
and it contradicts our own benchmark**, which reported r7 ranks of **1 / 1 / 3** — HG005 already
displaced it, because a background gene there reaches 0.8108 (`replay/RESULTADOS.md` §P-B2, and the
submitted Track 1 report says "2/3" in as many words). Caught by an adversarial reviewer. Inflating
the old baseline made the new wound look bigger than it is, which is the same class of error this
project has made in every round, this time in the direction of dramatising our own honesty.

**The actual change is one background.** r7 gave 1 / 1 / 3; r9 gives 1 / 2 / 3. The clean control
moves HG002 from first to second. HG005 was never first. The defensible sentence is therefore
narrower than the report's, but only by that one step:

> Under a phenotype unrelated to the disease, BUB1B's combined score is unchanged by the genomic
> background and it remains top-ranked **in the proband's genome** — but in two of three unrelated
> healthy backgrounds another gene outranks it, against one of three under the contaminated set. The
> retrieval is variant-driven in the sense that the score is carried by the variant; it is **not**
> background-independent in rank, and it was already not, before this correction.

**Why the rank moved, checked rather than assumed.** Neither KRT17 nor TNF is annotated to any of the
five control terms — we checked `genes_to_phenotype.txt` directly and found no direct annotation. The
displacement is consistent with Exomiser's graph-based semantic similarity: KRT17 disease terms are
cutaneous (palmoplantar blistering, cutaneous cyst) and the replacement control term HP:0000988 is
"skin rash". This is the limitation stated in §4 showing up in practice — removing directly annotated
terms does not remove terms that sit *near* a gene's phenotypes in the ontology. It is a property of
control-term selection in general, not a defect of this control set.

**Deltas.** With the clean set the phenotype delta is **0.1906** (0.5871 → 0.3965), not the 0.1684
computed with the contaminated set. As already established, **that delta is not convertible to a
percentage**: Exomiser's combiner is not additive and 0.3965 is not a phenotype-free baseline. The
retired "about 24%" stays retired, and 0.1906 is reported as an absolute score difference only.

Runs: `replay/_r9_hpolimpio.sh` → `replay/out_r9/`.
