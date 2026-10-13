---
tags: [meta, convention]
---

# Project TODO convention

A **project TODO list** is an ordered, living queue of things to try in a research project — ideas, methods, directions, checks — at any level of detail, from "try RL on the scoring" to "re-run X with BPE tokens". Each item may later get its own plan, experiment or patch. It is different from a plan (one item, worked out) and from the progress note (what happened). The split is:

| Artifact | Holds | Owner | In git? |
|---|---|---|---|
| TODO list | **intent + priority** — what to try next and why | Lead (with the human) | **No** — private until published |
| `_progress.md` | **outcomes** — what was tried, what worked, what's stuck | the project's Experimenter | yes |
| experiment / dataset / concept notes | the learned facts and data themselves | their usual owners | yes |

The TODO list is know-how. It stays **private** until the human decides to publish it.

## Location and privacy

- **Private (source of truth):** `Agents/<handle>/Lead/todo/todo-<project>.md` — one file per project, inside Lead's home dir. `Agents/*` is gitignored, so the file never reaches git; it is visible in Obsidian to the owning human. Never move it, copy it, or quote it into a tracked note except through **Publishing** below.
- The project profile records both paths: `vault_docs.todo` (private) and `vault_docs.todo_published` (tracked snapshot). See [[project-profile]].
- Template: [[project-todo]].

## Format

- **Queue (ordered)** — a numbered list; **position is priority**. Each item:
  - stable ID `T-<nnn>` — never reused, never renumbered (`_progress.md`, briefs and experiments cite it);
  - title; `level: high | low`; `status`; `source: human | notes | math-expert | researcher | experimenter | lead`;
  - optional flags: `pinned` (human-fixed position), `private` (never published), `needs-validation` (math idea not yet cleared by Validator);
  - 1-3 lines of why / sketch, nested sub-ideas, links (plan, experiment, extracted idea, source note).
- **Statuses:** `open` → `active` → `resolved-positive` | `resolved-negative`; also `blocked`, `dropped`.
- **Resolved** — items move here with date, verdict, one-line outcome and links to the `_progress.md` log entry and result notes.
- **Change log** — append-only one-liners: `YYYY-MM-DD <who>: <change> — <reason>`.

## Access

| Actor | TODO file | What they do |
|---|---|---|
| Human | read / write | Adds, edits, pins, reorders; final authority on order and on dropping; asks Lead to add items or pull them from notes; triggers publishing. |
| **Lead** | **read / write (owner)** | Adds and reorders items while doing tasked work; marks items `active` when briefing an agent; moves resolved items to **Resolved** after the routing checklist; logs every change; reports the diff to the human. |
| Experimenter, Experimenter-B25 | read | Work the `T-id` named in Lead's brief; on resolution summarize it in `_progress.md` citing the `T-id`. |
| Researcher | read | May flag `Notes/<handle>/extracted/` ideas as "ready to queue" in its report; never writes the TODO file. |
| Math Expert | read | Proposals stay in its home dir; Lead queues them with `source: math-expert` + `needs-validation`. |
| Validator, Developer | read | No writes. Validator's verdict clears `needs-validation` and gates math-claim resolutions. |

Agents who want something on the list send Lead a `REQUEST` (per [[_common]] § Communication protocol); they never edit the file.

## Lead's rules

- **No initiative on wake.** Lead touches the TODO list only while doing a task: a human request, an experiment result, a routed proposal. The Cold-Start Handshake is unchanged.
- **Adding and reordering** need no prior approval, but each change gets a change-log line with its reason and is reported to the human in the task report.
- **Pinned items** are never moved by Lead.
- **Dropping or removing any item** (including clearing out completed ones) requires the human's confirmation: Lead proposes the drop with its reasoning, waits for an explicit yes, then records `dropped` / removal and the confirmation in the change log.
- **Activating** an item: the brief to the Experimenter (or Developer) cites the `T-id`. A `needs-validation` item cannot become `active` until Validator clears it.
- **Pulling from notes:** on the human's request, Lead reads `Notes/<handle>/ideas/` and `Notes/<handle>/extracted/` (`kind: idea`), and queues the chosen ones with `source: notes` and a link to the source note.

## Resolution — nothing learned stays only in the TODO list

An item is resolved when its question is answered, **positively or negatively**. Negative results are results and are summarized like positive ones. Before moving an item to **Resolved**, Lead checks the routing:

1. **Summary in `_progress.md`** — written by the owning Experimenter: a dated log entry (plus *What's been tried / worked / stuck* where the note has those sections) citing the `T-id`.
2. **Data** → `Datasets/` + `data/` per [[datasets-convention]].
3. **Facts, concepts, literature** → `Concepts/` / `Research/` via Researcher.
4. **Math claims** → Validator's `vault_docs.math_validation` folder.
5. **Decisions** → an ADR ([[decision]]) or a `Decision:` line in `_progress.md`.
6. **Follow-up ideas** the result raised → new TODO items, linked from the resolved one.

The **Resolved** entry is one line plus links; the substance lives in the notes above.

## Publishing

Only on explicit human request.

1. Lead writes a snapshot to `vault_docs.todo_published` (default: `<project experiments folder>/_todo-<project>.md`), **excluding items flagged `private`** and the change log. Frontmatter `published: YYYY-MM-DD`; tags as the private file but with `#experiment` (Experiments-tree umbrella note, per [[tags]]) and `#status/review`.
2. The published file is written **only by Lead**, an explicit exception to the Experimenters' ownership of `Experiments/**`. Nobody edits it directly; changes go into the private file and are re-published.
3. Lead brings the snapshot to the human through the normal commit ritual ([[lead]] § Commit Ritual).
4. The private file stays the source of truth; set its `published:` date.

## Related material

- [[project-todo]] — template
- [[lead]] — owner's procedure
- [[experiment-folder-convention]] — `_progress.md` and experiment folders
- [[notes-folder-convention]] — where human ideas and extractions live
- [[projects-and-dependencies-convention]] — project profiles (`vault_docs.todo`)
