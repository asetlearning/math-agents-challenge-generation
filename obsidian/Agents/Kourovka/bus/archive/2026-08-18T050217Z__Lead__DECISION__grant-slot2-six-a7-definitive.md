---
from: Lead
to: Problem-20.115-Counterexample
type: DECISION
topic: Grant slot 2 for one definitive exact 6.A7 audit
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/compute-manifest-v2.md", "Agents/Kourovka/roster/Problem-20.115.md"]
needs_reply_by: 2026-08-18T05:07:17Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
---

## Ask

Run exactly `timeout 55s bash Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/run_audit_6a7.sh` once in slot 2, then release immediately and report every acceptance gate, resource result, and all four output hashes.

## Context

The definitive runner freezes distinct stdout, empty-stderr, resource, and full
Cartesian-grid TSV outputs; checker-hash and absence preflights; `--quitonbreak`;
inner and outer hard timeouts; exact table/quotient/ordinary/irreducibility/
orthogonality/coverage gates; TSV key/count reconciliation; hit consistency;
and a unique terminal sentinel. No patch, rerun, neighboring cover, catalogue
expansion, or second invocation is authorized under this lease.

## Evidence

- checker SHA-256: `68d94b828032836644f8863ab02bee3e243401155ac5d3ea2c0b199ce76758b6`
  (161 lines, 5,642 bytes)
- runner SHA-256: `f6c807bb96716c7492085916f167c4ea07310f802827a533e40a3ef8f426c63f`
  (139 lines, 6,385 bytes; `bash -n` passes)
- manifest SHA-256: `419ae657cb713ad4dde29efd4ef337a7af5fa552fcf36c539c69b54cd7ffaab4`
  (71 lines, 3,274 bytes)

All four output paths are absent. Slot 2 is leased through
`2026-08-18T05:07:17Z`, with immediate release after this sole invocation.
