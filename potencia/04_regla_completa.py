#!/usr/bin/env python3
"""Operating characteristics of the COMPLETE §6 advancement rule (PREREGISTRO_REGLA_COMPLETA.md,
commit 646a364, before this script existed). Batched Levenberg–Marquardt four-parameter Hill fit on
the GPU (PyTorch/CUDA), with a CPU acceptance test against scipy.curve_fit before any scenario runs.
Model, rule, scenarios, seeds and predictions are the pre-registered ones; nothing is chosen after a number.
"""
import json, time, sys, numpy as np, torch
from scipy import stats
from scipy.optimize import curve_fit

CONC = np.array([0.0, 5.0, 10.0, 25.0, 50.0, 75.0, 100.0, 200.0, 400.0, 700.0, 1000.0])
NSIM, SEED, ALPHA = 4000, 20261005, 0.05
E_ANEU, M_SLOPE = 40.0, 1.0
CV_DONOR, CV_PASS, CV_BIO, CV_PLATE, CV_WELL = 0.15, 0.10, 0.20, 0.05, 0.10
LAM0, CV_MN, MN_CONC_IDX = 20.0, 0.25, 6            # vehicle micronuclei per 1,000; 100 nM is index 6
RHO = {0.10: 1.14, 0.20: 1.30, 0.30: 1.50, 0.50: 2.00}
EXPOSURE_NM = 312.0
LB = np.array([0.0, 0.5, 0.0, 0.2]); UB = np.array([0.5, 1.5, 4.0, 6.0]); P0 = np.array([0.0, 1.0, np.log10(80.0), 1.0])
CENTRAL = dict(f=0.30, r=4.0, n=12, delta=0.0)
SWEEPS = dict(n=[3, 6, 12, 23], f=[0.10, 0.20, 0.30, 0.50], r=[1.0, 2.0, 4.0], delta=[0.0, 0.25, 0.5, 1.0])
GRID = [(n, r) for n in (3, 6, 12, 23) for r in (1.0, 2.0, 4.0)]
DEV = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------- truth and simulation (numpy, per-scenario random stream) ----------
def hill(c, e, m):
    c, e = np.broadcast_arrays(np.asarray(c, dtype=float), np.asarray(e, dtype=float))
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.divide(c, e, out=np.zeros_like(c), where=(c > 0))
        out = 1.0 / (1.0 + np.power(ratio, m))
    return np.where(c > 0, out, 1.0)

def truth(c, f, e, r, m):
    return (1.0 - f) * hill(c, e * r, m) + f * hill(c, e, m)

def simulate_experiments(rng, f, r, n, delta, nsim):
    """Returns curves [nsim, 3, n, 11] (arm 0 = patient, 1 = donor A, 2 = donor B) and
    micronucleus counts veh/trt [nsim, 3, n]. Passages of 3 cultures share a multiplier."""
    npass = int(np.ceil(n / 3)); pas_idx = np.repeat(np.arange(npass), 3)[:n]
    donor = np.exp(rng.normal(0.0, CV_DONOR, (nsim, 3, 1)))
    passage = np.exp(rng.normal(0.0, CV_PASS, (nsim, 3, npass)))[:, :, pas_idx]
    bio = np.exp(rng.normal(0.0, CV_BIO, (nsim, 3, n)))
    e_cult = E_ANEU * donor * passage * bio                                   # [nsim,3,n]
    fr = np.array([f, 0.0, 0.0])[None, :, None, None]
    y = truth(CONC[None, None, None, :], fr, e_cult[..., None], r, M_SLOPE)
    plate = np.exp(rng.normal(0.0, CV_PLATE, (nsim, 3, n, 1)))
    well = np.exp(rng.normal(0.0, CV_WELL, y.shape))
    curves = y * plate * well
    # micronuclei: gamma culture multiplier (mean 1, CV 0.25) × passage correlation, shared veh/trt
    g = rng.gamma(1 / CV_MN**2, CV_MN**2, (nsim, 3, n)) * passage
    veh = rng.poisson(LAM0 * g); trt = rng.poisson(LAM0 * (1.0 + delta) * g)
    return curves, veh, trt

