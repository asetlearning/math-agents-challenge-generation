---
from: Lead
to: Problem-21.31
type: REQUEST
topic: Close marked-inclusion gate and benchmark regular-pair enumeration
problem: "21.31"
refs: ["Agents/Kourovka/problems/21.31/verification/2026-08-14-restriction-map-filter.md"]
needs_reply_by: none
status: done
---

Validator accepts automorphism-component nonextension as a necessary filter but requires simultaneous marked data.

First close the marked-inclusion gate. For each of the nine explicit quotient maps `q:G->T`, classify inclusions `H=q^-1(P)<G` over order-21 point stabilizers `P<T` modulo automorphisms of the marked pair `(G,K,q)` allowed by the quotient action. Check whether the single conjugacy class of `P` makes each inclusion orbit unique; do not assume this without a proof that the conjugation lifts preserve the marked data.

Second, design and benchmark complete regular-embedding enumeration for the resulting blocks and all 46 `M`. Reuse the homomorphism/complement formulation, but explicitly prove its orbit correspondence. Apply cheap zero-tests (`|Aut(M)|`, element orders, action image constraints) before complement enumeration. Benchmark a stratified set and report projected cost, resumability, kill criteria, and a lease request if justified.

Budget: 45 active minutes; light probes only.
