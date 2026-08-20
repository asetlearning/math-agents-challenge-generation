---
title: "Kourovka 21.137 — K32 nonsplit root saturation log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: K32-NONSPLIT-ROOT-SATURATION
direction: counterexample
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# K32-NONSPLIT-ROOT-SATURATION log

## 2026-08-17T15:08:06Z — pre-computation freeze

Read the common protocol, problem-agent protocol, Lead decision, and exactly the
five resources permitted by that decision. Scope is revision 2, `p=3>2`, finite
3-group, exact exponent `9`, complete actual cube-value set, subgroup closure,
and explicit nonabelianity. Excluded material remains unopened.

Frozen the sole coordinate artifact at
`scratch/k32_nonsplit_frozen.py`; its manifest is
`scratch/FROZEN-ARTIFACT.md`. SHA-256 is
`0120923226d69921e25d8cb3d971b939d4d54210d9dc16c77e7c320ef195507c`.
No mathematical command has been run. Active
research ledger remains `470` cumulative minutes before this final increment;
this run is at `+0/55` pending the required Lead compute lease.

## 2026-08-17T15:20:24Z — lease wait handoff

The lease request remains unread in Lead's inbox. Research is stopped at
`+0/55`; waiting time is uncharged. Return to Lead with the session resumable;
do not run or alter the frozen artifact until an explicit lease arrives.

## 2026-08-17T15:30:35Z — exact gate failure and return to Lead

Ledger correction: the exact artifact design and writing from
`15:08:06Z` to `15:17:06Z` was mathematical work even though no command had
run, so it charges `9` active minutes. Lease waiting through `15:24:35Z` is
uncharged. Hash verification, the sole leased run, inspection, preservation,
and reporting from `15:24:35Z` to `15:30:35Z` charge `6` more minutes. Final
run total is exactly `+15/55`; scope cumulative total is `485`.
The exact unspent balance in the authorized 55-minute window is `40` active
minutes, returned to Lead for the next bounded decision.

The frozen SHA-256 matched. The exact leased command ran once in
`0.31164281` seconds, exited `2`, and had empty stderr. Compute slot 1 was
released at `15:25:02Z`. Frozen `GATE_0` passed: `R0` has order `3^5`,
exponent `3`, and central commutator rank `2`. Frozen `GATE_1` passed: the
single correction row satisfies all displayed Schreier equations and gives
the consistent orders `|G0|=3^10`, `|G|=3^11`. The complete quotient cube
formula then produced exactly `73` labels in `P/<c>`, with
`(0,0,0,1)` absent. Since `73` is not a power of `3`, this actual quotient
image cannot be a subgroup; hence the actual cube set is not a subgroup.
This fires the prescribed label hard kill. No fibre run, rerun, patch, second
correction row, representative change, PF generator, or generalized family
was opened. Outcome: `STRATEGY_EXHAUSTED` for this one frozen model;
`active_assignment_answered: no`. Return to Lead, not self-park.
