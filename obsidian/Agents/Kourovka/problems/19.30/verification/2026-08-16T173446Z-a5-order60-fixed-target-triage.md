---
title: "Triage — Kourovka 19.30 — A5 order-60 fixed-target partial result"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "For every finite group G, if |G|=60 and V_o(G)=V_o(A_5), then G is isomorphic to A_5."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
target_object: "Every pair (G,S) in the canonical universal scope."
witness_object: "The strict fixed-target subcase S=A_5, |G|=60."
witness_equals_target: false
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Triage — Kourovka 19.30

## Claim and scope lock

The submitted `REPORT` asks for hand verification of the fixed-target implication

\[
 \forall G\text{ finite},\quad |G|=60\ \text{and}\ V_o(G)=V_o(A_5)
 \Longrightarrow G\cong A_5.
\]

The canonical record is `19.30/vanishing-order-simple-recognition`, revision 1. The rendered source defines a vanishing element as one on which some irreducible complex character is zero and asks the universal same-order, same-vanishing-order-set recognition question for a finite group and a finite simple group. The canonical transcription agrees with the rendered statement. The fixed choice `S=A_5` is a strict subcase, so `witness_equals_target: false` regardless of whether the subcase proof survives.

## Clause matrix

| source clause | active? | submitted answer | remains open |
|---|---:|---|---|
| `c-definition`: vanishing means `chi(g)=0` for some irreducible complex character | yes | used literally for `A_5` and for same-order `G` | verification pending |
| `c-question`: universal recognition over finite `G` and finite simple `S` | yes | only `S=A_5`, hence order 60 | every other finite simple target |

`active_assignment_answered: pending` at triage; it must be `no` in the final note because the universal source clause is outside the submitted result.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted use | triage result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | every admissible pair `(G,S)` | fixes `S=A_5` | failed for universal coverage |
| `19.30-G-finite` | admissibility | `G` finite | arbitrary finite `G` of order 60 | pending hand audit |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | asserts and proves `A_5` finite simple | pending hand audit |
| `19.30-vanishing-definition` | admissibility | zero of some character in `Irr(H)` | six-point character for `A_5`; Clifford restriction for `G` | pending hand audit |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | `|G|=|A_5|=60` | pending hand audit |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets, without multiplicity | compares membership of the single order 5 | pending hand audit |
| `19.30-isomorphic` | target conclusion | `G\cong S` | concludes `G\cong A_5` | pending for fixed target; unproved universally |

The universal-quantifier row already prevents an affirmative answer to the active assignment. No failed fixed-target admissibility row is presently visible; every mathematical row remains to be reconstructed rather than inherited from the dossier's `PASS` labels.

## Target versus witness

The source target is the universal pair `(G,S)`. The proof vehicle is the strict singleton target `S=A_5`; there is no quotient or computational model. Thus witness equality is not unknown or assumed but false as a scope identity. This is a scope mismatch by design, appropriate only to a `PARTIAL_RESULT`.

## Subclaim decomposition

1. `A_5` has order 60 and is simple, including completeness of the class-union argument.
2. Its conjugation action on six Sylow-5 subgroups has the asserted normalizer, is 2-transitive, and yields an irreducible degree-five constituent vanishing on a 5-cycle.
3. Every nontrivial finite characteristically simple group is a direct power of one finite simple group, with no gap in the maximal-direct-subcollection argument.
4. Every proper nonabelian characteristically simple divisor of 60 has order prime to 5.
5. The characteristically simple 5-prime divisors of 60 are exactly `C_2`, `C_2^2`, and `C_3` (plus the optional trivial group), and their automorphism groups have order prime to 5.
6. Every finite simple group of order 60 is isomorphic to `A_5`, including the full `n_2=15` branch.
7. Every nonsimple group of order 60 has a normal Sylow-5 subgroup, via the simultaneous least-order induction over 5-divisible divisors of 60.
8. If a group has a normal Sylow subgroup of order 5, Clifford homogeneous restriction and cyclotomic noncancellation show that its nonidentity elements are nonvanishing.
9. Equality of vanishing-order sets then rules out nonsimple `G`, and simple-order uniqueness gives `G\cong A_5`.
10. The witness subcase is not the universal canonical target.

## Tools available and boundary

The required probe found GAP 4.12.1, Python 3.12.3, and `pdftotext` 24.02.0; Sage and Magma were absent. No mathematics will be computed. The rendered PDF page was inspected directly. The audit is restricted to the canonical scope, rendered source, and the three references in the incoming report; no web, solution-bearing history, unlisted verification note, character table, classification theorem, or delegate is authorised.

## Methods inventory

| subclaims | hand method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | enumerate even cycle types, centralizers, class sizes, and all class unions | `A_5` is simple of order 60 | anything about arbitrary simple `S` |
| 2 | orbit-stabilizer, normalizer action, rank-two permutation endomorphism algebra, invariant orthogonal complements | an explicit irreducible degree-five character of `A_5` vanishes on a 5-cycle | the full character table or all vanishing orders |
| 3–5 | minimal normal subgroups, direct products, divisor and Sylow exhaustion, elementary automorphism counts | the exact CS-5 and Aut-5 hypotheses at order 60 | analogous hypotheses at other orders |
| 6 | Sylow counts, faithful coset actions, sign, centralizers, and involution incidence | uniqueness of the simple group of order 60 | classification of simple groups in other orders |
| 7 | simultaneous strong induction on the order, split by whether 5 divides a minimal normal subgroup | a normal full Sylow-5 subgroup in every nonsimple order-60 group | normal Sylow subgroups at unrelated orders or primes |
| 8 | Clifford homogeneous restriction to normal `C_5` and the minimal polynomial `Phi_5` | order 5 is absent from `V_o(G)` when the Sylow-5 subgroup is normal | nonvanishing of arbitrary elements or larger normal `p`-subgroups |
| 9–10 | compare membership of the integer 5 and enforce the clause matrix | the fixed `A_5` implication only | the universal Kourovka scope |

## Hard limits and recommendation

The permitted evidence cannot establish the universal quantifier, and the explicit instruction fixes `witness_equals_target: false`, `active_assignment_answered: no`, and `status/conjectured`. A successful audit can therefore validate only the internal hand derivation of the fixed-target partial theorem; it cannot certify the active assignment, promote the note above conjectured, or import any family/classification consequence.

Recommendation: proceed with full line-by-line hand verification of the ten subclaims, reporting any repair explicitly and retaining the mandated scope/status fields.
