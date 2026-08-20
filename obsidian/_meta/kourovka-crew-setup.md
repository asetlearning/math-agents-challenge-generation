---
title: "Kourovka crew — from-scratch terminal setup (Windows)"
type: runbook
platform: windows
author: <operator>
created: 2026-08-11
tags:
  - domain/group-theory
  - topic/kourovka
  - topic/agents
  - project/kourovka
  - status/reference
  - reference
---

# Kourovka crew — from-scratch setup (Windows)

How to stand up the Kourovka open-problems agent crew on a **clean Windows machine**.
Assumes nothing is installed. Follow it top to bottom the first time.

> [!info] Who this is for
> The operator running the crew. Not the agents — the agents read
> [[_common-kourovka]] and their own role file, not this one. The single exception is
> **§5**, which Lead is told to read before its first spawn.

> [!important] The crew runs in a Linux shell, on Windows
> Everything below happens inside **WSL2 / Ubuntu**, not in PowerShell. Obsidian
> still runs as a normal Windows app on your normal vault folder; WSL just reaches
> the same folder through `/mnt/c/...`. Both `claude` and `codex` support native
> Windows, but only under WSL2 does `codex` get the Linux sandbox that
> `--sandbox workspace-write` relies on — and that sandbox is the thing stopping
> six autonomous agents from writing outside the vault. Take WSL2 if you can.
>
> If WSL2 is blocked on your machine (no admin rights, virtualization disabled in
> BIOS, corporate policy), use **§A — Git Bash fallback** instead. It works; you
> just lose the sandbox and have to be more careful.

**Read [[_common-kourovka]] once yourself before you start.** If you don't know what
the file bus is, the rest of this will look arbitrary.

---

## §0 — What you are building

Three **standing** agents, each in its own terminal window, running indefinitely:

| Terminal | Agent | Runtime | Role file |
|---|---|---|---|
| 1 | **Lead** | `claude --model fable` | [[lead-kourovka]] |
| 2 | **Validator** | `codex` | [[validator-kourovka]] |
| 3 | **Math Expert** | `codex` | [[math-expert-kourovka]] |

Plus exactly **3 ephemeral problem agents** — one per live problem — that Lead
spawns and kills itself with `codex exec` (§5). You never launch those by hand.

> [!note] Why 3 and not 8
> The August 2026 campaign ran up to eight and closed nothing. Attention spread
> thin across eight fronts is worse than depth on three; see
> [[Experiments/Kourovka/_post-mortem-2026-08]]. Six processes total, three of
> them ephemeral.

They talk to each other by **writing files** into
`Agents/Kourovka/bus/inbox/<Recipient>/`. There is no canvas, no daemon, no
message broker, no socket — nothing to install and nothing to keep running. If a
terminal dies, nothing is lost except that agent's in-context memory; the bus is
on disk.

```
            ┌──────────┐
   you ◀───▶│   Lead   │◀────────┐
            └────┬─────┘         │
                 │ spawns        │ review circle
    ┌────────────┼────────────┐  │
    ▼            ▼            ▼  │
 Problem-a   Problem-b   Problem-c
    └────────────┴────────────┴──▶ Validator ──▶ Math Expert ──┘
```

---

## §1 — Install the toolchain

Steps 1.1–1.2 run in **Windows PowerShell as Administrator**. Everything from 1.3
onward runs **inside the Ubuntu terminal**. Each block is safe to re-run.

### 1.1 Install WSL2 + Ubuntu

Open **PowerShell as Administrator** (Start → type `powershell` → *Run as
administrator*) and run:

```powershell
wsl --install -d Ubuntu
```

Then **reboot**. After the reboot Ubuntu opens by itself and asks you to invent a
UNIX username and password — these are local to Ubuntu and have nothing to do with
your Windows or Anthropic/OpenAI accounts. Write the password down; `sudo` needs it.

Confirm you're on version 2, back in PowerShell:

```powershell
wsl --status
wsl -l -v          # Ubuntu should show VERSION 2, STATE Running
```

If it says `VERSION 1`, fix it now — WSL1 has no sandbox support:

```powershell
wsl --set-version Ubuntu 2
wsl --set-default-version 2
```

> [!warning] If `wsl --install` fails
> The usual causes, in order of likelihood: **virtualization is disabled in
> BIOS/UEFI** (look for Intel VT-x / AMD-V / SVM and turn it on); you aren't
> Administrator; the machine is Windows 10 older than 2004; or corporate policy
> blocks it. If you can't clear it, stop here and use **§A — Git Bash fallback**.
> Do not spend an afternoon on this — §A works.

**Everything from here on is typed in the Ubuntu window, not PowerShell.**

### 1.2 Where your vault is, from Ubuntu

Your Windows `C:` drive is mounted at `/mnt/c`. Check you can see the vault:

```bash
ls /mnt/c/Users/         # find your Windows username
ls "/mnt/c/Users/<you>/Documents/Obsidian/Math/obsidian"
```

You should see `_meta`, `Research`, `Agents`. If your vault is elsewhere, find it in
Windows Explorer, copy the address bar, and convert it:

