---
title: "Observed leased output — rank-four H3 shear-orbit support"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: RANK4-H3-SHEAR-ORBIT-SUPPORT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/conjectured]
---

# Leased invocation

Frozen checker SHA-256:
`8b33f11c261c78aad8f8d5e54d52b9aa7c7fb3a449301c283a49d26d57f4f969`.

The exact one-time command was

```text
timeout 45s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/scratch/check_shear_orbits.py --full
```

Observed process result: exit code `0`, wall time `1.608543197` seconds,
runner chunk `0f2349`; the synchronous runner exposed no live PID.  This file
is a complete normalized transcription of the mathematical JSON output.  No
patch or rerun occurred.

# Scalar output

```text
field: 3
system equations/variables/rank/augmented-rank/dimension: 56/36/17/17/19
particular LX: 0000/1100/0000
particular LY: 0000/1000/0000
particular LZ: 0000/0201/0000
listed gauge generators: 24
translation gauge rank: 18
affine quotient dimension: 1
complete discrete stabilizer size: 9
signature coordinate count/image dimension/kernel dimension: 108/1/18
Burnside fixed points for every (a,d) in F3^2: 3
genuine orbit count: 3
orbit size of each representative: 3^18 = 387420489
orbit-size sum: 3^19 = 1162261467
hard_kill: null
factor_system_opened: false
group_enumeration_run: false
central_relators_varied: false
universal_scope_answered: false
```

# Complete representative support output

The quotient representatives are `r=0,1,2`.  For every one of the 27 quotient
section words, the observed norm image `W_h` is zero, so the observed affine
support is the singleton `F_h={lambda_r(h)}`.  Coordinates below are
`(e1,e2,f1,f2)`; this table therefore records all 81 affine supports from the
JSON output.

| `h=(a,b,d)` | `lambda_0=F_h` | `lambda_1=F_h` | `lambda_2=F_h` | `W_h` |
|---|---:|---:|---:|---:|
| 000 | 0000 | 0000 | 0000 | 0 |
| 001 | 0000 | 0000 | 0000 | 0 |
| 002 | 0000 | 0000 | 0000 | 0 |
| 010 | 0100 | 0100 | 0100 | 0 |
| 011 | 1100 | 1100 | 1100 | 0 |
| 012 | 2100 | 2100 | 2100 | 0 |
| 020 | 0200 | 0200 | 0200 | 0 |
| 021 | 1200 | 1200 | 1200 | 0 |
| 022 | 2200 | 2200 | 2200 | 0 |
| 100 | 0001 | 0001 | 0001 | 0 |
| 101 | 2001 | 2001 | 2001 | 0 |
| 102 | 1001 | 1001 | 1001 | 0 |
| 110 | 0000 | 0000 | 0000 | 0 |
| 111 | 0000 | 0000 | 0000 | 0 |
| 112 | 0000 | 0000 | 0000 | 0 |
| 120 | 2000 | 1000 | 0000 | 0 |
| 121 | 2000 | 1000 | 0000 | 0 |
| 122 | 2000 | 1000 | 0000 | 0 |
| 200 | 0002 | 0002 | 0002 | 0 |
| 201 | 2002 | 2002 | 2002 | 0 |
| 202 | 1002 | 1002 | 1002 | 0 |
| 210 | 1000 | 2000 | 0000 | 0 |
| 211 | 1000 | 2000 | 0000 | 0 |
| 212 | 1000 | 2000 | 0000 | 0 |
| 220 | 0000 | 0000 | 0000 | 0 |
| 221 | 0000 | 0000 | 0000 | 0 |
| 222 | 0000 | 0000 | 0000 | 0 |

The complete unions printed by the checker are

```text
Sigma_0 = Sigma_1 = {
  0000,0001,0002,0100,0200,
  1000,1001,1002,1100,1200,
  2000,2001,2002,2100,2200
}

Sigma_2 = {
  0000,0001,0002,0100,0200,
  1001,1002,1100,1200,
  2001,2002,2100,2200
}
```

Thus the three observed summaries are respectively

```text
r=0: |Sigma|=15, span dimension=3, subspace=false,
     symplectic rank on span=2, support_gate_pass=false
r=1: |Sigma|=15, span dimension=3, subspace=false,
     symplectic rank on span=2, support_gate_pass=false
r=2: |Sigma|=13, span dimension=3, subspace=false,
     symplectic rank on span=2, support_gate_pass=false
```

All three have the same explicit closure defect:

`e2=0100 in Sigma`, `f2=0001 in Sigma`, but
`e2+f2=0101 notin Sigma`.

The span is `<e1,e2,f2>` and is nonisotropic because
`omega(e2,f2)=1`; failure is exactly the required subspace gate, not the
nonisotropy gate.

# Output interpretation

The translation gauge lies in the signature kernel.  Both have dimension 18,
so they are equal.  The nine-element stabilizer has three fixed points on the
one-dimensional quotient, as witnessed by nine Burnside fixed-point counts all
equal to three.  Hence the three table rows are all genuine lift/shear orbits,
not merely support batches, and their sizes sum to the full `3^19` affine
solution space.

This is only a factor-independent necessary-gate exclusion for the frozen
`p=3`, rank-four kernel, fixed outer/center action, and fixed label pair.  It is
not a group, not a literal cube-set computation, not a counterexample, and not
an answer to the universal source scope.
