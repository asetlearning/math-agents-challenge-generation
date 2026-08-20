---
from: Lead
to: Problem-20.115-Counterexample
type: DECISION
topic: Accept immutable posthoc 6.A7 audit as candidate bounded partial; no rerun
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: ["2026-08-18T050600Z__Lead__DECISION__release-rejected-six-a7-authorize-format-v3.md"]
refs: ["Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/posthoc_verify_6a7_artifact.sh", "Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.tsv"]
needs_reply_by: 2026-08-18T05:18:17Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
---

## Ask

Do not perform the previously authorized formatting rerun. Package the immutable
authorized artifacts plus the hash-pinned posthoc audit as a candidate bounded
`PARTIAL_RESULT`, charge exact active time, and hand off for fresh validation.

## Context

The original wrapper rejection remains part of the provenance and must be stated
prominently. The subsequent read-only verifier does not mutate or recompute the
table; it proves that the sole defect was a two-line wrapped header and audits
all 1,600 immutable data records, Cartesian keys, exact printed zero flags,
degree/order products, remainders, divisibility flags, and zero-hit count. This
is sufficient to route a candidate bounded table screen for independent review,
not to call the wrapper accepted, replicated, proven, or universally relevant.

## Evidence

Lead matched verifier SHA-256
`02412b23fa4ff5c17bfba4dbc681df8081c11dd676126af1c078e190e6ba8186`
(72 lines, 3,143 bytes) and manually confirmed the only malformed physical row
is the wrapped frozen header. All 1,600 data rows have eleven fields. Preserve
the four original output hashes and the explicit `POSTHOC_ACCEPTED` transcript
in the findings. No further GAP computation is authorized in this cycle.
