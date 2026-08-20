---
title: "MathExpert: mixed-fibre obstruction and central-lift value for 12.15"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
---

# Scope and sourcing

This addresses revision 1 of the finite-2-group normal-closure-fibre scope. Everything below is **General knowledge, unverified** or a fresh hand assessment of the current clean run. No web or historical problem artifact was consulted.

# Assessment of the fixed-element lemma

The lemma

\[
D_G(x)=\{[x,g]:g\in G\}\text{ is a normal subgroup containing }x^2
\]

is strong enough for the audited quotient and least-counterexample reductions, but it has no evident short local route to \(G''=1\). Its sharp limitation is that it controls one first-entry fibre at a time. Metabelianity is a mixed assertion about commutators between values belonging to different fibres.

The strict nesting fact makes the endpoint especially clear. If \(1\ne d\in D_G(x)\), then \(D_G(d)<D_G(x)\): normality gives containment, while equality would put \(d\) in its own defect subgroup. In a least counterexample this produces elements \(a\in G'\setminus Z(G)\) with

\[
D_G(a)=Z(G)=G''\cong C_2.
\]

That is compatible with dihedral, quaternion, and extraspecial local sections. It does not force \(a\) to be central. The missing statement would have to compare \(D_G(x)\) and \(D_G(y)\), or equivalently control the central factor set measuring their interaction. Assuming that those subgroups commute is exactly the desired conclusion in disguise.

# Value of the order-128 central-lift route

The current `central-lift-spec.md` is genuinely useful as a finite certificate/search specification. Its two extension layers retain the weak action and nonabelian factor set, and rows P1--P2 recheck the original hypothesis upstairs. This avoids the demonstrated loss in the projected symplectic-module and center-module models.

Its usefulness is limited in a precise way:

- excluding all three order-128 regimes would strengthen the least-counterexample lower bound but would not settle arbitrary order;
- the isolated module conditions are consistent in nonzero rank, so more linear classification alone is unlikely to pay;
- a leased exact check would be worthwhile only if Lead values a certified order-128 exclusion. As a hand route to the universal assertion, the specification is a natural stopping point rather than evidence that a contradiction is near.

# Ranked next strategies

## M1 — square map on the surviving two-generator coset

In regime R3, write \(H=G'=\langle c,D\rangle\), where \(D=D_G(c)\) is an abelian maximal subgroup containing \(A=Z(H)\), and \(cD=c^G\). Since \(H\) has class two, the map

\[
q:D\longrightarrow A,
\qquad q(d)=d^2[c,d]
\]

is a homomorphism, and

\[
(cd)^2=c^2q(d).
\]

Because \(cD\) is one conjugacy class, the image \(c^2q(D)\) is exactly the conjugacy orbit of \(c^2\). First bounded experiment: combine this homomorphism with the faithful \(E=C_2^2\)-action on the three possible groups \(A\) of order eight and the condition \(A^E=\langle z\rangle\). A contradiction in all three cases would eliminate R3 by hand.

Success certificate: three explicit abelian-group/action calculations, with no classification of the full group. Kill criterion: stop if every compatible \(q(D)\) occurs in an elementary shear model; then the square orbit is another necessary-but-not-sufficient projection.

Cost: one to two hand hours.

## M2 — exact mixed-fibre cocycle identity

For arbitrary \(x,y,g\),

\[
[xy,g]=[x,g]^y[y,g].
\]

In the least-counterexample central extension, project this identity to the symplectic module and retain the residual \(z\)-valued factor. The target is a polarization formula expressing

\[
[D_G(x),D_G(y)]\le\langle z\rangle
\]

as the alternating part of that factor set. Then use subgroup closure for \(D_G(xy)\), \(D_G(xy^{-1})\), and \(D_G(xz)\) to try to force the alternating part to vanish.

Success certificate: a convention-fixed identity killing one mixed pairing without assuming either defect subgroup abelian. Kill criterion: if closure only says the residual values form \(\{1,z\}\), the route has merely restated the obstruction.

Cost: two to four hand hours.

## M3 — finite order-128 certificate check

If a compute lease is later granted, the exact data in `central-lift-spec.md` define a bounded search over three regimes. The certificate must reconstruct multiplication and check P1--P4 elementwise; projected orbit conditions are not enough.

Success certificate: an independently reproducible exhaustion or a concrete admissible multiplication table. Kill criterion: do not enlarge to higher orders if order 128 survives only through a large undirected parameter space.

Cost: tooling-dependent and requires a lease.

# Self-critique

The square-map refinement may still be absorbed by the shear examples already present in the run. The mixed-fibre route is the only proposed hand strategy that attacks the missing compatibility directly, but its likely failure mode is circularity: any unexplained orthogonality or commuting assertion is already metabelianity. The honest current assessment is therefore: the audited lemma yields a substantial structural reduction, while the central extension remains a real obstruction rather than a one-line final case.
