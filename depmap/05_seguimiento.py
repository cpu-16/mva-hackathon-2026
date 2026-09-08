#!/usr/bin/env python3
"""Paso 5 — seguimiento pre-registrado (PREREGISTRO_SEGUIMIENTO.md, commit ee59c9e, anterior a este script).

S1 tamaños de efecto con IC bootstrap · S2 interacción como coeficiente (OLS, IC analítico y bootstrap)
S3 dentro del estrato sólido por linaje · S4 leave-one-lineage-out · S5 rabdomiosarcoma (descriptivo)
S6 solapamiento de ensayos · S7 sensibilidad a la definición del score.
Nada se elige después de ver un número: los umbrales (n>=20), la semilla, los remuestreos y las dos
definiciones alternativas del score están fijados por escrito.
"""
import json, numpy as np, pandas as pd
from scipy import stats

SEED, B, NMIN = 20260908, 2000, 20
DRUGS = ["BORTEZOMIB", "CARFILZOMIB", "IXAZOMIB", "METFORMIN", "TRAMETINIB", "EVEROLIMUS", "PACLITAXEL"]
CORE20S = [f"PSMA{i}" for i in range(1, 8)] + [f"PSMB{i}" for i in range(1, 8)]
rng = np.random.default_rng(SEED)

# ---------- datos, idénticos a 02/03 ----------
an = pd.read_csv("aneuploidy_by_model.csv")
lm = pd.read_csv("lineage_map.tsv", sep="\t").set_index("OncotreeLineage")["stratum"]
an["stratum"] = an.OncotreeLineage.map(lm).fillna("solid")
an = an[an.stratum != "excluded"].set_index("ModelID")
an["frac"] = an.aneuploidy_score / an.arms_callable                       # S7 (i)
sl = stats.linregress(an.ploidy, an.aneuploidy_score)                     # S7 (ii)
an["resid"] = an.aneuploidy_score - (sl.intercept + sl.slope * an.ploidy)

cl = pd.read_csv("raw/Repurposing_CompoundList.csv"); cl = cl[cl.screen == "REP.PRIMARY"]
brd = {d: cl[cl["Drug.Name"].str.upper() == d].IDs.iloc[0].split(",")[0].strip() for d in DRUGS}
mat = pd.read_csv("raw/Repurposing_Extended_Primary_Matrix.csv", index_col=0); mat.index = mat.index.astype(str)
lfc = mat.loc[list(brd.values())]; lfc.index = list(brd.keys())

ce = pd.read_csv("raw/CRISPRGeneEffect.csv", index_col=0)
sym = {c.split(" (")[0]: c for c in ce.columns}
cr = an.join(ce[[sym[g] for g in CORE20S]].rename(columns={sym[g]: g for g in CORE20S}), how="inner")
cr["core20S_mean"] = cr[CORE20S].mean(axis=1)

sub = pd.read_csv("raw/Model.csv", usecols=["ModelID", "OncotreeSubtype"]).set_index("ModelID")["OncotreeSubtype"]

# ---------- utilidades ----------
def rho_ci(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float); n = len(x)
    r = stats.spearmanr(x, y)[0]
    idx = rng.integers(0, n, (B, n))
    bs = np.array([stats.spearmanr(x[i], y[i])[0] for i in idx])
    lo, hi = np.nanpercentile(bs, [2.5, 97.5])
    return r, lo, hi, n

def ols(y, X, names):
    X = np.column_stack([np.ones(len(y))] + X); beta = np.linalg.lstsq(X, y, rcond=None)[0]
    r = y - X @ beta; dof = len(y) - X.shape[1]; s2 = (r @ r) / dof
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X))); t = beta / se
    p = 2 * stats.t.sf(np.abs(t), dof); tcrit = stats.t.ppf(0.975, dof)
    return {n: dict(beta=b, se=e, p=q, lo=b - tcrit * e, hi=b + tcrit * e) for n, b, e, q in zip(["const"] + names, beta, se, p)}

