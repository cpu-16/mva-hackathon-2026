#!/usr/bin/env python3
"""mva_replay.py — run the MVA-Replay benchmark for ANY candidate gene in one command.

Input : a candidate gene, two alleles, a set of HPO terms, a background (healthy) VCF.
Output: the planted gene's combined score and rank under four conditions —
          planted     : alleles planted, your HPO terms            (the headline number)
          noclinvar   : same, Exomiser's ClinVar whitelist OFF      (counterfactual)
          unrelated   : same VCF, clinically unrelated HPO terms   (phenotype control)
          background  : the unspiked VCF, your HPO terms            (does the gene score without the plant?)
        plus the ingestion check (did both alleles reach Exomiser's variants table?),
        ACMG class/evidence, whitelist flags, and the absolute deltas between conditions.

Everything below is copied from the frozen scripts 01_run.py / 02_spike.py / 03_casos.py /
05_posthoc_clinvar.py (PREREGISTRO.md, builder frozen 2026-08-30) and only re-parametrised so the
paths are arguments instead of constants. The Exomiser analysis (tools/analysis_mva.yml) is NOT
touched: the only things that vary between runs are the VCF, the HPO list and one JVM property.

    ./mva_replay.py --gene BUB1B --allele chr15:40209701:T:G --allele 4600147 \\
        --hpo HP:0002859 HP:0000121 HP:0004322 --background bg/HG002.vcf.gz [--dry-run]
    ./mva_replay.py --self-check
"""
import argparse, csv, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXO  = f"{ROOT}/tools/exomiser-cli-15.1.0"
YML  = f"{ROOT}/tools/analysis_mva.yml"
CLIN = f"{ROOT}/pipeline/resources/clinvar.vcf.gz"
G2P  = f"{ROOT}/pipeline/resources/genes_to_phenotype.txt"
FASTA = f"{HERE}/raw/fasta"                  # chrN.fa.bgz, only the chromosomes we downloaded
# The five terms round 7 verified as not annotated to OMIM:257300 (PREREGISTRO.md, Experiment B).
HPO_UNRELATED = ["HP:0000365", "HP:0000509", "HP:0002205", "HP:0002315", "HP:0000989"]
GTS = {"trans": ["0|1", "1|0"], "cis": ["0|1", "0|1"], "unph": ["0/1", "0/1"]}

def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

# ---------- alleles ----------------------------------------------------------------------
def parse_allele(s):
    """chr15:40209701:T:G | chr15-40209701-T-G | NC_000015.10:g.40209701T>G | ClinVar id 533901."""
    m = re.fullmatch(r"(chr)?(\w+)[:\-](\d+)[:\-]([ACGTacgt]+)[:\-]([ACGTacgt]+)", s)
    if m:
        return {"chrom": "chr" + m[2], "pos": int(m[3]), "ref": m[4].upper(), "alt": m[5].upper(),
                "clinvar_id": ".", "input": s}
    m = re.fullmatch(r"NC_0000(\d\d)\.\d+:g\.(\d+)([ACGT]+)>([ACGT]+)", s)
    if m:  # ponytail: only genomic SNV/MNV HGVS; c./p. HGVS -> resolve to a ClinVar id first
        c = {"23": "X", "24": "Y"}.get(m[1], str(int(m[1])))
        return {"chrom": "chr" + c, "pos": int(m[2]), "ref": m[3], "alt": m[4], "clinvar_id": ".", "input": s}
    if re.fullmatch(r"(clinvar:)?\d+", s):
        vid = s.split(":")[-1]
        line = sh(["bcftools", "query", "-i", f'ID="{vid}"', "-f", "%CHROM\t%POS\t%REF\t%ALT\n", CLIN]).strip()
        if not line:
            sys.exit(f"ClinVar id {vid} not found in {CLIN}")
        c, p, r, a = line.split("\n")[0].split("\t")
        return {"chrom": "chr" + c, "pos": int(p), "ref": r, "alt": a, "clinvar_id": vid, "input": s}
    sys.exit(f"cannot parse allele {s!r}")

