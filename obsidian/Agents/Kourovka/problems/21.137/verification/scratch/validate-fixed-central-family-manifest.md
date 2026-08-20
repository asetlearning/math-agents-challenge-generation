---
title: "Validator frozen heavy manifest — fixed rank-four central family"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

# Frozen boundary

This is an independent replication of exactly one submitted `p=3` family:
kernel `3_+^(1+4) x C3^2`, quotient `H_3(3)`, the nine frozen
`A,B,C,TX,TY,TZ,LX,LY,LZ` arrays, prescribed labels `qX=f2`, `qY=e2`,
and the six fixed noncentral relator representatives. It may vary only the 18
central relator coordinates admitted by the derived cochain equations.

It does not test a different lift, shear, action, kernel, quotient, prime, or
the `p=2` sibling. A pass leaves `active_assignment_answered:no`.

# Independence

The checker imports only Python's standard library. The claimant's scripts,
factor digests, cochain solutions, orbit representatives, and raw cube output
are not read at runtime. The submitted nine arrays are frozen input data. The
submitted ten affine equations, gauge matrix, 27 representative strings, and
class cardinalities occur only as final assertions against independently
derived objects.

# Exact command and hash

```text
timeout 600s python3 -u Agents/Kourovka/problems/21.137/verification/scratch/validate_fixed_central_family.py
```

```text
04f8b72d3735b459326560ede404eb689ddfa257ccfac7c16b2c7a8d0b564efe  validate_fixed_central_family.py
```

One invocation only. Expected resources: one CPU, under 250 MiB RAM, expected
under 420 seconds, hard timeout 600 seconds, requested lease duration 15
minutes. No patch or rerun is authorized by this manifest.

# Required gates

The checker must abort on any failed assertion and print:

1. all 729 action defects, all 19,683 vector identities and 78,732 scalar
   identities;
2. the complete 2,028-variable, 59,049-equation central cochain rank and
   affine dimension;
3. relator-image rank eight, all ten exact affine equations, and all 6,561
   feasible rows;
4. coboundary rank 74, generator gauge rank five, exact displayed gauge
   matrix, equality of the two dimension-69 kernels, quotient dimension three,
   27 orbits and coverage of all 6,561 rows;
5. an independently extracted realizing factor for every representative;
6. exact crossed-product order `3^10`, kernel `3^7`, quotient `H_3(3)`, and
   exact exponent nine;
7. the cube of every one of 59,049 elements in every class, with the literal
   cube image kept distinct from its generated subgroup comparator;
8. literal image size 135, generated closure size 729, and an explicit
   closure outsider for every class.

The noncommutativity gate is not run after literal closure fails. The generated
closure is never substituted for the literal image.
