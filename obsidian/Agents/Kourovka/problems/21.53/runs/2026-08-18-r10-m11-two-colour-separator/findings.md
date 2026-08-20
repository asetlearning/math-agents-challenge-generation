---
title: "Bounded partial result — exact two-colour equality for M11"
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
strategy: M11-TWO-COLOUR-SEPARATOR
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Fixed-M11 bounded equality

## Active target

Scope: `21.53/two-minimal-prime-colours`, assignment revision 2.

The universal target asks whether, for every finite nonabelian simple `L` and
every single involution class `D`, the full exact product-order colour group is
`Aut_2(Gamma) intersection Aut_p(Gamma)`, where `p` is the second-smallest
distinct prime divisor of `|L|`.

## Partial result

For the explicit Mathieu group `M11` in its standard degree-11 permutation
model and its unique 165-element involution class `D`, the exact product-order
colours are `2,3,4,5,6`, and

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma)`.

Both groups have order 7,920 and equal the natural conjugation action on `D`.
Thus this fixed target supplies no separating permutation. This is one bounded
negative counterexample search result, not a universal conclusion.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed-pair use / evidence | result |
|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | universal over all admissible `(L,D)` | exactly one admissible pair is determined; no inference to other pairs | fixed-pair only |
| `21.53-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | explicit generators; computed order 7920, finite `true`, abelian `false`, simple `true`, finite-simple type `M11`, sharply 4-transitive degree-11 action | pass |
| `21.53-D-single-involution-class` | admissibility | one full conjugacy class of order-2 elements | all ten classes and all elements checked; exactly one involution class, size 165, centralizer order 48 | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | complete graph on `D`, colour exactly `|ab|` | all 13,530 unordered distinct pairs evaluated; complete matrix printed in accepted stdout | pass |
| `21.53-Aut-t-definition` | admissibility | preserve each exact `t`-edge one-way, absent labels vacuous | separately coloured incidence nodes encode exact relation stabilizers; every returned generator exhaustively audited | pass |
| `21.53-two-minimal-primes` | admissibility | `2` and second-smallest distinct divisor `p` | `7920=2^4*3^2*5*11`; printed prime list `[2,3,5,11]`, so `p=3` | pass |
| `21.53-full-colour-group-definition` | admissibility | intersection over every occurring exact colour | full incidence graph has a distinct vertex-colour cell for each of `2,3,4,5,6`; all-generator audit has zero failures | pass |
| `21.53-two-colours-determine-all` | target conclusion | full group equals the order-2/order-3 group | both restricted groups have order 7920 and explicit mutual containment | satisfied for this pair; universal unresolved |

No row violates the target conclusion, so this is not a counterexample and no
claim-check JSON is created.

## Exact object and identification

The checker constructs

`L = < (1,2,3,4,5,6,7,8,9,10,11), (3,7,11,8)(4,10,5,6) >`.

These are exactly GAP's installed standard `MathieuGroup(11)` generators. The
accepted run independently computes `|L|=7920`, nonabelian simplicity,
finite-simple short name `M11`, moved-point domain of size 11, and an orbit of
size `11*10*9*8=7920` on ordered distinct four-tuples. This identifies the
standard sharply 4-transitive degree-11 Mathieu model rather than relying only
on a library label.

The accepted run inventories all elements and conjugacy classes. There is one
involution class, represented in the sorted list by
`(4,10)(5,8)(6,7)(9,11)`, of size 165; its centralizer has order 48. The sorted
class equals the complete set of nonidentity elements of order 2.

## Exact colour inventory and tautology gate

For all `165 choose 2 = 13,530` unordered pairs, the output is:

| product order | edge count | valency |
|---:|---:|---:|
| 2 | 990 | 12 |
| 3 | 2,640 | 32 |
| 4 | 1,980 | 24 |
| 5 | 3,960 | 48 |
| 6 | 3,960 | 48 |

The counts sum to 13,530 and the valencies sum to 164. The checker checks each
relation has the displayed common valency at every vertex. Since colours 4, 5,
and 6 occur, preserving only colours 2 and 3 is not tautologically equivalent to
preserving all colours; the tautology gate prints `PASS_OTHER_COLOURS_OCCUR`.

