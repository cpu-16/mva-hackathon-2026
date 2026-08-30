# Codex — verificación de ronda 8 (los reportes ya corregidos)

`codex exec`, 30-ago-2026. Tercera pasada: pre-registro → resultados → reportes corregidos.

1. The benchmark’s “retained variants” comparison mixes two different units.

Track 1’s filtering cascade says:

> “9,935 after inheritance-mode compatibility”

and Q10 identifies 12,431 as:

> “12,431 variant-by-inheritance-model rows”

But the new benchmark says:

> “these callsets are … retaining 6,510–9,486 variants against this patient’s 12,431”

The patient’s 12,431 is not a variant count comparable to the GIAB “retained” counts; it is a variant × inheritance-mode row count. This repeats the same rows-versus-entities error corrected for the 4,565 denominator. Consequently, the claimed direction and magnitude of the null bias are not established by those numbers. Replace 12,431 with the patient count produced at the corresponding GIAB pipeline stage—possibly 9,935, but only if definitions are identical—or remove the comparison.

2. The report still says the phenotype chooses an interpretation that the pipeline itself did not choose.

The robustness conclusion says:

> “it is the phenotype that makes Exomiser attach the recessive model to mosaic variegated aneuploidy rather than to somatic colorectal cancer”

The abstract repeats:

> “the phenotype selects the recessive MVA interpretation over the dominant artefact”

But the report and results say:

> “BUB1B ranked 2nd … under the autosomal recessive model”

> “The same gene also took rank 1 under the autosomal dominant model”

and:

> “the row that wins for BUB1B is the autosomal-dominant row”

The phenotype did not make Exomiser select the recessive interpretation “rather than” the dominant one; both were emitted, and the dominant interpretation won. The clinical team selected the recessive interpretation using phenotype, known inheritance, and the two-allele architecture. Suggested replacement:

> Exomiser emitted both interpretations and ranked the dominant colorectal-cancer row first. We selected the recessive MVA1 interpretation during manual review because it matches the phenotype, known inheritance, and two-allele architecture; the retrieval score itself did not prefer it.

This is the most important uncorrected contradiction.

3. “Stripping ClinVar classifications from the same architecture” overstates the counterfactual.

Track 1 says:

> “with both ClinVar classifications stripped, the same molecular architecture still scores 0.5743”

and the benchmark introduction says it held everything except ClinVar status fixed.

But X3 replaces the original nonsense at `40209701` with a different nonsense at `40212550`. This is not literally the same pair with metadata stripped. Gene, broad consequence class, partner allele, phenotype, and reported variant score are held fixed; locus and allele are not.

The experiment strongly rebuts the original whitelist-saturation explanation, but it does not isolate ClinVar as cleanly as deleting CLNSIG from the exact original record would. “Same molecular architecture” is defensible only if explicitly defined as “nonsense-plus-missense in BUB1B,” not as the same alleles.

4. The corrected causal statement remains too broad.

Current formulations include:

> “the `stop_gained` consequence alone saturates it”

> “the truncating consequence carries the ranking”

> “the loss-of-function consequence carries the ranking”

The experiment establishes that both tested nonsense alleles receive variant score 1.0000 and that replacing the whitelisted nonsense with the unclassified nonsense leaves BUB1B first in two tested backgrounds. It does not establish that truncating consequence alone generally “carries the ranking,” because the result still includes gene-level evidence, the missense partner, phenotype evidence, and background competition.

I would submit:

> In this controlled counterfactual, replacing the ClinVar-whitelisted nonsense allele with a different unclassified `stop_gained` allele left the nonsense variant score at 1.0000 and reduced the combined BUB1B score only from 0.5871 to 0.5743, without changing rank 1 in either of the two tested backgrounds. Thus the original claim that ClinVar whitelisting saturates the variant score is refuted; in these constructs, saturation is associated with the `stop_gained` consequence rather than the ClinVar classification.

5. The report presents an incomplete benchmark without disclosing that its principal null experiment remains open.

The supplied results file says:

> “Experiment A tier 2 (30 × 1000 Genomes) is still running and is marked open.”

and:

> “P-A is OPEN, not ‘holds’.”