def clinvar_status(a):
    """What ClinVar says about this exact allele (or 'absent')."""
    reg = f"{a['chrom'][3:]}:{a['pos']}-{a['pos']}"
    for l in sh(["bcftools", "query", "-r", reg, "-f",
                 "%REF\t%ALT\t%ID\t%INFO/CLNSIG\t%INFO/CLNREVSTAT\t%INFO/GENEINFO\n", CLIN]).splitlines():
        r, al, vid, sig, rev, gi = l.split("\t")
        if r == a["ref"] and al == a["alt"]:
            return {"clinvar_id": vid, "clnsig": sig, "clnrevstat": rev, "geneinfo": gi}
    return {"clinvar_id": "absent", "clnsig": "absent", "clnrevstat": "", "geneinfo": ""}

def ref_ok(chrom, pos, ref, fasta=FASTA):
    """02_spike.ref_ok: planted REF must match the reference. None = no FASTA available."""
    fa = f"{fasta}/{chrom}.fa.bgz" if os.path.isdir(fasta) else fasta
    if not os.path.exists(fa): return None
    r = sh(["samtools", "faidx", fa, f"{chrom}:{pos}-{pos+len(ref)-1}"])
    return "".join(r.split("\n")[1:]).upper() == ref.upper()

def overlaps(bg, chrom, pos, ref):
    """02_spike.solapa: any background record overlapping the planted locus (not just same POS)."""
    for line in sh(["bcftools", "view", "-H", "-r", f"{chrom}:{max(1,pos-60)}-{pos+len(ref)+60}", bg]).splitlines():
        f = line.split("\t"); p, rf = int(f[1]), f[3]
        if p <= pos + len(ref) - 1 and pos <= p + len(rf) - 1: return True
    return False

def hpo_annotated_to_gene(gene, hpos):
    """Which of these HPO terms HPOA annotates to the gene, via any disease (OMIM or Orphanet)."""
    hits = {}
    with open(G2P) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["gene_symbol"] == gene and row["hpo_id"] in hpos:
                hits.setdefault(row["hpo_id"], set()).add(row["disease_id"])
    return {h: sorted(d) for h, d in hits.items()}

# ---------- build the spiked VCF (02_spike.construir, builder frozen 30-ago-2026) ----------
def spike_records(alleles, phase, chr_prefix):
    out = []
    for i, a in enumerate(sorted(alleles, key=lambda x: (x["chrom"], x["pos"]))):
        chrom = a["chrom"] if chr_prefix else a["chrom"][3:]
        out.append(f"{chrom}\t{a['pos']}\t.\t{a['ref']}\t{a['alt']}\t100\tPASS\t.\tGT:DP:AD:GQ\t{GTS[phase][i%2]}:44:22,22:99")
    return out

def build_case(case_vcf, bg, alleles, phase="trans"):
    hdr = sh(["bcftools", "view", "-h", bg])
    # Amendment 2: the spike FORMAT is GT:DP:AD:GQ; declare whatever the background lacks.
    for tag, num, typ in (("GT", "1", "String"), ("DP", "1", "Integer"), ("AD", "R", "Integer"), ("GQ", "1", "Integer")):
        if f"##FORMAT=<ID={tag}," not in hdr:
            hdr = hdr.replace("#CHROM", f'##FORMAT=<ID={tag},Number={num},Type={typ},Description="added by mva_replay">\n#CHROM', 1)
    chr_prefix = "##contig=<ID=chr" in hdr
    spk = case_vcf.replace(".vcf.gz", ".spike.vcf")
    with open(spk, "w") as f:
        f.write(hdr + "\n".join(spike_records(alleles, phase, chr_prefix)) + "\n")
    subprocess.run(["bgzip", "-f", spk], check=True)
    subprocess.run(["tabix", "-f", "-p", "vcf", spk + ".gz"], check=True)
    if hdr != sh(["bcftools", "view", "-h", bg]):   # header was amended -> background must carry it too
        bg_re = case_vcf.replace(".vcf.gz", ".bg_reheader.vcf.gz")
        with open(spk + ".hdr", "w") as f: f.write(hdr)
        subprocess.run(["bcftools", "reheader", "-h", spk + ".hdr", "-o", bg_re, bg], check=True)
        subprocess.run(["tabix", "-f", "-p", "vcf", bg_re], check=True)
        bg = bg_re
    subprocess.run(["bcftools", "concat", "-a", "-Oz", "-o", case_vcf, bg, spk + ".gz"], check=True, capture_output=True)
    subprocess.run(["tabix", "-f", "-p", "vcf", case_vcf], check=True)
    return case_vcf

