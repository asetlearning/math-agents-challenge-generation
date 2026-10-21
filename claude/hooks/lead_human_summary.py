#!/usr/bin/env python3
"""Daily summary of the human <-> Lead transcript.

Created by: Alex Myasnikov
Date: October 21, 2026

Days are processed in date order, and each run also updates a living
open-questions list at the top of the record.

Reads the day sections (`## YYYY-MM-DD`) of
    <vault>/Agents/<handle>/Lead/transcripts/lead-human-YYYY-MM.md
written by lead_human_transcript.py, and appends a short bullet summary of each
completed day to
    <vault>/Agents/<handle>/Lead/transcripts/lead-human-summaries.md
(private: the Agents/ tree is gitignored). Each day is summarized once: a day
already in the summaries file is skipped. Run it once a day (cron); it catches
up on missed days, back to --days days ago.

It only reads the transcript; Lead's Stop hook keeps the transcript current.

Usage:
  lead_human_summary.py [--vault <path>] [--handle <name>] [--days N]
                        [--date YYYY-MM-DD] [--model <model>] [--dry-run]

  --days N      summarize completed days from N days ago up to yesterday (default 3)
  --date D      summarize this one day only (also today; redo with --force; the
                open-questions list is updated from whatever it holds now)
  --force       replace an existing summary of --date
  --model M     model for `claude -p` (default: opus)
  --dry-run     print what would be summarized, call nothing
"""
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from maestri_message_log import handle_from_claude_md, opt  # noqa: E402

DAY_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$", re.M)
SUMMARY_FILE = "lead-human-summaries.md"
CLAUDE = os.environ.get("CLAUDE_CLI") or os.path.expanduser("~/.local/bin/claude")

SYSTEM_PROMPT = """You keep the decision record of a research project, written from the daily conversation between the \
human owner and the Lead agent of a multi-agent team (other agents' reports appear as collapsed callouts). The owner can \
open the full transcript for detail, so this record keeps only what matters at the level of the project.

You get (1) the current open-questions list and (2) one day's transcript. Output two parts, separated by a line that is \
exactly ===OPEN QUESTIONS===.

PART 1, the day's record. Sections in this order, each omitted if empty:

### Decisions and ideas
Main decisions about the project's direction and method, and conceptual ideas adopted or rejected: what measure drives \
the search, which construction or approach is pursued or dropped, new definitions and naming, success criteria, rules for \
how the work is done. Say why in a few words when the transcript gives the reason. Example style: "Use peaks, not areas, \
as the main measure for driving generation of hard examples." / "New hardness definition: solver resilience (levels S1-each, \
S2-chain)."

### Significant results
What was established, proved, confirmed or refuted, and what failed, stated as a finding. Example style: "Deep areas do \
not improve hardness: kbmag breaks every generated candidate." Include a number only when it is the finding itself.

### Significant code changes
New capabilities or changed logic, described by what they do and why, never as commits. Example style: "Added \
certificate extraction from the kbmag rewriting path, so more candidates can carry an R7 certificate." No hashes, \
branches, PR numbers, test counts, bug fixes or job files unless a fix changed a result.

Leave out: job ids, hashes, budgets, CPU hours, per-word or per-component details, logistics, reviews and approvals as \
events, agent relays, status updates, and anything that only says work progressed. HARD LIMITS: at most 6 bullets per \
section, flat (never sub-bullets), each at most 30 words; one bullet per theme; when there are more candidates, keep \
the most consequential for the project's direction. A quiet day may have 1-3 bullets in total. Use only what the \
transcript states; never invent. Keep project terms as written (T-numbers, level names). Refer to agents by role, \
never as he or she. No preamble or closing remark.

PART 2, the full updated open-questions list, in two sections:
### Open
- [opened YYYY-MM-DD] the question
### Resolved
- [opened YYYY-MM-DD, resolved YYYY-MM-DD] the question: the answer in a few words
Open questions are substantive research or design questions and open owner decisions on direction (for example: does \
method X reach the goal, which measure to use, is result Y real). Not logistics (pushes, commits, PDFs, budgets, \
reminders). Carry every item of the current list forward; add new questions raised this day; move an item to Resolved only \
when the day's transcript answers it; reword an item only to sharpen it. Each item at most 25 words, no supporting \
detail. Keep at most 10 open items: merge duplicates, and drop narrow technical items in favour of the questions that \
decide the project's direction. Keep the 8 most recent resolved items."""


