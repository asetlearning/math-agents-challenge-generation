---
description: One-time onboarding for a new contributor to the math-agents vault. Registers the user's handle and installs the /research handle for both Claude Code and Codex.
---

# /setup — Math vault onboarding

The canonical, tool-agnostic setup ritual lives at **`SETUP.md` in the repo
root** (single source of truth, shared with Codex). Read that file now and
execute it top to bottom.

Notes for this Claude Code invocation:

- You are already inside the math-agents repo (or the user just cloned it) —
  step 1's "already cloned" exception applies: use this clone's location.
- Use the AskUserQuestion tool for step 3 (the single name + handle question).
- Execute both the Claude Code steps AND the Codex steps — one run sets up
  both tools.
- Finish with the step 10 welcome summary, then remind the user to restart
  Claude Code so the skills load.
