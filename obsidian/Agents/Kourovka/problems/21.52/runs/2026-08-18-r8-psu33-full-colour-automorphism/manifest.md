---
title: "PSU(3,3) full-colour frozen run manifest"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
---

# Frozen run manifest

Frozen at 2026-08-18T04:31Z. Exactly one invocation is requested.

## Inputs

- Exact group: installed GAP primitive-library object `PrimitiveGroup(28,4)`, checked by exact isomorphism against the separate constructor `PSU(3,3)`.
- Checker: `Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_checker.g`
- Checker SHA-256: `86e2633dff9c8f5ec25c3ee7beb5ce21b8e2e3a957e26f550874b3e154843208`
- Checker size: 215 lines, 9024 bytes.
- Runner: `Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_run.sh`
- Runner SHA-256: `fc2fccac609c076e15d6168110e2f69f6340893e9b0d9c2e03d91970eee572e0`
- Runner size: 68 lines, 2459 bytes; `bash -n` passed, and a light `gap --quitonbreak -q -b -c 'QUIT;'` option check exited zero.

## Exact command

```text
bash Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_run.sh
```

The runner itself invokes exactly:

```text
/usr/bin/time -v -o <resource-path> timeout --signal=TERM --kill-after=10s 900s gap --quitonbreak -q -b <checker> > <stdout-path> 2> <stderr-path>
```

No rerun, patch, expanded class, alternate group, or second heavy command is requested.

## Bounds and lease

- Requested lease: 20 wall-clock minutes.
- Hard process cap: 900 seconds, then TERM, then forced kill after 10 seconds.
- Estimate: one CPU core and less than 1 GB RAM.
- Largest exact graph: 2016 vertices and 3906 undirected incidence edges.
- Finite group: order 6048; involution class: 63 vertices; complete colouring: 1953 edges.

## Outputs and preflight state

All paths are below the clean run directory. At freeze time every listed output was absent:

- `scratch/psu33-full-colour-stdout.txt`
- `scratch/psu33-full-colour-stderr.txt`
- `scratch/psu33-full-colour-resource.txt`
- `scratch/psu33-full-colour-output.txt`
- `scratch/psu33-colour-matrix.g`
- `scratch/psu33-full-colour-certificate.g`

The preliminary, non-heavy inventory output is separately present as `scratch/psu33-inventory-output.txt` and is not overwritten.

## Fail-fast and acceptance gates

Before running, the runner rejects a checker-hash mismatch or any pre-existing listed output. GAP is invoked with `--quitonbreak`. The runner then rejects nonzero exit, timeout, nonempty stderr, missing/empty required output, any checker line containing `=FAIL`, absence of the exact sentinel `PSU33_FULL_COLOUR_CHECKER_SUCCESS`, or a sentinel that is not the terminal line of both stdout and the GAP log. Only after all gates pass does it print `RUNNER_ACCEPTED_PSU33_FULL_COLOUR_CHECKER`.

The checker itself stops before colouring if the involution-class count is not exactly one. It exhaustively computes all 1953 product-order edge colours; the full automorphism group of the vertex-coloured incidence graph; the full exact `AutomorphismGroup(L)` restriction image; all-pair colour checks for every reported generator; and, on strict containment, an explicit separator with an exhaustive all-pair check.
