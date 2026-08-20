---
title: "Split elementary-abelian obstruction for the equivariant index-four template"
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

Let \(N\cong C_2^d\). For arbitrary actions of \(V_4\) and \(C_4\) on \(N\), the split extensions
\[
X=N\rtimes V_4,\qquad Y=N\rtimes C_4
\]
are not isomorphic.

# Proof

Both complements are abelian, and \(N\) is abelian, so
\[
X'=[N,V_4],\qquad Y'=[N,C_4].
\]
These are vector subspaces of \(N\). If \(X\cong Y\), isomorphism invariance of the derived subgroup order gives
\[
\dim_{mathbb F_2}[N,V_4]=\dim_{mathbb F_2}[N,C_4]. \tag{1}
\]

For a finite 2-group \(T\), write \(d(T)=\dim_{mathbb F_2}T/\Phi(T)\). Since \(N\) and the \(V_4\)-complement have exponent two, the squares in \(X\) lie in \([N,V_4]\), and hence
\[
\Phi(X)=X^2X'=[N,V_4].
\]
Therefore
\[
d(X)=\dim N/[N,V_4]+2. \tag{2}
\]

Let \(t\) generate the split \(C_4\)-complement in \(Y\). Then
\[
\Phi(Y)=Y^2Y'=[N,C_4]\langle t^2\rangle.
\]
Here \(t^2\notin N\), while \([N,C_4]\le N\), so the displayed product contributes one independent complement direction. It follows that
\[
d(Y)=\dim N/[N,C_4]+1. \tag{3}
\]

Equation (1) makes the coinvariant dimensions in (2) and (3) equal. Thus \(d(X)=d(Y)+1\), contradicting \(X\cong Y\). This proves the statement.

# Scope of the obstruction

It excludes only split extensions with an elementary-abelian common kernel. It does not exclude nonsplit extensions, non-elementary or nonabelian kernels, larger equivariant groups \(P\), the full-product Goursat branch, or the original Kourovka target in general.
