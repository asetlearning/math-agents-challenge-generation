---
title: "Problem 21.53 — exact bounded equality for the A7 involution class"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/conjectured
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: counterexample
strategy: A7-TWO-COLOUR-SEPARATOR
cycle_outcome: PARTIAL_RESULT
active_assignment_answered: no
state: awaiting_lead
---

# Exact bounded equality for the double-transposition class of A7

## Active target

Scope: `21.53/two-minimal-prime-colours`, assignment revision 2.

Universal target: for every finite nonabelian simple `L` and every single
involution class `D`, the full exact product-order colour group equals
`Aut_2(Gamma) intersect Aut_p(Gamma)`, where `p` is the second-smallest distinct
prime divisor of `|L|`.

## Bounded partial result

For `L=A_7` and its (unique) conjugacy class `D` of double transpositions,
`p=3`, the occurring product orders are exactly `2,3,4,5,6`, and

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma) = S_7^D`

with all three groups of order 5,040.  Thus this fixed pair is **not** a
counterexample.  This is one exact finite equality only; it does not establish
the source's universal assertion.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed-pair value / use | evidence | result |
|---|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | assertion ranges over every admissible `(L,D)` | only `(A_7,D)` is determined; an equality at one pair cannot settle the universal assertion | this note and run log | uncovered for source scope |
| `21.53-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `L=A_7`, order 2,520; `A_n` is nonabelian simple for `n>=5`; GAP also reports `IsSimpleGroup=true` | hand theorem; v4 stdout | pass |
| `21.53-D-single-involution-class` | admissibility | one conjugacy class, every element order 2 | parity forces every involution of `A_7` to have type `2^2 1^3`; that class does not split in `A_7`; exhaustive class/all-involution sets both have size 105 | hand derivation; Python inventory; v4 stdout | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | complete graph on `D`, exact colour `|ab|` | all 5,460 unordered distinct pairs were evaluated by exact permutation multiplication/order | both frozen checkers | pass |
| `21.53-Aut-t-definition` | admissibility | one-way preservation of each `t`-edge, vacuous if absent | every occurring relation is nonempty; for a permutation of the finite pair set, one-way preservation of `E_t` is setwise preservation; incidence gadgets encode the exact ordered relation partitions | hand finite-set argument; v4 checker | pass |
| `21.53-two-minimal-primes` | admissibility | `2,p` are the two smallest distinct divisors | `2520=2^3*3^2*5*7`, hence `p=3` | hand factorization; both checker outputs | pass |
| `21.53-full-colour-group-definition` | admissibility | preserve every occurring exact product-order colour | full gadget has separate edge-node classes for `2,3,4,5,6`; restriction kernel is trivial | v4 stdout and checker | pass |
| `21.53-two-colours-determine-all` | target conclusion | full group equals the 2/3 stabilizer | equality holds for this pair, so the conclusion is not violated; the universal conclusion remains unproved | v4 stdout; sandwich below | fixed-pair pass, source scope open |

## Exact object and colour inventory

The class is represented by `(1,2)(3,4)` in the natural degree-seven copy of
`A_7`.  Its size is

`7! / (2^2 * 2! * 3!) = 105`.

Regard each class element as a two-edge matching on seven points.  The union of
two distinct matchings has one of the following alternating component types:

| component type | product order |
|---|---:|
| common edge plus two disjoint residual edges, or an alternating 4-cycle | 2 |
| common edge plus meeting residual edges, or two `P_2` components | 3 |
| `P_3 + P_1` | 4 |
| `P_4` | 5 |
| `P_2 + P_1 + P_1` | 6 |

For each fixed vertex the respective valencies are `8,36,24,24,12`, yielding
the complete edge inventory

| order | edges |
|---:|---:|
| 2 | 420 |
| 3 | 1,890 |
| 4 | 1,260 |
| 5 | 1,260 |
| 6 | 630 |

