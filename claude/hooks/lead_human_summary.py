#!/usr/bin/env python3
"""Daily summary of the human <-> Lead transcript.

Created by: Alex Myasnikov
Date: October 21, 2026

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
  --date D      summarize this one day only (also today; redo with --force)
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

SYSTEM_PROMPT = """You summarize one day of a research project's conversation between the human owner and the Lead agent \
(project lead of a multi-agent team). The input is that day's transcript: human messages, Lead replies, and reports from \
other agents (Developer, Validator, Math Expert, Experimenter, Researcher) in collapsed callouts.

Write a concise, precise summary in Markdown bullets, for the owner, who can open the full transcript for detail. Sections, \
in this order, each omitted if empty:

### Results
Positive and negative results alike: what was found, measured, confirmed or refuted, with the key numbers, job ids and \
verdicts (CONFIRMED / NOT READY / ...). Say plainly when something failed or was ruled out.

### Approved
Decisions and approaches approved that day, and by whom (owner, or Lead under delegation): plans, budgets, rules, names, \
merges. One bullet each.

### Code changes
Main commits and merges: repo, branch, short hash, what changed in a few words. Skip trivial edits.

### Open
At most 3 bullets: what is waiting on the owner at the end of the day. Omit if nothing.

Rules: flat bullets only (no sub-bullets), each at most about 25 words; merge related items into one bullet; drop \
intermediate steps, fixed bugs that did not change a result, and routine relays between agents. No preamble, no closing \
remark, no headings other than the ones above. Use only facts stated in the transcript; never guess numbers or hashes. \
Keep identifiers (T-028, job ids, hashes, level names) exactly as written. Define nothing; the reader knows the project. \
At most 25 bullets in total; fewer on a quiet day."""


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


def summarize(day, text, model):
    prompt = "Transcript of %s:\n\n%s" % (day, text)
    run = subprocess.run(
        [CLAUDE, "-p", "--model", model, "--system-prompt", SYSTEM_PROMPT, "--tools", "",
         "--no-session-persistence", "--output-format", "text"],
        input=prompt, capture_output=True, text=True, timeout=1800, cwd=os.path.expanduser("~"))
    if run.returncode != 0 or not run.stdout.strip():
        raise RuntimeError("claude -p failed (%d): %s" % (run.returncode, run.stderr.strip()[:500]))
    return run.stdout.strip()


def write_summary(summary_path, day, body, model, force):
    block = "## %s\n\n_Summary of `lead-human-%s.md` § %s · %s · %s_\n\n%s\n\n" % (
        day, day[:7], day, model, datetime.now().strftime("%Y-%m-%d %H:%M"), body)
    try:
        with open(summary_path, encoding="utf-8") as f:
            old = f.read()
    except OSError:
        old = "# Lead ↔ human: daily summaries\n\nOne section per day; the full record is in `lead-human-YYYY-MM.md`.\n\n"
    if force and day in DAY_RE.findall(old):
        # drop the old section of this day
        old = re.sub(r"^## %s\s*\n.*?(?=^## \d{4}-\d{2}-\d{2}\s*$|\Z)" % re.escape(day), "", old, flags=re.M | re.S)
    # keep the days in order
    sections = re.split(r"(?=^## \d{4}-\d{2}-\d{2}\s*$)", old, flags=re.M)
    head, days = sections[0], [s for s in sections[1:] if s.strip()]
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
            body = summarize(day, text, model)
        except (RuntimeError, OSError, subprocess.SubprocessError) as e:
            print("%s: %s" % (day, e), file=sys.stderr)
            continue
        write_summary(summary_path, day, body, model, force)
        print("%s: summarized (%d chars)" % (day, len(body)))


if __name__ == "__main__":
    main(sys.argv[1:])
