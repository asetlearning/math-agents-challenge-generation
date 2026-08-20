---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
validator: Validator-21.53-PSL211
freeze_revision: 1
frozen_utc: 2026-08-17T20:54:54Z
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen dreadnaut incidence-comparison manifest

Frozen after the exact matrix reconstruction and before any automorphism
computation. Inputs were emitted by the independently frozen revision-2 Python
checker. They do not use the claimant's GAP/GRAPE graph code.

## Exact semantics

In each input, vertices `0..54` are one distinguished partition cell representing
the 55 involutions. Every encoded unordered pair receives one new degree-two
incidence vertex adjacent to exactly its two endpoints. Incidence vertices for
different product-order relations lie in separate partition cells.

- `two_relations.dre` has cells of sizes `55,165,330`, representing points,
  colour-2 edges, and colour-3 edges. It has 550 vertices and 990 graph edges.
- `full_colours.dre` has cells of sizes `55,165,330,660,330`, representing points
  and colours `2,3,5,6`. It has 1540 vertices and 2970 graph edges.

Restriction to the first cell is faithful because every incidence vertex is
uniquely determined by its two neighbours and its relation cell. Conversely every
permutation of the 55 points preserving each encoded relation extends uniquely to
the incidence vertices. Thus the two dreadnaut group orders are exactly the orders
of `Aut_2 intersect Aut_3` and `Aut(Gamma)`, respectively.

## Commands

Exactly one invocation of each is authorized:

```bash
timeout 60s dreadnaut < Agents/Kourovka/problems/21.53/verification/scratch/psl211/two_relations.dre
timeout 60s dreadnaut < Agents/Kourovka/problems/21.53/verification/scratch/psl211/full_colours.dre
```

Tool: nauty/dreadnaut 2.8.8. Expected for each: below 10 CPU seconds and below
256 MiB RAM. These are bounded non-heavy computations; no slot lease is required.
If either reaches 60 seconds or the heavy threshold, no retry or tuning is
authorized without a new frozen manifest and Lead lease.

## Frozen hashes and sizes

| file | lines | bytes | SHA-256 |
|---|---:|---:|---|
| `two_relations.dre` | 501 | 5756 | `ddb8f7a97b5065c99b056b6abc40d13c137c3982b8cb28c1f165802ff8ac9b4b` |
| `full_colours.dre` | 1491 | 17836 | `ea6abf00ed463527105d8bde521f3d7f53579b53c25663504b27d3ee56c3e8d7` |
| `independent_summary.json` | not an executable input | not applicable | `d8751582a5df6a9bca26dd50ff6e178fd8a6a77ed7f450c0eba32c6e0d2cb046` |
