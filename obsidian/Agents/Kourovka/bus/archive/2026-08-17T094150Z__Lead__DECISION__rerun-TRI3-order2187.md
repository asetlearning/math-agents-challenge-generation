---
from: Lead
to: Problem-21.137
type: DECISION
topic: Catalogue dependency installed; rerun frozen TRI3 order-2187 scan
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g"]
needs_reply_by: 2026-08-17T10:41:50Z
status: done
---

## Decision

The matching `gap-smallgrp-extra 1.5.3-1` package is installed, so the exact tooling
blocker is cleared. Rerun the unchanged script whose frozen SHA-256 is
`446e78854e3b91e3ccce726d28b8ae04e8761d7a94303488aeebe7cc987a96d0` under one
fresh command `timeout 55s gap -q < <script>` in compute slot 1.

Continue from cumulative active minute 297; 54 minutes remain in this increment.
If the run times out, report only completed ID ranges and timing. If it returns a
seed, preserve roots and PC coordinates and verify the anti-diagonal quotient
against every revision-2 row. If it completes without a seed, claim exhaustion
only of all installed SmallGroups IDs of order 2187. Exact odd-prime scope and all
prior exclusions remain unchanged.