def day_text(out_dir, day):
    """All sections of the transcript headed `## day` (a day can be split by interleaved sessions)."""
    path = os.path.join(out_dir, "lead-human-%s.md" % day[:7])
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return ""
    parts = DAY_RE.split(text)  # [pre, d1, body1, d2, body2, ...]
    return "\n".join(parts[i + 1] for i in range(1, len(parts) - 1, 2) if parts[i] == day).strip()


def summarized_days(summary_path):
    try:
        with open(summary_path, encoding="utf-8") as f:
            return set(DAY_RE.findall(f.read()))
    except OSError:
        return set()


def summarize(day, text, questions, model):
    prompt = "Current open-questions list:\n\n%s\n\nTranscript of %s:\n\n%s" % (questions or "(empty)", day, text)
    run = subprocess.run(
        [CLAUDE, "-p", "--model", model, "--system-prompt", SYSTEM_PROMPT, "--tools", "",
         "--no-session-persistence", "--output-format", "text"],
        input=prompt, capture_output=True, text=True, timeout=1800, cwd=os.path.expanduser("~"))
    if run.returncode != 0 or not run.stdout.strip():
        raise RuntimeError("claude -p failed (%d): %s" % (run.returncode, run.stderr.strip()[:500]))
    out = run.stdout.strip()
    if "===OPEN QUESTIONS===" not in out:
        raise RuntimeError("no ===OPEN QUESTIONS=== separator in the summary")
    body, questions = out.split("===OPEN QUESTIONS===", 1)
    return body.strip(), questions.strip()


HEAD = "# Lead ↔ human: decision record\n\nOne section per day, plus a living open-questions list; the full record is in `lead-human-YYYY-MM.md`.\n\n"
QUESTIONS_RE = re.compile(r"^## Open questions\s*\n(.*?)(?=^## \d{4}-\d{2}-\d{2}\s*$|\Z)", re.M | re.S)


def current_questions(summary_path):
    try:
        with open(summary_path, encoding="utf-8") as f:
            m = QUESTIONS_RE.search(f.read())
    except OSError:
        return ""
    return re.sub(r"^_.*_\s*\n", "", m.group(1).strip()) if m else ""


def write_summary(summary_path, day, body, questions, model, force):
    block = "## %s\n\n_Summary of `lead-human-%s.md` § %s · %s · %s_\n\n%s\n\n" % (
        day, day[:7], day, model, datetime.now().strftime("%Y-%m-%d %H:%M"), body)
    try:
        with open(summary_path, encoding="utf-8") as f:
            old = f.read()
    except OSError:
        old = HEAD
    if force and day in DAY_RE.findall(old):
        # drop the old section of this day
        old = re.sub(r"^## %s\s*\n.*?(?=^## \d{4}-\d{2}-\d{2}\s*$|\Z)" % re.escape(day), "", old, flags=re.M | re.S)
    # keep the days in order
    sections = re.split(r"(?=^## \d{4}-\d{2}-\d{2}\s*$)", old, flags=re.M)
    days = [s for s in sections[1:] if s.strip()]
    head = HEAD + "## Open questions\n\n_Updated with %s._\n\n%s\n\n" % (day, questions)
    days.append(block)
    days.sort(key=lambda s: DAY_RE.search(s).group(1))
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(head + "".join(s.rstrip("\n") + "\n\n" for s in days))


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    vault = opt(argv, "--vault") or os.path.normpath(os.path.join(here, "..", "..", "obsidian"))
    handle = opt(argv, "--handle") or os.environ.get("MATH_VAULT_HANDLE") or handle_from_claude_md()
    model = opt(argv, "--model") or "opus"
    dry = "--dry-run" in argv
    force = "--force" in argv
    out_dir = os.path.join(vault, "Agents", handle, "Lead", "transcripts")
    summary_path = os.path.join(out_dir, SUMMARY_FILE)

    if opt(argv, "--date"):
        days = [opt(argv, "--date")]
    else:
        n = int(opt(argv, "--days") or 3)
        days = [(date.today() - timedelta(days=k)).isoformat() for k in range(n, 0, -1)]
    done = summarized_days(summary_path)
    for day in days:
        if day in done and not (force and opt(argv, "--date")):
            continue
        text = day_text(out_dir, day)
        if not text:
            continue
        if dry:
            print("%s: %d chars to summarize" % (day, len(text)))
            continue
        try:
            body, questions = summarize(day, text, current_questions(summary_path), model)
        except (RuntimeError, OSError, subprocess.SubprocessError) as e:
            print("%s: %s" % (day, e), file=sys.stderr)
            continue
        write_summary(summary_path, day, body, questions, model, force)
        print("%s: summarized (%d chars)" % (day, len(body)))


if __name__ == "__main__":
    main(sys.argv[1:])
