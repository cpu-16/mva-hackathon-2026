#!/usr/bin/env bash
# Espera a que el piloto termine chr17, verifica cobertura (obligatorio: cuatro extracciones
# remotas de este proyecto truncaron en silencio con exit 0) y corre el analisis pre-registrado.
set -u
cd /home/gar16/datos/HACKATHON-MVA-2026
LOG=mosaico/_al_terminar.log
echo "== esperando el piloto ==  $(date)" > $LOG
while pgrep -f "mosaico/_piloto.sh" > /dev/null; do sleep 60; done
echo "piloto terminado $(date)" >> $LOG

echo "== verificacion de cobertura ==" >> $LOG
python3 - >> $LOG 2>&1 <<'PY'
import gzip, os
ok_all = True
for c in (8, 17):
    f = f"mosaico/piloto/chr{c}.tsv.gz"
    if not os.path.exists(f):
        print(f"chr{c}: FALTA el archivo"); ok_all = False; continue
    pos = [int(l.split('\t', 1)[0]) for l in gzip.open(f, 'rt')]
    a, b = 5_000_000, 25_000_000
    gaps = max(pos[i+1] - pos[i] for i in range(len(pos)-1))
    ok = pos[0] < a + 1_000_000 and pos[-1] > b - 1_000_000 and gaps <= 2_000_000
    ok_all &= ok
    print(f"chr{c}: {len(pos):,} sitios  {pos[0]:,}..{pos[-1]:,}  hueco mayor {gaps:,} bp  "
          f"-> {'PASA' if ok else 'FALLA (truncado, repetir)'}")
print("COBERTURA_OK" if ok_all else "COBERTURA_FALLA")
PY

if grep -q COBERTURA_OK $LOG; then
  echo "== analisis pre-registrado ==" >> $LOG
  python3 mosaico/08_control.py >> $LOG 2>&1
else
  echo "ABORTADO: la cobertura no pasa, no se corre el analisis" >> $LOG
fi
echo "== fin $(date) ==" >> $LOG
