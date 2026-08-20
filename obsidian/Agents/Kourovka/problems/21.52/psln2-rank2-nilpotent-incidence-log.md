---
title: "Working log — Kourovka 21.52 — PSL_n(2) rank-two nilpotent incidence"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
strategy: LIN2-RANK2-NILPOTENT-INCIDENCE
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

# Working log — rank-two square-zero involutions

## Active-time ledger

- `2026-08-18T00:17:53Z` — START fresh 45-active-minute family lane,
  revision 1; cumulative active minutes: 0.
- `2026-08-18T00:28:43Z` — STOP after the hard gate, write-up, scope check,
  and file-bus handoff; cumulative active minutes: 11.  State: `awaiting_lead`; 34 allocated
  minutes remain unused.

## Source, scope, and resource gate

- Read the common and problem-agent protocols, canonical revision-1 scope, and
  the independently reviewed rank-one family partial in full.
- Read configured PDF page 172 with `pdftotext -layout`, rendered the same page
  with `pdftoppm`, and visually checked the full statement.  It is unstarred and
  has no editor or later comment attached to 21.52 on that page.
- `source_transcription_checked: yes`.
- `active_scope_checked: yes`.
- Exact target retained: every finite nonabelian simple \(L\), every one
  involution class \(D\), every permutation preserving each exact product order.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`;
  the assignment explicitly prohibited web use.
- Exclusions retained: no Problem 21.53, no union of classes, no uncoloured graph,
  no conjugacy-class refinement, and no family-to-universal inference.
- No mathematical computation or web access was used.

## Minute-12 hard gate

The gate fired early.  A rank-two vertex is not a bare flag
\((A,K)=(\operatorname{im}N,\ker N)\), but a decorated flag
\((A,K,\phi_N)\) with \(\phi_N:V/K\simeq A\); every flag has six decorations.

For \(g=(I+N)(I+M)\), \(W=\operatorname{im}N+\operatorname{im}M\),
\(h=g|_W\), \(m=|h|\), and block extension \(c\), the exact formula obtained is

\[
|g|=m\ \text{or}\ 2m
\]

according as \((I+h+\cdots+h^{m-1})c\) vanishes or not.  In the transverse
case the small operator is

\[
h=\begin{pmatrix}I+pq&p\\q&I\end{pmatrix},
\qquad p=N|_{\operatorname{im}M},\quad
q=M|_{\operatorname{im}N}.
\]

Bare flag incidence fixes the ranks of \(p,q\), but not their compositions.
With both bare flags fixed, decorations give exact colours \(3,5,6\).  Also,
colour two is \(NM=MN\), and an explicit pair has \(NM=MN\ne0\), so it is
strictly coarser than mutual flag incidence \(NM=MN=0\).

Decision: hard-kill the direct rank-one flag/clique reconstruction.  Preserve
the exact obstruction as a `PARTIAL_RESULT`; do not start the materially different
six-fibre quotient strategy without a new Lead decision.

Full derivation: `Agents/Kourovka/problems/21.52/psln2-rank2-nilpotent-incidence.md`.
