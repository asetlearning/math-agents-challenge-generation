---
title: "Run log — v3 exact-only coverage correction"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Run log

## Active-time ledger

- Entered at global cumulative 12 active minutes after Lead required no
  conceptual change beyond expected coverage 57.
- `2026-08-17T15:01:20Z` — START exact-only corrective freeze.
- `2026-08-17T15:04:28Z` — STOP, global cumulative 16 active minutes (rounded
  up). Full script, runner, hashes, manifest, persistent outputs, coverage,
  timeout, and resource bounds frozen. Awaiting fresh Lead lease.

No v3 GAP call or mathematical probe has been run.

## Leased v3 run and outcome

- `2026-08-17T15:08:27Z` — START, global cumulative 16 active minutes. Lead
  matched both frozen hashes; the exact runner was invoked once.
- The runner completed after about 14.2 seconds with exit status zero, empty
  stderr, and 57/57 group rows. The target is `[168,42]`, its exact set is
  `[2,3,4,7]`, and there are zero nonisomorphic collisions.
- Slot 1 release report was written immediately after artifact inspection.
- `2026-08-17T15:12:00Z` — STOP, global cumulative 20 active minutes (rounded
  up). The fixed-target `PARTIAL_RESULT` package is complete and the named
  order-168 collision strategy has met its bounded-negative gate. State:
  `awaiting_lead`; no replacement strategy started.
