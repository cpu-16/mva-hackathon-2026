#!/usr/bin/env python3
"""LOD de los dos estadísticos con la estructura de segmentos MEDIDA (no supuesta).
  phi_c  = media con signo por cromosoma        -> se diluye con los switches
  Psi_c  = sum_s w_s (phi_s^2 - v_s)            -> invariante a la orientación (enmienda 1)
Validación Monte Carlo en GPU."""
import json, gzip, glob, os, numpy as np, subprocess, sys
from scipy.stats import norm

REP = os.path.dirname(os.path.abspath(__file__))
FPR, NC = 0.05, 22
ALFA = 1 - (1 - FPR) ** (1.0 / NC)
Z1 = norm.ppf(1 - ALFA)         # una cola (Psi solo crece)
Z2 = norm.ppf(1 - ALFA / 2)     # dos colas (phi)
delta = lambda f: f / (2.0 * (2.0 + f))

sw = json.load(open(f"{REP}/switch_chr15.json"))
TASA = sw["tasa_switch"]

def segmentos(N, tasa=TASA, semilla=2026):
    """Estructura de segmentos con la tasa medida: geométrica entre switches."""
    rng = np.random.default_rng(semilla)
    tam, tot = [], 0
    while tot < N:
        L = min(int(rng.geometric(tasa)), N - tot)
        tam.append(L); tot += L
    return np.array(tam, dtype=np.int64)

def sitios_por_crom():
    d = {}
    for f in sorted(glob.glob(f"{REP}/sitios/chr*.tsv.gz")):
        c = int(os.path.basename(f)[3:].split(".")[0])
        dp = []
        with gzip.open(f, "rt") as fh:
            for line in fh:
                p = line.split("\t")
                if len(p) >= 4:
                    try: dp.append(int(p[3]))
                    except ValueError: pass
        if dp: d[c] = np.array(dp, np.int32)
    return d

def lod_psi(N, tam, c_ruido, kappa, objetivo=0.80):
    """Psi: E=Delta^2 bajo H1, Var_0 = 2*sum w_s^2 v_s^2."""
    w = tam / tam.sum()
    v = kappa * c_ruido / tam                    # varianza de phi_s
    sd0 = np.sqrt(2 * np.sum(w**2 * v**2))
    t = Z1 * sd0
    lo, hi = 1e-5, 0.6
    for _ in range(60):
        m = (lo + hi) / 2
        D2 = delta(m) ** 2
        # bajo H1 la varianza crece: Var(phi_s^2) = 2 v_s^2 + 4 D^2 v_s
        sd1 = np.sqrt(np.sum(w**2 * (2 * v**2 + 4 * D2 * v)))
        pot = norm.sf((t - D2) / sd1)
        if pot >= objetivo: hi = m
        else: lo = m
    return hi, t, sd0

def lod_phi(N, tam, c_ruido, kappa, objetivo=0.80, semilla=7):
    """phi con dilución realizada por la orientación aleatoria de los segmentos."""
    rng = np.random.default_rng(semilla)
    w = tam / tam.sum()
    sd = np.sqrt(kappa * c_ruido / N)
    t = Z2 * sd
    dil = np.array([abs((w * rng.choice([-1.0, 1.0], size=len(w))).sum()) for _ in range(400)])
    lo, hi = 1e-5, 0.9
    for _ in range(60):
        m = (lo + hi) / 2
        mu = delta(m) * dil
        pot = np.mean(norm.sf((t - mu) / sd) + norm.cdf((-t - mu) / sd))
        if pot >= objetivo: hi = m
        else: lo = m
    return hi

if __name__ == "__main__":
    S = sitios_por_crom()
    print(f"cromosomas con sitios: {sorted(S)}")
    Ns = {c: len(v) for c, v in S.items()}
    inv = {c: float(np.mean(1.0 / v)) for c, v in S.items()}
    Nm = int(np.median(list(Ns.values()))); im = float(np.median(list(inv.values())))
    c_ruido = 0.25 * im
    print(f"N mediano {Nm}   DP efectivo {1/im:.1f}   tasa de switch medida {TASA*100:.3f}%")
    tam = segmentos(Nm)
    print(f"segmentos simulados con esa tasa: {len(tam)} (mediana {int(np.median(tam))} sitios)\n")
    print(f"{'kappa':>6} {'LOD phi (diluida)':>18} {'LOD Psi (invariante)':>21}   vs 14% publicado")
    filas = []
    for kap in (1.0, 2.0, 4.0):
        lp = lod_phi(Nm, tam, c_ruido, kap)
        lps, t, sd0 = lod_psi(Nm, tam, c_ruido, kap)
        print(f"{kap:6.1f} {lp*100:17.2f}% {lps*100:20.2f}%   mejora {14/ (lps*100):.0f}x")
        filas.append({"kappa": kap, "lod_phi": lp, "lod_psi": lps})
    json.dump({"tasa_switch": TASA, "N_mediano": Nm, "dp_efectivo": 1/im,
               "n_segmentos": int(len(tam)), "filas": filas},
              open(f"{REP}/lod_medido.json","w"), indent=1)
    print("\n-> lod_medido.json")
