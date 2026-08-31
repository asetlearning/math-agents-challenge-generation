# Parity with the Claude `/research` skill

This server is designed to reproduce the Claude `/research` skill
(`math-agents/obsidian/_meta/skills/research/`) for any MCP client. This
document maps each piece of the skill to how it is achieved here, and lists the
deliberate differences.

## The three layers of the "research handle"

The Claude handle is three stacked layers. Only Layer 3 (runtime) is rebuilt;
Layers 1–2 are reused unchanged because they live in the vault.

| Layer | Claude implementation | This server |
|---|---|---|
| **Identity** | `#user/<handle>`, `People/<handle>.md`, `author:`, `Agents/<handle>/` | Unchanged — register the ChatGPT handle in the vault exactly like a human. |
| **Doctrine** | `researcher.md`, `_common.md`, `tags.md`, templates, workflows | Read **live** from the vault by `load_doctrine`. Not duplicated in code. |
| **Runtime/tools** | `SKILL.md` + `~/.claude/skills/` + `defuddle`/`WebFetch`/`obsidian` CLI | This MCP server's tools (filesystem, no Node/plugin). |

## Tool-by-tool mapping

| Skill capability (source) | This server |
|---|---|
| Read doctrine at session start (`SKILL.md` "Read it once at the start") | `load_doctrine` tool + `research` prompt (auto-injects it) |
| `defuddle <url>` fetch (`researcher.md` Toolbelt) | `fetch_paper` (defuddle if present, else HTTP) |
| Citation count lookup (single-paper workflow step 6) | `lookup_citation` (Semantic Scholar / arXiv) |
| Check prior coverage `grep -r ...` (step 2) | `search_vault` |
| Reuse existing tags before inventing (topic discipline) | `list_tags` |
| Enumerate notes in scope (connection-pass step 2) | `list_notes` |
| Read a note (connection-pass step 3) | `get_note` |
| Write summary via paper-summary template (step 14) | `write_note` |
| Append to agent log (connection-pass step 3) | `append_to_note` |
| Update note in place / template migration | `replace_in_note` |
| `domain:`/`status:` properties + connection graph (steps 10, 15) | `manage_frontmatter` |
| 6-axis tags (step 15) | `manage_tags` |

## Workflow parity

All four invocation modes are preserved and described in the injected doctrine
(the workflow files are loaded verbatim):

- **single-paper** — `workflows/single-paper.md`
- **batch** — `workflows/batch.md`
- **literature-scan** — `workflows/literature-scan.md`
- **connection-pass** — `workflows/connection-pass.md`

The `research` prompt tells the agent to pick the matching workflow based on the
request shape (one URL / many URLs / a topic / a `--reconnect` scope).

## Doctrine invariants enforced (via injected prompt)

- English-only vault; translations marked `[trans.]`; no original-language text.
- No code, no experiments, no invented quality verdicts, no invented relevance.
- Unique lowercase-kebab-case filenames (`<first-author>-<year>.md` etc.).
- Correct `Research/<Domain>/<Topic>/` placement (never at domain root).
- Mandatory `domain:` and `status:` **properties**, not just tags (Bases bug).
- Connection-graph frontmatter with **bidirectional** links.
- Substance-tested `#topic/*` tags; reuse before invent.
- Concept hubs only when a concept appears in 2+ papers.
- ≥3 outgoing wikilinks before a summary is "done".

## Deliberate differences from the Claude skill

1. **Filesystem, not the Obsidian REST API.** The skill (and cyanheads) can go
   through the Local REST API plugin; this server reads/writes files directly.
   Simpler install, no plugin, no API key. Trade-off: it does not trigger
   Obsidian UI actions or use the Omnisearch BM25 index — search is a
   substring/rank scan. Adequate for the doctrine's `grep`-style checks.
2. **No `nuextract-cli` OCR path yet.** Image-only PDFs are surfaced to the user
   as a blocker (same *stop condition* as the skill), but automated OCR is not
   wired in. Add later if needed.
3. **Model-agnostic.** The skill assumes Claude; here the *client* (ChatGPT,
   Claude, etc.) supplies the model. Doctrine is identical regardless.
4. **`defuddle` optional.** Used automatically if installed, but the server does
   not require Node — it falls back to a pure-Python HTML→text reducer.

## Verifying parity on your machine

```bash
# 1. Tools + prompt register, doctrine loads from the real vault:
OBSIDIAN_VAULT_PATH=/path/to/Obsidian/Math \
  uv run python -c "import asyncio; from obsidian_research_mcp import server as s; \
  print(sorted(t.name for t in asyncio.run(s.mcp.list_tools())))"

# 2. Test suite:
uv run pytest -q
```
