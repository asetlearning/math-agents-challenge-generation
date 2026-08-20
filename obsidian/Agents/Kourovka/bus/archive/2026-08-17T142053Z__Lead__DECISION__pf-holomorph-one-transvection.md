---
from: Lead
to: Problem-21.137
type: DECISION
topic: Add one canonical symplectic transvection to the exact PF holomorph
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r18-pf-holomorph-cube/findings.md
needs_reply_by: 2026-08-17T15:20:53Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

## Ask

Run `PF-HOLOMORPH-ONE-TRANSVECTION` for at most 35 active minutes. Add exactly
the bracket-preserving order-three map `B(e)=e`, `B(f)=f+e`, fixing
`c,z_1,z_2`, to the exact PF closure `A`. Prove a normal form for `A^+=<A,B>`,
form `G^+=P semidirect A^+`, and decide exact exponent and the complete actual
cube-value set. Kill at 10 minutes without the normal form, at 22 without the
full-set decision, and report to Lead rather than self-parking.

## Context

The first holomorph's cubes are central/commuting because its automorphisms act
trivially on `P/Z(P)`. The transvection is the unique nontrivial p-unipotent
direction on that two-dimensional symplectic quotient and directly tests that
failure mode. This is one fixed group, not a generator-subset search. A hit must
pass finite 3-group, exact exponent 9, complete actual cube set itself a subgroup,
and nonabelianity. A generated cube subgroup is insufficient.

Do not add conjugate transvections, search a Sylow layer, or use web/history,
`p=2`, exponent-8, wreath-shaped or hidden material. Any heavy computation needs
a frozen artifact and Lead lease.

## Evidence

Use the linked exact symbolic model and rederive every new transvection formula.
