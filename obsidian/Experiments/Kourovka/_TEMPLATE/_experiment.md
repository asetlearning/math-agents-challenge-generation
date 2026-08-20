---
title: "Kourovka <ID> — <short problem description>"
domain: group-theory
project: kourovka
problem_id: "<ID>"
issue: <NN>
page: <page in the source PDF>
proposers: ["<name>"]
experiment_type: kourovka-problem
status: draft
outcome: open
tractability: <1-5>
shape: counterexample | finite-check | reduction | needs-new-theory
opened: <YYYY-MM-DD>
closed:
cycles: 0
elapsed_hours: 0
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, topic/kourovka, topic/<subject>, project/kourovka, status/draft, experiment-type]
---

# Kourovka <ID> — <short problem description>

> [!info] How to read this note
> This is the **human-readable record** for one Kourovka problem. Everything a
> mathematician needs is here or one link away. The agent bus traffic under
> `Agents/Kourovka/` is the audit trail, not the report — you should not need it.

## Summary

<!-- Lead writes this LAST, when the problem closes. Until then, leave the placeholder.
     Three to six sentences, for a group theorist who has never seen this vault:
     what the problem asks, what the crew established, what remains. -->

*Open — no summary yet.*

---

## The problem

**Kourovka Notebook <ID>**, issue <NN>, page <page>. Proposed by <proposers>.

> <The verbatim statement, transcribed from the SOURCE PDF — not the corpus text.
> The corpus is a plain-text mangle: `hx, yi` for `⟨x, y⟩`, flattened
> sub/superscripts. Transcribe properly, with real mathematical notation.>

**In plain words:** <one or two sentences restating it without notation>

**What a solution would look like:** <concretely>

**What a refutation would look like:** <concretely — usually: a single object with
these properties>

### Staleness check

Performed <date> by <agent>. The corpus is from the 2022 edition and problems get
solved between editions.

- Corpus flags: `answered: <>`, `has_editor_comment: <>`, `has_later_comment: <>`
- Source PDF page reads: <does the notebook itself mark this solved or commented?>
- Searched: <the exact queries, arXiv, MathSciNet, current Kourovka edition>
- **Result:** <not solved as of <date> / solved by [citation] / partial progress in [citation]>

---

## Why this problem was selected

| Field | Value |
|---|---|
| Tractability | <n>/5 |
| Shape | <counterexample-shaped / finite-check / reduction / needs-new-theory> |
| First computation | <the concrete scan run in the first 30 minutes> |
| Expected runtime | <seconds / minutes / hours> |
| Counterexample shape | <what one would look like, or "unknown"> |
| Tools required | <GAP, SmallGroups(<order>), ANUPQ, …> |
| Tools verified available | <yes / no / partial — and when this was checked> |

**Reasoning:** <Lead's one-paragraph justification. Why this one, why now, why the
crew expects a machine can move it.>

---

## Status

| Cycle | Dates | Agent | Hours | Outcome | Next computation named |
|---|---|---|---|---|---|
| 1 | <date> | Problem-<ID> | 3 | STILL-TRYING | <the named next step> |

**Current state:** <one line>

---

## Results

The most valuable rows here are the **negatives with explicit bounds.** "No
counterexample of order ≤ 2000" is a reusable result; "several approaches were
explored" is not.

| # | Finding | Type | Bound / scope | Evidence | Status |
|---|---|---|---|---|---|
| 1 | <e.g. no counterexample among groups of order ≤ 512> | negative | `SmallGroup(n,k)`, n ≤ 512, all k | [[results/<note>]] | status/replicated |

### Ruled out

<!-- Prose. What regions of the search space are closed, and how firmly. This is what
     stops the next person repeating the work. -->

### Still live

<!-- What has not been tried, and what the next person should run first. -->

---

## Write-ups

- [[methodology/cycle-1-<slug>|Methodology — cycle 1]] — what was tried, why, in what order
- [[results/<slug>|Results]] — what came out
- [[data/<slug>|Data]] — scripts, transcripts, enumeration output

## Related material

- [[Research/Group theory/Open problems/Kourovka/<ID>-<slug>|Problem synthesis]] — the pre-work note
- `Agents/Kourovka/problems/<ID>/` — raw agent logs and scratch (audit trail)
- [[Experiments/Kourovka/_kourovka|Kourovka program hub]]
- [[Experiments/Kourovka/_post-mortem-2026-08|August 2026 post-mortem]]

---

## §12 — what "human-readable" means here

<!-- Keep this section in the template; delete it from real experiment notes. -->

The point of this directory is that a **group theorist who has never seen this vault**
can open it and, within ten minutes, know:

1. **What the problem asks** — stated properly, in real notation, from the PDF.
2. **What the crew actually established** — with the bound or the scope attached to
   every claim. Never "we checked small cases"; always "all groups of order ≤ 512".
3. **What was ruled out** — the negative space, explicitly. This is usually the most
   valuable output and it is the part agents are most likely to leave vague.
4. **What to run next** — a concrete computation, not a research direction.
5. **Where the evidence is** — the actual scripts and transcripts in `data/`, not
   summaries of them.

Rules:

- **Prose, not JSON.** Tables where a table helps. No status codes, no
  machine-readable blobs, no bus message IDs in the body text.
- **Every quantitative claim carries its bound.** An unbounded negative result is an
  anecdote.
- **Copy the real scripts into `data/`.** Not descriptions of them. If a scan took
  31 seconds and settled a question, the next person wants to re-run it.
- **Write it as the cycle ends**, not from memory later. A cycle is not finished
  until this is current ([[_common-kourovka]] §12).
- **Negative results are results.** Write them up with the same care as a claim.
  Sixteen well-bounded negatives would have been a genuinely useful output from the
  last campaign; sixteen vague ones were not.
