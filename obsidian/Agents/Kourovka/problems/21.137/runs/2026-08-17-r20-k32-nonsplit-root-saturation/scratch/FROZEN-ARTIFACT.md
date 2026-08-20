---
title: "K32 nonsplit root saturation — frozen artifact"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: K32-NONSPLIT-ROOT-SATURATION
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# Frozen artifact

Frozen before any mathematical command is executed:

- artifact: `scratch/k32_nonsplit_frozen.py`;
- SHA-256: `0120923226d69921e25d8cb3d971b939d4d54210d9dc16c77e7c320ef195507c`;
- one model only: `p=3`, the two fixed PF length-three shear chains, the fixed
  `U`, and one central root `z` with `z^3=c`;
- one correction only: the lexicographically first `<c>`-valued Schreier row
  satisfying the fixed top-action and top-pair normalization;
- hard branch order: K32 outer action, extension consistency, complete actual
  quotient-label set, fibres/exponent, certificate;
- the script exits on the first failed gate and contains no alternate
  representative, PF generator, quotient type, or cocycle branch.

Exact leased command requested from Lead:

```text
timeout 120s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r20-k32-nonsplit-root-saturation/scratch/k32_nonsplit_frozen.py
```

Expected resources: one CPU, less than 256 MiB RAM, less than 30 seconds in the
success branch; hard timeout 120 seconds; requested lease 5 wall-clock minutes.

No mathematical command has been run at freeze time.
