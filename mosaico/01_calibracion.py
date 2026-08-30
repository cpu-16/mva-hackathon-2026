#!/usr/bin/env python3
"""Calibración del estadístico BAF con signo de haplotipo. SOLO datos públicos + la
distribución de DP declarada en el pre-registro. Se corre ANTES del estadístico del probando.

phi_c = (1/N) * sum_i s_i * (b_i - 0.5),  b_i = AD_alt/DP_i,  s_i = +-1 por haplotipo.
Ganancia mosaica de un homólogo en fracción f:  p = (1+f)/(2+f) si el ALT está en el
haplotipo ganado, 1/(2+f) si no.  Delta = f / (2*(2+f)).
"""
import numpy as np, json, sys, os, gzip, glob
from scipy.stats import norm

REP = os.path.dirname(os.path.abspath(__file__))
F_GRID   = [0.005, 0.01, 0.02, 0.05, 0.10, 0.20]   # fracción celular, pre-registrada
EPS_GRID = [0.0, 0.01, 0.02, 0.05]                  # error de switch de fase
KAP_GRID = [1.0, 2.0, 4.0]                          # sobredispersión del BAF
FPR_GENOMA = 0.05                                   # falso positivo genome-wide
N_CROM = 22
N_REP = 200                                         # réplicas por celda, pre-registrado

def umbral_z():
    alfa = 1 - (1 - FPR_GENOMA) ** (1.0 / N_CROM)    # por cromosoma
    return norm.ppf(1 - alfa / 2)                    # dos colas

def delta(f):
    return f / (2.0 * (2.0 + f))

def potencia_analitica(f, eps, kappa, N, inv_dp_medio):
    """z-test: phi ~ Normal(mu, sigma^2)."""
    mu = (1 - 2 * eps) * delta(f)
    var = kappa * 0.25 * inv_dp_medio / N
    sd = np.sqrt(var)
    t = umbral_z() * sd
    return norm.cdf((mu - t) / sd) + norm.cdf((-mu - t) / sd), mu, sd

def lod(eps, kappa, N, inv_dp_medio, objetivo=0.80):
    """f más pequeña con potencia >= objetivo (búsqueda fina, no solo la rejilla)."""
    lo, hi = 1e-5, 0.5
    if potencia_analitica(hi, eps, kappa, N, inv_dp_medio)[0] < objetivo: return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if potencia_analitica(mid, eps, kappa, N, inv_dp_medio)[0] >= objetivo: hi = mid
        else: lo = mid
    return hi

