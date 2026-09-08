#!/usr/bin/env bash
S=<scratch>
HPO="HP:0002667 HP:0006743 HP:0000520 HP:0000508 HP:0007663 HP:0012375"
cd $S/clone
for bg in HG001 HG002 HG005; do
  echo; echo "### $(date -Is) REAL RUN $bg (name T2_TRIP13_$bg)"
  /usr/bin/time -v python3 replay/mva_replay.py --gene TRIP13 --allele chr5:900524:T:TA --allele chr5:914464:G:C --hpo $HPO --sex FEMALE \
      --background replay/bg/$bg.vcf.gz --name T2_TRIP13_$bg 2> >(while IFS= read -r l; do echo "$(date +%s) $l"; done)
  echo "[rc=$?]"
done
echo "### $(date -Is) DONE"
