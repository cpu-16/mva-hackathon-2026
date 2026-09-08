#!/usr/bin/env bash
# One command that regenerates the Track 2 public-data figure and table, renders the worksheet from the
# machine-readable candidate table, checks every reported number against the results files, and builds
# the PDFs. Records what is missing instead of failing silently. Run from the analysis directory or
# from a checkout of the repository (paths differ; the script finds both layouts).
set -u
t0=$(date +%s)
cd "$(dirname "$0")/.."
if [ -d track2 ]; then REPORT=track2; BUILD=entrega/build_pdfs.sh; VERIF="analysis/verificar_afirmaciones.py"
else REPORT=report; BUILD=analysis/build_pdfs.sh; VERIF="analysis/verificar_afirmaciones.py --layout repo"; fi
status=0
step(){ echo; echo "### $(date -Is) $*"; }
need(){ command -v "$1" >/dev/null 2>&1 || { echo "MISSING dependency: $1"; status=1; return 1; }; }

step "dependencies"
for d in python3 pandoc pdfinfo pdftotext; do need $d && echo "ok $d $($d --version 2>&1 | head -1)"; done
python3 - <<'PY' || status=1
import importlib
for m in ("numpy","pandas","scipy","matplotlib","weasyprint","openpyxl"):
    try: importlib.import_module(m); print("ok python module", m)
    except Exception as e: print("MISSING python module", m, "-", e)
PY

step "1. DepMap follow-up: fig5 + tables from the public data (depmap/05_seguimiento.py)"
if [ -f depmap/raw/CRISPRGeneEffect.csv ] && [ -f depmap/raw/Repurposing_Extended_Primary_Matrix.csv ]; then
  ( cd depmap && /usr/bin/time -f "wall %e s, max RSS %M KiB" python3 05_seguimiento.py > /dev/null ) || status=1
  echo "regenerated depmap/fig5_seguimiento.png and resultados_seguimiento*.csv"
else
  echo "MISSING input: depmap/raw/ (DepMap 24Q4 figshare 27993248 + PRISM 24Q2 figshare 25917643, ~700 MB, not in the repository)"
  echo "-> fig5 and the tables are NOT regenerated; the committed copies are used"
fi

step "2. worksheet rendered from $REPORT/candidates.tsv"
python3 $REPORT/render_candidates.py || status=1

step "3. every reported number checked against the results files"
python3 $VERIF || { echo "VERIFIER FAILED"; status=1; }

step "4. PDFs"
if command -v pandoc >/dev/null && python3 -c "import weasyprint" 2>/dev/null; then
  bash $BUILD || status=1
else
  echo "SKIPPED: pandoc and/or weasyprint missing"
fi

step "done in $(( $(date +%s) - t0 )) s, exit status $status"
exit $status
