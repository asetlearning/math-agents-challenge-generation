---
title: "Frozen independent checker manifest — 21.137 shear-orbit support"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

# Clean-room boundary

The checker was written from the matrices and triple law displayed in the
submitted manifest after independently deriving the inverse, cube, kernel
conjugation, and mixed-word `h=(1,1,0)` cube-label formulas.  The claimant
checker was not opened, imported, or executed.

# Frozen checker

Path:
`Agents/Kourovka/problems/21.137/verification/scratch/verify_shear_orbits_independent.py`

SHA-256:
`7e39608a1c8847271a47e1c1441b41759d18e38e8b42f4203fea6a2b2ecbe0d7`

Exact command:

```text
timeout 45s python3 Agents/Kourovka/problems/21.137/verification/scratch/verify_shear_orbits_independent.py --full
```

Expected resources: one CPU, under 128 MB, under 45 seconds wall time; requested
lease duration five minutes.

# Bounded checks

The checker reconstructs the 56 residual coordinates by basis evaluation,
solves the affine system, tests each of 24 gauge generators, derives both
finite centralizers from their defining equations, applies Burnside to the
resulting one-dimensional quotient, and enumerates exactly 27 quotient words
for each of three representatives.  It asserts the projected norm formula's
finite data only.  It opens no factor system, cocycle, presentation, group
enumeration, prior verification, or claimant checker.

Any pass can yield at most `status/replicated` for this frozen family and keeps
`active_assignment_answered:no`.
