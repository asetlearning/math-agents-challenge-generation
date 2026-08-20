---
title: "Triage — Kourovka 21.52 — fixed PSL(2,7) equality"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
---

# Triage — fixed PSL(2,7) equality

## Claim restated

For the single pair consisting of the concrete quotient model
\(L=\operatorname{SL}(2,7)/\{\pm I\}\cong\operatorname{PSL}(2,7)\) and its
21-element involution class \(D\), the claimant reports that the full group of
permutations of \(D\) preserving every product-order edge colour is equal, as a
permutation set, to the restriction image on \(D\) of the setwise stabilizer of
\(D\) in \(\operatorname{Aut}(L)\), both having order 336.

This is explicitly a fixed-pair partial result. It neither proves nor answers the
universal revision-1 assignment.

## Scope lock

- `scope_id`: `21.52/involution-class-product-order-colouring`
- `assignment_revision`: 1
- Active target: for every finite nonabelian simple group \(L\) and every
  conjugacy class \(D\) of involutions in \(L\), every permutation of \(D\)
  preserving \(|ab|\) on all pairs of distinct vertices is induced on \(D\) by
  an automorphism of \(L\) stabilizing \(D\) setwise.
- Excluded: Problem 21.53; unions of involution classes; automorphisms of only the
  uncoloured complete graph; colouring by the conjugacy class of \(ab\); and any
  bounded list of simple groups presented as a universal proof.

The configured source PDF was rendered and visually inspected at page 172. Its
four clauses agree with the canonical revision-1 record, including the product
*order* colouring and the universal question. The typed comparison used here is
\(\operatorname{Aut}_{\rm col}(\Gamma)=
\operatorname{res}_D(\operatorname{Stab}_{\operatorname{Aut}(L)}(D))\).

## Clause matrix

| Source clause | Active row? | What this fixed claim addresses | What remains open |
|---|---:|---|---|
| \(L\) finite nonabelian simple; \(D\) one involution class | yes | One asserted model, \(L=\operatorname{PSL}(2,7)\), and one asserted complete class | Every other admissible pair and an independent check of this pair |
| Complete graph on vertex set \(D\) | yes | The asserted 21 vertices and all 210 unordered pairs | Independent reconstruction |
| Edge colours agree iff \(|ab|=|cd|\) | yes | The asserted full product-order matrix with edge counts 42, 84, 84 for orders 2, 3, 4 | Independent reconstruction of every entry |
| Every colour-preserving permutation is induced from \(\operatorname{Aut}(L)\) | yes | Asserted equality of two 336-element permutation sets for this pair | The universal question |

`active_assignment_answered: no`.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | Required condition | Fixed candidate / proof use | Evidence currently available | Triage result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | Universal quantification over every admissible pair | One pair only | Scope record and source page 172 | unknown universally |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(L\) finite nonabelian simple | Claimed quotient \(\operatorname{SL}(2,7)/\{\pm I\}\) | Claimant certificate; independent check pending | pending |
| `21.52-D-single-involution-class` | admissibility | \(D\) is one complete conjugacy class of elements of order 2 | Claimed 21-element class | Claimant certificate; independent check pending | pending |
| `21.52-Gamma-complete-on-D` | admissibility | All unordered distinct pairs are edges | Claimed 210 pairs | Claimant certificate; independent check pending | pending |
| `21.52-edge-colour-exact-product-order` | admissibility | Colour is exactly product order in \(L\) | Claimed orders 2, 3, 4 with counts 42, 84, 84 | Claimant certificate; independent check pending | pending |
| `21.52-tau-preserves-all-edge-colours` | admissibility | Enumerate every permutation preserving all colours | Claimed group of order 336 | Claimant certificate; independent full-group check pending | pending |
| `21.52-tau-induced-by-AutL` | target_conclusion | Every such permutation is a restriction of a setwise-stabilizing automorphism | Claimed equality of two 336-element permutation sets for this pair | Claimant certificate; independent restriction-image check pending | not proved universally |

The claimant's claim-check file is structurally candid (`ready_for_validator:false`):
the universal row is `unknown` and the target conclusion is `not_proved`. It is a
completeness gate for a partial result, not evidence that any mathematical row
passes.

## Target versus witness

- Source target: the universal assertion over every admissible pair \((L,D)\).
- Witness actually computed in: one explicit quotient model of
  \(\operatorname{PSL}(2,7)\) and one asserted 21-element involution class.
- `witness_equals_target: false`.

The fixed witness is strictly narrower than the source target. No successful
finite check can upgrade this result beyond the stated fixed-pair partial.

## Sub-claims

1. The proposed quotient has exactly 168 elements and is the group
   \(\operatorname{PSL}(2,7)\), hence is finite nonabelian simple.
2. The selected 21 elements are exactly one complete conjugacy class and each has
   order 2.
3. The 21-by-21 matrix contains exactly the product orders for all 210 unordered
   distinct pairs.
4. The independently computed full colour-preserving permutation group is complete.
5. The independently computed abstract automorphisms of the quotient are complete,
   and their restrictions after setwise stabilization of \(D\) are exact.
6. The two resulting permutation sets are equal, not merely equinumerous.
7. The witness is the source target. This sub-claim is false: it is one pair in a
   universal problem.

## Tool probe

- Python: `/usr/bin/python3`, version 3.12.3.
- GAP: `/usr/bin/gap` exists; the first version probe used an invalid identifier,
  so its version remains to be recorded before any GAP-based verdict.
- Sage and Magma: not found.
- nauty `labelg` and `geng`: not found.

## Methods inventory

| Sub-claim | Independent method | What a pass proves | What it does not prove |
|---|---|---|---|
| 1–3 | A newly written exact finite-field quotient enumerator, with canonical \(\pm I\) representatives, full multiplication table, order and conjugacy checks | Exact properties of the concrete finite quotient and its selected class/matrix | The universal 21.52 statement |
| 4 | Independent colour-group computation via a partition-refinement/coset traversal architecture, not the claimant's edge-exposure backtracking | Completeness of the colour group for the independently reconstructed matrix | Any other \((L,D)\) |
| 5 | Independently derive all automorphisms from images of a certified generating pair, checking every multiplication-table relation and bijectivity | Exact restriction image for this finite model | A theorem about all simple groups |
| 6 | Canonically encode and compare the two complete permutation sets element by element | Equality for this fixed pair | Equality from matching orders alone; the universal target |
| 7 | Scope/source comparison | Establishes that the fixed witness is not the universal target | No mathematical fixed-pair equality |

## Hard limits and recommendation

No independent mathematical computation has been run. The requested bounded check
requires a fresh checker frozen by SHA-256 and an explicit Lead compute lease. The
checker must not reuse the claimant's backtracking logic. If leased and passed, the
appropriate result is **partial fixed-pair replication only**, retaining
`witness_equals_target:false` and `active_assignment_answered:no`. If the lease is
not granted, return a partial-only blocker rather than infer correctness from the
claimant artifact.

