#!/usr/bin/env bash
# Analisis genome-wide con Exomiser 15.1.0: WGS singleton + 8 terminos HPO, sin panel de genes.
T=/home/gar16/datos/HACKATHON-MVA-2026/tools
D=/home/gar16/datos/HACKATHON-MVA-2026/data
cd "$T/exomiser-cli-15.1.0" || exit 1
echo "[$(date +%T)] Exomiser genome-wide, 8 HPO, analisis propio (sin preset)"
timeout 21600 nice -n 12 java -Xmx16g -jar exomiser-cli-15.1.0.jar \
  analyse \
  --sample "$T/sample_mva.yml" \
  --vcf "$D/WGS_EX2312012_HGWCNDSX7.vcf.gz" --assembly GRCh38 \
  --analysis "$T/analysis_mva.yml" \
  --output-directory "$T/results" --output-filename mva-genome-hpo \
  --output-format TSV_GENE,TSV_VARIANT,JSON,HTML \
  > "$T/logs/exomiser_run.log" 2>&1
rc=$?
echo "[$(date +%T)] codigo $rc"
if [ $rc -eq 0 ]; then
  echo "ANALISIS-OK"
else
  echo "ANALISIS-FALLO"
  grep -iE "IllegalState|IllegalArgument|Caused by|Exception:" "$T/logs/exomiser_run.log" \
    | grep -v "^[[:space:]]*at " | head -4
fi
