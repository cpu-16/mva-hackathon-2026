#!/usr/bin/env python3
"""Power of the §6 fibroblast dose-response assay, per potencia/PREREGISTRO.md.

Everything here was fixed in the pre-registration before this file computed anything.
No patient data, no GPU. Seeded and reproducible.
"""
import json
import numpy as np
from scipy.optimize import curve_fit
from scipy import stats

# --- fixed by the pre-registration, §4 -------------------------------------------------
CONC = np.array([0.0, 5.0, 10.0, 25.0, 50.0, 100.0, 200.0, 400.0])   # nM, §6 design
NSIM = 2000
ALPHA = 0.05
CENTRAL = dict(f=0.30, e_aneu=40.0, r=4.0, m=1.0, cv=0.10, n=3)
SWEEPS = dict(f=[0.02, 0.05, 0.10, 0.20, 0.30, 0.50],
              e_aneu=[20.0, 40.0],
              r=[2.0, 3.0, 4.0, 6.0, 10.0],
              m=[1.0, 1.5, 2.0],
              cv=[0.05, 0.10, 0.15],
              n=[3, 4, 6, 8])


def hill(c, e, m):
    """Viability fraction. c=0 gives exactly 1."""
    with np.errstate(divide="ignore", invalid="ignore"):
        out = 1.0 / (1.0 + np.power(np.divide(c, e, where=(c > 0)), m))
    return np.where(c > 0, out, 1.0)


def truth(c, f, e_aneu, r, m):
    """The mixture of §3: a fraction f of aneuploid cells inside a normal background."""
    return (1.0 - f) * hill(c, e_aneu * r, m) + f * hill(c, e_aneu, m)


def fit_log_ec50(c, y):
    """Fit a Hill curve and return log10(EC50), or nan if it does not converge.

    A failed fit is a non-rejection by pre-registration, never a discard.
    """
    def model(x, log_e, mm):
        return hill(x, 10.0 ** log_e, mm)
    try:
        p, _ = curve_fit(model, c, y, p0=[np.log10(80.0), 1.0],
                         bounds=([0.0, 0.2], [4.0, 6.0]), maxfev=8000)
    except Exception:
        return np.nan
    return p[0]


def power(rng, f, e_aneu, r, m, cv, n, nsim=NSIM):
    """Fraction of simulated experiments where patient and control EC50 differ (two-sided t)."""
    reject = 0
    for _ in range(nsim):
        pat, ctl = [], []
        for _ in range(n):
            # multiplicative log-normal noise per well, as declared
            yp = truth(CONC, f, e_aneu, r, m) * np.exp(rng.normal(0.0, cv, CONC.size))
            yc = truth(CONC, 0.0, e_aneu, r, m) * np.exp(rng.normal(0.0, cv, CONC.size))
            pat.append(fit_log_ec50(CONC, yp))
            ctl.append(fit_log_ec50(CONC, yc))
        pat, ctl = np.array(pat), np.array(ctl)
        if np.isnan(pat).any() or np.isnan(ctl).any():
            continue                      # counts as a non-rejection
        t = stats.ttest_ind(pat, ctl, equal_var=True)
        if t.pvalue < ALPHA:
            reject += 1
    return reject / nsim


def n_for_power(rng, target=0.80, nmax=24, **kw):
    """Smallest n reaching `target` power, or None within nmax."""
    for n in range(3, nmax + 1):
        if power(rng, n=n, nsim=600, **kw) >= target:
            return n
    return None


def main():
    rng = np.random.default_rng(20260901)
    out = {"central_params": CENTRAL, "conc_nM": CONC.tolist(), "nsim": NSIM}

    # the separation the assay is actually asked to see, at the central scenario
    sep = {}
    for f in SWEEPS["f"]:
        y = truth(CONC, f, CENTRAL["e_aneu"], CENTRAL["r"], CENTRAL["m"])
        y0 = truth(CONC, 0.0, CENTRAL["e_aneu"], CENTRAL["r"], CENTRAL["m"])
        sep[f] = dict(max_abs_viability_gap=float(np.max(np.abs(y - y0))),
                      ec50_ratio=float(10 ** (fit_log_ec50(CONC, y0) - fit_log_ec50(CONC, y))))
    out["separation_noiseless"] = sep
    print("Separación sin ruido (paciente vs control), escenario central salvo f:")
    for f, v in sep.items():
        print(f"  f={f:.2f}   brecha máx. de viabilidad {v['max_abs_viability_gap']:.4f}"
              f"   razón EC50 {v['ec50_ratio']:.2f}×")

    p_central = power(rng, **CENTRAL)
    out["power_central"] = p_central
    print(f"\nPOTENCIA, escenario central {CENTRAL}: {p_central:.3f}")

    out["sweeps"] = {}
    for key, values in SWEEPS.items():
        row = {}
        for v in values:
            kw = dict(CENTRAL)
            kw[key] = v
            row[str(v)] = power(rng, **kw)
        out["sweeps"][key] = row
        print(f"\nbarrido {key}:")
        for v, p in row.items():
            print(f"  {key}={v:>6s}  potencia {p:.3f}")

    # what n would be needed, at the central scenario and at the pessimistic f
    out["n_for_80"] = {}
    for f in (0.30, 0.10, 0.05, 0.02):
        kw = dict(CENTRAL)
        kw.pop("n")
        kw["f"] = f
        n = n_for_power(rng, **kw)
        out["n_for_80"][str(f)] = n
        print(f"n para potencia 0.80 con f={f}: {n if n else '>24'}")

    json.dump(out, open("potencia/resultados.json", "w"), indent=2)
    print("\nescrito potencia/resultados.json")


if __name__ == "__main__":
    main()
