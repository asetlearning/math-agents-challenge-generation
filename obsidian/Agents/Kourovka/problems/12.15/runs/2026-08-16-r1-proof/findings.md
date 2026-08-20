---
title: "Partial result for Kourovka 12.15: intrinsic fibres and minimum counterexamples"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/commutators
  - project/kourovka
  - status/conjectured
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Partial result

## Active target

Scope: `12.15/normal-closure-fibres`

Target: For every finite 2-group \(G\) in which any two elements with the same normal closure are conjugate, the derived subgroup \(G'\) is abelian.

This note does **not** establish the target conclusion.

## Result

For a finite 2-group \(G\), define the fixed-first-entry commutator value set

\[
D_G(x)=\{[x,g]:g\in G\}.
\]

Then the active normal-closure-fibre hypothesis is equivalent to:

1. \(D_G(x)\) is a subgroup for every \(x\in G\);
2. \(x^2\in D_G(x)\) for every \(x\in G\).

For an admissible \(G\), if \(N_x=\langle x\rangle^G\), then for every \(x\ne1\)

\[
D_G(x)=N_x^2[N_x,G],
\qquad |N_x:D_G(x)|=2,
\qquad x^G=N_x\setminus D_G(x)=xD_G(x).
\]

The intrinsic conditions are inherited by quotients. Consequently, if a counterexample of least order exists, then

\[
Z(G)=G''\cong C_2,
\]

\(G''\) lies in every nontrivial normal subgroup, and, writing \(G''=\langle z\rangle\),

\[
xz\sim_Gx \quad\text{for every }x\notin Z(G).
\]

Validator independently reported no gap in the fibre equality, intrinsic characterization, quotient inheritance, or these least-counterexample consequences, while explicitly retaining `active_assignment_answered: no`; see the current inbox report `2026-08-16T121217Z__Validator__REPORT__relative-frattini-partial.md`. The complete line-by-line proof is in `log.md` in this run directory.

## Further current-run deductions

The following hand deductions narrow the remaining case but are not needed for the independently audited core result:

- a minimum counterexample has a faithful irreducible complex character \(\chi\) vanishing off \(Z(G)\), so \(|G|=2\chi(1)^2=2^{2n+1}\);
- elementary lower-central-series arguments exclude order 32, hence a minimum counterexample has \(|G|\ge128\);
- with \(A=Z(G')\), one has \(\exp A\le8\) and \(\exp G'\le16\);
- \(G'/Z(G')\) is a nonzero symplectic \(\mathbf F_2\)-space acted on by the elementary-abelian group \(G/G'\), and every orbit-difference set is a vector subspace.
- if a minimum counterexample is 2-generated, then \(\dim_{\mathbf F_2}G'/Z(G')=2\); consequently only three exact size patterns remain at the first possible order 128.

The log gives the proofs and also gives an explicit symplectic action showing that the projected orbit condition alone does not force the symplectic space to vanish. The central lift and cocycle cannot be discarded.

Lead's bounded follow-up is recorded in `central-lift-spec.md`: it gives the three surviving order-128 regimes, normalized cocycle/weak-action equations reconstructing the full group, every upstairs defect-set row, and the independent certificate required for any future leased verifier. It contains no parameter tuple or coverage claim.

## Constraint status

| constraint_id | role | use in the partial result | result for active target |
|---|---|---|---|
| `12.15-forall-G` | admissibility | the intrinsic lemma is proved for an arbitrary admissible \(G\); the least-counterexample part is conditional | pass for the reduction |
| `12.15-finite` | admissibility | finiteness is used in the maximal invariant subgroup, minimal normal subgroup, and minimal-counterexample arguments | pass for the reduction |
| `12.15-two-group` | admissibility | the prime 2 is used for order-2 chief factors, square conditions, and elementary-abelian quotients | pass for the reduction |
| `12.15-normal-closure-fibre` | admissibility | used exactly to identify \(N_x\setminus N_x^2[N_x,G]\) with one conjugacy class | pass for the reduction |
| `12.15-derived-abelian` | target conclusion | reduced to excluding a monolithic central extension with \(Z(G)=G''=C_2\) | **not proved** |

## Exact scope covered and uncovered

Covered: an intrinsic equivalence, quotient closure, and necessary structure of a least-order counterexample for the exact active class of finite 2-groups.

Uncovered: the possibility that a finite 2-group satisfies all intrinsic defect-subgroup conditions while \(G''=Z(G)\cong C_2\). No proof that the compatible central extension is impossible has been obtained.

## Computational-status correction

One exact 128-element permutation-group diagnostic was run before Lead corrected the compute interpretation. Common-protocol §4 requires a lease for enumeration regardless of runtime; that diagnostic was unleased and is retained only as exploratory output in the log. It is not evidence for the hand reduction, not catalogue coverage, and not a certificate. No further enumeration was performed after the correction.

## How this partial result could be wrong

1. The relative maximal-invariant-subgroup argument could conceal a normality or quotient error; Validator reports having independently checked precisely this step and found none.
2. The reverse intrinsic implication could fail if \(D_G(x)\) were not normal; the proof explicitly derives normality from conjugacy-class stability before using it.
3. Quotient inheritance could be confused with an unjustified lift of normal closures; the proof instead passes the intrinsic commutator-value conditions to the quotient.
4. The later character, order, exponent, or symplectic deductions may contain a gap not covered by Validator's stated core audit; none is used to claim the target conclusion.

## What this does not establish

It does not prove \(G''=1\), does not provide a counterexample, does not certify any finite-order catalogue range, and does not answer the active assignment.
