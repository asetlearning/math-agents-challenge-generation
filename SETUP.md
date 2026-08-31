# SETUP — one-time onboarding (for AI agents to execute)

You are an AI agent (Claude Code, Codex, or similar) and a user asked you to
set up this repo — typically with a prompt like *"Clone
https://github.com/ai-math-edu-lab/math-agents repo, start the setup"*.
Execute this file top to bottom. When you finish, the user can type
`/research <paper-url>` (or say "add this paper to the vault") in **both**
Claude Code **and** Codex, and the paper lands in the shared Obsidian vault
correctly tagged and linked.

Rules for you, the executing agent:

- **Ask the user only ONE question** (step 3: name + handle). Everything else
  is automatic. Don't ask for confirmation between steps; do stop and report
  if a step fails.
- Every step is **idempotent** — if something is already installed or
  registered, detect it and move on. Never duplicate registrations, never
  touch another user's files.
- Works on **macOS and Windows**. Use bash on macOS/Linux, PowerShell on
  Windows; where they differ, both are given.

## What you are installing

```
Desktop/math-agents/          ← this repo, one folder on the user's Desktop
├── obsidian/                 ← THE VAULT (open this folder in Obsidian)
├── claude/                   ← Claude Code context (claude/CLAUDE.md)
└── codex/                    ← Codex context + the obsidian-research MCP server
```

The research skill itself lives *inside the vault* at
`obsidian/_meta/skills/research/` — both tools link to it, so a `git pull`
updates everyone's doctrine.

## Step 1 — Clone (skip if already cloned)

If this repo is already on disk (you may be running inside it), use that
location. Otherwise clone to the Desktop:

- macOS/Linux: `git clone https://github.com/ai-math-edu-lab/math-agents.git "$HOME/Desktop/math-agents"`
- Windows: `git clone https://github.com/ai-math-edu-lab/math-agents.git "$env:USERPROFILE\Desktop\math-agents"`

Record three absolute paths:

- `REPO`  = the clone
- `VAULT` = `<REPO>/obsidian` — the vault root (contains `_meta/` and
  `_templates/`); **not** the repo root
- `MCP`   = `<REPO>/codex` (the MCP server lives directly in this folder)

Sanity check: `test -d "$VAULT/_meta" && test -d "$MCP/src"`.

## Step 2 — Prerequisites

Check, install only what's missing:

1. **git** — `git --version` (missing: macOS `xcode-select --install`, Windows
   `winget install Git.Git`).
2. **uv** (runs the MCP server; brings its own Python):
   - check: `uv --version`
   - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - After a fresh install `uv` may not be on PATH in this session — locate it
     (`~/.local/bin/uv` / `%USERPROFILE%\.local\bin\uv.exe`) and use the
     absolute path in step 6.

Claude Code, Codex, and Obsidian are installed by the human. Don't install
them; if one is missing, complete every step that doesn't need it and list the
gap in the final summary.

## Step 3 — Ask the user who they are (the ONE question)

Ask, in a single question:

1. **Full name** — e.g. `Anna Petrova`
2. **Handle** — kebab-case, e.g. `anna-p` (lowercase letters, digits,
   hyphens). If they give spaces/capitals, kebab-case it and confirm in
   passing.

Set `FULL_NAME` and `HANDLE`.

## Step 4 — Register the handle in the vault (skip if already there)

Check: `grep "#user/$HANDLE" "$VAULT/_meta/tags.md"` — if it matches, skip to
step 5. Otherwise:

**4a.** In `$VAULT/_meta/tags.md`, find the `Registered handles:` list under
"Axis 2" and add one line, keeping the list alphabetical:

```
- `#user/<HANDLE>` — <FULL_NAME> (see [[People/<HANDLE>]])
```

**4b.** Create `$VAULT/People/<HANDLE>.md`. Read `People/maumayma.md` first
and copy its **structure only** (frontmatter keys, section headings) — never
Maria's content. Fill in:

- frontmatter: `title: <FULL_NAME>`, `handle: <HANDLE>`, `author: <HANDLE>`,
  `tags: [meta, user/<HANDLE>]`, `domain_focus: []`, `projects: []`
- body: `# <FULL_NAME> — \`<HANDLE>\``, a "## Who" line saying they joined
  today (real date), "Domains of focus: TBD. Active projects: TBD."

## Step 5 — Claude Code handle

Skip any sub-step whose result already exists.

**5a. Install the `/research` skill** (lives at `~/.claude/skills/<name>/`):

- macOS/Linux (symlink → `git pull` updates propagate):
  ```bash
  mkdir -p ~/.claude/skills
  [ -e ~/.claude/skills/research ] || ln -s "$VAULT/_meta/skills/research" ~/.claude/skills/research
  ```
- Windows (symlinks usually unavailable — copy; re-copy after future pulls):
  ```powershell
  New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills"
  Copy-Item -Recurse "$VAULT\_meta\skills\research" "$env:USERPROFILE\.claude\skills\research"
  ```

