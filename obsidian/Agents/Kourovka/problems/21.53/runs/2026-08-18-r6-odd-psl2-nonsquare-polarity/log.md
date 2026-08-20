---
title: "Run log — odd PSL(2,q) nonsquare polarity completion"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: proof
strategy: ODD-PSL2-NONSQUARE-POLARITY-COMPLETION
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/draft]
---

# Active-time ledger

- Work start: 2026-08-17T23:01:20Z; official cumulative active minutes at start: 76.
- The reviewed `q=1 mod 4` family theorem, the revision-2 source scope, and the exact one-way/vacuous `Aut_t` convention are inherited inputs. This run does not redo the source or staleness gates and does not inspect excluded solution-bearing history.

## Strategy lock

For odd `q>=7`, `q=3 mod 4`, write `D` for the internal nonsingular points of the conic and `A` for the exact order-2 adjacency matrix.  With `X` the incidence matrix between `D` and exterior poles (equivalently, between internal points and secant lines), the reviewed identity is

`XX^T=qI+J-A^2`.

Every column has weight `(q-1)/2`.  The first test is whether this Gram matrix has a unique binary constant-column-weight factorization up to column permutation.  Only after that test passes is it legitimate to classify the `q`-block resolutions recovering conic points.

## Early kill-signature: an exact `q=7` Pasch trade

Work over `F_7` with conic

`C: Y^2=XZ`

and quadratic form `Q(X,Y,Z)=Y^2-XZ`.  The nonsquares are `3,5,6`, so the six affine projective points

`P=(1,0,1), A=(3,1,1), B=(5,2,1), C=(2,0,1), D=(4,0,1), R=(6,4,1)`

are internal: their `Q`-values are respectively `6,5,6,5,3,3`.

The following four secant lines have as their complete internal-point sections the displayed triples:

| line | two conic parameters | internal support |
|---|---:|---|
| `X=2Y+Z` | `4,5` | `PAB` |
| `Y=0` | `0,infinity` | `PCD` |
| `X=Y+2Z` | `2,6` | `ACR` |
| `X=4Y+4Z` | `1,3` | `BDR` |

The four endpoint pairs partition the eight conic points.  The six internal points are the six pairwise intersections of the four lines.  Consequently every pair in each of

`PAC, PBD, ABR, CDR`

also lies on one of the four displayed secants and has zero `R_2` codegree.  Each new triple is noncollinear, hence is not a geometric column support.

Let `1_S` denote the indicator column of a triple `S`.  The tetrahedral star/face identity is

```
sum_{S in {PAB,PCD,ACR,BDR}} 1_S 1_S^T
 =
sum_{T in {PAC,PBD,ABR,CDR}} 1_T 1_T^T.
```

Indeed every one of the six points occurs twice on either side, and the same twelve unordered point-pairs occur once on either side.  Replacing those four geometric columns of `X` by the four nongeometric columns therefore produces a binary matrix `X'` with the same 28 columns, the same column weight three, and

`X'X'^T=XX^T=7I+J-A^2`,

but `X'` is not a column permutation of `X`.  This is a hand certificate; no computation is used.

### Decision at the first milestone

Canonical uniqueness of the geometric `0`--`1` column supports, in the exact form required by the assigned route, is false already at the allowed boundary `q=7`.  The trade refutes only the Gram-factorization lemma: it is not an exotic automorphism of the order-2 graph and does not refute the desired `PSL(2,7)` equality.

## Characteristic-three empty-colour audit

If `q=3^f` with `f` odd, then `q=3 mod 4` and `epsilon=chi(-1)=-1`.  Exact order three would require `u=1=4`; for distinct shell points the degenerate value `u=4` occurs only in the exterior shell `epsilon=1`.  Thus `R_3` is empty.  Under revision 2's one-way definition, `Aut_3=S_D` vacuously, so the source equality in this subfamily reduces exactly to `Aut(Gamma)=Aut_2`.  No second relation is available to distinguish the geometric factorization from a competing Gram factorization.  The `q=7` trade does not itself extend to `q=3^f`; it shows that a field-uniform uniqueness assertion cannot be inferred from the matrix identity and weight data alone.

## Lease status

At 2026-08-17T23:10:00Z a request was filed for a two-minute lease to run a prepared, under-five-second exact `q=7` audit of resolution counts in the original and traded column systems.  Lead granted slot 1 for exactly one invocation.  The script SHA-256 matched the approved value

`87abf88b48cd189708b19d61442c1deaa6ee60cd1b4e0fb31b218582297ed33f`.

The frozen command was run exactly once and exited `0` after approximately `0.17` seconds.  Complete stdout, also preserved verbatim in `scratch/q7_pasch_audit.stdout.txt`, was:

```
points=57 conic=8 internal=21
geometric_columns=28 traded_columns=28
gram_equal=True
original_resolutions=8
traded_resolutions=0
```

This proves only that the original geometric `q=7` system has eight exact seven-block resolutions while the one displayed Pasch-traded system has none.  The resolution pattern therefore filters this competitor.  It does not classify all factorizations and supplies no larger-field inference.

## Stop and accounting

- Research stop: 2026-08-17T23:15:30Z.
- Initial charged work: 14 active minutes (mandatory reading, hand derivation, certificate writing, and packaging).
- Leased audit and correction: 1 active minute.
- Official cumulative active minutes: 91/180.
- Unused from the authorized 45-minute increment: 30 minutes.
- State: `awaiting_lead`.  No replacement method or field expansion was started.
