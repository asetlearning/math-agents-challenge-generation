---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
run: 2026-08-17-r3-psl211-two-colour-separation
freeze_revision: 1
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen PSL(2,11) automorphism-comparison manifest

Frozen before any automorphism computation. The discovery model is
`SL(2,11)/{+I,-I}`, with each central pair represented by the lexicographically
smaller tuple `(a00,a01,a10,a11)` in `{0,...,10}^4`.

## Pre-comparison matrix facts

- Quotient order: 660 = 2^2 * 3 * 5 * 11; hence the required second-smallest
  distinct prime is `p=3`.
- Direct class enumeration gives eight conjugacy classes and one involution class,
  of size 55 and centralizer order 12. Every one of the 55 quotient involutions is
  in this class.
- The full 55 by 55 matrix (diagonal 1, all 1,485 unordered off-diagonal entries)
  has exactly the colours `2,3,5,6`, with valencies `6,12,24,12` and edge counts
  `165,330,660,330`, respectively.
- The four-colour gate therefore requires a Lead lease before comparison.

## Frozen command

```bash
timeout 120s gap -q Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/compare_aut_groups.g
```

Expected resources: at most 30 CPU seconds, at most 512 MB RAM. Requested lease:
one compute slot for five wall-clock minutes. Exactly one invocation; no repair,
rerun, or target expansion without a new freeze and lease.

The GAP 4.12.1 / GRAPE 4.9.0 script constructs one graph for each frozen colour,
computes the individual colour automorphism groups, intersects colours 2 and 3,
then intersects all four colours. If containment is strict, it must print an
explicit generator outside the full-colour group, its complete 55-entry image
list, exhaustive colour-2 and colour-3 checks, and one changed other-colour edge.

## SHA-256

| file | sha256 |
|---|---|
| `build_psl211_matrix.py` | `35de58e18081fdd9fb5ae1bfbbce702108074564ce75c2b85f203bb142afb887` |
| `vertices.tsv` | `9c5f091980d4d8cb31c592f42d9cc8af92aee0747a3851b9122ccfff999942b0` |
| `unordered_edges.tsv` | `587f24029567ab255a6ced078e066c9e6307e613acd6a7530165214c76f97f2a` |
| `product_order_matrix.csv` | `8c37e927915a312ac4962d4cd762347102059d78ec53965da1ec9ec95829c74e` |
| `matrix_data.g` | `4a0001b7bfc6e77a3a93d8d6cd490a73b106c301447376f1e19ac980968d0bf6` |
| `summary.json` | `540dc07722c94806142734153d48bf329a5ab4af1cf0f14746bb4b5229fb151a` |
| `compare_aut_groups.g` | `34a946f10ef13758c1309dd2ff63004fdcedc921c586ba2c7caf8ce38ff5ab4b` |