```bash
wslpath -u 'C:\Users\Ada\Documents\Obsidian\Math\obsidian'
```

> [!warning] `$HOME` is not your Windows home
> In Ubuntu, `$HOME` is `/home/<you>` — a Linux-only folder that Obsidian cannot
> see. The vault lives under `/mnt/c/...`. Never use `~` or `$HOME` to reach it.

### 1.3 Base packages and poppler — gives you `pdftotext`

`pdftotext` rebuilds the problem corpus from the PDF and is what every agent uses to
read the real problem statement.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y poppler-utils curl git ripgrep python3
pdftotext -v      # expect: pdftotext version 2x.xx.x  (prints to stderr)
```

### 1.4 GAP — the computational algebra system

This is the crew's only real mathematical tool. Without it the problem agents can
do nothing but read.

```bash
sudo apt install -y gap
```

Verify it actually computes — this matters more than the version string:

```bash
echo 'Print(Size(SymmetricGroup(5)), "\n"); QUIT;' | gap -q -b
# expect: 120
```

If that prints `120`, GAP works. `gap --version` also works on 4.12+; on older
builds it isn't recognised, which is fine — the computation is the real test.

Ubuntu's `gap` package is usually a release or two behind. That's acceptable here;
what is *not* acceptable is silently missing GAP packages. If an agent later reports
that a specific GAP package is unavailable, install it rather than letting the agent work around it.

> [!warning] Do not let an agent reimplement GAP
> [[_common-kourovka]] forbids it. If GAP isn't working, fix GAP. A hand-rolled
> Python coset enumerator is how you get a wrong answer that looks right.

### 1.5 Node.js 22+

Ubuntu's own `nodejs` package is too old for the Codex CLI. Use NodeSource:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node --version    # expect: v22.x or newer
npm --version
```

### 1.6 Claude Code CLI — for Lead

Use the native installer; it doesn't go through npm.

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

The installer puts `claude` in `~/.local/bin`. If the next command says "not found",
open a new Ubuntu window (the installer edits your shell profile) or run
`export PATH="$HOME/.local/bin:$PATH"`.

```bash
claude --version
claude doctor      # read-only diagnostics; fix anything it flags
```

Then authenticate — run it once interactively and follow the browser login:

```bash
claude
```

WSL usually opens your Windows browser automatically. If it doesn't, copy the URL it
prints into a browser by hand. Once you're logged in and see the prompt, type
`/exit`.

**Verify the `fable` alias resolves for this account:**

```bash
claude --help | grep -A 12 -- "--model"
```

You want `fable` among the aliases. If it isn't there, the account doesn't have
access and you must pick another — `opus` is the right fallback for Lead, whose job
is judgement rather than speed. If you change it, also change the `runtime:` line in
[[lead-kourovka]] so the file doesn't lie.

### 1.7 Codex CLI — for Validator, Math Expert, and every problem agent

```bash
npm install -g @openai/codex
codex --version
```

If npm refuses with a permissions error, do **not** rerun it with `sudo`. Point npm
at your home directory instead:

```bash
mkdir -p "$HOME/.npm-global"
npm config set prefix "$HOME/.npm-global"
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
npm install -g @openai/codex
```

Authenticate:

```bash
codex login
```

Verify headless mode, which is what the entire spawn mechanism depends on:

```bash
codex exec --sandbox read-only --skip-git-repo-check "Reply with exactly: OK"
```

If that doesn't print `OK`, stop here. Nothing downstream will work.

### 1.8 rtk — the token proxy

`rtk` wraps common CLI tools and strips the parts of their output a language model
doesn't need. Same command, same result, **60–90% fewer tokens.** The crew runs long
sessions across many agents; this is the difference between a campaign that fits in
budget and one that doesn't.

This step is **optional** — the crew works without it — but do it, because the savings
compound across six agents running for days.

Install (any one of these):

```bash
# 1. Homebrew, if you have it on WSL
brew install rtk

# 2. Install script — puts the binary in ~/.local/bin
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh

# 3. From source, if you have Rust
cargo install --git https://github.com/rtk-ai/rtk
```

If you used the install script, make sure `~/.local/bin` is on your `PATH`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Verify:

```bash
rtk --version     # expect: rtk 0.40.0 or later
rtk gain          # token-savings analytics; must not error
```

> [!warning] Name collision
> There is an unrelated tool also called `rtk` (Rust Type Kit). If `rtk gain` fails
> with an unknown-subcommand error, you have the wrong one. Check `which rtk`.

**Lead gets automatic rewriting; the codex agents don't.** Lead runs on Claude Code,
which supports a hook that rewrites commands transparently:

```bash
rtk init -g       # installs the global Claude Code hook
```

Codex has no such hook, so Validator, Math Expert and the problem agents are told to
type `rtk` themselves — that instruction lives in `_common-kourovka.md` §13, and it is
reinforced by `AGENTS.md` at the vault root, which `codex` reads automatically on
startup. You don't have to do anything for that; both files are already in the repo.

**One thing to know:** the crew is instructed **never** to wrap GAP, Sage, or its own
scripts in `rtk`. Mathematical output has to arrive verbatim. `rtk` is for `ls`,
`grep`, `find`, `cat`, and `git` — inspection, not computation.

