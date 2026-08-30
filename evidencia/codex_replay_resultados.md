# Codex — crítica adversarial de los RESULTADOS de MVA-Replay y de la fase

`codex exec`, 30-ago-2026. Brief: `brief_replay_resultados.md`. Segunda ronda: la primera fue sobre el pre-registro.

Blunt verdict: you found several real and valuable results, but the strongest causal sentences overreach. The biggest problem is not statistical—it is procedural: Amendment 3 contradicts the frozen-builder rule, so the corrected FANCD2 arm is exploratory, not a clean preregistered falsification.

1. The “24% phenotype contribution” statement is genuinely wrong—but 28.7% is not a valid causal replacement.

The original 24% compares two controls:

\[
(0.5506-0.4187)/0.5506=23.9\%
\]

That measures the score reduction after removing two MVA-associated terms from the contaminated control. It does not measure the phenotype’s total contribution.

The new calculation is arithmetically correct:

\[
(0.5871-0.4187)/0.5871=28.7\%
\]

But “the phenotype contributes 28.7% of the score” is still unsound. Exomiser’s combined score is a nonlinear integration, not an additive budget whose components can be assigned percentages. Changing the HPO set is a counterfactual perturbation of one input; it does not isolate a Shapley-like or additive phenotype component. Your FANCD2 table proves why that distinction matters: a 0.13 difference in phenotype score can correspond to a roughly threefold combined-score difference.

The replicated quantity is an HPO-set contrast, not a component attribution.

Use this sentence:

> Replacing the patient’s eight HPO terms with five verified-unrelated terms reduced the BUB1B combined score from 0.5871 to 0.4187, an absolute decrease of 0.1684, or 28.7% relative to the original score. Because Exomiser combines phenotype and variant evidence nonlinearly, this contrast measures sensitivity to the HPO query and should not be interpreted as the fraction of the score causally attributable to phenotype.

That correction is worth a submission slot if the existing report explicitly says “phenotype contributes 24%.” Correct both the wrong comparison and the invalid attribution.

2. “The combined score is a property of the two alleles and phenotype, not the genome” is over-stated and partly trivial.

What you demonstrated is narrower:

> Under this frozen Exomiser version and configuration, once these planted BUB1B alleles survive filtering and receive the same annotations, their gene-level combined score is invariant across the three tested GIAB backgrounds; the background changes rank through competing genes.

That is useful operational validation, but it is largely a consequence of a gene-local scoring function. It is not evidence that genomes generally cannot affect the score.

The invariance could break if a background:

- already contains another variant in BUB1B;
- changes the inferred inheritance configuration or contributing-variant set;
- overlaps or conflicts with a planted allele;
- differs in sex, pedigree, zygosity or phase information used by scoring;
- causes an allele to fail a frequency, quality or effect filter;
- changes annotations through multiallelic representation or normalization;
- uses another Exomiser/data version or configuration.

Calling it “fully determined” is especially unsafe after your phase pilot: phase changed the score from 0.9339 to 0.9305. That alone proves genotype context beyond “the two alleles and phenotype” can affect the number, even if slightly.

Also, “the score is portable” is wrong. The planted BUB1B score was background-invariant in this experiment. A healthy genome’s top score is absolutely background-dependent because its candidate genes and variants define that maximum. Scores may also change across Exomiser releases, data snapshots and configuration.

Use:

> For these constructs, backgrounds and frozen pipeline, the planted BUB1B gene score was background-invariant to four decimal places, whereas its rank changed with the competing variants in each genome.

3. Experiment C demonstrates an architecture gradient, not that “ClinVar classification is worth 88%.”

The numerical gradient is real:

\[
0.9332 > 0.5871 > 0.1120
\]

But the causal attribution is confounded because C-hi, C-mid and C-lo are different allele pairs. They can differ simultaneously in:

- consequence severity;
- computational pathogenicity scores;
- population frequency;
- splice predictions;
- gene-specific variant annotations;
- ClinVar classification and review evidence;
- which allele becomes the leading contributor;
- ACMG evidence beyond PP5/ClinVar.

Therefore these claims do not follow:

> “ClinVar’s classification is worth 88%.”

> “Had the child’s nonsense not been in ClinVar, the same two variants would have scored 0.1120.”

The latter is factually false as written: 0.1120 came from two different VUS records, not from the same child-architecture alleles with their ClinVar status removed.

The 88% calculation is apparently:

\[
(0.9332-0.1120)/0.9332=88.0\%
\]

That is the separation between two confounded constructs. It is not the fraction attributable to ClinVar, and it is not even the relevant comparison for the child-like C-mid construct.

What survives the objection is:

> Within the rule-selected BUB1B constructs, score and rank were strongly associated with the ClinVar-class architecture.

That is strong evidence of dependence on the selected allele package, but not identification of which annotation caused it.

The decisive single extra construct is:

> Run the exact C-mid alleles with their ClinVar-derived evidence ablated or neutralized, while preserving coordinates, consequences, frequencies and computational pathogenicity annotations.

