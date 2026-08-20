---
title: "Triage — Kourovka 21.53 — odd square branch"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claimant: Problem-21.53-Proof
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/draft]
---

# Triage — odd `PSL(2,q)` square branch

## Claim, restated

For every odd prime power `q>=9` with `q=1 mod 4`, if `L=PSL(2,q)` and
`D` is its unique involution class, then the permutations of `D` preserving
the exact product-order-2 and product-order-3 edge relations form
`PGammaO(3,q)` and preserve every product-order colour.  Consequently
`Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)` for precisely this family.

This is an infinite-family `PARTIAL_RESULT`, not an answer to the universal
active assignment.

## Scope lock

- `scope_id`: `21.53/two-minimal-prime-colours`
- `assignment_revision`: `2`
- Exact active target: the two-minimal-prime equality for every finite
  nonabelian simple `L` and every involution conjugacy class `D`.
- Excluded: Problem 21.52; unions of involution classes; replacing the
  second-smallest prime by an arbitrary prime; and bounded-list evidence
  presented as a universal conclusion.
- The assigned clean-room boundary permits the canonical source record, the
  submitted run artifacts, and the claimant's `REQUEST`/`REPORT`; no prior
  verification or solution-bearing history is being used.

## Clause matrix

| source clause | active target | bounded claim | triage result |
|---|---|---|---|
| inherited notation: one involution class of a finite nonabelian simple group, complete graph coloured by exact product order | universal in `(L,D)` | `L=PSL(2,q)`, its unique involution class, `q>=9`, `q=1 mod 4` | pending verification for this subfamily only |
| `Aut_t` preserves every edge of exact label `t`, with the vacuous convention | all positive integers `t` | uses the exact `t=2,3` relations; neither is asserted empty in this branch | pending |
| full colour group is the intersection over all occurring labels | yes | intended to follow from the trace parameter and semilinear orthogonal action | pending |
| `Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)` for the second-smallest prime `p` | universal | claims the equality only for this `PSL(2,q)` family, with `p=3` | `active_assignment_answered: pending` (cannot become `yes` from this claim) |

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | bounded proof use | triage result |
|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | every admissible `(L,D)` | only the displayed infinite `PSL(2,q)` subfamily | fails as a universal-answer row; legitimate partial-result restriction |
| `21.53-L-finite-nonabelian-simple` | admissibility | finite nonabelian simple `L` | simplicity of `PSL(2,q)` for `q>=9` | pending hand check |
| `21.53-D-single-involution-class` | admissibility | one class of elements of order 2 | uniqueness and the trace-zero shell model | pending hand check |
| `21.53-Gamma-product-order-colouring` | admissibility | complete graph, exact colour `|ab|` | trace-squared parameter must determine the exact projective order | pending hand check |
| `21.53-Aut-t-definition` | admissibility | exact edge-label stabilizers | identify `R_2` and `R_3`, including characteristic 3 and distinct-vertex issues | pending hand check |
| `21.53-two-minimal-primes` | admissibility | `p` is the least divisor greater than 2 | show `3` divides `|PSL(2,q)|` | pending hand check |
| `21.53-full-colour-group-definition` | admissibility | intersection of every occurring colour stabilizer | compare the two-relation group with the full colour group | pending hand check |
| `21.53-two-colours-determine-all` | target conclusion | universal equality | asserted only on the displayed subfamily | pending for the subfamily; unproved universally |

## Target versus proof model

- Source target object: every admissible pair `(L,D)` in revision 2.
- Bounded target object: the unique involution class in `PSL(2,q)` for odd
  `q>=9`, `q=1 mod 4`.
- Proof model: the square-class shell in the projective trace-zero space
  `P(sl_2(q))`, with `Q=-det`, its polar form, and the two equations for
  product orders 2 and 3.
- `proof model = bounded target`: pending an explicit algebraic identification.
- `bounded target = universal source target`: false; it is a proper subfamily.
- There is no computed witness and hence no computation-proven object equality.

## Subclaims

1. `PSL(2,q)` is admissible, has one involution class, `p=3`, and that class
   is exactly the asserted projective quadratic shell.
2. The invariant `u=B(x,y)^2/(Q(x)Q(y))` identifies exact order-2 and
   order-3 products, including the unipotent characteristic-3 case, and
   controls all remaining product orders.
3. The sign in `c_22` and every exceptional case in `m_23` are correct.
4. The two given relations canonically define `u=4` tangent-sharing, with a
   separate valid construction in characteristic 3.
5. Exterior points are canonically tangent pairs, and tangent-sharing is the
   triangular graph on the conic points.
6. For `q>=9`, including `q=9`, its maximum cliques recover exactly the stars.
7. Orthogonality of tangent intersections is exactly harmonic cross-ratio.
8. A harmonicity-preserving conic permutation is semilinear fractional,
   including all coincident/omitted values in the additive and multiplicative
   reconstruction.
9. The resulting permutation group is exactly `PGammaO(3,q)`, and this group
   preserves every exact product-order colour.
10. No step reaches `q=3 mod 4`, another simple-group family, or the universal
    source quantifier.

## Tools available

- GAP `4.12.1`: available, not used for mathematical computation.
- Python `3.12.3`: available, not used for mathematical computation.
- Sage: unavailable.
- Magma: unavailable.
- The submission is proof-shaped.  The assigned validation is hand-only; no
  independent script, frozen manifest, or Lead compute lease exists.

## Methods inventory and limits

| subclaim | authorised method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1--2 | direct `2x2` matrix algebra and finite-field order analysis | target/model fidelity and exact relation dictionary for the bounded family | any non-`PSL(2,q)` case |
| 3--4 | hand Gram-determinant and binary-quadratic-form reconstruction | the claimed intersection numbers and canonical tangent relation | uniqueness of any structure in the `q=3 mod 4` branch |
| 5--6 | elementary conic incidence and classification of pairwise-intersecting 2-subsets | canonical recovery of the conic in this branch | a projective-plane completion outside this branch |
| 7--8 | explicit conic coordinates and line-by-line harmonic field reconstruction | `pi in PGammaL(2,q)` if every exceptional value is covered | the fundamental theorem for a relation other than harmonicity |
| 9 | symmetric-square/conic-stabilizer identification plus the trace parameter | exact two-colour and full-colour groups on the bounded class | the universal Problem 21.53 assertion |
| 10 | mechanical scope comparison | exact limitations and `active_assignment_answered:no` | mathematical progress on excluded cases |

No computational result can be claimed or upgraded in this review.  A hand-proof
pass may support the bounded partial theorem only.  The absence of Sage/Magma is
not a blocker because the proof is elementary and computation is neither needed
nor authorised.

## Recommendation

Proceed to full line-by-line hand verification of the bounded partial theorem.
Regardless of the mathematical outcome, retain
`active_assignment_answered:no` for revision 2.
