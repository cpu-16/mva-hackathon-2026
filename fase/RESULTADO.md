# The phase of the two BUB1B variants is not resolvable from the data we have — and here is exactly why

**Team ciberpty · MVA Hackathon 2026 · 30-ago-2026.**

Both external reviewers of our benchmark pre-registration independently said the same thing: the
largest unresolved fact in the actual case is whether the child's two BUB1B variants lie in *trans*,
and settling it matters more than any synthetic benchmark. *"If phasing says cis, Track 1 is wrong
regardless of any rank."* This is the result. It is negative, it is definitive, and it took three
queries and one 18-second run rather than the 2–5 days the backlog allocated.

**Answer: phase cannot be resolved from the evidence this challenge provides.** Both reviewers
pushed back on an earlier draft that called it "not computable"; that was too absolute and it is
withdrawn. The precise, defensible statement is below, route by route, and it is enough to change
what the report should say.

## The variants

| | Locus (GRCh38) | cDNA | Protein | ClinVar | gnomAD max AF |
|---|---|---|---|---|---|
| Allele 1 | `chr15:40209701 T>G` | c.2210T>G | p.Leu737Ter | 533901, Pathogenic/Likely pathogenic | **1.00 × 10⁻⁴** |
| Allele 2 | `chr15:40220612 T>G` | c.3006T>G | p.Asn1002Lys | absent (4600147 is `T>A`, VUS) | **9.0 × 10⁻⁷** |

Distance between them: **10,911 bp**.

## Route 1 — read-backed phasing: closed because we have no alignments

**The challenge distributed a VCF, not a BAM or CRAM.** `data/` contains
`WGS_EX2312012_HGWCNDSX7.vcf.gz` and nothing else at the read level. Read-backed phasers
(WhatsHap, HapCUT2) work from alignments, so none of them can be run at all — this route is closed by
data availability, not by inference from the caller's behaviour.

What the VCF does tell us is consistent with that route failing anyway:

The patient VCF is a GATK singleton call set with `PGT`/`PID` fields available. Queried directly:

```
40209701  T>G   GT=0/1  PGT=.  PID=.  DP=46  AD=21,25  GQ=99
40220612  T>G   GT=0/1  PGT=.  PID=.  DP=28  AD=15,13  GQ=99
```

**Neither variant carries a phase group.** GATK physically phases only variants it can place in the
same active region; at 10,911 bp apart with short-read WGS this is impossible, and the caller says so
by leaving both fields empty. The only phased genotypes anywhere in the 20 kb window are two
homozygous indels 2 bp apart (`40216568`, `40216570`, `PID=40216568_TA_T`), and homozygous sites
carry no phase information.

**One caveat we are explicit about.** An empty `PGT`/`PID` proves what GATK did, not what every
read-backed phaser would do. The one place a dedicated phaser could conceivably add something is
allele 2 against `40221421`, which is only **809 bp** away — within reach of a long-insert fragment.
That test needs the BAM, which we do not have. Even if it succeeded it would place allele 2 on a
haplotype and say nothing about allele 1, which is 10.9 kb away with no intervening informative
marker. So it could not answer the question, and we could not run it either way.

## Route 2 — statistical phasing: closed by the reference panel

Statistical phasing needs heterozygous markers that exist in the reference panel *between* the two
variants, so that a haplotype can be traced from one to the other. We counted them.

In the patient's 20 kb window there are exactly **four heterozygous sites**: the two causal variants,
`40216470 A>G`, and `40221421 G>C`. Checked against the 1000 Genomes 30× GRCh38 phased panel
(3,202 individuals, 6,404 haplotypes):

| Site | Inside the 10,911 bp interval? | In the 1000G panel? |
|---|---|---|
| `40209701 T>G` (allele 1) | boundary | **no** |
| `40216470 A>G` | **yes** | **no** |
| `40220612 T>G` (allele 2) | boundary | **no** |
| `40221421 G>C` | no — 809 bp beyond allele 2 | yes, AF 0.0075 |

**Inside the interval there is not one panel-present heterozygous marker.** Widening to ±100 kb, the
patient has 124 heterozygous sites, 118 of which are in the panel — but the nearest one before
allele 1 is `40192892` (16,809 bp upstream, AF 0.0016) and the nearest after allele 2 is `40221421`
(809 bp downstream, AF 0.0075). The 10.9 kb that has to be spanned is empty.

**Empirical confirmation.** Beagle 5.5 (27Feb25.75f), reference = the 1000G panel above, genetic map
= PLINK GRCh38, target = the patient's chr15:39.65–40.73 Mb (1,452 variants). The run completes in
18 seconds and outputs 26,194 phased markers. Of the patient's 1,452 input variants, 1,391 survive:

| Site | In Beagle's output |
|---|---|
| `40209701` (allele 1) | **dropped** |
| `40216470` | **dropped** |
| `40220612` (allele 2) | **dropped** |
| `40221421` | present, phased `0\|1` |