def verify_insertion(case_vcf, alleles):
    """Pre-registration assertion 1 at the VCF level: every planted allele is in the built file."""
    ok = []
    for a in alleles:
        rows = sh(["bcftools", "view", "-H", "-r", f"{a['chrom']}:{a['pos']}-{a['pos']}", case_vcf]).splitlines()
        rows += sh(["bcftools", "view", "-H", "-r", f"{a['chrom'][3:]}:{a['pos']}-{a['pos']}", case_vcf]).splitlines()
        ok.append(any(l.split("\t")[3] == a["ref"] and l.split("\t")[4] == a["alt"] for l in rows))
    return all(ok)

# ---------- run Exomiser (01_run.run / 01_run.sample_yml) ------------------------------------
def sample_yml(path, sample_id, hpos, sex):
    with open(path, "w") as f:
        f.write(f"---\nid: replay\nsubject:\n  id: {sample_id}\n  sex: {sex}\nphenotypicFeatures:\n")
        for h in hpos: f.write(f'  - type: {{ id: "{h}" }}\n')
        f.write('metaData:\n  created: "2026-08-30T00:00:00Z"\n  createdBy: "mva-replay"\n  phenopacketSchemaVersion: "1.0.0"\n')

def exomiser_cmd(case, vcf, sample_id, hpos, out, sex, xmx, clinvar=True):
    y = f"{out}/{case}.sample.yml"
    sample_yml(y, sample_id, hpos, sex)
    # ponytail: "no ClinVar" = whitelist off (one JVM property); ClinVar still feeds ACMG PP5/BP6.
    # To strip it fully, plant an unclassified allele of the same consequence (05_posthoc_clinvar.py X2/X3).
    prop = [] if clinvar else ["-Dexomiser.hg38.use-clinvar-whitelist=false"]
    return ["nice", "-n", "12", "java", f"-Xmx{xmx}", *prop, "-jar", "exomiser-cli-15.1.0.jar", "analyse",
            "--sample", y, "--vcf", os.path.abspath(vcf), "--assembly", "GRCh38", "--analysis", YML,
            "--output-directory", out, "--output-filename", case, "--output-format", "TSV_GENE,TSV_VARIANT"]

def run_exomiser(cmd, case, out):
    with open(f"{out}/{case}.log", "w") as lg:
        r = subprocess.run(cmd, cwd=EXO, stdout=lg, stderr=subprocess.STDOUT, timeout=7200)
    if r.returncode or not os.path.exists(f"{out}/{case}.genes.tsv"):
        sys.exit(f"Exomiser failed for {case} (rc={r.returncode}); see {out}/{case}.log")

