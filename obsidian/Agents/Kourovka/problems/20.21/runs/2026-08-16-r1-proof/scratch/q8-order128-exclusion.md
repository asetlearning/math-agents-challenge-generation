---
title: "Exclusion of the Q8 common-kernel family at order 128"
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

In the equivariant index-four template, there is no group \(P\) of order 128 whose combined-map kernel is \(N\cong Q_8\).

# Outer actions

The clean equivariant Goursat reduction gives
\[
1\longrightarrow N\longrightarrow P\longrightarrow
Q=C_4\times V_4\longrightarrow1
\]
and an order-three lift of the automorphism fixing \(C_4\) and cycling the nonzero elements of \(V_4\). Hence the outer action extends to
\[
C_4\times A_4\longrightarrow Out(Q_8)\cong S_3.
\]
There are three types:

1. \(A_4\twoheadrightarrow C_3\), with outer-trivial \(C_4\);
2. outer-trivial \(A_4\), with \(C_4\twoheadrightarrow C_2\);
3. both factors outer-trivial.

In every type, the \(V_4\)-action on \(Q_8\) is outer-trivial.

# The V4 preimage

Let \(K/N=V_4\). After changing lifts by elements of \(Q_8\), an outer-trivial action is represented by lifts centralizing \(Q_8\). Thus
\[
K\cong(Q_8\times E_V)/\Delta C_2,
\]
where \(E_V\) is a central extension of \(V_4\) by \(Z(Q_8)=C_2\), and the two central involutions are identified.

The order-three symmetry restricts the extension class to the fixed line in \(H^2(V_4,C_2)\). There are two cases:

- the zero class, \(E_V\cong C_2^3\), giving \(K\cong Q_8\times V_4\) and \(Z(K)\cong C_2^3\);
- the nonzero invariant class, whose quadratic form is nonzero on every nonzero vector of \(V_4\), so \(E_V\cong Q_8\); this gives the central product \(K\cong Q_8\circ Q_8\), with \(Z(K)\cong C_2\).

Mixed factor-set terms involving the \(C_4\) coordinate do not change the restriction to this preimage.

# The C4 preimage: outer-trivial cases

Let \(L/N=C_4\). In outer-action types 1 and 3, the \(C_4\)-action is outer-trivial, so
\[
L\cong(Q_8\times E_C)/\Delta C_2
\]
for a central extension \(E_C\) of \(C_4\) by \(C_2\). The two classes give:

- \(E_C\cong C_2\times C_4\), hence \(L\cong Q_8\times C_4\) and \(Z(L)\cong C_2\times C_4\);
- \(E_C\cong C_8\), hence \(L\cong Q_8\circ C_8\) and \(Z(L)\cong C_8\).

Neither center is isomorphic to \(C_2^3\) or \(C_2\), so \(K\not\cong L\).

# The C4 preimage: nontrivial outer action

In type 2, choose an order-two representative \(\theta\in Aut(Q_8)\) of the nontrivial element of \(Out(Q_8)\). A normalized extension has a lift \(t\) of the \(C_4\) generator with
\[
tnt^{-1}=\theta(n),
\qquad
t^4=z^\varepsilon,
\]
where \(z\) is the central involution of \(Q_8\) and \(\varepsilon\in\{0,1\}\). Since \(\theta^2=1\), the element \(t^2\) centralizes \(Q_8\), and it commutes with \(t\). No element in an odd coset \(Q_8t\) can be central because its induced outer automorphism is nontrivial. Therefore
\[
Z(L)=\langle z,t^2\rangle,
\]
which is \(C_2^2\) if \(\varepsilon=0\) and \(C_4\) if \(\varepsilon=1\). In either case \(|Z(L)|=4\), again different from the possible center orders 8 and 2 for \(K\).

# Conclusion and limits

All three outer-action types fail the isomorphism condition by center invariants. This excludes exactly the \(|P|=128\), \(N\cong Q_8\) family inside the sufficient equivariant template. It does not cover \(N\cong D_8\), the three abelian groups of order eight, larger \(P\), or the original target outside the template.
