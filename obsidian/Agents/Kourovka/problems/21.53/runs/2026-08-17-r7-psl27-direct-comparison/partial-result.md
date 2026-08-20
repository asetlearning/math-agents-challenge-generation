---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/replicated]
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Fixed-pair equality for PSL(2,7)

## Precise bounded result

For `L=PSL(2,7)` and its unique involution conjugacy class `D` of size 21, the
complete product-order colouring has exactly the three edge colours `2,3,4`, with
valencies `4,8,8`.  Consequently, under the source's one-way definition,

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma)`.

This is equality for one fixed admissible pair, hence bounded partial progress.  It
does not answer the universal source question.

## Exact group and class model

Use `PSL(2,7)=SL(2,7)/{+I,-I}` and represent a projective element by the
lexicographically smaller of `A` and `-A`, read as the row-major tuple `(a,b,c,d)`
over `F_7`.  Exhaustive integer arithmetic gives 336 determinant-one matrices and
168 projective elements.  Their element-order counts are

`1:1, 2:21, 3:56, 4:42, 7:48`,

and the conjugacy-class `(order,size)` list is

`(1,1), (2,21), (3,56), (4,42), (7,24), (7,24)`.

All 32 unions of conjugacy classes containing the identity were tested for inverse
and multiplication closure; the only subgroup sizes found were 1 and 168.  This
gives a direct finite simplicity certificate.  Nonabelianity is witnessed by

`A=(0,1,6,0), B=(0,1,6,1), AB=(1,6,0,1), BA=(1,0,1,1)`.

Thus this is a finite nonabelian simple group of order
`168=2^3*3*7`, and the required second-smallest distinct prime is `p=3`.  There is
one conjugacy class of exact involutions, of size 21.

## Vertex labels

The complete matrix below uses these canonical projective representatives:

```text
 1 (0,1,6,0)   2 (0,2,3,0)   3 (0,3,2,0)
 4 (1,1,5,6)   5 (1,2,6,6)   6 (1,3,4,6)   7 (1,4,3,6)
 8 (1,5,1,6)   9 (1,6,2,6)  10 (2,1,2,5)  11 (2,2,1,5)
12 (2,3,3,5)  13 (2,4,4,5)  14 (2,5,6,5)  15 (2,6,5,5)
16 (3,1,4,4)  17 (3,2,2,4)  18 (3,3,6,4)  19 (3,4,1,4)
20 (3,5,5,4)  21 (3,6,3,4)
```

## Complete product-order matrix

The diagonal `1`s are included for orientation; every off-diagonal entry is the
exact order of the product of its row and column involutions.  This displays all
210 unordered distinct pairs.

```text
    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
 1  1  3  3  4  4  3  3  4  4  3  3  2  2  3  3  4  2  4  4  2  4
 2  3  1  3  3  4  4  4  4  3  2  3  3  3  3  2  4  4  2  2  4  4
 3  3  3  1  4  3  4  4  3  4  3  2  3  3  2  3  2  4  4  4  4  2
 4  4  3  4  1  4  2  4  2  3  4  3  3  2  2  4  3  4  3  3  3  4
 5  4  4  3  4  1  2  4  3  2  2  4  2  3  4  3  3  3  3  4  4  3
 6  3  4  4  2  2  1  3  4  4  2  3  4  4  2  3  3  3  3  4  3  4
 7  3  4  4  4  4  3  1  2  2  3  2  4  4  3  2  4  3  4  3  3  3
 8  4  4  3  2  3  4  2  1  4  3  4  3  2  4  2  3  4  4  3  3  3
 9  4  3  4  3  2  4  2  4  1  4  2  2  3  3  4  4  3  3  3  4  3
