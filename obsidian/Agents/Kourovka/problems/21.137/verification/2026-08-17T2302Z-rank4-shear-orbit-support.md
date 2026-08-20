---
title: "Verification — Kourovka 21.137 — rank-four H3 shear-orbit support"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For the frozen p=3 rank-four kernel/H3-quotient action with qX=f2 and qY=e2, every compatible shear class has a non-additively-closed factor-independent projected literal-cube support."
claimant: Problem-21.137-Counterexample
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the literal set P={g^p:g in G} is a subgroup, then P is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "the general powerful-subgroup clause", "all other actions, kernels, quotients, labels, and odd primes"]
target_object: "Every finite odd-prime p-group of exact exponent p^2 whose literal p-th-power set is a subgroup."
witness_object: "The affine F3 space of compatible 3-by-4 shear triples for one fixed rank-four kernel/H3 quotient action and fixed nonorthogonal labels."
witness_equals_target: false
citation: none
verification_method: "clean-room hand derivation plus one frozen independently written exact-F3 Python checker"
tools_used: ["Python 3.12.3", "GAP 4.12.1 (availability probe only)", "GNU sha256sum 9.4"]
scope_answered: ["RANK4-H3-SHEAR-ORBIT-SUPPORT frozen family only"]
scope_not_answered: ["21.137/odd-prime-exponent-p2", "all unfrozen p=3 families", "all odd primes other than 3"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.137

## The claim

The bounded claim is correct: every one of the `3^19` compatible shear rows in
the declared frozen `p=3` action/lift family has a factor-independent projected
literal-cube set that is not additively closed.  This excludes the family before
cohomology.  It does not construct a group and does not answer the universal
odd-prime problem.

## Scope, revision, and clause matrix

The rendered page 184 was checked directly.  Revision 2 accurately selects the
odd-prime, exponent-`p^2` abelianity clause.

| source clause | active | result of this verification |
|---|---:|---|
| If literal `p`-th powers form a subgroup, is it powerful? | no | not addressed |
| For `p != 2`, exponent `p^2`, must the literal-power subgroup be abelian? | yes | not answered universally; one frozen `p=3` family excluded |
| For `p=2`, exponent 8, must the square subgroup be abelian? | no | not opened |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independently checked use | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd `p,G` | only one `p=3` affine family was classified | not universal |
| `21.137-odd-p-not-2` | admissibility | odd prime | all arithmetic is over `F3`; no `p=2` input occurs | pass for bounded family |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime group | no group is claimed; realizations are excluded conditionally | no witness |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | not tested because the literal-set subgroup gate already fails in projection | no witness |
| `21.137-odd-power-set-definition` | admissibility | literal set, not generated verbal subgroup | every quotient coset is treated by its full affine norm image and the 27 images are unioned without taking generated closure | pass for projected literal set |
| `21.137-odd-power-set-subgroup` | admissibility | literal set itself is a subgroup | its projection contains `e2,f2` and omits `e2+f2` in every shear orbit | violated throughout frozen family |
| `21.137-odd-P-abelian` | target conclusion | `P` is abelian | no row reaches the subgroup hypothesis | not established |

## Target versus witness

The witness is not the target.  It is an affine compatibility space, not a
finite group.  The valid conclusion is conditional and negative: if a central
factor system realizes any row of this fixed action/lift family, its literal
cube set cannot be a subgroup.  Nothing here excludes other actions, kernels,
quotients, label pairs, or odd primes.

## Subclaims and what each method proves

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| triple transformations and equation count | hand derivation from the displayed law | signs, order, and completeness of the 56 residual coordinates | consistency of an extension group |
| ranks and all finite tables | separately written exact-`F3` checker | complete bounded linear certificate | the universal theorem |
| 24 gauge generators | hand provenance plus independent rank test | all declared inner-lift and kernel-shear directions, rank 18 | classification under unlisted quotient automorphisms (which could only merge the tested classes) |
| nine-element stabilizer | hand centralizer proof plus independent enumeration from defining equations | completeness within the frozen named-generator stabilizer | all abstract isomorphisms of possible groups |
| projected cube formula | hand group calculation | exact literal-cube projection and immunity to central factor changes | any central coordinate or exponent claim |
| closure defect | all 81 independently recomputed labels | failure of the necessary subgroup gate for every row | abelianity of a nonexistent/failed power subgroup |

## Hand reconstruction

For triples acting by `(v,z) -> (Mv,Tz+Lv)`, direct multiplication gives

```text
(M,T,L)^-1 = (M^-1,T^-1,-T^-1 L M^-1),
(M,T,L)^3  = (M^3,T^3,T^2 L + T L M + L M^2).
```

The two fixed labels require all 12 shear coordinates of `alphaX^3=J_qX`
and all 12 of `alphaY^3=J_qY`.  For each of `alphaZ^3`,
`[alphaX,alphaY]alphaZ^-1`, `[alphaX,alphaZ]`, and
`[alphaY,alphaZ]`, being inner is exactly vanishing of the two non-`c` rows,
giving `4*8` further coordinates.  Thus the complete gate has
`12+12+4*8=56` equations in 36 shear variables.

For a compatible kernel automorphism `beta=(D,U,R)`, direct conjugation gives

```text
L_i -> U^-1 (L_i D + T_i R - R M_i).
```

The `D=U=I` part therefore has all twelve matrix-unit directions in
`R in Mat(3,4)`.  Each named quotient lift may independently change by an
inner automorphism; nondegeneracy of `omega` identifies `V` with the four
possible `c`-row directions.  Since `I+A+A^2=I+B+B^2=0`, these changes preserve
the fixed `X,Y` labels.  These are exactly the displayed 12+12 generators.

For completeness of the finite stabilizer, fixing `e2` and `f2` and commuting
with `B` first forces `D(e1)=e1`.  Symplecticity then forces
`D(f1)=f1+a e1`; every such `D_a` commutes with `A,B,C`.  On the center,
commuting with `TY` and fixing `c` gives the upper-Toeplitz centralizer, while
also commuting with `TX` kills its `s`-translation term.  Thus
`U(c)=c`, `U(s)=s`, `U(t)=t+d c`; these `U_d` also commute with `TZ`.
There are precisely `3*3=9` pairs.

Before opening claimant code I also multiplied the particular mixed word
`alphaX alphaY`.  Its shear is `TX LY+LX B`, and
`T^2L+TLM+LM^2=0`; hence `lambda(1,1,0)=0000`.

## Why central cohomology cannot repair the projection

Let `K` be the fixed kernel, `V=K/Z(K)`, and let a section lift `s_h` induce
`alpha_h` with `V`-matrix `M_h`.  Since the quotient is the exponent-three
Heisenberg group, every cube lies in `K`.  For a root in the `h`-coset with
kernel projection `v`, the cube calculation gives

```text
pi(root^3) = lambda_h + (I+M_h+M_h^2)v.
```

Here `alpha_h^3=J_lambda_h`, so the noncentral projection of `s_h^3` is
`lambda_h`.  Every element of the coset supplies one `v in V`, making the
projected fibre exactly

```text
F_h = lambda_h + im(I+M_h+M_h^2).
```

Changing a realizing factor element while keeping its prescribed inner
automorphism multiplies it by an element of `Z(K)`.  Changing central cochain
or cocycle coordinates likewise changes only the central component of a cube.
All such changes vanish under `pi`.  Thus
`Sigma=union_h F_h` is factor-independent, not merely a necessary subset.

If the literal cube set were a subgroup, its image under the homomorphism
`pi:K->V` would be a subgroup of the elementary abelian group `V`, hence an
`F3`-subspace.  The displayed additive defect in `Sigma` therefore cannot be
repaired by any central cohomology class.

## Independent computation evidence

The clean-room checker and its pre-run manifest are
`verification/scratch/verify_shear_orbits_independent.py` and
`verification/2026-08-17T2252Z-independent-shear-orbit-checker-manifest.md`.
It was frozen before claimant-code inspection with SHA-256
`7e39608a1c8847271a47e1c1441b41759d18e38e8b42f4203fea6a2b2ecbe0d7`.

The single Lead-leased command, verbatim, was

```text
timeout 45s python3 Agents/Kourovka/problems/21.137/verification/scratch/verify_shear_orbits_independent.py --full
```

Runner result: exit code `0`, wall time `1.907130209` seconds, chunk `18e7a4`;
that runner record preserves the complete verbatim JSON stdout.  Its scalar
values are normalized here for readability:

```text
field: 3
system equations/variables/rank/augmented-rank/dimension: 56/36/17/17/19
particular LX: 0000/1100/0000
particular LY: 0000/1000/0000
particular LZ: 0000/0201/0000
gauge listed/inner-rank/total-rank: 24/12/18
signature image-dimension/kernel-dimension: 1/18
stabilizer D: 1000/0100/0010/0001, 1010/0100/0010/0001, 1020/0100/0010/0001
stabilizer U: 100/010/001, 101/010/001, 102/010/001
stabilizer pairs: 9
induced quotient map for every pair: [0,1,2]
Burnside fixed counts: 3,3,3,3,3,3,3,3,3
Burnside orbit count: 3
orbit sizes: 387420489,387420489,387420489
orbit-size sum: 1162261467
mixed-word 110 label: 0000
support sizes (independent numbering): 15,13,15
span dimensions: 3,3,3
restricted symplectic ranks: 2,2,2
```

The independent representatives map to claimant representatives as
`independent 0 -> claimant 0`, `independent 1 -> claimant 2`, and
`independent 2 -> claimant 1`.  After that harmless relabeling, all 81 cells
agree exactly:

| `h=(a,b,d)` | claimant/independent `r=0` | claimant/independent `r=1` | claimant/independent `r=2` | `W_h` |
|---|---:|---:|---:|---:|
| 000 | 0000 | 0000 | 0000 | 0 |
| 001 | 0000 | 0000 | 0000 | 0 |
| 002 | 0000 | 0000 | 0000 | 0 |
| 010 | 0100 | 0100 | 0100 | 0 |
| 011 | 1100 | 1100 | 1100 | 0 |
| 012 | 2100 | 2100 | 2100 | 0 |
| 020 | 0200 | 0200 | 0200 | 0 |
| 021 | 1200 | 1200 | 1200 | 0 |
| 022 | 2200 | 2200 | 2200 | 0 |
| 100 | 0001 | 0001 | 0001 | 0 |
| 101 | 2001 | 2001 | 2001 | 0 |
| 102 | 1001 | 1001 | 1001 | 0 |
| 110 | 0000 | 0000 | 0000 | 0 |
| 111 | 0000 | 0000 | 0000 | 0 |
| 112 | 0000 | 0000 | 0000 | 0 |
| 120 | 2000 | 1000 | 0000 | 0 |
| 121 | 2000 | 1000 | 0000 | 0 |
| 122 | 2000 | 1000 | 0000 | 0 |
| 200 | 0002 | 0002 | 0002 | 0 |
| 201 | 2002 | 2002 | 2002 | 0 |
| 202 | 1002 | 1002 | 1002 | 0 |
| 210 | 1000 | 2000 | 0000 | 0 |
| 211 | 1000 | 2000 | 0000 | 0 |
| 212 | 1000 | 2000 | 0000 | 0 |
| 220 | 0000 | 0000 | 0000 | 0 |
| 221 | 0000 | 0000 | 0000 | 0 |
| 222 | 0000 | 0000 | 0000 | 0 |

The three unions have sizes `15,15,13`.  Each contains `0100=e2` and
`0001=f2`, but none contains `0101=e2+f2`; each spans
`<e1,e2,f2>` and has restricted symplectic rank two.

Every one of the 24 displayed gauge vectors was tested individually against
all 56 residuals.  The first 12 have rank 12; all 24 have rank 18.  The
independently enumerated defining-equation centralizers are exactly the three
`D_a` and three `U_d` above.  Since the translation space equals the
18-dimensional signature kernel, each of the three quotient points represents
one complete orbit of size `3^18`; their sum is all `3^19` rows.

## Later claimant-code inspection

Only after the clean-room formulas, mixed-word label, and independent checker
freeze, I opened the claimant checker read-only.  Its SHA-256 was the submitted
`8b33f11c261c78aad8f8d5e54d52b9aa7c7fb3a449301c283a49d26d57f4f969`.
I did not execute, import, patch, or copy it into the independent checker.  The
inspection found the same triple convention and confirmed that its span and
symplectic-rank calculations are diagnostics only: the literal union `Sigma`
itself is tested for subspace closure.  It contains no `p=2` branch, generated
power subgroup, factor system, cohomology enumeration, or finite-group
construction.  One methodological difference strengthened the replication:
the claimant code checks the nine displayed stabilizer matrices, whereas the
independent checker enumerates the complete centralizers from their defining
linear equations before recovering exactly those nine pairs.

## Verdict

`status/replicated` for exactly the frozen
`RANK4-H3-SHEAR-ORBIT-SUPPORT` family.

The finite certificate, transformation rules, factor-independent literal-cube
projection, three-orbit coverage, all 81 coset entries, and the common explicit
closure defect independently agree.  The route is exhausted before cohomology.

## Why this verdict

There are two separately written exact computations plus hand derivations of
the convention-sensitive steps.  The independent program reconstructed rather
than imported the affine matrix and derived rather than assumed the finite
centralizer.  Protocol caps this bounded computational family result at
`replicated`; it is not promoted to `proven` and does not answer the active
assignment.

## What is NOT established

No finite extension group is constructed.  Exact exponent nine, consistency of
any central factor system, and central cube coordinates are not computed.  No
other rank-four action, label pair, quotient, kernel, or odd prime is excluded.
The universal statement that every literal power-set subgroup is abelian
remains open.  `active_assignment_answered: no`.

## What would upgrade it

There is no scope-level upgrade from more checking of this family.  Progress on
the active assignment requires a genuinely different family yielding an exact
finite witness, or a universal proof covering every odd prime and admissible
group.
