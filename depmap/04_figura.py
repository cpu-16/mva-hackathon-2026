#!/usr/bin/env python3
"""Figura 4 del reporte: la prueba pre-registrada, incluido el resultado que nos contradice."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, pandas as pd, numpy as np
from scipy import stats

ACCENT="#1a9e8f"; ALERT="#b8452a"; INK="#2a2724"; MUTED="#8a8378"; SURF="#fcfcfb"; BAND="#ede9e2"

R=pd.read_csv("rho_todos_compuestos.csv")
cl=pd.read_csv("raw/Repurposing_CompoundList.csv"); cl=cl[cl.screen=="REP.PRIMARY"]
nm=cl.set_index(cl.IDs.str.split(",").str[0].str.strip())["Drug.Name"].to_dict()
R["name"]=R.brd.map(nm)
d=pd.read_csv("psmb5_merged.csv")

fig,(a,b)=plt.subplots(1,2,figsize=(11.6,4.9))
fig.patch.set_facecolor(SURF)

# --- A: dónde caen nuestros fármacos en la distribución de los 6790
a.set_facecolor(SURF)
a.hist(R.rho,bins=70,color=BAND,edgecolor="#d8d2c8",linewidth=.4)
marks=[("BORTEZOMIB",ALERT,1.0),("CARFILZOMIB",ALERT,.65),("IXAZOMIB",MUTED,.9),
       ("METFORMIN",MUTED,.9),("PACLITAXEL",INK,.9)]
ymax=a.get_ylim()[1]
for i,(nme,col,al) in enumerate(marks):
    r=R[R.name==nme]
    if not len(r): continue
    x=r.rho.iloc[0]; y=ymax*(0.92-i*0.135)
    a.plot([x,x],[0,y],color=col,lw=1.8 if col==ALERT else 1.1,alpha=al)
    a.annotate(f"{nme.title()}  ρ={x:+.3f}",xy=(x,y),xytext=(6 if x<0 else 6,0),
               textcoords="offset points",fontsize=8.6,color=col,va="center",
               weight="bold" if col==ALERT else "normal")
a.axvline(0,color=MUTED,lw=.8,ls=":")
a.set_xlabel("Spearman ρ  ·  aneuploidy score vs drug sensitivity\n(negative = more aneuploid, more killed)",fontsize=9.2,color=INK)
a.set_ylabel("compounds",fontsize=9.2,color=INK)
a.set_title("A · PRISM: 6,790 compounds; n = 424–444 solid lines",fontsize=10.4,weight="bold",color=INK,loc="left")
a.text(.02,.60,"No proteasome inhibitor\nreaches FDR < 0.05.\nBortezomib sits in the 4th\npercentile by direction —\nsuggestive, not significant.",
       transform=a.transAxes,fontsize=8.1,color=MUTED,va="top",ha="left",
       bbox=dict(boxstyle="round,pad=0.45",facecolor=SURF,edgecolor="#ddd8cf",linewidth=.7))
for s in ("top","right"): a.spines[s].set_visible(False)

# --- B: CRISPR PSMB5 por estrato
b.set_facecolor(SURF)
for st,col,lab in [("solid",INK,"solid tumour (n=833)"),("haematological",ALERT,"haematological (n=113)")]:
    s=d[d.stratum==st]
    b.scatter(s.aneuploidy_score,s.PSMB5,s=7,alpha=.28,color=col,linewidths=0)
    z=np.polyfit(s.aneuploidy_score,s.PSMB5,1); xs=np.linspace(0,39,50)
    rho,p=stats.spearmanr(s.aneuploidy_score,s.PSMB5)
    b.plot(xs,np.polyval(z,xs),color=col,lw=2.2,label=f"{lab}   ρ={rho:+.3f}")
b.legend(frameon=False,fontsize=8.6,loc="lower left")
b.set_xlabel("aneuploidy score (altered chromosome arms, 0–39)",fontsize=9.2,color=INK)
b.set_ylabel("PSMB5 CRISPR gene effect\n(more negative = more essential)",fontsize=9.2,color=INK)
b.set_title("B · CRISPR: dependency on bortezomib's target",fontsize=10.4,weight="bold",color=INK,loc="left")
b.text(.98,.97,"interaction aneuploidy × lineage: p = 0.026\nthe association is significantly weaker\nin solid tumours",
       transform=b.transAxes,fontsize=8.3,color=ALERT,ha="right",va="top",weight="bold")
for s in ("top","right"): b.spines[s].set_visible(False)

fig.suptitle("Pre-registered test of our own candidate: no significant drug association; weaker PSMB5 link in solid lines",
             fontsize=12.4,weight="bold",color=INK,x=.008,ha="left",y=.995)
fig.tight_layout(rect=[0,0,1,.94])
fig.savefig("../track2/fig4_depmap.png",dpi=200,facecolor=SURF,bbox_inches="tight")
print("fig4_depmap.png escrita")
