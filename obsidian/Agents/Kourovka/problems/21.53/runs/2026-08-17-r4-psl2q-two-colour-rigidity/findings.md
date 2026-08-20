---
title: "Claim under review — even-characteristic PSL(2,q) two-colour rigidity"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
claim_id: 21.53-psl2-even-r2-partial-001
claim_scope: bounded_partial
active_assignment_answered: false
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/conjectured]
---

# Even-characteristic `PSL(2,q)` claim under review

## Active target

Scope: `21.53/two-minimal-prime-colours`

Assignment revision: 2

Target statement: For every finite nonabelian simple group `L` and every
conjugacy class `D` of involutions in `L`, if `Gamma` is the complete
product-order-coloured graph on `D` and `p` is the second-smallest distinct prime
divisor of `|L|`, then
`Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)`.

## The claim

For every `q=2^f` with `f>=2`, and for the complete involution class `D` of the
simple group `PSL(2,q)`,

`Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)=PGammaL(2,q)`.

The identical abstract pair at `q=5`, namely the unique involution class of
`PSL(2,5) isomorphic to PSL(2,4) isomorphic to A5`, is covered by the `q=4`
instance. This is an infinite-family partial theorem, not the universal target.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | Universal quantifier over all admissible pairs | The submitted claim explicitly specializes to all `PSL(2,2^f)`, `f>=2`, plus the identical `A5` pair represented by `q=5`; it does not discharge the canonical universal quantifier. | `partial-result.md`, Exact scope | pass for bounded-claim gate; canonical result unknown |
| `21.53-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `PSL(2,2^f)` is simple for `f>=2`; the `q=5` transfer is the same simple group `A5` as `q=4`. | `partial-result.md`, §§2--3 | pass |
| `21.53-D-single-involution-class` | admissibility | `D` one complete involution class | The nilpotent-vector model gives all `q^2-1` involutions and proves transitivity; `A5` has the identical unique class. | `partial-result.md`, §§2--3 | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | Complete graph coloured exactly by product order | Every distinct pair is assigned determinant `delta`, with product characteristic polynomial `T^2+delta^2T+1`; this determines its exact order. | `partial-result.md`, §2 | pass |
| `21.53-Aut-t-definition` | admissibility | Literal preservation of each `t`-edge, with absent-label vacuity | Dependence is exactly colour 2, determinant one exactly colour 3, and every absent positive label gives `Aut_t=S_D` vacuously. | `partial-result.md`, §2 | pass |
| `21.53-two-minimal-primes` | admissibility | `p` is the least prime divisor above 2 | The exact order formula proves divisibility by 2 and 3, hence `p=3`. | `partial-result.md`, §1 | pass |
| `21.53-full-colour-group-definition` | admissibility | Full group preserves every occurring product-order colour | The trace/determinant formula is applied to all pair colours, not only 2 and 3. | `partial-result.md`, §2 | pass |
| `21.53-two-colours-determine-all` | target_conclusion | Full colour group equals the 2/3 intersection | The functional-equation argument determines the intersection as `GammaSL(2,q)`, and the trace formula proves it preserves every colour. | `partial-result.md`, §2 | proved for bounded claim only; canonical result not proved |

## What I computed in

The theorem is a hand derivation in the exact matrix group
`SL(2,F_q)=PSL(2,F_q)` for every `q=2^f`, `f>=2`. No finite computation is used
as proof. The separately leased GAP/GRAPE run concerns only `q=27` and is not
evidence for this claim.

## Is that object the target?

It is a strict infinite subfamily of the canonical target. The proof establishes
the conclusion for every even-characteristic simple `PSL(2,q)` and the identical
`q=5`/`A5` pair, but not for general odd `q` and not for finite simple groups
outside `PSL(2,q)`. Therefore `active_assignment_answered:false`.

## Argument / evidence

The complete proof is in
`Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/partial-result.md`.
It constructs every involution as `u_x=I+x(x^TJ)`, derives
`tr(u_xu_y)=det(x,y)^2`, and proves by a coordinate functional equation that every
permutation preserving dependence and determinant one is semilinear of determinant
one. Field automorphisms preserve element orders, completing the bounded equality.

The mandatory mechanical matrix is
`Agents/Kourovka/problems/21.53/claim-checks/21.53-psl2-even-r2-partial-001.json`.

## What this does NOT establish

- The odd-characteristic shell-rigidity lemma is not proved.
- The `q=27` equality of computed automorphism-group orders is one finite stress
  test only; it is not promoted to an odd-family theorem.
- No claim is made for simple groups outside `PSL(2,q)`.
- The universal revision-2 target remains unanswered.
- Problem 21.52's separate induction question is excluded.

## How I could be wrong

- The parameterization might omit or duplicate characteristic-two involutions.
- The one-way source implication for `Aut_t` might have been used as an equivalence
  without the required finite-bijection argument.
- The functional equation might implicitly use a zero vector or a diagonal pair,
  neither of which is a graph edge.
- The determinant trace could determine a characteristic polynomial without
  determining projective element order in a repeated-root case.
- The `q=5` transfer would fail if the group or chosen involution class differed
  from the `q=4` abstract pair.

Each issue is addressed explicitly in the linked proof and remains a required
Validator audit point.
