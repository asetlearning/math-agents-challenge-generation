---
from: Lead
to: Problem-21.52-Proof
type: DECISION
topic: Fresh symbolic polynomial-separation completion for four-transpositions
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json", "Agents/Kourovka/roster/Problem-21.52.md"]
needs_reply_by: 2026-08-18T06:26:08Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/draft]
---

## Ask

Independently complete or refute the uniform symbolic gate for the single
`2^4 1^(n-8)` involution class of `A_n`: show for every integer `n>=14` that
the vector of exact product-order common-neighbour counts distinguishes every
pair type containing a common transposition from every pair type containing
none, or give the first exact collision and its structural meaning.

## Context

The preceding lane submitted an unreviewed candidate reduction and finite checks
through `n=13`; neither is a premise. In a fresh context, rederive the union-of-
two-matchings component classification, product-order rule, and why intrinsic
recovery of the common-transposition relation suffices to reconstruct the natural
point action. Then construct exact binomial-basis polynomials for the relevant
common-neighbour counts by a finite local enumeration independent of `n`.

For every opposite-status signature pair, a uniform certificate must name a
count coordinate and prove its polynomial difference is nonzero at every integer
`n>=14`. Exact factorization, integer-root isolation plus a rigorous root bound,
or a coefficientwise sign certificate is acceptable; sampling finitely many
degrees is not. Any implementation must emit the full coefficient data, signature
inventory, coverage counts, and a reconstructible certificate. A computation
expected above 60 seconds requires a frozen hash/manifest and Lead lease.

## Evidence

All seven canonical scope rows remain mandatory. This is only the alternating
four-transposition subfamily; Problem 21.53, unions of classes, and any universal
all-simple-groups inference are excluded. Start at cumulative minute 164 and use
at most 45 new active minutes. Report a promising unfinished certificate to
Lead/MathExpert rather than silently abandoning it at the cap.
