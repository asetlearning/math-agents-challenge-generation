---
title: "Frozen heavy manifest — exact R0 group and literal cube set"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

# Exact active source scope

Odd `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual set
`{g^p:g in G}`, never generated subgroup; literal set itself a subgroup; ask
whether it is abelian; `p=2`/exponent-eight sibling excluded.

# Frozen row and command

Freeze all matrices, shears, labels, and noncentral representatives from
`../cohomology.md`. Freeze the simplest feasible central row `(R0)`:

`r14=r17=2`, every other `ri=0`.

Equivalently, only append `t^2` to `[X,Z]` and `[Y,Z]`. No other action,
shear, label, central row, kernel, quotient, or prime is admitted.

One invocation only:

```text
timeout 180s python3 -u Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/check_exact_group.py
```

Frozen script hashes:

```text
e9932eb57e0d219604f251bccd4f951e9851fe5e0c7226aa6cbd2b8dad218329  central_cohomology.py
f64ebe165da86d87333236b1752bbd409d1e43975db8739d969848422a01948f  check_exact_group.py
```

The checker imports only the hash-pinned `central_cohomology.py` in the same
directory and Python's standard library. Its mathematical inputs are the
literal frozen arrays `A,B,C,TX,TY,TZ,LX,LY,LZ`, the prescribed labels
`qX=f2`, `qY=e2`, the six frozen noncentral representatives, and the single
central row `(R0)` above. The prior unleased output is not an input and is not
used as evidence.

The checker must independently recompute the complete normalized factor
system, impose `(R0)`, certify all V and central associativity identities,
construct the exact ten-coordinate pc normal form, prove the `3^7` kernel
slice and `H_3(3)` quotient projection, inspect all 59,049 elements for exact
exponent nine, form the literal cube set, compare it exactly with its generated
subgroup closure, and
separately seek a noncommuting pair. It may not replace the literal cube set
by its generated subgroup.

Expected resources: one CPU, under 150 MiB RAM, under 120 seconds; hard
timeout 180 seconds. This is heavy because it exhausts all 59,049 elements,
so it must not run without a new Lead lease.

## Required output fields

The one invocation must print, and must abort on any failed assertion before
promoting a later gate:

1. the exact `(R0)` row, normalized factor-solution digest, cochain rank and
   dimension, 729 pair-defect checks, all 19,683 V-associativity checks, and
   all 19,683 central-associativity checks;
2. the six corrected pc relator check, unique coordinate-normal-form order
   `3^10`, embedded-kernel slice order `3^7`, and quotient projection order
   `3^3` with the frozen `H_3(3)` law;
3. exactly 59,049 inspected elements/cubes, an order-nine witness, and the
   cardinality of the literal cube image;
4. the exact generated-subgroup closure size and equality comparison with the
   literal cube set (the generated subgroup is a comparator only, never a
   replacement for the literal image);
5. separately, either a noncommuting pair of literal cubes or an exact
   generator-commutation conclusion if the literal set is a subgroup.

No mathematical value in fields 1--5 is pre-assumed beyond the frozen input
row and structural counts forced by the coordinate domains.
