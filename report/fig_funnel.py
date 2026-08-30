#!/usr/bin/env python3
"""Figura 3: el embudo de los cinco filtros.

Misma direccion de arte que fig1/fig2: fondo hueso, acento verde-petroleo para
lo que sobrevive, terracota para lo que muere. Codificacion secundaria: la
etiqueta dice el veredicto, no solo el color.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ACCENT = "#1a9e8f"
ALERT = "#b8452a"
INK = "#2a2724"
MUTED = "#8a8378"
SURFACE = "#fcfcfb"
BAND = "#ede9e2"

FILTERS = [
    ("1  Regulatory", "Approved for marketing?",
     "AICAR · 17-AAG · reversine · apcin · proTAME · DCZ0415"),
    ("2  Mechanistic", "Addresses the lesion or its consequence?",
     "agents on uninvolved pathways"),
    ("3  Pharmacokinetic", "C$_{max}$ $\\geq$ effective concentration?",
     "METFORMIN — no aneuploidy-selective EC$_{50}$ exists;\n~1000$\\times$ short for the complex I route proposed"),
    ("4  Safety in $\\it{this}$ patient", "Compatible with his comorbidities?",
     "BORTEZOMIB — neuropathy 18% of children, on existing muscle atrophy"),
    ("5  Direction of effect", "Avoids worsening mis-segregation?",
     "anything selecting for unstable clones"),
]

fig, ax = plt.subplots(figsize=(9.1, 6.5))
fig.patch.set_facecolor(SURFACE); ax.set_facecolor(SURFACE)

TOP, STEP, H = 9.2, 1.62, 0.92
W0, SHRINK = 8.9, 0.40

for i, (name, question, killed) in enumerate(FILTERS):
    y = TOP - i * STEP
    w = W0 - i * SHRINK
    x = (10 - w) / 2
    is_kill = killed.split()[0] in ("METFORMIN", "BORTEZOMIB")
    ax.add_patch(FancyBboxPatch((x, y - H/2), w, H,
                 boxstyle="round,pad=0.02,rounding_size=0.12",
                 facecolor=BAND, edgecolor=INK, linewidth=1.1, zorder=2))
    ax.text(x + 0.28, y + 0.17, name, fontsize=11.5, weight="bold",
            color=INK, va="center", zorder=3)
    ax.text(x + 0.28, y - 0.22, question, fontsize=9.2, color=MUTED,
            va="center", style="italic", zorder=3)
    # lo que muere en este filtro, a la derecha
    ax.annotate("", xy=(x + w + 1.02, y), xytext=(x + w + 0.06, y),
                arrowprops=dict(arrowstyle="-|>", color=ALERT if is_kill else MUTED,
                                linewidth=1.9 if is_kill else 1.0, shrinkA=0, shrinkB=0),
                zorder=3)
    ax.text(x + w + 1.14, y, killed, fontsize=9.6 if is_kill else 8.4,
            color=ALERT if is_kill else MUTED, va="center",
            weight="bold" if is_kill else "normal", zorder=3)
    if i < len(FILTERS) - 1:
        ax.annotate("", xy=(5, y - STEP + H/2 + 0.04), xytext=(5, y - H/2 - 0.04),
                    arrowprops=dict(arrowstyle="-|>", color=INK, linewidth=1.3), zorder=1)

# salida
y_out = TOP - len(FILTERS) * STEP - 0.15
ax.add_patch(FancyBboxPatch((0.15, y_out - 0.78), 9.7, 1.56,
             boxstyle="round,pad=0.02,rounding_size=0.14",
             facecolor="#e4f2ef", edgecolor=ACCENT, linewidth=1.8, zorder=2))
ax.text(5.0, y_out + 0.41, "Nothing passes all five today",
        fontsize=12.2, weight="bold", color=ACCENT, ha="center", va="center", zorder=3)
ax.text(5.0, y_out - 0.22,
        "The proteasome class survives filters 1$-$3 and is held\n"
        "as a conditional answer for a future active tumour ($\\S$4, $\\S$6)",
        fontsize=9.0, color=INK, ha="center", va="center", zorder=3)

ax.text(0.35, TOP + 1.15, "Five filters, not two",
        fontsize=15, weight="bold", color=INK)
ax.text(0.35, TOP + 0.78,
        "Filters 3 and 5 are the two most often skipped, and they eliminate the most candidates.",
        fontsize=9.6, color=MUTED)

ax.set_xlim(0, 15.4); ax.set_ylim(y_out - 1.25, TOP + 1.7)
ax.axis("off")
fig.tight_layout()
fig.savefig("fig3_funnel.png", dpi=200, facecolor=SURFACE, bbox_inches="tight")
print("fig3_funnel.png escrita")
