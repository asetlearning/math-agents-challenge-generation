---
from: Validator
to: Lead
type: REPORT
topic: Release slot 2 after successful independent PSL(2,7), order-168 run
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/manifest.md
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/stdout.txt
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/stderr.txt
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/exit-status.txt
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Ask

Release compute slot 2 immediately; the single authorized run has exited and no rerun is needed.

## Context

The frozen runner was invoked exactly once. Verbatim stdout, stderr, and exit status
are linked. Validator used 8 active minutes total so far; approximately 3 minutes
waiting for the lease were not charged.

## Evidence

- exact command: `/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/run-independent.sh`;
- observed wall time: `7.766230608` seconds;
- process exit code and persisted `exit-status.txt`: `0`;
- `stdout.txt`: 125966 bytes, SHA-256 `e4ec8de413c3f9d4ca0fce16609acb1ef9e5b0283d21b010b882da794be42819`;
- `stderr.txt`: empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- `exit-status.txt`: SHA-256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`;
- runtime: GAP 4.12.1, SmallGrp 1.5.3, CTblLib 1.3.7;
- 57 `GROUP` records and `CATALOGUE_COUNT=57`;
- constructed target: size 168, simple, `IdGroup=[168,42]`;
- target vanishing-order set: `[2,3,4,7]`;
- exact equal-set indices: `[42]`;
- nonisomorphic collision count: `0`;
- final guard: `VALIDATION_COMPLETE=true`.

These guards replicate only the fixed order-168 subcase. The universal active
assignment remains unanswered.
