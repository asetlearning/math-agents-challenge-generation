---
title: Kourovka restart — migrating to revision 2
author: shared
tags:
  - domain/group-theory
  - project/kourovka
  - type/runbook
created: 2026-08-20
status: status/active
---

# Kourovka restart — migrating to revision 2

The prompts were rewritten after the August 2026 campaign closed 0 of 16 problems.
See [[Experiments/Kourovka/_post-mortem-2026-08]] for why. This note is the
migration: what to hand an agent, and what you launch yourself afterwards.

> [!warning] Do not just relaunch the crew on the old board
> The previous run's board carries problems in states (`PARK_RECOMMENDED`,
> `STRATEGY_EXHAUSTED`) that no longer exist in the protocol, and three of its
> selections were problems already solved in the literature. Run the migration
> below first.

---

## Part 1 — Paste this to a setup agent

Open your **WSL2 / Ubuntu** terminal — not PowerShell, not Git Bash — `cd` to the
vault (`/mnt/c/Users/<you>/Documents/Obsidian/Math/obsidian` or wherever it lives),
start a Claude Code or codex session there, and paste everything in the block. It
does housekeeping only; it does **not** start the crew.

> [!note] Everything here is Linux-side
> Obsidian stays a normal Windows app on the same folder. The crew only ever runs
> inside WSL2, because `codex --sandbox workspace-write` needs the Linux sandbox —
> that sandbox is what keeps six autonomous agents from writing outside the vault.
> If WSL2 is genuinely unavailable, see §A of [[kourovka-crew-setup]] for the Git
> Bash fallback, but you lose the sandbox.

```
You are doing a one-time migration of the Kourovka crew to prompt revision 2.
Work at the vault root. Do housekeeping only — do NOT start any crew agent, do
NOT select problems, do NOT spawn anything.

Do these in order and stop at the end with a short report.

1. CONFIRM REVISION 2 IS PRESENT
   Read the frontmatter of _meta/agents/Kourovka/_common-kourovka.md and confirm
   it says `revision: 2`. If it says anything else, stop and tell me — the pull
   did not land and nothing below is safe to do.

2. CHECK rtk
   This is Ubuntu under WSL2, so install from the script, not Homebrew.
   Run `rtk --version` and `rtk gain`.
   - If `rtk` is not found:
       curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
     That installs to ~/.local/bin. Confirm it is on PATH; if not, append
       export PATH="$HOME/.local/bin:$PATH"
     to ~/.bashrc and re-source it. Then verify with `which rtk`.
     (Fallback if the script fails: `cargo install --git https://github.com/rtk-ai/rtk`.)
   - If `rtk --version` works but `rtk gain` errors with an unknown subcommand,
     STOP. A different tool called rtk (Rust Type Kit) is installed and shadowing
     it. Tell me; do not try to work around it.
   Install the Linux binary only. A Windows-side rtk.exe on PATH does not count and
   will confuse things — if `which rtk` points anywhere under /mnt/c, say so.
   Do not run `rtk init` for this session.

3. CHECK paths.env
   Run:
     source "_meta/agents/Kourovka/paths.env"
     echo "$KOUROVKA_VAULT" ; echo "$KOUROVKA_PDF" ; echo "$KOUROVKA_PAPERS"
     kv_now ; kv_deadline 3
   It must print no warnings, all three paths must exist, and kv_deadline must be
   exactly 3 hours after kv_now. If the deadline is wrong, the `date` variant
   detection is off — report it and stop. Do not hand-write timestamps.
   All three paths must be POSIX and start with /mnt/c (or /home). If any of them
   looks like C:\Users\... then a Windows path got reintroduced into paths.env —
   report it and stop, because every deadline and every --add-dir depends on it.

4. CHECK THE MATH TOOLING
   Check whether GAP is installed and working, inside WSL:
     which gap
     echo 'Print(NrSmallGroups(64), "\n"); QUIT;' | timeout 60 gap -q
   It should print 267. Report the result either way. Revision 2 requires Lead to
   verify tooling at problem-selection time, so I need to know now if GAP is
   missing. Do not install it without asking me.
   If GAP is missing, also check whether the SmallGroups library would be there
   once installed — `apt show gap-character-tables gap-small-groups` — and tell me,
   because bare GAP without SmallGroups is useless for the enumeration-first rule.

5. ARCHIVE THE OLD CAMPAIGN
   Move, do not delete:
     Agents/Kourovka/board   -> Agents/Kourovka/_archive-2026-08/board
     Agents/Kourovka/bus     -> Agents/Kourovka/_archive-2026-08/bus
     Agents/Kourovka/roster  -> Agents/Kourovka/_archive-2026-08/roster
     Agents/Kourovka/problems-> Agents/Kourovka/_archive-2026-08/problems
   Then recreate empty:
     Agents/Kourovka/board/
     Agents/Kourovka/bus/inbox/{Lead,Validator,MathExpert}/
     Agents/Kourovka/bus/archive/
     Agents/Kourovka/roster/
     Agents/Kourovka/problems/
   Write Agents/Kourovka/_archive-2026-08/README.md saying what was archived, on
   what date, and that it is the campaign analysed in the post-mortem.

