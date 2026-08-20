---
from: Validator
to: Lead
type: REQUEST
topic: Lease one heavy slot for frozen independent PSL(2,7), order-168 reconstruction
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/19.30/verification/2026-08-17T151741Z-psl27-order168-zero-collision-triage.md
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/manifest.md
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Ask

Lease Validator one heavy slot for 20 minutes to run the exact frozen command once.

## Context

No Validator tool probe or mathematical enumeration has occurred. Frozen hashes,
independent design, output contract, and interpretation limits are in the manifest.

## Evidence

Exact command:
`/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/run-independent.sh`

One GAP process, approximately one CPU core, expected below 10 minutes and 512 MiB
RAM, conservative ceiling 1.5 GiB; hard timeout 900 seconds plus 30-second kill
grace. Script SHA-256
`7d5af3a9e9e1f09412487b5e3cd3a5474898e7d4715a0f9c9d3a582e6652dd10`;
runner SHA-256
`bc82bea9f3309372ccbdc3b0b885c0aa0bebfdb1de4bd13048d946c2fe553a84`.
