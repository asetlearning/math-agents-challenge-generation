---
title: "Frozen Validator manifest v2 — A6 order-360 mechanical retry"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
frozen_utc: 2026-08-17T16:34:31Z
supersedes_manifest: Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/manifest.md
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Frozen Validator manifest v2

V1 and every V1 output artifact remain untouched. Lead authorized exactly one
fresh mechanical freeze/request after V1 failed closed. No mathematical
computation occurred while preparing V2; only file copying through `apply_patch`,
the authorized one-expression API correction, advanced output paths, addition of
GAP `--quitonbreak`, `bash -n`, hashes, and a static diff were performed.

## Frozen files and hashes

| file | SHA-256 |
|---|---|
| `independent-a6-order360-v2.g` | `49ba1996a27cdf69c39bc2481ace2df59e43436bfc7c71e1a9a9659bb11c1ed9` |
| reused V1 `verify-independent.py` | `8bb3fb2b7924ec41e98c701f6a9b802cf7d39bc5d0e178394ef0cf6510c89109` |
| `run-independent-v2.sh` | `27ac0709d5492b6590e2ac71a86bcaa0db41b20a0f88fc22604e5617f026b88c` |
| `v1-to-v2.diff` | `cba7b3b77ef9753790130d52a3fd7cbd6cb0110567b1eeda78936fd488ab386e` |
| `frozen-v2.sha256` | `e96fb99703d771181bbaf0bb046a319dd5b3fb9b92fa2ae222fb7e9375edbf82` |

The V2 runner verifies the first four hashes, including its own, before launch.

## Mechanical diff only

The complete frozen diff is `v1-to-v2.diff`. Its only GAP-source change is:

```diff
- character -> UnderlyingCharacteristic(character) = 0
+ character -> UnderlyingCharacteristic(UnderlyingCharacterTable(character)) = 0
```

This retains the existing table-level characteristic-zero guard and queries the
characteristic through each character's underlying table, as supported by GAP
4.12.1. The runner changes only its V2 directory/script/output names, reuses the
identically hashed V1 Python checker, and invokes GAP with `--quitonbreak` so a GAP
error becomes a nonzero stage exit. There is no conceptual, coverage, invariant,
target, parser, resource, or acceptance-criterion change.

## Exact command and limits

Run once from the vault root only under a fresh Lead lease:

```bash
/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-v2-20260817/run-independent-v2.sh
```

- one GAP process and one CPU;
- 870 CPU-second limit inside the runner;
- 2 GiB virtual-memory ceiling;
- 960-second outer wall cap plus 30-second kill grace;
- expected wall time 1–3 minutes;
- requested lease duration 18 minutes including inspection and release.

Any nonzero stage exit, absent completion marker, target/coverage discrepancy,
parser failure, or row disagreement remains a failed result. Even a full pass is
only fixed-`A6` evidence and requires `active_assignment_answered:no`.
