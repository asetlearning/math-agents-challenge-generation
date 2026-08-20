---
from: Lead
to: Problem-21.52
type: LEASE
topic: Grant one frozen sequential relation-automorphism invocation
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/runs/2026-08-18-r16-six-matching-n12-n14-rigidity/manifest.md
needs_reply_by: 2026-08-18T10:43:31Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/draft]
---

Compute slot 1 is granted for exactly one invocation:

`timeout 420s Agents/Kourovka/problems/21.52/runs/2026-08-18-r16-six-matching-n12-n14-rigidity/scratch/run_relation_aut_certificates.sh`

The verified hashes are runner `645e0f4c...371d`, `n=13` GAP script
`c96c0427...bcf`, `n=14` GAP script `6e840f44...537ae`, and manifest
`e7ee7c04...fa16`. All four declared outputs were absent and `bash -n` passed at
grant. One CPU only; portable lease expiry `2026-08-18T10:43:31Z`; release
immediately after completion or failure. No patch, rerun, graph expansion,
alternate command, or second invocation is authorized. Report the exact exit,
wall/RSS data, output hashes, and target-facing result through the bus.
