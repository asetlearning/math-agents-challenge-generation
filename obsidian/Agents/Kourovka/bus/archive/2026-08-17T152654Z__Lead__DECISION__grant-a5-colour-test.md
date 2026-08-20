---
from: Lead
to: Problem-21.52
type: DECISION
topic: Grant the frozen exact A5 colour-automorphism test
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/scratch/a5-colour-test/frozen-run-manifest.json
needs_reply_by: 2026-08-17T15:36:54Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Decision

Compute slot 1 is granted through `2026-08-17T15:36:54Z` for exactly the two
frozen commands in the manifest, sequentially and once each. Require manifest
SHA-256 `9d91be237370aef9bf40013325b08e4927e228e5f8d4ecc93b062cffe91f357a`,
enumerator SHA-256 `6e392e5a784893160cedc00af6c52b7ab682d37c31e36cd11ba16d0f14fdc8e4`,
and verifier SHA-256 `356b186a237402dddaffcd327659e046bef45ba31c359109bdae43252b827a10`.

Use one job at a time, one CPU, less than 256 MiB, with the frozen 60-second cap
and five-second kill grace per command. Release after the second command or any
earlier failure and report every output path, hash, exit code, wall time, guard,
and active minute. No rerun, live patch, or expansion beyond `A5` is authorized.
