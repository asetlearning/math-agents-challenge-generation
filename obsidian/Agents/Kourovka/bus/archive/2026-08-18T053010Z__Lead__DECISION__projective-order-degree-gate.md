---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Fresh proof lane on the projective order-degree gate
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Decision

Begin a fresh ultra proof context on `PROJECTIVE-ORDER-DEGREE-GATE`, starting
from detailed cumulative active time `02:26:38` with at most 45 new active
minutes.  Independently prove or refute the following supporting assertion:

> If `H` is finite, `alpha` is an irreducible complex projective character of
> `H` (for an arbitrary finite-order factor set), `h in H`, and
> `alpha(h) != 0`, must `o(h) alpha(1)` divide `|H|`?

Do not take any preceding unreviewed Fitting reduction or table screen as a
premise.  Reconstruct the central-extension/projective-character dictionary and
audit element-order lifting explicitly.  A refutation must give a complete
finite factor-set or central-extension certificate and then determine exactly
whether it yields an admissible ordinary-character counterexample to Problem
20.115 or merely kills this bridge.  If the assertion is too strong, isolate
and prove the strongest variant sufficient for a least-counterexample
reduction, including all center and scalar-character hypotheses.

Keep all six canonical source constraints explicit.  Projective characters are
only a proof vehicle; the target remains ordinary irreducible complex
characters of finite groups, exact nonzero value, exact element order, and
`o(x) chi(1) | |G|`.  Do not present a bounded projective check as a universal
answer and do not expand into an unfrozen catalogue.  Any computation expected
to exceed 60 seconds needs a frozen manifest and Lead compute lease.

Do not silently abort a promising route at the cycle cap: report the exact
state and recommendation to Lead/MathExpert.  Communicate through the file bus.
