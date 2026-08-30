#!/usr/bin/env python3
"""Paso 2 — la prueba pre-registrada. Ver PREREGISTRO.md (commit 4b0b7c2, anterior a este script).

Nada aquí se elige después de ver resultados: los 7 fármacos, las 3 estratificaciones,
el estadístico (Spearman), la corrección (BH sobre 21 pruebas) y el piso de potencia (n>=20)
estaban fijados por escrito.
"""
import pandas as pd, numpy as np
from scipy import stats

DRUGS = ["BORTEZOMIB","CARFILZOMIB","IXAZOMIB","METFORMIN","TRAMETINIB","EVEROLIMUS","PACLITAXEL"]
PRED = {"BORTEZOMIB":"sensible","CARFILZOMIB":"sensible","IXAZOMIB":"sensible",
        "METFORMIN":"nulo","TRAMETINIB":"nulo","EVEROLIMUS":"no sensible","PACLITAXEL":"nulo (control)"}

# --- fármaco -> BRD id, restringido al cribado REP.PRIMARY (único que contiene estos 7)
cl = pd.read_csv("raw/Repurposing_CompoundList.csv")
cl = cl[cl.screen == "REP.PRIMARY"]
brd = {}
for d in DRUGS:
    r = cl[cl["Drug.Name"].str.upper() == d]
    if len(r) == 0: print(f"  !! {d} sin BRD id"); continue
    brd[d] = r.IDs.iloc[0].split(",")[0].strip()

# --- matriz de sensibilidad (LFC; más negativo = más muerte celular)
mat = pd.read_csv("raw/Repurposing_Extended_Primary_Matrix.csv", index_col=0)
mat.index = mat.index.astype(str)
lfc = mat.loc[[b for b in brd.values() if b in mat.index]]
lfc.index = [k for k, v in brd.items() if v in mat.index]
print(f"fármacos recuperados de la matriz: {list(lfc.index)}")

# --- aneuploidía + linaje
an = pd.read_csv("aneuploidy_by_model.csv")
lm = pd.read_csv("lineage_map.tsv", sep="\t").set_index("OncotreeLineage")["stratum"]
an["stratum"] = an.OncotreeLineage.map(lm).fillna("solid")
an = an[an.stratum != "excluded"]

res = []
for drug in lfc.index:
    s = lfc.loc[drug].dropna()
    d = an.set_index("ModelID").join(s.rename("lfc"), how="inner").dropna(subset=["lfc"])
    for stratum in ["all", "solid", "haematological"]:
        sub = d if stratum == "all" else d[d.stratum == stratum]
        n = len(sub)
        if n < 3: continue
        rho, p = stats.spearmanr(sub.aneuploidy_score, sub.lfc)
        # LFC negativo = muerte -> rho negativo significa "más aneuploide, más sensible"
        res.append(dict(drug=drug, stratum=stratum, n=n, rho=rho,
                        p=p if n >= 20 else np.nan,
                        direccion="sensible" if rho < 0 else "resistente",
                        prediccion=PRED[drug],
                        potencia="OK" if n >= 20 else "descriptivo (n<20)"))

R = pd.DataFrame(res)
ok = R.p.notna()
q = np.full(len(R), np.nan)
pv = R.loc[ok, "p"].values
order = np.argsort(pv); ranked = pv[order]
qv = ranked * len(ranked) / (np.arange(len(ranked)) + 1)
qv = np.minimum.accumulate(qv[::-1])[::-1]
tmp = np.empty(len(ranked)); tmp[order] = np.minimum(qv, 1.0)
q[np.where(ok)[0]] = tmp
R["q_BH"] = q
R["signif_FDR05"] = R.q_BH < 0.05
R.to_csv("resultados_prereg.csv", index=False)

pd.set_option("display.width", 200)
print("\n" + "="*100)
print("RESULTADO DE LA PRUEBA PRE-REGISTRADA  (rho<0 = más aneuploide -> más sensible)")
print("="*100)
print(R[["drug","stratum","n","rho","p","q_BH","signif_FDR05","direccion","prediccion","potencia"]]
      .to_string(index=False, float_format=lambda x: f"{x:.4g}"))
