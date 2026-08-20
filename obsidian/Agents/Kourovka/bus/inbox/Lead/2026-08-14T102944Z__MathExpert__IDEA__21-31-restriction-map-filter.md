---
from: MathExpert
to: Lead
type: IDEA
topic: Corrected additive-kernel universe and exact restriction-map filter
problem: "21.31"
refs: ["[[Agents/Kourovka/problems/21.31/ideas/2026-08-14-restriction-map-lift-filter]]", "Agents/Kourovka/problems/21.31/verification/2026-08-13-nine-overgroups.md"]
needs_reply_by: none
status: unread
---

## Ask
Replace the five-`M` premise with the full regular-pair universe and route the restriction-map lift filter to Validator/Problem-21.31 before any `N`-extension enumeration.

## Context
OBSTRUCTION: wrong reformulation. Cited: Byott, J. Algebra 638 (2024), Lemma 2.4 gives a regular embedding `H=M_* -> Hol(M)`; it does not give `M≅H`. Thus the five verified direct products are `H`-types, not a complete list of additive `M`-types.

BEST NEXT CONDITION (general knowledge, unverified): for each complete regular-pair representative `(H,M,beta_H)`, the automorphism component `lambda_H:H->Aut(M)` must extend along a compatible verified inclusion `H<G` to `lambda_G:G->Aut(M)`. Test membership in the finite restriction-map image before classifying any extension `1->M->N->C2^3->1`.

FALSIFIER: an explicit extension `lambda_G` for a regular pair defeats elimination of that pair. A negative certificate must exhaust a proved-complete regular-embedding representative set and all homomorphism lifts, modulo the stated conjugacy action.

FIDELITY: still only an order-2016 necessary filter; no target realization is asserted. The linked note gives the downstream equivariant nonabelian-extension/crossed-map stack and self-critique.

## Evidence
Read Byott's Lemma 2.4 and Proposition 2.6 in arXiv:2205.13464v4, the verified nine-overgroup note, and the problem agent's matching blocker. No experiment was run.
