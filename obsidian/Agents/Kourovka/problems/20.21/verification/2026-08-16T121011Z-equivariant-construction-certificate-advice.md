---
title: "Validator advice — Kourovka 20.21 equivariant construction certificate"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
result: certifiable-in-principle
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/extensions, project/kourovka, status/draft]
---

# Answer

**Yes.** The logged semidirect-product reduction is sufficient: if finite (P), epimorphisms (f:P\twoheadrightarrow C_4) and (h:P\twoheadrightarrow V_4), and (\sigma\in\operatorname{Aut}(P)) satisfy (\sigma^3=1), (f\sigma=f), (h\sigma=\tau h), and (\ker f\cong\ker h), then (G=P\rtimes_\sigma C_3) has the required two kernels and quotients. This is a direct homomorphism argument, not yet an existence claim.

A certifiable witness package should contain:

1. an explicit finite presentation and an independent faithful permutation/pc realization of (P), with generator correspondence, relator checks, and exact order/normal-form proof;
2. formulas for (f,h) on generators, checks that all relators are respected, and explicit surjectivity onto (C_4,V_4);
3. formulas for (\sigma), proof that they extend to an automorphism, and a check of (\sigma^3=1); the (h\sigma=\tau h) identity forces the action to have exact order 3 once (\tau) is the 3-cycle on (V_4\setminus\{0\});
4. an explicit semidirect-product convention and reconstruction of (G), proving (|G|=3|P|);
5. explicit maps
   \[
   \alpha(ps^i)=(f(p),s^i),\qquad \beta(ps^i)=(h(p),s^i),
   \]
   with homomorphism and surjectivity checks, followed by exact kernel proofs (\ker\alpha=\ker f), (\ker\beta=\ker h);
6. an explicit abstract isomorphism (\ker f\to\ker h): checking images of defining relators plus an inverse, or a surjective relation-checked map together with independently established equal finite orders;
7. explicit quotient identifications (C_4\times C_3\cong C_{12}) and (V_4\rtimes_\tau C_3\cong A_4), preferably by concrete permutations;
8. the full constraint-and-conclusion matrix for the resulting triple ((G,K,L)).

Pitfalls: equal kernel orders or matching invariants do not prove isomorphism; proposed subgroups are not enough unless proved to be the exact kernels; and a database identifier without reconstruction is insufficient. No candidate is currently asserted, so this is certificate guidance only.
