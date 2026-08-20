---
title: "Fixed PSU(3,3) full product-order colouring — bounded equality"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Fixed PSU(3,3) full-colour equality

## Active target

Scope: `21.52/involution-class-product-order-colouring`

Assignment revision: 1

Target statement: For every finite nonabelian simple group L and every conjugacy class D of involutions in L, every permutation of D preserving the order |ab| for each pair of distinct vertices a,b is induced on D by an automorphism of L that stabilizes D setwise.

## Outcome

`PARTIAL_RESULT`: for the exact fixed pair consisting of `L = PSU(3,3)` and its unique conjugacy class `D` of 63 involutions, the full product-order colour-preserving permutation group on `D` and the restriction image of `Aut(L)` are equal, both of order 12,096.

This excludes this fixed pair as a counterexample. It does not answer the universal scope.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed-pair value / computation | evidence | result |
|---|---|---|---|---|---|
| 21.52-forall-L-D | admissibility | universal assertion over every admissible pair | exactly one pair `(PSU(3,3),D)` was tested | frozen manifest and output | bounded only; universal row unanswered |
| 21.52-L-finite-nonabelian-simple | admissibility | L finite nonabelian simple | `PrimitiveGroup(28,4)` has order 6048, is nonabelian/simple, and is exactly isomorphic to the separate `PSU(3,3)` constructor | checks at output lines 5–16 | pass |
| 21.52-D-single-involution-class | admissibility | D one conjugacy class, all elements order 2 | all 14 conjugacy classes inventoried; exactly one involution class, size 63, centralizer order 96 | output lines 17–39 | pass |
| 21.52-Gamma-complete-on-D | admissibility | every unordered pair of distinct D-elements | all `binomial(63,2)=1953` pairs enumerated | output lines 43–52; matrix artifact | pass |
| 21.52-edge-colour-exact-product-order | admissibility | edge colour exactly `Order(a*b)` | exact 63×63 product-order matrix; colours 2,3,4 with counts 189,1008,756 | matrix and output lines 40–47 | pass |
| 21.52-tau-preserves-all-edge-colours | admissibility | every reported colour-group generator preserves all pair colours | exhaustive 1953-pair check passed for every colour-group generator | output line 81 | pass |
| 21.52-tau-induced-by-AutL | target conclusion | every colour automorphism lies in the Aut(L) restriction image | full colour group and restriction image are equal of order 12096 | output lines 55–102; certificate generators | not violated; equality for this fixed pair |

## Exact object and identity

The computation used GAP 4.12.1's installed primitive-library object `PrimitiveGroup(28,4)`. GAP reported structure `PSU(3,3)`, order 6048, nonabelian, simple, and centreless. An exact `IsomorphismGroups` call against the separately constructed matrix/projective group `PSU(3,3)` returned a non-fail isomorphism.

AtlasRep's optional representation fetch returned `fail`; no identity claim rests on it. The installed primitive-library object and separate projective-unitary constructor were used instead.

The complete conjugacy-class inventory `(representative order, class size, centralizer order)` was:

```text
(1,1,6048), (2,63,96), (3,56,108), (4,63,96), (4,63,96),
(6,504,12), (12,504,12), (12,504,12), (7,864,7), (7,864,7),
(3,672,9), (8,756,8), (8,756,8), (4,378,16).
```

Thus there is exactly one involution class, and it has 63 elements.

## Complete colouring

For the sorted 63-element class `D`, the checker computed `Order(D[i]*D[j])` for every ordered matrix entry and every unordered edge. The complete graph's 1953 edges split as:

| product order | edge count |
|---:|---:|
| 2 | 189 |
| 3 | 1008 |
| 4 | 756 |

The exact 63×63 matrix is `scratch/psu33-colour-matrix.g`, SHA-256 `59ef40bb4d41015243a77914badfd8e851c2a6fc0a09d451b7fa0f5312b5b287`.

## Why the computed graph group is the full colour group