Track 1’s benchmark section reports only the seven GIAB genomes without saying that the preregistered 30-genome tier is pending. The abstract calls this:

> “A benchmark pre-registered in git … 61 runs”

which can reasonably be read as 61 completed runs.

This matters because the maximum-null claim is explicitly falsified by a single future exceedance. State both the interim nature and the open prediction:

> In the completed GIAB tier, 0.5871 exceeded all seven top scores; the preregistered 30-genome 1000 Genomes tier remains in progress, so the maximum-null prediction is still open.

6. The reported phase penalty is arithmetically wrong.

From the supplied endpoints:

\[
(0.9339-0.9305)/0.9339 = 0.0036406 = 0.364\%.
\]

Therefore, “0.34%” should be approximately **0.36%**. The absolute penalty is **0.0034**. This error occurs in Track 1 Q9, Track 2, and the results narrative.

The direction also needs labeling: identify explicitly which endpoint is cis and which is trans rather than writing only `0.9339 → 0.9305`.

7. The other requested arithmetic checks pass, subject to the denominator defect in finding 1.

- `0.5871 − 0.5619 = 0.0252`, correctly rounded to **0.025**.
- `0.0128 / 0.5871 = 2.18%`, correctly rounded to **2.2%**.
- `40220612 − 40209701 = 10,911 bp`.
- `6,404 × 9.98×10⁻⁵ = 0.639`, correctly reported as **0.64**.
- `6,404 × 8.99×10⁻⁷ = 0.00576`, correctly reported as **0.006**.
- The supplied results support **3,139 unique genes, 257 above zero, and 32 ≥0.01**.
- `4,565 − 303 = 4,262` zero-score rows is internally possible, but 303 positive rows and 257 positive genes are different units; the wording must continue to distinguish them.

8. The denominator correction contains a smaller entities/rows wording slip.

Track 1 says:

> “of those only 257 receive a combined score above zero … while the remaining rows are tied at the bottom”

“Of those” refers to 3,139 genes, but “remaining rows” switches back to rows. The results support 257 positive-score genes and 4,262 zero-score rows, not “3,139 minus 257 remaining rows.” Write:

> The run contains 3,139 unique genes; 257 genes have at least one row above zero and 32 have at least one row ≥0.01. Separately, 4,262 of the 4,565 gene × inheritance-mode rows have score zero.

9. The abstract’s benchmark statement inherits both substantive problems above.

It says:

> “the database record is not what drives the result, the truncating consequence is”

That is stronger than the controlled experiment supports, and it omits that X2/X3 use a different nonsense allele. It also fails to label the healthy-genome maximum experiment as interim/open.

I would replace the benchmark’s final two sentences with something like:

> In the completed seven-genome GIAB tier, the highest unspiked score was 0.5619, only 0.0252 below the case; the preregistered 30-genome tier remains pending. In a post-hoc two-background counterfactual, replacing the whitelisted nonsense with an unclassified nonsense reduced the score from 0.5871 to 0.5743 without changing rank, refuting our earlier claim that ClinVar whitelisting saturates the variant score.

To make room, cut the abstract’s mosaicism sentence. It is valuable work but less central to the method’s diagnostic validity than disclosing that the benchmark is incomplete and that the ClinVar counterfactual changes the allele.

10. “Without being told” is now too broad in the convergent-result framing.

Track 1 says:

> “the correct disease, reached without being told”

That is fair as a statement about candidate generation: no disease name or panel was supplied. But the document later acknowledges that the automated winner was the dominant colorectal-cancer row and that the defensible recessive interpretation required manual adjudication. As currently placed, “the correct disease” can sound like the pipeline chose the final diagnosis.

A precise version would be:

> Exomiser generated the correct recessive MVA disease association without receiving a disease name or candidate gene, although its higher-scoring BUB1B row was the clinically inappropriate dominant colorectal-cancer interpretation.

The core newly introduced break is finding 1: while correcting the gene denominator, the benchmark comparison reused another row count as though it were a unique-variant count. The most consequential surviving old claim is finding 2: the report still credits the phenotype with making a choice that Exomiser’s ranking demonstrably did not make.

