---
title: "RANK4-H3-SHEAR-ORBIT-SUPPORT — complete projected-support exclusion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: RANK4-H3-SHEAR-ORBIT-SUPPORT
direction: counterexample
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - topic/power-maps
  - project/kourovka
  - status/replicated
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/manifest.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/leased-output.md
---

# Active target

Scope: `21.137/odd-prime-exponent-p2`, assignment revision `2`.

Target: for odd prime `p`, a finite same-`p` group `G` of exact exponent
`p^2` whose literal actual power set `P={g^p:g in G}` is a subgroup; decide
whether `P` must be abelian.  The `p=2`/exponent-eight sibling is excluded.

# Bounded claim under review

For the one frozen `p=3` rank-four kernel/Heisenberg-quotient automorphism row
with the exact matrices, center actions, and labels in `manifest.md`, all
`3^19` solutions of the complete 56-equation shear system lie in exactly three
admissible lift/conjugacy orbits.  For every orbit the factor-independent image
`Sigma` of the literal cube set in `V=K/Z(K)` is not an `F3`-subspace.  Hence no
central factor system realizing any shear in this frozen automorphism row can
make the literal cube set a subgroup.  This is a bounded family exclusion, not
a counterexample and not an answer to the source scope.

# What was computed in

The exact finite object was the affine `F3` solution space of triples
`(LX,LY,LZ) in Mat(3,4)^3` satisfying the 56 displayed automorphism-lift
equations for fixed `A,B,C,TX,TY,TZ,qX=f2,qY=e2`.

It was **not** a group, presentation, factor system, central cochain family, or
literal cube enumeration.  No submitted `6,561/27/135/729` result entered the
checker.

# Exact classification

- Independently reconstructed system: 56 equations, 36 variables, coefficient
  and augmented rank 17, affine dimension 19.
- The 12 independent inner lift changes together with the 12 simultaneous
  kernel-shear changes span an 18-dimensional translation gauge.
- The complete finite stabilizer is the nine pairs
  `D_a:f1->f1+a e1`, `U_d:t->t+d c`.  Its induced action fixes every point of
  the one-dimensional quotient.
- Therefore there are exactly three genuine orbits, each of size `3^18`, and
  the orbit-size sum is `3^19=1,162,261,467`.
- Every one of the 27 norm images is zero.  The three complete projected
  supports have sizes `15,15,13`; each spans `<e1,e2,f2>` and has restricted
  symplectic rank two, but none is a subspace.
- In every orbit `e2` and `f2` occur while `e2+f2` does not.  This is an exact
  additive-closure defect.  The full 27-row tables are in `leased-output.md`.

# Why the projected obstruction is factor-independent

For a section representative with conjugation action `alpha_h`, its cube acts
innerly as `J_lambda`.  If a kernel element has image `v in V`, then the cube
of the corresponding root has projected value

`lambda+(I+M_h+M_h^2)v`.

Thus the image of the **literal** cube set is exactly
`Sigma=union_h(lambda_h+W_h)`, regardless of central factor coordinates.  If
the literal cube set were a subgroup, its homomorphic image in the elementary
abelian group `V` would be an `F3`-subspace.  Each classified orbit violates
that necessary condition.

# Constraint-and-limitation matrix

| constraint_id | role | required condition | bounded computation / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | Every admissible odd `p,G` | Only `p=3` and one frozen automorphism row are classified. | manifest and full orbit table | **not established universally** |
| `21.137-odd-p-not-2` | admissibility | `p>2` prime | Frozen parameter is `p=3`; no `p=2` object enters. | checker field and manifest | pass for bounded family |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | No group is constructed; the result conditionally excludes every finite extension realizing the frozen row. | factor-independent projection argument | no witness; bounded exclusion only |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | Exponent is not tested because the subgroup hypothesis already fails at the projected pre-cohomology gate; in particular any exponent-nine realization is excluded. | all-orbit closure defect | no witness; bounded exclusion only |
| `21.137-odd-power-set-definition` | admissibility | literal actual set, not generated subgroup | `Sigma` is derived coset-by-coset from every actual root using the cube norm formula; no generated-power comparator is used. | 27 complete affine-support rows per orbit | pass for projected literal set |
| `21.137-odd-power-set-subgroup` | admissibility | literal set itself a subgroup | Its image would be a subspace, but all three images contain `e2,f2` and omit `e2+f2`. | sizes `15,15,13` and explicit defect | violated for every frozen shear orbit |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | No row reaches the subgroup hypothesis, so abelianity is not tested and no source conclusion follows. | limitation of necessary gate | not established |

# What this does not establish

It does not construct a finite group, prove exponent nine, compute any central
factor system, or say that every rank-four kernel action has this defect.  It
does not exclude another outer action, center action, label pair, quotient,
kernel, or odd prime.  It neither proves nor refutes the universal assertion.
`active_assignment_answered: no`.

# How this bounded claim could be wrong

1. The 56 equations could have been ordered or signed incorrectly despite the
   independent matrix reconstruction.
2. The displayed inner lift changes or nine-element stabilizer might omit an
   admissible equivalence, although completeness is derived in `manifest.md`.
3. The section convention might reverse the action/cube formula; Validator
   should reconstruct one mixed word and the universal defect by hand.
4. The bespoke exact-linear-algebra implementation could contain a common bug;
   an independent implementation should reproduce ranks, three orbits, and the
   27-row tables without importing the checker.

# Outcome

`PARTIAL_RESULT`: complete factor-independent exclusion of the one frozen
rank-four/H3 automorphism-lift family.  The selected strategy is exhausted and
no support-pass orbit exists to justify cohomology.  The unrestricted source
scope remains active and all unused minutes return to Lead.

Verified by [[Agents/Kourovka/problems/21.137/verification/2026-08-17T2302Z-rank4-shear-orbit-support.md]].
