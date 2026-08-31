# obsidian-research-mcp

A tiny **MCP server** that gives **Codex and ChatGPT** (or Claude, or any MCP
client) the exact same **"research handle"** as the Claude `/research` skill in
[`ai-math-edu-lab/math-agents`](https://github.com/ai-math-edu-lab/math-agents):
it ingests academic papers into the shared Obsidian **Math** vault as
structured, connection-graph-rich summaries — following the *same* doctrine,
templates, taxonomy, and workflows.

It talks to the vault **directly on disk**. There is **no Node.js**, **no
Obsidian plugin**, and **no API key** to configure. If you can install one small
command-line tool, you can run it.

---

## What it does (parity with the Claude `/research` skill)

| Capability | Tool |
|---|---|
| Load the vault's Researcher doctrine (agent prompt + templates + taxonomy + the 4 workflows) | `load_doctrine` |
| Fetch a paper / web page as clean text | `fetch_paper` |
| Best-effort citation count (Semantic Scholar / arXiv) | `lookup_citation` |
| Check for prior coverage / find connections / reuse tags | `search_vault`, `list_tags`, `list_notes` |
| Read a note | `get_note` |
| Write a paper summary / synthesis / concept hub | `write_note` |
| Append (e.g. agent log) | `append_to_note` |
| Surgical text replace | `replace_in_note` |
| Connection-graph + `domain:`/`status:` properties | `manage_frontmatter` |
| Add/remove tags | `manage_tags` |
| The `/research` entry point (injects doctrine + your task) | `research` prompt |

The **behavior** (English-only `[trans.]`, no-code, no-experiments, unique
kebab-case filenames, `Research/<Domain>/<Topic>/` placement, mandatory
`domain:`/`status:` properties, bidirectional connection-graph links,
substance-tested `#topic/*` tags) is read **live from the vault** by
`load_doctrine`, so it stays in sync with whatever Maria updates — exactly like
the skill's symlink propagation.

---

## Install (for non-programmers)

You need two things: **`uv`** (a single-file tool runner) and a **local copy of
the Math vault**.

### 1. Install `uv` (one line, no admin needed)

**macOS / Linux** — paste into Terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** — paste into PowerShell:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

That's the only software install. (`uv` handles Python and all libraries for you
automatically the first time the server runs.)

### 2. Get this server

It ships inside the math-agents repo — if you followed `SETUP.md` you already
have it at `<math-agents clone>/codex` (workshop
default: `~/Desktop/math-agents/codex`). No separate
clone needed.

### 3. Tell Codex about it (recommended)

One command (fill in your two absolute paths):

```bash
codex mcp add obsidian-research \
  --env OBSIDIAN_VAULT_PATH="/ABSOLUTE/PATH/TO/math-agents/obsidian" \
  -- uv run --directory "/ABSOLUTE/PATH/TO/math-agents/codex" obsidian-research-mcp
```

Then open `~/.codex/config.toml` and add one line inside the
`[mcp_servers.obsidian-research]` table (without it, every vault tool call
stops for manual approval):

```toml
default_tools_approval_mode = "approve"
```

Verify with `codex mcp list` — the server should show as `enabled`. Restart
Codex; the `obsidian-research` tools are now available in every session, from
any directory, outside the sandbox.

> Setting this up by hand is unnecessary if you ran the math-agents `SETUP.md`
> onboarding — it does all of this for you.

### 3b. Tell ChatGPT about it

In **ChatGPT → Settings → Connectors / MCP** (Desktop app or a client that
supports MCP), add a server with this configuration. Replace the two paths with
your own.

```json
{
  "mcpServers": {
    "obsidian-research": {
      "command": "uv",
      "args": ["run", "--directory", "/ABSOLUTE/PATH/TO/math-agents/codex", "obsidian-research-mcp"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/ABSOLUTE/PATH/TO/Obsidian/Math"
      }
    }
  }
}
```

- `--directory ...` → the folder from step 2.
- `OBSIDIAN_VAULT_PATH` → your local copy of the **Math** vault root (the folder
  that contains `_meta/` and `_templates/`). That is the `obsidian/` subfolder
  of the math-agents clone — workshop default:
  `~/Desktop/math-agents/obsidian`. **Not** the repo root.

Restart ChatGPT. You should see the `obsidian-research` tools appear.

> The same JSON works for **Claude Desktop** (`claude_desktop_config.json`) if
> you'd rather use it there.

### 4. (Optional) read-only mode

Add `"OBSIDIAN_READ_ONLY": "1"` to `env` to disable every write tool — good for
a first trial run where the agent can look but not touch.

---

## How to use it

Start any chat with:

> **Use `load_doctrine` first, then help me add this paper to the vault:
> https://arxiv.org/abs/2410.12345**

Or invoke the **`research`** prompt directly if your client exposes MCP prompts —
it pre-loads the doctrine and takes your request, just like typing `/research`.

The four modes match the skill exactly:

- **Single paper** — one URL/ID → one summary.
- **Batch** — several URLs → one summary each, cross-linked.
- **Literature scan** — a topic → the agent proposes sources, you approve, it
  ingests + writes a synthesis.
- **Connection pass** — "re-link all the Burnside papers" → retag / re-link
  existing notes, no new ingest.

---

## Optional: better paper extraction with `defuddle`

The server fetches papers with plain HTTP by default (works everywhere). If you
*also* install [`defuddle`](https://github.com/kepano/defuddle-cli)
(`npm install -g defuddle`, needs Node), `fetch_paper` will automatically prefer
it for cleaner extraction. This is **optional** — the server works fine without
it.

---

## Safety

- The server can only read/write **inside** `OBSIDIAN_VAULT_PATH`. Any path that
  tries to escape the vault root is rejected.
- `OBSIDIAN_READ_ONLY=1` disables all writes.
- The vault is under your own version control; review diffs as usual.

---

## Development

```bash
uv run pytest        # run the test suite
uv run obsidian-research-mcp   # start the server over stdio (for manual testing)
```

See [`docs/PARITY.md`](docs/PARITY.md) for the point-by-point mapping between
this server and the Claude `/research` skill.
