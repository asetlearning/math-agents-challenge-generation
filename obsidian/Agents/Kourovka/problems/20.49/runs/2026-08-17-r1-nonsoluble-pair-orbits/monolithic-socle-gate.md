---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - project/kourovka
  - status/conjectured
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
direction: counterexample
strategy: MONOLITHIC-SOCLE-GATE
---

# Monolithic-socle gate: explicit obstruction

The presently established exponent-critical and direct-indecomposability conditions do **not** by themselves force a unique minimal normal subgroup.

Let

```text
D = <r,s | r^15=1, s^2=1, srs=r^(-1)>,
```

the dihedral group of order 30.

## Required properties of the obstruction

1. `exp(D)=lcm(15,2)=30`: rotations have orders dividing 15 and reflections have order 2.
2. Every proper subgroup has exponent below 30. A subgroup inside `<r>` is cyclic of order dividing 15. A subgroup not inside `<r>` is dihedral on a proper rotation subgroup, so has order `2m` with `m in {1,3,5}` and exponent `2m in {2,6,10}`.
3. Every nontrivial proper quotient has exponent below 30. Every proper normal subgroup is contained in `<r>`; quotienting by the rotation subgroups of orders 3, 5, or 15 gives respectively dihedral groups of rotation orders 5 or 3, or `C2`, with exponents 10, 6, or 2.
4. `D` is directly indecomposable. The normal closure of any reflection is all of `D` (products of its conjugate reflections generate the rotations). Hence every proper normal subgroup lies in the odd-order rotation group. Two proper normal direct factors would therefore have odd-order product and cannot equal `D`.
5. `D` has at least two distinct minimal normal subgroups: `<r^5>` of order 3 and `<r^3>` of order 5.

Thus subgroup-exponent-criticality, quotient-exponent-criticality, and direct indecomposability coexist with a non-monolithic socle.

## Exact limitation

This obstruction is soluble and two-generated, so it is not a candidate for Problem 20.49 and does not show that the *full* least-counterexample package (which also includes nonsolubility and `d(G)=3`) permits multiple minimal normal subgroups. It does show that the submitted direct-indecomposability argument cannot be upgraded to monolithicity from the two exponent-critical conditions alone. A new use of nonsolubility or three-generation would be required before an abelian/nonabelian unique-socle split is justified.

