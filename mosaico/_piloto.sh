#!/usr/bin/env bash
# Piloto del control externo, enmienda 4. Ventanas FIJAS declaradas antes de correr.
set -u
cd /home/gar16/datos/HACKATHON-MVA-2026/mosaico
D=https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20201028_3202_raw_GT_with_annot
M=$(paste -sd, <(head -10 ../replay/raw/muestras_1kgp.txt))
mkdir -p piloto
for c in 8 17; do
  F=20201028_CCDG_14151_B01_GRM_WGS_2020-08-05_chr$c.recalibrated_variants.vcf.gz
  O=piloto/chr$c.tsv.gz
  [ -s "$O" ] && { echo "chr$c ya"; continue; }
  echo "[chr$c] extrayendo chr$c:5000000-25000000 para 10 muestras…"
  t0=$(date +%s)
  ( cd piloto && bcftools view -r "chr$c:5000000-25000000" -s "$M" -v snps -m2 -M2 -f PASS "$D/$F" 2>../piloto/chr$c.err ) \
    | bcftools query -f '%POS\t%REF\t%ALT[\t%GT,%DP,%AD]\n' 2>>piloto/chr$c.err | gzip > "$O.part"
  mv "$O.part" "$O"
  n=$(zcat "$O" | wc -l); first=$(zcat "$O" | head -1 | cut -f1); last=$(zcat "$O" | tail -1 | cut -f1)
  echo "[chr$c] $n sitios, $first..$last, $(( ($(date +%s)-t0)/60 )) min"
done
echo PILOTODONE
