#!/usr/bin/env python3
"""Figura 2: los dos alelos de BUB1B sobre el mapa de dominios de BubR1.

Misma direccion de arte que fig1: fondo hueso, acento verde-petroleo para el
dominio relevante, terracota para las variantes. Par validado (CVD dE 13.2).
Codificacion secundaria: etiquetas directas, no solo color.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ACCENT = "#1a9e8f"     # dominio quinasa C-terminal (el que importa aqui)
ALERT = "#b8452a"      # variantes
INK = "#2a2724"
MUTED = "#8a8378"
SURFACE = "#fcfcfb"
DOMAIN_BG = "#ddd8cf"

# alturas escalonadas para que las etiquetas de dominios pequenos no colisionen
LABEL_OFFSETS = {"KEN1": 0.50, "KEN2": 0.34, "GLEBS": 0.50, "KARD": 0.34}

L = 1050  # residuos

# (inicio, fin, etiqueta, ¿es el dominio de interes?)
DOMAINS = [
    (20, 32, "KEN1", False),
    (50, 204, "TPR", False),
    (298, 310, "KEN2", False),
    (392, 426, "GLEBS", False),
    (665, 682, "KARD", False),
    (766, 1050, "kinase domain", True),
]

fig, ax = plt.subplots(figsize=(8.4, 3.5), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)


def draw_protein(y, end, label, truncated=False, height=0.30):
    """Dibuja una copia de la proteina desde 1 hasta `end`."""
    ax.add_patch(FancyBboxPatch((0, y - height / 2), end, height,
                                boxstyle="round,pad=0,rounding_size=4",
                                facecolor="#f0ece5", edgecolor=MUTED,
                                linewidth=0.7, zorder=2, mutation_aspect=0.02))
    for s, e, name, is_key in DOMAINS:
        if s >= end:
            continue
        e_clip = min(e, end)
        col = ACCENT if is_key else DOMAIN_BG
        ax.add_patch(Rectangle((s, y - height / 2), e_clip - s, height,
                               facecolor=col, edgecolor="none", zorder=3))
        if y == 2:
            mid = (s + e_clip) / 2
            if (e_clip - s) > 90:
                ax.text(mid, y + height / 2 + 0.13, name, ha="center",
                        va="bottom", fontsize=8.2, color=INK)
            else:
                off = LABEL_OFFSETS.get(name, 0.34)
                ax.plot([mid, mid], [y + height / 2 + 0.02, y + height / 2 + off - 0.04],
                        color=MUTED, linewidth=0.6, zorder=1)
                ax.text(mid, y + height / 2 + off, name, ha="center",
                        va="bottom", fontsize=8.2, color=INK)
    if truncated:
        ax.plot([end, end], [y - height / 2 - 0.06, y + height / 2 + 0.06],
                color=ALERT, linewidth=2.4, zorder=5, solid_capstyle="butt")
    ax.text(-30, y, label, ha="right", va="center", fontsize=9.5, color=INK)


# fila 1: proteina de referencia
draw_protein(2, L, "BubR1\nreference")
ax.text(L + 18, 2, "1,050 aa", ha="left", va="center", fontsize=8.5, color=MUTED)

# fila 2: alelo truncante
draw_protein(1.1, 737, "allele 1", truncated=True)
ax.annotate("p.Leu737Ter\npremature stop — removes the entire domain",
            xy=(737, 1.1 - 0.18), xytext=(560, 0.60),
            fontsize=9, color=ALERT, ha="center",
            arrowprops=dict(arrowstyle="-", color=ALERT, linewidth=1))

# fila 3: alelo missense
draw_protein(0.2, L, "allele 2")
ax.plot([1002], [0.2], marker="v", markersize=9, color=ALERT, zorder=6,
        markeredgecolor=SURFACE, markeredgewidth=1)
ax.annotate("p.Asn1002Lys\nmissense in the C-lobe",
            xy=(1002, 0.2 + 0.18), xytext=(1005, 0.62),
            fontsize=9, color=ALERT, ha="center",
            arrowprops=dict(arrowstyle="-", color=ALERT, linewidth=1))

ax.set_xlim(-210, L + 130)
ax.set_ylim(-0.15, 3.05)
ax.axis("off")
ax.set_title("Both BUB1B alleles converge on the C-terminal kinase domain",
             fontsize=12, color=INK, loc="left", x=-0.02, pad=26, weight="semibold")
ax.text(-0.02, 1.055, "one removes it entirely; the other alters it — with significance still uncertain",
        transform=ax.transAxes, fontsize=9.3, color=MUTED, ha="left")
fig.text(0.012, 0.015,
         "Domain intervals from UniProt O60566 (protein kinase domain, residues 766–1050); "
         "annotation coordinates, not clinical ones.",
         fontsize=7.6, color=MUTED, ha="left")

fig.tight_layout()
fig.savefig("/home/gar16/datos/HACKATHON-MVA-2026/track2/fig2_domains.png",
            bbox_inches="tight", facecolor=SURFACE)
print("fig2_domains.png escrita")