# ---------- batched Levenberg–Marquardt on the GPU ----------
LN10 = float(np.log(10.0))
def lm_fit(curves_np, iters=80):
    """curves_np [N, 11] -> log10 EC50 [N] with nan on a pre-registered failure."""
    y = torch.as_tensor(curves_np, dtype=torch.float64, device=DEV)
    N = y.shape[0]
    c = torch.as_tensor(CONC, dtype=torch.float64, device=DEV)[None, :].expand(N, -1)
    pos = c > 0; logc = torch.where(pos, torch.log(torch.clamp(c, min=1e-12)), torch.zeros_like(c))
    lb = torch.as_tensor(LB, dtype=torch.float64, device=DEV); ub = torch.as_tensor(UB, dtype=torch.float64, device=DEV)
    p = torch.as_tensor(P0, dtype=torch.float64, device=DEV)[None, :].repeat(N, 1)
    lam = torch.full((N,), 1e-2, dtype=torch.float64, device=DEV)
    def model_jac(p):
        b, t, le, m = p[:, 0:1], p[:, 1:2], p[:, 2:3], p[:, 3:4]
        lne = le * LN10
        u = torch.where(pos, torch.exp(m * (logc - lne)), torch.zeros_like(c))   # (c/e)^m
        h = 1.0 / (1.0 + u)
        yhat = b + (t - b) * h
        dh_dle = h * h * u * m * LN10
        dh_dm = -h * h * u * torch.where(pos, logc - lne, torch.zeros_like(c))
        J = torch.stack([1.0 - h, h, (t - b) * dh_dle, (t - b) * dh_dm], dim=2)     # [N,11,4]
        return yhat, J
    yhat, J = model_jac(p); res = y - yhat; cost = (res * res).sum(1)
    eye = torch.eye(4, dtype=torch.float64, device=DEV)[None]
    for _ in range(iters):
        JTJ = J.transpose(1, 2) @ J; JTr = (J.transpose(1, 2) @ res[:, :, None])[:, :, 0]
        A = JTJ + lam[:, None, None] * (torch.diagonal(JTJ, dim1=1, dim2=2)[:, :, None] * eye + 1e-12 * eye)
        step = torch.linalg.solve(A, JTr[:, :, None])[:, :, 0]
        p_new = torch.maximum(torch.minimum(p + step, ub), lb)
        yhat_new, J_new = model_jac(p_new); res_new = y - yhat_new; cost_new = (res_new * res_new).sum(1)
        better = cost_new < cost
        p = torch.where(better[:, None], p_new, p); res = torch.where(better[:, None], res_new, res)
        J = torch.where(better[:, None, None], J_new, J); cost = torch.where(better, cost_new, cost)
        lam = torch.where(better, lam / 3.0, lam * 2.0).clamp(1e-7, 1e7)
    b, t, le = p[:, 0], p[:, 1], p[:, 2]
    fail = (~torch.isfinite(cost)) | (le <= LB[2] + 1e-3) | (le >= UB[2] - 1e-3) | (t < b + 0.2)
    out = torch.where(fail, torch.full_like(le, float("nan")), le)
    return out.cpu().numpy()

def model4(x, b, t, log_e, mm): return b + (t - b) * hill(x, 10.0 ** log_e, mm)
def fit4_cpu(y):
    try: p, _ = curve_fit(model4, CONC, y, p0=P0, bounds=(LB, UB), maxfev=20000)
    except Exception: return np.nan
    b, t, log_e, mm = p
    if log_e <= LB[2] + 1e-6 or log_e >= UB[2] - 1e-6 or t < b + 0.2: return np.nan
    return log_e

