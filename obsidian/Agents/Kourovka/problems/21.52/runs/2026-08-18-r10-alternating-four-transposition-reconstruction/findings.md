---
title: "Four-transposition class in alternating groups: component theorem and reconstruction reduction"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/conjectured
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: false
---

# Outcome

`PARTIAL_RESULT`, not a universal answer to 21.52.  There is a complete hand
classification of the product order for two four-transposition involutions, a
uniform reduction of natural-action reconstruction to one intrinsic relation,
and an exact first implementation showing that the first two-point colour
refinement recovers that relation for `8 <= n <= 13`.  The remaining uniform
gate begins at `n=14`.

## Active target and exact limitation

The active source scope quantifies over every finite nonabelian simple pair
`(L,D)`.  This note treats only

`L=A_n`, `D={four-edge matchings on {1,...,n}}`, `n>=8`.

Even a theorem for every `n>=8` would therefore be an infinite-family partial,
not an answer to the universal notebook question.  The presently completed
reconstruction check is only for `8<=n<=13`; no finite list is presented as a
uniform theorem.

# 1. Complete alternating-component classification

Name the edges of `a` red and those of `b` blue.  Every component of their union
is exactly one of the following; these cases are exhaustive because every vertex
has red degree and blue degree at most one.

| symbol | component | red/blue edge counts | action of `ab` | order contribution |
|---|---|---:|---|---:|
| `E` | one doubled common edge | `(1,1)` | fixes both endpoints | `1` |
| `C_k`, `2<=k<=4` | alternating cycle on `2k` vertices | `(k,k)` | two disjoint `k`-cycles | `k` |
| `P_{2k}`, `1<=k<=4` | alternating path with `2k` edges | `(k,k)` | one `(2k+1)`-cycle | `2k+1` |
| `R_{2k+1}`, `0<=k<=3` | odd path, red-majority | `(k+1,k)` | one `(2k+2)`-cycle | `2k+2` |
| `B_{2k+1}`, `0<=k<=3` | odd path, blue-majority | `(k,k+1)` | one `(2k+2)`-cycle | `2k+2` |

For a path, label its vertices consecutively.  Direct composition moves along
alternating edges and then back along the other colour, producing one cycle on
all path vertices.  On an alternating `2k`-cycle the even and odd vertices form
the two `k`-cycles of `ab`.  This proves the action column without computation.

Thus a component multiset is feasible exactly when

```
e + sum k*c_k + sum k*p_k + sum (k+1)*r_k + sum k*b_k = 4,
e + sum k*c_k + sum k*p_k + sum k*r_k     + sum (k+1)*b_k = 4,
```

with the ranges in the table, nonnegative multiplicities, and with `e=4` excluded
because the graph edge requires `a!=b`.  Conversely, disjointly realizing the
listed paths and cycles realizes every solution, so these equations are also
sufficient.  They give 68 signatures for an ordered pair `(a,b)`, or 54 after
the global interchange red/blue.  The exact formula is

```
|ab| = lcm({k:c_k>0}, {2k+1:p_k>0}, {2k+2:r_k+b_k>0}).
```

If `V` is the number of vertices in the union and `h` the number of path
components, endpoint counting gives `V=8+h` and
`|supp(a) intersect supp(b)|=16-V=8-h`.  The number of common transpositions is
exactly `e`.

The possible product orders are precisely

`{2,3,4,5,6,7,8,9,10,12,14,15,20,21,30}`.

The degree-dependent coincidences are:

| degree | realized ordered signatures | product-order colours |
|---:|---:|---|
| `8` | 4 | `2,3,4` |
| `9` | 11 | `2,3,4,5,6,7,9,10` |
| `10` | 30 | previous plus `8,12,15,21` |
| `11` | 43 | previous plus `14,20` |
| `12` | 57 | previous plus `30` |
| `13,14,15` | `62,66,67` | same stable 15-colour set |
| `n>=16` | all 68 | same stable 15-colour set |

