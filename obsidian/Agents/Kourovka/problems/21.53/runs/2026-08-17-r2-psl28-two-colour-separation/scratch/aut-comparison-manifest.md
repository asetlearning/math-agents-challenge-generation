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

# Frozen leased manifest — `Aut_2 intersect Aut_3` versus every colour

- frozen UTC: `2026-08-17T19:35:14Z`
- scope: `21.53/two-minimal-prime-colours`, assignment revision 2
- sole object: the 63-element involution class in the exact `PSL(2,8)` model
- input: `scratch/psl28-product-scheme.json`
- input SHA-256: `54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90`
- wrapper: `scratch/compare_colour_groups.py`
- wrapper SHA-256: `70ca1991ff26db9dc765049bb3b22e604efe7e5130db3946444d5f7f3e7409e4`
- exact command from the run directory:

  `timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison`

- software: CPython 3.12.3; GAP 4.12.1 (`/usr/bin/gap` SHA-256 `9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3`); GRAPE 4.9.0; nauty/dreadnaut 2.8.8+ds-5 (`/usr/bin/dreadnaut` SHA-256 `b8ab2d4aaf12343ac40e68929a0e62092be47d0154cbaf660b26cbf8ecec512f`)
- platform: Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
- wall timeout: 300 seconds outside, 270 seconds for the GAP subprocess
- resource estimate: at most 120 CPU seconds, at most 512 MiB RAM, one heavy slot for 5 minutes
- determinism: no seed, network, catalogue, or external group database

## Exact incidence encoding

The 63 original vertices form their own fixed vertex-colour cell. For each unordered pair of a selected product order, add one new degree-two incidence vertex adjacent exactly to the two endpoints. Incidence vertices belonging to different product orders occupy distinct fixed vertex-colour cells.

- Two-colour graph: original cell plus 189 order-2 incidence vertices and 252 order-3 incidence vertices; 504 vertices total.
- Full-colour graph: original cell plus the order-2, order-3, 756 order-7, and 756 order-9 incidence cells; 2,016 vertices total.

Because each incidence vertex is uniquely determined by its endpoint pair and its colour cell, restriction to the original 63 vertices is faithful and gives exactly, respectively, `Aut_2(Gamma) intersect Aut_3(Gamma)` and the full product-order colour group. Both 2 and 3 occur, so neither defining factor is vacuous in this pair. The wrapper checks every returned two-colour generator against all defining 2/3 edges and every full-colour generator against all 1,953 colours before comparing groups.

## Output schema and strict-inequality gate

The command writes the generated GAP program, raw GAP output, and a summary JSON containing both group orders, generators as explicit 63-entry image lists, subgroup/equality flags, and input/output hashes. If containment is strict, it selects a generator outside the full group, checks that 63-entry list is a permutation, exhaustively checks all 189 order-2 edges and all 252 order-3 edges, and emits a six-entry changed edge `[i,j,old_order,image_i,image_j,new_order]` plus the four endpoint matrices. A strict result is unusable unless all these assertions pass. An equality result is bounded evidence for this fixed pair only.

The input, wrapper, command, resources, timeout, and schema are frozen. Do not execute before Lead records a lease.
