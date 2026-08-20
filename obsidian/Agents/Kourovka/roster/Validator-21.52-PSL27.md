---
agent: Validator-21.52-PSL27
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
direction: validation
session_id: collaboration:/root/v2152_psl27
parent_session_id: collaboration:/root/p2152_psl27
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-17T16:06:14Z
cycle: 0
budget_hours: 0.5
active_budget_minutes: 30
active_minutes_used: 0
extensions_granted: 0
safety_stop_utc: 2026-08-17T16:36:14Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: approved
truth_likelihood: 0.62
alternate_direction: none
run_dir: Agents/Kourovka/problems/21.52/verification
state: running
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

Independently reconstruct the bounded fixed-`PSL(2,7)` claim: the complete
product-order colour group on its 21-element involution class equals the
restriction image of `Aut(PSL(2,7))`, and both have order 336. Do not reuse the
claimant's backtracking logic. Preserve `witness_equals_target:false` and
`active_assignment_answered:no`; the universal Problem 21.52 is not claimed.

## 2026-08-17T16:26:12Z — independent fixed-pair compute lease

Lead matches the frozen GAP checker SHA-256
`b888d48d2b0cb0dcae0254e2381e8d8e1426056b7f96d603c53b22d3a1c876ce`.
Grant slot 1 through `2026-08-17T16:31:12Z` for exactly the manifest command,
one GAP process, 120-second timeout, and 512 MiB workspace cap. The checker uses
a GRAPE coloured-incidence graph rather than the claimant's backtracking logic.
No rerun or live patch; release immediately with exact exit status and artifacts.

## 2026-08-17T16:30:41Z — corrected v2 lease

V1 released slot 1 after aborting before mathematics on GAP's read-only global
`Z`. Lead independently diffs v2: the only semantic change is renaming that local
binding to `centreSL`; transcript labels and output paths advance to v2. Match
SHA-256 `9a55a712f1b256bc07a8ceafc3325572d6436547b4dc0dbe50bad7fea37c1adb`.
Grant a fresh slot-1 lease through `2026-08-17T16:35:41Z` for exactly one v2
manifest command. No further correction or rerun is authorized.

## 2026-08-17T16:34:02Z — slot 1 released after fixed-pair pass

The one v2 run exits zero in 2.15 seconds. Its independent GRAPE incidence model
gives a faithful colour group of order 336, while the complete automorphism
restriction image also has order 336; the two canonical permutation sets are
equal with empty differences. Release slot 1 and package the bounded verdict.
The universal scope remains unanswered.
