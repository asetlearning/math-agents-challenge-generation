---
title: Kourovka open-problems program
domain: group-theory
project: kourovka
experiment_type: kourovka-problem
status: active
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, topic/kourovka, project/kourovka, status/active, experiment-type]
---

# Kourovka open-problems program

An AI agent crew attacking open problems from the **Kourovka Notebook**. This note is
the hub: one directory per problem, each readable on its own by a mathematician who
has never seen this vault.

**Everything here is written for humans.** The agents' own message traffic lives under
`Agents/Kourovka/` and is an audit trail — 1,300 messages across a campaign. Nobody
should have to read it to find out what the crew did.

## Live problems

The crew runs **exactly three problems at a time**, worked in descending order of
tractability (easiest first).

| Problem | Slug | Tract | Opened | Cycles | Hours | State | Outcome |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

## Closed problems

| Problem | Slug | Outcome | Hours | Write-up |
|---|---|---|---|---|
| — | — | — | — | — |

## Program record

- [[_post-mortem-2026-08|August 2026 post-mortem]] — the first campaign: sixteen
  problems opened, zero closed. The autopsy, and the evidence base for the current
  protocol. **Read this before running the crew.**

## How a problem directory works

```
Experiments/Kourovka/<id>-<slug>/
├── _experiment.md      # hub — problem statement, selection reasoning, status, results
├── methodology/        # one note per cycle: what was tried, why, in what order
├── results/            # what came out, including negatives WITH BOUNDS
└── data/               # the actual GAP scripts and verbatim transcripts
```

Create one with:

```bash
bash _meta/scripts/kourovka-new-experiment.sh <id> <slug>
```

Or copy `_TEMPLATE/` by hand. The template carries the full rubric for what
"human-readable" means in this program — see §12 of
[[_TEMPLATE/_experiment|the template]].

### Who writes what, when

| When | Who | What |
|---|---|---|
| Problem selected | Lead | Directory, frontmatter, problem statement from the PDF, tractability block |
| End of each cycle | Problem agent | `methodology/cycle-N-*.md`, scripts into `data/`, results table |
| On a claim | Validator | Verdict into `results/` |
| Problem closes | Lead | The Summary at the top of `_experiment.md` |

A cycle is not finished until its write-up is current. This is the deliverable, not
paperwork.

### What makes a good entry

The most valuable thing this program produces short of a solution is a **bounded
negative result**: *"no counterexample exists among groups of order ≤ 2000, by
exhaustive scan, eight minutes, script attached."* That is reusable by anyone.

*"The agent explored several approaches"* is not, and a directory full of that is the
failure the post-mortem documents.

## Related material

- [[_kourovka-20-corpus]] — the parsed corpus and its limitations
- `Research/Group theory/Open problems/Kourovka/` — per-problem synthesis notes (the
  pre-work: statement, known results, expected tractability)
- `_meta/agents/Kourovka/` — the crew prompts
- [[kourovka-crew-setup]] — how to run the crew
- [[Experiments/Group Theory/Burnside Group/B29/_progress|B(2,9) program]] — the
  adjacent group-theory program this structure is modelled on
