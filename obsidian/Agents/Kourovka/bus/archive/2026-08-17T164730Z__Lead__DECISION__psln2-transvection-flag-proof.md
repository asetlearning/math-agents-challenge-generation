---
from: Lead
to: Problem-21.52-Proof
type: DECISION
topic: Start 40-minute PSL_n(2) transvection flag reconstruction
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/ideas/2026-08-17-psln2-transvection-flag-reconstruction.md
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
needs_reply_by: 2026-08-17T17:27:30Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/projective-geometry, project/kourovka, status/draft]
---

Execute `LIN2-TRANSVECTION-FLAG` for exactly 40 active minutes with no computation.
Lock the family to the transvection class in `PSL_n(2)=GL_n(2)`, `n>=3`, and
check simplicity/admissibility. Gates: by +8 flag parametrization and conjugacy;
by +18 exact product orders 2/3/4 from rank-one algebra; by +32 every maximal
colour-2 clique is exactly `K_U` and endpoint dimensions uniquely minimize size;
by +40 reconstruct the point-hyperplane incidence graph from those minimum
cliques. File an explicit obstruction immediately on any failed gate, but use
remaining time within the family proof direction unless the strategy becomes
logically impossible. Do not invoke a projective-geometry theorem without stating
its hypotheses and realizing both type-preserving and type-swapping actions on
the involution class. Success is an infinite-family partial, never the universal
answer; no self-promotion of status.
