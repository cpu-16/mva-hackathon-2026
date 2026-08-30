#!/usr/bin/env python3
"""POST-HOC, pedido por los dos revisores. NO es confirmatorio ni pre-registrado.
Aisla la etiqueta de ClinVar manteniendo consecuencia, gen, alelo compañero y fenotipo fijos.

C-mid (pre-registrado) = 40209701 T>G  [ClinVar 533901, P/LP, nonsense, whitelisted]
                       + 40220612 T>A  [ClinVar 4600147, VUS, missense]  -> 0.5871

X1 = mismo nonsense P/LP + 40220612 T>G  (el alelo REAL del niño, ausente de ClinVar)
     -> ¿aporta algo el registro VUS del missense?
X2 = 40212550 G>T [ClinVar 4401823, nonsense SIN clasificacion] + 40220612 T>A (VUS)
     -> ¿cuanto pone la etiqueta P/LP, con la consecuencia fija?
X3 = 40212550 G>T (nonsense sin clasificar) + 40220612 T>G (missense ausente de ClinVar)
     -> la arquitectura molecular EXACTA del niño sin ninguna etiqueta de ClinVar
"""
import sys, os, json, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module
sp = import_module('02_spike'); rn = import_module('01_run')

NS_PLP  = {"chrom":"chr15","pos":40209701,"ref":"T","alt":"G","clinvar_id":"533901","nota":"nonsense P/LP whitelisted"}
NS_NOCL = {"chrom":"chr15","pos":40212550,"ref":"G","alt":"T","clinvar_id":"4401823","nota":"nonsense SIN clasificacion ClinVar"}
MS_VUS  = {"chrom":"chr15","pos":40220612,"ref":"T","alt":"A","clinvar_id":"4600147","nota":"missense VUS"}
MS_REAL = {"chrom":"chr15","pos":40220612,"ref":"T","alt":"G","clinvar_id":"ausente","nota":"missense del niño, ausente de ClinVar"}

CASOS = {"X1_plp_msREAL":[NS_PLP,MS_REAL], "X2_nsSINclin_msVUS":[NS_NOCL,MS_VUS],
         "X3_ambos_sin_clinvar":[NS_NOCL,MS_REAL]}
FONDOS = ["HG002","HG005"]   # HG001 excluido: fondo inerte (gen top 0.0578), rank ahi no informa

if __name__ == "__main__":
    for a in (NS_NOCL, MS_REAL):
        ok = sp.ref_ok(a["chrom"], a["pos"], a["ref"])
        print(f"  REF de {a['chrom']}:{a['pos']} {a['ref']}>{a['alt']} vs FASTA hg38: {ok}")
        assert ok, "REF no coincide"
    filas=[]
    for nombre, alelos in CASOS.items():
        for f in FONDOS:
            caso = f"{nombre}_{f}"
            for a in alelos:
                if sp.en_alta_confianza(f, a["chrom"], a["pos"]) is not True:
                    print(f"  AVISO {caso}: {a['pos']} fuera de la region de alta confianza de {f}")
            if not os.path.exists(f"{sp.CASES}/{caso}.vcf.gz"):
                sp.construir(caso, f, alelos, "trans")
            rn.run(f"{caso}_real", f"{sp.CASES}/{caso}.vcf.gz", f, rn.HPO_REAL)
            d = rn.resumen(f"{caso}_real", "BUB1B")
            vt = f"{rn.OUT}/{caso}_real.variants.tsv"
            with open(vt) as fh: rows = list(csv.DictReader(fh, delimiter="\t"))
            plant = [r for r in rows if r["GENE_SYMBOL"]=="BUB1B" and r["CONTRIBUTING_VARIANT"]=="1"]
            d.update({"caso":nombre,"fondo":f,
                      "alelos_ingeridos":f"{sum(1 for a in alelos if any(r['START']==str(a['pos']) and r['ALT']==a['alt'] for r in rows))}/{len(alelos)}",
                      "white":";".join(sorted({r['WHITELIST_VARIANT'] for r in plant})),
                      "clases":";".join(sorted({r['FUNCTIONAL_CLASS'] for r in plant})),
                      "acmg":plant[0]["EXOMISER_ACMG_CLASSIFICATION"] if plant else "",
                      "vscores":";".join(sorted({r['EXOMISER_VARIANT_SCORE'] for r in plant}))})
            filas.append(d); print(json.dumps(d, ensure_ascii=False), flush=True)
    with open("resultados_posthoc.tsv","w",newline="") as fh:
        cols=sorted({k for d in filas for k in d})
        w=csv.DictWriter(fh,fieldnames=cols,delimiter="\t",extrasaction="ignore"); w.writeheader(); w.writerows(filas)
    print("OK")