So stabilization of the colour *set* at `n=12` does not mean stabilization of
the pair types; the latter occurs only at `n=16`.

# 2. Intrinsic two-point refinement

For product-order colours `r,s`, define the entirely colour-intrinsic number

`N_{r,s}(a,b)=#{c in D\{a,b}: |ac|=r and |bc|=s}`.

Every colour automorphism preserves the complete vector `(N_{r,s}(a,b))_{r,s}`.
The deterministic enumerator in `pair_array_probe.py` constructs one representative
of every feasible ordered component signature and all four-matchings `c`; hence
equality of two output vectors is exactly the possible collision that matters.

After correcting the normalization issue documented in the log, the exact output is:

| `n` | `|D|` | realized signatures | distinct full arrays | collisions |
|---:|---:|---:|---:|---:|
| 8 | 105 | 4 | 4 | 0 |
| 9 | 945 | 11 | 11 | 0 |
| 10 | 4,725 | 30 | 30 | 0 |
| 11 | 17,325 | 43 | 43 | 0 |
| 12 | 51,975 | 57 | 57 | 0 |
| 13 | 135,135 | 62 | 62 | 0 |

For the two degrees explicitly singled out in the assignment there are very
small certificates.

### Degree 8

The four signatures `C4`, `C2 C2`, `E C3`, `E E C2` have respectively
`N_{2,2}=5,11,3,7`.  Thus one scalar intrinsic count recovers the full pair type,
and in particular whether a pair shares a transposition.

### Degree 9

The triple `(N_{9,9},N_{7,7},N_{7,9}+N_{9,7})` is already injective:

| signature | common edges `e` | triple |
|---|---:|---:|
| `P8` | 0 | `(148,36,160)` |
| `C4` | 0 | `(160,32,192)` |
| `C3 P2` | 0 | `(144,36,168)` |
| `C2 P4` | 0 | `(144,36,176)` |
| `C2 C2` | 0 | `(160,64,192)` |
| `E P6` | 1 | `(160,36,144)` |
| `E C3` | 1 | `(192,48,144)` |
| `E C2 P2` | 1 | `(160,52,144)` |
| `E E P4` | 2 | `(192,56,96)` |
| `E E C2` | 2 | `(192,48,192)` |
| `E E E P2` | 3 | `(192,72,96)` |

These tables treat `n=8` (one support only) and `n=9` (nine supports, with the
support quotient alone a complete graph) without importing a stable-range
argument.

# 3. Uniform reconstruction once common-edge incidence is intrinsic

Let `H_n` be the graph on four-matchings in which two vertices are adjacent iff
they contain a common transposition.  The matching Erdős--Ko--Rado lemma says that
for `n>=8` the maximum pairwise edge-intersecting families of four-matchings are
exactly

`F_e={M:e in M}`, for the two-subsets `e` of the natural point set,

of size `15*binom(n-2,6)`.  (The equality case is the only part needed here; it
is also the precise standard matching-EKR statement that Validator should check
independently.)  Therefore `H_n` intrinsically recovers the set of transposition
edges as its maximum cliques.

Two recovered stars `F_e,F_f` have empty intersection exactly when the original
edges `e,f` meet in one point; if they are disjoint, a four-matching containing
both exists for every `n>=8`.  Hence the intersection pattern of the recovered
stars is the line graph of `K_n`.  Its automorphism group is `S_n` for `n>=5`.
Finally a four-matching `M` is determined by the four stars containing it, so a
permutation of `D` inducing the point permutation `sigma` on stars must satisfy
`tau(M)=sigma(M)` for every `M`.

Consequently:

> If the product-order colouring intrinsically defines the predicate `e(a,b)>0`,
> then every colour automorphism on this class is induced by the natural `S_n`.

