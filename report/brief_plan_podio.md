# Plan: what to BUILD to move from ~3rd place to podium contention (MVA Hackathon 2026)

## The situation, stated bluntly
Our Track 2 submission scores ~74-78/100 with two independent judges. Its weakness is structural
and both judges named it: **everything we have is reasoning. We produced no new result.** It is an
excellent essay. Track 1 is saturated (52+ teams scored a perfect 100), so the podium is decided by
the Track 2 write-up and by what we can show that others cannot.

**Judging rubric (official): Scientific Rigor 35% · Potential Impact 25% · Innovation 25% · Scalability 15%.**
One podium across both tracks. Panel = researchers, clinicians AND patient advocates. There is also a
separate Innovation/Community Award for "exceptional creativity, community impact, or patient-centered design".

**Deadline: 24-Oct-2026. Today is 30-Aug-2026. We have ~8 weeks.**

## What we HAVE
- The proband's **VCF only**: 5,012,204 records / 4,740,790 PASS, GRCh38, GATK 4.2.4.0, ~44× mean depth,
  single sample, no parents. Already derived: per-site BAF and depth tables.
- **Exomiser 15.1.0** installed with the full 2602 hg38 + phenotype databases (55 GB) — runs genome-wide
  in ~53 s on CPU.
- bcftools, Python scientific stack, WeasyPrint/pandoc, matplotlib.
- Internet access to public APIs: Ensembl VEP REST, ClinVar, gnomAD, PubMed/Europe PMC, HPO
  (ontology.jax.org), ClinicalTrials.gov, Open Targets, ChEMBL, PharmGKB, FDA labels/DailyMed, PDB, UniProt.
- Local LLMs via Ollama; commercial LLM subscriptions (declared in the submission).
- CPU compute and ~8 weeks of wall time.

## Hard constraints — a proposal that violates one of these is useless to us
1. **No wet lab.** No cells, no patient material, no collaborators with a bench. Anything requiring an
   experiment to be RUN is out (we can still PROPOSE one; we already do).
2. **No BAM, no FASTQ.** Only the VCF. Read-level analyses are impossible.
3. **No parental samples.** Phase cannot be resolved experimentally.
4. **GPU is unreliable**: RTX 4060 Laptop with documented Xid 79 "GPU has fallen off the bus" under
   sustained load; the clock-lock workaround does NOT prevent it. Assume CPU-only, or GPU work that is
   short, checkpointed and restartable. Do not propose anything requiring days of stable GPU.
5. **Data rules**: patient genotype data may not be re-shared, may not be pasted into an LLM, and must be
   deleted by 23-Nov-2026. Derived findings and named variants may be published.
6. **No more literature review, no more prose.** We have done five rounds. Another essay adds nothing.

## What we need from you
Propose **concrete things we can BUILD OR COMPUTE in the next 8 weeks that produce a NEW result** —
something that did not exist before we ran it, that a judge can inspect, and that could be wrong.

For each proposal give exactly:
1. **Name** and one-sentence description.
2. **What is actually computed**, concretely — inputs, method, outputs. Name the data sources and tools.
3. **What is NEW about the output** — why does this not already exist in the literature?
4. **How it could be falsified / what a negative result looks like.** A proposal that cannot fail is worthless.
5. **Effort**: person-days, and whether it is CPU-only.
6. **Which rubric criterion it moves, and roughly how much.**
7. **The single biggest reason it might not work.**

Rank your proposals by (points gained) / (effort). Be ruthless: 3-6 proposals, best first. Kill your own
weak ideas rather than padding the list.

Bias toward: things that use **the patient's own data** to make a **patient-specific** claim; things that
turn our asserted "transferable framework" into an artifact someone else can actually run; things a
clinician or a patient advocate would find useful. Bias against: dashboards, literature-mining that just
summarises, anything whose output is another document.
