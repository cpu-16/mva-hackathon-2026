#!/usr/bin/env bash
# Fast MVA-panel triage. NOT the primary analysis — that is genome-wide Exomiser+HPO.
# This is a control: "do any obvious biallelic hits sit in known MVA genes?"
#
# Needs bcftools (not installed here yet).
#   Fedora:  sudo dnf install bcftools htslib
#   Debian:  sudo apt install bcftools tabix
#   conda:   conda install -c bioconda bcftools
#
# Usage:  ./triage.sh patient.vcf.gz [outdir]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
BED="$ROOT/mva_panel.hg38.bed"
CLINVAR="$ROOT/resources/clinvar.vcf.gz"
MAP_STRIP="$ROOT/chroms_ucsc_to_ncbi.txt"
MAP_ADD="$ROOT/chroms_ncbi_to_ucsc.txt"
MAX_AF="${MAX_AF:-0.01}"

if [[ $# -lt 1 ]]; then
  echo "usage: $0 patient.vcf.gz [outdir]" >&2
  exit 2
fi
VCF=$1
OUT=${2:-"$ROOT/out"}
mkdir -p "$OUT"

if ! command -v bcftools >/dev/null 2>&1; then
  echo "bcftools not found. Install with: sudo dnf install bcftools htslib" >&2
  exit 1
fi
if [[ ! -f "$VCF" ]]; then
  echo "missing VCF: $VCF" >&2
  exit 1
fi
if [[ ! -f "$CLINVAR" ]]; then
  echo "missing ClinVar: $CLINVAR" >&2
  exit 1
fi

# ponytail: -T streams, no index on the 315 MB WGS VCF. -R would need .tbi.
# FILTER=. is an unfiltered GATK site; dropping it would empty a raw WGS VCF.
# Keep ALT-carrying genotypes only (singleton hom-ref is noise).

# Detect chr prefix from ##contig (head|cut on variants trips SIGPIPE + set -e).
bed="$OUT/panel.bed"
hdr="$OUT/input.header"
bcftools view -h "$VCF" > "$hdr"
if grep -q '##contig=<ID=chr' "$hdr"; then
  vcf_has_chr=1
elif grep -q '##contig=<ID=' "$hdr"; then
  vcf_has_chr=0
else
  set +o pipefail
  first_chrom=$(bcftools view -H "$VCF" | head -n 1 | cut -f1)
  set -o pipefail
  case "$first_chrom" in chr*) vcf_has_chr=1 ;; *) vcf_has_chr=0 ;; esac
fi
if [[ "$vcf_has_chr" -eq 1 ]]; then
  grep -v '^#' "$BED" > "$bed"
else
  grep -v '^#' "$BED" | sed 's/^chr//' > "$bed"
fi

# INFO header for the gene tag we stamp from the BED name column.
gene_hdr="$OUT/gene.hdr"
printf '##INFO=<ID=MVA_GENE,Number=1,Type=String,Description="MVA panel gene (Ensembl span +/-5kb)">\n' > "$gene_hdr"

panel="$OUT/panel.pass.vcf.gz"
bcftools view -T "$bed" -f 'PASS,.' "$VCF" \
  | bcftools view -i 'GT="alt"' \
  | bcftools annotate -a "$bed" -h "$gene_hdr" -c CHROM,FROM,TO,INFO/MVA_GENE \
  | bcftools view -Oz -o "$panel"
bcftools index -t "$panel"

# ClinVar is NCBI-style (1,2,…,X,MT). Rename only the tiny panel VCF to match, annotate, rename back.
ann="$OUT/panel.clinvar.vcf.gz"
if [[ "$vcf_has_chr" -eq 1 ]]; then
  bcftools annotate --rename-chrs "$MAP_STRIP" "$panel" \
    | bcftools annotate -a "$CLINVAR" -c INFO/ALLELEID,INFO/CLNSIG,INFO/CLNREVSTAT,INFO/CLNDN,INFO/GENEINFO \
    | bcftools annotate --rename-chrs "$MAP_ADD" \
    | bcftools view -Oz -o "$ann"
else
  bcftools annotate -a "$CLINVAR" -c INFO/ALLELEID,INFO/CLNSIG,INFO/CLNREVSTAT,INFO/CLNDN,INFO/GENEINFO \
    "$panel" -Oz -o "$ann"
fi
bcftools index -t "$ann"

# Drop common variants only if a gnomAD AF tag is already in the VCF.
# Do NOT use INFO/AF: in a singleton GATK file that is 0.5/1.0, not population frequency.
# No VEP CSQ parsing here — Exomiser covers frequency genome-wide.
af_tag=$(bcftools view -h "$ann" | awk '
  /^##INFO=<ID=/ {
    tag=$0
    sub(/^##INFO=<ID=/, "", tag)
    sub(/,.*/, "", tag)
    low=tolower(tag)
    if (low ~ /gnomad/ && low ~ /af/) { print tag; exit }
  }')

freq="$OUT/panel.rare.vcf.gz"
if [[ -n "$af_tag" ]]; then
  echo "frequency filter: drop INFO/$af_tag > $MAX_AF (missing AF kept)" >&2
  bcftools view -e "$af_tag > $MAX_AF" "$ann" -Oz -o "$freq"
else
  echo "no gnomAD AF tag in VCF; skipping frequency filter" >&2
  cp "$ann" "$freq"
  cp "$ann.tbi" "$freq.tbi"
fi
if [[ ! -f "$freq.tbi" ]]; then
  bcftools index -t "$freq"
fi

raw="$OUT/candidates.raw.tsv"
bcftools query -H -f '%CHROM\t%POS\t%REF\t%ALT\t%INFO/MVA_GENE\t[%GT]\t%FILTER\t%INFO/CLNSIG\t%INFO/CLNREVSTAT\t%INFO/CLNDN\t%INFO/GENEINFO\n' \
  "$freq" > "$raw"

# Biallelic flag per gene: hom alt, or >=2 hets (possible compound het). No phase, so "possible".
awk -F'\t' -v OFS='\t' '
  BEGIN {
    print "chrom","pos","ref","alt","gene","gt","filter","clnsig","clnrevstat","clndn","clinvar_gene","biallelic"
  }
  $1 ~ /^#/ { next }
  {
    n++
    chrom[n]=$1; pos[n]=$2; ref[n]=$3; alt[n]=$4; gene[n]=$5; gt[n]=$6
    filt[n]=$7; sig[n]=$8; rev[n]=$9; dn[n]=$10; cg[n]=$11
    g=$5
    if (g == "." || g == "") next
    if ($6 ~ /(1\/1|1\|1)/) hom[g]++
    else if ($6 ~ /[1-9]/) het[g]++
  }
  END {
    for (i=1; i<=n; i++) {
      g=gene[i]
      flag="het_single"
      if (g=="." || g=="") flag="."
      else if (hom[g] >= 1) flag="homozygous"
      else if (het[g] >= 2) flag="possible_compound_het"
      else if (het[g] == 0 && hom[g] == 0) flag="."
      print chrom[i],pos[i],ref[i],alt[i],gene[i],gt[i],filt[i],sig[i],rev[i],dn[i],cg[i],flag
    }
  }
' "$raw" > "$OUT/candidates.tsv"

echo "$OUT/candidates.tsv"
