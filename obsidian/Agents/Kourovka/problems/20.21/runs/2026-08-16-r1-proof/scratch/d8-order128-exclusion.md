---
title: "Exclusion of the D8 common-kernel family at order 128"
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

In the equivariant index-four template, there is no group \(P\) of order 128 whose combined-map kernel is \(N\cong D_8\) (where \(D_8\) has order eight).

# Outer actions

For \(D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\),
\[
Aut(D_8)\cong D_8,
\qquad
Inn(D_8)\cong V_4,
\qquad
Out(D_8)\cong C_2.
\]
The required lift gives an outer-action homomorphism
\[
C_4\times A_4\longrightarrow C_2.
\]
Every homomorphism \(A_4\to C_2\) is trivial, so the \(V_4\) and order-three factors are outer-trivial. The \(C_4\)-image is trivial or \(C_2\).

# The V4 preimage

As in any outer-trivial restriction, the preimage \(K/N=V_4\) is
\[
K\cong(D_8\times E_V)/\Delta C_2,
\]
where \(E_V\) is a central extension of \(V_4\) by \(Z(D_8)=C_2\). Order-three invariance leaves:

- \(E_V\cong C_2^3\), giving \(K\cong D_8\times V_4\) and \(Z(K)\cong C_2^3\);
- \(E_V\cong Q_8\), giving \(K\cong D_8\circ Q_8\), an extraspecial group with \(Z(K)\cong C_2\).

# The C4 preimage

If the \(C_4\)-outer action is trivial, the two central extension classes give
\[
L\cong D_8\times C_4,
\qquad Z(L)\cong C_2\times C_4,
\]
or
\[
L\cong D_8\circ C_8,
\qquad Z(L)\cong C_8.
\]

For nontrivial outer action, choose the order-two representative
\[
\theta:r\mapsto r^{-1},\qquad s\mapsto rs
\]
of the nontrivial element of \(Out(D_8)\). A normalized extension has a lift \(t\) with conjugation \(\theta\) and \(t^4=z^\varepsilon\), where \(z=r^2\). Exactly as in the quaternion calculation, \(t^2\) is central, odd \(t\)-cosets cannot contain central elements, and
\[
Z(L)=\langle z,t^2\rangle\cong C_2^2\quad\text{or}\quad C_4.
\]

The possible centers of \(K\) have orders 8 and 2, whereas the possible centers of \(L\) have order 8 with exponent 4 or 8, or order 4. No types match. Hence \(K\not\cong L\) in every outer-action and factor-set case.

# Limit

This excludes exactly the \(|P|=128\), \(N\cong D_8\) family inside the sufficient template. It does not cover abelian kernels of order eight, larger \(P\), or the original target outside the template.
