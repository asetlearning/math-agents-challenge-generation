---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: counterexample
outcome: PARTIAL_RESULT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/graph-automorphisms
  - project/kourovka
  - status/replicated
---

# Bounded equality for the PSL(2,11) involution class

## Precise bounded claim

Let `L=PSL(2,11)` and let `D` be its complete (unique) conjugacy class of
involutions. For the product-order colouring of the complete graph on `D`, the
discovery computations return

`Aut(Gamma) = Aut_2(Gamma) intersect Aut_3(Gamma)`, both of order 1320.

This is a `PARTIAL_RESULT` for this fixed pair only, pending independent
validation. It is neither a counterexample nor evidence that closes the universal
revision-2 scope.

## Admissibility reconstruction

- `L` is represented exactly as `SL(2,11)/{+I,-I}` using canonical matrix
  representatives. There are 1,320 determinant-one matrices and 660 central
  pairs. Two explicitly saved quotient generators generate all 660 elements and
  do not commute.
- A direct normal-subgroup certificate enumerates all eight conjugacy classes.
  The normal closure of every nonidentity class has order 660, so this exact
  finite nonabelian group has no proper nontrivial normal subgroup.
- Exactly 55 quotient elements have order 2. They form one conjugacy class, whose
  centralizer has order 12; hence `D` is one complete class and not a union.
- `|L|=660=2^2*3*5*11`, so the source-required second-smallest distinct prime is
  `p=3`.
- Every one of the 1,485 unordered pairs in `D` is saved with its exact product
  order. The occurring colours are precisely `2,3,5,6`, with valencies
  `6,12,24,12` and edge counts `165,330,660,330`.
- For each positive integer `t` not in `{2,3,5,6}`, the `t`-edge set is empty and
  `Aut_t(Gamma)=S_55` vacuously. Colours 2 and 3 both occur here.

## Exact comparison

After the four-colour gate and a Lead lease, one frozen GAP 4.12.1 / GRAPE 4.9.0
command returned:

```text
AUT2_ORDER=1320
AUT3_ORDER=1320
AUT5_ORDER=1320
AUT6_ORDER=1320
TWO_COLOUR_ORDER=1320
FULL_COLOUR_ORDER=1320
FULL_SUBGROUP_TWO=true
EQUALITY=true
```

The script constructs all four relation graphs from the frozen matrix, computes
their automorphism groups, and takes the required intersections. It also checks
every generator of the two-colour group exhaustively against every colour-2 and
colour-3 edge, and every generator of the full group against all four colours.
Containment plus equal finite orders proves equality inside this exact
computation. Because the result is equality, the strict-result separator branch
does not apply.

## Reproduction files

- `scratch/build_psl211_matrix.py`: independent-of-GAP finite quotient, class,
  normal-closure, and matrix constructor.
- `scratch/vertices.tsv`: canonical labels for all 55 involutions.
- `scratch/unordered_edges.tsv`: all 1,485 unordered edge colours.
- `scratch/product_order_matrix.csv`: complete 55 by 55 matrix.
- `scratch/summary.json`: group, class, factorization, colour, and valency summary.
- `scratch/compare_aut_groups.g`: the one leased automorphism comparison.
- `scratch/frozen-manifest.md`: exact command, versions, pre-run facts, and hashes.
- `log.md`: verbatim command output, exit status, observed wall time, ledger, and
  source/admissibility gates.

## What this does not establish

It does not establish the assertion for any other finite nonabelian simple group,
for a hypothetical other class, or universally. It does not identify the order-
1320 group structurally, although that is unnecessary for the fixed equality.
The discovery computation still requires independent reconstruction; no status
above `conjectured` is assigned here.

Verified by [[Agents/Kourovka/problems/21.53/verification/2026-08-17T205829Z-psl211-bounded-equality]].

## How this could be wrong

1. A bug in canonical quotient multiplication could corrupt both the class and
   product-order matrix; Validator should reconstruct the matrix independently.
2. A frozen-matrix indexing error could make the GAP relation graphs differ from
   the saved vertex labelling; hashes and spot products should be checked.
3. GRAPE could return an incorrect automorphism group or the intersection code
   could be misread; Validator should use an independent incidence or permutation
   reconstruction.
4. Equality for this pair could be mistakenly promoted to the universal claim;
   the scope remains explicitly open.
