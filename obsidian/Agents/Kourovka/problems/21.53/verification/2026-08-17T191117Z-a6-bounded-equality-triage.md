---
title: "Triage — Kourovka 21.53 — bounded A6 class-2A equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Triage — bounded `(A6,2A)` equality

## Claim and locked scope

Claim to check: for `L=A6` and its class `D` of 45 double transpositions, the complete product-order-coloured graph satisfies
`Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma)`, and both groups have order 1440.

The active revision-2 target asks for this equality for **every** finite nonabelian simple `L` and every involution class `D`. Excluded here are Problem 21.52, unions of classes, replacement of the second-smallest prime, and any inference from a bounded list to the universal statement. The routed artifact is a `REPORT`, not a closing `CLAIM`, and supplies no `claim-checks/*.json`; this review is therefore confined to its explicitly non-closing finite statement.

## Source and clause matrix

Rendered source PDF page 172 was inspected visually after `pdftotext` navigation. Problem 21.53 says, in the notation of 21.52, that `Aut_t(Gamma)` contains the permutations preserving every edge with product order `t`, that `Aut(Gamma)` is the intersection over all `t`, and asks whether the intersection for the two least prime divisors suffices.

| source clause | active? | bounded claim | remainder |
|---|---:|---|---|
| inherited finite nonabelian simple `L`, one involution class `D`, complete product-order colouring | yes | proposes `A6,2A` | every other admissible pair |
| `Aut_t` for every positive integer `t`, including vacuous absent colours | yes | must be checked exactly | none at this pair once definitions are audited |
| full group is the intersection of every colour restriction | yes | must be checked | none at this pair once definitions are audited |
| equality for the two least primes | yes | proposes equality for one pair | universal quantifier remains open |

`active_assignment_answered: pending` (mechanically it cannot become `yes` from this bounded claim).

## Constraint-and-conclusion matrix

| constraint_id | role | candidate/proof use | present status |
|---|---|---|---|
| 21.53-forall-L-D | admissibility | only one pair is treated | fails as universal coverage; acceptable only as partial evidence |
| 21.53-L-finite-nonabelian-simple | admissibility | `A6` | to prove independently |
| 21.53-D-single-involution-class | admissibility | 45 double transpositions | to prove independently |
| 21.53-Gamma-product-order-colouring | admissibility | all 990 unordered products | to recompute independently |
| 21.53-Aut-t-definition | admissibility | restrictions at all positive integers; absent labels vacuous | to audit explicitly |
| 21.53-two-minimal-primes | admissibility | `|A6|=360`, hence `p=3` | to prove independently |
| 21.53-full-colour-group-definition | admissibility | intersection over occurring colours | to audit explicitly |
| 21.53-two-colours-determine-all | target conclusion | asserted only for `(A6,2A)` | to prove/refute for this pair only |

## Target versus witness

Source target: all pairs `(L,D)` inherited from 21.52. Witness: the explicit even-permutation group `A6` acting on six letters and its double-transposition class. The witness is an admissible instance, not equal to the universally quantified target domain. `witness_equals_target: false` for the universal scope; exact equality of the computational model with the bounded pair will be established from explicit permutations.

## Subclaims and methods inventory

1. `A6` is finite nonabelian simple, has order 360, and its 45 involutions form one class. Method: standard permutation-group proof plus direct enumeration. A pass proves admissibility of this pair only.
2. The complete matrix has precisely colours `2,3,4,5` (and the stated valencies). Method: a fresh tuple-permutation enumerator. A pass proves the finite matrix only.
3. Each graph restriction encodes exactly `Aut_2 intersection Aut_3` or the full colour group, including vacuity. Method: prove the incidence encoding in both directions. A pass proves encoding equality, not its computed automorphism order.
4. Both groups have order 1440. Method: a duad--syntheme reconstruction giving a 1440 upper bound, plus explicit colour-preserving `S6` and a colour-preserving duality for the lower bound; if useful, a separately written bounded backtracker may cross-check. A pass proves the exact bounded equality without trusting the claimant's nauty run.
5. Universal 21.53. No method in this review addresses it. A bounded pass does not answer the active assignment.

## Tool probe and limits

Confirmed: GAP 4.12.1 at `/usr/bin/gap`, Python 3.12.3 at `/usr/bin/python3`, dreadnaut and bliss installed, Poppler `pdftotext` 24.02.0. Sage and Magma are absent. The claimant used nauty, so nauty/dreadnaut will not be used as independent order evidence. A complete structural proof or independently designed bounded checker is available; neither can justify the universal statement.

## Recommendation

Proceed with full verification of the finite `(A6,2A)` statement only. Any pass is `PARTIAL_RESULT` with `active_assignment_answered: no`.
