---
title: "Verification triage — Kourovka 20.21 — minimum-witness reductions"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
scope_record: Agents/Kourovka/scopes/20.21-two-index-twelve-kernels.json
assignment_revision: 1
claim: "If an active-scope witness exists, a minimum-order witness lies in the common-C3 branch and has even, odd-core-free intersection N, nonabelian coordinate kernels, and N not contained in Z(L)."
claimant: Problem-20.21
target_statement: "There exist a finite group G and normal subgroups K,L normal in G such that [G:K]=[G:L]=12, K is isomorphic to L, G/K is isomorphic to C_12, and G/L is isomorphic to A_4."
excluded_scopes:
  - Pairs of nonnormal subgroups
  - Pairs with only one index equal to 12
  - Pairs with the two quotient isomorphism types swapped unless K and L are correspondingly relabelled
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/group-extensions, project/kourovka, status/draft]
---

# Triage

## Claim and locked scope

Scope `20.21/two-index-twelve-kernels`, assignment revision 1.  The submitted claim is a conditional necessary reduction about a hypothetical witness and a minimum-order witness; it does not exhibit a triple and does not claim nonexistence.

## Clause matrix

| source clause | active | submission answers | remains |
|---|---:|---|---|
| c1: existence of a finite triple `(G,K,L)` satisfying all seven structural rows | yes | Candidate necessary restrictions on a minimum-order witness | The entire yes/no existence question |

`active_assignment_answered: pending` at triage; it cannot become `yes` from these conditional restrictions alone.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted proof use | triage result |
|---|---|---|---|---|
| 20.21-exists-GKL | admissibility | One triple satisfies every remaining row | Assumes a hypothetical witness in order to derive restrictions | not established |
| 20.21-G-finite | admissibility | `G` finite | Needed for minimum-order choice and finite-group arguments | conditional input only |
| 20.21-KL-normal | admissibility | `K,L normal in G` | Needed for `N=K intersection L` normality and conjugation descent | conditional input only |
| 20.21-both-index-12 | admissibility | Both indices exactly 12 | Used in the reviewed Goursat branches and smaller-witness descent | conditional input only |
| 20.21-kernels-isomorphic | admissibility | `K` abstractly isomorphic to `L` | Supplies the isomorphism theta and the Sylow/torsion comparisons | conditional input only |
| 20.21-quotient-K-C12 | admissibility | `G/K isomorphic to C12` | Fixes the ordered Goursat orientation and must survive descent | conditional input only |
| 20.21-quotient-L-A4 | admissibility | `G/L isomorphic to A4` | Fixes the ordered Goursat orientation and the order-three action | conditional input only |
| 20.21-existence-conclusion | target_conclusion | At least one such triple exists | Not addressed by a conditional reduction | unproved |

No row is claimed to pass for a concrete witness.

## Target versus witness

The source/canonical target is the finite triple above.  There is no submitted concrete witness.  The objects to check are an arbitrary hypothetical target triple and the smaller triples produced from it.  Accordingly, `witness = target` is not an available route to answering the active scope; the audit must instead check that every descended triple still has exactly the target orientation and hypotheses.

## Subclaims

1. A minimum-order witness exists if any finite witness exists.
2. A full-product witness strictly descends to a smaller active-scope witness, with both new kernels normal and the quotient orientation unchanged.
3. In the common-C3 branch, odd `|N|` contradicts `K isomorphic to L` via Sylow 2-subgroups.
4. `O_{2'}(K)=O_{2'}(N)=O_{2'}(L)` as the same subgroup; it is normal in `G`, is preserved by every `K to L` isomorphism, and quotienting it produces a smaller active-scope witness.
5. If `K` were abelian, the characteristic filtration `Q[2^j]` would be equivariant for the order-three conjugation action, while isomorphic kernels would force equal image sizes for the `V4` and `C4` quotient maps, giving a contradiction.
6. Nonabelianity plus `L/N isomorphic to C4` implies `N` is not contained in `Z(L)`.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | well-ordering of finite orders | A minimum witness may be selected conditionally | That any witness exists |
| 2 | hand audit of normality, restriction of theta, quotient isomorphisms, and orders | Full-product branch is absent from a minimum witness | Nonexistence of larger full-product witnesses |
| 3 | Sylow order and isomorphism-type comparison | `|N|` is even in any surviving witness | A classification of even `N` |
| 4 | characteristic odd-core and quotient correspondence | A minimum witness has trivial odd core in `N` | That `N` is a 2-group |
| 5 | finite-abelian torsion filtration and equivariance | Coordinate kernels in a surviving witness are nonabelian | Exclusion of nonabelian kernels |
| 6 | cyclic central quotient lemma | `N` is not contained in `Z(L)` | Any stronger placement statement for `N` |

## Tools and hard limits

Tools used: none.  The Lead imposed a computation-free, no-web, no-delegate audit and an exact three-artifact mathematical resource boundary.  The canonical scope record and the prior Validator Goursat audit are therefore the locked source/orientation inputs.  The existence question cannot be settled by the submitted arguments.

## Recommendation

Proceed with a line-by-line hand audit of all six subclaims.  At most a scoped necessary `PARTIAL_RESULT` can pass; `active_assignment_answered` must be `no`.
