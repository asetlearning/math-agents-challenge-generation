---
title: "Leased all-ten primitive-group replay at degree 540"
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Leased all-ten primitive-group replay

Under heavy-compute slot 2, the frozen script with SHA-256
`eabac5012cff9fe6edbb89d66be7b63b9dafda84eabd6417b49104d919627dbb`
was run exactly once by the authorized command

`timeout 180s gap -q Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/scratch/order540_primitive_allten_replay.g`.

It exited 0.  The deterministic 22-line output is
`scratch/order540_primitive_allten_replay.out`, SHA-256
`8490cee8a67751dfa64dc97bd16dbe67aa903fc76d42c44fa07a4494815a3793`.

GAP 4.12.1 / PrimGrp 3.4.4 reports exactly ten installed primitive groups of
degree 540.  Exact point-stabilizer orbits give, for each index 1 through 8,
subdegrees

`[1,63,224,252]`.

Exact natural-group recognition gives index 9 as natural `A_540` and index 10
as natural `S_540`; their 2-transitivity gives subdegrees `[1,539]`.  Hence the
complete installed layer contains zero suborbits of length 77, and therefore
zero self-paired length-77 suborbits.  No orbital graph was available for the
requested `(540,77,4,12)` parameter check, and the graph-verification branch
was not entered.

The transcript contains two GAP syntax warnings about `adj` in that dormant
conditional branch.  They are warnings, not errors; `adj` would be assigned
immediately before use if the branch were entered.  They do not affect the
executed subdegree or natural-group-recognition paths, and the process exited
normally.

This is an exact negative frontier only for the ten groups in the installed
degree-540 PrimGrp layer.  It says nothing about SRGs with automorphism groups
outside this primitive-orbital realization and does not exclude the order-540
intersection array or answer the revision-3 scope.  No coclique enumeration,
CSP, web query, or broader catalogue scan was performed.

Outcome: `PARTIAL_RESULT` for the bounded installed layer and
`STRATEGY_EXHAUSTED` for `SRG540-RANK3-ORBITAL-GATE`;
`active_assignment_answered: no`.
