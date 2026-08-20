---
title: "Triage — Kourovka 21.53 — fixed PSL(2,11) bounded equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claimant: Problem-21.53
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Triage — fixed `PSL(2,11)` bounded equality

## Claim restated

For the single involution conjugacy class `D` of `PSL(2,11)`, the complete
product-order colouring has 55 vertices and colours `2,3,5,6`, and its full
colour-preserving group equals `Aut_2(Gamma) intersect Aut_3(Gamma)`; both groups
have order 1320. This is a bounded `PARTIAL_RESULT`, not an answer to the universal
scope.

The routed artifact is a `REPORT`, not a `CLAIM` or `STALE_MATCH`; consequently the
claim-check JSON gate in the common protocol §5.1 does not apply.

## Locked scope

- Scope: `21.53/two-minimal-prime-colours`.
- Assignment revision: 2, matching the request and current canonical record.
- Exact active target: for every finite nonabelian simple group `L` and every
  involution class `D`, the full product-order-colour automorphism group equals
  `Aut_2(Gamma) intersect Aut_p(Gamma)`, where `p` is the second-smallest distinct
  prime divisor of `|L|`.
- Excluded: Problem 21.52; unions of involution classes; arbitrary choices of `p`;
  and presenting any bounded list of fixed pairs as the universal conclusion.

## Rendered-source clause matrix

The source PDF page 172 was read both with `pdftotext -layout` and as a rendered
PNG. Problem 21.53 explicitly inherits the notation of 21.52. The source's `G` in
21.53 is therefore the inherited finite nonabelian simple group called `L` in
21.52; the canonical revision-2 record preserves that interpretation.

| source clause | active? | fixed-pair report | universal remainder |
|---|---:|---|---|
| `Gamma` is complete on one involution class `D`, with colour determined exactly by `|ab|` | yes | pending reconstruction | every other admissible pair |
| `Aut_t(Gamma)` preserves every `t`-edge, for every positive integer `t` | yes | definition to be implemented literally, including vacuity | all labels/all pairs |
| `Aut(Gamma)=intersection_t Aut_t(Gamma)` | yes | full four-colour group to be computed | all pairs |
| `Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)` for the two minimal prime divisors | yes | pending for `PSL(2,11)`, allegedly `p=3` | universal quantifier wholly open |
| Problem 21.52 asks whether full colour automorphisms come from `Aut(L)` | no | not claimed | excluded scope |

`active_assignment_answered: pending` at triage; even a complete pass on this fixed
pair will force `active_assignment_answered: no`.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | candidate value / proof use | independent evidence planned | triage result |
|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility/quantifier | one fixed pair only | compare bounded claim with rendered universal source | **not answered universally** |
| `21.53-L-finite-nonabelian-simple` | admissibility | alleged `PSL(2,11)` | construct `SL(2,11)/{+-I}` exactly; direct order/noncommutativity; independently test simplicity in a faithful permutation model and invoke the standard `PSL(2,q)` simplicity theorem | pending |
| `21.53-D-single-involution-class` | admissibility | alleged unique class of all 55 involutions | exhaustive element-order and conjugation-orbit enumeration | pending |
| `21.53-Gamma-product-order-colouring` | admissibility/definition | all unordered distinct pairs in `D` | recompute all `binomial(55,2)=1485` products from exact quotient multiplication | pending |
| `21.53-Aut-t-definition` | admissibility/definition | preserve each specified relation as a set; nonoccurring labels impose no restriction | audit the implication and encode only occurring relation cells; state `S_D` for absent `t` | pending |
| `21.53-two-minimal-primes` | admissibility/parameter | alleged `|L|=660=2^2*3*5*11`, hence `p=3` | exact enumeration and integer factorization | pending |
| `21.53-full-colour-group-definition` | admissibility/definition | intersection for colours `2,3,5,6` | independently coloured incidence-graph automorphism computation | pending |
| `21.53-two-colours-determine-all` | target conclusion | equality for this fixed pair only | exact containment plus independently obtained group orders | pending fixed pair; universal conclusion open |

No admissibility row is inherited from claimant output.

## Target versus witness and provenance

- Source target: the universal class of pairs `(L,D)` in Problems 21.52–21.53.
- Reported witness: a quotient model `SL(2,11)/{+I,-I}` with canonical matrix-pair
  representatives, and its alleged complete involution class.
- Active assignment: the universal equality, revision 2.
- Status of witness identity: pending. The verification will independently build the
  quotient rather than read claimant matrix/code. By definition this quotient is
  `PSL(2,11)` once the centre is proved to be `{+-I}`; the exact enumerator and an
  independently generated faithful projective-line action will check the concrete
  object. The fixed witness is an instance of, not equal to, the universal target.
- Circularity risk: low but explicitly checked. The group will come from determinant-one
  matrices over the independently implemented field `F_11`; `D` will be found by
  exhaustive order and conjugacy computation, not selected from desired colours;
  graph relations will be derived from products, not imposed to force equality.

## Subclaims

1. The independently constructed quotient is exactly `PSL(2,11)`, has order 660,
   is nonabelian and simple.
2. It has exactly one involution conjugacy class, containing all 55 involutions.
3. The exact complete off-diagonal product-order matrix has 1485 entries, colours
   `2,3,5,6`, and the reported counts.
4. Since `660=2^2*3*5*11`, the prescribed second prime is `p=3`.
5. The every-positive-integer `Aut_t` convention is used, with absent labels giving
   `S_D` vacuously.
6. A separately designed incidence structure has automorphism group exactly
   `Aut_2 intersect Aut_3`; a second incidence structure has automorphism group
   exactly the full colour group.
7. Both groups have order 1320; the automatic containment of the full group in the
   two-colour group then proves fixed-pair equality.
8. None of these finite checks answers the universal assignment.

## Tool probe and methods inventory

Available: GAP 4.12.1, Python 3.12.3, dreadnaut (nauty), Poppler `pdftotext`
24.02.0 and `pdftoppm`. Sage and Magma are absent.

| subclaims | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1–5 | fresh bounded Python enumerator using only arithmetic mod 11 and canonical `+-I` quotient representatives | exact quotient size, multiplication facts, orders, conjugacy orbits, full pair matrix, hashes/indexing and prime choice | by itself, the general `PSL(2,q)` simplicity theorem or any universal statement |
| 1 | fresh GAP check fed an independently generated faithful permutation action on `P^1(F_11)` | order and computational simplicity/nonabelianness of that concrete action group | any larger family or equality of colour groups |
| 6–7 | fresh Python generator of vertex-coloured incidence graphs, followed by bounded dreadnaut runs | exact automorphism-group orders of the encoded two-relation and four-relation structures; encoding proof identifies them with the requested groups | no universal inference and no structural theorem for other pairs |
| 3, 6 | independent audit code checking every pair and every emitted incidence edge, plus SHA-256 hashes | absence of dropped/duplicated vertices or unordered pairs and reproducible indexing | correctness of software outside the audited finite semantics |

The graph encoding will have one distinguished cell for the 55 original vertices
and one cell per relation type for degree-2 incidence vertices. Hence a
colour-preserving incidence automorphism restricts faithfully and bijectively to a
permutation of `D` preserving precisely the encoded product-order relations.

## Hard limits and recommendation

The universal assertion cannot be verified by this bounded computation, and the
fixed example cannot be upgraded to a proof of it. No missing general-purpose tool
blocks the finite reconstruction. Freeze the exact checker commands and resource
bounds before running them; all are expected below the heavy-job threshold. Proceed
with full verification of the bounded report only, retaining
`active_assignment_answered: no` even on a pass.
