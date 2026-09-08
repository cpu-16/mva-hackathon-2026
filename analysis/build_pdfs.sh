#!/usr/bin/env bash
# Regenerate both submission PDFs from the corrected markdown and copy them into listo-para-enviar/.
# The Track 2 form accepts ONE file, so the methods description is appended as Appendix B.
set -euo pipefail
cd "$(dirname "$0")/.."
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# Track 2 methods -> appendix: drop its own title block, demote every heading one level.
sed '1,6d; s/^#/##/' entrega/methods_track2.md > "$TMP/appendix_b.md"
{ echo "## Appendix B — Methods description (Track 2 form)"; echo; cat "$TMP/appendix_b.md"; } > "$TMP/appb.md"

pdf() {  # pdf <out.pdf> <in.md>...
  local out="$1"; shift
  pandoc "$@" -f markdown -t html5 --standalone -o "$TMP/x.html" 2>/dev/null
  python3 -c "
from weasyprint import HTML, CSS
HTML('$TMP/x.html', base_url='track2').write_pdf('$out', stylesheets=[CSS('track2/report.css')])"
  echo "$out  $(pdfinfo "$out" | awk '/^Pages/{print $2}') pages"
}

pdf entrega/methods_track1.pdf entrega/methods_track1.md

# Track 2 = Part I (decision document) + Part II (full evidence: the full report with its family page,
# references, acknowledgement and data-availability sections removed, since Part I carries them) + Appendix B.
python3 - "$TMP" <<'PY'
import re, sys
tmp = sys.argv[1]
s = open("track2/REPORT_track2_EN.md", encoding="utf-8").read()
s = s[s.index("## Executive summary"):]                       # drop title block + family page
s = s[:s.index("## References")]                              # drop refs/ack/data availability (in Part I)
s = re.sub(r"^(#{2,6}) ", lambda m: "#" + m.group(1) + " ", s, flags=re.M)   # demote one level
head = ("# Part II — Full evidence\n\n*The complete report: every section at full length, with derivations, "
        "sources quoted verbatim, the correction history and every pre-registered analysis. Part I is the "
        "reading version; where the two differ in wording, this part carries the detail and Part I never "
        "claims more than this part supports. Section numbers match Part I.*\n\n")
open(f"{tmp}/part2.md", "w", encoding="utf-8").write(head + s)
PY
pdf track2/REPORT_track2.pdf track2/PART1_decision_document.md "$TMP/part2.md" "$TMP/appb.md"

cp entrega/methods_track1.pdf entrega/listo-para-enviar/ciberpty_track1_report.pdf
cp track2/REPORT_track2.pdf   entrega/listo-para-enviar/ciberpty_track2_report.pdf

# Stale-text guard: retracted wording that must not survive in the shipped PDFs.
# 0.4187 is deliberately NOT here — the write-up discloses the contaminated value on purpose.
# grep -q would exit early and SIGPIPE pdftotext, which pipefail then reads as "no match": use -c.
STALE='still running at the time of writing|about twelve weeks|growth inhibition through AMPK|and not optional|property of the alleles; the rank is not|clears the pharmacology|no feasible n rescues|two independent measurements agree'
fail=0
for f in entrega/listo-para-enviar/ciberpty_track*_report.pdf; do
  n=$(pdftotext "$f" - | grep -cE "$STALE" || true)
  [ "$n" -eq 0 ] || { echo "STALE TEXT ($n hits) STILL IN $f" >&2; fail=1; }
done
[ "$fail" -eq 0 ] || exit 1
echo "ok — both PDFs regenerated and free of the retracted wording"