# ---------- read the results (01_run.resumen + the 03/05 variants-TSV checks) ----------------
def summarize(case, gene, out, alleles=()):
    with open(f"{out}/{case}.genes.tsv") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    best = {}   # best MOI row per gene — RESULTADOS.md §0.2(c): rank genes, not gene×MOI rows
    for r in rows:
        if r["GENE_SYMBOL"] not in best or float(r["EXOMISER_GENE_COMBINED_SCORE"]) > float(best[r["GENE_SYMBOL"]]["EXOMISER_GENE_COMBINED_SCORE"]):
            best[r["GENE_SYMBOL"]] = r
    score = {g: float(r["EXOMISER_GENE_COMBINED_SCORE"]) for g, r in best.items()}
    top = rows[0]
    d = {"case": case, "top_gene": top["GENE_SYMBOL"], "top_score": round(float(top["EXOMISER_GENE_COMBINED_SCORE"]), 4),
         "n_genes": len(best), "n_genes_score_gt0": sum(s > 0 for s in score.values()),
         "score": "", "gene_rank": "", "row_rank": "", "moi": "", "pheno_score": ""}
    if gene in best:
        r = best[gene]
        d.update({"score": round(score[gene], 4), "gene_rank": 1 + sum(s > score[gene] for s in score.values()),
                  "row_rank": int(r["#RANK"]), "moi": r["MOI"], "pheno_score": round(float(r["EXOMISER_GENE_PHENO_SCORE"]), 4)})
        d["runner_up"] = max(((g, s) for g, s in score.items() if g != gene), key=lambda x: x[1], default=("", 0))[0]
    vt = f"{out}/{case}.variants.tsv"
    if alleles and os.path.exists(vt):
        with open(vt) as f: vrows = list(csv.DictReader(f, delimiter="\t"))
        ingested = sum(any(r["CONTIG"].replace("chr", "") == a["chrom"][3:] and r["START"] == str(a["pos"])
                           and r["REF"] == a["ref"] and r["ALT"] == a["alt"] and r["GENE_SYMBOL"] == gene for r in vrows)
                       for a in alleles)
        contrib = [r for r in vrows if r["GENE_SYMBOL"] == gene and r["CONTRIBUTING_VARIANT"] == "1"]
        d.update({"alleles_ingested": f"{ingested}/{len(alleles)}", "technical_failure": ingested < len(alleles),
                  "acmg": contrib[0]["EXOMISER_ACMG_CLASSIFICATION"] if contrib else "",
                  "acmg_evidence": contrib[0]["EXOMISER_ACMG_EVIDENCE"] if contrib else "",
                  "whitelist_flags": ";".join(r["WHITELIST_VARIANT"] for r in contrib),
                  "functional_class": ";".join(r["FUNCTIONAL_CLASS"] for r in contrib),
                  "variant_scores": ";".join(r["EXOMISER_VARIANT_SCORE"] for r in contrib)})
    return d

