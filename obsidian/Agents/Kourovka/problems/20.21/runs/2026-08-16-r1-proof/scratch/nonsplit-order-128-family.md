---
title: "Next constructor: nonsplit order-128 extension family"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/extensions
  - project/kourovka
  - status/draft
problem: "20.21"
scope_id: "20.21/two-index-twelve-kernels"
assignment_revision: 1
---

# Named approach

Nonsplit \(C_2^3\)-by-\((C_4\times V_4)\) factor-set search with an order-three lift.

# Why this is the next representation

The separately leased screen excludes the sufficient equivariant template for \(|P|=16,32,64\). The next possible order is 128. The clean equivariant Goursat reduction gives
\[
P/N\cong C_4\times V_4,
\]
so at order 128 the common kernel has exact order \(|N|=8\). The split elementary-abelian case is excluded by the standalone Frattini argument, making nonsplit extensions the first untested linear family.

# Exact finite data

Fix
\[
Q=C_4\times V_4=\langle a\rangle\times\langle b,c\rangle
\]
and let \(\bar\tau\in\operatorname{Aut}(Q)\) fix \(a\) and send
\[
b\mapsto c,\qquad c\mapsto bc.
\]
Set \(N=C_2^3\). An extension in the family is specified by:

1. an action \(\rho:Q\to\operatorname{GL}(N)\cong\operatorname{GL}(3,2)\);
2. a normalized 2-cocycle \(\eta:Q\times Q\to N\) for that action, modulo coboundaries;
3. a matrix \(S\in\operatorname{GL}(3,2)\) with \(S^3=1\), together with a normalized 1-cochain accounting for a lift \(\sigma\) of \(\bar\tau\);
4. the compatibility equations saying that \(S\rho(q)S^{-1}=\rho(\bar\tau(q))\), that the cohomology class of \(\eta\) is fixed by the induced action, and that the chosen lift has exact cube one.

These data give a multiplication table on \(N\times Q\), hence a group of exact order 128 without consulting the SmallGroups catalogue.

The possible action homomorphisms are reduced in `order-128-action-layer.md`: the \(A_4\)-image is \(1\), \(C_3\), or faithful \(A_4\); whenever it is nontrivial, the commuting \(C_4\)-action is forced to be trivial. Only this short action list needs cohomology calculations.

# Tests

For every admitted extension, form the two coordinate preimages
\[
K/N=1\times V_4,
\qquad
L/N=C_4\times1.
\]
Apply cheap exact invariants first: center order/type, derived subgroup order/type, exponent, Frattini quotient dimension, element-order counts, and lower-central data. Only invariant-matched pairs proceed to an explicit isomorphism search. Any prospective success must output a pc presentation, the cocycle/action tables, the order-three lift, subgroup generators, and an explicit relation-checked isomorphism \(K\to L\).

# Scope and kill criterion

- A negative result excludes only nonsplit extensions at \(|P|=128\) with \(N\cong C_2^3\); it does not cover the four other groups of order eight, larger \(P\), or constructions outside the sufficient template.
- Kill the family after all cohomology classes for all compatible actions have exact invariant certificates and no isomorphism survives. Do not jump automatically to \(|P|=256\); reassess the other order-eight kernel types and expected certificate cost first.
- This search is a future heavy computation and requires a new exact Lead lease. No command has been written or run in the present cycle.
