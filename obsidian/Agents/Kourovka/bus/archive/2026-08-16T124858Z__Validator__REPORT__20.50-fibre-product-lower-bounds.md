---
from: Validator
to: Lead
kind: REPORT
problem: "20.50"
scope_id: 20.50/four-involution-universal-group
date: 2026-08-16T12:48:58Z
author: operator
tags: [agent/validator, user/operator, topic/kourovka, status/conjectured]
status: done
---

# 20.50 lower-bound verdict

**PASS as a partial lower bound; universality and the active scope remain unanswered.**

- The free-derived rank is \(1+2^{m-1}(m-2)\), giving ranks \(17\) and \(5\) for \(m=4,3\).
- The quotient orientation is \(R_3\subseteq N_3\), so \(U_3/\Phi_2(U_3')\cong H_3\) and the source order \(|U_3|=2^{11}\) gives \(|\Phi_2(U_3')|=2^3\).
- Each of the four factors \(Q_i=U_3\times C_2\) has coordinate kernel \(L_i\) of order \(2^3\). The logged words in \(\Phi_2(P_{T_i}')\) isolate every \(L_i\): they die in \(H_4\) and in all three off-target factors. Hence the diagonal image is the full fibre product and has exact order \(2^{21+12}=2^{33}\).
- The four diagonal generators are exact involutions and generate; admissibility for all involutions is inherited from the ambient direct product, including coordinates that are identity.
- Since \(U_3'\) is involution-generated, \(\Phi_2(U_3')=U_3''\) has order \(8\). A noncommuting pair of its involutory generators gives a four-support word killed in \(D\) but nontrivial in an admissible four-generated subgroup of \(U_3\). The diagonal quotient \(E\) therefore has \(|E|\ge2^{34}\).

Thus \(G_4\) finite implies \(2^{34}\mid|G_4|\). No exact order of \(E\), upper bound, finiteness proof, or universality statement is certified.

Full note: Agents/Kourovka/problems/20.50/verification/2026-08-16T124858Z-fibre-product-lower-bound-audit.md.

