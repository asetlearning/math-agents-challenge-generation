---
title: "Triage — Kourovka 21.52 — fixed-A5 equality"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
claim: "For L=A5 and its unique conjugacy class D of 15 involutions, the product-order colour-automorphism group equals the restriction image of Aut(A5), and both groups have order 120."
claimant: Problem-21.52
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/conjectured]
---

# Triage — Kourovka 21.52 — fixed-A5 equality

## Scope lock

- Canonical scope: `21.52/involution-class-product-order-colouring`, revision 1.
- Active target: the assertion for **every** finite nonabelian simple `L` and every single involution conjugacy class `D` in `L`.
- Excluded here: Problem 21.53, unions of involution classes, uncoloured automorphisms, conjugacy-class colouring, and any inference from a bounded list to the universal assertion.
- The routed artifact is a fixed-`A5` `PARTIAL_RESULT`, not a universal `CLAIM`. No `claim-checks/<claim-id>.json` was linked; this prevents treating it as a scope-closing claim but does not prevent auditing the expressly bounded special case.

## Source-clause matrix

| source clause | source requirement | fixed-A5 claim | result |
|---|---|---|---|
| `c-objects` | all finite nonabelian simple `L`, every involution class `D` | only `L=A5` and its unique involution class | partial only |
| `c-colouring` | complete graph on `D`, edge colour exactly determined by `|ab|` | same definition for the 15 involutions of `A5` | addressed |
| `c-colour-automorphism` | all permutations preserving every edge colour | fixed-`A5` full colour group | addressed in the bounded claim |
| `c-question` | every admissible `(L,D)` has its colour group induced by `Aut(L)` | equality asserted only for fixed `A5` | universal target not answered |

`active_assignment_answered: pending` at triage; the universal quantifier already forces the eventual value to `no` unless the routed claim changes materially.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate / proof use | evidence planned | triage result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible pair `(L,D)` | one pair only | compare quantifiers | failed for universal coverage |
| `21.52-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `L=A5` | standard elementary structure of `A5` | pass for fixed pair |
| `21.52-D-single-involution-class` | admissibility | one conjugacy class of elements of order 2 | 15 double transpositions | cycle-type conjugacy argument in `A5` | pass for fixed pair |
| `21.52-Gamma-complete-on-D` | admissibility | complete simple graph on `D` | all unordered pairs of distinct double transpositions | direct definition | pass for fixed pair |
| `21.52-edge-colour-exact-product-order` | admissibility | equality of colours iff product orders agree | use the exact order-2 and order-3 relations, with order 5 the remaining colour | hand derivation in `A5` | pending |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary colour-preserving permutation | derive its action on five order-2 blocks and order-3 matchings | hand combinatorial proof | pending |
| `21.52-tau-induced-by-AutL` | target conclusion | extension for every admissible pair | prove only for fixed `A5` | compare upper bound with conjugation action of `S5` | pending for fixed pair; unproved universally |

## Target versus witness

- Source/active target: the full family of all admissible pairs `(L,D)`.
- Witness actually covered: `(A5,D)`, where `D` is its unique involution class.
- `witness_equals_target: false`. A single family member is not the universally quantified target.

## Subclaims

1. `A5` is finite nonabelian simple and its 15 double transpositions form its unique involution class.
2. Distinct involutions have product order 2 exactly when they fix the same point; the order-2 colour therefore recovers five 3-vertex blocks.
3. Between every two blocks, the order-3 edges form a perfect matching.
4. Triangle holonomy of these matchings is a transposition on a block; the three holonomies generate `S3`, forcing the kernel of the action on the five blocks to be trivial.
5. Hence the colour group embeds in `S5` and has order at most 120.
6. Conjugation by `S5` supplies 120 distinct restrictions belonging to the `Aut(A5)` restriction image, so both groups are equal of order 120.
7. None of the preceding steps covers any other admissible `(L,D)`.

## Tool probe

- GAP is present: banner reports GAP 4.12.1 (2022-10-20).
- Python is present: Python 3.12.3.
- `nauty-geng` and `dreadnaut` are present.
- Sage and Magma were not found on `PATH`.

No mathematical computation is planned: the fixed special case admits a short independent hand derivation. Consequently no implementation is being written or run and no Lead compute lease is needed.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| source and scope | rendered-PDF comparison plus canonical JSON | exact target and fixed-case boundary | truth of either assertion |
| involution blocks | cycle notation and centralizers in `A5` | recovery of five fixed-point blocks from colour 2 | kernel triviality |
| kernel | order-3 matching maps and triangle holonomy | injectivity of the colour group's action on the five blocks | any assertion beyond `A5` |
| lower bound/equality | faithful conjugation action of `S5` on `A5` and the five blocks | 120 induced colour automorphisms and fixed-`A5` equality | `Aut(A5)` claims not needed for the restriction equality; universal 21.52 |
| claimant certificates | secondary comparison only, after the hand derivation | possible agreement with the independently derived result | independence if used as the derivation; universal coverage |

## Hard limits and recommendation

Proceed with the independent hand proof. Even if every fixed-`A5` subclaim passes, keep `witness_equals_target: false`, `active_assignment_answered: no`, and the overall certification at most `status/conjectured` under the witness/target gate. The result is a rigorous bounded partial, not an answer to Problem 21.52.
