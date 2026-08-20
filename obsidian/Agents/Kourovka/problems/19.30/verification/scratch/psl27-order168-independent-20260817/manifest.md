---
title: "Frozen Validator manifest — PSL(2,7), order-168 independent reconstruction"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
frozen_utc: 2026-08-17T15:21:18Z
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Frozen Validator manifest

No Validator GAP/tool probe or mathematical enumeration preceded this freeze. The
claimant's `screen-v3.g` was not opened, copied, or reused. This checker was written
from the rendered source definition, canonical scope, and requested fixed-target
statement.

## Frozen files and hashes

| file | SHA-256 |
|---|---|
| `independent-order168.g` | `7d5af3a9e9e1f09412487b5e3cd3a5474898e7d4715a0f9c9d3a582e6652dd10` |
| `run-independent.sh` | `bc82bea9f3309372ccbdc3b0b885c0aa0bebfdb1de4bd13048d946c2fe553a84` |

## Independent design

The implementation constructs `PSL(2,7)` and all installed SmallGroups
representatives of order 168. For each group it obtains a group character table,
converts every irreducible character to a value row with
`ValuesOfClassFunction`, scans the transposed class columns for exact zeros, and
forms the set of the aligned class-representative orders. It independently checks
class-size sums, degree-square sums, all catalogue identifiers, target size,
simplicity, identifier, and target-to-catalogue isomorphism. It derives the target
index from `IdGroup(PSL(2,7))`, while also checking the requested value `[168,42]`.

The output persists class orders, class sizes, irreducible degrees, all zero-row
indices by class, vanishing-class positions, and the vanishing-order set for each
of the 57 representatives. The final guards require target set `[2,3,4,7]`, exact
set-equality indices `[42]`, and zero nonisomorphic collisions.

## Exact command and cap

Run once from the vault root, only under a current Lead lease:

```bash
/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/run-independent.sh
```

The runner invokes exactly one `/usr/bin/gap -q` process through
`/usr/bin/timeout --signal=TERM --kill-after=30s 900s`. It persists verbatim stdout,
stderr, and the exit status in this directory. Any timeout, nonzero status, GAP
error, missing `VALIDATION_COMPLETE true`, catalogue count other than 57, or failed
guard is not a result.

## Resources and requested lease

- heavy slots: one;
- processes: one GAP process plus the timeout wrapper;
- CPU: approximately one core;
- expected wall/CPU time: below 10 minutes;
- hard wall cap: 900 seconds plus 30-second termination grace;
- expected RAM: below 512 MiB, conservative ceiling 1.5 GiB;
- requested lease duration: 20 minutes, including output inspection and release.

The run may establish independent computational replication of the fixed finite
subcase only. It cannot establish the universal active assignment and does not
independently certify GAP's SmallGroups catalogue or character algorithms.
