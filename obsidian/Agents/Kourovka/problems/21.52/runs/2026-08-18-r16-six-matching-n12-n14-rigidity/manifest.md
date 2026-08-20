---
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/draft]
---

# Frozen heavy-compute manifest — relation automorphisms for n=13,14

Frozen after two honest 60-second capped probes both timed out without mathematical output. Those failed probes are not evidence. No output below exists at freeze time.

## Frozen inputs

| file | lines | bytes | SHA-256 |
|---|---:|---:|---|
| `scratch/n13_exchange_aut.g` | 27 | 1155 | `c96c04274647baca29726ad8893a88646f156efc6214ef900cb87960e21dcbcf` |
| `scratch/perfect_matching_flip_aut.g` | 48 | 1484 | `6e840f4444db78d6e5c51e96b5ed8bfa20498dea3bb8cab3228f466b03f537ae` |
| `scratch/run_relation_aut_certificates.sh` | 26 | 906 | `645e0f4cb83098cc934fe4595acd4de2358c94fd85e3a2ae8fecac1a647a371d` |

Software: GAP `4.12.1`; GRAPE `4.9.0`; system GRAPE invokes nauty/dreadnaut.

## Exact single invocation requested

```bash
timeout 420s Agents/Kourovka/problems/21.52/runs/2026-08-18-r16-six-matching-n12-n14-rigidity/scratch/run_relation_aut_certificates.sh
```

The runner is fail-fast and performs exactly two sequential jobs, never simultaneously:

1. full automorphism group of the 135,135-vertex degree-12 five-common-edge graph on six-matchings of `K_13`, timeout 180 seconds;
2. full automorphism group of the 135,135-vertex degree-42 four-point flip graph on perfect matchings of `K_14`, timeout 180 seconds.

Each script constructs the labelled natural `S_n` action, checks its kernel is trivial, checks it is a subgroup of the full graph automorphism group, and tests exact permutation-group equality; the certificate is not group-order-only.

## Outputs absent at freeze

- `scratch/n13_exchange_aut.stdout`
- `scratch/n13_exchange_aut.stderr`
- `scratch/n14_flip_aut.stdout`
- `scratch/n14_flip_aut.stderr`

Estimated resources: one CPU; peak RAM below 512 MiB based on the capped probes (`302592` and `329728` KiB); expected total wall time 2--4 minutes, hard outer cap 420 seconds. Request one heavy slot for five minutes. No patch, rerun, expanded graph, or second invocation is authorized by this manifest.

