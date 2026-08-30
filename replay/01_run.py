#!/usr/bin/env python3
"""MVA-Replay runner. Corre Exomiser sobre un VCF con un set de HPO y devuelve
las metricas pre-registradas. Sin GPU, sin datos del paciente."""
import subprocess, sys, os, csv, json
from concurrent.futures import ThreadPoolExecutor

ROOT = "/home/gar16/datos/HACKATHON-MVA-2026"
EXO  = f"{ROOT}/tools/exomiser-cli-15.1.0"
YML  = f"{ROOT}/tools/analysis_mva.yml"
OUT  = f"{ROOT}/replay/out"

HPO_REAL = ["HP:0002859","HP:0000121","HP:0004322","HP:0001508",
            "HP:0003202","HP:0001622","HP:0001518","HP:0200067"]
HPO_AJENO = ["HP:0000365","HP:0000509","HP:0002205","HP:0002315","HP:0000989"]

def sample_yml(path, sample_id, hpos):
    with open(path, "w") as f:
        f.write("---\nid: replay\nsubject:\n  id: %s\n  sex: MALE\n"
                "phenotypicFeatures:\n" % sample_id)
        for h in hpos:
            f.write('  - type: { id: "%s" }\n' % h)
        f.write('metaData:\n  created: "2026-08-30T00:00:00Z"\n'
                '  createdBy: "mva-replay"\n  phenopacketSchemaVersion: "1.0.0"\n')

def run(case, vcf, sample_id, hpos, xmx="10g"):
    os.makedirs(OUT, exist_ok=True)
    y = f"{OUT}/{case}.sample.yml"
    sample_yml(y, sample_id, hpos)
    vcf = os.path.abspath(vcf)
    cmd = ["nice","-n","12","java",f"-Xmx{xmx}","-jar","exomiser-cli-15.1.0.jar","analyse",
           "--sample",y,"--vcf",vcf,"--assembly","GRCh38","--analysis",YML,
           "--output-directory",OUT,"--output-filename",case,
           "--output-format","TSV_GENE,TSV_VARIANT"]
    with open(f"{OUT}/{case}.log","w") as lg:
        r = subprocess.run(cmd, cwd=EXO, stdout=lg, stderr=subprocess.STDOUT, timeout=3600)
    return case, r.returncode

def genes_tsv(case):
    p = f"{OUT}/{case}.genes.tsv"
    if not os.path.exists(p): return []
    with open(p) as f:
        return list(csv.DictReader(f, delimiter="\t"))

def resumen(case, gene_of_interest=None):
    """Metricas pre-registradas de una corrida."""
    rows = genes_tsv(case)
    if not rows: return {"case": case, "error": "sin salida"}
    k_rank, k_gene = "#RANK", "GENE_SYMBOL"
    k_moi, k_comb = "MOI", "EXOMISER_GENE_COMBINED_SCORE"
    top = rows[0]
    # mejor fila por gen (el gen aparece una vez por modo de herencia)
    best = {}
    for r in rows:
        g = r[k_gene]
        if g not in best or float(r[k_comb]) > float(best[g][k_comb]):
            best[g] = r
    runner = next((r for r in rows if r[k_gene] != top[k_gene]), None)
    d = {"case": case,
         "n_filas": len(rows), "n_genes": len(best),
         "top_gene": top[k_gene], "top_moi": top[k_moi],
         "top_score": round(float(top[k_comb]), 4),
         "segundo_gene": runner[k_gene] if runner else "",
         "segundo_score": round(float(runner[k_comb]), 4) if runner else ""}
    for g in filter(None, [gene_of_interest, "BUB1B"]):
        r = best.get(g)
        d[f"{g}_rank"] = int(r[k_rank]) if r else ""
        d[f"{g}_moi"]  = r[k_moi] if r else ""
        d[f"{g}_score"]= round(float(r[k_comb]), 4) if r else ""
    return d

if __name__ == "__main__":
    # uso: 01_run.py <caso> <vcf> <sample_id> <real|ajeno>
    case, vcf, sid, ph = sys.argv[1:5]
    hpos = HPO_REAL if ph == "real" else HPO_AJENO
    c, rc = run(case, vcf, sid, hpos)
    print(json.dumps(resumen(case), ensure_ascii=False))
