#!/usr/bin/env python3
"""Elige el tamaño de ventana W del estadístico Psi MAXIMIZANDO LA POTENCIA EN DATOS PÚBLICOS,
antes de calcular nada del probando. En el probando no conocemos las posiciones de los switches,
así que Psi se calcula sobre ventanas fijas de W sitios; un switch dentro de una ventana atenúa
phi_s en vez de anularlo. Se simula ese proceso con la tasa MEDIDA (0.810%/sitio)."""
import numpy as np, torch, json, os
REP = os.path.dirname(os.path.abspath(__file__))
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
FPR, NC = 0.05, 22; ALFA = 1-(1-FPR)**(1/NC)
TASA = json.load(open(f"{REP}/switch_chr15.json"))["tasa_switch"]
N, INV = 148048, 0.02359
delta = lambda f: f/(2*(2+f))

def simula(W, f, kappa, n_rep, semilla):
    """Ventanas fijas de W sitios. Dentro de cada ventana el signo cambia con tasa TASA.
    Se procesa por trozos: n_rep*N elementos no caben en 8 GB de VRAM."""
    g = torch.Generator(device=dev); g.manual_seed(semilla)
    S = N // W
    trozo = max(1, int(6e7 // N))
    salida = torch.empty(n_rep, device=dev); hecho = 0
    while hecho < n_rep:
        b_ = min(trozo, n_rep - hecho)
        salida[hecho:hecho+b_] = _un_trozo(W, f, kappa, b_, S, g)
        hecho += b_
    return salida

def _un_trozo(W, f, kappa, n_rep, S, g):
    # orientación por sitio: camino aleatorio de switches -> media de signo por ventana
    flips = (torch.rand(n_rep, S, W, generator=g, device=dev) < TASA).cumsum(dim=2)
    signo = torch.where(flips % 2 == 0, 1.0, -1.0)          # +-1 por sitio dentro de la ventana
    o0 = torch.where(torch.rand(n_rep, S, 1, generator=g, device=dev) < .5, -1., 1.)
    signo = signo * o0                     # flip_i: fase de Beagle / fase verdadera, +-1
    D = delta(f)
    ruido = np.sqrt(kappa*0.25*INV)        # sd de (b_i - 0.5) por sitio
    # Firmando por la fase de BEAGLE: s_beagle*(b-0.5) = flip_i*D + ruido.
    # La atenuacion viene de promediar flip_i dentro de la ventana; no se cancela.
    phi = D*signo.mean(dim=2) + (ruido/np.sqrt(W))*torch.randn(n_rep, S, generator=g, device=dev)
    v = kappa*0.25*INV/W
    w = 1.0/S
    return ((phi**2 - v)*w).sum(dim=1)

if __name__ == "__main__":
    print(f"dispositivo: {dev} | tasa de switch medida: {TASA*100:.3f}%/sitio | N={N}")
    print(f"\n{'W':>5} {'segmentos':>10} {'LOD kappa=1':>13} {'LOD kappa=2':>13} {'LOD kappa=4':>13}")
    mejor = None; filas=[]
    for W in (20, 50, 100, 125, 150, 200, 300, 500):
        fila = {"W": W, "S": N//W}
        txt = f"{W:5d} {N//W:10d}"
        for kap in (1.0, 2.0, 4.0):
            nulo = simula(W, 0.0, kap, 40000, 101+W)
            umbral = torch.quantile(nulo.float(), 1-ALFA).item()
            lo, hi = 1e-4, 0.30
            for _ in range(16):
                m = (lo+hi)/2
                pot = (simula(W, m, kap, 8000, 202+W) > umbral).float().mean().item()
                if pot >= 0.80: hi = m
                else: lo = m
            fila[f"lod_k{int(kap)}"] = hi; fila[f"umbral_k{int(kap)}"] = umbral
            txt += f" {hi*100:12.2f}%"
            if kap == 2.0 and (mejor is None or hi < mejor[1]): mejor = (W, hi)
        print(txt); filas.append(fila)
        torch.cuda.empty_cache() if dev.type=='cuda' else None
    print(f"\n  VENTANA ELEGIDA (mejor LOD a kappa=2, el caso central): W = {mejor[0]} sitios, LOD {mejor[1]*100:.2f}%")
    json.dump({"tasa_switch": TASA, "N": N, "W_elegida": mejor[0], "filas": filas},
              open(f"{REP}/ventana.json","w"), indent=1)
