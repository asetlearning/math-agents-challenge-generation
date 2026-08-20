---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
validator: Validator-21.53-PSL211
freeze_revision: 1
frozen_utc: 2026-08-17T20:53:18Z
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen independent-model verification manifest

This manifest was frozen before either checker was executed. Neither checker
imports, calls, or copies claimant code. The Python checker independently builds
`SL(2,11)/{+-I}`, proves the concrete simplicity certificate by normal closures,
reconstructs the full product-order matrix, compares immutable claimant data, and
emits but does not execute two dreadnaut inputs. The GAP checker independently
constructs the projective-line permutation action from `x -> x+1` and
`x -> -1/x`.

## Commands

Exactly one invocation of each is authorized:

```bash
timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/psl211_independent_validator.py
timeout 30s gap -q Agents/Kourovka/problems/21.53/verification/scratch/psl211_projective_gap_crosscheck.g
```

Expected for each: below 10 CPU seconds, below 256 MiB RAM, one process. These are
bounded non-heavy checks, so no compute-slot lease is required. If either reaches
its timeout or the heavy-job threshold, there is no repair or retry; Validator
must freeze a new manifest and request a Lead lease first.

## Frozen hashes

| file | SHA-256 |
|---|---|
| `psl211_independent_validator.py` | `61c0c3f45ffe397526bd13ad008e04f94502fb4981b62b645768dcc87032eeb5` |
| `psl211_projective_gap_crosscheck.g` | `7ec608bbd51221aa32c0abe9879499620ec3a71510195b29a49a8428527a4f85` |

The subsequently emitted dreadnaut inputs will receive a separate immutable
pre-execution manifest containing their exact hashes, sizes, commands, and bounds.
