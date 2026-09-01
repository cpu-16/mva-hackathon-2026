#!/usr/bin/env python3
"""Compare the proband against the 1000G control envelope, per PREREGISTRO.md amendment 3.

WRITTEN BEFORE THE CONTROL DATA EXISTED. The two statistics, the depth handling, the window size
and the falsification rules all come from the amendment; nothing here was chosen after seeing a
control number.

Two unsigned statistics, both from the amendment:

    sigma2_extra = var(b - 0.5) - 0.25/DP          additive, comparable across depths
    kappa_window = var(W-site mean of (b-0.5)) / (0.25 / DP / W)

Depth is a confound with a known direction: a fixed mapping bias is a LARGER multiple of binomial
standard error at higher depth, so the proband (~44x) would look worse than the controls (~30x)
even if the physics were identical. The amendment handles it by binomially thinning the proband's
allele depths down to each control's depth and repeating the comparison.
"""
import glob, gzip, json, os, sys
import numpy as np

W = 125                      # window size, fixed on public data in amendment 2
SEED = 20260901
PROBAND = "mosaico/sitios/chr{c}.tsv.gz"
CONTROL = "mosaico/piloto/chr{c}.tsv.gz"
WINDOW = (5_000_000, 25_000_000)     # the pilot window, fixed in amendment 4
CHROMS = [8, 17]


def stats_from(dp, ad_alt, rng=None, thin_to=None):
    """The two pre-registered statistics for one sample on one chromosome.

    dp, ad_alt: per-site depth and alternate-allele count, already filtered.
    thin_to: if given, binomially thin each site to this depth before computing.
    """
    dp = np.asarray(dp, float)
    alt = np.asarray(ad_alt, float)
    if thin_to is not None:
        # thin to min(dp, thin_to) site by site; sites already shallower are left alone
        target = np.minimum(dp, thin_to)
        keep = target > 0
        p = np.divide(alt, dp, out=np.zeros_like(alt), where=dp > 0)
        alt = rng.binomial(target.astype(int), np.clip(p, 0, 1)).astype(float)
        dp = target
        dp, alt = dp[keep], alt[keep]
    b = np.divide(alt, dp, out=np.full_like(alt, 0.5), where=dp > 0)
    dev = b - 0.5
    mean_dp = float(np.mean(dp))

    sigma2_extra = float(np.var(dev, ddof=1) - 0.25 / mean_dp)

    n_win = len(dev) // W
    if n_win < 2:
        return dict(n_sites=len(dev), mean_dp=mean_dp, sigma2_extra=sigma2_extra,
                    kappa_window=float("nan"), n_windows=n_win)
    wm = dev[:n_win * W].reshape(n_win, W).mean(axis=1)
    expected = 0.25 / mean_dp / W
    kappa_window = float(np.var(wm, ddof=1) / expected)
    return dict(n_sites=len(dev), mean_dp=mean_dp, sigma2_extra=sigma2_extra,
                kappa_window=kappa_window, n_windows=n_win)


def load_proband(c):
    """mosaico/sitios/chrN.tsv.gz -> POS REF ALT DP AD, restricted to the pilot window."""
    dp, alt = [], []
    with gzip.open(PROBAND.format(c=c), "rt") as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            pos = int(f[0])
            if not (WINDOW[0] <= pos <= WINDOW[1]):
                continue
            try:
                d = int(f[3])
                ad = f[4].split(",")
                a = int(ad[1])
            except (IndexError, ValueError):
                continue
            if d > 0:
                dp.append(d); alt.append(a)
    return dp, alt


def panel_sites(c):
    """Positions in the 1000G panel with MAF >= 0.01, inside the pilot window.

    The proband site rule (00_sitios.sh) requires panel membership at MAF >= 0.01; applying it to
    the controls too is what makes the two comparable. Without it the controls carry ~30k het sites
    against the proband's ~20k, and they are not the same population of sites.
    """
    import subprocess
    reg = f"chr{c}:{WINDOW[0]}-{WINDOW[1]}"
    out = subprocess.run(
        ["bcftools", "view", "-H", "-r", reg, "-v", "snps", "-m2", "-M2",
         "-i", "AF>=0.01 && AF<=0.99", f"replay/raw/1kgp/chr{c}.vcf.gz"],
        capture_output=True, text=True).stdout
    return {int(l.split("\t", 2)[1]) for l in out.splitlines() if l}


def load_controls(c, keep=None):
    """mosaico/piloto/chrN.tsv.gz -> POS REF ALT then one 'GT,DP,AD' field per sample.

    Only heterozygous calls are kept, and only at positions in `keep`, so the site rule matches
    the proband's.
    """
    per_sample = None
    with gzip.open(CONTROL.format(c=c), "rt") as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 4:
                continue
            if keep is not None and int(f[0]) not in keep:
                continue
            fields = f[3:]
            if per_sample is None:
                per_sample = [([], []) for _ in fields]
            for i, g in enumerate(fields):
                parts = g.split(",")
                if len(parts) < 4:
                    continue
                gt, d, ref_c, alt_c = parts[0], parts[1], parts[2], parts[3]
                if gt not in ("0/1", "1/0", "0|1", "1|0"):
                    continue
                try:
                    d = int(d); a = int(alt_c)
                except ValueError:
                    continue
                if 20 <= d <= 80:                    # same depth rule as the proband
                    per_sample[i][0].append(d)
                    per_sample[i][1].append(a)
    return per_sample or []


