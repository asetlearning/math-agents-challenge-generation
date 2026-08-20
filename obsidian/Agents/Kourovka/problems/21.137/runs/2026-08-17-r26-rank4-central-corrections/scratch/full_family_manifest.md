---
title: "Frozen heavy manifest — full 18-relator image and section quotient"
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

# Purpose and frozen boundary

The earlier unleased full-family ranks and the suggested 27-class count remain
quarantined. This one checker must derive from scratch:

1. all noncentral action defects and V-associativity identities;
2. the full normalized central cochain system;
3. its exact projection to the assigned 18 central relator coordinates;
4. the exact normalized central generator-lift gauge image;
5. the quotient orbit count and representatives, without assuming it is 27;
6. one full normalized factor certificate for every extracted representative.

It may not construct or enumerate alternate groups/cube sets, search another
action/shear/label/kernel/quotient, enumerate `3^18`, or use the prior unleased
output as an input.

Resource hard gates are independent of the quarantined expected values: abort
before row enumeration if the freshly derived relator dimension exceeds 10
(so at most `3^10` feasible rows are ever materialized), and abort before
per-representative factor extraction if the freshly derived quotient has more
than 100 representatives. Either abort is an exact derivation blocker, not
permission to expand the run.

# One command only

```text
timeout 240s python3 -u Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/check_full_family.py
```

Frozen input hashes:

```text
ecf9ebd11e5c74307e533e19d195348f99cfe4a68be44211cb1ad2b029eee10a  check_full_family.py
e9932eb57e0d219604f251bccd4f951e9851fe5e0c7226aa6cbd2b8dad218329  central_cohomology.py
```

The checker imports only the hash-pinned module in the same directory and
Python's standard library. The prior quarantined stdout is neither read nor
encoded as an expected assertion.

Expected resources: one CPU, under 150 MiB RAM, expected under 180 seconds,
hard timeout 240 seconds, one invocation. This is a heavy solver/enumeration
job and must not run before a new Lead lease.

# Required output

The checker must print the V-check counts; cochain equation/rank/dimension;
every eliminated affine relator equation; feasible-image dimension and size;
gauge rank and image size; equality of the exact-row cochain kernel with the
zero-relator gauge image; equality of the two quotient dimensions; the derived
orbit count; and every extracted representative with a realizing full-factor
digest. Any failed assertion aborts the run. No class count or representative
is pre-assumed.