def acceptance_test():
    rng = np.random.default_rng(SEED - 1)
    curves, _, _ = simulate_experiments(rng, 0.30, 4.0, 3, 0.0, 56)      # 56×3×3 = 504 curves
    flat = curves.reshape(-1, CONC.size)[:500]
    g = lm_fit(flat); s = np.array([fit4_cpu(y) for y in flat])
    both = np.isfinite(g) & np.isfinite(s)
    agree = np.mean(np.abs(g[both] - s[both]) <= 0.02) if both.any() else 0.0
    flags = np.mean(np.isfinite(g) == np.isfinite(s))
    ok = (agree >= 0.98) and (flags >= 0.95)
    return dict(n_curves=int(flat.shape[0]), within_0p02=float(agree), same_failure_flag=float(flags),
                gpu_failures=int((~np.isfinite(g)).sum()), cpu_failures=int((~np.isfinite(s)).sum()),
                max_abs_diff=float(np.nanmax(np.abs(g[both] - s[both]))) if both.any() else None, passed=bool(ok))

# ---------- the rule ----------
def welch(a, b):
    """mean(a)-mean(b), SE, df (Welch) for equal n columns."""
    n = a.shape[-1]; va = a.var(-1, ddof=1); vb = b.var(-1, ddof=1)
    se = np.sqrt(va / n + vb / n)
    df = (va / n + vb / n) ** 2 / ((va / n) ** 2 / (n - 1) + (vb / n) ** 2 / (n - 1) + 1e-300)
    return a.mean(-1) - b.mean(-1), se, df

def classify(le, veh, trt, f):
    """le [nsim,3,n] log10 EC50 (nan = failed). Returns outcome labels per experiment."""
    nsim = le.shape[0]; rho = np.log10(RHO[f]); two_rho = np.log10(2.0 * RHO[f])
    missing = np.isnan(le).any(axis=(1, 2))
    le0 = np.where(np.isnan(le), 0.0, le)
    # response, per donor j = 1,2: log ratio donor - patient
    met = np.ones(nsim, bool); insuff = np.zeros(nsim, bool); tox = np.ones(nsim, bool)
    for j in (1, 2):
        d, se, df = welch(le0[:, j, :], le0[:, 0, :])
        tq = stats.t.ppf(1 - ALPHA / 2, df); lo, hi = d - tq * se, d + tq * se
        met &= (lo > 0) & ~(hi < rho)
        insuff |= (hi < rho)
        tox &= (d > two_rho)
    exposure = (10.0 ** le0[:, 0, :].mean(-1)) <= EXPOSURE_NM
    # micronuclei: Δ - M = T - 1.5 V, delta method with Welch df, pooled over the three lines? No: per the
    # PDF, "treated versus vehicle cultures of the same line" — the patient line is the one that decides.
    T = trt[:, 0, :].astype(float); V = veh[:, 0, :].astype(float); n = T.shape[-1]
    vT = T.var(-1, ddof=1); vV = V.var(-1, ddof=1)
    est = T.mean(-1) - 1.5 * V.mean(-1); se = np.sqrt(vT / n + 2.25 * vV / n)
    df = (vT / n + 2.25 * vV / n) ** 2 / ((vT / n) ** 2 / (n - 1) + (2.25 * vV / n) ** 2 / (n - 1) + 1e-300)
    tq = stats.t.ppf(1 - ALPHA / 2, df); mn_lo, mn_hi = est - tq * se, est + tq * se
    harm = mn_lo > 0; below = mn_hi < 0
    out = np.full(nsim, "inconclusive", dtype=object)
    out[met & exposure & below & ~missing] = "advance"
    out[insuff & ~missing] = "insufficient"          # precedence below advance? No: insufficient and advance are exclusive (met requires not wholly below)
    out[tox & ~missing] = "toxicity_stop"
    out[harm] = "harm"
    labels = ["harm", "toxicity_stop", "advance", "insufficient", "inconclusive"]
    freq = {k: float(np.mean(out == k)) for k in labels}
    freq["missing_ec50_rate"] = float(missing.mean()); freq["exposure_met_rate"] = float(exposure.mean())
    freq["mn_below_margin_rate"] = float(below.mean()); freq["response_met_rate"] = float((met & ~missing).mean())
    return freq

