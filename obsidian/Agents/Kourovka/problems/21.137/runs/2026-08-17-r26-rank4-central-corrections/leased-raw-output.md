---
title: "R0 exact-group leased run — raw output"
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

# Lease and command

Slot 1 was explicitly leased by Lead through `2026-08-17T22:21:00Z` for one
invocation only. All three hashes matched the lease exactly. The single
authorized invocation exited with code zero:

```text
timeout 180s python3 -u Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/check_exact_group.py
```

# Raw stdout

```text
fixed R0 central row: 000000000000002002
normalized factor solution SHA-256: a74a5d9b959366b0b8913fabd7cc7e7af1a4e3605df09c3d95d2f3a00492f824
cochain rank/dimension after R0: 1959 69
V defect/associativity checks: 729 19683 78732
central associativity checks: 19683 59049
six corrected pc relators: PASS
unique coordinate normal forms/order: 3^10 59049
embedded kernel coordinate slice/order: 3^7 2187
quotient H3(3) coordinate projection/order: 3^3 27
all elements/cubes inspected: 59049
exact exponent: 9 witness (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
literal cube-set size: 135
literal cube generated-closure size: 729
incremental subgroup orders: [1, 3, 9, 27, 81, 243, 729]
literal cube set equals its subgroup closure: False
generated element outside literal set: (2, 1, 0, 2, 2, 0, 1, 0, 0, 0)
noncommuting literal cube pair: None
TARGET ROWS: exponent nine PASS; literal cube set subgroup FAIL
```

No patch, rerun, alternate row, or expanded search occurred.