### 1.9 Confirm everything at once

```bash
for t in node npm pdftotext gap claude codex python3; do
  printf '%-12s %s\n' "$t" "$(command -v $t || echo MISSING)"
done
printf '%-12s %s\n' "rtk" "$(command -v rtk || echo 'not installed (optional)')"
```

Seven paths, no `MISSING`. That's the gate. `rtk` may be absent.

---

## §2 — Point the crew at your machine

**This is the only step where you type a path.** Everything downstream reads from one
config file, so there are no machine-specific paths anywhere else in the program.

Two locations matter:

| What | Where it lives |
|---|---|
| **Vault root** — the agents' working directory | wherever you keep the Obsidian vault |
| **Papers dir** — the folder holding the Kourovka PDF | anywhere; not part of the vault |

### 2.1 Edit `paths.env`

Open `_meta/agents/Kourovka/paths.env` — you can edit it in Obsidian, or from Ubuntu
with `nano` — and replace the two `CHANGEME` paths:

```bash
KOUROVKA_VAULT="/mnt/c/Users/Ada/Documents/Obsidian/Math/obsidian"  # has _meta/, Research/, Agents/
KOUROVKA_PAPERS="/mnt/c/Users/Ada/Documents/papers"                 # has the PDF
KOUROVKA_PDF_NAME="Kourovka 2022.pdf"
```

Rules, all of which the file will warn you about if you break them:

- **POSIX paths, forward slashes.** `/mnt/c/Users/...`, never `C:\Users\...`.
- **Absolute.** No `~`, no `$HOME` — under WSL those point at the Linux home, which
  is not where your vault is.
- `KOUROVKA_VAULT` is the folder that *directly* contains `_meta/`, not its parent.

Then load and verify. The file self-checks and prints nothing when it's right:

```bash
cd "/mnt/c/Users/Ada/Documents/Obsidian/Math/obsidian"
source "_meta/agents/Kourovka/paths.env"
echo "$KOUROVKA_VAULT" ; echo "$KOUROVKA_PDF" ; kv_now ; kv_deadline 3
```

You should get the two paths, the current UTC time, and a time exactly three hours
later. If you get a `paths.env:` warning, fix it before going further. A wrong
`KOUROVKA_PDF` is the single most damaging misconfiguration in this setup: it makes
the mandatory staleness check ([[_common-kourovka]] §7) silently impossible, and
agents fall back to the mangled corpus text without telling you.

`kv_now` and `kv_deadline` are the crew's clock. Every deadline in the timing
contract is computed with them, which is why `paths.env` — not any prompt — owns
them.

### 2.2 Load it automatically in every shell

```bash
echo 'source "/mnt/c/Users/Ada/Documents/Obsidian/Math/obsidian/_meta/agents/Kourovka/paths.env"' >> ~/.bashrc
```

Open a new Ubuntu window and confirm `echo $KOUROVKA_VAULT` prints the vault.

### 2.3 The PDF

~1.9 MB, 269 pages, arXiv:1401.0300v23, editors Khukhro & Mazurov. If you don't have
it, fetch that arXiv version — but then **re-run §3 and check the counts**, because a
different version will shift the section boundaries.

Agents get **read** access to `$KOUROVKA_PAPERS` via `--add-dir` and nothing else
outside the vault. They never get write access to whatever repo the PDF sits in.

### 2.4 Directory scaffold

Idempotent; safe to re-run.

```bash
mkdir -p "$KOUROVKA_VAULT"/Agents/Kourovka/{board,roster,problems,bus/archive} \
         "$KOUROVKA_VAULT"/Agents/Kourovka/bus/inbox/{Lead,Validator,MathExpert} \
         "$KOUROVKA_VAULT"/Experiments/Kourovka
```

---

## §3 — Build the problem corpus

The corpus is already committed to the vault. **You only need this if you're on a
fresh vault or the PDF changed.**

```bash
cd "$KOUROVKA_VAULT"
export KOUROVKA_AUTHOR="your-name"       # goes in the generated notes' frontmatter
python3 "_meta/scripts/kourovka-extract.py" \
  "$KOUROVKA_PDF" \
  "Research/Group theory/Open problems/Kourovka/corpus"
```

`KOUROVKA_AUTHOR` is optional; without it the notes say `<operator>`. The script
never guesses a name from your machine.

The script prints per-issue counts to stderr. **Check them against the table in
[[_kourovka-20-corpus]].** The load-bearing number is:

```
issue 20 -> 123 problems
```

The notebook's own preface says issue 20 "contains 123 new problems". If the
extractor recovers 123, the section-boundary logic is right. If it recovers anything
else, the parse has drifted and the corpus is not trustworthy — do not start the crew
on it.

Totals you should see: **1213 parsed**, **65 flagged answered**, **1148 open**.

Outputs:

```
Research/Group theory/Open problems/Kourovka/
├── _kourovka-20-corpus.md              overview + limitations (read this)
└── corpus/
    ├── kourovka-20-corpus.jsonl        canonical, one JSON object per problem
    └── kourovka-issue-NN-YYYY.md × 20  human-readable, grep-friendly
```

