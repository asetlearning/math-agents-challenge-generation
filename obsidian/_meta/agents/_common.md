---
name: math-common
description: Shared conventions for every agent on the Math canvas. Architecture-neutral; project specifics come from project profiles. Read first, every session.
---

# Common Conventions (all roles)

## Project context

- **Vault root and code checkouts:** resolved from the human's own agent config (`## Math vault — local checkouts` in `~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md`), per [[projects-and-dependencies-convention]] § Local checkouts. Never hardcode a machine path in a vault note.
- **Active project:** every task brief from Lead names a **project profile** (`_meta/projects/project-<name>.md`). Read it, and the dependency notes it lists (`_meta/dependencies/`), before running or editing code. The profile supplies repos, build/test/run commands, the `runs/` layout, provenance fields, protected interfaces, hot paths and vault doc locations. No profile in the brief → ask Lead.
- **Projects & dependencies convention:** [[projects-and-dependencies-convention]]
- **Mission & invariants:** [[mission]]
- **Tag taxonomy:** [[tags]]
- **Canvas setup:** [[canvas-setup]]
- **Experiment folder convention:** [[experiment-folder-convention]]
- **Project TODO list:** [[project-todo-convention]] — each project's private, ordered queue of things to try (profile key `vault_docs.todo`). **Lead owns it; everyone else reads it.** Want something added? Send Lead a `REQUEST`. Briefs cite items by `T-id`.

## No unsolicited initiative

On wake (any new session, "run protocol", any vague greeting): perform the **Cold-Start Handshake** in your role file. That is the entire wake-up routine.

You do **not** on wake:
- write to any log
- send `maestri ask` messages to peers (other than the single ack the human asked for, if any)
- read the repo, scan the vault beyond what your role file says, or pre-load context speculatively
- offer status updates, plans, or "here's what I noticed" reports

You wait. The human tasks you. Then you act.

## Probe before assuming

Setup docs (canvas-setup, role files, mission) describe the intended tooling state at some prior moment. They can drift. Before declaring a tool unavailable, run `which <tool>` or the tool's `--version` check. Before declaring a directory absent, `ls` it. Before declaring a file's contents stale, `grep` for current usage. The vault is durable; the world isn't. Trust verification over assertion.

**Grep-before-cite.** Before including any `file:line` reference in a note, message, or doctrine edit, run `grep -rn "<path-or-symbol>" <repo-root>` (or equivalent) to confirm it exists and matches what you claim. A citation in a vault note or commit message is a fact-claim; unverified, it is invention. If grep returns no results, do not include the citation. If you have a hypothesis but can't verify it, mark it `(unverified)` or `(TODO: verify file:line)` and route it back to Lead for confirmation. This applies to all roles, including Lead.

## Verification ≠ experiment

Some kinds of "verification" tasks are actually experiment-shaped. Distinguishing them matters because the experiment program owns the open research questions; Validator (or any other role) attempting to solve them via "verification" would scoop the experiment.

- **Verification**: takes a *pre-existing artifact* (a claimed reduction chain, a specific group-equality assertion between two given words, a documented invariant) and checks whether it is sound, using available tools as oracles. Does not generate new mathematical content.
- **Experiment**: takes an *open question* (e.g. "is `comm_12_9` equal to identity in B(2,5)?") and tries to answer it. Generates new mathematical content.

Concrete examples for the B(2,5) program:
- ✅ Verifying that the 7,245-char reduced word equals the 28,652-char input under the rules Experimenter-B25 documented — **verification**.
- ✅ Running an established external tool (from the dependency registry) as a black-box oracle on a specific word-equality check — **verification**.
- ❌ Attempting to prove a B(2,5) target word equals identity — **experiment** (this is the open research question of the entire B(2,5) program).
- ❌ Searching for new (unknown) reductions, running beam search on a target — **experiment**.
- ❌ Reimplementing an established tool's semantics yourself because it isn't installed (or is believed not to be installed) — **brute-force tool substitution**, forbidden; escalate the install request instead.

If a routed task, when scoped honestly, would require solving an open research question, send it back to Lead with the boundary stated: "this is the experiment program's job, not mine."

## Terminology — "agent" is overloaded

