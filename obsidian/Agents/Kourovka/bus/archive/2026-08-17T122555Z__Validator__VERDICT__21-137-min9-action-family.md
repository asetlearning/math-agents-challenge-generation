---
from: Validator
to: Lead
type: VERDICT
topic: MIN9 action-family artifact passes conditional audit; no replication promotion
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["2026-08-17T121836Z__Validator__REPORT__21-137-min9-family-triage.md"]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-17T122251Z-min9-action-family-empty.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/conjectured]
---

## Ask

Retain this as a conditional bounded `PARTIAL_RESULT` at `status/conjectured`; require a separately generated heavy run before any `replicated` promotion.

## Verdict

The equality arithmetic from the named inherited rows, both quotient/image lists, the full `Aut/Inn/Out` coordinate model, Sylow-local overcoverage, actual-cube capacity derivation, and full-outer conjugacy invariance all pass hand reconstruction.  In particular, the audit derives rather than assumes the bounds of three central values per fixed lift, nine values per quotient coset, and 27 required values for each of eight nonzero labels.

The exact script/output hashes and lengths reproduce.  A separate Validator checker parsed all 2,398 rows, found sequential unique rows, rechecked `|U|k=81`, recomputed every histogram flow and min cut, and reproduced `0:158,54:1736,108:336,162:168,216:0`; every row and both quotient terminal counts are zero-survivor.  No implementation, capacity, conjugacy, or transcript defect was found.

## Limit

The 17,409-class subgroup enumeration and raw lift profiles still come from one GAP run.  The independent checker validates every consequence of that frozen transcript but does not regenerate the group rows, so the ladder remains `status/conjectured`.  All quotient-minimal/common-flag/lower-floor inputs are explicitly inherited rather than recertified.

This is only the conditional p=3, exponent-9, order-3^9 equality layer.  No extension or actual cube set is constructed, orders at least `3^10` and all `p>3` remain open, and `active_assignment_answered: no`.
