---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
cycle: 21
strategy: SL2Q-DIRECT-CHARACTER-FAMILY
---

# Cycle 21 — direct SL(2,q) character family

## Active-time ledger

- Start: 2026-08-18T11:09:00Z; newly elapsed active time `00:00:00`; detailed cumulative time `07:44:01`.
- Ledger correction: protocol and assignment reading began at the roster spawn time
  `2026-08-18T11:04:43Z`; that earlier instant is the chargeable start.  The
  `11:09:00Z` entry records only the start of mathematical writing.

## Target and isolation

For every quasisimple group `G=SL(2,q)`, audit every ordinary irreducible complex character and every element class against
`chi(x) != 0 => o(x) chi(1) | |G|`.  This is only a family partial toward the universal scope.  No earlier rank-one-family finding is used as a premise.

## Outcome

- Stop: 2026-08-18T11:16:16Z; newly elapsed active time `00:11:33` from the
  corrected start; detailed cumulative time `07:55:34`.
- Outcome: `PARTIAL_RESULT`.  The abstract ordinary table yields a candidate
  family theorem for every quasisimple `SL(2,q)`, including exact central lifts,
  exceptional rows, and all cancellation gates.  The universal scope remains
  unanswered.
- Computation: none.  No heavy-compute lease was requested or used.
- Evidence: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r21-sl2q-direct-character-family/findings.md`.