def main():
    missing = [c for c in CHROMS if not os.path.exists(CONTROL.format(c=c))]
    if missing:
        sys.exit(f"todavía no está el control de chr{missing}; el piloto sigue corriendo")

    rng = np.random.default_rng(SEED)
    out = {"W": W, "window": WINDOW, "seed": SEED, "chroms": {}}

    for c in CHROMS:
        pdp, palt = load_proband(c)
        keep = panel_sites(c)
        ctrls = load_controls(c, keep=keep)
        prob_raw = stats_from(pdp, palt)
        rows = []
        for i, (dp, alt) in enumerate(ctrls):
            if len(dp) < W * 2:
                continue
            s = stats_from(dp, alt)
            # proband thinned to THIS control's mean depth
            th = stats_from(pdp, palt, rng=rng, thin_to=int(round(s["mean_dp"])))
            rows.append(dict(sample=i, control=s, proband_thinned=th))

        if not rows:
            out["chroms"][str(c)] = dict(error="ningún control con sitios suficientes")
            continue

        cs = np.array([r["control"]["sigma2_extra"] for r in rows])
        ck = np.array([r["control"]["kappa_window"] for r in rows])
        ts = np.array([r["proband_thinned"]["sigma2_extra"] for r in rows])
        tk = np.array([r["proband_thinned"]["kappa_window"] for r in rows])

        d = dict(
            n_controls=len(rows),
            panel_sites_in_window=len(keep),
            proband_raw=prob_raw,
            proband_thinned_mean=dict(sigma2_extra=float(ts.mean()), kappa_window=float(tk.mean())),
            control_sigma2=dict(min=float(cs.min()), max=float(cs.max()), mean=float(cs.mean())),
            control_kappa=dict(min=float(ck.min()), max=float(ck.max()), mean=float(ck.mean())),
            inside_sigma2=bool(cs.min() <= ts.mean() <= cs.max()),
            inside_kappa=bool(ck.min() <= tk.mean() <= ck.max()),
            per_sample=rows,
        )
        out["chroms"][str(c)] = d

        print(f"\n=== chr{c} ===  ({len(rows)} controles, ventana {WINDOW[0]:,}-{WINDOW[1]:,})")
        print(f"  probando crudo      DP {prob_raw['mean_dp']:.1f}  "
              f"sigma2_extra {prob_raw['sigma2_extra']:+.6f}  kappa_window {prob_raw['kappa_window']:.2f}")
        print(f"  probando adelgazado sigma2_extra {ts.mean():+.6f}  kappa_window {tk.mean():.2f}")
        print(f"  sobre de controles  sigma2_extra [{cs.min():+.6f}, {cs.max():+.6f}]  "
              f"kappa_window [{ck.min():.2f}, {ck.max():.2f}]")
        print(f"  DENTRO del sobre?   sigma2: {'SÍ' if d['inside_sigma2'] else 'NO'}   "
              f"kappa: {'SÍ' if d['inside_kappa'] else 'NO'}")

    # The pre-registered falsification rule, applied mechanically.
    both = [out["chroms"][str(c)] for c in CHROMS if "error" not in out["chroms"][str(c)]]
    if len(both) == len(CHROMS):
        inside_all = all(d["inside_sigma2"] and d["inside_kappa"] for d in both)
        c8, c17 = out["chroms"]["8"], out["chroms"]["17"]
        if inside_all:
            v = ("TÉCNICO. El probando cae dentro del sobre de los controles en ambos cromosomas y en "
                 "ambos estadísticos, tras adelgazar a la profundidad de cada control. El exceso de "
                 "2.27x es el modelo de ruido de las profundidades alélicas de GATK en SNPs comunes, "
                 "y el límite publicado se sostiene como límite de segundo orden.")
        elif not c17["inside_kappa"] and c8["inside_kappa"]:
            v = ("ESPECÍFICO DE CROMOSOMA. chr17 queda fuera y chr8 dentro — que es exactamente el "
                 "patrón que la enmienda 3 declaró como justificación para el trabajo a nivel de "
                 "lecturas. NO es evidencia de mosaicismo por sí solo.")
        else:
            v = ("NO CONCLUYENTE bajo las reglas pre-registradas. Se reporta como tal; no se amplía "
                 "la ventana ni se vuelve a mirar.")
        out["verdict"] = v
        print("\nVEREDICTO PRE-REGISTRADO:\n ", v)

    out["not_matched"] = (
        "GQ >= 30 forma parte de la regla de sitios del probando pero NO se pudo aplicar a los "
        "controles: la extracción del piloto pidió GT,DP,AD y no GQ, y re-extraer cuesta otras "
        "cuatro horas por cromosoma. Dirección del sesgo: sin filtro de GQ los controles retienen "
        "sitios de menor calidad, lo que INFLA su dispersión y por tanto ENSANCHA el sobre — es "
        "decir, hace más fácil que el probando caiga dentro. El resultado 'dentro del sobre' es por "
        "tanto el desenlace favorecido por este desajuste y debe leerse con esa reserva; un "
        "resultado 'fuera del sobre' no queda debilitado por él. Tampoco están pareados el caller "
        "(GATK singleton 4.2.4.0 contra el joint call de NYGC), la química de PCR ni el alineador."
    )
    json.dump(out, open("mosaico/control_resultado.json", "w"), indent=2)
    print("\nescrito mosaico/control_resultado.json")


if __name__ == "__main__":
    main()
