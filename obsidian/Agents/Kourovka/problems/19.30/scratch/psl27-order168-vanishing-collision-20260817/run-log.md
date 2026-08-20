---
title: "Run log — PSL(2,7), order-168 vanishing-set collision screen"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Run log

## Active-time ledger

- `2026-08-17T14:43:13Z` — START, cumulative 0 minutes. Read the required
  protocol, role file, current Lead decision, canonical scope, and its explicit
  reviewed reference; no solution-bearing history or web resource opened.
- `2026-08-17T14:50:47Z` — STOP, cumulative 8 active minutes (rounded up).
  Complete manifest, script, runner, output paths, coverage assertion, resource
  estimate, and hashes frozen. Awaiting Lead compute lease; waiting time is not
  charged.

## Freeze checkpoint

The fixed strategy is `PSL27-ORDER168-VANISHING-COLLISION`. The immutable run
manifest is `manifest.md` in this directory. No GAP invocation or mathematical
computation has been run. The next permitted action is the exact command in the
manifest, and only after a Lead lease is received.

## First leased run

- `2026-08-17T14:56:21Z` — START, cumulative 8 active minutes. Lead-matched
  hashes checked immediately before the exact frozen runner.
- The one permitted run exited after about 1.5 seconds with status 2. Its first
  mathematical row was `NumberSmallGroups(168)=57`, so the frozen `42` guard
  aborted before target construction or enumeration. Completed coverage: 0/57;
  no target set or collision result exists.
- `2026-08-17T14:57:01Z` — slot-release report written to Lead. No rerun.
- `2026-08-17T14:59:27Z` — STOP, cumulative 12 active minutes (rounded up),
  after freezing a distinct corrected v2 run from the sanctioned coverage row.