> [!warning] The corpus text is a mangle
> `pdftotext` flattens typeset mathematics: `hx, yi` is really `⟨x, y⟩`, subscripts
> and superscripts are lost, displayed formulas lose their layout. The corpus is for
> **selection and search only**. Every agent is required by [[_common-kourovka]] §7
> to re-read its problem in the PDF before doing any mathematics. Enforce that.

---

## §4 — Launch the three standing agents

Three terminal windows (or tabs). Leave them open. Each command **loads the role file
as the opening prompt**, which is how the agent knows who it is.

Three **Ubuntu** windows — open them from the Start menu, or run `wsl` three times,
or use Windows Terminal tabs (Ctrl+Shift+T), whichever you prefer. Not PowerShell.

If you did §2.2 the `source` already happened when the shell opened, so each block
below just needs:

```bash
cd "$KOUROVKA_VAULT"
```

### Terminal 1 — Lead

```bash
cd "$KOUROVKA_VAULT"
claude --model fable --add-dir "$KOUROVKA_PAPERS"
```

Then paste as the first message:

```
You are Lead on the Kourovka program.

Read, in this order, and follow them for the rest of this session:
  1. _meta/agents/Kourovka/_common-kourovka.md
  2. _meta/agents/Kourovka/lead-kourovka.md

Then perform the cold start defined in _common-kourovka.md §8 and stop.
```

### Terminal 2 — Validator

```bash
cd "$KOUROVKA_VAULT"
codex --sandbox workspace-write --add-dir "$KOUROVKA_PAPERS"
```

First message:

```
You are Validator on the Kourovka program.

Read, in this order, and follow them for the rest of this session:
  1. _meta/agents/Kourovka/_common-kourovka.md
  2. _meta/agents/Kourovka/validator-kourovka.md

Then perform the cold start defined in _common-kourovka.md §8 and stop.
```

### Terminal 3 — Math Expert

```bash
cd "$KOUROVKA_VAULT"
codex --sandbox workspace-write --add-dir "$KOUROVKA_PAPERS"
```

First message:

```
You are Math Expert on the Kourovka program.

Read, in this order, and follow them for the rest of this session:
  1. _meta/agents/Kourovka/_common-kourovka.md
  2. _meta/agents/Kourovka/math-expert-kourovka.md

Then perform the cold start defined in _common-kourovka.md §8 and stop.
```

### 4.1 What a correct cold start looks like

Each agent replies with **one short message** — role, unread inbox count, and (Lead
only) live-agent count — and then waits. That's it.

If an agent instead starts proposing problems to attack, dumping ideas, or spawning
anything: **stop it and re-paste the cold-start instruction.** An agent that ignores
the cold-start gate will ignore the timing contract too.

### 4.2 Waking an agent later

The standing agents are polling agents, not daemons — they act when you prompt them.
Nudge with:

```
Poll your inbox at Agents/Kourovka/bus/inbox/<YourRole>/ and process it oldest-first,
BLOCKER and KILL first. Report what you did in one message.
```

---

## §5 — Spawning, resuming and killing problem agents

**This is the section [[lead-kourovka]] points to.** Lead runs these; you shouldn't
need to, except to debug.

### 5.1 Spawn

```bash
source "$KOUROVKA_VAULT/_meta/agents/Kourovka/paths.env"
V="$KOUROVKA_VAULT"
ID="18.31"                       # the Kourovka problem number
SLUG="dpi-groups"                # matches the synthesis note filename

mkdir -p "$V/Agents/Kourovka/problems/$ID/scratch" \
         "$V/Agents/Kourovka/bus/inbox/Problem-$ID"

# The write-up directory must exist before the agent starts (_common §12).
bash "$V/_meta/scripts/kourovka-new-experiment.sh" "$ID" "$SLUG"

codex exec \
  --sandbox workspace-write \
  -C "$V" \
  --skip-git-repo-check \
  --add-dir "$KOUROVKA_PAPERS" \
  -m gpt-5-codex \
  --json \
  -o "$V/Agents/Kourovka/problems/$ID/last-message.md" \
  "$(cat "$V/_meta/agents/Kourovka/problem-agent-kourovka.md")

=== YOUR ASSIGNMENT ===
PROBLEM_ID:      $ID
PROBLEM_DIR:     Agents/Kourovka/problems/$ID
EXPERIMENT_DIR:  Experiments/Kourovka/$ID-$SLUG
SYNTHESIS:       Research/Group theory/Open problems/Kourovka/$ID-$SLUG.md
CYCLE:           1
BUDGET_HOURS:    3
STARTED_UTC:     $(kv_now)
DEADLINE_UTC:    $(kv_deadline 3)

FIRST_COMPUTATION: <the concrete scan from the tractability block — required>
TRACTABILITY:      <n>/5 — <one-line reason>
COUNTEREXAMPLE_SHAPE: <what one would look like, or 'unknown'>
" > "$V/Agents/Kourovka/problems/$ID/cycle-1.jsonl" 2>&1 &
```

