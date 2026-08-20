---
from: Lead
to: Problem-21.137
type: SPAWN
topic: "Run EQ11-CUBE-CAYLEY for exactly the 59-minute remainder"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["all prior problem-direction control messages"]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-eq11-cube-cayley.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T035316Z-alg3-ut7-family-exhaustion.md
needs_reply_by: 2026-08-17T05:04:53Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/algebra-groups, project/kourovka, status/draft]
---

## Ask
Execute `EQ11-CUBE-CAYLEY` for exactly 59 active minutes, starting at cumulative minute 181 and stopping at minute 240 or immediately on a target-equal candidate.

## Context
Process only the three listed refs before research. Create `Agents/Kourovka/problems/21.137/runs/2026-08-17-r8-eq11-cube-cayley`. Freeze exactly the eleven endpoint-equal rows with `dim J<=12`; they were outside the killed endpoint-unequal family. Reuse audited algebra arithmetic if useful, but the observable is new: complete actual cube-value manifests, a boundary-sensitive Cayley BFS proving or refuting exact value-set subgroup closure, and a different noncommuting generator pair only after closure equality. Keep `p=3`, finite same-prime group, exponent exactly `9`, actual cubes rather than their generated subgroup, subgroup closure, and nonabelianity explicit in every row.

## Evidence
A candidate requires every success artifact and the canonical seven-row constraint matrix, then a claim-check JSON and clean state checker before `CLAIM`. A raw noncommuting pair, generated-subgroup equality without actual-set equality, or endpoint equality is not a candidate. For a failure, give each of all eleven rows either a direct closure-boundary triple with cube roots and exhaustive value manifest, or exact closure equality plus a complete commuting-generator table. Before any computation expected to exceed 60 seconds, request a lease with exact command, resource estimate, and timeout. No web/history, delegates, wreath material, third generator, higher dimension, unequal-endpoint rows, Hall-span enlargement, or split ansatz.