The independent pure-Python inventory reconstructed all 5,040 permutations on
seven points, filtered the 2,520 even ones, identified the 105 nonidentity
involutions with the explicit matching model, checked the complete conjugacy
orbit, and evaluated all pairs.  Its upper-triangle product-order digest is
`4d3fe83103fe078db14711e68a7932fa2e30428ae5f69c08ef69bf812fdcfcfa`.

## Automorphism comparison and structural sandwich

The two-colour gadget has:

- 105 original vertices;
- one degree-two edge node for each of the 420 order-2 edges;
- one separately coloured degree-two edge node for each of the 1,890 order-3
  edges.

Its order is 2,415.  Preserving its ordered vertex-colour partition is exactly
preserving `E_2` and `E_3` separately.  Every edge node has a unique two-vertex
neighbourhood, so restriction to the 105 original vertices is faithful.  GRAPE
4.9.0/nauty returns group order 5,040.  Each of its six returned generators was
then audited directly against all 420 order-2 edges and all 1,890 order-3 edges,
with zero failures.

The analogous full gadget has 5,565 vertices and five separate edge-node colour
classes.  It also returns a faithful group of order 5,040; all seven returned
generators preserve all 5,460 matrix entries.

There is also a transparent sandwich.  Conjugation by `S_7` normalizes `A_7`,
permutes its double transpositions, and preserves every product order, so its
faithful order-5,040 action `S_7^D` lies in the full colour group.  Hence

`S_7^D <= Aut(Gamma) <= Aut_2(Gamma) intersection Aut_3(Gamma)`.

The computed rightmost group has order 5,040, forcing equality throughout.  The
separate full-gadget computation independently agrees with this sandwich.

## Reproducible evidence

- Run log: `Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/log.md`
- Pure-Python inventory: `a7_inventory.py`, SHA-256
  `3974349af9ac2edbb1c73f4ac3ab034d39d92762931f2010fa2df03109c392bb`
- Frozen v4 GAP checker: `a7_two_colour_gap.g`, SHA-256
  `ccd5087fe6d4bf47d624800e61bd8c2e0dd28ae94eae6a6521eddbc8fc08ff39`
- Frozen manifest: `compute-manifest.md`, SHA-256
  `1cf891e9debdaa90f99ce8396afeaaac3b33823ff7fc3bb4a31e1215a1f35c1d`
- Accepted stdout: `a7_two_colour_gap_v4.stdout.txt`, SHA-256
  `9c9acecd3f65a450af9868867ca19086b77bafc26c215b55dbdd77b58b2a444d`
- Empty stderr: SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Resource record: SHA-256
  `4c724a56b63a03ca7a9d39d21c9a82d2e61d8e690a4d153da5dba0655cc0a300`

The accepted invocation used GAP 4.12.1 and GRAPE 4.9.0, exited zero after
12.62 wall seconds, used 142,336 KiB maximum RSS, had empty stderr, and ended in
the exact frozen success sentinel.

## What this does not establish

- It does not prove the equality for any `L` other than `A_7` or for the
  universal all-simple-groups scope.
- It supplies no separating permutation and therefore no counterexample.
- It makes no assertion about Problem 21.52 or whether every full colour
  automorphism is induced by an automorphism of `A_7`.
- It does not replace `p=3` by an arbitrary prime and does not use a union of
  involution classes.
- The first v3 GAP attempt is a recorded failed run and supplies no mathematical
  evidence; only the separately leased, fail-fast v4 output is used.

## How this could be wrong

1. The incidence gadget might fail to model the one-way source definition.  The
   finite-set injection argument and unique-neighbourhood restriction justify
   the equivalence, but Validator should reconstruct it independently.
2. GRAPE/nauty or the GAP action restriction could be faulty.  Direct generator
   audits, the natural `S_7` lower bound, and the independent Python inventory
   reduce but do not eliminate that software risk.
3. The class might be misidentified.  The parity/cycle-type hand argument and
   the independent exhaustive all-involution equality both address this.
4. Equality for this highly symmetric pair could be overread as universal.  It
   is explicitly only one bounded fixed-pair result and leaves
   `active_assignment_answered: no`.
