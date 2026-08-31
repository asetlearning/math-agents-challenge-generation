# Math vault — agent context (Codex and other AGENTS.md-reading tools)

This repo contains the shared **Math** Obsidian vault — a multi-user,
multi-domain research wiki (group theory, AI, CS, methodology). The vault
lives at `obsidian/`; the repo root holds onboarding files only.

## First-time user?

If the user is not yet registered (no `#user/<their-handle>` in
`obsidian/_meta/tags.md`), read **`SETUP.md`** at the repo root and execute
it. It installs the research handle for both Claude Code and Codex, asks the
user one question (name + handle), and registers them in the vault.

## Adding a paper to the vault (the main workflow)

Preferred route: the **`obsidian-research` MCP tools** (registered by
SETUP.md). They work from any directory, outside the sandbox:

1. Call `load_doctrine` FIRST — it returns the Researcher rules, templates,
   taxonomy, and the four workflows, read live from this vault. Follow it
   verbatim.
2. Then `fetch_paper`, `search_vault` (check prior coverage), `list_tags`
   (reuse before inventing), `write_note`, `manage_frontmatter`,
   `manage_tags`, `lookup_citation`.

If the MCP tools are unavailable, operate on the vault directly on disk
following the same doctrine, which lives at:

- `obsidian/_meta/agents/researcher.md` — the Researcher prompt (source of truth)
- `obsidian/_meta/tags.md` — 6-axis tag taxonomy
- `obsidian/_templates/paper-summary.md` — exact output structure
- `obsidian/_meta/skills/research/workflows/` — single-paper / batch /
  literature-scan / connection-pass

## Non-negotiable conventions

- Every note: `author: <handle>` frontmatter, and tags for **agent, user,
  domain, topic(s), status** (5 axes minimum; `#project/*` optional sixth).
- Registered `#domain/*` values only (`group-theory`, `ai`, `cs`,
  `methodology`); new domains are registered in `tags.md` first, never invented.
- **English-only vault**: translate quotes/abstracts, mark them `[trans.]`,
  record the original in `language:` frontmatter.
- Unique kebab-case filenames; placement under `Research/<Domain>/<Topic>/`.
- Every `Research/` note ends with `## Related material` — ≥3 substantive
  wikilinks (parent overview, MOC, siblings).
- Never write into another user's `obsidian/Agents/<other-handle>/` subtree.
- **No commits without explicit human approval** (the one exception: the
  registration commit inside SETUP.md).

## Where things are

```
<repo-root>/
├── README.md          ← human-facing walkthrough
├── SETUP.md           ← agent-executed onboarding (Claude + Codex)
├── claude/CLAUDE.md   ← the same context, for Claude Code
├── codex/             ← this file + the obsidian-research MCP server
└── obsidian/          ← THE VAULT (operate here)
    ├── _meta/       doctrine: taxonomy, agent prompts, conventions, skills
    ├── _templates/  paper-summary, concept-note, synthesis, …
    ├── Research/    paper summaries + MOCs + syntheses
    ├── Concepts/  Experiments/  People/  Agents/<handle>/  Architecture/
```

When unsure what the user wants: new user → `SETUP.md`; paper in hand →
the workflow above.
