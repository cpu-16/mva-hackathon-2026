#!/usr/bin/env python3
"""Render the five-filter worksheet in both report files FROM candidates.tsv, so the table a judge
reads in the PDF is the machine-readable table, not a hand-copied one.

usage: render_candidates.py            # rewrite the worksheet tables in place (idempotent)
       render_candidates.py --check    # exit 1 if either report's table differs from the TSV rendering
"""
import csv, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = f"{HERE}/candidates.tsv"
TARGETS = [f"{HERE}/PART1_decision_document.md", f"{HERE}/REPORT_track2_EN.md"]
HEADER = "| Candidate | F1 approved | F2 mechanism | F3 exposure | F4 safe in *this* patient | F5 margin excluded | Verdict |"
SEP = "|---|---|---|---|---|---|---|"
STATUS = {"pass": "pass", "fail": "**fail**", "untested": "untested", "not_evaluable": "not evaluable",
          "not_reached": "not reached", "not_excluded": "not excluded", "unresolved": "exposure unresolved"}

def cell(s):
    return STATUS.get(s, s).replace("_", " ")

def render(compact):
    """compact=True (Part I): statuses and verdict only, one page. compact=False (Part II): with the
    filter-3 model context and the reason, i.e. every column of the TSV a reader needs."""
    rows = list(csv.DictReader(open(TSV, encoding="utf-8"), delimiter="\t"))
    out = [HEADER, SEP]
    for r in rows:
        name = r["candidate"].replace("_", " ")
        verdict = r["verdict"].replace("_", " ").replace(";", "; ")
        f3 = cell(r['filter3_exposure']) if compact else f"{cell(r['filter3_exposure'])} — {r['model_context_for_filter3']}"
        v = f"**{verdict}**" if compact else f"**{verdict}** — {r['reason']}"
        out.append(f"| **{name}** | {cell(r['filter1_approved'])} | {cell(r['filter2_mechanism'])} | {f3} | "
                   f"{cell(r['filter4_safety_this_child'])} | {cell(r['filter5_direction_of_effect'])} | {v} |")
    out.append("| *(your candidate)* | | | | | | |")
    return "\n".join(out)

BLOCK = re.compile(r"\| Candidate \| (?:1\. Approved\?|F1 approved).*?\n(?:\|.*\n)+?\| \*\(your candidate\)\* \|[^\n]*\n(?:\| \*\(your candidate\)\* \|[^\n]*\n)?", re.S)

def main():
    check = "--check" in sys.argv
    bad = 0
    for path in TARGETS:
        table = render(compact=path.endswith("PART1_decision_document.md")) + "\n"
        s = open(path, encoding="utf-8").read()
        m = BLOCK.search(s)
        if not m:
            print(f"{path}: worksheet table not found"); bad += 1; continue
        if m.group(0) == table:
            print(f"{path}: worksheet matches candidates.tsv"); continue
        if check:
            print(f"{path}: worksheet DIFFERS from candidates.tsv"); bad += 1; continue
        s = s[:m.start()] + table + s[m.end():]
        open(path, "w", encoding="utf-8").write(s); print(f"{path}: worksheet rewritten from candidates.tsv")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
