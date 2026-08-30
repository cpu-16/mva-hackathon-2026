#!/usr/bin/env bash
cd /home/gar16/datos/HACKATHON-MVA-2026/fase
until [ -s panel_chr15.vcf.gz.tbi ] && [ -s plink.chr15.GRCh38.map ]; do sleep 20; done
# el mapa plink usa "15"; Beagle exige que coincida con el VCF (chr15)
awk 'BEGIN{OFS="\t"}{$1="chr15"; print}' plink.chr15.GRCh38.map > mapa_chr15.map
for s in 1 2 3 4 5 6 7 8 9 10; do
  java -Xmx10g -jar beagle.jar \
     gt=paciente_chr15_win.vcf.gz ref=panel_chr15.vcf.gz map=mapa_chr15.map \
     out=fase_seed$s seed=$s nthreads=6 impute=false > log_seed$s.txt 2>&1
  if [ -s fase_seed$s.vcf.gz ]; then
    tabix -f -p vcf fase_seed$s.vcf.gz
    echo -n "seed $s: "
    bcftools query -r chr15:40209701,chr15:40220612 -f '%POS=[%GT] ' fase_seed$s.vcf.gz
    echo
  else
    echo "seed $s: SIN SALIDA ($(tail -2 log_seed$s.txt | tr '\n' ' '))"
  fi
done
echo BEAGLEDONE
