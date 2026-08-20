---
title: "Triage — Kourovka 12.15 — R1/R2 pc eliminations and universal elementary-centre witness"
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
claim: "Conditional on the reviewed order-128 least-counterexample reductions, the R1, cyclic-centre R2, and elementary-centre R2 regimes are all impossible; this does not address any larger order."
claimant: Problem-12.15
target_statement: "For every finite 2-group G in which equality of normal closures implies conjugacy, G' is abelian."
excluded_scopes: []
target_object: "An arbitrary finite 2-group satisfying the source normal-closure-fibre hypothesis."
witness_object: "Three structural regimes inside the proposed order-128 least-counterexample reduction; separately, one materialized elementary-centre presentation G0."
witness_equals_target: false
citation: none
verification_method: "independent hand reconstruction of finite-group and commutator arguments; no unleased GAP computation"
tools_used: ["GAP 4.12.1 (availability/version probe only)", "Python 3.12.3 (availability/version probe only)", "Poppler pdftotext 24.02.0", "rendered source PDF page 58"]
scope_answered: []
scope_not_answered: ["12.15/normal-closure-fibres at orders greater than 128", "the unrestricted source assertion"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/2-groups, project/kourovka, status/draft]
---

# Triage

## Claim locked

The routed assertion is a **bounded conditional elimination**, not a solution claim:
assuming the previously reviewed reduction of an order-128 counterexample to the
R1/R2 structural rows, eliminate R1, cyclic-centre R2, and every elementary-centre
R2 row.  The single group `G0` is only a materialized local table which itself
fails the source hypothesis.  No claim-check JSON is present; that is acceptable
for the routed `PARTIAL_RESULT` questions but prevents treating them as a formal
scope-closing `CLAIM`.

## Source and clause matrix

The rendered PDF, issue 12 page 58, says: in a finite 2-group, if any two elements
whose normal closures coincide are conjugate, must the derived subgroup be
abelian?  The canonical revision-1 transcription is faithful.

| source clause | active | claim coverage | result |
|---|---:|---|---|
| c1, unrestricted finite 2-groups | yes | proposed elimination of the residual order-128 R1/R2 cases only | pending bounded verification; unrestricted clause unanswered |

`active_assignment_answered: pending` at triage and cannot become `yes` from this
package: larger orders are expressly untouched.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | proposed proof use / candidate value | evidence status | result |
|---|---|---|---|---|---|
| 12.15-forall-G | admissibility | every admissible finite 2-group | only order-128 residual regimes are treated | bounded subset only | fail for full scope |
| 12.15-finite | admissibility | G finite | all routed regimes have proposed order 128 | dependency audit pending | conditional pass |
| 12.15-two-group | admissibility | G a 2-group | all routed regimes are pc 2-group regimes | dependency audit pending | conditional pass |
| 12.15-normal-closure-fibre | admissibility | equal normal closures imply conjugacy | elementary-centre regime is to be excluded by an equal-closure/different-order pair; `G0` therefore fails this row | exact closure proof pending | pending; `G0` is out of scope as a source counterexample |
| 12.15-derived-abelian | target conclusion | G''=1 | no unrestricted conclusion; the conditional regimes posit nonabelian G'=H and are to be eliminated | larger orders unaddressed | unproved globally |

## Target versus witness

The source target is an arbitrary admissible finite 2-group.  The R1/R2 objects
are proposed necessary cases only for a hypothetical order-128 counterexample;
they are not equal to the source target.  A successful audit proves a bounded
case exclusion, not the source conclusion.  The explicit `G0` presentation is a
finite 2-group but has a claimed equal-normal-closure nonconjugate pair, so it is
an `OUT_OF_SCOPE_EXAMPLE` for the source admissibility class and cannot be a
counterexample to 12.15.

## Subclaims

1. The prior order-128 reduction really makes R1/R2 exhaustive and supplies each
   structural hypothesis used below (`G'=H`, the structures of `H,A,Z,E,V`, and
   trivial `E`-action on `V`).
2. Every automorphism of `D8` or `Q8` trivial on `H/Z(H)` is inner; consequently
   R1 gives `G=H C_G(H)` and then `G'<=Z(H)`, contradicting `G'=H`.
3. In cyclic-centre R2, the action-square identity makes every square centralize
   `H`; because squares lie in `H`, every square lies in `A=Z(H)`, so `G/A` has
   exponent two and is abelian, contradicting `G'=H>A`.
4. In elementary-centre R2, the non-kernel lift can be normalized so its residual
   functional is zero and its square lies in `<z>`.
5. The map `L:K->V` defined by kernel-lift actions is linear and is an isomorphism,
   using `G'=H` and the quotient commutator span.
6. The quadratic function `d=q+rho` has a nonzero value 1, so `r` and `rh` have
   different orders.
7. Both normal closures are exactly `<r,H>` for every central offset.
8. The structural normal form used in 4--7 covers every pc-consistent
   elementary-centre R2 row; exact overlap equations may delete rows but do not
   create an omitted relation type.
9. Separately, the displayed `G0` presentation has the claimed finite invariants
   and named pair.  This computational materialization is not needed if 4--8 are
   proved abstractly, and a claimant transcript alone is not independent
   replication.

## Methods inventory and limits

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1 | inspect the already reviewed reduction notes and re-check each imported implication | the three regimes exhaust the order-128 remainder | anything at larger order |
| 2 | explicit automorphism calculation and commutator decomposition | R1 is inconsistent with the imported order-128 counterexample data | the source assertion outside R1 |
| 3 | hand calculation of conjugation squares, followed by the exponent-two quotient lemma | cyclic-centre R2 is inconsistent | elementary-centre R2 or larger orders |
| 4--8 | direct abstract calculation in an arbitrary group satisfying the elementary-centre R2 structural axioms | universal exclusion of that conditional family, independent of pc offsets | that every source counterexample must have order 128 or be in this family |
| 9 | an independently designed GAP run would replicate the concrete finite presentation | invariants of `G0` only | universal family coverage; no run is authorized without a compute lease |

GAP 4.12.1, Python 3.12.3, and Poppler 24.02.0 are installed; Sage and Magma were
not found.  No heavy computation is leased, so no GAP verification will be run.
The recommended path is full hand verification of subclaims 1--8 and a partial,
non-replicated note on subclaim 9 unless Lead separately leases a run.