# ---------- CLI ------------------------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--gene", help="candidate gene symbol as Exomiser/HGNC spells it, e.g. BUB1B")
    p.add_argument("--allele", action="append", default=[], help="chr:pos:ref:alt, genomic HGVS (NC_...:g.) or a ClinVar variation id; give it twice")
    p.add_argument("--hpo", nargs="+", default=[], help="the patient's HPO terms")
    p.add_argument("--hpo-unrelated", nargs="+", default=HPO_UNRELATED, help="phenotype control terms (default: the five from the pre-registration)")
    p.add_argument("--background", help="healthy single-sample GRCh38 VCF (bgzip + tabix), e.g. replay/bg/HG002.vcf.gz")
    p.add_argument("--out", default=f"{HERE}/out_tool", help="output directory")
    p.add_argument("--name", help="case name (default GENE_BACKGROUND)")
    p.add_argument("--phase", choices=GTS, default="trans", help="genotype encoding of the two planted alleles")
    p.add_argument("--sex", choices=["MALE", "FEMALE"], default="MALE")
    p.add_argument("--fasta", default=FASTA, help="hg38 FASTA (indexed file, or a dir of chrN.fa.bgz) for the REF check")
    p.add_argument("--xmx", default="10g")
    p.add_argument("--dry-run", action="store_true", help="resolve alleles, run the checks, print the plan; do not run Exomiser")
    p.add_argument("--self-check", action="store_true")
    a = p.parse_args(argv)
    if a.self_check: return self_check()
    if not (a.gene and len(a.allele) == 2 and a.hpo and a.background):
        p.error("--gene, two --allele, --hpo and --background are required")
    # ponytail: one gene, exactly two alleles per run; a panel is a shell loop over this script

    os.makedirs(a.out, exist_ok=True)
    name = a.name or f"{a.gene}_{os.path.basename(a.background).split('.')[0]}"
    samples = sh(["bcftools", "query", "-l", a.background]).split()
    if len(samples) != 1:
        sys.exit(f"background must have exactly one sample (has {len(samples)}); bcftools view -s SAMPLE first")
    alleles = [parse_allele(s) for s in a.allele]
    report = {"name": name, "gene": a.gene, "background": a.background, "sample": samples[0], "hpo": a.hpo,
              "hpo_unrelated": a.hpo_unrelated, "phase": a.phase, "alleles": [], "warnings": []}
    for al in alleles:
        al.update(clinvar_status(al))
        al["ref_matches_fasta"] = ref_ok(al["chrom"], al["pos"], al["ref"], a.fasta)
        al["background_overlap"] = overlaps(a.background, al["chrom"], al["pos"], al["ref"])
        # ponytail: the GIAB high-confidence BED criterion of the pool rule is not applied here — the user
        # chooses the alleles, so the post-run ingestion check is the gate
        report["alleles"].append(al)
        if al["ref_matches_fasta"] is False: sys.exit(f"REF of {al['input']} does not match hg38 at {al['chrom']}:{al['pos']}")
        if al["ref_matches_fasta"] is None: report["warnings"].append(f"no FASTA for {al['chrom']}: REF of {al['input']} not verified")
        if al["background_overlap"]: report["warnings"].append(f"background already has a record overlapping {al['input']}")
    for h, dis in hpo_annotated_to_gene(a.gene, a.hpo_unrelated).items():
        report["warnings"].append(f"'unrelated' term {h} IS annotated to {a.gene} via {','.join(dis)} — pick another control term")
    for h, dis in hpo_annotated_to_gene(a.gene, a.hpo).items():
        report.setdefault("hpo_annotated_to_gene", []).append(f"{h} ({','.join(dis)})")

    case_vcf = f"{a.out}/{name}.vcf.gz"
    runs = [("planted",    case_vcf,     a.hpo,           True),
            ("noclinvar",  case_vcf,     a.hpo,           False),
            ("unrelated",  case_vcf,     a.hpo_unrelated, True),
            ("background", a.background, a.hpo,           True)]
    if a.dry_run:
        report["plan"] = {"spiked_vcf": case_vcf, "spike_records": spike_records(alleles, a.phase, True),
                          "runs": {k: " ".join(exomiser_cmd(f"{name}_{k}", v, samples[0], h, a.out, a.sex, a.xmx, c))
                                   for k, v, h, c in runs}}
        print(json.dumps(report, indent=1)); return
    if not os.path.exists(case_vcf):
        build_case(case_vcf, a.background, alleles, a.phase)
    report["insertion_ok"] = verify_insertion(case_vcf, alleles)
    for k, v, h, c in runs:   # ponytail: sequential, ~55 s each on GIAB; parallelise with a shell loop if needed
        case = f"{name}_{k}"
        if not os.path.exists(f"{a.out}/{case}.genes.tsv"):
            print(f"[{k}] running Exomiser ...", file=sys.stderr, flush=True)
            run_exomiser(exomiser_cmd(case, v, samples[0], h, a.out, a.sex, a.xmx, c), case, a.out)
        report[k] = summarize(case, a.gene, a.out, alleles if v == case_vcf else ())
    s = lambda k: report[k]["score"] if report[k]["score"] != "" else 0.0
    # Absolute differences only — the combined score is non-linear, so shares are undefined (RESULTADOS.md §4b iii)
    report["delta_clinvar_abs"] = round(s("planted") - s("noclinvar"), 4)
    report["delta_phenotype_abs"] = round(s("planted") - s("unrelated"), 4)
    with open(f"{a.out}/{name}.json", "w") as f: json.dump(report, f, indent=1)
    print(f"\n{a.gene} planted in {samples[0]}  ({a.out}/{name}.json)")
    print(f"{'condition':11s} {'score':>7s} {'gene_rank':>9s} {'/genes':>6s}  {'moi':22s} {'top gene':18s} acmg / ingested")
    for k, *_ in runs:
        r = report[k]
        print(f"{k:11s} {str(r['score']):>7s} {str(r['gene_rank']):>9s} {r['n_genes']:>6d}  {r['moi']:22s} "
              f"{r['top_gene']+' '+str(r['top_score']):18s} {r.get('acmg','')} {r.get('alleles_ingested','')}")
    print(f"delta ClinVar (planted - noclinvar) = {report['delta_clinvar_abs']}   "
          f"delta phenotype (planted - unrelated) = {report['delta_phenotype_abs']}")
    for w in report["warnings"]: print("WARNING:", w)