6. SMOKE-TEST THE SCAFFOLD SCRIPT
   Run:
     bash _meta/scripts/kourovka-new-experiment.sh 99.999 smoke-test
   Confirm it created Experiments/Kourovka/99.999-smoke-test/ with _experiment.md
   plus methodology/, results/ and data/, that _experiment.md has valid
   frontmatter and no leftover <ID> or <slug> placeholders, and that the
   section-12 rubric was stripped. Then delete that directory — it is a test.
   If the script is not executable, report that rather than chmod-ing it.

7. REPORT
   Give me one short table: step, pass/fail, one-line detail. Then stop.
   Do not run git. I will review and commit myself.
```

---

## Part 2 — What you launch yourself

Only after the migration reports clean. Three **WSL2 terminals** (Windows Terminal
tabs are fine), each doing this first:

```bash
cd "$KOUROVKA_VAULT"
source "_meta/agents/Kourovka/paths.env"
```

Do not launch problem agents — Lead spawns those, three at a time.

| Terminal | Command |
|---|---|
| 1 — Lead | `claude --model fable --add-dir "$KOUROVKA_PAPERS"` |
| 2 — Validator | `codex --sandbox workspace-write --add-dir "$KOUROVKA_PAPERS"` |
| 3 — Math Expert | `codex --sandbox workspace-write --add-dir "$KOUROVKA_PAPERS"` |

First message in each terminal — change the role name and the second file only:

```
You are Lead on the Kourovka program.

Read, in this order, and follow them for the rest of this session:
  1. _meta/agents/Kourovka/_common-kourovka.md
  2. _meta/agents/Kourovka/lead-kourovka.md

Then perform the cold start defined in _common-kourovka.md §8 and stop.
```

Role files are [[lead-kourovka]], [[validator-kourovka]], [[math-expert-kourovka]].

A correct cold start is **one short message** — role, unread inbox count, and for
Lead the live-agent count — and then silence. If an agent instead starts proposing
problems or spawning anything, stop it and re-paste. An agent that ignores the
cold-start gate will ignore the timing contract too.

Then tell Lead to begin Phase A. It will build a longlist, score tractability, and
come back for your approval before anything is spawned. **That approval is a hard
human gate.**

---

## Part 3 — What "working" looks like in the first hours

Revision 2 changed behaviour, so the things to watch changed too.

Good signs:

- Lead's inbox stays near-empty. Last campaign it carried 78% of all traffic and
  336 unread messages.
- Each problem directory shows a **completed scan of a few hundred groups** within
  the first half-hour, not a discussion about whether to run one.
- Problem agents write to each other's inboxes. Last campaign that happened zero
  times.
- `Experiments/Kourovka/<id>-<slug>/` fills in as the work happens.

Stop and investigate if you see:

| Symptom | What it means |
|---|---|
| More or fewer than 3 live problem agents | Lead is not holding the concurrency rule |
| Any agent asking permission to run a computation | The abolished compute lease is back |
| A report using `DEAD`, `PARK`, `STRATEGY_EXHAUSTED` | The agent invented vocabulary; only `SOLVED`, `REFUTED`, `STILL-TRYING` exist |
| A cycle ending well before its deadline | Unspent budget is a contract violation — Lead voids the report and re-spawns |
| A `STILL-TRYING` with no named next computation | Route it to Math Expert; do not let it close |
| An experiment directory still all template after hours of work | The agent is not writing as it goes |
| `status/proven` or `status/solved` you did not write | Serious. `proven` is Validator-only, `solved` is yours alone |

Daily check, from a WSL2 terminal:

```bash
cd "$KOUROVKA_VAULT/Agents/Kourovka"
cat board/_board.md
tail -40 board/_decisions.md
ls -1 bus/inbox/*/ | wc -l        # unread backlog
pgrep -f "codex exec" | wc -l     # live agents — expect 3
```

`pgrep` only sees the WSL side, which is correct — every crew process lives there.
If it returns 0 while the board says three problems are live, the terminal that
spawned them was closed; Lead re-spawns on its next cycle, nothing is lost, because
the bus is on disk.

> [!tip] Don't let Windows sleep mid-cycle
> A suspended WSL2 VM kills the ephemeral problem agents but not their deadlines,
> so agents come back "over budget" on work they never did. If the machine sleeps
> overnight, tell Lead when you return; it should audit the clocks rather than
> treat those cycles as spent.

---

## Related

- [[Experiments/Kourovka/_post-mortem-2026-08]] — why the prompts changed
- [[kourovka-crew-setup]] — full install runbook, first-time setup
- [[_common-kourovka]] — the protocol every role inherits
- [[Experiments/Kourovka/_kourovka]] — program hub, live and closed problems
