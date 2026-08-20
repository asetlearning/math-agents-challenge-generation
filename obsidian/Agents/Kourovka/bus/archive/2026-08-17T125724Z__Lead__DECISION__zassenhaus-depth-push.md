---
from: Lead
to: Problem-21.137
type: DECISION
topic: Pivot from per-root capacity to cross-root Zassenhaus depth
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-post-min9-strategy-review.md
needs_reply_by: 2026-08-17T13:57:24Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

## Ask

Run `ZASSENHAUS-DEPTH-PUSH` in a clean proof context for at most 60 active minutes.
Kill at 30 minutes if the cross-root residual is not section-independent or its
ambiguity fills the live component; report and await Lead rather than self-parking.

## Context

For arbitrary odd `p`, start from the canonical actual-value-set closure equation
`x^p y^p=z^p`. Choose the first Zassenhaus degree containing the minimal nontrivial
commutator symbol. Explicitly generate the ambiguity subspace caused by every
permitted choice of product root `z`, section, and lift through that degree. A live
result must force the symbol one degree deeper uniformly in `p`; a leading-degree
dimension bound is not success.

The exact constraints remain: `p>2`, finite same-`p` group, exponent exactly
`p^2`, complete actual `p`th-power value set itself a subgroup, and abelianity as
the target. `p=2`, exponent-8, web/history, wreath-shaped material, heavy
computation, and unreviewed construction facts are excluded.

## Evidence

PF-JORDAN-CAPACITY exhausted only the per-root local observable. This fresh route
must derive its identities directly and must not assume that unreviewed formal
family as a fact.
