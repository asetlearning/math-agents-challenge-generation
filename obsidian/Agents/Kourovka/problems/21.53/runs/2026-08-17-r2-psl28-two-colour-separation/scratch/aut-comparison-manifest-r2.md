---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/graph-automorphisms
  - project/kourovka
  - status/draft
---

# Frozen leased manifest revision 2 — `Aut_2 intersect Aut_3` versus every colour

- frozen UTC: `2026-08-17T19:46:48Z`
- manifest revision: 2
- scope: `21.53/two-minimal-prime-colours`, assignment revision 2
- sole object: the same 63-element involution class in the exact `PSL(2,8)` model
- input: `scratch/psl28-product-scheme.json`
- input SHA-256: `54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90`
- wrapper: `scratch/compare_colour_groups.py`
- repaired wrapper SHA-256: `3f96ab5def2a55fe273191e1abf9e99235705f095f01f08640e944eb8d5f6ff0`
- superseded wrapper SHA-256: `70ca1991ff26db9dc765049bb3b22e604efe7e5130db3946444d5f7f3e7409e4`
- exact revision-2 command from the run directory:

  `timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison-r2`

- new output paths: `scratch/aut-comparison-r2.generated.g`, `scratch/aut-comparison-r2.raw.txt`, and `scratch/aut-comparison-r2.summary.json`; the failed revision-1 artifacts are never overwritten
- software: CPython 3.12.3; GAP 4.12.1 (`/usr/bin/gap` SHA-256 `9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3`); GRAPE 4.9.0; nauty/dreadnaut 2.8.8+ds-5 (`/usr/bin/dreadnaut` SHA-256 `b8ab2d4aaf12343ac40e68929a0e62092be47d0154cbaf660b26cbf8ecec512f`)
- platform: Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
- wall timeout: 300 seconds outside, 270 seconds for the GAP subprocess
- resource estimate: at most 120 CPU seconds, at most 512 MiB RAM, one heavy slot for 5 minutes
- determinism: no seed, network, catalogue, or external group database

## Authorized repair audit

The sole source change replaces the fourteen Python string escapes `\n` in the generated GAP `Print` block by `\\n`, so the generated GAP program receives a backslash followed by `n` instead of a literal newline inside its string token. Static Python parsing passes. The wrapper remains 294 lines; its byte length increased from 10,958 to 10,972, exactly one additional backslash for each of the fourteen repaired occurrences. No object construction, incidence edge, colour cell, group comparison, parser requirement, resource bound, or certificate assertion changed.

## Exact incidence encoding

The 63 original vertices form their own fixed vertex-colour cell. For each unordered pair of a selected product order, add one new degree-two incidence vertex adjacent exactly to the two endpoints. Incidence vertices belonging to different product orders occupy distinct fixed vertex-colour cells.

- Two-colour graph: original cell plus 189 order-2 incidence vertices and 252 order-3 incidence vertices; 504 vertices total.
- Full-colour graph: original cell plus the order-2, order-3, 756 order-7, and 756 order-9 incidence cells; 2,016 vertices total.

Because each incidence vertex is uniquely determined by its endpoint pair and colour cell, restriction to the original 63 vertices is faithful and gives exactly, respectively, `Aut_2(Gamma) intersect Aut_3(Gamma)` and the full product-order colour group. Both defining colours occur, so neither `Aut_2` nor `Aut_3` is vacuous here. The wrapper checks every returned two-colour generator on the 2/3 relations and every full-colour generator on all 1,953 pair colours before comparing the groups.

## Output schema and strict-inequality gate

The command must create all three new output files. The summary JSON must contain both group orders, explicit generators as 63-entry image lists, subgroup/equality flags, input/wrapper/generated/raw hashes, the incidence vertex counts, and relation-edge counts. If containment is strict, it must also contain one generator outside the full group, checked as a permutation of all 63 vertices, exhaustive success on all 189 order-2 edges and all 252 order-3 edges, and a six-entry changed edge `[i,j,old_order,image_i,image_j,new_order]` with all four endpoint matrices. A strict result is unusable unless every assertion and direct certificate passes. Equality is bounded evidence for this fixed pair only.

The fixed input, repaired wrapper, new output names, exact command, resources, timeout, and certificate schema are frozen. Do not execute before Lead records a fresh lease.
