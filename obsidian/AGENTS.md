# Agent instructions — Obsidian maths vault

`codex` reads this file automatically on startup, from the working directory. It
applies to **every** agent running in this vault, and it is deliberately short.

If you are part of the Kourovka crew, your real instructions are the prompt you were
launched with, plus `_meta/agents/Kourovka/_common-kourovka.md`. This file only
carries the few things that are true for everyone and that nobody should have to be
told twice.

---

## 1. Use `rtk` for shell commands

`rtk` is a token-reducing proxy. It runs the real command and strips output a language
model doesn't need — 60–90% fewer tokens for the same result. Long sessions live or
die on this.

```bash
rtk git status
rtk ls Agents/Kourovka/bus/inbox/Lead
rtk grep -rn "wreath" Agents/Kourovka/problems/
rtk cat Agents/Kourovka/board/_board.md
rtk find Agents/Kourovka -name "*.g"
```

Check once per session with `command -v rtk`. **If it isn't installed, just run the
commands normally** — everything works without it. Don't block on it, and don't try to
install it yourself.

### Never wrap computation in `rtk`

```bash
gap -q -b scan.g > scan.out 2>&1        # correct
rtk gap -q -b scan.g                    # WRONG
```

`rtk` is for inspecting files and repos. Mathematical output must reach you **verbatim
and complete** — GAP, Sage, Python, and your own scripts run bare. A filtered
computation transcript is worse than no transcript, and you are forbidden from
reporting outputs you did not actually see.

### Known edges

| Situation | What to do |
|---|---|
| `-not`, `-exec` or other compound `find` predicates | use plain `find` — `rtk find` rejects them |
| Path contains a space (e.g. `Research/Group theory/`) | use plain `find`, or a Python `pathlib` walk — `rtk find` mangles these |
| You need raw, unfiltered output | `rtk proxy <cmd>` |
| Checking savings | `rtk gain` |

---

## 2. Never run git

**No agent in this vault commits, pushes, stages, or branches. Ever.** The human
handles all version control. This is not a preference — agent-authored commits in a
shared research repo are unreviewable.

If you think something needs committing, say so in a message and stop.

## 3. Stay inside the vault

The vault is your working root. Write vault-relative paths (`Agents/Kourovka/...`),
never absolute ones. Machine-specific paths live in exactly one place —
`_meta/agents/Kourovka/paths.env` — and you `source` it rather than hard-coding
anything.

The papers directory (`$KOUROVKA_PAPERS`) is **read-only**. Nothing here writes to it.

## 4. Never fabricate an output

If you did not run it, do not report it as run. Not to complete a table, not to round
out a summary, not because you are confident what the answer would be. A fabricated
transcript in a mathematics vault poisons every downstream result and is the single
fastest way to make this program worthless.

The same goes for citations: author, venue, year, or it is not a citation.

---

*Kourovka crew: `_meta/agents/Kourovka/_common-kourovka.md` §13 has the full `rtk`
section. Setup: `_meta/kourovka-crew-setup.md` §1.8.*
