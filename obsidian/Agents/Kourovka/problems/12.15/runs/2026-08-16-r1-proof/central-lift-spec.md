---
title: "Exact central-lift specification after the 12.15 partial reduction"
author: operator
tags:
  - agent/problem
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
active_assignment_answered: no
---

# Purpose and boundary

This is the bounded action-plus-central-cocycle deliverable requested by Lead. It parametrizes the first possible order of a hypothetical minimum counterexample and states every row a future hand proof or explicitly leased verifier must check. It neither runs a search nor asserts that any parameter system exists.

# Dependencies

## Independently audited core

For every admissible finite 2-group, with

\[
D_G(x)=\{[x,g]:g\in G\},
\]

the source hypothesis is equivalent to: every \(D_G(x)\) is a subgroup and \(x^2\in D_G(x)\). This is quotient-closed. A least-order counterexample would satisfy

\[
Z(G)=G''=\langle z\rangle\cong C_2,
\qquad xz\sim_Gx\quad(x\notin Z(G)).
\]

Validator reported no gap in these dependencies and retained `active_assignment_answered: no`.

## Current-run secondary dependencies awaiting separate audit

Writing \(H=G'\), \(A=Z(H)\), and \(E=G/H\):

- \(G^2\le G'\), hence \(H=\Phi(G)\) and \(E\) is the minimum-generator quotient;
- \(H'=\langle z\rangle\), \(H/A\) is a nonzero symplectic \(\mathbf F_2\)-space, \(\exp A\le8\), and \(\exp H\le16\);
- a faithful irreducible central-type character gives \(|G|=2^{2n+1}\), and the lower-central argument excludes order 32, so \(|G|\ge128\);
- Clifford analysis gives \(|E:C_E(A)|=|A:\langle z\rangle|\);
- if \(G\) is 2-generated, then \(\dim_{\mathbf F_2}H/A=2\).

The clean-run log proves each item and labels the separation from the audited core.

# Surviving order-128 regimes

Put \(V=H/A\). The 2-generator dimension lemma removes the former row with \((|E|,|H|,|A|,|V|)=(4,32,2,16)\). The surviving regimes are:

| regime | generator rank \(d\) | \(E\) | \(|H|\) | \(A\) | \(V\) | forced action sizes |
|---|---:|---|---:|---|---|---|
| R1 | 4 | \(C_2^4\) | 8 | \(C_2=\langle z\rangle\) | \(C_2^2\) | image on \(V\) has order at most 2 |
| R2 | 3 | \(C_2^3\) | 16 | \(C_4\) or \(C_2^2\) | \(C_2^2\) | image on \(A\) has order 2; image on \(V\) at most 2 |
| R3 | 2 | \(C_2^2\) | 32 | \(C_8\), \(C_4\times C_2\), or \(C_2^3\) | \(C_2^2\) | faithful action on \(A\); image on \(V\) has order 2 |

In R1, \(H\) is \(D_8\) or \(Q_8\). In R3, if \(c\) is the basic commutator of a minimal generating pair, then \(D_G(c)\) is an abelian maximal subgroup of \(H\), contains \(A\), and \(cD_G(c)\) is a constant-order conjugacy class of size 16.

# Layer 1: exact central extension defining \(H\)

For each regime choose:

1. the listed finite abelian 2-group \(A\), with a distinguished element \(z\) of order 2;
2. \(V=C_2^2\), written additively;
3. a normalized central 2-cocycle \(\eta:V\times V\to A\), satisfying

\[
\eta(0,u)=\eta(u,0)=1,
\]

\[
\eta(u,v)\eta(u+v,w)=\eta(v,w)\eta(u,v+w)
\quad(u,v,w\in V).
\]

Define multiplication on \(H=A\times V\) by

\[
(a,u)(b,v)=(ab\,\eta(u,v),u+v).
\]

The alternating part must obey

\[
\eta(u,v)\eta(v,u)^{-1}=\beta(u,v)\in\langle z\rangle,
\]

where \(\beta:V\times V\to\langle z\rangle\cong\mathbf F_2\) is the unique nondegenerate alternating form up to basis. Required Layer-1 rows are:

| row | exact requirement | dependency / purpose |
|---|---|---|
| H1 | normalized cocycle identity for every \(u,v,w\) | associativity of \(H\) |
| H2 | alternating part has image exactly \(\langle z\rangle\) and is nondegenerate | \(H'=\langle z\rangle\), \(Z(H)=A\) |
| H3 | \(|A||V|\) equals the regime's \(|H|\) | exact order, no hidden quotient |
| H4 | squares \((a,u)^2=a^2\eta(u,u)\) respect \(\exp A\le8\), \(\exp H\le16\) | secondary exponent restriction |

# Layer 2: exact extension defining \(G\)

Write \(E=C_2^d\) additively. Choose a normalized section symbol \(s(e)\) and data

\[
\alpha_e\in\operatorname{Aut}(H),
\qquad f(e_1,e_2)\in H,
\]

using the convention \(\alpha_e(h)=s(e)h s(e)^{-1}\) and

\[
f(e_1,e_2)=s(e_1)s(e_2)s(e_1+e_2)^{-1}.
\]

The exact compatibility equations are

\[
\alpha_0=\operatorname{id},
\qquad f(0,e)=f(e,0)=1,
\]

\[
\alpha_e\alpha_f=\operatorname{Inn}(f(e,f))\,\alpha_{e+f},
\]

\[
f(e,f)f(e+f,k)=\alpha_e(f(f,k))f(e,f+k)
\quad(e,f,k\in E),
\]

where \(\operatorname{Inn}(h)\) denotes \(x\mapsto hxh^{-1}\). Multiplication on \(G=H\times E\) is then

\[
(h,e)(k,f)=(h\,\alpha_e(k)\,f(e,f),e+f).
\]

Required Layer-2 rows are:

| row | exact requirement | dependency / purpose |
|---|---|---|
| G1 | all normalization, weak-action, and factor-set equations above | associativity and exact reconstruction |
| G2 | every \(\alpha_e\) fixes \(z\), preserves \(A\), and induces a symplectic map on \((V,\beta)\) | characteristic subgroups and commutator form |
| G3 | \(A^E=\langle z\rangle\), with the action sizes listed in R1–R3 | ensures no extra center inside \(A\); uses secondary Clifford row for exact sizes |
| G4 | direct computation from the multiplication law gives \(Z(G)=\langle z\rangle\) | also excludes central section lifts outside \(H\) |
| G5 | \(H=\langle H',\,[H,s(e)],\,[s(e),s(f)]:e,f\in E\rangle\) | ensures the reconstructed group's derived subgroup is exactly \(H\), not a proper subgroup |
| G6 | \(G/H\cong E\), \(|G|=128\), and \(H=\Phi(G)\) | exact regime and minimum-generator rank |
| G7 (R3) | the basic section commutator normally generates \(H\), with its defect subgroup the required abelian maximal subgroup | two-generator dependency |
| H5 (R3; deferred from Layer 1) | some lift \(c\) has the logged abelian maximal defect subgroup shape | depends on the completed group through \(D_G(c)\); enforced at this level alongside G7 |

The commutators in G5 are evaluated from the displayed multiplication law; no simplifying commutativity assumption is permitted.

# Layer 3: exact source-hypothesis and target rows

For each reconstructed element \(x=(h,e)\), compute using only the multiplication law

\[
D_G(x)=\{x^{-1}g^{-1}xg:g\in G\}.
\]

The decisive rows are:

| row | exact requirement | result meaning |
|---|---|---|
| P1 | identity belongs to \(D_G(x)\), and the set is closed under products and inverses, for every \(x\) | \(D_G(x)\) is a subgroup; audited equivalent-hypothesis row |
| P2 | \(x^2\in D_G(x)\) for every \(x\) | audited square row; together with P1 exactly the source hypothesis |
| P3 | for every noncentral \(x\), \(z\in D_G(x)\) and hence \(xz\sim_Gx\) | minimum-counterexample consistency check |
| P4 | \([H,H]=\langle z\rangle\ne1\) | target conclusion is violated in a counterexample parameter system |

Rows P1–P2 must be checked upstairs for every element (or for explicitly justified conjugacy representatives). Checking only their images in \(A\), \(V\), or \(E\) is insufficient. A hand proof in the assigned direction must show that H1–G7 force some P1 or P2 row to fail, or force P4 to become trivial. Assuming the defect subgroups commute is circular because that would already force the missing metabelian conclusion.

# Independent certificate for any future leased verifier

A reproducible certificate must contain:

1. explicit multiplication tables or normalized value tables for \(A,V,E,\eta,\alpha,f\);
2. verbatim checks of every H1–H5 and G1–G7 equation;
3. a reconstructible full multiplication table for the resulting 128-element group;
4. every element's defect-set identifier, subgroup closure check, and square-membership witness for P1–P2;
5. independent center, first-derived, and second-derived subgroup calculations for P3–P4;
6. a second implementation or hand reconstruction that does not trust the discovery code or constants.

No parameter tuple, multiplication table, finite coverage claim, or solution claim is produced in this run.
