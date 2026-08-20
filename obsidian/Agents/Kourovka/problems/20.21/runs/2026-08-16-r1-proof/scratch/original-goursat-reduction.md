---
title: "Goursat reduction for every candidate to Kourovka 20.21"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/extensions
  - project/kourovka
  - status/conjectured
problem: "20.21"
scope_id: "20.21/two-index-twelve-kernels"
assignment_revision: 1
---

# Reduction

Suppose \((G,K,L)\) satisfies the target conditions, and let
\[
\alpha:G\twoheadrightarrow C_{12},\qquad \ker\alpha=K,
\]
\[
\beta:G\twoheadrightarrow A_4,
\qquad \ker\beta=L.
\]
Put \(N=K\cap L\). The combined map has kernel \(N\), so
\[
D:=G/N\cong\operatorname{im}(\alpha,\beta)\le C_{12}\times A_4.
\]
Both coordinate projections of \(D\) are onto; hence \(D\) is a subdirect product.

By Goursat's lemma, \(D\) is determined by a common quotient of \(C_{12}\) and \(A_4\). The normal quotients of \(A_4\) are \(A_4\), \(C_3=A_4/V_4\), and \(1\). Since every quotient of \(C_{12}\) is cyclic, the only common quotients are \(1\) and \(C_3\).

## Branch I: trivial common quotient

Then
\[
D=C_{12}\times A_4,
\qquad |D|=144.
\]
The two kernel images are
\[
K/N\cong A_4,
\qquad
L/N\cong C_{12}.
\]

## Branch II: common quotient \(C_3\)

Use the unique quotient \(C_{12}\twoheadrightarrow C_3\), whose kernel is \(C_4\), and the abelianization quotient \(A_4\twoheadrightarrow C_3\), whose kernel is \(V_4\). Then
\[
D=\{(x,y)\in C_{12}\times A_4:\bar x=\bar y\in C_3\},
\qquad |D|=48.
\]
Writing \(C_{12}\cong C_4\times C_3\), the map
\[
C_4\times A_4\longrightarrow D,
\qquad
(u,y)\longmapsto ((u,\bar y),y)
\]
is an isomorphism. The kernel images are
\[
K/N\cong V_4,
\qquad
L/N\cong C_4.
\]

# Meaning and limits

Every target witness lies in exactly one of these two extension branches. Thus a constructor may work with an extension of either \(C_{12}\times A_4\) or \(C_4\times A_4\) by \(N\), while enforcing that the two coordinate preimages are abstractly isomorphic. This is a necessary reduction, not an existence proof; it does not classify the extension kernel, outer action, or factor set.