- **AI agent** (default meaning) = an LLM agent on this canvas. **Seven roles**: Lead, Researcher, Developer, Experimenter, Experimenter-B25, Validator, Math Expert.
- **Algorithm process / component** = a program under test (a solver, a reducer, a search process). Some projects have their own name for it (defined in the project profile); use the project's qualified term, never bare "agent".

When in doubt, qualify.

## Topology — hub-and-spoke through Lead, with one exception

- **Lead Dev** is the human's interface and the *only* AI agent that runs `git commit` / `git push`.
- Researcher, Developer, Experimenter, Experimenter-B25 route work-changing requests through Lead.
- Read-only peer Q&A allowed.
- **Exception — Validator's math verdicts**: when Validator says a math result is `#status/disproven` or otherwise wrong, that verdict overrides any other agent's claim *immediately*, without waiting for Lead routing. The other agent must freeze any work building on that result and surface to Lead. Lead can't override Validator on math correctness; only the human can.

## Communication protocol (inter-AI-agent handoff)

When messaging a peer via `maestri ask "<Name>" "..."`:

```
TYPE: <REQUEST | REPORT | QUESTION | BLOCKER | VERDICT | ACK>
FROM: <your canvas name, e.g. Lead, Experimenter-B25>
TOPIC: <one line>
PROJECT: <[[project-<name>]] — mandatory on any REQUEST that involves code, runs or experiments>
CONTEXT: <wikilink>
ASK: <what you need, or "FYI">
DEADLINE: <none | needed by <event>>
```

`VERDICT` is reserved for Lead's code reviews and Validator's math verdicts. `ACK` is a short acknowledgement of a received message (received, understood, will do); it carries no new request or result, and `ASK:`, `CONTEXT:`, `PROJECT:` and `DEADLINE:` may be omitted. Long context in linked vault notes, not in the message. Keep `TYPE:` as the first header line and always fill `FROM:` — the message-log hook uses them to recognize and attribute incoming messages.

### Message log (automatic)

Every inter-agent `maestri ask` is recorded in a shared, append-only message log. **Claude Code hooks write it deterministically** — you don't append to it yourself.

- **Location:** `Agents/<your-user>/_shared/message-log-YYYY-MM.md` — one file per month. `_shared/` is the per-user folder for data all roles share; like the rest of `Agents/`, it is gitignored and never committed.
- **Writer:** `claude/hooks/maestri_message_log.py` (repo root), installed per machine in `~/.claude/settings.json` — see [[canvas-setup]] § Step 7. It runs only inside Maestri terminals.
  - `SENT` — sender side, before each `maestri ask` runs (one line per target; `--batch` included, `--raw` skipped).
  - `REPLY` — sender side, after the `ask` returns: the synchronous answer, or `(no reply: …)` on timeout/error.
  - `RECV` — receiver side, when a prompt whose header contains `TYPE:` arrives.
- **Entry format** — one line, header fields + ASK (the body stays in linked notes):

  ```
  - 2026-10-13 14:05:12 | SENT | Lead → Developer | REQUEST | <TOPIC> | <PROJECT or -> | <CONTEXT or -> | ASK: <one line, truncated>
  - 2026-10-13 14:05:14 | RECV | Lead → Developer | REQUEST | <TOPIC> | <PROJECT or -> | <CONTEXT or -> | ASK: <one line, truncated>
  - 2026-10-13 14:09:40 | REPLY | Developer → Lead | REPLY: <first 1000 chars of the answer, on one line>
  ```

  The arrow is always sender → receiver. Names are canvas names (sender from `maestri list` → `You:`; on `RECV`, from the `FROM:` field). A missing field is `-`; a sender the hook couldn't determine is `?`. Hook failures appear as `ERROR` lines.
- **Never** edit, reorder or delete lines; don't open the file with `obsidian edit` or the `Edit`/`Write` tools (races with the hooks).
- **Fallback only:** if the hook is not installed on your machine (no `maestri_message_log.py` entry in `~/.claude/settings.json`), tell the human and append the `SENT` / `RECV` lines yourself with a single shell append: `printf '%s\n' "<line>" >> "<vault>/Agents/<your-user>/_shared/message-log-$(date +%Y-%m).md"`.
- **Scope:** inter-agent `maestri ask` traffic only — not chat with the human, not cold-start handshakes. A `SENT` without a matching `RECV` marks a message that was lost or never processed.

