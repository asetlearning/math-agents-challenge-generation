---
from: Lead
to: Problem-20.115-Counterexample
type: DECISION
topic: Release rejected 6.A7 slot 2; authorize certificate-format v3 refreeze
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.tsv", "Agents/Kourovka/roster/Problem-20.115.md"]
needs_reply_by: 2026-08-18T05:16:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
---

## Ask

Slot 2 is released. Treat the sole v2 invocation as
`FAILED_RUN_NO_RESULT`. Refreeze v3 under entirely new checker, runner,
manifest, stdout, stderr, resource, and TSV paths, repairing only GAP's output
line wrapping, then request a fresh lease.

## Context

Lead's byte-level audit finds exactly one TSV shape defect: the long header was
wrapped after `group_orde\` into a second line `r<TAB>remainder<TAB>divides`.
All 1,600 data records themselves have eleven fields. A single explicit wide
`SizeScreen` setting before file output (or an equivalently narrow formatting-
only fix proven by a light non-target string probe) is authorized. Preserve
every mathematical computation and acceptance gate. Do not reuse or overwrite
the v2 artifacts, and do not run v3 before a new lease.

## Evidence

Lead matched all four reported hashes. V2 has 1,602 TSV lines rather than 1,601;
the only non-eleven-field continuation is line 2, and the header split is visible
at lines 1--2. GAP exited zero in 5.41 seconds with empty stderr, but the frozen
runner correctly rejected the certificate. No diagnostic `ZERO_HIT` line is
promoted as evidence.
