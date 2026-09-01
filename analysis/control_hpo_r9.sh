#!/usr/bin/env bash
# CONTROL 3 corregido (ronda 9, 01-sep-2026).
# Motivo: el control original declaraba cinco HPO "clinicamente no relacionados",
# pero DOS de ellos (HP:0001250 convulsiones y HP:0001631 comunicacion interauricular)
# SI estan anotados a MVA1 (OMIM:257300) en la HPO -> el control estaba contaminado.
# Aqui se repite con cinco terminos verificados como NO anotados a MVA1 via
# hpo/01_verificar.py, contra TODAS las MVA (OMIM:257300, OMIM:614114, OMIM:617598, ORPHA:1052) y contra los genes BUB1B/CEP57/TRIP13
T=/home/gar16/datos/HACKATHON-MVA-2026/tools
D=/home/gar16/datos/HACKATHON-MVA-2026/data
C=$T/exomiser-cli-15.1.0
OUT=$T/results/controles
mkdir -p "$OUT"

hacer_sample () { local dest=$1; shift
  { echo "---"; echo "id: control"; echo "subject:"; echo "  id: WGS_EX2312012"; echo "  sex: MALE"
    echo "phenotypicFeatures:"; for h in "$@"; do echo "  - type: { id: \"$h\" }"; done
    echo "metaData:"; echo "  created: \"2026-08-30T00:00:00Z\""; echo "  createdBy: \"control_r9\""
    echo "  phenopacketSchemaVersion: \"1.0.0\""; } > "$dest"; }

correr () { cd "$C" || return
  timeout 900 nice -n 12 java -Xmx12g -jar exomiser-cli-15.1.0.jar \
    analyse --sample "$2" --vcf "$D/WGS_EX2312012_HGWCNDSX7.vcf.gz" --assembly GRCh38 \
    --analysis "$T/analysis_mva.yml" --output-directory "$OUT" --output-filename "$1" \
    --output-format TSV_GENE > /dev/null 2>&1
  local g="$OUT/$1.genes.tsv"
  if [ -f "$g" ]; then
    rank=$(awk -F'\t' 'NR>1 && $3=="BUB1B"{print $1; exit}' "$g")
    score=$(awk -F'\t' 'NR>1 && $3=="BUB1B"{printf "%.4f",$7; exit}' "$g")
    top=$(awk -F'\t' 'NR==2{print $3; exit}' "$g")
    tops=$(awk -F'\t' 'NR==2{printf "%.4f",$7; exit}' "$g")
    n=$(( $(wc -l < "$g") - 1 ))
    printf "%-30s BUB1B rank=%-6s score=%-9s | top: %s (%s) | genes=%s\n" "$1" "${rank:-ausente}" "${score:--}" "$top" "$tops" "$n"
  else printf "%-30s FALLO\n" "$1"; fi; }

echo "=== CONTROL 3c (r9): cinco HPO verificados contra TODAS las formas de MVA ==="
echo "Motivo: HP:0000365 (hipoacusia), usado en el control r7 YA ENVIADO, esta anotado a"
echo "OMIM:614114 (MVA2), a ORPHA:1052 (MVA generico) y a los genes BUB1B, CEP57 y TRIP13."
echo "La verificacion de la r7 solo consulto OMIM:257300 (MVA1). Reemplazado por HP:0000988."
echo "HP:0000509 conjuntivitis | HP:0002205 infecciones respiratorias | HP:0002315 cefalea"
echo "HP:0000989 prurito | HP:0000988 rash cutaneo"
hacer_sample "$T/_ctl_r9.yml" HP:0000509 HP:0002205 HP:0002315 HP:0000989 HP:0000988
correr "hpos_ajenos_r9_limpios" "$T/_ctl_r9.yml"
echo
echo "=== Replica del control r7 (contaminado por HP:0000365), para comparar ==="
hacer_sample "$T/_ctl_r9.yml" HP:0000365 HP:0000509 HP:0002205 HP:0002315 HP:0000989
correr "hpos_r7_con_hipoacusia" "$T/_ctl_r9.yml"
rm -f "$T/_ctl_r9.yml"
echo "CONTROLES-R9-LISTOS"
