---
title: "Post-separator assessment and A5, p=5 hypothesis-closure experiment"
author: operator
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
strategy_id: P-A5-5-HYPOTHESIS-CLOSURE
direction: proof
witness_equals_target: false
active_assignment_answered: no
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Post-separator assessment

## Resource and sourcing boundary

This assessment uses only the canonical scope record, the abstract separator
draft, and its linked hand-audit note. No web, historical solution, computation,
or delegated reasoning entered it.

**Sourcing label for every new mathematical route proposed below: General
knowledge, unverified.** No external citation is claimed. Each candidate fact is
an obligation of the experiment, not an input that may be silently assumed.

## Fidelity

My judgement is that Theorem 4 is target-faithful only as a restricted sufficient
theorem. It keeps the source's exact group order and exact set (not multiset) of
orders of vanishing elements, and it compares the same integer (p^a) inside the
two actual groups. Thus there is no quotient/model substitution inside the
restricted argument. However, Target-vanishing, CS-p, Aut-p, and Simple-order
uniqueness are four additional hypotheses absent from the source. The universal
row `19.30-forall-GS` is therefore not discharged:
`witness_equals_target: false` and `active_assignment_answered: no` remain
controlling.

## Significance

The separator has moderate structural value: it turns recognition into a
one-integer discrepancy and cleanly separates a nonsimple-side normal-Sylow task
from a simple-side character task. Its present extensional value is limited. The
permitted artifacts place no named nonabelian simple group in the subclass, and
CS-p, Aut-p, and order uniqueness can themselves carry classification-scale cost.
It does not yet meet the scope's stated infinite-family partial-progress target.

# Exactly one prescribed experiment

## `P-A5-5-HYPOTHESIS-CLOSURE` — proof direction

Treat (S=A_5) and (p=5) only as a candidate singleton target. Do not announce
that it satisfies Theorem 4. Attempt a self-contained hand dossier closing the
base admissibility fact and all four added hypotheses, without a pre-existing
character table or a named classification theorem.

### Exact observable

At the hard stop there must be a line-referenced five-row ledger:

| row | required terminal entry |
|---|---|
| base | (|A_5|=60) and (A_5) is finite simple |
| Target-vanishing | (m_5=5), an explicit (s) of order 5, and a constructed θ in `Irr(A5)` with θ(s)=0 |
| CS-5 | every proper nonabelian characteristically simple divisor of 60 is excluded or shown to have order prime to 5 |
| Aut-5 | every characteristically simple group of divisor order prime to 5 has automorphism order prime to 5 |
| uniqueness | every finite simple group of order 60 is identified with (A_5) |

The observable is **five `PASS` entries with explicit derivations, or the first
non-`PASS` row**. A conditional, cited-but-unexpanded, or blank row is a failure.

### Candidate hand routes (obligations, not assertions)

1. For the base row, derive the (A_5) conjugacy-class sizes and use the normal
   subgroup union-of-classes test.
2. For Target-vanishing, use the conjugation action on the six Sylow-5
   subgroups. Attempt to show that a Sylow-5 subgroup acts regularly on the other
   five points, hence the action is 2-transitive; then show the degree-five
   constituent θ=π-1 is irreducible and has value zero on a nonidentity
   5-element because exactly one Sylow subgroup is fixed.
3. For CS-5, derive the direct-power form of finite characteristically simple
   groups and exhaust the proper divisors of 60. Any required exclusion of a
   smaller simple order must be supplied by a Sylow argument in the dossier.
4. For Aut-5, use the same exhaustion to reduce to the elementary-abelian
   candidates (C_2,C_2^2,C_3), then calculate their automorphism-group orders
   by hand.
5. For uniqueness, start with an arbitrary simple (T) of order 60. Attempt the
   Sylow counts (n_5=6), (n_3=10), and (n_2\in\{5,15\}). If (n_2=5), use
   the faithful action on five Sylow subgroups. If (n_2=15), separate cyclic
   and Klein-four Sylow subgroups; use generator counting in the cyclic case and
   involution-class sizes plus incidence counting in the Klein-four case to force
   a faithful degree-five action. Finish only after the image is forced into
   (A_5) and the orders agree.

### Allocation — exactly 74 active problem minutes

| active minutes | task | gate |
|---:|---|---|
| 0–9 | base row: order and simplicity of (A_5) | stop if not self-contained |
| 9–24 | Target-vanishing via the six-point permutation character | stop if irreducibility or the zero value remains conditional |
| 24–38 | CS-5 divisor exhaustion | stop if any divisor case is unclassified |
| 38–49 | Aut-5 exhaustion and automorphism orders | stop if the candidate list is incomplete |
| 49–66 | simple-order uniqueness at order 60 | stop if a named classification result is needed |
| 66–74 | integrate Theorem 4, audit the five rows, and write the outcome | no new lemma may start here |

Time is not borrowed across gates.

### Success certificate

A self-contained dossier containing the five-row ledger, the constructed
degree-five irreducible character argument, the complete characteristically
simple divisor list, the three elementary automorphism orders, and the full
order-60 uniqueness argument. It must end with a constraint matrix stating only
the fixed-target consequence:

> For every finite (G), if (|G|=60) and
> (V_o(G)=V_o(A_5)), then (G\cong A_5).

That is the exact result a pass would support. It is a single-(S) special case,
not an infinite family and not the universal active assignment. Route it as a
conjectured special-case claim for review; retain `active_assignment_answered: no`.

### Failure certificate and hard kill

On the first failed gate, record the row, the exact unresolved implication or
counterexample, and all completed preceding rows. Report
`STRATEGY_EXHAUSTED: P-A5-5-HYPOTHESIS-CLOSURE`; do not invoke Theorem 4 and do not
promote (A_5), the alternating groups, or any other named family.

Kill immediately if a required row needs an external character table, a named
classification theorem, computation, or an unproved family input. Kill
unconditionally at 74 cumulative active problem minutes, even mid-sentence.

## Self-critique

The most likely weakness is significance, not boundedness: even a pass supplies
only one elementary order and may expose no scalable pattern. It is nevertheless
a sharp nonvacuity and stress test of the four-hypothesis separator; every outcome
is auditable, and failure identifies exactly which added hypothesis makes the
reduction unusable in practice.