# ---------- validación Monte Carlo en GPU ----------
def montecarlo_gpu(f, eps, kappa, dps, n_rep=N_REP, semilla=2026):
    """Simula phi replicando el muestreo binomial sitio a sitio. dps = vector de DP reales."""
    import torch
    dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    g = torch.Generator(device=dev); g.manual_seed(semilla)
    DP = torch.as_tensor(dps, dtype=torch.float32, device=dev)
    N = DP.numel()
    p_gan = (1 + f) / (2 + f)
    out = torch.empty(n_rep, device=dev)
    # trozos para no reventar 8 GB de VRAM
    trozo = max(1, int(2e8 // max(N, 1)))
    hecho = 0
    while hecho < n_rep:
        b = min(trozo, n_rep - hecho)
        # el ALT cae en el haplotipo ganado con prob 1/2; el switch invierte el signo
        en_ganado = (torch.rand(b, N, generator=g, device=dev) < 0.5)
        switch    = (torch.rand(b, N, generator=g, device=dev) < eps)
        s = torch.where(en_ganado, 1.0, -1.0) * torch.where(switch, -1.0, 1.0)
        p = torch.where(en_ganado, p_gan, 1 - p_gan).to(torch.float32)
        if kappa > 1.0:   # beta-binomial: inflar la varianza manteniendo la media
            conc = (DP - kappa) / (kappa - 1.0)
            conc = torch.clamp(conc, min=1.0)
            a = p * conc; bb = (1 - p) * conc
            p_eff = torch._standard_gamma(a.expand(b, N).contiguous())
            q_eff = torch._standard_gamma(bb.expand(b, N).contiguous())
            p_use = p_eff / (p_eff + q_eff + 1e-12)
        else:
            p_use = p
        x = torch.binomial(DP.expand(b, N).contiguous(), p_use, generator=g)
        baf = x / DP
        out[hecho:hecho + b] = ((s * (baf - 0.5)).mean(dim=1))
        hecho += b
        del en_ganado, switch, s, p_use, x, baf
        torch.cuda.empty_cache() if dev.type == 'cuda' else None
    return out.cpu().numpy()

# ---------- P5: variegación balanceada ----------
def variegacion_balanceada_gpu(f, dps, n_rep=N_REP, semilla=2026):
    """Mezcla balanceada: g células ganan A, g ganan B, l pierden A, l pierden B, con g=l=f/4.
    Copias medias = 2 y BAF media = 0.5 por simetría. Debe salir INDETECTABLE a cualquier f."""
    import torch
    dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    g_ = torch.Generator(device=dev); g_.manual_seed(semilla + 7)
    DP = torch.as_tensor(dps, dtype=torch.float32, device=dev); N = DP.numel()
    gg = f / 4.0
    # copias de A y B promediadas sobre células:  A: 1 + gg - gg = 1 ; B igual -> p = 0.5 exacta
    cop_A = 1 + gg - gg
    cop_B = 1 + gg - gg
    p = cop_A / (cop_A + cop_B)
    out = torch.empty(n_rep, device=dev)
    trozo = max(1, int(2e8 // max(N, 1))); hecho = 0
    while hecho < n_rep:
        b = min(trozo, n_rep - hecho)
        en_A = (torch.rand(b, N, generator=g_, device=dev) < 0.5)
        s = torch.where(en_A, 1.0, -1.0)
        x = torch.binomial(DP.expand(b, N).contiguous(),
                           torch.full((b, N), float(p), device=dev), generator=g_)
        out[hecho:hecho + b] = ((s * (x / DP - 0.5)).mean(dim=1))
        hecho += b
    return out.cpu().numpy()

def cargar_sitios():
    """N y DP por cromosoma desde la lista retenida."""
    datos = {}
    for f in sorted(glob.glob(os.path.join(REP, "sitios", "chr*.tsv.gz"))):
        c = os.path.basename(f).replace("chr", "").replace(".tsv.gz", "")
        dp = []
        with gzip.open(f, "rt") as fh:
            for line in fh:
                p = line.rstrip("\n").split("\t")
                if len(p) >= 4:
                    try: dp.append(int(p[3]))
                    except ValueError: pass
        if dp: datos[int(c)] = np.array(dp, dtype=np.int32)
    return datos

if __name__ == "__main__":
    sitios = cargar_sitios()
    if not sitios:
        print("faltan las listas de sitios (00_sitios.sh)"); sys.exit(1)
    print(f"cromosomas con sitios: {sorted(sitios)}")
    Ns = {c: len(v) for c, v in sitios.items()}
    inv = {c: float(np.mean(1.0 / v)) for c, v in sitios.items()}
    N_med = int(np.median(list(Ns.values()))); inv_med = float(np.median(list(inv.values())))
    print(f"N mediano por cromosoma: {N_med}   E[1/DP] mediano: {inv_med:.5f}  (DP efectivo {1/inv_med:.1f})")
    print(f"umbral z (FPR genome-wide {FPR_GENOMA}, 22 cromosomas, dos colas): {umbral_z():.3f}\n")

    filas = []
    print(f"{'eps':>5} {'kappa':>6} {'LOD (f)':>9}   potencia en la rejilla de f")
    for eps in EPS_GRID:
        for kap in KAP_GRID:
            L = lod(eps, kap, N_med, inv_med)
            pots = [potencia_analitica(f, eps, kap, N_med, inv_med)[0] for f in F_GRID]
            print(f"{eps:5.2f} {kap:6.1f} {('%.4f'%L) if L else '   —':>9}   " +
                  " ".join(f"{f*100:g}%:{p:.2f}" for f, p in zip(F_GRID, pots)))
            filas.append({"eps": eps, "kappa": kap, "N": N_med, "LOD": L,
                          "potencia": dict(zip(map(str, F_GRID), pots))})
    with open(os.path.join(REP, "calibracion_analitica.json"), "w") as fh:
        json.dump({"umbral_z": umbral_z(), "N_mediano": N_med, "inv_dp": inv_med,
                   "N_por_cromosoma": Ns, "filas": filas}, fh, indent=1)
    print("\n-> calibracion_analitica.json")
