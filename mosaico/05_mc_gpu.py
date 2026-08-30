#!/usr/bin/env python3
"""Distribución nula EXACTA de Psi por Monte Carlo en GPU, con la estructura de segmentos
EMPÍRICA medida en chr15 (no una geométrica idealizada). Psi es una suma ponderada de
chi-cuadrados con pesos muy desiguales: la aproximación normal no es fiable en la cola."""
import json, gzip, glob, os, sys, numpy as np, subprocess
import torch

REP = os.path.dirname(os.path.abspath(__file__))
FPR, NC = 0.05, 22
ALFA = 1 - (1 - FPR) ** (1.0 / NC)
delta = lambda f: f / (2.0 * (2.0 + f))
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def segmentos_empiricos(N, semilla=2026):
    """Remuestrea tamaños de segmento de la distribución medida en chr15."""
    tam_obs = np.load(f"{REP}/segmentos_chr15.npy")
    rng = np.random.default_rng(semilla)
    out, tot = [], 0
    while tot < N:
        L = int(rng.choice(tam_obs))
        L = min(L, N - tot)
        if L > 0: out.append(L); tot += L
    return np.array(out, dtype=np.int64)

def mc_psi(tam, c_ruido, kappa, f, n_rep=200000, semilla=11):
    """Simula Psi = sum w_s (phi_s^2 - v_s). phi_s ~ N(o_s*Delta, v_s), o_s=+-1 aleatorio."""
    g = torch.Generator(device=dev); g.manual_seed(semilla)
    t = torch.as_tensor(tam, dtype=torch.float32, device=dev)
    w = t / t.sum()
    v = kappa * c_ruido / t
    D = delta(f)
    sd = torch.sqrt(v)
    S = t.numel()
    out = torch.empty(n_rep, device=dev)
    trozo = max(1, int(4e8 // S)); hecho = 0
    while hecho < n_rep:
        b = min(trozo, n_rep - hecho)
        o = torch.where(torch.rand(b, S, generator=g, device=dev) < 0.5, -1.0, 1.0)
        phi = o * D + sd * torch.randn(b, S, generator=g, device=dev)
        out[hecho:hecho+b] = ((phi**2 - v) * w).sum(dim=1)
        hecho += b
    return out

def lod_mc(tam, c_ruido, kappa, objetivo=0.80, n_rep=200000):
    nulo = mc_psi(tam, c_ruido, kappa, 0.0, n_rep)
    umbral = torch.quantile(nulo.float(), 1 - ALFA).item()
    lo, hi = 1e-4, 0.25
    for _ in range(18):
        m = (lo + hi) / 2
        alt = mc_psi(tam, c_ruido, kappa, m, n_rep // 4, semilla=23)
        pot = (alt > umbral).float().mean().item()
        if pot >= objetivo: hi = m
        else: lo = m
    return hi, umbral

if __name__ == "__main__":
    print(f"dispositivo: {dev} ({torch.cuda.get_device_name(0) if dev.type=='cuda' else 'CPU'})")
    S = {}
    for f in sorted(glob.glob(f"{REP}/sitios/chr*.tsv.gz")):
        c = int(os.path.basename(f)[3:].split(".")[0]); dp = []
        with gzip.open(f, "rt") as fh:
            for line in fh:
                p = line.split("\t")
                if len(p) >= 4:
                    try: dp.append(int(p[3]))
                    except ValueError: pass
        if dp: S[c] = np.array(dp, np.int32)
    Nm = int(np.median([len(v) for v in S.values()]))
    im = float(np.median([np.mean(1.0/v) for v in S.values()]))
    c_ruido = 0.25 * im
    tam = segmentos_empiricos(Nm)
    print(f"N mediano {Nm}  DP efectivo {1/im:.1f}")
    print(f"segmentos (remuestreo empírico): {len(tam)}  mediana {int(np.median(tam))}  máx {tam.max()}")
    print(f"umbral: cola superior alfa={ALFA:.5f} por cromosoma (FPR {FPR} sobre {NC})\n")
    print(f"{'kappa':>6} {'LOD Psi (Monte Carlo)':>23}   {'vs 14% publicado':>18}")
    filas = []
    for kap in (1.0, 2.0, 4.0):
        L, u = lod_mc(tam, c_ruido, kap)
        print(f"{kap:6.1f} {L*100:22.2f}%   {'mejora %.0fx' % (14/(L*100)):>18}")
        filas.append({"kappa": kap, "lod_psi_mc": L, "umbral": u})
        torch.cuda.empty_cache() if dev.type=='cuda' else None
    json.dump({"dispositivo": str(dev), "N": Nm, "dp_efectivo": 1/im,
               "n_segmentos": int(len(tam)), "alfa_por_cromosoma": ALFA, "filas": filas},
              open(f"{REP}/lod_montecarlo.json","w"), indent=1)
    print("\n-> lod_montecarlo.json")
