#!/usr/bin/env bash
# Operational half of replay/TRANSFER_TRIP13.md: bare clone -> resources step by step -> 3 real runs.
# Every command and its exit code is logged; nothing in the analysis is modified.
S=<scratch>
A=/home/gar16/datos/HACKATHON-MVA-2026
HPO="HP:0002667 HP:0006743 HP:0000520 HP:0000508 HP:0007663 HP:0012375"
AL1=chr5:900524:T:TA
AL2=chr5:914464:G:C
step(){ echo; echo "### $(date -Is) STEP: $*"; }
run(){ echo "\$ $*"; "$@"; echo "[rc=$?]"; }

cd "$S" && rm -rf clone
step "0 bare clone"
run /usr/bin/time -f "clone wall %e s" gh repo clone cpu-16/mva-hackathon-2026 clone -- -q
cd clone && run git log -1 --format='%h %cI %s'
run du -sh --exclude=.git .

step "O-1 test_output_reuse in the bare clone"
run python3 replay/test_output_reuse.py

step "O-2 self-check in the bare clone (expected to stop and name what is missing)"
run python3 replay/mva_replay.py --self-check

step "1 provide Exomiser + analysis YAML"
mkdir -p tools && ln -s "$A/tools/exomiser-cli-15.1.0" tools/ && cp analysis/analysis_mva.yml tools/analysis_mva.yml
run python3 replay/mva_replay.py --self-check

step "2 provide ClinVar + HPOA"
mkdir -p pipeline/resources && for f in clinvar.vcf.gz clinvar.vcf.gz.tbi genes_to_phenotype.txt hp.obo; do ln -s "$A/pipeline/resources/$f" pipeline/resources/; done
run python3 replay/mva_replay.py --self-check

step "3 dry-run with no background VCF"
run python3 replay/mva_replay.py --gene TRIP13 --allele $AL1 --allele $AL2 --hpo $HPO --sex FEMALE --background replay/bg/HG001.vcf.gz --dry-run --name T_TRIP13_HG001_dry3

step "4 provide backgrounds"
ln -s "$A/replay/bg" replay/bg
run python3 replay/mva_replay.py --gene TRIP13 --allele $AL1 --allele $AL2 --hpo $HPO --sex FEMALE --background replay/bg/HG001.vcf.gz --dry-run --name T_TRIP13_HG001_dry4

step "5 provide hg38 FASTA (chr5)"
mkdir -p replay/raw && ln -s "$A/replay/raw/fasta" replay/raw/fasta
for bg in HG001 HG002 HG005; do
  run python3 replay/mva_replay.py --gene TRIP13 --allele $AL1 --allele $AL2 --hpo $HPO --sex FEMALE --background replay/bg/$bg.vcf.gz --dry-run --name T_TRIP13_${bg}_dry5
done

for bg in HG001 HG002 HG005; do
  step "REAL RUN $bg"
  /usr/bin/time -v python3 replay/mva_replay.py --gene TRIP13 --allele $AL1 --allele $AL2 --hpo $HPO --sex FEMALE \
      --background replay/bg/$bg.vcf.gz --name T_TRIP13_$bg 2> >(while IFS= read -r l; do echo "$(date +%s) $l"; done)
  echo "[rc=$?]"
done
echo; echo "### $(date -Is) DONE"
