#!/usr/bin/env python3
"""Slope of PSMB5 dependency per altered chromosome arm, per potencia/PREREGISTRO_2_DOSIS.md.

Attacks our own power result: the mixture model treats aneuploidy as a switch, but an MVA cell
carries about one altered chromosome, not the sixteen of the lines the 4x selectivity came from.
"""
import csv, json
import numpy as np

SRC = "depmap/psmb5_merged.csv"
ARMS_MVA = 2          # one whole chromosome = two arms
ARMS_HIGH = 18        # the order of a highly aneuploid cancer line (declared, not fitted)


def load():
    rows = []
    with open(SRC) as f:
        for r in csv.DictReader(f):
            try:
                rows.append(dict(arms=float(r["aneuploidy_score"]), ploidy=float(r["ploidy"]),
                                 psmb5=float(r["PSMB5"]), stratum=r["stratum"]))
            except (ValueError, KeyError):
                continue
    return rows


def ols(X, y):
    """Returns beta, standard errors, residual sd, dof."""
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = len(y) - X.shape[1]
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.pinv(X.T @ X)
    return beta, np.sqrt(np.diag(cov)), float(np.sqrt(s2)), dof


def fit(rows, quadratic=False):
    a = np.array([r["arms"] for r in rows])
    p = np.array([r["ploidy"] for r in rows])
    y = np.array([r["psmb5"] for r in rows])
    cols = [np.ones_like(a), a, p] + ([a ** 2] if quadratic else [])
    return ols(np.column_stack(cols), y), len(rows)


def main():
    from scipy import stats
    rows = load()
    out = {"n_total": len(rows), "arms_mva": ARMS_MVA, "arms_high": ARMS_HIGH, "strata": {}}
    print(f"{len(rows)} líneas con PSMB5, aneuploidía y ploidía\n")

    for stratum in ("solid", "haematological"):
        sub = [r for r in rows if r["stratum"] == stratum]
        if len(sub) < 30:
            continue
        (beta, se, sigma, dof), n = fit(sub)
        b1, se1 = beta[1], se[1]
        tcrit = stats.t.ppf(0.975, dof)
        lo, hi = b1 - tcrit * se1, b1 + tcrit * se1
        p1 = 2 * (1 - stats.t.cdf(abs(b1 / se1), dof))
        d2, d18 = b1 * ARMS_MVA, b1 * ARMS_HIGH

        # curvature check, pre-declared
        (betaq, seq, _, dofq), _ = fit(sub, quadratic=True)
        pq = 2 * (1 - stats.t.cdf(abs(betaq[3] / seq[3]), dofq))

        d = dict(n=n, slope_per_arm=b1, se=se1, ci95=[lo, hi], p=p1, resid_sd=sigma,
                 delta_2arms=d2, delta_18arms=d18,
                 ratio_2=abs(d2) / sigma, ratio_18=abs(d18) / sigma,
                 quad_coef=betaq[3], quad_p=pq,
                 arms_mean=float(np.mean([r["arms"] for r in sub])))
        out["strata"][stratum] = d
        print(f"=== {stratum}  (n={n}, media {d['arms_mean']:.1f} brazos alterados) ===")
        print(f"  pendiente por brazo   {b1:+.5f}  IC95 [{lo:+.5f}, {hi:+.5f}]  p={p1:.3f}")
        print(f"  SD residual de PSMB5  {sigma:.4f}")
        print(f"  Δ a {ARMS_MVA} brazos (una célula MVA)  {d2:+.4f}  =  {abs(d2)/sigma:.3f} SD residual")
        print(f"  Δ a {ARMS_HIGH} brazos (línea muy aneuploide)  {d18:+.4f}  =  {abs(d18)/sigma:.3f} SD residual")
        print(f"  término cuadrático    {betaq[3]:+.6f}  p={pq:.3f}\n")

    s = out["strata"].get("solid")
    if s:
        r2 = s["ratio_2"]
        ci_covers_zero = s["ci95"][0] <= 0 <= s["ci95"][1]
        if ci_covers_zero:
            verdict = ("FALSIFICACIÓN DEL EJERCICIO: la pendiente no difiere de cero en sólidos, "
                       "así que este análisis NO puede acotar la selectividad. Se reporta como no informativo.")
        elif r2 >= 0.25:
            verdict = "≥0.25 SD: la selectividad 4× no es implausible; el resultado de la mañana se sostiene."
        elif r2 < 0.10:
            verdict = ("<0.10 SD: el efecto de un cromosoma es despreciable en la escala que separa líneas. "
                       "EL ESCENARIO CENTRAL DE LA MAÑANA NO ES DEFENDIBLE y hay que re-centrarlo.")
        else:
            verdict = "entre 0.10 y 0.25 SD: hay que re-correr la potencia a la selectividad implicada."
        out["verdict"] = verdict
        print("VEREDICTO (estrato sólido, el relevante para este niño):")
        print(" ", verdict)

    json.dump(out, open("potencia/dosis.json", "w"), indent=2)


if __name__ == "__main__":
    main()


def contraste_no_parametrico():
    """POST-HOC, no pre-registrado: comparación directa bajo-vs-alto sin asumir linealidad.

    Se etiqueta como robustez exploratoria porque el pre-registro fijó una regresión lineal.
    Un lector debe leerlo como "la conclusión no depende del modelo lineal", no como una prueba.
    """
    from scipy import stats
    import numpy as np
    rows = load()
    print("\n--- POST-HOC (no pre-registrado): bajo vs alto, sin modelo lineal ---")
    out = {}
    for st in ("solid", "haematological"):
        sub = [r for r in rows if r["stratum"] == st]
        low = np.array([r["psmb5"] for r in sub if r["arms"] <= 4])
        high = np.array([r["psmb5"] for r in sub if r["arms"] >= 16])
        if len(low) < 10 or len(high) < 10:
            continue
        t = stats.mannwhitneyu(low, high)
        sd = np.std([r["psmb5"] for r in sub], ddof=1)
        d = (low.mean() - high.mean()) / sd
        out[st] = dict(n_low=len(low), n_high=len(high), mean_low=float(low.mean()),
                       mean_high=float(high.mean()), cohens_d=float(d), p=float(t.pvalue))
        print(f"  {st}: <=4 brazos n={len(low)} media {low.mean():+.3f} | "
              f">=16 brazos n={len(high)} media {high.mean():+.3f} | "
              f"d={d:+.3f}  p={t.pvalue:.4f}")
    return out


if __name__ == "__main__":
    import json as _j
    extra = contraste_no_parametrico()
    d = _j.load(open("potencia/dosis.json"))
    d["posthoc_low_vs_high"] = extra
    _j.dump(d, open("potencia/dosis.json", "w"), indent=2)