10  3  2  3  4  2  2  3  3  4  1  3  4  3  4  4  4  4  4  2  3  3
11  3  3  2  3  4  3  2  4  2  3  1  4  3  4  4  2  4  3  4  3  4
12  2  3  3  3  2  4  4  3  2  4  4  1  4  3  3  3  4  4  3  2  4
13  2  3  3  2  3  4  4  2  3  3  3  4  1  4  4  4  2  3  4  4  3
14  3  3  2  2  4  2  3  4  3  4  4  3  4  1  3  4  3  4  3  4  2
15  3  2  3  4  3  3  2  2  4  4  4  3  4  3  1  3  3  2  4  4  4
16  4  4  2  3  3  3  4  3  4  4  2  3  4  4  3  1  2  3  2  3  4
17  2  4  4  4  3  3  3  4  3  4  4  4  2  3  3  2  1  3  2  4  3
18  4  2  4  3  3  3  4  4  3  4  3  4  3  4  2  3  3  1  4  2  2
19  4  2  4  3  4  4  3  3  3  2  4  3  4  3  4  2  2  4  1  3  3
20  2  4  4  3  4  3  3  3  4  3  3  2  4  4  4  3  4  2  3  1  2
21  4  4  2  4  3  4  3  3  3  3  4  4  3  2  4  4  3  2  3  2  1
```

The edge inventory is

| product order | unordered edges | valency at every vertex |
|---:|---:|---:|
| 2 | 42 | 4 |
| 3 | 84 | 8 |
| 4 | 84 | 8 |

## Why the two retained colours determine the third

Write `E_t` for the `t`-edge set.  A vertex permutation induces a bijection of the
finite set of 210 unordered edges.  If it is in the source-defined `Aut_t`, then it
maps `E_t` into `E_t`; injectivity and finiteness imply it maps `E_t` onto `E_t`.
Hence every element of `Aut_2 intersection Aut_3` preserves `E_2` and `E_3`
setwise.  The inventory shows

`E_4 = all edges minus (E_2 union E_3)`,

so it preserves `E_4` as well.  This gives containment in the full colour group;
the reverse containment is definitional.  For every nonoccurring positive integer
`t`, `Aut_t=S_D` vacuously, so the all-label intersection introduces no hidden
condition.

This intrinsic complement argument is the requested equality certificate; an
automorphism-group comparison would be unnecessary.  No such comparison was run.

## Constraint-and-conclusion matrix

| constraint_id | role | value in this bounded determination | evidence | result |
|---|---|---|---|---|
| 21.53-forall-L-D | admissibility | one admissible pair only; universal quantifier remains open | fixed target stated above | not answered |
| 21.53-L-finite-nonabelian-simple | admissibility | direct order-168 projective model; noncommuting witness; exhaustive normal-class-union test | exact certificate and script | pass for pair |
| 21.53-D-single-involution-class | admissibility | exactly one order-2 class, size 21 | exact class partition | pass |
| 21.53-Gamma-product-order-colouring | admissibility | every one of 210 edges evaluated by exact multiplication and order | displayed matrix | pass |
| 21.53-Aut-t-definition | admissibility | one-way preservation used; nonoccurring labels treated vacuously | complement proof | pass |
| 21.53-two-minimal-primes | admissibility | `168=2^3*3*7`, hence `p=3` | group count/factorization | pass |
| 21.53-full-colour-group-definition | admissibility | intersection over occurring 2,3,4; all other labels vacuous | inventory and proof | pass |
| 21.53-two-colours-determine-all | target conclusion | equality holds for this pair | finite-set complement proof | holds, not violated |

## Reproducibility artifacts

- `scratch/psl27_exact_scheme.py`, SHA-256
  `54545eba3defdba8faade61d957d55dd7671d4eab540363bb7d6a3723a0a9d8a`.
- `scratch/psl27_exact_scheme_certificate.json`, containing the full vertex list,
  matrix, 210-edge list, group/class data, and internal canonical-object digests;
  file SHA-256
  `9dc3be4f7b84564e1ecd1cddc33c0f101210ec142225f3fdbfd48d50ff8536f7`.
- `scratch/psl27_product_order_matrix.csv`, file SHA-256
  `c184a782544ea0b3dceefc3cd495c5679044a4dc3693aabf6caf1b3f56e53ff2`.
- Exact command and observed output are recorded in `log.md`.

## What this does not establish

It does not compute the numerical order or generators of either automorphism group,
does not treat any other involution class or group, does not prove a PSL(2,q)
family theorem, and does not prove the universal Kourovka assertion.  In particular
it supplies no counterexample because the required strict inequality fails for this
pair.

Verified by [[Agents/Kourovka/problems/21.53/verification/2026-08-18T001534Z-psl27-fixed-pair-equality]]
