---
title: "Action-layer reduction for the order-128 nonsplit family"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/representations
  - project/kourovka
  - status/conjectured
problem: "20.21"
scope_id: "20.21/two-index-twelve-kernels"
assignment_revision: 1
---

# Setup

In the order-128 family, let \(N=C_2^3\). An extension action \(Q=C_4\times V_4\to\operatorname{Aut}(N)\), together with a lift \(\sigma\) of the order-three automorphism of the \(V_4\) factor, induces an action homomorphism
\[
C_4\times A_4\longrightarrow \operatorname{GL}(3,2).
\]

# Reduction

The kernel of the restricted homomorphism from \(A_4\) is normal in \(A_4\). Hence the \(A_4\)-image is one of
\[
1,\qquad C_3,\qquad A_4.
\]

If the image is \(C_3\), an element \(s\) of order three acts on \(N\) as the direct sum of a one-dimensional fixed space and the irreducible two-dimensional \(C_3\)-module. Its centralizer in \(GL(3,2)\) is \(C_3\): commuting matrices preserve the two primary summands, are the identity on the one-dimensional summand, and are multiplication by a nonzero element of \(\mathbb F_4\) on the irreducible summand.

If the image is faithful \(A_4\), its centralizer is contained in the preceding \(C_3\). A nonidentity element of that \(C_3\) does not centralize the normal \(V_4\) in \(A_4\), so the centralizer of the whole \(A_4\)-image is trivial.

The image of the commuting \(C_4\) factor is a 2-subgroup of these centralizers. Therefore:

- for image \(C_3\) or faithful \(A_4\), the \(C_4\)-action on \(N\) is trivial;
- if the \(A_4\)-image is trivial, the \(C_4\)-image may have order 1, 2, or 4 (the identity, a unipotent involution, or a unipotent order-four element, up to matrix conjugacy).

Thus the action layer is reduced to a small finite list before any second-cohomology calculation. This does not classify the cocycles, test the order-three lift on an extension class, or establish kernel isomorphism.
