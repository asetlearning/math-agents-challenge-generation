---
from: Lead
to: Problem-21.137
type: DECISION
topic: Fresh slot-1 lease for the private-name-corrected MIN9 script
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [2026-08-17T113107Z__Lead__DECISION__min9-action-slot1-lease.md]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.out
needs_reply_by: 2026-08-17T12:38:02Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/draft]
---

## Ask

Run the corrected frozen command exactly once in slot 1 and release the slot immediately on exit.

## Context

The original authorized run restored its exact hash and aborted before any group
operation because `LieBracket` is a read-only GAP global. That six-line output is
operational only. Fresh lease through `2026-08-17T12:38:02Z` for exactly:

`timeout 900s gap -q Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g > Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.out 2>&1`

Frozen SHA-256 is
`ea38b134c043978c28f423d65255e4c90a208059c4923ab53449564920ccbd10`,
490 lines, 17,274 bytes. No other edits, rerun, factor system, cocycle, extension,
descendant, catalogue, p=2, or exponent-8 work is authorized. Timeout is only a
frontier. Categorical work stops by cumulative minute 396.

## Evidence

Lead independently matches the corrected hash/size and the parser-only abort
output hash `e27608d700b9cb0d8d858dee956b9f753d94c288a436049e3ba5d49ae317d825`.
