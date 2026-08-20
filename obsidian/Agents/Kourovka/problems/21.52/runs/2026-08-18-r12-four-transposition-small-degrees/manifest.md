---
title: "Cycle 12 exact-computation manifest"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/draft]
---

# Exact computation record

No invocation was expected to exceed 60 seconds or 1 GB, so no heavy-compute
lease was required. Every command had a 55-second timeout. Peak observed RSS was
177,228 KiB (aggregate certificate), and the largest individual elapsed time was
24.63 seconds (six-degree orbit batch).

## Software

- Python 3.12.3
- nauty/dreadnaut 2.8.8+ds-5
- GAP 4.12.1

## Frozen source hashes

| file | SHA-256 |
|---|---|
| `scratch/orbit_audit.py` | `408fbd54b00e598e56d1528e638b28e69b66e1ab9453ee5faca2e1f21cfe9892` |
| `scratch/matching_relation_dre.py` | `7ac92bd962ae99a57b9ed79b1e69a0a06168314945faea12ec2d6aee8045845f` |
| `scratch/certify_boundary.py` | `497f7590be6be9987646281e16e47f4169c268f6946095ec8b586b5c73b005c8` |
| `scratch/a8_outer_audit.g` | `3b30136f2a7c831a74a1991fa9d5b15a07a156dd8b07feedf2fa301a84100791` |

## Commands

Orbit audit, one bounded batch:

```bash
timeout 55s /usr/bin/time -f 'orbit-batch elapsed=%e rss_kb=%M' bash -c 'for n in 8 9 10 11 12 13; do python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/orbit_audit.py "$n" "Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/orbit-n${n}.json"; done'
```

Relation inputs, one bounded batch:

```bash
timeout 55s /usr/bin/time -f 'relation-input-batch elapsed=%e rss_kb=%M' bash -c 'for n in 8 9 10 11 12 13; do python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/matching_relation_dre.py "$n" "Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/relation-n${n}.dre"; done'
```

Full sparse-graph automorphism groups, one bounded batch:

```bash
timeout 55s /usr/bin/time -f 'dreadnaut-batch elapsed=%e rss_kb=%M' bash -c 'for n in 8 9 10 11 12 13; do dreadnaut < "Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/relation-n${n}.dre" > "Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/relation-n${n}.out" 2> "Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/relation-n${n}.err"; done'
```

Aggregate fail-fast certificate:

```bash
timeout 55s /usr/bin/time -f 'elapsed=%e rss_kb=%M' python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/certify_boundary.py Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/boundary-certificate.json
```

`A_8` automorphism/class audit:

```bash
timeout 55s gap -q Agents/Kourovka/problems/21.52/runs/2026-08-18-r12-four-transposition-small-degrees/scratch/a8_outer_audit.g
```

## Outputs

- `scratch/boundary-certificate.json`, SHA-256
  `1489748b454e07e738087b04e64e97ed7c96ca763914e3c0a46d1c8c5880ef91`.
- `scratch/certify_boundary.out`, SHA-256
  `4f72c264158595e2023caa62152addf32a7e1867cc270058634e860085076986`,
  contains `PASS degrees=8..13 all exact gates`.
- `scratch/a8_outer_audit.out`, SHA-256
  `858e2805cf0fc177b151a5a0a4667f2ba3cbf96223bb1fe7bc093324ebde7d8e`.
- Every nauty stderr file `scratch/relation-n8.err` through
  `scratch/relation-n13.err` is empty.
- Exact per-degree hashes of all six orbit JSON files, all six complete
  dreadnaut inputs, and all six complete dreadnaut outputs are embedded in
  `scratch/boundary-certificate.json`.

## Observed resource lines

```text
orbit-batch elapsed=24.63 rss_kb=82048
relation-input-batch elapsed=21.35 rss_kb=68376
dreadnaut-batch elapsed=6.46 rss_kb=101760
certificate elapsed=9.19 rss_kb=177228
A8 GAP elapsed=2.38 rss_kb=141952
```
