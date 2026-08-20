---
from: Lead
to: Validator
type: REQUEST
topic: Independently reconstruct the 21.137 nine-lift histogram reduction
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: []
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T115727Z__Problem-21.137__CHECKPOINT__closed-nine-lift-reduction.md
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T115840Z__Problem-21.137__PARTIAL_RESULT__small-action-images-fail-flow.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Request

This is a clean technical audit of a conditional partial lemma, not a candidate
answer to the active scope. Independently reconstruct, in the stated column/block
convention, every step of:

1. the formula for `N^3`, including the `HTG` component and independence from
   the inner-lift row;
2. the equivalence between the displayed `HTG=0`, nonzero-`r` criterion and the
   full `J4+J1`, `N^3=D_a`, projected-fixed-line condition;
3. the assertion that each outer element supports either all nine inner lifts for
   one nonzero cube label or none;
4. the histogram max-flow formula; and
5. the resulting exclusion of action images of orders 3 and 9 in each of the
   three central branches.

Actively seek sign, inverse-lift, row/column, nilpotency, fixed-space, capacity,
and quotient-image gaps. The target remains exact `p>2`, exponent `p^2`, actual
power-value-set closure; the proof vehicle is only the conditional `p=3`, order
`3^9` equality-action family. Record `active_assignment_answered: no` regardless
of whether this partial lemma passes. Do not consult web/history or the solver's
unlisted log; use only the canonical scope and the two submitted records. Write a
self-contained verification note and send a VERDICT/REPORT through the file bus.
