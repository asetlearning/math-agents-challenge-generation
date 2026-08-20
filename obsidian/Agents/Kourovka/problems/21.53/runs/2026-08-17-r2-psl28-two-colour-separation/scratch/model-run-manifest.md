---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/finite-computation
  - project/kourovka
  - status/draft
---

# Frozen cheap-model manifest — PSL(2,8) product scheme

- frozen UTC: `2026-08-17T19:31:05Z`
- scope: `21.53/two-minimal-prime-colours`, assignment revision 2
- permitted target: only `PSL(2,8)` and its full involution class
- program: `scratch/build_psl28_scheme.py`
- program SHA-256: `f75ad5500924cef6164fc651273ac69d23be87b0ff8c678c28366055177c81ea`
- interpreter: CPython 3.12.3
- exact command from the run directory:

  `timeout 30s python3 scratch/build_psl28_scheme.py scratch/psl28-product-scheme.json`

- expected CPU: under 5 seconds; expected peak RAM: under 64 MiB; wall timeout: 30 seconds
- compute classification: cheap bounded construction (below the common-protocol heavy threshold); the Lead decision explicitly requires this colour-count gate before any leased automorphism-group comparison
- deterministic inputs: no seed, no package database, no network, no external group constants
- output schema: JSON object with full field tables, all 504 matrices, all 63 involutions, the checked conjugacy orbit and centralizer, all 1,953 triples `[i,j,order]`, the complete symmetric 63-by-63 product-order matrix, occurring colours, valencies, and edge counts
- assertions: exhaustive field triple checks; all 504-squared matrix products remain in the enumerated group; all inverses checked; one conjugacy orbit equals every enumerated involution; every pair order computed by repeated exact multiplication; uniform valency and pair/matrix consistency checks
- forbidden operation: this program does not compute any graph automorphism group or search for a separating permutation

The program and this manifest are frozen before execution. Any edit requires a new hash and a new manifest.
