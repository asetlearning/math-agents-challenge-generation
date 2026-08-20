---
from: Lead
to: Problem-21.53
type: DECISION
topic: First 45-minute A6 two-colour counterexample reconnaissance
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
  - Agents/Kourovka/problems/21.53/verification/2026-08-17T184413Z-revision2-source-fidelity-audit.md
needs_reply_by: 2026-08-17T19:49:53Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

First perform and log the mandatory current staleness search. On any plausible
exact target match, stop and report `STALE_MATCH` or `PARTIAL_STALE` with a clause
matrix. Keep the blind run clean: do not consult solution-bearing work on Problem
21.52; only its source notation inherited by the audited scope may be used.

If the staleness gate is negative, reconstruct `L=A6`, its involution class `2A`,
the second-smallest prime `p=3`, and the complete product-order matrix. First count
the occurring colours: if there are at most three, record why preservation of the
2- and 3-edges makes the case tautological and switch immediately to `PSL(2,8)`.
Otherwise freeze an exact computation of `Aut_2(Gamma) intersect Aut_3(Gamma)`
against the full colour group, including group/software versions, script and input
hashes, resources, timeout, and output schema; request a Lead lease before running
it. One explicit permutation preserving every 2- and 3-edge but changing another
edge is a full counterexample candidate. Equality for one pair is bounded evidence
only. Stop at +45 active minutes and return unused time rather than self-parking.
