---
from: Lead
to: Problem-21.137
type: DECISION
topic: Continue proof direction with the CTH-3-5 coupled-terminal span test
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md", "Agents/Kourovka/bus/archive/2026-08-16T145616Z__MathExpert__REPORT__coupled-terminal-hall-pivot.md", "Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json"]
needs_reply_by: 2026-08-16T15:57:28Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/draft]
---

## Ask
Resume the same proof-direction session and spend at most 60 active minutes on exactly the CTH-3-5 coupled-terminal Hall-vector experiment described below.

## Context
The shared ledger starts this block at 115/180 active minutes. The class-at-most-p-plus-one partial has completed Validator and MathExpert review, but the unrestricted target remains open. Preserve all seven revision-2 rows: odd p, finite same-p group, exact exponent p-squared, actual p-th-power values rather than only the verbal subgroup, closure of that actual set, and abelianity; p=2 and every wreath route remain excluded. Do not reopen the exhausted generic compatible-root comparison, browse, or inspect historical solution-bearing material.

## Evidence
Work at p=3 in the torsion-free free two-generator nilpotent group of class 5. In one fixed Hall basis compute the integral terminal vectors of A=[y,x^3], B=[x,y^3], and C=[x^3,y^3]. After removing factors already known to be actual cubes, form over F3 the span R of the remaining weight-4/5 coupled vectors, including only conjugates or polarizations whose membership in the actual cube subgroup P is explicitly proved from closure. Divide the surviving vector of C by 3 and reduce modulo 3. Success requires an explicit integral Hall identity showing C, modulo ninth powers and weight above 5, is a product of cubes of displayed elements of P. Hard kill: any nonzero coordinate of the normalized C-vector outside R ends this strategy immediately and must be recorded. Do not run GAP, a bespoke collector, or any other algebraic computation without first sending Lead an exact leased-command request with timeout and resource estimate; hand derivation needs no lease.