That requires a mechanistic follow-up outside the frozen confirmatory pipeline—likely a controlled Exomiser data/configuration modification. Compare it directly with the ordinary C-mid score of 0.5871. Do not substitute other VUS variants.

A safer conclusion now:

> Rule-selected BUB1B P/LP, P/LP+VUS and VUS/VUS constructs produced a large monotonic score gradient. Because the constructs differ in annotations beyond ClinVar classification, this experiment does not isolate ClinVar’s causal contribution.

4. “Phase is not computable” is too absolute; “not resolvable with the available evidence” is defensible.

4.1. Beagle

Your observed Beagle behavior is plausible for the particular reference-panel workflow: the target-only variants were not represented in the reference-driven output. But this sentence is too broad:

> “A reference-panel phaser can only place a variant that exists in the panel.”

Population phasers can phase target-only or very rare variants in sufficiently large multi-sample target datasets, often by placing them onto a common-variant haplotype scaffold. SHAPEIT5, for example, explicitly has a rare-variant phasing stage; its demonstrations concern large sequencing cohorts, not one singleton. [SHAPEIT5 documentation](https://odelaneau.github.io/shapeit/docs/tutorials/simulated/)

Your correct claim is:

> In this singleton-reference configuration, Beagle 5.5 omitted the three target-only heterozygous sites, so that run produced no phase estimate for either causal variant.

Before asserting tool necessity, confirm from the Beagle log that they were excluded specifically for non-overlap, rather than an allele-representation, chromosome-name or map issue. Your table alone demonstrates what this run did, not the universal reason Beagle must do it.

4.2. Other short-read routes

You have not fully excluded read-backed phasing merely by inspecting GATK’s `PGT/PID`. Absence of GATK phase tags means that caller did not phase them; it is not equivalent to proving no other read-based phaser can.

The proper remaining check is to run a read-backed phaser such as WhatsHap on the original BAM/CRAM and inspect whether the two causal variants land in the same connected phase block. WhatsHap can connect chains of reads when each read or pair covers at least two heterozygous variants. [WhatsHap guide](https://github.com/whatshap/whatshap/blob/main/doc/guide.rst)

In your particular interval, the sparse heterozygosity makes success extremely unlikely: the internal marker is about 6.8 kb from one allele and 4.1 kb from the other, well beyond ordinary short-read fragments. But “unlikely from the site geometry” should become “tested and absent” before you call the route closed. Official guidance likewise says Illumina paired-end data generally produces short phase blocks and recommends examining the actual blocks. [WhatsHap FAQ](https://whatshap.readthedocs.io/en/latest/faq.html)

Allele balance cannot determine cis versus trans: 50:50 balance is expected for both. Local LD cannot reliably orient two essentially private alleles without either a carrier haplotype, read linkage, relatives or a large target cohort. Assembly from ordinary short reads cannot bridge an uninformative 10.9 kb region unless the library contains linking fragments or distinctive graph structure that you have not described.

4.3. Expected copies

The calculations are correct:

- \(6404 \times 10^{-4}=0.6404\)
- \(6404 \times 9\times10^{-7}=0.00576\)

But “therefore a bigger panel would not help” is wrong. A bigger panel increases the chance of observing the alleles. Under a simple Poisson approximation, the chance of at least one copy is \(1-e^{-n\,AF}\).

For approximately 95% probability of at least one copy:

- AF \(10^{-4}\): about 30,000 haplotypes;
- AF \(9\times10^{-7}\): about 3.3 million haplotypes.

“One expected copy” of the second allele requires about 1.1 million haplotypes, but that corresponds to only about a 63% chance of seeing at least one. And merely observing an allele once would not automatically establish its phase in this child.

Use:

> Phase could not be resolved from the available singleton short-read data: the caller supplied no read-backed phase, the tested Beagle reference-panel workflow omitted both causal variants, and the interval lacks panel-overlapping heterozygous markers capable of linking them. Definitive resolution requires parental genotyping or new molecule-level linkage data.

Do not write “not computable.” It invites a technically valid objection.

5. P-B3 is not a clean preregistered falsification, and the proposed mechanism is not established.

First, the procedural problem: after the sentinel passed, the preregistration said:

> “The builder is frozen.”

and:

> a planted allele not reaching the variants TSV is a `technical_failure`, counted and reported.

Amendment 3 then changed the pool rule, selected a different FANCD2 allele and reran the arm after observing pre-amendment ranks. That is exactly a post-unblinding change to the construct. It may be an entirely justified bug fix—but according to your own stopping rule, the original cells should remain technical failures and the corrected cells should be labeled post-amendment exploratory or sensitivity analyses.

You cannot simultaneously claim:

- the builder was frozen;
- technical failures would not be patched;
- the corrected decoy arm is preregistered confirmatory evidence.

Therefore P-B3 is not formally “falsified” by the amended runs. The honest status is:

> P-B3 was not evaluable in the originally locked construct because of a target-gene pool defect. In a post-amendment corrected construct, FANCD2 reached rank 1 in 1/3 backgrounds, contrary to the preregistered direction.

Second, the AD explanation is insufficient. BUB1B’s AD row scores 0.5871, but its AR row scores 0.5538—still approximately three times FANCD2’s 0.1841. Thus BUB1B does not need the AD row to beat FANCD2. The AD row explains which BUB1B row wins, not the BUB1B–FANCD2 separation.

Third, you have not isolated nonlinearity in the phenotype term. You are comparing different genes, disease models, allele pairs and underlying annotations. A nonlinear mapping is plausible, but two rows do not demonstrate that phenotype alone caused the amplification.

Alternative explanations include:

- different variant-level evidence and aggregation;
- different inheritance-model compatibility;
- different disease-model or OMIM integration beneath the displayed summaries;
- differences in which variants are marked contributing;
- gene/disease-specific score calibration;
- the decoy’s weaker missense annotation;
- threshold or transformation effects involving several terms jointly.

Use:

> The corrected FANCD2 construct scored substantially below BUB1B despite a high phenotype score, showing that phenotype similarity and a coarse P/LP+VUS label were insufficient to reproduce BUB1B’s score. The present experiment does not identify whether the separation arose from variant strength, inheritance-model integration, disease-model scoring or nonlinear combination.

6. Your results contradict at least six things you wrote.

6.1. Builder freeze versus Amendment 3

This is the most serious contradiction. You froze the builder and promised that post-freeze ingestion failures would be reported, not patched. Then you changed the eligibility rule, substituted an allele and reran the affected arm after seeing results.

The correction may improve scientific validity, but it sacrifices confirmatory status.

6.2. “Same allele architecture” versus unmatched evidence

You repeatedly describe FANCD2 as carrying the “same architecture.” It shares only the coarse label P/LP+VUS. Your own results admit that its missense and variant scores are weaker. Experiment C then demonstrates that allele selection within those labels can move scores enormously. Your data undermine the premise that class labels alone constitute a matched architecture.

6.3. “Phenotype contributes 28.7%” versus your nonlinearity explanation

You correctly invoke steep nonlinearity to explain FANCD2, but then treat the BUB1B score difference as an additive percentage contribution. Both cannot be used without qualification.

6.4. “BUB1B wins on the AD row” versus its AR score

BUB1B’s AR score is 0.5538 and still decisively beats FANCD2’s 0.1841. AD dominance is not necessary to explain the decoy result. More damagingly, the highest score reported for the actual recessive diagnosis comes from an AD model. That means your headline 0.5871 is not specifically evidence for compound-heterozygous MVA1 retrieval; it is partly a single-allele dominant-model result.

This should be stated prominently:

> The overall BUB1B rank was driven by an AD row, although the proposed diagnosis is recessive; the matching AR row scored slightly lower at 0.5538.

6.5. “ClinVar classification is worth 88%” versus different alleles

You claim a counterfactual about “the same two variants,” but Experiment C never ran that counterfactual. It changed variants as well as ClinVar class.

6.6. “Replicated in three genomes” versus background-invariant computation

If the gene score is locally computed and background-invariant, reproducing it in three backgrounds is not three independent replications of the 28.7% contrast. It is one software behavior executed three times. The backgrounds independently test rank robustness, not the score contrast.

6.7. “Score does not have this [background] problem”

The planted gene’s score did not vary, but Experiment A’s endpoint is each background’s maximum score. That maximum plainly depends on which variants and genes the genome contains. Score avoids the denominator problem of rank; it is not background-free.

6.8. Prediction counting

There are seven labeled predictions: P-A, P-A2, P-B1, P-B2, P-B3, P-B4 and P-C. Six are currently resolved and one pending. Write “one of the six resolved predictions was contrary to its predicted direction,” not wording that might imply only six were preregistered.

7. Pre-commit these P-A sentences now.

Do not say “one or two exceedances” softens the prediction. P-A used the maximum. A single exceedance falsifies it.

If exactly one of the 30 exceeds 0.5871:

> P-A was falsified: one of 30 prespecified 1000 Genomes healthy controls produced a top-gene score above the patient’s 0.5871 under the same eight-HPO query. The patient score therefore lies inside the observed healthy-genome range in tier 2; 29/30 tier-2 controls scored below it, but it is not separated from the null by the preregistered maximum criterion.

If exactly two exceed:

> P-A was falsified: two of 30 prespecified 1000 Genomes healthy controls produced top-gene scores above the patient’s 0.5871 under the same eight-HPO query. The patient score therefore lies inside the observed healthy-genome range in tier 2; 28/30 tier-2 controls scored below it, so the result indicates a high but non-exclusive score rather than separation from healthy genomes.

Add in either case:

> GIAB and 1000 Genomes are reported separately as preregistered because their callsets and variant burdens differ; we do not pool them into a single percentile.

Do not call 29/30 “the 96.7th percentile” or 28/30 “the 93.3rd percentile” without defining a percentile convention. “29/30 below” and “28/30 below” are exact and harder to misuse.

The report’s defensible central conclusion is narrower but still valuable: the BUB1B retrieval is robust for the planted construct, heavily dependent on the particular annotated allele package, only partly sensitive to the phenotype query, not evidence of end-to-end diagnostic sensitivity, and unable to validate the essential trans configuration.

