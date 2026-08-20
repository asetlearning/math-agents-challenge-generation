---
agent: Validator-20.115-SU38
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
direction: validation
session_id: collaboration:/root/v20115_su38
parent_session_id: collaboration:/root
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-18T00:53:01Z
cycle: 1
active_budget_minutes: 35
selection_status: inactive
run_dir: Agents/Kourovka/problems/20.115/verification
state: complete
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

Fresh hostile reconstruction of the submitted `SU_3(8)=3.U3(8)`, prime-three
central-height obstruction. Audit all 82 rows and the exact six failures, while
distinguishing failure of the proposed sufficient inequality from a source
counterexample. Use only canonical scope and the submitted claim/evidence.

## 2026-08-18T01:01:24Z — independent checker lease

Grant slot 2 for exactly one invocation of the frozen independent GAP checker,
SHA-256 `c3f56e2eb0bd57c1ec66e7cde8a30182545686200154d6226c27507917974f6c`,
under the requested 45-second timeout command. The named output path was absent
at grant. No patch, rerun, alternative table, or expanded audit is authorized;
release immediately after the invocation or failure.

## 2026-08-18T01:04:21Z — release slot 2

The sole frozen invocation exited zero in 4.40 seconds with maximum RSS 141824
KB. Output SHA-256
`d83ea633133eb512a81ad841298c27b0160bd53bec489e2d286b860c4e4a8953`
independently reproduces failure rows 35--40 and the `76/6` split. Release slot
2; no further computation is authorized.

## 2026-08-18T01:09:36Z — verdict accepted

Fresh reconstruction independently replicates the bounded `SU_3(8)` auxiliary
obstruction: exactly rows 35--40 fail the sufficient height threshold, while 76
rows pass. This refutes neither Proposition 3.2 nor the source target;
`active_assignment_answered: no`.