> [!important] No spawn without a named first computation
> `FIRST_COMPUTATION` is not decoration. Lead may not spawn an agent on a problem
> unless it can name the concrete scan the agent should run in its first half hour
> ([[lead-kourovka]] Phase A §6a). If you can't fill that line, the problem isn't
> ready — work out the computation, or pick a more tractable problem.

Flag by flag, because each one is load-bearing:

| Flag | Why |
|---|---|
| `--sandbox workspace-write` | Agent can write inside the vault, nowhere else. Not `danger-full-access`. |
| `-C "$V"` | Working root = vault, so every path in the role files resolves. |
| `--skip-git-repo-check` | The vault is not a git repo; without this `codex exec` refuses to start. |
| `--add-dir "$KOUROVKA_PAPERS"` | Read access to the source PDF. Mandatory — the §7 staleness check needs it. |
| `-m gpt-5-codex` | Pin the model so cycles are comparable. |
| `--json` | Emits the event stream, which is where the **session id** comes from. |
| `-o .../last-message.md` | Final message lands in a file Lead can read without parsing JSONL. |
| `... .jsonl 2>&1 &` | Full transcript to disk; background so Lead keeps 3 in flight. |

`kv_now` and `kv_deadline` come from `paths.env`. Never substitute a bare `date`
here — the relative-time flag differs between shells, and a wrong `DEADLINE_UTC`
breaks the timing contract silently rather than loudly.

### 5.2 Capture the session id — do this immediately

Without it you cannot extend the agent, only restart it from zero.

```bash
grep -m1 -o '"session_id":"[^"]*"' \
  "$V/Agents/Kourovka/problems/$ID/cycle-1.jsonl"
```

If the key name differs in your codex version, just look at the first event:

```bash
head -c 800 "$V/Agents/Kourovka/problems/$ID/cycle-1.jsonl"
```

Write it into `Agents/Kourovka/roster/Problem-$ID.md` under `session_id:`.

### 5.3 Extend (`+2h`) or start a new cycle

**Resume. Never re-spawn.** A fresh `codex exec` throws away everything the agent
learned and burns the extension on re-reading.

```bash
codex exec resume "$SESSION_ID" \
  --sandbox workspace-write \
  -C "$V" \
  --skip-git-repo-check \
  --add-dir "$KOUROVKA_PAPERS" \
  "EXTENSION GRANTED. CYCLE: 2. BUDGET_HOURS: 2.
DEADLINE_UTC: $(kv_deadline 2)
Named next computation on record: <the one from the STILL-TRYING report>.
Run it first. Read Agents/Kourovka/bus/inbox/Problem-$ID/ after." \
  >> "$V/Agents/Kourovka/problems/$ID/cycle-2.jsonl" 2>&1 &
```

Extensions are **+2 hours** and, on a `STILL-TRYING` report that names a next
computation, they are the **default** — Lead needs a reason to refuse, not a reason to
grant ([[lead-kourovka]], "Extension discipline"). Cumulative cap is 12 hours before
the human is asked.

`codex exec resume --last` resumes the most recent session — convenient
interactively, **wrong** with several agents in flight. Always pass the explicit id.

### 5.4 Kill

Soft kill, which is the only kind you should normally use:

1. Write a `type: KILL` message into `Agents/Kourovka/bus/inbox/Problem-$ID/`.
2. Set `state: killed` in the roster note.
3. Log reason + elapsed budget in `board/_decisions.md`.

Hard kill only if the process is genuinely stuck:

```bash
pgrep -fl "problems/$ID"          # look before you shoot
pkill -f "problems/$ID"           # SIGTERM, lets it finish the write
```

