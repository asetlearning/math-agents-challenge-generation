---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
validator: Validator-21.53-PSL211
freeze_revision: 2
frozen_utc: 2026-08-17T20:54:11Z
supersedes: [psl211-validation-model-frozen-manifest.md]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen independent-model verification manifest — revision 2

Revision 1 executed once and terminated on its assertion that the identity
conjugacy class would be enumerated first. Lexicographic representative order does
not imply that order. No result files or mathematical output were accepted from
that failed run.

The only revision sorts the already exhaustively enumerated class records by
`(element_order, representative)` and checks the multiset of normal-closure sizes.
No construction, multiplication, class enumeration, edge computation, expected
value, artifact comparison, or incidence encoding changed.

## Authorized retry

Exactly one invocation is authorized:

```bash
timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/psl211_independent_validator.py
```

Expected below 10 CPU seconds and 256 MiB. This is non-heavy. Timeout or threshold
crossing ends the route pending a fresh manifest and Lead lease.

## Hash

`psl211_independent_validator.py`:
`bd6277091db2b82f9c7eab89f144d6e7385a5b9ad03ba3766a35d93578aaace2`.

The unchanged GAP checker remains authorized exactly once by revision 1 and has
not yet been invoked.
