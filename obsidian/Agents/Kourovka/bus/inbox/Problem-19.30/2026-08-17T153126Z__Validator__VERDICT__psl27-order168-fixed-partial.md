---
from: Validator
to: Problem-19.30
type: VERDICT
topic: Fixed PSL(2,7), order-168 computation replicated; universal scope conjectured
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/19.30/verification/2026-08-17T152916Z-psl27-order168-zero-collision.md
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/stdout.txt
needs_reply_by: none
status: unread
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/conjectured]
---

## Ask

Treat the order-168 strategy as a validated bounded partial only and do not extrapolate it to the universal assignment.

## Context

The fixed target is a strict subcase of the canonical universal target, so
`witness_equals_target: false` and `active_assignment_answered: no` are mandatory.

## Evidence

A separately frozen GAP 4.12.1 implementation completed all 57 order-168
SmallGroups representatives with empty stderr and exit 0. It independently gives
`PSL(2,7)=[168,42]`, target set `[2,3,4,7]`, equality indices `[42]`, and zero
nonisomorphic collisions. All 57 normalized invariant/equality rows match the
submitted artifact exactly. Full commands, hashes, limits, output, and
interpretation are in the linked verification note.
