#!/usr/bin/env python3
"""Extract the open-problem corpus from the Kourovka Notebook No. 20 (2022) PDF.

Input : the PDF (uses `pdftotext -layout`)
Output: kourovka-20-corpus.jsonl  (one JSON object per open problem)
        kourovka-20-index.md      (human-readable index table)

Only the MAIN part (pages 5-163 of the printed doc) is parsed. The
"Archive of Solved Problems" section is deliberately excluded.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import os

USAGE = """usage: kourovka-extract.py [PDF] [OUTDIR]

  PDF     path to the Kourovka Notebook PDF.
          Defaults to $KOUROVKA_PDF, set by _meta/agents/Kourovka/paths.env.
  OUTDIR  where to write the corpus.
          Defaults to $KOUROVKA_CORPUS_DIR, else ./kourovka-corpus.

  source "_meta/agents/Kourovka/paths.env"
  python3 _meta/scripts/kourovka-extract.py \\
      "$KOUROVKA_PDF" "Research/Group theory/Open problems/Kourovka/corpus"
"""

PDF = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("KOUROVKA_PDF", "")
if not PDF:
    sys.exit(USAGE + "\nerror: no PDF given and $KOUROVKA_PDF is not set.")
if not Path(PDF).is_file():
    sys.exit(f"error: PDF not found: {PDF}")

OUTDIR = Path(
    sys.argv[2]
    if len(sys.argv) > 2
    else os.environ.get("KOUROVKA_CORPUS_DIR", "kourovka-corpus")
)
OUTDIR.mkdir(parents=True, exist_ok=True)

# Whose name goes in the generated notes' frontmatter. The operator sets this;
# it is never guessed from the filesystem.
AUTHOR = os.environ.get("KOUROVKA_AUTHOR", "<operator>")

ISSUE_YEAR = {
    1: 1965, 2: 1966, 3: 1969, 4: 1973, 5: 1976, 6: 1978, 7: 1980,
    8: 1982, 9: 1984, 10: 1986, 11: 1990, 12: 1992, 13: 1995, 14: 1999,
    15: 2002, 16: 2006, 17: 2010, 18: 2014, 19: 2018, 20: 2022,
}

# --- 1. text extraction -------------------------------------------------
raw = subprocess.run(
    ["pdftotext", "-layout", PDF, "-"], capture_output=True, text=True, check=True
).stdout
pages = raw.split("\f")

# main part = from "Problems from the 1st Issue" page up to (not incl.)
# the "Archive of solved problems" divider page.
start = next(i for i, p in enumerate(pages)
             if "Problems from the 1st Issue" in p and ". . ." not in p)
end = next(i for i, p in enumerate(pages)
           if i > start and any(ln.strip().lower() == "archive of solved problems"
                                for ln in p.split("\n")))
main = pages[start:end]
sys.stderr.write(f"main part: pdf page idx {start}..{end - 1} ({len(main)} pages)\n")

# --- 2. line stream, stripping running heads/feet -----------------------
HEAD = re.compile(r"^\s*(\d{1,3}\s+)?(New Problems \(\d{1,2}(st|nd|rd|th) issue, \d{4}\)"
                  r"|\d{1,2}(st|nd|rd|th) Issue \(\d{4}\))(\s+\d{1,3})?\s*$", re.I)
SECTION = re.compile(r"^\s*(?:Problems from the (\d{1,2})(?:st|nd|rd|th) Issue"
                     r"|New Problems\s*$)")
PROB = re.compile(r"^(?P<star>∗\s*)?(?P<iss>\d{1,2})\.(?P<num>\d{1,3})\.(?P<rest>\s|$)")

lines = []          # (issue_of_current_section, printed_page, text)
last_printed = None
cur_issue = None
for pidx, page in enumerate(main):
    plines = page.split("\n")
    # printed page number: first or last non-empty line usually carries it
    printed = None
    for probe in (plines[0] if plines else "", plines[-1] if plines else ""):
        m = re.search(r"\b(\d{1,3})\b", probe or "")
        if m and HEAD.match(probe or ""):
            printed = int(m.group(1))
            break
    if printed is None:
        printed = last_printed + 1 if last_printed else None
    last_printed = printed or last_printed
    for ln in plines:
        s = SECTION.match(ln)
        if s:
            cur_issue = int(s.group(1)) if s.group(1) else 20
            continue
        if HEAD.match(ln):
            continue
        lines.append((cur_issue, printed, ln))

# --- 3. split into problems --------------------------------------------
problems = []
cur = None
for issue, printed, ln in lines:
    m = PROB.match(ln)
    if m and issue is not None and int(m.group("iss")) == issue:
        if cur:
            problems.append(cur)
        cur = {
            "id": f"{m.group('iss')}.{m.group('num')}",
            "issue": int(m.group("iss")),
            "year": ISSUE_YEAR[int(m.group("iss"))],
            "page": printed,
            "answered": bool(m.group("star")),
            "_lines": [ln[m.end("num") + 1:]],
        }
    elif cur is not None:
        cur["_lines"].append(ln)
if cur:
    problems.append(cur)

# --- 4. clean each problem ---------------------------------------------
NAME = re.compile(
    r"^(?:[A-ZÀ-Þ][a-z]?\.\s?){1,3}[A-ZÀ-Þ][\w’'\-]+"
    r"(?:\s*,\s*(?:[A-ZÀ-Þ][a-z]?\.\s?){1,3}[A-ZÀ-Þ][\w’'\-]+)*$"
)


def pop_proposers(body):
    """Right-aligned attribution lines sit at the tail, possibly sharing a
    physical line with the last sentence (>=4 spaces of gutter)."""
    names = []
    while body:
        last = body[-1].rstrip()
        if not last:
            body.pop()
            continue
        stripped = last.strip()
        # whole line is a right-aligned name
        if (len(last) - len(last.lstrip())) >= 20 and NAME.match(stripped):
            names.insert(0, stripped)
            body.pop()
            continue
        # name shares the line with trailing prose, split on a wide gutter
        parts = re.split(r"\s{3,}", last.rstrip())
        if len(parts) >= 2 and NAME.match(parts[-1].strip()):
            names.insert(0, parts[-1].strip())
            body[-1] = "    ".join(parts[:-1])
            continue
        break
    return names


def finish(p):
    body = p.pop("_lines")
    proposers = pop_proposers(body)
    text = "\n".join(body)
    if re.search(r"^\s*∗\s", text, re.M):
        p["answered"] = True
    p["has_editor_comment"] = bool(re.search(r"[Ee]ditors?[’\']\s?comment", text))
    p["has_later_comment"] = bool(re.search(r"Comment of \d{4}", text))
    paras, buf = [], []
    for ln in text.split("\n"):
        if ln.strip():
            buf.append(" ".join(ln.split()))
        elif buf:
            paras.append(" ".join(buf))
            buf = []
    if buf:
        paras.append(" ".join(buf))
    p["statement"] = "\n\n".join(paras).strip()
    out = []
    for pr in proposers:
        out.extend(x.strip() for x in pr.split(",") if x.strip())
    p["proposers"] = out
    p["chars"] = len(p["statement"])
    return p


problems = [finish(p) for p in problems]

# --- 4b. second pass: recover names glued to fully-justified last lines --
# Build a surname lexicon from the attributions already recovered, then use
# it to strip trailing "A. B. Surname" runs that had no wide gutter.
LEX = set()
_idx_start = next((i for i, pg in enumerate(pages)
                   if i > end and any(ln.strip().lower() == "index of names"
                                      for ln in pg.split("\n"))), None)
if _idx_start is not None:
    _surname = re.compile(
        r"\b([A-ZÀ-Þ][\w\u00C0-\u024F\u2019'\-]{1,})\s+(?:[A-ZÀ-Þ][a-z]?\.\s*){1,3}(?=\d|A:)")
    for pg in pages[_idx_start:]:
        for ln in pg.split("\n"):
            for m in _surname.finditer(ln):
                LEX.add(m.group(1))
    sys.stderr.write(f"index-of-names lexicon: {len(LEX)} surnames\n")
for p in problems:
    for n in p["proposers"]:
        LEX.add(n.split()[-1])
TAIL = re.compile(
    r"\s+((?:[A-ZÀ-Þ][a-z]?\.\s?){1,3}[A-ZÀ-Þ][\w\u2019'\-]+"
    r"(?:\s*,\s*(?:[A-ZÀ-Þ][a-z]?\.\s?){1,3}[A-ZÀ-Þ][\w\u2019'\-]+)*)$"
)
recovered = 0
for p in problems:
    if p["proposers"] or not p["statement"]:
        continue
    m = TAIL.search(p["statement"])
    if not m:
        continue
    cand = [x.strip() for x in m.group(1).split(",") if x.strip()]
    if all(c.split()[-1] in LEX for c in cand):
        p["statement"] = p["statement"][: m.start()].rstrip()
        p["proposers"] = cand
        p["chars"] = len(p["statement"])
        recovered += 1
sys.stderr.write(f"proposers recovered in 2nd pass: {recovered}\n")

# dedupe (same id can appear only once in the main part)
seen, uniq = set(), []
for p in problems:
    if p["id"] in seen:
        sys.stderr.write(f"DUP {p['id']}\n")
        continue
    seen.add(p["id"])
    uniq.append(p)
problems = uniq

# --- 5. write ------------------------------------------------------------
def sortkey(p):
    return (p["issue"], p["id"].split(".")[1].zfill(4))


problems.sort(key=sortkey)

jsonl = OUTDIR / "kourovka-20-corpus.jsonl"
with jsonl.open("w", encoding="utf-8") as f:
    for p in problems:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

open_only = [p for p in problems if not p["answered"]]

by_issue = {}
for p in problems:
    by_issue.setdefault(p["issue"], []).append(p)

# per-issue readable notes
STAMP = subprocess.run(["date", "+%Y-%m-%d"], capture_output=True, text=True).stdout.strip()
for iss in sorted(by_issue):
    ps = by_issue[iss]
    yr = ISSUE_YEAR[iss]
    label = "New Problems (20th Issue)" if iss == 20 else f"{iss}th Issue"
    fn = OUTDIR / f"kourovka-issue-{iss:02d}-{yr}.md"
    out = [
        "---",
        f'title: "Kourovka Notebook No. 20 — Issue {iss} ({yr}) open problems"',
        "type: problem-corpus",
        f"issue: {iss}",
        f"year: {yr}",
        f"problem_count: {len(ps)}",
        f'answered_count: {sum(1 for x in ps if x["answered"])}',
        'source: "Kourovka Notebook No. 20 (2022), arXiv:1401.0300v23"',
        f'source_pdf: "{Path(PDF).name}"',
        f'extracted: "{STAMP}"',
        'extractor: "_meta/scripts/kourovka-extract.py"',
        f"author: {AUTHOR}",
        "tags:",
        "  - domain/group-theory",
        "  - topic/kourovka",
        "  - topic/open-problems",
        "  - project/kourovka",
        "  - status/reference",
        "  - reference",
        "---",
        "",
        f"# Kourovka No. 20 — {label}, {yr}",
        "",
        "> [!warning] Verbatim machine extraction",
        "> Generated by `_meta/scripts/kourovka-extract.py` from the source PDF via",
        "> `pdftotext -layout`. Mathematical notation is plain-text-mangled",
        "> (`hx, yi` = `⟨x, y⟩`, `⩽` etc.). **Always re-read the statement in the",
        "> original PDF before doing serious work on a problem.** Problems marked",
        "> `[ANSWERED]` carry an editors' `∗` answer note and are NOT open.",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Problems in this issue (main part) | {len(ps)} |",
        f'| Of which flagged answered | {sum(1 for x in ps if x["answered"])} |',
        f'| Genuinely open | {sum(1 for x in ps if not x["answered"])} |',
        "",
        "---",
        "",
    ]
    for x in ps:
        flag = " `[ANSWERED]`" if x["answered"] else ""
        who = ", ".join(x["proposers"]) if x["proposers"] else "_(see statement)_"
        out.append(f'## {x["id"]}{flag}')
        out.append("")
        out.append(f'*Issue {x["issue"]} ({x["year"]}) · printed p. {x["page"]} · proposed by {who}*')
        out.append("")
        out.append(x["statement"])
        out.append("")
    fn.write_text("\n".join(out), encoding="utf-8")
sys.stderr.write(f"wrote {len(by_issue)} per-issue notes\n")

sys.stderr.write(f"\ntotal parsed        : {len(problems)}\n")
sys.stderr.write(f"flagged answered (∗): {len(problems) - len(open_only)}\n")
sys.stderr.write(f"genuinely open      : {len(open_only)}\n")
for i in sorted(by_issue):
    n = len(by_issue[i])
    a = sum(1 for p in by_issue[i] if p["answered"])
    sys.stderr.write(f"  issue {i:2d} ({ISSUE_YEAR[i]}): {n:4d}  (answered {a})\n")
sys.stderr.write(f"\nwrote {jsonl}\n")
