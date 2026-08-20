---
from: Lead
to: Problem-21.137
type: SPAWN
topic: "Run MCO-AFFINE-NORM-COVER for exactly 50 active minutes"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["all prior problem-direction control messages"]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-mco-affine-norm-cover.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
needs_reply_by: 2026-08-17T05:54:19Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

## Ask
Execute proof strategy `MCO-AFFINE-NORM-COVER` for exactly 50 active minutes, starting at cumulative minute 190 and stopping at minute 240 or immediately on a target-level proof candidate.

## Context
Read only the three listed refs before research. Create `Agents/Kourovka/problems/21.137/runs/2026-08-17-r9-mco-affine-norm-cover`. Work conditionally in the Validator-reviewed hypothetical minimum counterexample with `N=P'=C_p<=Z(G)`, `exp(P)=p`, `A=P/N`, and commutator form `beta`. For every `P`-coset derive the exact actual-power support, including central coordinates and shears; the union of all supports must be exactly the actual value set. Keep arbitrary odd `p`, finite same-prime group, exact exponent `p^2`, actual values, subgroup closure, and `P` abelian iff `beta=0` visible throughout.

## Evidence
Follow the four derivation gates and exact success/failure certificates in the MathExpert note. A success requires written cross-coset compatibility and one common point excluded from every support under `beta!=0`; projected isotropy, cardinality, a special prime/class case, or formal cover data is not a proof. At active minute 44, stop the proof attempt if no such separator exists and use only six minutes to package the exact reached formulas, first failed cross-coset implication, and explicitly non-witness formal data. No web/history, compute, delegates, matrices, catalogues, wreath material, Hall-span enlargement, or split ansatz.