**5b. Install kepano's obsidian-skills** (nice-to-have; on any failure skip
and note it in the summary):

```bash
TMP=$(mktemp -d)
git clone --depth 1 https://github.com/kepano/obsidian-skills "$TMP/obsidian-skills"
for s in obsidian-markdown obsidian-bases obsidian-cli json-canvas defuddle; do
  [ -d "$TMP/obsidian-skills/skills/$s" ] && [ ! -e ~/.claude/skills/$s ] \
    && cp -r "$TMP/obsidian-skills/skills/$s" ~/.claude/skills/$s
done
```

**5c. Record the vault in Claude's memory.** Append to `~/.claude/CLAUDE.md`
(create if missing), unless an equivalent block already exists:

```
## Math vault (math-agents)
- Math vault root: <VAULT absolute path>
- My vault handle: <HANDLE> (<FULL_NAME>)
- To ingest a paper: /research <url>. The research skill reads this path.
```

## Step 6 — Codex handle

Skip any sub-step whose result already exists.

**6a. Register the MCP server** (vault tools that work from any directory,
outside the sandbox):

```bash
codex mcp add obsidian-research \
  --env OBSIDIAN_VAULT_PATH="<VAULT absolute path>" \
  -- uv run --directory "<MCP absolute path>" obsidian-research-mcp
```

Use the absolute `uv` path if step 2 installed it fresh. If the `codex` CLI is
missing, write the equivalent directly into `~/.codex/config.toml` (create
folder/file if needed; forward slashes on Windows):

```toml
[mcp_servers.obsidian-research]
command = "uv"
args = ["run", "--directory", "<MCP absolute path>", "obsidian-research-mcp"]

[mcp_servers.obsidian-research.env]
OBSIDIAN_VAULT_PATH = "<VAULT absolute path>"
```

**6b. Set the approval mode — required.** In `~/.codex/config.toml`, inside
the `[mcp_servers.obsidian-research]` table, ensure:

```toml
default_tools_approval_mode = "approve"
```

`codex mcp add` does not write this key; without it every vault tool call
stops for manual approval.

**6c. Install the same research skill for Codex** (`~/.codex/skills/<name>/`,
same SKILL.md format as Claude):

- macOS/Linux: `mkdir -p ~/.codex/skills && [ -e ~/.codex/skills/research ] || ln -s "$VAULT/_meta/skills/research" ~/.codex/skills/research`
- Windows: copy the folder instead, as in 5a.

**6d. Record the vault in Codex's memory.** Append the step-5c block to
`~/.codex/AGENTS.md` (create if missing).

## Step 7 — (Optional) ChatGPT Desktop

Only if the user says they use ChatGPT Desktop with MCP connectors: hand them
the JSON from `codex/README.md` with both paths filled in. Don't try to edit ChatGPT's config yourself.

## Step 8 — Commit and push the registration

Only if step 4 registered a new handle:

```bash
cd "$REPO"
git add obsidian/_meta/tags.md "obsidian/People/<HANDLE>.md"
git commit -m "chore(onboarding): register <HANDLE> (<FULL_NAME>)"
git pull --rebase origin main
git push origin main
```

If the push is rejected (someone registered at the same moment), run
`git pull --rebase origin main && git push origin main` once more. If it still
fails (auth / no access): registration is complete **locally**; show the error
and say Maria (`@maumayma` on GitHub) needs to add them as a collaborator. Do
not retry further; never force-push.

This is the **only** pre-authorized push. Every later vault change follows the
normal rule: ask the human before committing.

## Step 9 — Verify

Run whichever apply to the tools present:

1. `ls ~/.claude/skills/research/SKILL.md` → exists.
2. `codex mcp list` → `obsidian-research … enabled`.
3. Codex round-trip (proves the whole chain):
   ```bash
   codex exec --skip-git-repo-check --sandbox read-only \
     "Call the obsidian-research list_notes tool with subdir='People' and report the filenames."
   ```
   Expect the People/ filenames, including `<HANDLE>.md`.
4. `grep "user/$HANDLE" "$VAULT/_meta/tags.md"` → the registration line.

## Step 10 — Welcome summary

Print, with real values:

```
✓ Repo:         <REPO>
✓ Registered:   #user/<HANDLE> (<FULL_NAME>) — committed & pushed
✓ Claude Code:  /research skill installed; vault path in ~/.claude/CLAUDE.md
✓ Codex:        obsidian-research MCP server + research skill; ~/.codex/AGENTS.md
→ Restart Claude Code and Codex so skills/servers load.
→ Open the vault in Obsidian: File → Open folder as vault → <VAULT>
→ Try it (either tool):  /research https://arxiv.org/abs/<id>
   …or just say: "add this paper to the vault: <url>"
Questions → Maria (#user/maumayma in the vault, @maumayma on GitHub).
```

## Stop conditions

- User declines to give a handle → stop; nothing works without it.
- Handle already registered **to a different name** → ask for another handle.
- `$VAULT/_meta` missing after clone → broken clone; re-clone, else stop.
- Push failure → report per step 8; never force-push, at most one retry.
