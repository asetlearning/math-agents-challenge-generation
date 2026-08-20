---
from: Lead
to: Problem-21.53-Proof
type: DECISION
topic: Seek a uniform two-colour rigidity theorem for PSL(2,q)
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/verification/2026-08-17T205829Z-psl211-bounded-equality.md", "Agents/Kourovka/problems/21.53/verification/2026-08-17T201248Z-psl28-bounded-equality.md"]
needs_reply_by: 2026-08-17T22:03:08Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

## Ask

Run `PSL2Q-TWO-COLOUR-RIGIDITY` in a fresh ultra proof context for at most 60
active minutes, starting at cumulative minute 42.

## Exact bounded family target

Treat the simple groups `L=PSL(2,q)` for prime powers `q` in their complete
simple range, including the small exceptional isomorphisms rather than silently
discarding them. For each admissible `L`, `D` must be one complete conjugacy class
of involutions. Prove directly that the source's second-smallest distinct prime
divisor is `p=3`.

Construct a uniform projective, trace, or cross-ratio model for `D` and for the
exact order of every product `ab`. Determine the permutations preserving all
order-2 and order-3 edges and prove or refute that they preserve every occurring
product-order colour. Handle even and odd characteristic separately, as well as
any empty 2- or 3-edge relation under the source's vacuous `Aut_t` convention.

The desired success is a reconstructible theorem for this whole family. If the
family statement fails, an exception closes the universal source problem only
with an explicit admissible `q`, full product-order colouring, and one permutation
exhaustively preserving the 2/3 relations while changing a displayed other colour.
No broad finite-q catalogue enumeration; small exact calculations may only audit a
symbolic claim. Heavy computation requires a frozen manifest and Lead lease.

Report active time and return unused minutes. Do not self-park the universal
problem; equality for this family would remain partial progress outside `PSL(2,q)`.
