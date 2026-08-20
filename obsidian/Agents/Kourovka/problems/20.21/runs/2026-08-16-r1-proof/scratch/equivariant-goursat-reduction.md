---
title: "Equivariant Goursat reduction for the index-four template"
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

# Statement

Let \(P\) be finite, let
\[
f:P\twoheadrightarrow C_4,
\qquad
h:P\twoheadrightarrow V_4,
\]
and let \(\sigma\in\operatorname{Aut}(P)\) satisfy
\[
f\sigma=f,
\qquad
h\sigma=\tau h,
\]
where \(\tau\) cyclically permutes the three nonzero elements of \(V_4\). Then the combined map
\[
(f,h):P\longrightarrow C_4\times V_4
\]
is onto.

# Proof

Its image \(S\) is a subdirect product because both coordinate maps are onto. By Goursat's lemma, \(S\) is determined by a common quotient of \(C_4\) and \(V_4\). The only possibilities are the trivial group and \(C_2\).

The equivariance identities make \(S\) invariant under \(1\times\tau\). Suppose the common quotient were \(C_2\). On the \(V_4\) side, the Goursat kernel would be an order-two subgroup \(B<V_4\), equivalently the kernel of a nonzero map \(V_4\to C_2\). It can be recovered intrinsically from \(S\) as
\[
B=\{v\in V_4:(1,v)\in S\}.
\]
Invariance of \(S\) under \(1\times\tau\) would therefore make \(B\) invariant under \(\tau\). But \(\tau\) cycles the three order-two subgroups of \(V_4\), so none is invariant. This is a contradiction.

Thus the common quotient is trivial and \(S=C_4\times V_4\).

# Consequences

Let \(K=\ker f\), \(L=\ker h\), and \(N=\ker(f,h)=K\cap L\). Surjectivity gives
\[
K/N\cong V_4,
\qquad
L/N\cong C_4,
\qquad
P=KL.
\]
Accordingly, a cocycle search for this template may be formulated as an extension of \(C_4\times V_4\) by \(N\), equipped with an order-three lift of \(1\times\tau\), whose two coordinate preimages are abstractly isomorphic.

This is a reduction inside the sufficient template; it does not say that every solution of Kourovka 20.21 arises this way.
