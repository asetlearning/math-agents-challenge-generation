---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/graph-automorphisms
  - project/kourovka
  - status/replicated
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: PARTIAL_RESULT
---

# Bounded A6 equality for Problem 21.53

## Active target

Scope: `21.53/two-minimal-prime-colours`, revision 2. The universal question asks whether the full product-order colouring on every involution class of every finite non-abelian simple group is determined by the colours 2 and the second-smallest prime.

## Bounded claim

For `L=A6` and its unique involution class `D=2A` of 45 double transpositions, `p=3` and

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma)`;

both finite permutation groups in this equality have order 1440. This is a claim about one pair only, not the universal target.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | bounded instance / evidence | result |
|---|---|---|---|---|
| 21.53-forall-L-D | admissibility | universal pair quantifier | only `(A6,2A)` is determined | universal row not answered |
| 21.53-L-finite-nonabelian-simple | admissibility | finite non-abelian simple `L` | `A6`, order 360 | pass for bounded instance |
| 21.53-D-single-involution-class | admissibility | one involution conjugacy class | exact 45-element `A6` conjugation orbit | pass |
| 21.53-Gamma-product-order-colouring | admissibility | complete product-order-coloured graph | complete 45-by-45 matrix, SHA-256 `e16df34378e87aa57e4bac7b6094eab1507b27e66fe36e7939ba9fb26d8f2932` | pass |
| 21.53-Aut-t-definition | admissibility | exact `t`-edge preservation | vertex-coloured incidence encodings with one auxiliary vertex per edge | pass |
| 21.53-two-minimal-primes | admissibility | 2 and second-smallest prime | `360=2^3*3^2*5`, so `p=3` | pass |
| 21.53-full-colour-group-definition | admissibility | preserve all occurring colours | four separate auxiliary cells for colours 2,3,4,5 | pass |
| 21.53-two-colours-determine-all | target conclusion | equality of full and 2/3 groups | both nauty group orders are 1440 and full is contained in 2/3 | holds for bounded instance |

## What was computed in

The script enumerates `A6` literally as the 360 even permutations of `[1..6]` and `D` literally as all 45 permutations of cycle type `2^2 1^2`. It checks that `D` is one conjugacy orbit and computes the order of every product for all unordered pairs. The occurring colours are 2,3,4,5, with vertex degrees 4,16,8,16 and edge counts 90,360,180,360.

The two-colour group is represented by a 495-vertex graph: 45 original vertices, one uniquely attached auxiliary vertex for each 2-edge, and one for each 3-edge, with the three types fixed as partition cells. The full group uses the analogous 1035-vertex graph with separate auxiliary cells for all four colours. Restriction to original vertices is an isomorphism from each augmented graph automorphism group to the intended relation automorphism group.

Dreadnaut/nauty 2.8.8 reports group order 1440 for both encodings. Since every full-colour automorphism preserves colours 2 and 3, the full group is a subgroup of the two-colour group; equality of orders gives equality of groups.

## Structural explanation

Identify a double transposition `(ab)(cd)` with the flag consisting of its fixed duad `ef` and the syntheme `{ab,cd,ef}`. Two distinct vertices have product order 2 exactly when their flags share a duad or share a syntheme. Hence the 2-colour graph is the line graph of the 15-duad/15-syntheme incidence graph. Its maximal triangles recover that connected bipartite graph. A part-preserving incidence automorphism acts on the duad disjointness graph; its six maximum independent 5-sets recover the six underlying points, so there are at most 720 such automorphisms and at most 1440 after allowing a part swap. This explains the exact order. A second conceptual lower bound is supplied by the standard model `A6 isomorphic to PSL(2,9)`, whose projective semilinear automorphisms have order 1440 and preserve product orders on the unique involution class; Validator should check those standard identifications independently.

## Reproducibility

- Frozen generator: `scratch/build_a6_instance.py`, SHA-256 `b23f6a8e09f6ff8a4957484eec3de527664ab9556a9a5e682f7603397746195a`.
- Frozen parameters: `scratch/a6-parameters.json`, SHA-256 `e0b6ecf6752967c10a2d04009ce044ca3b0b5c89d36d04a3b4f6e5a893e966c5`.
- Frozen wrapper: `scratch/run_a6_exact.sh`, SHA-256 `61d85e072dc93ef60b60f63a1b508308438d030407d9c7380f12f73d1ecf2a6e`.
- Build summary and all output hashes: `scratch/output/a6_build_summary.json` and `scratch/output/all-output-sha256.txt`.
- Exact nauty outputs: `scratch/output/a6_two_colour.nauty.out` and `scratch/output/a6_full_colour.nauty.out`; both stderr files are empty.

## What this does not establish

It gives no counterexample and no universal proof. Equality for one finite pair cannot be extrapolated to any other simple group or involution class. The computation has one implementation lineage (the hand degree count agrees with it, while the structural model explains the group size); Validator still needs an independent reconstruction before assigning any status above conjectured.

Verified by [[Agents/Kourovka/problems/21.53/verification/2026-08-17T191934Z-a6-bounded-equality.md]].
