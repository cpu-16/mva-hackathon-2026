#!/usr/bin/env python3
"""EXPLORATORY, post-hoc, 2026-10-05 after an adversarial read of RESULTADOS_REGLA_COMPLETA.md.
Not pre-registered. Four targeted checks of the primary run's diagnoses, same model and seed family:
 (A) the micronucleus interval with a PAIRED contrast per culture (D_i = T_i - 1.5 V_i), since veh/trt
     share the culture multiplier (the primary used the independent-sample delta method);
 (B) the null (r = 1) with CV_donor = 0 — does the false-advance inflation come from the donor effect?
 (C) f = 0.10 at n in {3, 6, 23} — P-R5's "for every n" clause, untested by the primary design;
 (D) the effective true ratio under the fitted-EC50 estimand at the central scenario (mean log10 EC50
     of donor cultures minus patient cultures, large n), to replace the wrong "exactly 1.50" claim.
"""
import json, time, importlib.util, numpy as np
spec = importlib.util.spec_from_file_location("m", __file__.replace("05_regla_exploratorio.py", "04_regla_completa.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
from scipy import stats

def classify_paired(le, veh, trt, f):
    """Same rule as m.classify but the micronucleus interval is on per-culture D_i = T_i - 1.5 V_i."""
    nsim = le.shape[0]; rho = np.log10(m.RHO[f]); two_rho = np.log10(2.0 * m.RHO[f])
    missing = np.isnan(le).any(axis=(1, 2)); le0 = np.where(np.isnan(le), 0.0, le)
    met = np.ones(nsim, bool); insuff = np.zeros(nsim, bool); tox = np.ones(nsim, bool)
    for j in (1, 2):
        d, se, df = m.welch(le0[:, j, :], le0[:, 0, :]); tq = stats.t.ppf(1 - m.ALPHA / 2, df)
        lo, hi = d - tq * se, d + tq * se
        met &= (lo > 0) & ~(hi < rho); insuff |= (hi < rho); tox &= (d > two_rho)
    exposure = (10.0 ** le0[:, 0, :].mean(-1)) <= m.EXPOSURE_NM
    D = trt[:, 0, :].astype(float) - 1.5 * veh[:, 0, :].astype(float); n = D.shape[-1]
    est = D.mean(-1); se = D.std(-1, ddof=1) / np.sqrt(n); tq = stats.t.ppf(1 - m.ALPHA / 2, n - 1)
    harm = est - tq * se > 0; below = est + tq * se < 0
    out = np.full(nsim, "inconclusive", dtype=object)
    out[met & exposure & below & ~missing] = "advance"; out[insuff & ~missing] = "insufficient"
    out[tox & ~missing] = "toxicity_stop"; out[harm] = "harm"
    labels = ["harm", "toxicity_stop", "advance", "insufficient", "inconclusive"]
    fr = {k: float(np.mean(out == k)) for k in labels}; fr["mn_below_margin_rate"] = float(below.mean()); return fr

def run(label, f, r, n, delta, off, cv_donor=m.CV_DONOR, paired=False):
    old = m.CV_DONOR; m.CV_DONOR = cv_donor
    rng = np.random.default_rng(m.SEED + 1000 + off)
    curves, veh, trt = m.simulate_experiments(rng, f, r, n, delta, m.NSIM)
    m.CV_DONOR = old
    le = m.lm_fit(curves.reshape(-1, m.CONC.size)).reshape(m.NSIM, 3, n)
    fr = classify_paired(le, veh, trt, f) if paired else m.classify(le, veh, trt, f)
    fr.update(f=f, r=r, n=n, delta=delta, cv_donor=cv_donor, paired=paired)
    print(f"{label:<34} advance {fr['advance']:.3f} insufficient {fr['insufficient']:.3f} inconclusive {fr['inconclusive']:.3f} harm {fr['harm']:.3f} tox {fr['toxicity_stop']:.3f}", flush=True)
    return label, fr, le

t0 = time.time(); res = {}; off = 0
for n, r in [(n, r) for n in (3, 6, 12, 23) for r in (1.0, 4.0)]:          # (A) paired MN interval
    lab, fr, _ = run(f"A:paired:n={n}:r={r}", 0.30, r, n, 0.0, off, paired=True); res[lab] = fr; off += 1
for n in (3, 6, 12, 23):                                                       # (B) null without donor effect
    lab, fr, _ = run(f"B:null_no_donor:n={n}", 0.30, 1.0, n, 0.0, off, cv_donor=0.0); res[lab] = fr; off += 1
for n in (3, 6, 23):                                                           # (C) f = 0.10 across n
    lab, fr, _ = run(f"C:f=0.10:n={n}", 0.10, 4.0, n, 0.0, off); res[lab] = fr; off += 1
lab, fr, le = run("D:central:n=23", 0.30, 4.0, 23, 0.0, off); res[lab] = fr   # (D) effective true ratio
d = np.nanmean(le[:, 1:, :], axis=(1, 2)) - np.nanmean(le[:, 0, :], axis=1)   # per experiment, donors minus patient
res["D:effective_log10_ratio"] = dict(mean=float(np.nanmean(d)), sd_across_experiments=float(np.nanstd(d)),
                                      ratio=float(10 ** np.nanmean(d)), table_row=m.RHO[0.30],
                                      share_of_experiments_with_point_estimate_below_row=float(np.mean(d < np.log10(m.RHO[0.30]))))
# noiseless half-viability ratio of the mixture, for the record
from scipy.optimize import brentq
f, E, r = 0.30, 40.0, 4.0
half = brentq(lambda c: m.truth(np.array([c]), f, E, r, 1.0)[0] - 0.5, 1e-3, 1e5)
res["D:noiseless_half_viability_ratio"] = dict(patient_half_nM=float(half), control_half_nM=float(E * r), ratio=float(E * r / half))
print("D:", res["D:effective_log10_ratio"], res["D:noiseless_half_viability_ratio"])
res["runtime_s"] = round(time.time() - t0, 1); print("runtime", res["runtime_s"])
json.dump(res, open("resultados_regla_exploratorio.json", "w"), indent=1)