**The phasing tool discards both causal variants.** This is documented behaviour for the mode we ran,
not a misconfiguration: with `ref=`, Beagle emits the reference panel's markers, so target-only sites
are dropped. We state the scope precisely: *we tested reference-panel phasing of two alleles that are
not in the panel, which was guaranteed to drop them.* Running Beagle without `ref=` is not an
alternative — cohort phasing needs a cohort, and this is a singleton. Cohort phasers with a
rare-variant stage (SHAPEIT5) have the same requirement. **The Beagle run is a consistency check; the
result is the empty interval above.** There is no posterior to report and no "probably trans" to
write down.

## Why a bigger panel would not fix this — stated correctly

The absence is what the allele frequencies predict. In 6,404 panel haplotypes the expected copy count
is **0.64** for allele 1 (gnomAD max AF 1.0 × 10⁻⁴) and **0.006** for allele 2 (9.0 × 10⁻⁷).

An earlier draft concluded from this that "a bigger panel would not help". That is wrong for allele 1
and right only for the pair, and the correction matters:

- **Allele 1 is not hopeless at scale.** Under a Poisson approximation, P(≥1 copy) = 1 − e^(−n·AF);
  reaching 95% needs roughly **3 × 10⁴ haplotypes**, which existing large cohorts already exceed.
- **Allele 2 is.** The same calculation needs roughly **3.3 × 10⁶ haplotypes** for 95%, and about
  1.1 × 10⁶ for a single *expected* copy — and one expected copy is a 63% chance of seeing any.
- **Phasing the pair needs both.** Panel phasing can only orient two variants relative to each other
  if both are placeable, or if a chain of panel-present heterozygous markers links them — and §Route 2
  shows that chain is empty. A larger panel could at best seat allele 1 on a local haplotype, which
  does not answer cis versus trans.

Sending patient genotypes to a remote imputation server is not an option for this dataset in any case.

## What this changes in our submission

Our Track 1 and Track 2 reports carry the caveat *"phase not demonstrated"*, phrased as an
unfinished piece of work. It is not unfinished; it is **undoable with this dataset**, and the
sentence should say so with these numbers. Combined with the phase pilot (`replay/PILOTO_FASE.md`),
which showed that our pipeline would have returned the same rank, the same score to three decimals
and the same PATHOGENIC classification even if both variants sat on the same chromosome, the honest
statement is:

> The compound-heterozygous interpretation rests on the inheritance model and the phenotype, not on
> observed phase. Phase could not be observed with the evidence provided: the challenge distributes a
> VCF and no alignments, so no read-backed phaser can be run, and the caller itself produced no phase
> group for either variant, which sit 10,911 bp apart. Neither variant — nor the only other
> heterozygous site between them — exists in the 1000 Genomes 3,202-sample reference panel, and the
> interval contains no panel-present heterozygous marker that could link them, so reference-panel
> phasing discards all three. Exomiser does read phase into its ACMG evidence (trans → PM3,
> cis → BP2) but does not apply it to the compound-heterozygous model: in a controlled test, two
> pathogenic nonsense alleles declared in *cis* were still called AR_COMP_HET, still classified
> PATHOGENIC, and still ranked first, at an absolute combined-score difference of 0.0034. The pipeline could not
> have flagged the difference had it existed.

## What would resolve it, in order of cost

1. **Genotype the parents at the two loci.** Two targeted Sanger reactions per parent. If each parent
   carries one variant, phase is settled. Cheapest by a wide margin and the standard clinical answer.
2. **Long-read or linked-read sequencing of the child** (ONT / PacBio HiFi / 10x-style). A single
   read spanning 10.9 kb resolves it directly; PacBio HiFi reads average 15–20 kb.
3. **Allele-specific analysis of BUB1B transcript** (RNA from a cultured fibroblast or lymphoblast
   line, cDNA cloning or long-read cDNA). Also answers whether the nonsense allele escapes
   nonsense-mediated decay — relevant to the §6 experiment.

All three require new laboratory work. None can be done from the data in this challenge.

## Reproduce

```
fase/paciente_chr15_win.vcf.gz   ventana chr15:39,650,000-40,730,000 del paciente (renombrada a chr15)
fase/panel_chr15.vcf.gz          1000G 30x GRCh38 phased panel, chr15
fase/plink.chr15.GRCh38.map      mapa genético GRCh38
fase/prueba.vcf.gz               salida de Beagle
java -Xmx10g -jar beagle.jar gt=paciente_chr15_win.vcf.gz ref=panel_chr15.vcf.gz \
     map=plink.chr15.GRCh38.map chrom=chr15:39650000-40730000 out=prueba seed=1 nthreads=6
```

Nothing in this analysis leaves the machine. The panel and the map are public; the patient window is
local and covered by `data/BORRAR-AL-TERMINAR.md`.
