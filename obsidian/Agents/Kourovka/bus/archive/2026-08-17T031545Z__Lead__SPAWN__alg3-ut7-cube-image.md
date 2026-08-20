---
from: Lead
to: Problem-21.137
type: SPAWN
topic: "Run ALG3-UT7-CUBE-IMAGE for exactly 60 active minutes"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["all prior problem-direction control messages"]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-alg3-ut7-cube-image.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
needs_reply_by: 2026-08-17T04:15:45Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/algebra-groups, project/kourovka, status/draft]
---

## Ask
Execute strategy `ALG3-UT7-CUBE-IMAGE` in a fresh counterexample context for exactly 60 active minutes, stopping at cumulative minute 225 or immediately on a target-equal candidate.

## Context
Read only the three listed refs before research. Create run directory `Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image` and preserve the cumulative ledger starting at 165 minutes. The exact active target has odd `p`, here `p=3`; a finite same-prime group; exponent exactly `9`; the actual cube-value set, not merely its generated subgroup; subgroup closure of that set; and nonabelianity for a counterexample. The exponent-8 two-group clause, every `p=2` example, wreath-shaped material, the failed Hall-span enlargement, and the exhausted split ansatz are excluded. Do not browse, consult solution-bearing history, delegate, or use quarantined files.

Implement only the frozen 729-row, two-generator, `dim J<=12` family in the MathExpert note. Hand-audit the algebra identities first. A target-equal candidate requires all five success artifacts and a complete seven-row constraint matrix; create a claim-check JSON and run the state checker before any `CLAIM`. A leading-layer survivor, a nonzero commutator without actual-value-set closure, or closure only after generation is not a counterexample.

## Evidence
The problem-active allocation is minutes 165 through 225. Before any computation expected to exceed 60 seconds, send Lead a compute-lease request naming the exact command, timeout at most 600 seconds, one-core/RAM estimate, and lease duration; do not start it until granted. A complete no-pass manifest is `STRATEGY_EXHAUSTED` for this family only. An incomplete implementation/run is a bounded incomplete outcome or exact `BLOCKER`, never family exhaustion.