def interaction_model(d, score="aneuploidy_score", gene="PSMB5"):
    d = d.dropna(subset=[gene, score, "ploidy"])
    y = d[gene].values.astype(float); a = d[score].values.astype(float)
    h = (d.stratum == "haematological").values.astype(float); p = d.ploidy.values.astype(float)
    full = ols(y, [a, h, a * h, p], ["score", "haem", "score:haem", "ploidy"])
    main = ols(y, [a, h, p], ["score", "haem", "ploidy"])
    # bootstrap del coeficiente de interacción
    idx = rng.integers(0, len(y), (B, len(y)))
    bs = []
    for i in idx:
        X = np.column_stack([np.ones(len(i)), a[i], h[i], a[i] * h[i], p[i]])
        bs.append(np.linalg.lstsq(X, y[i], rcond=None)[0][3])
    full["score:haem"]["boot_lo"], full["score:haem"]["boot_hi"] = np.percentile(bs, [2.5, 97.5])
    return full, main, len(y)

out, lines = {}, []
def say(s=""): print(s); lines.append(s)

# ---------- S1 ----------
say("## S1 — effect sizes with 95% bootstrap intervals")
s1 = []
for drug in DRUGS:
    s = lfc.loc[drug].dropna()
    d = an.join(s.rename("lfc"), how="inner"); d = d[d.stratum == "solid"]
    r, lo, hi, n = rho_ci(d.aneuploidy_score, d.lfc)
    s1.append(dict(measure=f"PRISM {drug.title()}", stratum="solid", n=n, rho=r, lo=lo, hi=hi, score="arms"))
    say(f"  {drug:12s} solid n={n:4d}  rho={r:+.3f} [{lo:+.3f}, {hi:+.3f}]")
for st in ["all", "solid", "haematological"]:
    d = cr if st == "all" else cr[cr.stratum == st]
    for g in ["PSMB5", "core20S_mean"]:
        r, lo, hi, n = rho_ci(d.aneuploidy_score, d[g])
        s1.append(dict(measure=f"CRISPR {g}", stratum=st, n=n, rho=r, lo=lo, hi=hi, score="arms"))
        say(f"  CRISPR {g:13s} {st:14s} n={n:4d}  rho={r:+.3f} [{lo:+.3f}, {hi:+.3f}]")

# ---------- S2 ----------
say("\n## S2 — PSMB5 ~ score + haem + score×haem + ploidy (OLS), and the main-effects model")
full, main, n2 = interaction_model(cr)
for k, v in full.items():
    extra = f"  boot95=[{v['boot_lo']:+.5f}, {v['boot_hi']:+.5f}]" if "boot_lo" in v else ""
    say(f"  full   {k:11s} beta={v['beta']:+.5f}  95%CI=[{v['lo']:+.5f}, {v['hi']:+.5f}]  p={v['p']:.4g}{extra}")
for k, v in main.items():
    say(f"  main   {k:11s} beta={v['beta']:+.5f}  95%CI=[{v['lo']:+.5f}, {v['hi']:+.5f}]  p={v['p']:.4g}")
slope_solid = full["score"]["beta"]; slope_haem = full["score"]["beta"] + full["score:haem"]["beta"]
say(f"  change in PSMB5 gene effect per 10 altered arms: solid {10*slope_solid:+.3f}, haematological {10*slope_haem:+.3f}  (n={n2})")
out["S2"] = dict(full=full, main=main, n=n2, per10_solid=10 * slope_solid, per10_haem=10 * slope_haem)

# ---------- S3 ----------
say("\n## S3 — inside the solid stratum, by OncotreeLineage (n>=20 = pre-registered floor; below = descriptive)")
s3 = []
bort = an.join(lfc.loc["BORTEZOMIB"].dropna().rename("lfc"), how="inner"); bort = bort[bort.stratum == "solid"]
for name, d, col in [("PRISM bortezomib", bort, "lfc"), ("CRISPR PSMB5", cr[cr.stratum == "solid"], "PSMB5")]:
    for lin, g in d.groupby("OncotreeLineage"):
        if len(g) < 5: continue
        r, lo, hi, n = rho_ci(g.aneuploidy_score, g[col])
        s3.append(dict(measure=name, lineage=lin, n=n, rho=r, lo=lo, hi=hi, floor="OK" if n >= NMIN else "descriptive (n<20)"))