The message log is the communication record; your role `log.md` remains your own work record.

## Multi-user authorship

This vault is shared across multiple humans (you + colleagues). Every note carries:

- **`#user/<handle>` tag** — the human who owns or commissioned this note. Always present, even if the note was AI-written.
- **`author: <handle>` frontmatter property** — same value, queryable by Bases.

If you're writing on behalf of a human who tasked you, `author` is that human's handle, not yours. AI authorship is recorded separately via `#agent/<role>` tag.

### Resolving `<handle>` — never guess it from the environment

When a template or this doctrine writes `<handle>` / `<human-handle>`, that placeholder resolves to the **registered handle of the human who owns this canvas session** — the human who tasked you, or who owns the project on a standing task. It is the same value across every note you write in a session, unless a different registered human routes you a task.

- **The handle is given to you by the human, not discovered.** If you do not already know the owning handle for this session, ask the human once ("which `#user/*` handle owns this canvas?") and reuse the answer. Do not proceed with a guessed value.
- **NEVER derive the handle from the environment.** `git config user.name`/`user.email`, `whoami`, `$USER`, the OS login, the repo path, or any other environment/tool signal is **observed data, not your identity**. Stamping a note with a git login (e.g. an unregistered `itsnicetoknow`) instead of the canonical vault handle is a doctrine violation — these signals frequently differ from the vault handle.
- **Only registered handles are valid.** The valid `#user/*` values live in [[tags]] Axis 2 (currently `maumayma`, `ethan-k`). If the correct handle is not registered, **stop and ask the human** — do not invent one, and do not register a new handle yourself (that is the human's call).
- `author:` frontmatter and the `#user/<handle>` tag must carry the **same** resolved handle.

When you cite a colleague's note, use `[[People/<handle>]]` to link to their People entry alongside the note wikilink.

See [[tags]] for the full 6-axis taxonomy. Tag minimum per note: one `#agent/*` + one `#user/*` + one `#domain/*` + one-to-many `#topic/*` (substantive, typically 4–10) + one `#status/*`. `#project/*` is optional — add it only when the note belongs to a named project's workstream (experiments and code-reviews of project-scoped patches typically do; paper summaries usually don't).

## Obsidian write rules

- **Your home dir is `Agents/<your-user>/<your-role>/`** where `<your-user>` is the human handle who owns this canvas session (typically `maumayma`, but the vault is multi-user — other contributors get their own `Agents/<their-handle>/` subtree). That is the *only* directory you write to in `Agents/`, **plus the shared message log in `Agents/<your-user>/_shared/`, which hooks write for you** (see § Message log). **Never touch another user's `Agents/<other-user>/` subtree, and never touch another role's dir within your own user subtree** — not their `log.md`, not their scratch, nothing. If you have something for them, send via `maestri ask`; they own deciding whether to record it in their `log.md`.
- **Path qualification with obsidian-cli is mandatory.** When using `obsidian append/edit/create`, pass the **full vault-relative path** (e.g. `Agents/maumayma/Experimenter/log.md`), not just `log` — multiple `log.md` files exist and name-resolution will pick the wrong one. Read the result back to confirm.
- **Researcher has restructure authority** over `Research/` and `Concepts/`: may retag/move any note in those subtrees when a better organization emerges. Must log every restructure in `Agents/<owning-user>/Researcher/log.md` with before/after. This authority is unique to Researcher. Other agents only touch their own home dirs.
- **Validator may add tests** to the project codebase (test paths named in the project profile) and write proof sketches to the profile's `vault_docs.math_validation` folder. Doesn't touch other Architecture areas.
- Keep your `log.md` append-only.
- Templates in `_templates/`. Use them.
- Wikilinks > paths.
- Tags mandatory per [[tags]] (6-axis minimum: agent + user + domain + topic + status; project optional).
- Frontmatter mandatory on templated notes.
- Prefer the `obsidian` CLI (requires Obsidian open + CLI enabled) — *with full paths*. Or use the `Write`/`Edit` tools directly.
- Never paste >50 lines of logs into chat — save to a vault note and link.

## Dual-audience writing convention (K3 pattern)

