---
title: "Working log — Kourovka 21.52 — rank-two decorated-fibre quotient"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
strategy: LIN2-RANK2-DECORATED-FIBRE-QUOTIENT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/projective-geometry
  - project/kourovka
  - status/draft
---

# Working log — rank-two decorated-fibre quotient

## Active-time ledger

- `2026-08-18T00:30:45Z` — START the Lead-authorized 34-active-minute pivot at
  official proof-direction cumulative minute 66; revision 1.
- `2026-08-18T00:42:45Z` — The mandatory minute-12 gate fired with an exact
  collision; no further mathematical route was started.
- `2026-08-18T00:46:45Z` — STOP after the derivation, scope caveats, formatting
  repair, and file-bus handoff; official proof-direction cumulative active
  minutes: 82.  State: `awaiting_lead`; 18 allocated minutes returned unused.

## Scope and resource gate

- Read the common and problem-agent protocols, canonical revision-1 scope, the
  just-filed rank-two nilpotent-incidence result, and the current Lead decision in
  full.
- Retained the exact universal target and every exclusion.  This lane concerns
  only the rank-two square-zero involution class in
  \(\operatorname{PSL}_n(2)\), and no family conclusion is promoted to the
  universal assertion.
- `active_scope_checked: yes`.
- The continuation inherited the already completed source/staleness gate.
- No computation and no web access were used.

## Minute-12 fibre gate

The tested intrinsic signature for a colour-\(2\) pair was its whole closed
common-colour-\(2\) core: the complete set of common colour-\(2\) neighbours and
the exact induced product-order colouring.

In \(\operatorname{GL}_4(2)\), a same-fibre pair

\[
 J(I),\quad J\!\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)
\]

has precisely six rank-two square-zero maps in its common centralizer, namely
all \(J(Y)\) with \(Y\in\operatorname{GL}_2(2)\).  They form a monochromatic
colour-\(2\) \(K_6\).

The cross-fibre pair

\[
 J(I),\quad
 \operatorname{diag}\!\left(
   \begin{smallmatrix}0&1\\0&0\end{smallmatrix},
   \begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)
\]

also has precisely six rank-two square-zero maps in its common centralizer, and
those six again form a monochromatic colour-\(2\) \(K_6\).  The second pair has
nonzero equal products and different image/kernel flags.

Decision: hard-kill `SIX-FIBRE-BY-COMMON-2-CORE`; do not assume the fibre
projection and do not start ambient incidence recovery.  The stronger all-colour
intersection-array refinement remains untested and would require a new Lead
decision.  Full derivation:
`Agents/Kourovka/problems/21.52/psln2-rank2-decorated-fibre-collision.md`.

Outcome: `STRATEGY_EXHAUSTED`; `active_assignment_answered: no`.
