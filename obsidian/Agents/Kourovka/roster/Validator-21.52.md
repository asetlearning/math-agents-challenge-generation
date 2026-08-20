---
agent: Validator-21.52-A5
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
direction: validation
session_id: collaboration:/root/v2152_a5
parent_session_id: collaboration:/root/p2152_small_simple
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-17T15:34:25Z
cycle: 0
budget_hours: 0.5
active_budget_minutes: 30
active_minutes_used: 0
extensions_granted: 0
safety_stop_utc: 2026-08-17T16:04:25Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: approved
truth_likelihood: 0.62
alternate_direction: none
run_dir: Agents/Kourovka/problems/21.52/verification
state: complete
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

Independently audit rendered page 172 against the canonical revision-1 scope,
including every quantifier, the single involution-class requirement, exact edge
colour `|ab|`, and the typed meaning of the source inclusion in `Aut(L)`. No
mathematical search or status claim begins before this audit passes.

## 2026-08-17T15:15:48Z — PASS

Rendered page 172 and all seven constraints/five exclusions pass. The typed
conclusion is exact: with `B=Stab_Aut(L)(D)`, every colour automorphism lies in
the restriction image, while the reverse inclusion is automatic, hence equality.

## 2026-08-17T15:34:25Z — fixed-A5 validation assignment

Independently reconstruct or refute the bounded claim that the complete
product-order colour-automorphism group on the unique involution class of `A5`
equals the restriction image of `Aut(A5)` and both have order 120. Do not reuse
the claimant's enumeration logic. Any mathematical computation requires a newly
frozen artifact and a Lead lease. Keep `active_assignment_answered:no` unless the
universal quantifier is genuinely addressed.

## 2026-08-17T15:48:43Z — fixed-A5 verdict complete

An independent hand proof reconstructs the five colour-2 blocks, the faithful
block action from order-3 matching holonomies, and the matching `S5` lower bound.
It validates equality of the two order-120 groups only for `A5`, with
`witness_equals_target:false` and `active_assignment_answered:no`.
