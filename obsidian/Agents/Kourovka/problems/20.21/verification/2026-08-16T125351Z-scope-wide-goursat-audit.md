---
title: "Verification — Kourovka 20.21 — scope-wide Goursat reduction"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
scope_record: Agents/Kourovka/scopes/20.21-two-index-twelve-kernels.json
assignment_revision: 1
claim: "Every hypothetical witness belongs to exactly one of the full-product or common-C3 Goursat branches, with the stated kernel images."
claimant: Problem-20.21
verification_method: computation-free line-by-line hand proof
tools_used: ["none"]
scope_answered: ["necessary two-branch Goursat reduction"]
scope_not_answered: ["20.21/two-index-twelve-kernels"]
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/extensions, project/kourovka, status/conjectured]
---

# Verdict

**PASS as a necessary PARTIAL_RESULT.** The common-quotient list is exhaustive, both kernel-image identifications have the correct orientation, and the two subdirect products have the stated orders and isomorphism types. This is not an existence proof.

# Audit

For a hypothetical witness, let

\[
\alpha:G\twoheadrightarrow C_{12},\quad K=\ker\alpha,
\qquad
\beta:G\twoheadrightarrow A_4,\quad L=\ker\beta,
\qquad N=K\cap L.
\]

Then

\[
D=G/N\cong\operatorname{im}(\alpha,\beta)
\le C_{12}\times A_4
\]

is subdirect. Goursat's lemma supplies normal subgroups \(A_0\triangleleft C_{12}\), \(B_0\triangleleft A_4\), and an isomorphism

\[
C_{12}/A_0\cong A_4/B_0.
\]

The complete normal-quotient list of \(A_4\) is \(A_4,C_3,1\): its only normal subgroups are \(1,V_4,A_4\). All quotients of \(C_{12}\) are cyclic, so \(A_4\) cannot be common. Hence the common quotient is exactly \(1\) or \(C_3\).

1. For common quotient \(1\), \(A_0=C_{12}\), \(B_0=A_4\), and

   \[
   D=C_{12}\times A_4,\qquad |D|=144.
   \]

2. For common quotient \(C_3\), \(A_0=C_4\) and \(B_0=V_4\). After choosing the quotient identification,

   \[
   D=\{(x,y):\bar x=\bar y\}
   \]

   has order \(12\cdot12/3=48\), and the displayed map \(C_4\times A_4\to D\) is a bijective homomorphism. The two automorphisms of the common \(C_3\) merely change the chosen quotient identification (and can be absorbed by an automorphism of \(C_{12}\)); they do not create a third branch or a new isomorphism type.

The kernel orientations follow from the coordinate order:

\[
K/N=D\cap(1\times A_4)\cong B_0,\qquad
L/N=D\cap(C_{12}\times1)\cong A_0.
\]

Thus the two ordered pairs are

\[
(K/N,L/N)\cong(A_4,C_{12})
\]

in the full-product branch and

\[
(K/N,L/N)\cong(V_4,C_4)
\]

in the common-\(C_3\) branch. These agree with the standalone note and are not reversed.

# Boundary and minor edit

Every witness must be an extension of the corresponding \(D\) by \(N\), with the two coordinate preimages additionally required to be abstractly isomorphic. The reduction does not classify \(N\), the action, the factor set, or prove that either branch contains a witness.

The standalone note has one typesetting typo: the first display should read \(D\le C_{12}\times A_4\), not “\(D\) ... le \(C_{12}\times A_4\)”. It has no mathematical effect.