The exact array separation establishes the premise in the first implementation
for `8<=n<=13`.  The proposed uniform completion is finite symbolic algebra:
express every `N_{r,s}` as a binomial-coefficient polynomial in the number of
points outside the union for the 68 component signatures, and prove that no
signature with `e=0` has the same vector as one with `e>0` for any integer
`n>=14`.  This also avoids the spurious complement automorphism of the support
Johnson scheme at `n=16`: edge-star reconstruction has no complement ambiguity.

More explicitly, fix a signature on its union `U`, `|U|=V`.  If the support of
the third matching `c` uses `q` points outside `U`, choose those points in
`binom(n-V,q)` ways.  After replacing them by `q` labelled placeholders, the two
orders depend only on the chosen `8-q` points of `U` and one of the 105 perfect
matchings of that eight-set.  Hence, for every `r,s>=2`,

`N^S_{r,s}(n)=sum_{q=0}^8 A^S_{r,s,q} binom(n-V,q)`

with nonnegative integer coefficients obtained from a finite local enumeration.
There are at most
`105*sum_{t=0}^8 binom(16,t)=4,116,315` local cases for any one signature.
Thus the open uniform gate is literally a finite list of degree-at-most-eight
integer-polynomial noncollision checks; it does not require enumeration growing
with `n`.  A certifying run should output the coefficients and, for each pair
with opposite common-edge status, one coordinate and an exact root/sign
certificate valid for every integer `n>=14`.

# 4. Alternating-group admissibility and faithfulness

- `A_n` is finite nonabelian simple for every `n>=8`.
- The `S_n` class of type `2^4 1^(n-8)` lies in `A_n`.  An `S_n` class splits in
  `A_n` only when all cycle lengths are odd and distinct; four even 2-cycles
  violate this criterion.  Thus `D` is one `A_n` conjugacy class, including at
  `n=8,9`.
- For every `n>=8`, `Aut(A_n)=S_n`; the exceptional outer automorphism degree is
  `n=6`, outside the range.  Every such automorphism stabilizes `D` by cycle type.
- The `S_n` action on `D` is faithful: the stars `F_e` distinguish every
  two-subset, and the action of `S_n` on two-subsets is faithful for `n>=3`.

# 5. Constraint-and-conclusion matrix

| constraint_id | role | use/evidence | result |
|---|---|---|---|
| `21.52-forall-L-D` | admissibility | explicitly only the alternating four-transposition subfamily | partial only |
| `21.52-L-finite-nonabelian-simple` | admissibility | simplicity of `A_n`, `n>=8` | pass in family |
| `21.52-D-single-involution-class` | admissibility | nonsplitting criterion above | pass in family |
| `21.52-Gamma-complete-on-D` | admissibility | enumerator and hand argument retain every distinct pair | pass |
| `21.52-edge-colour-exact-product-order` | admissibility | lcm component formula; no finer conjugacy colour | pass |
| `21.52-tau-preserves-all-edge-colours` | admissibility | only `N_{r,s}` and relations derived from exact orders are used | pass |
| `21.52-tau-induced-by-AutL` | target conclusion | candidate for `8<=n<=13`; uniform `n>=14` polynomial gate open | not established universally |

# Reproducibility and limitations

- Python `3.12.3`.
- `component_signatures.py`, 38 lines, SHA-256
  `00f5cd745c4bcb7d6bc3ce9a2f79914f9def6e3a38d46a78512a3648f0f95d6f`.
- `pair_array_probe.py`, 113 lines, SHA-256
  `e0c7c322183f44254d4a4ed11d5cd981aebf969e46b02d88adc044864bf5e3cf`.
- The largest corrected run (`n=13`) used 43.38 seconds and 35,072 KiB RSS.
- No heavy compute, external search, prior double-transposition theorem, or
  solution-bearing historical artifact was used.

What this does **not** establish: it does not prove array separation for any
`n>=14`; it does not independently certify the implementation; it does not replace
an equality-case check for matching EKR; and it does not answer 21.52 outside this
single alternating-group involution class.
