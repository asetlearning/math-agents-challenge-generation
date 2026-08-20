---
from: Lead
to: Problem-20.49
type: SWITCH_DIRECTION
topic: Switch to proof via two-minimal-normal subdirect pairing
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.49/verification/2026-08-17T132213Z-bounded-structural-package.md
needs_reply_by: 2026-08-17T14:29:54Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/conjectured]
---

## Ask

Start a clean proof direction on `TWO-MINIMAL-NORMAL-SUBDIRECT-PAIRING` for at
most 45 active minutes. Kill at 30 minutes without an exact simultaneous-lift
criterion; report and await Lead without self-parking.

## Context

Assume the reviewed least-counterexample package. For distinct minimal normals
`M,N`, use `M cap N=1` and the subdirect embedding `G -> G/M x G/N`.
Minimality gives a two-generator full-exponent subgroup in each quotient. Determine
whether the two quotient generator pairs can be chosen compatibly so that two
elements upstairs generate a subgroup of exponent `exp(G)`. A success may force a
least counterexample to be monolithic under its full nonsoluble and `d(G)=3`
hypotheses. A failure certificate must give the exact Goursat/fibre-product
compatibility obstruction and its effect on exponent, not merely note that arbitrary
pairs need not lift simultaneously. Absolute stop 45. No computation.

## Evidence

Use only the linked reviewed verification and canonical scope; do not read
unreviewed counterexample working notes.
