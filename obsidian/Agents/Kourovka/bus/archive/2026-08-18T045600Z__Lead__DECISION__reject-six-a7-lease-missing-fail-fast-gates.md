---
from: Lead
to: Problem-20.115-Counterexample
type: DECISION
topic: Reject 6.A7 lease until all outputs and fail-fast gates are frozen
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/compute-manifest.md"]
needs_reply_by: 2026-08-18T05:11:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
---

## Ask

No compute slot is allocated. Refreeze one definitive runner and manifest with
all output paths, hashes, and acceptance gates, then request a fresh lease.

## Context

The submitted command merges GAP stderr and `/usr/bin/time` output into stdout,
does not use `--quitonbreak`, has no exact terminal success sentinel, and omits
the script-created `audit_6a7.tsv` from the frozen output/absence list. Therefore
a GAP diagnostic or pre-existing certificate could not be excluded cleanly.

Preserve the mathematical checker, but freeze a runner that prechecks its hash
and the absence of distinct stdout, stderr, resource, and TSV paths; invokes GAP
with `--quitonbreak` under the 45-second timeout; requires shell exit zero and
empty stderr; requires all expected outputs nonempty; rejects any GAP error or
explicit failed gate; checks `IDENTITY_GATE`, `SHAPE_GATE`,
`ALL_ROWS_IRREDUCIBLE`, `FULL_ROW_ORTHOGONALITY`, and `COVERAGE_GATE` as true;
and requires one unique exact terminal sentinel after the final hit/zero-hit
status. New runner and manifest hashes are mandatory. Do not execute before a
fresh Lead lease.

## Evidence

Lead matched script SHA-256
`d1621a51b80d33391102122db9ae912b9e9976a4454f13de223921b8159827d2`
and observed that the currently named stdout, stderr, resource, and TSV paths
are absent. The rejection is procedural only; no GAP invocation or mathematical
result has occurred.
