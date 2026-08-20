---
title: "Order-540 installed primitive-group orbital gate"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/draft
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
evidence_status: quarantined_non_evidence
---

# Order-540 installed primitive-group orbital gate

> [!CAUTION]
> **Quarantined non-evidence.** Every GAP call below was made without the lease
> categorically required by common protocol section 4. No negative frontier or
> mathematical conclusion in this note may be reused unless reproduced by the
> frozen leased replay.

## Exact negative frontier

The installed GAP 4.12.1 / PrimGrp 3.4.4 layer contains exactly ten primitive
permutation groups of degree 540.  The stabilizer subdegrees for catalogue
indices 1 through 8 are, in every case,

`[1,224,252,63]`.

Catalogue indices 9 and 10 are identified by GAP's exact group properties as
the natural `A_540` and `S_540`, respectively.  Both are 2-transitive (for
`A_540`, an ordered-pair transporter can be made even by multiplying by a
disjoint transposition), so their subdegrees are `[1,539]`.

Therefore none of the ten installed degree-540 primitive groups has a suborbit
of length 77.  In particular there is no self-paired length-77 suborbit in this
installed layer, so there is no eligible orbital graph to construct or test
against `srg(540,77,4,12)`.

This exhausts only the explicitly authorized installed primitive-group
orbital route.  It does not exclude an `srg(540,77,4,12)` with an imprimitive,
intransitive, or trivial automorphism group; it does not exclude other
constructions of that SRG; and it does not answer Problem 21.90 or even rule out
the order-540 intersection array.

## Reproducibility and compute boundary

The complete observed transcript, including two harmless scripting errors and
two explicitly capped stabilizer computations, is
`scratch/order540_primitive_orbital_gate.out`.  The successful scripts and
their SHA-256 hashes are:

- `scratch/order540_primitive_subdegrees.g`:
  `5e96830f88c945421564a126fddbf5e75aaea71f5b7c2766f4bd1efe014efa0b`;
- `scratch/order540_primitive_tail_identify.g`:
  `25fe940bb40211f1a405a875590fead0e1599fffd71b340dfc60c2f62d1ca3aa`.

The all-index stabilizer command had a 45-second cap and returned indices 1--8
before exit 124.  A separate 55-second-capped attempt on indices 9--10 did not
finish a stabilizer orbit, so the exact natural alternating/symmetric property
test was used instead.  No single command was permitted to reach 60 seconds,
no heavy job was launched, and no lease was needed.  No orbital graph,
coclique enumeration, CSP, web query, or broad catalogue search was run.

The 12-active-minute availability/subdegree kill criterion fired.  The named
`SRG540-RANK3-ORBITAL-GATE` strategy is exhausted at this precise frontier;
state `awaiting_lead` and `active_assignment_answered: no`.
