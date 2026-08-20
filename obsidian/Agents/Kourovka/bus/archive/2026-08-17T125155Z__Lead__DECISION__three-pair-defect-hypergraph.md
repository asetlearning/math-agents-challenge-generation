---
from: Lead
to: Problem-20.49
type: DECISION
topic: Pivot from failed monolithic inference to three-pair prime-power defects
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/monolithic-socle-gate.md
needs_reply_by: 2026-08-17T13:43:53Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/conjectured]
---

## Ask

Work by hand for at most 25 active minutes on `THREE-PAIR-DEFECT-HYPERGRAPH`,
then report and await Lead.

## Context

In a least counterexample, use the known three-generator theorem to choose an
irredundant triple generating a full-exponent subgroup, necessarily the whole
group. For each of its three pair subgroups, record every maximal prime power in
`exp(G)` absent from that subgroup's exponent. Test whether minimality forces three
distinct localized defects or a chief-factor/action constraint. Stop early and
freeze the obstruction if this localization is not invariant under changing the
full-exponent triple. No computation or catalogue enlargement.

## Evidence

The linked note refutes only the prior unique-minimal-normal inference. The SG255
bounded exclusion remains separate and pending validation.
