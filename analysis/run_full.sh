#!/usr/bin/env bash
# Corrida COMPLETA: incluye no-codificantes via REMM, sin variantEffectFilter.
# Control para verificar que la respuesta no dependa de haber filtrado el no-codificante.
T=/home/gar16/datos/HACKATHON-MVA-2026/tools
D=/home/gar16/datos/HACKATHON-MVA-2026/data
R=$T/data/remm/ReMM.v0.4.hg38.tsv.gz

# esperar a que la descarga de REMM se estabilice
prev=0
for _ in $(seq 1 60); do
  cur=$(stat -c%s "$R" 2>/dev/null || echo 0)
  [ "$cur" = "$prev" ] && [ "$cur" -gt 1000000000 ] && break
  prev=$cur; sleep 30
done
echo "[$(date +%T)] REMM estable en $((prev/1048576)) MB"

cd "$T/exomiser-cli-15.1.0" || exit 1
timeout 21600 nice -n 12 java -Xmx16g -jar exomiser-cli-15.1.0.jar \
  analyse \
  --sample "$T/sample_mva.yml" \
  --vcf "$D/WGS_EX2312012_HGWCNDSX7.vcf.gz" --assembly GRCh38 \
  --analysis "$T/analysis_full.yml" \
  --output-directory "$T/results" --output-filename mva-genome-full \
  --output-format TSV_GENE,TSV_VARIANT \
  > "$T/logs/exomiser_full.log" 2>&1
rc=$?
echo "[$(date +%T)] codigo $rc"
if [ $rc -eq 0 ] && [ -f "$T/results/mva-genome-full.genes.tsv" ]; then
  echo "FULL-OK"
  echo "--- top 10 genes (con no-codificantes) ---"
  awk -F'\t' 'NR>1 && NR<12 {printf "  %-3s %-14s %s\n", NR-1, $3, $7}' "$T/results/mva-genome-full.genes.tsv"
  echo "--- posicion de BUB1B ---"
  awk -F'\t' 'NR>1 && $3=="BUB1B" {print "  rank "$1"  MOI="$5"  score="$7; exit}' "$T/results/mva-genome-full.genes.tsv"
else
  echo "FULL-FALLO ($rc)"
  grep -iE "IllegalState|IllegalArgument|Caused by|Exception:" "$T/logs/exomiser_full.log" \
    | grep -v "^[[:space:]]*at " | head -4
fi
