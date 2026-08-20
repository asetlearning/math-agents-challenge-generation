---
title: "MathExpert: audit and cocycle target for the equivariant 20.21 construction"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/extensions
  - topic/p-groups
  - project/kourovka
  - status/conjectured
problem: 20.21
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
---

# Scope and sourcing

This addresses the sufficient equivariant 2-group template in revision 1, not every possible solution of the original existence problem. Everything below is **General knowledge, unverified** or a fresh hand audit of the current clean run. No web or historical artifact was used.

# Audit of the sufficient reduction

I found no gap in the semidirect-product reduction, but it still needs independent checking. If

\[
f:P\twoheadrightarrow C_4,qquad h:P\twoheadrightarrow V_4,
\]

and an order-three automorphism \(\sigma\) satisfies \(f\sigma=f\) and \(h\sigma=\tau h\), then the two displayed maps from \(P\rtimes_\sigma C_3\) have kernels \(\ker f\) and \(\ker h\), respectively, and quotients \(C_{12}\) and \(A_4\). No hidden kernel element involving the \(C_3\)-coordinate occurs because both quotient maps retain that coordinate.

There is a useful forced strengthening. Put

\[
K=\ker f,qquad L=\ker h,qquad N=K\cap L.
\]

The subgroup \(h(K)\) is \(\tau\)-invariant. Irreducibility of \(\tau\) on \(V_4\) makes it either zero or all of \(V_4\); the zero case would give \(K=L\), impossible because the quotient types differ. Therefore

\[
K/N\cong V_4,qquad L/N\cong C_4,qquad P=KL,
\]

and the combined map is an epimorphism

\[
P\twoheadrightarrow C_4\times V_4.
\]

Thus the common-\(C_2\) fibre-product branch is incompatible with the required order-three equivariance.

# Assessment of the current exclusions

The abelian-kernel argument in the run log looks mathematically credible. Coprime decomposition under \(\sigma|_K\) makes the moving part a module over the unramified quadratic ring over \(\mathbb Z/2^t\). Passing to the irreducible \(V_4\) quotient lowers two equal invariant factors, while transporting \(N\) across \(K\cong L\) makes it a kernel of a cyclic \(C_4\) quotient and can lower each elementary layer by at most one. Those two invariant-factor changes are incompatible. This step deserves Validator review because it uses the module classification over that local ring, but I see no immediate gap.

The consequences are appropriately sharp:

- \(K\) and \(L\) must be nonabelian;
- \(N\) cannot be central in \(P\);
- a split construction with elementary-abelian \(N\) is impossible by comparing derived-subgroup ranks and Frattini generator ranks;
- the completed order-16/32/64 scan is a bounded exclusion only, and its negative result correctly triggers a representation change.

# Recommended structured family

Parametrize the next search as one nonabelian extension, not as a larger catalogue. Let

\[
Q=C_4\times V_4,
\]

choose a finite 2-group \(N\), an outer action

\[
\rho:Q\to\operatorname{Out}(N),
\]

and a nonabelian factor set \(\kappa\) defining an extension

\[
1\to N\to P(N,\rho,\kappa)\to Q\to1.
\]

Require an automorphism \(s\in\operatorname{Aut}(N)\) of order dividing three and a lift \(\sigma\in\operatorname{Aut}(P)\) satisfying

\[
\sigma_Q=\operatorname{id}_{C_4}\times\tau,
\]

which becomes explicit equivariance equations on \(\rho\) and \(\kappa\). The two restricted extensions over \(V_4\le Q\) and \(C_4\le Q\) must have isomorphic total groups; these are exactly \(K\) and \(L\).

The first live family should take \(N\) nonabelian of class two and exponent four, while allowing the full extension \(P\) to have class three. Central \(N\), elementary split \(N\), and abelian total kernels have already been excluded, so a purely linear module family repeats dead work.

First bounded experiment: before solving cocycle equations, inspect whether \(\operatorname{Out}(N)\) contains compatible images of \(C_4\) and \(V_4\) whose ordered pair is normalized by an element of order three acting as \(\tau\) on the latter and trivially on the former. This is a cheap structural filter.

Success certificate: an explicit presentation for \(N\), action lifts, factor-set table, isomorphism \(K\to L\), and formulas for \(f,h,\sigma\). Kill criterion: if every small \(N\) fails already in \(\operatorname{Out}(N)\), stop before constructing extensions and reassess the full-product/non-2-group branches of the original Goursat problem.

# Self-critique

This parametrization is sharper than a group catalogue but can still become a cohomology catalogue. Its value is that failures split cleanly into action, extension, and kernel-isomorphism obstructions. It does not imply that the sufficient template contains a witness, and a negative result for this family would not answer the original Kourovka scope.