S3 = pd.DataFrame(s3).sort_values(["measure", "n"], ascending=[True, False])
say(S3.to_string(index=False, float_format=lambda x: f"{x:+.3f}"))
S3.to_csv("resultados_seguimiento_lineajes.csv", index=False)

# ---------- S4 ----------
say("\n## S4 — leave-one-lineage-out (solid stratum)")
s4 = []
base_b = stats.spearmanr(bort.aneuploidy_score, bort.lfc)[0]
crs = cr[cr.stratum == "solid"]; base_p = stats.spearmanr(crs.aneuploidy_score, crs.PSMB5)[0]
for lin in sorted(set(crs.OncotreeLineage) | set(bort.OncotreeLineage)):
    b2 = bort[bort.OncotreeLineage != lin]; p2 = crs[crs.OncotreeLineage != lin]
    rb = stats.spearmanr(b2.aneuploidy_score, b2.lfc)[0] if len(b2) >= NMIN else np.nan
    rp = stats.spearmanr(p2.aneuploidy_score, p2.PSMB5)[0]
    f2, _, _ = interaction_model(pd.concat([cr[cr.stratum == "haematological"], p2]))
    ic = f2["score:haem"]
    s4.append(dict(dropped=lin, n_dropped_crispr=int((crs.OncotreeLineage == lin).sum()),
                   rho_bortezomib=rb, rho_psmb5=rp, inter_beta=ic["beta"], inter_lo=ic["lo"], inter_hi=ic["hi"], inter_p=ic["p"]))
S4 = pd.DataFrame(s4)
flip_b = S4[np.sign(S4.rho_bortezomib.fillna(base_b)) != np.sign(base_b)].dropped.tolist()
flip_p = S4[np.sign(S4.rho_psmb5) != np.sign(base_p)].dropped.tolist()
cross = S4[(S4.inter_lo <= 0) & (S4.inter_hi >= 0)].dropped.tolist()
say(f"  baseline: bortezomib rho={base_b:+.3f}, PSMB5 rho={base_p:+.3f}, interaction beta={full['score:haem']['beta']:+.5f}")
say(f"  bortezomib rho range {S4.rho_bortezomib.min():+.3f}..{S4.rho_bortezomib.max():+.3f}; sign flips: {flip_b or 'none'}")
say(f"  PSMB5 rho range {S4.rho_psmb5.min():+.3f}..{S4.rho_psmb5.max():+.3f}; sign flips: {flip_p or 'none'}")
say(f"  interaction beta range {S4.inter_beta.min():+.5f}..{S4.inter_beta.max():+.5f}; p range {S4.inter_p.min():.3g}..{S4.inter_p.max():.3g}; CI crosses zero when dropping: {cross or 'none'}")
verdict_s4 = "driven by composition" if (flip_b or flip_p or cross) else "not driven by any single lineage"
say(f"  -> pre-registered criterion: {verdict_s4}")
S4.to_csv("resultados_seguimiento_loo.csv", index=False)

# ---------- S5 ----------
say("\n## S5 — rhabdomyosarcoma coverage (descriptive only; no statistic on 3 or 10 lines)")
rms = an[an.index.map(sub).fillna("").str.contains("habdomyosarcoma")].copy()
rms["subtype"] = rms.index.map(sub)
rms["bortezomib_lfc"] = lfc.loc["BORTEZOMIB"].reindex(rms.index)
rms["PSMB5"] = ce[sym["PSMB5"]].reindex(rms.index)
solid_lfc = bort.lfc; solid_p = crs.PSMB5
rms["lfc_percentile_in_solid"] = rms.bortezomib_lfc.apply(lambda v: np.nan if pd.isna(v) else 100 * (solid_lfc < v).mean())
rms["PSMB5_percentile_in_solid"] = rms.PSMB5.apply(lambda v: np.nan if pd.isna(v) else 100 * (solid_p < v).mean())
say(rms[["subtype", "aneuploidy_score", "ploidy", "bortezomib_lfc", "lfc_percentile_in_solid", "PSMB5", "PSMB5_percentile_in_solid"]]
    .to_string(float_format=lambda x: f"{x:.2f}"))
