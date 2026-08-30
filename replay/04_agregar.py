#!/usr/bin/env python3
"""Agrega todas las corridas de MVA-Replay en una tabla y calcula las metricas
pre-registradas. No re-corre nada: solo lee out/*.genes.tsv."""
import json, os, csv, glob, statistics as st

REP = os.path.dirname(os.path.abspath(__file__))
NUESTRO = 0.5871          # BUB1B AD, corrida real del paciente
NUESTRO_AJENO = 0.4187    # control HPO ajeno de la ronda 7

def leer(log):
    out = []
    for l in open(os.path.join(REP, log)):
        l = l.strip()
        if l.startswith("{"):
            out.append(json.loads(l))
    return out

A  = leer("_runA1.log") + leer("_runA2.log")
A1k= leer("_1kgp_pipeline.log") if os.path.exists(os.path.join(REP,"_1kgp_pipeline.log")) else []
A1k= [d for d in A1k if isinstance(d, dict) and d.get("case","").startswith("A1k_")]
BC = leer("_runBC.log")
F2 = leer("_rerun_fancd2.log")

# el re-run del brazo señuelo sustituye las celdas pre-enmienda
BC = [d for d in BC if not d.get("caso","").startswith("B_arm2_FANCD2")] + F2

print("="*78)
print("EXPERIMENTO A — escala del 0.5871 en genomas sanos, HPO real del paciente")
print("="*78)
giab   = sorted([d for d in A if d["case"].endswith("_real")], key=lambda d: d["top_score"])
mil    = sorted([d for d in A1k if d["case"].endswith("_real")], key=lambda d: d["top_score"])
for tier, rows in (("GIAB v4.2.1", giab), ("1000G 30x", mil)):
    if not rows: continue
    ts = [d["top_score"] for d in rows]
    print(f"\n  {tier}  (n = {len(rows)})")
    print(f"    rango del gen top: {min(ts):.4f} – {max(ts):.4f}   mediana {st.median(ts):.4f}")
    print(f"    genomas con gen top >= {NUESTRO}: {sum(1 for t in ts if t >= NUESTRO)} de {len(ts)}")
    print(f"    BUB1B aparece en la tabla:        {sum(1 for d in rows if d.get('BUB1B_rank') not in ('',None))} de {len(rows)}")
    print(f"    genes rankeados (mediana):        {st.median([d['n_genes'] for d in rows]):.0f}  (paciente: 4565)")
    print(f"    top-5 mas altos: " + ", ".join(f"{d['case'].split('_')[1]}={d['top_score']:.4f}({d['top_gene']})"
                                               for d in rows[-5:][::-1]))
todos = [d["top_score"] for d in giab + mil]
if todos:
    sup = sum(1 for t in todos if t >= NUESTRO)
    print(f"\n  P-A: nuestro {NUESTRO} vs el maximo sano {max(todos):.4f}  ->  "
          f"{'SE SOSTIENE' if sup==0 else 'FALSIFICADA'} ({sup} de {len(todos)} genomas sanos lo igualan o superan)")
    todos_s = sorted(todos)
    pct = 100.0 * sum(1 for t in todos_s if t < NUESTRO) / len(todos_s)
    print(f"       percentil de 0.5871 en la distribucion sana: {pct:.1f}")

print("\n" + "="*78)
print("EXPERIMENTO B — variante vs fenotipo, con señuelo que el fenotipo si quiere")
print("="*78)
for arm, gene in (("B_arm1_BUB1B","BUB1B"), ("B_arm2_FANCD2","FANCD2")):
    print(f"\n  {arm}  (gen plantado: {gene})")
    for ph in ("real","ajeno"):
        cel = [d for d in BC if d.get("caso","").startswith(arm) and d.get("hpo")==ph]
        if not cel: continue
        r1 = sum(1 for d in cel if d.get(gene+"_rank")==1)
        sc = {d.get(gene+"_score") for d in cel}
        tf = sum(1 for d in cel if d.get("technical_failure"))
        print(f"    HPO {ph:6s}: rank 1 en {r1}/{len(cel)}   score = {sorted(sc)}"
              f"   fallos tecnicos: {tf}")
b1r = {d.get("BUB1B_score") for d in BC if d.get("caso","").startswith("B_arm1") and d.get("hpo")=="real"}
b1a = {d.get("BUB1B_score") for d in BC if d.get("caso","").startswith("B_arm1") and d.get("hpo")=="ajeno"}
if b1r and b1a:
    dr, da = list(b1r)[0], list(b1a)[0]
    print(f"\n  P-B4: delta(real - ajeno) = {dr-da:.4f}  ({100*(dr-da)/dr:.1f}% del score)  "
          f"-> {'se sostiene' if dr-da < 0.20 else 'FALSIFICADA'} (umbral 0.20)")

print("\n" + "="*78)
print("EXPERIMENTO C — cuanto del score lo pone ClinVar")
print("="*78)
for arq, etq in (("C_hi","dos P/LP"), ("B_arm1","P/LP + VUS (la del niño)"), ("C_lo","dos VUS")):
    cel = [d for d in BC if d.get("caso","").startswith(arq) and d.get("hpo")=="real"]
    if not cel: continue
    sc = sorted({d.get("BUB1B_score") for d in cel})
    rk = sorted(d.get("BUB1B_rank") for d in cel)
    ac = sorted({d.get("acmg","") for d in cel})
    print(f"  {etq:26s} score={sc}  ranks={rk}  ACMG={ac}")
hi = [d.get("BUB1B_score") for d in BC if d.get("caso","").startswith("C_hi")]
lo = [d.get("BUB1B_score") for d in BC if d.get("caso","").startswith("C_lo")]
if hi and lo:
    print(f"\n  P-C: C-hi - C-lo = {hi[0]-lo[0]:.4f}  -> "
          f"{'se sostiene' if hi[0]-lo[0] >= 0.10 else 'FALSIFICADA'} (umbral 0.10)")

filas = A + A1k + BC
with open(os.path.join(REP,"resultados_todos.tsv"),"w",newline="") as f:
    cols = sorted({k for d in filas for k in d})
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", extrasaction="ignore")
    w.writeheader(); w.writerows(filas)
print(f"\n-> resultados_todos.tsv  ({len(filas)} corridas)")