def run_scenario(label, f, r, n, delta, off):
    rng = np.random.default_rng(SEED + off)
    curves, veh, trt = simulate_experiments(rng, f, r, n, delta, NSIM)
    le = lm_fit(curves.reshape(-1, CONC.size)).reshape(NSIM, 3, n)
    return label, dict(f=f, r=r, n=n, delta=delta, **classify(le, veh, trt, f))

def main():
    t0 = time.time()
    acc = acceptance_test(); print("acceptance test:", acc)
    if not acc["passed"]:
        print("GPU fitter FAILED the acceptance test; per the pre-registration this run stops here and an amendment records the fallback."); 
        json.dump({"acceptance_test": acc, "device": str(DEV)}, open("resultados_regla_completa.json", "w"), indent=1); sys.exit(2)
    tasks = [("central", CENTRAL["f"], CENTRAL["r"], CENTRAL["n"], CENTRAL["delta"])]
    for key, vals in SWEEPS.items():
        for v in vals:
            kw = dict(CENTRAL); kw[key] = v
            tasks.append((f"sweep:{key}={v}", kw["f"], kw["r"], kw["n"], kw["delta"]))
    for n, r in GRID: tasks.append((f"grid:n={n}:r={r}", 0.30, r, n, 0.0))
    res = {}
    for off, (label, f, r, n, d) in enumerate(tasks):
        if label in res: continue
        lab, out = run_scenario(label, f, r, n, d, off); res[lab] = out
        print(f"{lab:<24} f={f} r={r} n={n:>2} δ={d}  advance {out['advance']:.3f}  insufficient {out['insufficient']:.3f}  inconclusive {out['inconclusive']:.3f}  harm {out['harm']:.3f}  tox {out['toxicity_stop']:.3f}  missing {out['missing_ec50_rate']:.3f}", flush=True)
    c = res["central"]; grid = {k: v for k, v in res.items() if k.startswith("grid:")}
    null = {k: v for k, v in grid.items() if v["r"] == 1.0}
    f010 = res["sweep:f=0.1"]; d05 = res["sweep:delta=0.5"]
    adv_r4 = {v["n"]: v["advance"] for v in grid.values() if v["r"] == 4.0}
    pred = {
        "P-R1_central_advance_below_0.80_and_0.60": bool(c["advance"] < 0.60),
        "P-R1_central_advance": c["advance"],
        "P-R2_null_false_advance_le_0.05_all_n": bool(all(v["advance"] <= 0.05 for v in null.values())),
        "P-R2_null_dominant_not_harm": bool(all(max(v, key=lambda k: v[k] if k in ("harm","toxicity_stop","advance","insufficient","inconclusive") else -1) != "harm" for v in null.values())),
        "P-R3_delta0.5_advance_below_0.20": bool(d05["advance"] < 0.20),
        "P-R3_delta0.5_inconclusive_dominant": bool(d05["inconclusive"] >= max(d05["advance"], d05["harm"], d05["insufficient"], d05["toxicity_stop"])),
        "P-R4_no_n_reaches_0.80_advance": bool(all(a < 0.80 for a in adv_r4.values())),
        "P-R5_f0.10_insufficient_exceeds_advance": bool(f010["insufficient"] > f010["advance"]),
    }
    out = dict(device=str(DEV), gpu=torch.cuda.get_device_name(0) if DEV.type == "cuda" else None, acceptance_test=acc,
               nsim=NSIM, seed=SEED, central=CENTRAL, variance=dict(cv_donor=CV_DONOR, cv_pass=CV_PASS, cv_bio=CV_BIO, cv_plate=CV_PLATE, cv_well=CV_WELL),
               micronuclei=dict(lambda0_per_1000=LAM0, cv_culture=CV_MN, margin="0.5 x vehicle mean", concentration_nM=float(CONC[MN_CONC_IDX])),
               results=res, predictions=pred, runtime_s=round(time.time() - t0, 1))
    print(pred, f"runtime {out['runtime_s']} s")
    json.dump(out, open("resultados_regla_completa.json", "w"), indent=1)

if __name__ == "__main__":
    main()