## Exact automorphism comparison

For selected relations, the checker uses a bipartite incidence graph whose
original 165 vertices form one colour cell and whose incidence vertices for
order-2 and order-3 edges form separate colour cells. An automorphism preserving
these cells restricts exactly to a permutation of `D` preserving both selected
relations, and every such permutation lifts uniquely by sending each incidence
vertex to the incidence vertex on its image pair. Uniqueness of each two-point
neighbourhood makes restriction faithful.

The two-colour incidence graph has 3,795 vertices and 7,260 edges. Its exact
automorphism group restricts faithfully to order 7,920 on `D`; all four returned
generators preserve all 990 order-2 edges and all 2,640 order-3 edges with zero
failures.

The full graph uses a separate incidence-vertex colour cell for every occurring
product order. It has 13,695 vertices and 27,060 edges. Its exact automorphism
group also restricts faithfully to order 7,920; all four returned generators
preserve all 13,530 exact colours with zero failures.

The checker separately checks both containments between the restricted groups.
It also constructs the natural conjugation action of `M11` on `D`, computes its
order as 7,920, and checks that it lies in the full-colour group. Hence the accepted
data give the sandwich

`M11(conjugation) <= Aut(Gamma) <= Aut_2(Gamma) intersect Aut_3(Gamma)`,

with all three orders 7,920. This is an exact equality certificate for this fixed
pair within the explicit permutation model.

## Reproducible evidence

- Frozen checker:
  `Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11_two_colour_gap_v3.g`,
  SHA-256 `f5da7d297c349c7a1709fd5e5cebf7fca7a1ba2407997ead1697298c7b576f28`.
- Frozen manifest:
  `Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11-compute-manifest-v3.md`,
  SHA-256 `876f34f3439566ddae815887e7c9df7d7b586ff92c5e1eced475d1f1ca583aa3`.
- Accepted stdout (includes the sorted 165 vertices and complete 165-row matrix):
  `Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11_two_colour_gap_v3.stdout.txt`,
  66,445 bytes, SHA-256
  `7d6f5778c49232bd608dde20b52e2e33627d2e2bb95cfaed05996fe61c9e4e41`.
- Empty stderr: SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Resource record:
  `Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11_two_colour_gap_v3.resource.txt`,
  SHA-256 `bf1d1f6487461a0cdf3a9eb4390c4eb9c03bfb96c3a87adf65ea94150a438669`.

The sole v3 invocation used GAP 4.12.1 and GRAPE 4.9.0, exited zero, took 7.64
seconds wall time, and used 142,208 KiB maximum RSS. The empty-stderr and unique-
terminal-sentinel gates pass. Versions 1 and 2 are retained as explicitly
non-evidentiary failed runs and are not used for this result.

## What this establishes

- Exact group, class, prime, and all-colour inventory for the fixed pair.
- Exact non-tautological equality of the two relevant permutation groups for
  that pair.
- Therefore no permutation separator exists for this fixed M11 target.

## What this does not establish

- It does not prove the universal statement for other simple groups or classes.
- It does not produce a counterexample.
- It does not address Problem 21.52, unions of classes, or arbitrary choices of
  primes.
- It does not permit any inference from this bounded equality to the universal
  source question.
- It remains `status/conjectured` pending independent Validator reconstruction.

## How this could be wrong

1. A flaw in the incidence encoding could make the computed graph group differ
   from an exact relation stabilizer; the unique-two-neighbour lift argument and
   independent generator audits are intended to expose this.
2. A restriction kernel on incidence vertices could inflate a raw group order;
   the checker compares raw and restricted orders and requires equality.
3. A class or group identification error could put the computation outside the
   source scope; explicit generators, all-elements enumeration, simplicity,
   finite-simple-type, and conjugacy-orbit gates address this.
4. A GAP/GRAPE or implementation defect could survive the self-audits. A fresh
   Validator should reconstruct the group and relation stabilizers independently,
   preferably without reusing this script.
