#!/usr/bin/env python3
"""Paso 3 — extensión declarada en la Enmienda 1 del PREREGISTRO (commit c54e678, previo a este script).

Prueba el MISMO mecanismo (dependencia del proteasoma) con una medida que sí cubre líneas
hematológicas, porque PRISM no las tiene para estos fármacos.
Genes y dirección fijados por escrito antes de correr esto.
"""
import pandas as pd, numpy as np
from scipy import stats

CORE20S = [f"PSMA{i}" for i in range(1,8)] + [f"PSMB{i}" for i in range(1,8)]
ATP19S  = [f"PSMC{i}" for i in range(1,7)]
NEGCTRL = ["PSMD9"]

an = pd.read_csv("aneuploidy_by_model.csv")
lm = pd.read_csv("lineage_map.tsv", sep="\t").set_index("OncotreeLineage")["stratum"]
an["stratum"] = an.OncotreeLineage.map(lm).fillna("solid")
an = an[an.stratum != "excluded"].set_index("ModelID")

ce = pd.read_csv("raw/CRISPRGeneEffect.csv", index_col=0)
sym = {c.split(" (")[0]: c for c in ce.columns}
print(f"CRISPR: {ce.shape[0]:,} líneas × {ce.shape[1]:,} genes")

d0 = an.join(ce, how="inner")
print("líneas con score + CRISPR por estrato:")
print(d0.stratum.value_counts().to_string())

def rho(gene, stratum):
    col = sym.get(gene)
    if col is None: return None
    sub = d0 if stratum == "all" else d0[d0.stratum == stratum]
    v = sub[col].astype(float); m = v.notna()
    if m.sum() < 20: return None
    r, p = stats.spearmanr(sub.aneuploidy_score[m], v[m])
    return dict(gene=gene, stratum=stratum, n=int(m.sum()), rho=r, p=p)

rows = [r for g in CORE20S + ATP19S + NEGCTRL for s in ["all","solid","haematological"]
        if (r := rho(g, s)) is not None]
for r in rows:
    r["set"] = "20S core" if r["gene"] in CORE20S else ("19S ATPase" if r["gene"] in ATP19S else "control neg")
R = pd.DataFrame(rows)
# BH sobre todas las pruebas
pv = R.p.values; o = np.argsort(pv); q = pv[o]*len(pv)/(np.arange(len(pv))+1)
q = np.minimum.accumulate(q[::-1])[::-1]; qq = np.empty(len(pv)); qq[o] = np.minimum(q,1.0)
R["q_BH"] = qq; R["signif"] = R.q_BH < 0.05
R.to_csv("resultados_crispr.csv", index=False)

# fondo nulo: 200 genes al azar (semilla fija)
rng = np.random.default_rng(20260830)
bg_genes = rng.choice([c for c in ce.columns], 200, replace=False)
bg = []
for c in bg_genes:
    sub = d0[d0.stratum=="solid"]; v = sub[c].astype(float); m = v.notna()
    if m.sum() >= 20: bg.append(stats.spearmanr(sub.aneuploidy_score[m], v[m])[0])
bg = np.array(bg)

print("\n" + "="*92)
print("EXTENSIÓN CRISPR — rho<0 = más aneuploide -> MÁS dependiente del gen (predicho para el proteasoma)")
print("="*92)
for s in ["all","solid","haematological"]:
    sub = R[R.stratum==s]
    if not len(sub): continue
    c20 = sub[sub.set=="20S core"]
    print(f"\n[{s}]  n={c20.n.iloc[0] if len(c20) else 0}")
    print(f"  20S core (14 genes): rho medio {c20.rho.mean():+.4f} | significativos FDR<0.05: {int(c20.signif.sum())}/{len(c20)}")
    a19 = sub[sub.set=="19S ATPase"]
    print(f"  19S ATPasas (6):     rho medio {a19.rho.mean():+.4f} | significativos: {int(a19.signif.sum())}/{len(a19)}")
    nc = sub[sub.set=="control neg"]
    if len(nc): print(f"  PSMD9 (control neg): rho {nc.rho.iloc[0]:+.4f} q={nc.q_BH.iloc[0]:.3g}")
    if s=="solid":
        print(f"  fondo nulo 200 genes: media {bg.mean():+.4f} sd {bg.std():.4f}")
        z=(c20.rho.mean()-bg.mean())/bg.std()
        print(f"  -> separación del 20S respecto al fondo: z = {z:+.2f}")
print("\nPSMB5 (diana de bortezomib):")
print(R[R.gene=="PSMB5"][["stratum","n","rho","p","q_BH","signif"]].to_string(index=False,float_format=lambda x:f"{x:.4g}"))
print("\nTop 6 subunidades más asociadas (sólidos):")
print(R[(R.stratum=="solid")&(R.set!="control neg")].nsmallest(6,"rho")[["gene","set","rho","p","q_BH","signif"]].to_string(index=False,float_format=lambda x:f"{x:.4g}"))
