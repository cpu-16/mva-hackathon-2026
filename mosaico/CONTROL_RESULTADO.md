# The external control ran, and it does not rescue the mosaicism result

**Team: ciberpty** · 2026-09-01, 19:50 · Design in `PREREGISTRO.md` amendment 3, window fixed in
amendment 4 (`6405d9e`), analysis code committed in `138a40f` **before the chr17 data existed**.

**Verdict, by the pre-registered rule: NOT CONCLUSIVE.** The mosaicism result stays withdrawn.

---

## 1. What ran

10 unrelated 1000 Genomes individuals, 2 per superpopulation, the first ten of the pre-registered
list, on the two fixed windows **chr8:5–25 Mb** and **chr17:5–25 Mb**.

Coverage was verified explicitly before any statistic was computed, because four remote extractions
in this project have truncated silently while returning exit code 0:

| | sites | span | largest gap | verdict |
|---|---:|---|---:|---|
| chr8 | 995,160 | 5,000,009–24,999,993 | 50,420 bp | **passes** |
| chr17 | 668,916 | 5,000,049–24,999,493 | 50,053 bp | **passes** |

## 2. The result

σ²_extra on the raw proband (it is depth-comparable by construction), κ_window on the proband
binomially thinned to each control's depth:

| | proband | control envelope (n = 10) | inside? |
|---|---:|---|---|
| **chr8** σ²_extra | **+0.000879** | +0.001471 … +0.004293 | **no — below** |
| **chr8** κ_window | **2.74** | 9.52 … 46.04 | **no — below** |
| **chr17** σ²_extra | **+0.001528** | +0.002115 … +0.003015 | **no — below** |
| **chr17** κ_window | **4.60** | 6.05 … 14.97 | **no — below** |

**The proband is below the envelope on both statistics and both chromosomes.** Amendment 3 foresaw
two outcomes — inside the envelope (technical) or outside it *upward* (a chromosome-specific claim
worth read-level work). **Below the envelope was not among them**, so the pre-registered verdict is
*not conclusive*, and we report it as such rather than inventing a rule after the fact that would
read this as good news.

## 3. Why it is not conclusive, and it is our own declared mismatch

Before the run we wrote that GQ ≥ 30 is part of the proband's site rule but could not be applied to
the controls, because the pilot extraction requested `GT,DP,AD` without `GQ`. We stated the direction
of that bias in advance: *without a GQ filter the controls keep lower-quality sites, which inflates
their dispersion and widens the envelope.*

**That is exactly the direction of the observed result**, and the controls are not matched on caller
either — a singleton GATK 4.2.4.0 call for the proband against the NYGC joint call of 3,202 samples,
which introduces correlated structure across sites by construction. A κ_window of **46** in a healthy
individual is not plausible as biology; it is a property of how those calls were made.

So the comparison cannot decide whether the proband's excess is technical or biological. **The
control did not fail to run; it failed to be a control.**

## 4. What can be said, narrowly

One thing survives, and it is worth stating because it removes a specific objection:

> The proband's window-scale overdispersion, κ ≈ 2.3, was the hole a reviewer would use to kill the
> mosaicism limit — *"your negative may be your own noise model"*. Against ten healthy genomes
> processed by a different pipeline, κ runs from **6 to 46**. **An elevated κ is not by itself
> anomalous**, and the proband's is the lowest number in the comparison.

That is **not** evidence that the proband's excess is technical, because the mismatch above already
predicts this direction. It only means the excess is not remarkable in size.

## 5. What would settle it

A control processed **identically**: a public genome called as a singleton with GATK 4.2.4.0, the
same filters including GQ, from reads. That is a real cost — alignment and calling of at least one
30× genome — and it is now the only version of this experiment worth running. Extending the window,
adding more 1000 Genomes samples, or re-looking at these data does none of it, and amendment 4 says
we do not do that.

## 6. An implementation error we found by reading our own output

Recorded as **amendment 5**, applied, and both passes reported.

The first pass compared the **thinned** proband on both statistics. Thinning does not remove the
original sampling noise, it carries it:

    var(b_thin) = var_true + E[p(1−p)]/DP_original + E[p(1−p)]/DP_thinned

so subtracting only `0.25/DP_thinned` leaves `var_true + 0.25/DP_original` behind. The arithmetic is
visible in the first pass: σ²_extra went from **+0.001118** raw to **+0.006525** thinned on chr8, a
difference of **+0.005407** against `0.25/44.8 = 0.005580`; on chr17, **+0.005311** against
`0.25/45.7 = 0.005470`. The gap *is* the un-subtracted original noise, on both chromosomes.

Amendment 3 had already said the right thing — *"σ²_extra is reported because it is additive and
depth-comparable"* — and the code did not follow it. Thinning belongs to κ_window alone.

**It mattered.** Under the erroneous version the two statistics pointed in **opposite** directions:
the proband looked *above* the envelope on σ²_extra and *below* it on κ_window. Corrected, they
agree. A second, minor error was fixed at the same time: the binomial correction used
`0.25/mean(DP)` where the expectation is `mean(0.25/DP_i)`, worth **+0.000239** on the raw proband
and changing nothing.

## 7. Reproduce

    mosaico/PREREGISTRO.md      amendments 3, 4 and 5
    mosaico/_piloto.sh          the extraction, with the fixed windows
    mosaico/08_control.py       the analysis, committed as 138a40f before chr17 existed
    mosaico/control_resultado.json   every number, including the erroneous first pass
