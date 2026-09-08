#!/usr/bin/env python3
"""Paso 3 — seguimiento pre-registrado (PREREGISTRO_4P.md, commit fa9eaae, anterior a este script).

Ajuste de Hill de CUATRO parámetros (fondo, tope, EC50, pendiente), variabilidad biológica por réplica
(multiplicador log-normal compartido sobre la EC50, CV_bio) y por placa (CV 0.05), fallos de ajuste
contados como no-rechazo y reportados aparte, t de Welch sobre log10 EC50. Escenarios, semilla y
número de simulaciones fijados por escrito. Nada se elige después de ver un número.
"""
import json, time, numpy as np
from scipy.optimize import curve_fit
from scipy import stats

CONC = np.array([0.0, 5.0, 10.0, 25.0, 50.0, 75.0, 100.0, 200.0, 400.0, 700.0, 1000.0])
NSIM, NSIM_N, ALPHA, SEED = 2000, 600, 0.05, 20260908
CENTRAL = dict(f=0.30, e_aneu=40.0, r=4.0, m=1.0, cv=0.10, cv_bio=0.20, n=3)
SWEEPS = dict(f=[0.10, 0.20, 0.30, 0.50], r=[2.0, 4.0], n=[3, 4, 6, 8],
              cv_bio=[0.10, 0.20, 0.30], cv=[0.05, 0.10, 0.15])
CV_PLATE = 0.05
LB = [0.0, 0.5, 0.0, 0.2]; UB = [0.5, 1.5, 4.0, 6.0]; P0 = [0.0, 1.0, np.log10(80.0), 1.0]

def hill(c, e, m):
    with np.errstate(divide="ignore", invalid="ignore"):
        out = 1.0 / (1.0 + np.power(np.divide(c, e, where=(c > 0)), m))
    return np.where(c > 0, out, 1.0)

def truth(c, f, e_aneu, r, m):
    return (1.0 - f) * hill(c, e_aneu * r, m) + f * hill(c, e_aneu, m)

def model4(x, b, t, log_e, mm):
    return b + (t - b) * hill(x, 10.0 ** log_e, mm)

def fit4(c, y):
    """log10 EC50 from the four-parameter fit, or nan on a pre-registered failure."""
    try:
        p, _ = curve_fit(model4, c, y, p0=P0, bounds=(LB, UB), maxfev=20000)
    except Exception:
        return np.nan
    b, t, log_e, mm = p
    if log_e <= LB[2] + 1e-6 or log_e >= UB[2] - 1e-6: return np.nan     # EC50 at a bound
    if t < b + 0.2: return np.nan                                          # degenerate curve
    return log_e

def fit2(c, y):
    """The original two-parameter fit (top 1, bottom 0), for the paired comparison only."""
    def model(x, log_e, mm): return hill(x, 10.0 ** log_e, mm)
    try:
        p, _ = curve_fit(model, c, y, p0=[np.log10(80.0), 1.0], bounds=([0.0, 0.2], [4.0, 6.0]), maxfev=8000)
    except Exception:
        return np.nan
    return p[0]

def simulate_curve(rng, f, e_aneu, r, m, cv, cv_bio):
    """One biological replicate: shared EC50 multiplier, plate offset, per-well noise."""
    bio = np.exp(rng.normal(0.0, cv_bio))
    plate = np.exp(rng.normal(0.0, CV_PLATE))
    y = truth(CONC, f, e_aneu * bio, r, m) * plate * np.exp(rng.normal(0.0, cv, CONC.size))
    return y

def power(rng, f, e_aneu, r, m, cv, cv_bio, n, nsim=NSIM, fitter=fit4, also2=False):
    reject = fail = reject2 = 0
    for _ in range(nsim):
        pat = [simulate_curve(rng, f, e_aneu, r, m, cv, cv_bio) for _ in range(n)]
        ctl = [simulate_curve(rng, 0.0, e_aneu, r, m, cv, cv_bio) for _ in range(n)]
        ep = np.array([fitter(CONC, y) for y in pat]); ec = np.array([fitter(CONC, y) for y in ctl])
        if np.isnan(ep).any() or np.isnan(ec).any():
            fail += 1
        elif stats.ttest_ind(ep, ec, equal_var=False).pvalue < ALPHA:
            reject += 1
        if also2:
            ep2 = np.array([fit2(CONC, y) for y in pat]); ec2 = np.array([fit2(CONC, y) for y in ctl])
            if not (np.isnan(ep2).any() or np.isnan(ec2).any()) and stats.ttest_ind(ep2, ec2, equal_var=False).pvalue < ALPHA:
                reject2 += 1
    out = dict(power=reject / nsim, fit_failure_rate=fail / nsim)
    if also2: out["power_2p_same_data"] = reject2 / nsim
    return out

def n_for_power(rng, target=0.80, nmax=24, **kw):
    for n in range(3, nmax + 1):
        if power(rng, n=n, nsim=NSIM_N, **kw)["power"] >= target: return n
    return None

def main():
    t0 = time.time(); rng = np.random.default_rng(SEED)
    out = {"central_params": CENTRAL, "conc_nM": CONC.tolist(), "nsim": NSIM, "cv_plate": CV_PLATE, "seed": SEED}
    c = power(rng, **CENTRAL, also2=True); out["central"] = c
    print(f"CENTRAL {CENTRAL}\n  4p power {c['power']:.3f}  fit-failure rate {c['fit_failure_rate']:.3f}  2p power on the same data {c['power_2p_same_data']:.3f}")
    out["sweeps"] = {}
    for key, values in SWEEPS.items():
        out["sweeps"][key] = {}
        for v in values:
            kw = dict(CENTRAL); kw[key] = v
            res = power(rng, **kw); out["sweeps"][key][str(v)] = res
            print(f"  sweep {key}={v:<5}  4p power {res['power']:.3f}  failures {res['fit_failure_rate']:.3f}")
    out["n_for_80"] = {}
    for f in (0.30, 0.20, 0.10):
        kw = dict(CENTRAL); kw.pop("n"); kw["f"] = f
        n = n_for_power(rng, **kw); out["n_for_80"][str(f)] = n
        print(f"  n for 0.80 power at f={f}: {n if n else '>24'}")
    out["predictions"] = {
        "P-4P1_central_below_0.80": c["power"] < 0.80,
        "P-4P2_failure_rate_ge_0.05": c["fit_failure_rate"] >= 0.05,
        "P-4P3_n80_f030_ge_5_and_f010_gt_24": (out["n_for_80"]["0.3"] is None or out["n_for_80"]["0.3"] >= 5) and out["n_for_80"]["0.1"] is None,
        "P-4P4_2p_recovers_more_than_half": (c["power_2p_same_data"] - c["power"]) > 0.5 * (0.897 - c["power"]),
    }
    out["runtime_s"] = round(time.time() - t0, 1)
    print(out["predictions"], f"runtime {out['runtime_s']} s")
    json.dump(out, open("resultados_4p.json", "w"), indent=1, default=lambda x: None if x is None else float(x) if isinstance(x, (np.floating,)) else bool(x) if isinstance(x, (np.bool_,)) else x)

if __name__ == "__main__":
    main()
