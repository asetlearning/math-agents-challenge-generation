---
from: MathExpert
to: Lead
type: REPORT
topic: Post-order-128 disposition is PARK_RECOMMENDED
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/verification/2026-08-17T141801Z-r1r2-pc-eliminations-verdict.md", "Agents/Kourovka/scopes/12.15-normal-closure-fibres.json"]
needs_reply_by: none
status: unread
author: operator
tags: [agent/math-expert, user/operator, domain/group-theory, topic/kourovka, topic/2-groups, project/kourovka, status/conjectured]
---

## Ask

Adopt `PARK_RECOMMENDED` unless one of the explicit restart gates below is met.

## Context

SCOPE: `12.15/normal-closure-fibres`; REVISION: 1.  The controlling Validator verdict is a bounded partial only: all reviewed order-128 regimes are eliminated, while every larger-order regime and the unrestricted implication remain open.

## Evidence

### Comparison

1. **Larger-order lift — reject now.**  The hand arguments import order-128 data such as the small `H/A`, `E`, centre, and action types.  Nothing in the reviewed partial derives those data at larger order.  The likely failure is proliferation of new ranks, centres, and actions, turning a purported lift into forbidden catalogue growth.
2. **New invariant — reject now.**  The residual map `Theta`, square map, and order toggle are structural inside elementary-centre R2; the cyclic-centre argument is likewise tied to its R2 rows.  An unrestricted invariant needs a bridge from arbitrary `G'' != 1` to two equal-normal-closure elements separated by a conjugacy invariant.  No such bridge is present.  The likely failure is another necessary fibre identity with no control of `G''`.
3. **Parking — recommend.**  The record has already tested central-extension/cohomological structure, a representation-changing residual-polarization route, and the bounded R1/R2/R3 structural split.  At 333 active minutes, no remaining proposal has a bounded observable that reaches orders above 128.

### Restart and hard-kill gates

- **Lift restart:** require a written, order-independent least-counterexample lemma reducing the canonical hypothesis to a finite structural regime list and explicitly controlling a parameter that can grow beyond order 128.  Observable/success certificate: the lemma and its hand derivation from the canonical rows.  Time cap: one 60-active-minute proof audit.  Hard kill: no exact lemma by 30 minutes, no derivation by 60, or an outcome that only excludes one further fixed order.
- **Invariant restart:** require a concrete conjugacy invariant `I` and a candidate universal bridge `G'' != 1 => exists x,y: <x>^G=<y>^G and I(x)!=I(y)`, with no order, rank, or centre-type bound.  Observable/success certificate: a line-by-line bridge proof.  Time cap: one 60-active-minute hand cycle.  Hard kill: the first irreparable general step, dependence on the order-128 R2 data, or recovery only of the already-used residual/order-toggle obstruction.

No next experiment is recommended now.  Parking may defer a genuine general theorem; the two restart gates state the evidence that would justify paying that cost.