say(f"  scored RMS lines: {len(rms)}; with PRISM bortezomib: {rms.bortezomib_lfc.notna().sum()}; with CRISPR PSMB5: {rms.PSMB5.notna().sum()}")
rms.to_csv("resultados_seguimiento_rms.csv")

# ---------- S6 ----------
say("\n## S6 — the two assays on the same models")
both = bort.join(cr[["PSMB5"]], how="inner")
r_bp, lo_bp, hi_bp, n_bp = rho_ci(both.lfc, both.PSMB5)
r_sb, lo_sb, hi_sb, _ = rho_ci(both.aneuploidy_score, both.lfc)
r_sp, lo_sp, hi_sp, _ = rho_ci(both.aneuploidy_score, both.PSMB5)
say(f"  shared solid models n={n_bp}: rho(bortezomib LFC, PSMB5 effect)={r_bp:+.3f} [{lo_bp:+.3f}, {hi_bp:+.3f}]")
say(f"  in that set: rho(score, LFC)={r_sb:+.3f} [{lo_sb:+.3f}, {hi_sb:+.3f}]; rho(score, PSMB5)={r_sp:+.3f} [{lo_sp:+.3f}, {hi_sp:+.3f}]")
out["S6"] = dict(n=n_bp, rho_lfc_psmb5=[r_bp, lo_bp, hi_bp], rho_score_lfc=[r_sb, lo_sb, hi_sb], rho_score_psmb5=[r_sp, lo_sp, hi_sp])

# ---------- S7 ----------
say("\n## S7 — sensitivity to the score definition (fixed alternatives: fraction of callable arms; ploidy-residualised)")
s7 = []
for score in ["frac", "resid"]:
    for drug in ["BORTEZOMIB", "CARFILZOMIB", "IXAZOMIB"]:
        d = an.join(lfc.loc[drug].dropna().rename("lfc"), how="inner"); d = d[d.stratum == "solid"]
        r, lo, hi, n = rho_ci(d[score], d.lfc)
        s7.append(dict(score=score, measure=f"PRISM {drug.title()}", n=n, rho=r, lo=lo, hi=hi))
        say(f"  [{score:5s}] {drug:12s} rho={r:+.3f} [{lo:+.3f}, {hi:+.3f}]")
    f7, _, _ = interaction_model(cr, score=score)
    ic = f7["score:haem"]
    s7.append(dict(score=score, measure="interaction score:haem (PSMB5)", n=n2, rho=np.nan, lo=ic["lo"], hi=ic["hi"], beta=ic["beta"], p=ic["p"], boot_lo=ic["boot_lo"], boot_hi=ic["boot_hi"]))
    say(f"  [{score:5s}] interaction beta={ic['beta']:+.5f} 95%CI=[{ic['lo']:+.5f}, {ic['hi']:+.5f}] p={ic['p']:.4g} boot95=[{ic['boot_lo']:+.5f}, {ic['boot_hi']:+.5f}]")
S7 = pd.DataFrame(s7)
signs_ok = all(np.sign(S7[S7.measure.str.startswith("PRISM")].rho) == np.sign([r["rho"] for r in s1 if r["measure"] in ("PRISM Bortezomib", "PRISM Carfilzomib", "PRISM Ixazomib")] * 2)) \
           and all(S7[S7.measure.str.startswith("interaction")].beta < 0)
say(f"  -> signs unchanged under both alternatives: {signs_ok}")