(On the Git Bash fallback these don't exist — see §A.3b.)

Never `kill -9` an agent mid-turn. It will leave a half-written note in the vault and
the next agent to read it will believe it.

### 5.5 See what's live

```bash
pgrep -fl "codex exec" | wc -l    # should be ≤ 3 problem agents
```

Concurrency ([[_common-kourovka]] §4.1): **six agents total** — Lead, Validator, Math
Expert, and **exactly three problem agents.**

> [!note] This was eight, and the change is the main lesson of the first campaign
> The August 2026 run kept eight problem agents alive and opened sixteen problems in a
> week. Nothing got depth and nothing closed. Three is an *attention* limit, not a
> resource limit: it is how many problems Lead can actually think about while also
> reading the mathematics. See `Experiments/Kourovka/_post-mortem-2026-08.md`.

**There are no compute slots any more.** Agents run whatever computation they need
without asking ([[_common-kourovka]] §4.2) — the old 60-second lease produced 252
permission messages, nineteen percent of all bus traffic, and in one case cost an
agent nineteen active minutes to authorise a three-minute job. Jobs over two hours or
~8 GB get an FYI to Lead so it can sequence them. Everything gets a `timeout`.

---

## §6 — Smoke test before the real run

Do this once. It costs twenty minutes and catches every wiring mistake.

**0. Clock and paths.** In any Ubuntu window:

```bash
source "$KOUROVKA_VAULT/_meta/agents/Kourovka/paths.env"   # must print nothing
kv_now ; kv_deadline 3
ls -l "$KOUROVKA_PDF"
```

Silence from the `source`, two timestamps exactly three hours apart, and a real file
size for the PDF. If `kv_deadline 3` equals `kv_now`, or prints an error, your
`date` isn't the one `paths.env` expected — fix that before anything else, because
every budget in the program is computed from it.

**0b. Obsidian sees what Ubuntu writes.** Still in Ubuntu:

```bash
echo "wsl round-trip $(kv_now)" > "$KOUROVKA_VAULT/Agents/Kourovka/_wsltest.md"
```

Open the vault in Obsidian on Windows and confirm `_wsltest.md` is there with that
text, then delete it. This proves the two halves of the machine are looking at the
same folder — if they aren't, the whole file bus is invisible to you.

**1. Bus round-trip.** In Lead's terminal:

```
Write a type: QUESTION message to Validator's inbox asking it to confirm it can
read Agents/Kourovka/bus/inbox/Validator/ and reply into yours. Then stop.
```

Then nudge Validator (§4.2). You should end up with a reply file in
`bus/inbox/Lead/`. If not, the bus is broken and nothing else matters.

**2. GAP through an agent.** In Validator's terminal:

```
Run this and paste the literal output:
  echo 'Print(Size(SymmetricGroup(5)), "\n"); QUIT;' | gap -q -b
```

Expect `120`. If the agent *describes* the answer instead of running it, that's the
"reported an output I didn't observe" failure mode — correct it now, hard.

**3. PDF access.** In Math Expert's terminal:

```
Run exactly this and paste the literal first three lines of output:
  source "_meta/agents/Kourovka/paths.env"
  pdftotext -f 148 -l 148 -layout "$KOUROVKA_PDF" - | head -3
```

Expect the running head `New Problems (20th issue, 2022)` and problem `20.11`. If you
get a different issue, the PDF is a different arXiv version — go back to §3 and
re-check the corpus counts before doing anything else.

**4. Spawn one throwaway agent.** Run §5.1 with `ID="smoke"` and a prompt that just
says "Reply OK and stop." Confirm `problems/smoke/last-message.md` appears and that
you can pull a session id out of `cycle-1.jsonl`. Then delete `problems/smoke/`.

Only after all of these pass do you let Lead start Phase A.

---

## §7 — Running the program

Once the crew is up, you do very little. The sequence:

1. **Lead runs Phase A** ([[lead-kourovka]]): builds a ~150 longlist from the corpus,
   sends it to Math Expert and Validator, intersects the three views, writes 50
   synthesis notes, and puts a ranked list in `Agents/Kourovka/board/_board.md`.
2. **You approve the 50.** This is a hard human gate. No agent gets spawned before
   you've looked at the list.
3. **Lead spawns 3** — the three highest-tractability problems, easiest first — and
   keeps exactly 3 alive while the queue is non-empty. Each spawn is preceded by
   `kourovka-new-experiment.sh`, so the write-up directory exists before the agent does.
4. **You get pinged** only when a problem has burned ≥3h **and** completed the full
   Validator → Math Expert → Lead circle. Anything else reaching you is a protocol
   violation; say so.
5. **Every problem gets written up** in `Experiments/Kourovka/<id>-<slug>/`, whether it
   closed or not. A `STILL-TRYING` write-up naming what was ruled out is worth as much
   to the next campaign as a solution.

### 7.1 What to check daily

```bash
cd "$KOUROVKA_VAULT/Agents/Kourovka"
cat board/_board.md
tail -40 board/_decisions.md
ls -1 bus/inbox/*/ | wc -l        # unread backlog
pgrep -f "codex exec" | wc -l     # live agents
```

Five things mean something is wrong:

- **Live agents < 3 with a non-empty queue** — Lead let the board drain.
- **Live agents > 3** — Lead is spreading attention thin again.
- **`_decisions.md` not growing** — extensions are being granted without a record,
  which means without justification.
- **An `Experiments/Kourovka/<id>-<slug>/` directory that is still all template** on a
  problem that has burned hours. The agent is not writing as it goes.
- **Any note tagged `status/proven` or `status/solved`** that you didn't write.
  `proven` is Validator-only and `solved` is yours alone. Investigate immediately.

Also worth a glance, weekly: `grep -c '' Agents/Kourovka/bus/inbox/Lead/*` — if
Lead's inbox is carrying a third of all crew traffic, the bottleneck is back.

### 7.2 Expected outcome

These problems are in the Kourovka Notebook because competent mathematicians did not
close them, so most of the 50 will not close here either. But note what the first
campaign actually produced: **zero false positives and zero true positives.** It was
so well defended against claiming a wrong result that it stopped trying to get a
right one.

So there are two ways to fail, not one:

| Failure | What it costs |
|---|---|
| A fabricated claim reaches a mathematician | Credibility. Unrecoverable. |
| A closable problem is abandoned at minute 12 | The entire point of the program. |

The status ladder, the review circle and the mandatory "What this does NOT establish"
section exist to prevent the first. The persistence rules ([[_common-kourovka]] §3.2),
the enumerate-first mandate and the abolished compute lease exist to prevent the
second. A run of 47 well-documented `STILL-TRYING`s, each naming a concrete next
computation, is a good run. A run of 47 twelve-minute abandonments is not, however
honestly it was reported.

---

## §8 — Troubleshooting

### Windows / WSL specific

**`wsl --install` fails, or Ubuntu won't start**
Virtualization disabled in BIOS/UEFI (Intel VT-x, AMD-V, or SVM — enable it), not
running PowerShell as Administrator, Windows 10 older than 2004, or corporate
policy. If you can't clear it, switch to §A. Don't grind on this.

**`ls /mnt/c` is empty, or the vault isn't visible**
The drive isn't mounted. `wsl --shutdown` in PowerShell, then reopen Ubuntu. If the
vault is on a different drive, it's `/mnt/d/...` and so on. OneDrive-redirected
folders live under `/mnt/c/Users/<you>/OneDrive/Documents/...` — check there before
concluding the path is wrong.

**Obsidian doesn't show files the agents wrote**
Almost always a path mismatch: `$KOUROVKA_VAULT` points at a different folder than
the one the Obsidian vault is opened on. Run smoke test 0b. Note the reverse case
too — Obsidian caches; `Ctrl+R` reloads it.

**Everything is extremely slow**
You put the vault inside the Linux filesystem (`/home/...`) or you're reaching it
over a network drive. `/mnt/c` is slower than native Linux disk but perfectly
usable for text files. If it's unbearable, close Obsidian's sync/plugins while a run
is in flight.

**`claude` or `codex`: command not found, right after installing**
The installer edited `~/.bashrc` but this shell started before that. Open a new
Ubuntu window, or `source ~/.bashrc`.

**Login won't open a browser**
WSL can't always launch the Windows browser. Copy the URL it prints into a browser
manually; the callback still completes.

**`kv_deadline` prints an error or the same time as `kv_now`**
Your `date` isn't behaving as `paths.env` detected. Check `date --version` — GNU
prints a version, BSD errors. Fix `paths.env` rather than hand-writing deadlines.

**Paths with backslashes anywhere**
Something reintroduced a Windows path. `paths.env` warns about this in
`KOUROVKA_VAULT`, but if you see `C:\` inside a prompt or a note, correct it —
agents will copy the mistake forward.

### General

**`codex exec` exits immediately with a git error**
Add `--skip-git-repo-check`. The vault isn't a repo.

**Agent says it can't write to the vault**
`--sandbox workspace-write` missing, or `-C` points somewhere else. Check with
`pgrep -fl codex`.

**Agent can't open the PDF**
Three candidates, in order: `--add-dir "$KOUROVKA_PAPERS"` missing from the launch
command; `$KOUROVKA_PAPERS` empty because `paths.env` wasn't sourced in that shell; or
the filename is unquoted somewhere — it **contains a space**, so every reference must
stay quoted. Diagnose with `source "_meta/agents/Kourovka/paths.env"; ls -l "$KOUROVKA_PDF"`.

**`$KOUROVKA_VAULT` is empty / paths.env prints a warning**
You edited the wrong copy, left a `CHANGEME` in, used `~` or `$HOME` (which under WSL
point at the Linux home, not the vault), used backslashes, or pointed
`KOUROVKA_VAULT` at the vault's *parent*. It must be the folder that directly
contains `_meta/`.

**`claude --model fable` errors on an unknown model**
The alias isn't available to that account. Check `claude --help | grep -A 12 -- "--model"`,
fall back to `opus`, and update `runtime:` in [[lead-kourovka]].

**Corpus counts don't match [[_kourovka-20-corpus]]**
The parse drifted, most likely because the PDF was replaced with a different arXiv
version. Do not proceed. Diff the per-issue counts to find which section boundary
moved; the extractor's section logic is in `_meta/scripts/kourovka-extract.py`.

**Two agents are working the same problem**
[[_common-kourovka]] §10 requires both to stop and report to Lead. Check
`board/_board.md` for a duplicate row and kill one.

**An agent claims it solved an open problem**
Follow [[lead-kourovka]] §Handling claimed solutions. Do not forward it anywhere.
The base rate for this being correct is very low, and the cost of forwarding a wrong
one is the credibility of the whole program.

**The vault feels like it's filling with junk**
It is, by design — logs, scratch scripts, JSONL transcripts. `problems/<id>/scratch/`
and `*.jsonl` are disposable. The bus archive is not; it's the audit trail.

---

## §A — Git Bash fallback (only if WSL2 is blocked)

Use this **only** if §1.1 failed and you can't fix it. You lose the Linux sandbox,
which is a real cost: `--sandbox workspace-write` no longer constrains the agents to
the vault the way it does under WSL2. Read §A.4 before you start a real run.

### A.1 Install

Everything here is native Windows. In **PowerShell**:

```powershell
winget install --id Git.Git -e                    # Git for Windows, gives Git Bash
winget install --id OpenJS.NodeJS.LTS -e          # Node 22+
winget install --id Anthropic.ClaudeCode -e       # claude
```

Then **close PowerShell and open Git Bash** (Start → "Git Bash"). Everything below
is Git Bash, and every command in §2–§7 works there unchanged.

`pdftotext` and GAP have no winget packages worth using. Install them by hand:

- **poppler** — download a Windows build (the `poppler-windows` releases), unzip to
  e.g. `C:\tools\poppler`, and add `C:\tools\poppler\Library\bin` to your PATH.
- **GAP** — take the official Windows installer from `gap-system.org`, install to
  the default location, and add its `bin` directory to your PATH.

Then in Git Bash:

```bash
npm install -g @openai/codex
codex login
claude          # log in, then /exit
```

### A.2 Verify

```bash
for t in node npm pdftotext gap claude codex python; do
  printf '%-12s %s\n' "$t" "$(command -v $t || echo MISSING)"
done
echo 'Print(Size(SymmetricGroup(5)), "\n"); QUIT;' | gap -q -b     # expect 120
```

If `gap` or `pdftotext` is `MISSING`, the PATH edit didn't take — restart Git Bash,
and if it still fails, check the directory you added actually contains `gap.exe` /
`pdftotext.exe`.

If `python` is missing but `python3` exists, or vice versa, use whichever works in
§3; the extractor doesn't care.

### A.3 Paths under Git Bash

Same `paths.env`, different prefix — Git Bash uses `/c/...` where WSL uses
`/mnt/c/...`:

```bash
KOUROVKA_VAULT="/c/Users/Ada/Documents/Obsidian/Math/obsidian"
KOUROVKA_PAPERS="/c/Users/Ada/Documents/papers"
```

Auto-load it the same way (`~/.bashrc` exists in Git Bash too). `wslpath` does not
exist here; if you need to convert a Windows path, just replace `C:\` with `/c/` and
flip the slashes.

The `kv_now` / `kv_deadline` helpers work unchanged — Git Bash ships GNU coreutils,
so `paths.env` takes the same branch WSL does.

### A.3b Counting and killing agents

Git Bash has no `pgrep` or `pkill`, so the process commands in §5.4, §5.5 and §7.1
don't work as written. Substitute:

```bash
ps -W | grep -c '[c]odex'                      # how many are live   (§5.5, §7.1)
ps -W | grep '[c]odex'                         # look before you shoot (§5.4)
```

`ps -W` is Git Bash's "show Windows processes too" flag; plain `ps` only sees the
shell's own children and will under-report. To stop one, take the PID from that
listing and use PowerShell:

```powershell
Stop-Process -Id <pid>
```

As under WSL, **soft kill first** — the `type: KILL` message, roster update, and
decision-log entry in §5.4. Killing the process is the last resort, and never while
it's mid-write.

### A.4 What you give up, and what to do about it

| | WSL2 | Git Bash |
|---|---|---|
| `codex` sandbox | Linux seccomp/Landlock — enforced | not enforced |
| `claude` sandbox | supported | not supported |
| GAP packages | one `apt` command | manual |

With no enforced sandbox, `--sandbox workspace-write` becomes a request rather than
a guarantee, and a misbehaving agent could in principle write outside the vault.
Mitigations, in order of value:

1. **Keep the vault and `$KOUROVKA_PAPERS` on a drive with nothing else valuable
   on it**, or at least back the vault up before the first real run.
2. **Never use `--sandbox danger-full-access`.** It is already forbidden by
   [[_common-kourovka]]; on this configuration it's the difference between a bad day
   and a very bad day.
3. **Check §7.1 daily rather than occasionally**, especially the `_decisions.md`
   growth and the `status/*` tags.

Everything else in this runbook — the bus, the timing contract, the review circle,
all four role files — is identical.

---

## §9 — File map

```
_meta/
├── kourovka-crew-setup.md              ← this file
├── scripts/kourovka-extract.py         corpus extractor
└── agents/Kourovka/
    ├── paths.env                       ← the ONLY file with machine paths. Edit once.
    ├── _common-kourovka.md             protocol: bus, timing, budget, status ladder
    ├── lead-kourovka.md                Terminal 1
    ├── validator-kourovka.md           Terminal 2
    ├── math-expert-kourovka.md         Terminal 3
    └── problem-agent-kourovka.md       spawn template (never launched by hand)

Research/Group theory/Open problems/Kourovka/
├── _kourovka-20-corpus.md              corpus overview + limitations
├── corpus/                             JSONL + 20 per-issue notes
└── <id>-<slug>.md                      the 50 synthesis notes (Lead writes these)

Agents/Kourovka/
├── board/_board.md                     Lead-owned single source of truth
├── board/_decisions.md                 append-only: every spawn/extend/skip/kill
├── roster/<Agent>.md                   one per live agent, holds the session id
├── bus/inbox/<Recipient>/              the message bus
├── bus/archive/                        processed messages, never deleted
└── problems/<id>/                      log.md, findings.md, scratch/, *.jsonl

Experiments/Kourovka/                   final write-ups of closed problems
```

## Related

- [[_common-kourovka]] — the protocol. Read before this file.
- [[lead-kourovka]] · [[validator-kourovka]] · [[math-expert-kourovka]] ·
  [[problem-agent-kourovka]]
- [[_kourovka-20-corpus]] — the 1213-problem corpus and its limitations
- [[kourovka-11.48-kostrikin-1990]] — the model every synthesis note imitates
- [[mission]] · [[tags]] · [[naming-conventions]]
