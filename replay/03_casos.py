#!/usr/bin/env python3
"""Experimentos B y C del pre-registro. Construye los casos con el builder congelado
y corre Exomiser. Escribe resultados_BC.tsv."""
import sys, os, csv, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module
sp = import_module('02_spike'); rn = import_module('01_run')

FONDOS = ["HG001", "HG002", "HG005"]

# Experimento B, arm 1: los dos registros ClinVar nombrados en el pre-registro
BUB1B_ARM1 = [
 {"chrom":"chr15","pos":40209701,"ref":"T","alt":"G","clinvar_id":"533901","nota":"P/LP nonsense p.Leu737Ter"},
 {"chrom":"chr15","pos":40220612,"ref":"T","alt":"A","clinvar_id":"4600147","nota":"VUS missense p.Asn1002Lys (analogo publico)"},
]

def par(gene, ka, kb, fondo):
    """Regla congelada: alelo1 = primer registro del pool de ka, alelo2 = ultimo del pool de kb."""
    pa = [r for r in sp.pool(gene, ka)]
    pb = pa if ka == kb else [r for r in sp.pool(gene, kb)]
    def valido(r):
        return (sp.ref_ok(r["chrom"], r["pos"], r["ref"]) is True
                and sp.en_alta_confianza(fondo, r["chrom"], r["pos"]) is True
                and not sp.solapa(fondo, r["chrom"], r["pos"], r["ref"]))
    a = next((r for r in pa if valido(r)), None)
    b = next((r for r in reversed(pb) if valido(r) and (a is None or r["pos"] != a["pos"])), None)
    return a, b

def caso(nombre, fondo, gene, alelos, ph):
    if any(x is None for x in alelos):
        return {"caso":nombre,"fondo":fondo,"gen":gene,"hpo":ph,"error":"pool insuficiente"}
    vcf_caso = f"{sp.CASES}/{nombre}.vcf.gz"
    if not os.path.exists(vcf_caso):
        sp.construir(nombre, fondo, alelos, "trans")
    ok = sp.verificar_insercion(nombre, alelos)
    rn.run(f"{nombre}_{ph}", vcf_caso, fondo, rn.HPO_REAL if ph=="real" else rn.HPO_AJENO)
    d = rn.resumen(f"{nombre}_{ph}", gene)
    d.update({"caso":nombre,"fondo":fondo,"gen":gene,"hpo":ph,"insercion_ok":ok,
              "alelos":";".join(f'{a["chrom"]}:{a["pos"]}{a["ref"]}>{a["alt"]}({a["clinvar_id"]})' for a in alelos)})
    # ¿llegaron los alelos plantados al TSV de variantes?
    vt = f"{rn.OUT}/{nombre}_{ph}.variants.tsv"
    llegaron = 0
    if os.path.exists(vt):
        with open(vt) as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        for a in alelos:
            if any(r["CONTIG"].replace("chr","")==a["chrom"].replace("chr","")
                   and r["START"]==str(a["pos"]) and r["REF"]==a["ref"] and r["ALT"]==a["alt"]
                   for r in rows): llegaron += 1
        contrib = [r for r in rows if r["GENE_SYMBOL"]==gene and r["CONTRIBUTING_VARIANT"]=="1"]
        d["acmg"] = contrib[0]["EXOMISER_ACMG_CLASSIFICATION"] if contrib else ""
        d["acmg_ev"] = contrib[0]["EXOMISER_ACMG_EVIDENCE"] if contrib else ""
    d["alelos_ingeridos"] = f"{llegaron}/{len(alelos)}"
    d["technical_failure"] = llegaron < len(alelos)
    return d

if __name__ == "__main__":
    res = []
    for f in FONDOS:
        # --- Experimento B ---
        res.append(("B_arm1_BUB1B", f, "BUB1B", BUB1B_ARM1, "real"))
        res.append(("B_arm1_BUB1B", f, "BUB1B", BUB1B_ARM1, "ajeno"))
        a, b = par("FANCD2", "PLP", "VUS", f)
        res.append(("B_arm2_FANCD2", f, "FANCD2", [a, b], "real"))
        res.append(("B_arm2_FANCD2", f, "FANCD2", [a, b], "ajeno"))
        # --- Experimento C (BUB1B, solo HPO real) ---
        a, b = par("BUB1B", "PLP", "PLP", f)
        res.append(("C_hi_BUB1B", f, "BUB1B", [a, b], "real"))
        a, b = par("BUB1B", "VUS", "VUS", f)
        res.append(("C_lo_BUB1B", f, "BUB1B", [a, b], "real"))
    filas = []
    for nombre, fondo, gene, alelos, ph in res:
        d = caso(f"{nombre}_{fondo}", fondo, gene, alelos, ph)
        filas.append(d); print(json.dumps(d, ensure_ascii=False), flush=True)
    cols = sorted({k for d in filas for k in d})
    with open("resultados_BC.tsv","w",newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t"); w.writeheader(); w.writerows(filas)
    print("OK ->", len(filas), "filas")
