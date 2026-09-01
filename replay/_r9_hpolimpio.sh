#!/usr/bin/env bash
# Re-corre el brazo de HPO-ajeno del benchmark con el set r9 (verificado contra TODAS las MVA),
# en los tres fondos GIAB usados en RESULTADOS.md. Ejercita ademas la herramienta empaquetada
# sobre fondos distintos, ruta que su verificacion inicial no cubrio.
set -u
cd /home/gar16/datos/HACKATHON-MVA-2026
for bg in HG001 HG002 HG005; do
  echo "=== fondo $bg ==="
  python3 replay/mva_replay.py --gene BUB1B \
    --allele chr15:40209701:T:G --allele chr15:40220612:T:G \
    --hpo HP:0002859 HP:0000121 HP:0004322 HP:0001508 HP:0003202 HP:0001622 HP:0001518 HP:0200067 \
    --hpo-unrelated HP:0000509 HP:0002205 HP:0002315 HP:0000989 HP:0000988 \
    --background /home/gar16/datos/HACKATHON-MVA-2026/replay/bg/$bg.vcf.gz --out /home/gar16/datos/HACKATHON-MVA-2026/replay/out_r9 --name BUB1B_${bg}_r9 2>&1 | tail -12
done
echo R9DONE
