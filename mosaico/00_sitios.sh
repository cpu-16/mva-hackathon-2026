#!/usr/bin/env bash
# Sitios retenidos por la regla del pre-registro: het del probando, PASS, SNV bialélico,
# DP 20-80, GQ>=30, presente en el panel 1000G con MAF>=0.01.
set -u
P=/home/gar16/datos/HACKATHON-MVA-2026
V=$P/data/WGS_EX2312012_HGWCNDSX7.vcf.gz
K=$P/replay/raw/1kgp
mkdir -p sitios
for c in $(seq 1 22); do
  [ -s $K/chr$c.vcf.gz ] || { echo "chr$c: panel aún no disponible"; continue; }
  [ -s sitios/chr$c.tsv.gz ] && { echo "chr$c: ya"; continue; }
  # sitios comunes del panel (MAF>=0.01), sin prefijo chr para cruzar con el VCF del probando
  bcftools view -v snps -m2 -M2 -i 'AF>=0.01 && AF<=0.99' $K/chr$c.vcf.gz 2>/dev/null \
    | bcftools query -f '%POS\t%REF\t%ALT\n' > /tmp/panel_$c.tsv
  # hets del probando con los filtros
  bcftools view -r $c -v snps -m2 -M2 -f PASS -i 'GT="het" && FMT/DP>=20 && FMT/DP<=80 && FMT/GQ>=30' $V 2>/dev/null \
    | bcftools query -f '%POS\t%REF\t%ALT\t[%DP\t%AD]\n' > /tmp/prob_$c.tsv
  awk -F'\t' 'NR==FNR{k[$1"_"$2"_"$3]=1; next} ($1"_"$2"_"$3) in k' /tmp/panel_$c.tsv /tmp/prob_$c.tsv | gzip > sitios/chr$c.tsv.gz
  echo "chr$c  panel_comunes=$(wc -l < /tmp/panel_$c.tsv)  hets_probando=$(wc -l < /tmp/prob_$c.tsv)  RETENIDOS=$(zcat sitios/chr$c.tsv.gz | wc -l)"
  rm -f /tmp/panel_$c.tsv /tmp/prob_$c.tsv
done
echo SITIOSDONE