pd.concat([pd.DataFrame(s1), S7], ignore_index=True).to_csv("resultados_seguimiento.csv", index=False)
out["S4"] = dict(verdict=verdict_s4, flips_bortezomib=flip_b, flips_psmb5=flip_p, ci_crosses_zero_when_dropping=cross)
out["S7_signs_unchanged"] = bool(signs_ok)
out["P-S1"] = bool(lo <= 0 <= hi) if False else bool([r for r in s1 if r["measure"] == "PRISM Bortezomib"][0]["lo"] <= 0 <= [r for r in s1 if r["measure"] == "PRISM Bortezomib"][0]["hi"])
ic = full["score:haem"]
out["P-S2"] = bool((ic["lo"] < 0 and ic["hi"] < 0) and (ic["boot_lo"] < 0 and ic["boot_hi"] < 0))
out["P-S3"] = verdict_s4 == "not driven by any single lineage"
out["P-S5"] = bool(signs_ok)
json.dump(out, open("resultados_seguimiento.json", "w"), indent=1, default=float)
open("_seguimiento_stdout.txt", "w").write("\n".join(lines))
say(f"\nP-S1 {out['P-S1']}  P-S2 {out['P-S2']}  P-S3 {out['P-S3']}  P-S5 {out['P-S5']}")

# ---------- figura 5: forest de S1 + S3 ----------
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 6.2), gridspec_kw=dict(width_ratios=[1, 1.15]))
S1 = pd.DataFrame(s1); S1 = S1[S1.measure.str.startswith("PRISM") | (S1.measure == "CRISPR PSMB5")]
lab = [f"{m.replace('PRISM ','')} · {st}" if m.startswith("CRISPR") else m.replace("PRISM ", "") for m, st in zip(S1.measure, S1.stratum)]
ys = np.arange(len(S1))[::-1]
a1.errorbar(S1.rho, ys, xerr=[S1.rho - S1.lo, S1.hi - S1.rho], fmt="o", color="#1f3b57", ecolor="#1f3b57", capsize=3, ms=5)
a1.axvline(0, color="#999", lw=0.8); a1.set_yticks(ys); a1.set_yticklabels(lab, fontsize=8.5)
a1.set_xlabel("Spearman ρ with aneuploidy score (95% bootstrap CI)\nρ < 0: more aneuploid → more sensitive / more dependent", fontsize=8.5)
a1.set_title("S1 — effect sizes, solid lines (PRISM) and strata (CRISPR PSMB5)", fontsize=9.5, loc="left")
for m, col in [("CRISPR PSMB5", "#b5473a"), ("PRISM bortezomib", "#1f3b57")]:
    g = S3[S3.measure == m].sort_values("n", ascending=True)
    yy = np.arange(len(g)) + (0.18 if m.startswith("PRISM") else -0.18)
    a2.errorbar(g.rho, yy, xerr=[g.rho - g.lo, g.hi - g.rho], fmt="o", color=col, ecolor=col, capsize=2, ms=4, alpha=[1 if f == "OK" else 0.45 for f in g.floor][0] if False else 0.95, label=m)
    if m == "CRISPR PSMB5":
        a2.set_yticks(np.arange(len(g))); a2.set_yticklabels([f"{l} (n={n})" for l, n in zip(g.lineage, g.n)], fontsize=7.8)
a2.axvline(0, color="#999", lw=0.8); a2.legend(fontsize=8, loc="lower right")
a2.set_xlabel("Spearman ρ within lineage (95% bootstrap CI); n < 20 is descriptive, see table", fontsize=8.5)
a2.set_title("S3 — inside the solid stratum, by lineage", fontsize=9.5, loc="left")
fig.suptitle("DepMap follow-up (pre-registered): the aneuploidy–proteasome association, with its uncertainty", fontsize=11, x=0.01, ha="left")
fig.tight_layout(rect=[0, 0, 1, 0.95]); fig.savefig("fig5_seguimiento.png", dpi=170)
print("fig5_seguimiento.png written")
