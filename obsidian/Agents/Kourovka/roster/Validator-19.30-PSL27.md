---
agent: Validator-19.30-PSL27
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
direction: validation
session_id: collaboration:/root/v1930_psl27
parent_session_id: collaboration:/root/p1930_psl27
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-17T15:14:30Z
cycle: 0
budget_hours: 0.5
active_budget_minutes: 30
active_minutes_used: 8
extensions_granted: 0
safety_stop_utc: 2026-08-17T15:44:30Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: approved
truth_likelihood: 0.56
alternate_direction: none
run_dir: Agents/Kourovka/problems/19.30/verification
state: running
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

Independently reconstruct the fixed-`PSL(2,7)` order-168 result without reusing
the discovery script. Any GAP or mathematical enumeration requires a separately
frozen implementation and Lead compute lease. The universal scope remains open.

## 2026-08-17T15:25:07Z — independent reconstruction lease

Lead matches the frozen independent GAP checker SHA-256
`7d5af3a9e9e1f09412487b5e3cd3a5474898e7d4715a0f9c9d3a582e6652dd10`
and runner SHA-256
`bc82bea9f3309372ccbdc3b0b885c0aa0bebfdb1de4bd13048d946c2fe553a84`.
Grant compute slot 2 through the existing safety stop
`2026-08-17T15:44:30Z` for exactly one runner invocation, one GAP process,
one CPU, conservative 1.5 GiB ceiling, and a 900-second child timeout plus
30-second kill grace. This can replicate only the fixed order-168 subcase.

## 2026-08-17T15:27:02Z — slot 2 released after successful reconstruction

The one frozen runner exits 0 after `7.766230608` seconds with 57/57 catalogue
records, target set `[2,3,4,7]`, equality index `[42]`, zero nonisomorphic
collisions, and `VALIDATION_COMPLETE=true`. Release slot 2. The Validator has used
eight active minutes and is packaging the fixed-subcase verdict; the universal
assignment remains unanswered.