def self_check():
    """One executable check against the artefacts the 61-run benchmark already produced."""
    a1 = parse_allele("chr15:40209701:T:G"); a2 = parse_allele("NC_000015.10:g.40209701T>G"); a3 = parse_allele("533901")
    assert a1["chrom"] == "chr15" and a1["pos"] == 40209701 and a1["ref"] == "T" and a1["alt"] == "G"
    assert {k: a2[k] for k in ("chrom", "pos", "ref", "alt")} == {k: a1[k] for k in ("chrom", "pos", "ref", "alt")}, a2
    assert {k: a3[k] for k in ("chrom", "pos", "ref", "alt")} == {k: a1[k] for k in ("chrom", "pos", "ref", "alt")} and a3["clinvar_id"] == "533901", a3
    assert parse_allele("15-40209701-t-g")["chrom"] == "chr15"
    assert clinvar_status(a1)["clnsig"] == "Pathogenic/Likely_pathogenic"
    assert clinvar_status(parse_allele("chr15:40220612:T:G"))["clnsig"] == "absent"      # the child's real allele
    assert ref_ok("chr15", 40209701, "T") is True and ref_ok("chr15", 40209701, "A") is False
    recs = spike_records([parse_allele("chr15:40220612:T:A"), a1], "trans", True)
    assert recs[0].startswith("chr15\t40209701\t.\tT\tG\t100\tPASS\t.\tGT:DP:AD:GQ\t0|1:") and "\t1|0:" in recs[1]
    assert spike_records([a1], "trans", False)[0].startswith("15\t")
    hits = hpo_annotated_to_gene("BUB1B", HPO_UNRELATED)
    assert "HP:0000365" in hits and "ORPHA:1052" in hits["HP:0000365"], hits   # positive control: the check must fire
    assert hpo_annotated_to_gene("BUB1B", ["HP:0000001"]) == {}                 # negative control
    out, case = f"{HERE}/out", "B_arm1_BUB1B_HG002_real"
    arm1 = [a1, parse_allele("chr15:40220612:T:A")]
    if os.path.exists(f"{out}/{case}.genes.tsv"):
        d = summarize(case, "BUB1B", out, arm1)
        assert d["score"] == 0.5871 and d["gene_rank"] == 1 and d["moi"] == "AD", d      # RESULTADOS.md §2
        assert d["alleles_ingested"] == "2/2" and d["acmg"] == "PATHOGENIC", d
        assert summarize("A_HG002_real", "BUB1B", out)["score"] == "", "BUB1B must be absent in unspiked HG002 (P-A2)"
        assert summarize("X3_ambos_sin_clinvar_HG002_real", "BUB1B", out)["score"] == 0.5743  # RESULTADOS.md §3.2
        assert overlaps(f"{HERE}/bg/HG002.vcf.gz", "chr15", 40209701, "T") is False
        assert overlaps(f"{HERE}/cases/{case[:-5]}.vcf.gz", "chr15", 40209701, "T") is True
        assert verify_insertion(f"{HERE}/cases/{case[:-5]}.vcf.gz", arm1) is True
        assert verify_insertion(f"{HERE}/cases/{case[:-5]}.vcf.gz", [parse_allele("chr15:40209701:T:C")]) is False
        print("self-check: 20 assertions passed (incl. 8 against replay/out and replay/cases artefacts)")
    else:
        print("self-check: 12 pure assertions passed; replay/out artefacts not present, result checks skipped")

if __name__ == "__main__":
    main()