Architecture / Components / Experiments / Research / Concepts notes serve **two readers**: humans (you + colleagues) and AI agents. Both need different things from the same file. We use the **K3 pattern**:

- **Frontmatter is the agent layer.** Structured properties — `public_api`, `invariants` (list of `{id, summary, why}`), `hot_path`, `domain`, `project`, `status`, `related`, `tests`, `author`. Agents and Bases read frontmatter directly.
- **Body is the human layer.** Pure narrative — **What it is**, **Why it exists**, **How it fits**, **Critical invariants — why each one exists**, **Public surface** (plain English), **Hot path?**, **Tests**, **Related**, **Recent changes**.
- **No `TypeName (file:line)` lists in body.** That goes in frontmatter `public_api`.
- **Why-paragraphs mandatory for invariants.** Bare invariant statements without rationale teach nothing.
- **Upstream code and docs (a repo's own `CLAUDE.md`/`README.md`, library manuals) are canonical for the full API surface.** The vault links to them and doesn't duplicate them.
- **External dependencies are never edited in place.** Each dependency note (`_meta/dependencies/`) states its `ownership` (we-own / upstream-pristine / upstream-with-accepted-patch) and any accepted local patch. For example, [[dep-kbmag]] records the one accepted biasing patch in `kbmag_source/`. Everything a dependency note marks pristine stays bytewise pristine.

Dashboards are built with **Obsidian Bases** (`.base` files) in the project's docs folder (`Architecture/<Project>/Bases/`). Bases queries frontmatter for filtered/sorted views.

### Templates following K3
- [[component-doc]], [[experiment]], [[paper-summary]], [[concept-note]], [[synthesis]], [[decision]], [[code-review]]

When in doubt: **structured data in frontmatter, prose in body, never both in body**.

## Validator's verdict layers

When Validator returns a verdict on a math claim:

- `#status/proven` — rigorous proof exists (link to it). Code or experiment building on this can proceed with confidence.
- `#status/replicated` — empirically confirmed (multiple seeds, multiple runs); not proven theoretically.
- `#status/conjectured` — claimed without verification; flagged for Validator follow-up.
- `#status/disproven` — Validator found a counterexample or contradiction. **All work depending on this stops until the underlying claim is reformulated.**

Other agents respect these labels. If you find a claim tagged `#status/disproven`, you may not cite it as evidence.

## Token discipline

- `defuddle <url>` for web reads (especially math papers — defuddle handles arxiv well).
- `nuextract-cli <pdf> <schema>` for image-only / scanned PDFs (when available — see [[ocr-tooling]]).
- RTK auto-rewrites `git`, `cargo`, `ls`, `find`, test runners — prefix shell
  commands with `rtk` (`rtk git status`, `rtk ls <path>`, `rtk grep -rn ...`) for
  60-90% fewer tokens on the same result. Check it exists once per session
  (`command -v rtk`); if missing, just run commands normally, don't block on it.
  **Never wrap mathematical computation (CAS sessions, solvers, your own scripts) in `rtk`** — it's
  for file/repo inspection only; mathematical output must reach you verbatim and
  complete. Known edges: `rtk find` rejects compound predicates (`-not`, `-exec`)
  and mishandles paths with spaces (e.g. `Research/Group theory/...`) — use plain
  `find` for those. `rtk proxy <cmd>` gives raw unfiltered output when needed.
  `rtk gain` shows savings.
- `Read` with `offset`/`limit` for huge files. `Grep` with context.

## Git safety

- Agents never commit the vault and never run `git init` inside it (vault commits are a human decision).
- Only Lead commits. Others never run `git commit`, `git push`, `git rebase`, `git config`.
- Working branches: `feat/<topic>`, `fix/<topic>`, `chore/<topic>`. Never `main` directly.
- Forbidden: `git push --force`, `git reset --hard` on shared branches, `--no-verify`, `git config --global`.

## Compute budget — HARD GLOBAL CAP (all agents, non-negotiable)

**MAXIMUM 4 heavy compute processes running in parallel, TOTAL, ACROSS ALL AGENTS — not per agent.**

- "Heavy compute process" = any long-running solver/search/algebra/training process: every name in the
  active project profile's and its dependency notes' `heavy_processes` lists, plus any search, training or
  equivalent CPU-, RAM- or GPU-bound run not listed there.
- The cap is **4 in total, shared across the whole canvas** — Lead, every Experimenter, Developer,
  Validator combined. Not 4 each. If 4 are already running anywhere, you may NOT start a 5th — wait,
  or coordinate via Lead to free a slot.
- **Before launching any heavy process, CHECK first:** `pgrep -fl '<heavy_processes joined with |>'`
  (plus any other heavy binary) to count what is ALREADY running across all agents. If the count is ≥ 4,
  do not launch. This is mandatory — the canvas has overrun to 20+ parallel heavy processes at once
  (2026-06-26), saturating the machine. That must never recur.
- **Never spawn a batch of parallel runs.** Scoring/sweeping many items (e.g. reducing N fragments,
  beam-reducing K centralizer elements) must be done **sequentially within a single process**, or in a
  pool bounded to fit inside the global 4-cap — NOT one OS process per item.
- Lead is responsible for the global count: if routing work to multiple agents, Lead ensures the sum of
  their heavy processes stays ≤ 4, and serializes if needed.
- After any run: kill the process and `pgrep`-verify clean (already required under Process hygiene).
- If a task genuinely needs more than 4 parallel processes, that is a request to escalate to the human
  (Maria) — never self-authorize exceeding the cap.
- **Scope: the cap is local to the agents' machine (the VM).**
  - **Remote jobs don't count.** A job submitted to a remote host through a project's remote runner (e.g. `rjob`, see the profile's execution policy) runs under that host's own scheduler slots, and the host enforces them.
  - **Not heavy:**
    - the client calls (`rjob submit|status|wait|fetch`);
    - a background `rjob wait`.
  - **Still check disk** before fetching large outputs.
  - **Moving heavy work remote:** if a project's execution policy says a run belongs remote, run it remotely rather than squeezing it into the local cap.

### Memory cap and rjob fallback (mandatory; owner 2026-10-16)

On 2026-10-15/16 an unbounded 6-worker Python job on the VM used ~4.6 GB of RAM and swap. The kernel OOM killer then killed `maestri-app` twice, which took every agent session down with it. Maestri's processes carry oom_score_adj 200–300, so the kernel prefers them over the job that is actually using the memory. To prevent this:

- **Every local run that is not trivial goes through `capjob`** (`~/.local/bin/capjob`): any script, `uv run python …`, enumeration, search or test suite expected to run longer than ~1 min or to use more than a few hundred MB. Only one-liners (`python3 -c` checks, `git`, `rjob`, `pgrep`) are exempt.
  ```
  capjob [--mem 2G] [--swap 1G] [--cpus 2] [--out DIR] [--rjob JOB.toml] -- CMD ...
  ```
  It runs CMD in its own systemd scope capped at `--mem`, `--swap` and `--cpus`, with oom_score_adj 1000, so the job dies instead of Maestri. Thread variables (OMP/MKL/OPENBLAS/RAYON, `RJOB_CPUS`) default to `--cpus`. Never raise the caps above 2G / 2 CPUs locally. A run that needs more belongs on `rjob` from the start (execution policy: over ~30 min, 2 GB or 2 cores).
- **Fallback when the cap kills the job:** exit code 75 or 76, with `CAPJOB:` lines on stderr.
  - `--rjob JOB.toml` given: capjob submits that spec. Exit 76 and the job id are printed.
  - Otherwise capjob writes `<project>/jobs/capjob/<name>-<stamp>/job.toml` and submits it automatically (exit 76) when it is safe: the code is committed and the tree is clean, `--out` names the results directory, and no argument is an absolute path outside the repo.
  - If any of those is missing, it leaves the draft and exits 75. **You must then finish the draft** (commit the code, move inputs into `[run] files` or `[data]`, set `outputs`), `rjob submit` it, and tell Lead. Never re-run the killed job locally with a bigger cap.
  - So: commit before running, and always pass `--out`. That makes the fallback automatic.
- **Pools count against the cap:** a multiprocessing pool shares the one `--mem` and `--cpus` budget. Size pools to `RJOB_CPUS`, not to `os.cpu_count()`.
- After an exit-76 fallback, track the job with `rjob wait <id>` (background) and `rjob fetch <id>`, and cite the job id in the experiment note.

## Implementation language: C++ core, Python interface (mandatory; owner 2026-10-16)

1. **Every algorithm or procedure that can run in a heavy experiment is implemented in C++** in the project's C++ core (for challenge-gen: tcgraph, see [[dep-tcgraph-agentic]]). Examples: search, attachment and candidate generation, gates, power tests, reduction, compression and closure, certificate minimisation, diagram folding and depth, guards and novelty checks.
2. **Group-theoretic algorithms belong in C++** (word, relator, certificate and diagram algorithms), unless the code is a temporary proof of concept or a test.
3. **Prototypes may be written in Python** to test and refine an idea. They must be **ported to C++ before any large-scale experiment** uses them. "Large-scale" means any full run, sweep or rjob job, or anything over the local smoke size. The Python prototype stays as the reference implementation: the port ships with equivalence tests (Python vs C++ on the same inputs, identical results) and a timing comparison.
4. **Python is the interface:** bindings (for tcgraph, `tcgraph_ext`), orchestration, configs, analysis and plots. Any C++ algorithm an experiment needs gets a Python binding.

Consequences:
- An experiment plan whose heavy loop runs in Python is a prototype plan. Lead does not approve a full run on it, and the port is planned first.
- Developer owns the C++ ports and bindings (on branches, with the tcgraph submodule pin bumped in b25). Validator cross-checks the math layer, including the Python-vs-C++ equivalence on property tests.
- Background (2026-10-16): T-018's search, gates, compression and diagram statistics were pure Python, so the full run needed up to 16 h on 9 Mac cores. tcgraph was used only for 2.5-reduction.

## Test discipline (mandatory)

- New algorithm / component → tests showing it runs end-to-end on a small problem.
- Bug fix → regression test that fails before / passes after.
- Any change → the active project profile's `test` command + `smoke` check, plus the rows of its **Test matrix** that apply.
- New orchestration / policy component (scheduler, transform, search heuristic, …) → unit test + an experiment showing the expected behavior.
- **Math layer changes** → Validator owns testing this layer. Developer ships behavior tests; Validator ships property/cross-verification tests.
- "Not testable" must be argued explicitly to Lead.

## Reproducibility (specific to experiments)

- Every experiment run produces output in the profile's `runs_dir` — by default **`runs/<project>/<experiment>/<timestamp>/`** in the project's code repo (project-scoped to avoid clobber between Experimenters). **Never delete `runs/`** without explicit human approval.
- **Provenance record** = code SHA of each of our repos involved + environment lock hash(es) + version/SHA of every dependency exercised (with local patches) + tool/binary versions + where it ran. The project profile's `provenance_fields` may add more (e.g. the mixer-core build hash). Full definition: [[projects-and-dependencies-convention]] § Provenance record. Record it in every experiment note.
- Random seeds: log them. If an experiment isn't deterministic, document the noise floor.
- **Persist expensive corpus-independent artifacts.** Any costly artifact whose computation does NOT depend on the specific corpus/query — BFS/Cayley distance tables, `EpimorphismPGroup`/PcGroup builds, confluent rule banks, FSA tables — MUST be saved to `runs/<project>/<experiment>/<timestamp>/` with its provenance record, so later runs (fresh-corpus re-tests, compound features, follow-ups) reuse it as a cheap lookup instead of recomputing. Rationale: a ~62-min `Q5 = B₀/γ₆` BFS (9.77M states) was discarded and would have been needlessly re-run just for a fresh-corpus validation (2026-06-29). Corpus-independent ≠ throwaway.

## Datasets (all roles)

Reusable data (challenge sets, corpora, relator banks, labelled sets) is registered as a **dataset note** in `Datasets/<Domain>/<Instance>/`, per [[datasets-convention]] (template [[dataset-note]]).
- **Cite datasets by their note, never by a bare path.** Verify the file's sha256 against the note before use and record it in the provenance; a mismatch is a stop condition.
- **Datasets are immutable.** A changed file is a new dataset with `supersedes:`; never edit a registered file in place.
- **State the object of every vetting check** (free group proof vs finite-quotient consistency vs syntactic). Don't let a dataset's name or `property_claimed` overstate what was checked.
- Committing a registered dataset file (the vault repo's `data/`, ≤ 10 MB; the fork, never the original math-agents) is a human gate, like any commit. Add it by name; parent and intermediate files stay untracked.

## Done = verifiable

- Claims of "faster", "converges", "scales" → numbers, not adjectives.
- Cross-verification when claiming a math result: an independent established tool chosen from the dependency registry by its `capabilities` (see [[validator]] § Choosing oracles), property tests, hand proofs. **Validator owns this layer.**
- Unknown? Ask via Lead. Don't invent.

## Stop conditions

Escalate to Lead (Lead escalates to the human as needed) when:

- About to change any **protected interface** listed in the active project profile (e.g. a protocol, ABI, public API or on-disk format) → escalate immediately, breaking change.
- About to add a dependency → human gate, no exceptions.
- Tests fail unexpectedly for >20 min.
- An experiment produces a result that contradicts a published theorem → triple-check, then surface to Validator first, then Lead.
- A note you're about to write conflicts with a note tagged `#status/disproven` → stop, surface to Lead.
- About to touch a file outside your declared scope.
- You need a tool that isn't installed → request the install and **keep working a
  branch that doesn't need it** while waiting, don't park the whole task.
- A single thinking turn runs past ~30 minutes with no computation in it → you're
  theorizing when you should be enumerating. Stop, run something small, let the
  output redirect you.

## Rigor and persistence doctrine

Lessons from a related program's failure mode, generalized: a crew can be so
well-defended against a false positive that it produces zero true positives either.
Both failure directions are treated as equally fatal here.

### Five ways to be wrong

Named so you can catch yourself:

1. **Solving a different problem.** Computing in a finite quotient, a restricted
   variant, or a slightly-restated version, then reporting on the original. State
   exactly which object you computed in, and whether it's proven equal to the target.
2. **Circularity.** Testing objects constructed from the assumptions being tested —
   the test passes by construction and proves nothing. Trace where every object in a
   computation came from before trusting the output.
3. **Necessary mistaken for sufficient.** An invariant that must hold if a claim is
   true, holding, is not the claim being true (abelianization is blind on `[G,G]`).
   For every check, state what a pass proves and what it does not.
4. **It's already known.** Spending hours rediscovering a proven theorem, or "solving"
   something already closed elsewhere. Literature check first, before any thinking.
5. **Walking away from the answer.** Reasoning to a candidate, then not building or
   testing it — or abandoning a live line too early. Before writing any report, answer:
   "what is the cheapest computation that could still close this, and why haven't I
   run it?" If there's no answer, run it instead of writing.

### Compute — run it, don't ask

- **Under 10 minutes wall-clock: just run it.** No permission needed. Log the command
  and output, move on.
- **10 minutes to 2 hours:** run it, and send a one-line status report *while it's
  running* — informing, not asking.
- **Over 2 hours, or over ~8 GB RAM:** say so before starting, since it may collide
  with another agent's job.
- Always use `timeout` / an explicit wall-clock cap on any run.

### `BLOCKER` means one thing

A blocker means **"I cannot run the mathematics"** — a missing tool, an unresolvable
path, a genuine contradiction in a problem statement. It does not mean a wrong
`author:` field, a path string you'd prefer differently, or a typo. If you can keep
doing mathematics, it isn't a blocker — note it and carry on.

### Judging is not certifying

Every agent judges mathematics — you're all reasoning about groups, and pretending
otherwise makes you useless. State opinions and why: this line looks live, that lemma
smells wrong, this reduction drops a hypothesis that mattered. What's reserved to
Validator is **certification** — moving a claim's status. Use hedged language for your
own conclusions ("I think," "this looks like," "my reading is"); certification words
("proven," "verified," "confirmed," "correct") belong to Validator alone, regardless of
your role. Disagreeing with a Validator verdict is allowed — say so, with reasoning; a
verdict stands until Validator changes it or the human intervenes.

### Additional forbidden actions

Beyond what's forbidden above: reporting that no candidate exists when your own log
contains one you didn't test. Declaring a line of attack over — you don't have that
authority; report where you actually are and let Lead/the human decide what ends.
Inventing a rule that forbids a construction (a novelty bar, an elegance bar) that
isn't in the problem statement itself. Returning unspent time/budget without having
spent it on the actual mathematics.
