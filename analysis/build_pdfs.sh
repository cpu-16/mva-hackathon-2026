#!/usr/bin/env bash
# Regenerate both submission PDFs from the corrected markdown and copy them into listo-para-enviar/.
# The Track 2 form accepts ONE file, so the methods description is appended as Appendix B.
set -euo pipefail
cd "$(dirname "$0")/.."
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# Two layouts: the analysis directory (track2/, entrega/) and a checkout of the repository (report/, submission/).
if [ -d track2 ]; then
  T1MD=entrega/methods_track1.md; T1PDF=entrega/methods_track1.pdf; T2MD=entrega/methods_track2.md
  RPT=track2; T2PDF=track2/REPORT_track2.pdf; OUT=entrega/listo-para-enviar
else
  T1MD=submission/ciberpty_track1_report.md; T1PDF=submission/ciberpty_track1_report.pdf; T2MD=submission/ciberpty_track2_methods.md
  RPT=report; T2PDF=report/REPORT_track2.pdf; OUT=submission
fi
mkdir -p "$OUT"

# Track 2 methods -> appendix: drop its own title block, demote every heading one level.
sed '1,6d; s/^#/##/' "$T2MD" > "$TMP/appendix_b.md"
{ echo "## Appendix B — Methods description (Track 2 form)"; echo; cat "$TMP/appendix_b.md"; } > "$TMP/appb.md"

pdf() {  # pdf <out.pdf> <in.md>...
  local out="$1"; shift
  pandoc "$@" -f markdown -t html5 --standalone -o "$TMP/x.html" 2>/dev/null
  python3 -c "
from weasyprint import HTML, CSS
HTML('$TMP/x.html', base_url='$RPT').write_pdf('$out', stylesheets=[CSS('$RPT/report.css')])"
  echo "$out  $(pdfinfo "$out" | awk '/^Pages/{print $2}') pages"
}

pdf "$T1PDF" "$T1MD"

# Track 2 = Part I (decision document) + Part II (full evidence: the full report with its family page,
# references, acknowledgement and data-availability sections removed, since Part I carries them) + Appendix B.
python3 - "$TMP" <<'PY'
import re, sys
tmp = sys.argv[1]
import os
s = open(("track2" if os.path.isdir("track2") else "report") + "/REPORT_track2_EN.md", encoding="utf-8").read()
s = s[s.index("## Executive summary"):]                       # drop title block + family page
s = s[:s.index("## References")]                              # drop refs/ack/data availability (in Part I)
s = re.sub(r"^(#{2,6}) ", lambda m: "#" + m.group(1) + " ", s, flags=re.M)   # demote one level
head = ("# Part II — Full evidence\n\n*The complete report: every section at full length, with derivations, "
        "sources quoted verbatim, the correction history and every pre-registered analysis. Part I is the "
        "reading version; where the two differ in wording, this part carries the detail and Part I never "
        "claims more than this part supports. Section numbers match Part I.*\n\n")
open(f"{tmp}/part2.md", "w", encoding="utf-8").write(head + s)
PY
pdf "$T2PDF" "$RPT/PART1_decision_document.md" "$TMP/part2.md" "$TMP/appb.md"

cp "$T1PDF" "$OUT/ciberpty_track1_report.pdf"
cp "$T2PDF" "$OUT/ciberpty_track2_report.pdf"

# Stale-text guard: retracted wording that must not survive in the shipped PDFs.
# 0.4187 is deliberately NOT here — the write-up discloses the contaminated value on purpose.
# grep -q would exit early and SIGPIPE pdftotext, which pipefail then reads as "no match": use -c.
STALE='still running at the time of writing|about twelve weeks|growth inhibition through AMPK|and not optional|property of the alleles; the rank is not|clears the pharmacology|no feasible n rescues|two independent measurements agree'
fail=0
for f in "$OUT"/ciberpty_track*_report.pdf; do
  n=$(pdftotext "$f" - | grep -cE "$STALE" || true)
  [ "$n" -eq 0 ] || { echo "STALE TEXT ($n hits) STILL IN $f" >&2; fail=1; }
done
[ "$fail" -eq 0 ] || exit 1
echo "ok — both PDFs regenerated and free of the retracted wording"
