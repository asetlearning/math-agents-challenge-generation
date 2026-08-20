---
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
strategy: PSL33-FULL-COLOUR-AUTOMORPHISM
frozen_utc: 2026-08-18T04:09:35Z
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

# Frozen run manifest

- Checker: `Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/psl33_full_colour.g`
- SHA-256: `4fd4e8ef68143e31421986f8fa2b02adfce1fa136f2075d181928e9668da1c79`
- Frozen size: 156 lines, 6,708 bytes.
- Exact command:

  `timeout --signal=TERM --kill-after=5s 60s gap -q Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/psl33_full_colour.g > Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/run.stdout 2> Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/run.stderr`

- Bound: one process, one invocation, 60 seconds wall time plus five-second kill grace, estimated peak workspace below 768 MiB, output below 2 MiB.
- Expected finite model: `|SL(3,3)|=|PSL(3,3)|=5616`; one involution class of 117 elements; 6,786 unordered edges; incidence encoding on 6,903 vertices.
- Exact tasks: verify group identity/nonabelian simplicity and all involution classes; compute the complete product-order matrix; compute the full vertex-colour-preserving automorphism group of the incidence encoding; compute `Aut(L)` and its restriction to the unique class; compare exact permutation subgroups; if strict, emit an explicit separator and exhaustively check all 6,786 edge colours.
- Outputs `run.stdout` and `run.stderr` were absent at freeze time.
- No patch, rerun, or expanded model is authorized by this manifest.

