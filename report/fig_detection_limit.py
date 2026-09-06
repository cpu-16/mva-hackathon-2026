#!/usr/bin/env python3
"""Figura: limite de deteccion de mosaicismo en WGS bulk.

Direccion de arte: editorial cientifico sobrio. Fondo hueso, una tinta de acento
(verde-petroleo #1a9e8f, validada), grises calidos para lo secundario. Una sola
serie de datos -> sin caja de leyenda, etiquetas directas.
"""
import random
import statistics
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ACCENT = "#1a9e8f"      # tinta de datos (validada: lightness y chroma OK)
INK = "#2a2724"         # texto primario
MUTED = "#8a8378"       # texto secundario / ruido
SURFACE = "#fcfcfb"     # fondo hueso
NOISE_FILL = "#e8e4dd"

random.seed(11)


def mean_dev(f, dp=44, n=30000):
    """Desviacion media |BAF-0.5| con trisomia mosaico en fraccion f de celulas."""
    out = []
    for _ in range(n):
        p = 0.5 if f == 0 else random.choice([(1 + f) / (2 + f), 1 / (2 + f)])
        alt = sum(1 for _ in range(dp) if random.random() < p)
        out.append(abs(alt / dp - 0.5))
    return statistics.mean(out)


fracs = [0, 0.02, 0.05, 0.08, 0.10, 0.12, 0.14, 0.17, 0.20, 0.25, 0.30]
base = mean_dev(0)
effects = [(mean_dev(f) - base) for f in fracs]

NOISE = 0.005   # dispersion sistematica medida entre cromosomas (DP 40-48)

fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

# banda de ruido: lo que hay que superar para detectar algo
ax.add_patch(Rectangle((0, 0), 32, NOISE, facecolor=NOISE_FILL,
                       edgecolor="none", zorder=1))
ax.text(31.2, NOISE * 0.45, "systematic between-chromosome noise",
        ha="right", va="center", fontsize=8.5, color=MUTED, style="italic", zorder=4)

# donde cae la variegacion real
ax.axvspan(1, 2, color=ACCENT, alpha=0.10, zorder=1)

# la curva
xs = [f * 100 for f in fracs]
ax.plot(xs, effects, color=ACCENT, linewidth=2, zorder=3,
        marker="o", markersize=4.5, markerfacecolor=SURFACE,
        markeredgecolor=ACCENT, markeredgewidth=1.6)

# cruce: donde la curva sale del ruido
lod = None
for i in range(1, len(fracs)):
    if effects[i - 1] < NOISE <= effects[i]:
        t = (NOISE - effects[i - 1]) / (effects[i] - effects[i - 1])
        lod = (fracs[i - 1] + t * (fracs[i] - fracs[i - 1])) * 100
        break
if lod:
    ax.plot([lod], [NOISE], marker="o", markersize=8, color=ACCENT, zorder=5)
    ax.annotate(f"detection limit\n≈ {lod:.0f}% of cells",
                xy=(lod, NOISE), xytext=(lod + 1.2, NOISE + 0.0112),
                fontsize=9.5, color=INK, ha="left",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=1))

ax.annotate("variegation leaves each\nchromosome here (1–2%)",
            xy=(1.5, 0.0009), xytext=(4.2, 0.0125),
            fontsize=9.5, color=INK, ha="left",
            arrowprops=dict(arrowstyle="->", color=MUTED, linewidth=1,
                            connectionstyle="arc3,rad=-0.25"))

# NOTA (2026-09-06): el limite calibrado posterior (Psi por ventanas, MC, kappa=2 -> 2.07%)
# NO se dibuja aqui a proposito. Sale de otro estadistico y no se puede leer de esta curva;
# superponerlo sugeriria que si. Vive en el texto del §5 y en mosaico/RESULTADOS.md §3.

ax.set_xlim(0, 32)
ax.set_ylim(0, 0.022)
ax.set_xlabel("cells carrying a given trisomy  (%)", fontsize=10, color=INK)
ax.set_ylabel("effect on |BAF − 0.5|   (×10⁻³)", fontsize=10, color=INK)
ax.set_yticks([0, 0.005, 0.010, 0.015, 0.020])
ax.set_yticklabels(["0", "5", "10", "15", "20"])
ax.set_title("Bulk WGS cannot resolve variegated aneuploidy",
             fontsize=12.5, color=INK, pad=22, loc="left", weight="semibold")
ax.text(0, 1.045, "and more coverage does not fix it: the limit is set by library bias, not read sampling",
        transform=ax.transAxes, fontsize=9.5, color=MUTED, ha="left")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(MUTED)
    ax.spines[s].set_linewidth(0.8)
ax.tick_params(colors=MUTED, labelsize=9, length=3)
ax.grid(axis="y", color=NOISE_FILL, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)

fig.text(0.005, -0.02,
         "Binomial simulation, DP = 44, 30,000 sites per point; the binomial baseline is subtracted. "
         "The 0.005 threshold is \u22481.4\u00d7 the standard deviation of mean |BAF \u2212 0.5| measured between "
         "the 22 autosomes at fixed depth (SD = 0.0035); a 2-SD criterion would move the limit to 16 %. "
         "This is the first-order analysis; the calibrated \u03a8 limit of mosaico/RESULTADOS.md \u00a73 is a "
         "different statistic and is not plotted here.",
         fontsize=7.8, color=MUTED, ha="left")

fig.tight_layout()
fig.savefig("/home/gar16/datos/HACKATHON-MVA-2026/track2/fig1_detection_limit.png",
            bbox_inches="tight", facecolor=SURFACE)
print(f"figura escrita. LOD calculado = {lod:.1f}% de las células")