The checker formed a simple incidence graph with 2016 vertices: 63 original vertices and one new vertex for each of the 1953 unordered pairs. Every pair-vertex is adjacent precisely to its two endpoints. Vertex colour classes distinguish the 63 original vertices and partition pair-vertices by the exact product order 2, 3, or 4.

A colour-preserving permutation of `D` extends uniquely to this incidence graph by mapping each pair-vertex to the vertex of the image pair. Conversely, any automorphism preserving the vertex colour classes restricts to a permutation of `D` preserving every product-order colour. The computed incidence action had trivial kernel on the original 63 vertices. Therefore the nauty/GRAPE group restricted to `D` is exactly the full colour group, not merely a known subgroup. Its order is 12,096.

## Restriction image of Aut(L)

The checker computed GAP's full exact `AutomorphismGroup(L)`, of order 12,096. Since `D` is the unique involution class, its setwise stabilizer is all of `Aut(L)`; this was also checked on every automorphism-group generator. Restricting those generators to `D` gives an image of order 12,096. Every image generator passed the exhaustive 1953-edge colour check and lies in the full colour group. Equal finite orders then give equality.

Explicit generators for both permutation groups are saved in `scratch/psu33-full-colour-certificate.g`, SHA-256 `097452a47e77d62d984b556e5afda7754b63d4a90356f5f7141d5db3ef925976`.

## Frozen run and acceptance evidence

The sole Lead-leased command was:

```text
bash Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_run.sh
```

Frozen input hashes:

- checker: `86e2633dff9c8f5ec25c3ee7beb5ce21b8e2e3a957e26f550874b3e154843208`;
- runner: `fc2fccac609c076e15d6168110e2f69f6340893e9b0d9c2e03d91970eee572e0`;
- manifest: `338d83d91f5847e9758cf15336ce383b5db5ecb5be84b3d1ba9180e43cd8fb8a`.

Observed acceptance evidence:

- wrapper exit: 0; terminal wrapper output: `RUNNER_ACCEPTED_PSU33_FULL_COLOUR_CHECKER`;
- 26/26 named GAP checks passed; no `=FAIL` or error text;
- stderr empty; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- exact `PSU33_FULL_COLOUR_CHECKER_SUCCESS` sentinel is terminal in both stdout and GAP log;
- elapsed wall time 2.59 seconds; user CPU 2.02 seconds; max RSS 142,208 KiB; no swaps; exit 0;
- stdout/GAP-log SHA-256 `053658d829015e9a0addb12eedc363ba43e1d35653041755de7c8ac1ea8c7238`;
- resource-report SHA-256 `193e9df39e6630abbd68b12d6f5546369cb2bd99640d49d9c0cba97e65930aba`.

## What this does not establish

- It does not prove the universal assertion in Problem 21.52.
- It does not produce a colour-preserving permutation outside the automorphism restriction image; strict containment is false for this pair.
- It does not cover another involution class or another finite simple group.
- It is a single exact computational determination awaiting independent reconstruction, not certification.

## How this could be wrong

1. A defect in GAP's primitive-group or `PSU` constructors could undermine the object identification, though two independent constructors and an exact isomorphism check reduce this risk.
2. A defect in GAP's `AutomorphismGroup` or GRAPE/nauty could give a wrong group. Validator should reconstruct at least one side independently or rerun in a separate implementation.
3. An incidence-encoding error could admit or omit permutations. The explicit bijection argument above, the trivial-kernel check, and exhaustive pair checks address but do not independently certify the implementation.
4. The ordering of `D` is implementation-specific. The saved matrix and both explicit generator sets must be treated together; changing the ordering requires recomputation or conjugation of the permutation representations.

## Honest scope status

`active_assignment_answered: no`. The named fixed-target strategy `PSU33-FULL-COLOUR-AUTOMORPHISM` is exhausted by equality. The counterexample direction remains subject to Lead's next decision; this agent does not self-park or select another target.
