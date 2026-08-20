---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
validator: Validator-21.53-PSL211
freeze_revision: 1
frozen_utc: 2026-08-17T20:57:46Z
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen quiet-wrapper transcript audit

Dreadnaut command-line option `-o a` sets rather than clears generator output, so
the first concise-transcript attempt still printed generators. These two wrappers
issue the documented dreadnaut command `-a` and then read the **unchanged frozen
input**. This affects output verbosity only. It does not alter the graph,
partition, algorithm, or group computation.

## Commands

```bash
timeout 60s dreadnaut < Agents/Kourovka/problems/21.53/verification/scratch/psl211/two_relations_quiet.dre
timeout 60s dreadnaut < Agents/Kourovka/problems/21.53/verification/scratch/psl211/full_colours_quiet.dre
```

Exactly one invocation each. Expected below 10 CPU seconds and 256 MiB; no heavy
lease required. No retry after timeout.

## Hash chain

| file | SHA-256 |
|---|---|
| `two_relations_quiet.dre` | `e753024b890b7de2a087116a6179e078cbc1549e96dd4e81f974d0767be80878` |
| underlying `two_relations.dre` | `ddb8f7a97b5065c99b056b6abc40d13c137c3982b8cb28c1f165802ff8ac9b4b` |
| `full_colours_quiet.dre` | `c407a06de69c2c085ffcfd95c93d9697373d8074bda19ce9c72323484129f362` |
| underlying `full_colours.dre` | `ea6abf00ed463527105d8bde521f3d7f53579b53c25663504b27d3ee56c3e8d7` |

The wrapper does not hide warnings, partition acceptance, search statistics,
group order, or exit status; it suppresses only explicit generator cycles.
