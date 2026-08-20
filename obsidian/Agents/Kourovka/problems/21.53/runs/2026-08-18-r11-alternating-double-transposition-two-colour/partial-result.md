---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, topic/alternating-groups, project/kourovka, status/conjectured]
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Candidate family theorem: double transpositions in `A_n`

## Precise claim

Let `n>=7`, let `L=A_n`, and let `D` be its conjugacy class of double
transpositions.  For the complete exact product-order-coloured graph on `D`,

`Aut(Gamma) = Aut_2(Gamma) intersect Aut_3(Gamma)`.

This is a candidate `PARTIAL_RESULT` for one infinite family only.  It does not
answer the universal quantifier over all finite nonabelian simple groups and all
involution classes in Problem 21.53.

## Admissibility and conclusion matrix

| constraint_id | role | required condition | family value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | all admissible `(L,D)` | Only `(A_n,D_{2^2})`, `n>=7`, is treated | explicit claim range | partial only |
| `21.53-L-finite-nonabelian-simple` | admissibility | finite nonabelian simple `L` | `A_n` is finite nonabelian simple for `n>=7` | standard alternating-group simplicity theorem | pass |
| `21.53-D-single-involution-class` | admissibility | one conjugacy class of involutions | all cycle-type `2^2 1^{n-4}` elements form one `A_n`-class | the `S_n` centralizer contains the odd transposition `(ab)` from a factor, so the `S_n`-class does not split in `A_n` | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | exact order `|xy|` colours | complete overlay table below gives every exact order | four-edge overlay lemma | pass |
| `21.53-Aut-t-definition` | admissibility | exact one-way preservation for every `t` | on the finite pair set, one-way preservation by a permutation implies setwise preservation | injectivity and equal finite cardinalities | pass |
| `21.53-two-minimal-primes` | admissibility | `2,p` are two smallest primes of `|L|` | `|A_n|=n!/2`, so for `n>=7` the two smallest distinct prime divisors are `2,3`; hence `p=3` | divisibility by 2 and 3 | pass |
| `21.53-full-colour-group-definition` | admissibility | preserve every occurring exact colour | the only occurring colours are `2,3,4,5,6`; all five are preserved below | complete type table and reconstruction | pass in family |
| `21.53-two-colours-determine-all` | target conclusion | equality of full and selected-colour groups | proved below for the stated family | common-`R_3` neighbour invariant | proved in family, not universally |

## 1. Complete product-order type table

Write `ab|cd` for `(a b)(c d)`.  A vertex is an unordered matching of two
disjoint edges.  Superpose the red edges of `x` and blue edges of `y`.  After a
common doubled edge is cancelled, every component is an alternating path or an
alternating even cycle.  A path of `ell` edges contributes one `(ell+1)`-cycle
to `xy`; an alternating cycle of `2k` edges contributes two `k`-cycles.  Since
there are only two edges of each colour, this gives the following exhaustive
table for distinct `x,y`.  Here `r=|supp(x) intersect supp(y)|` and `c` is the
number of common transposition factors.

| exact order | `c` | `r` | noncancelled overlay | representative with `x=01|23` | union size | feasibility |
|---:|---:|---:|---|---|---:|---|
| 2 | 1 | 2 | `P1 + P1` | `y=01|45` | 6 | `n>=6` |
| 2 | 0 | 0 | `4 P1` | `y=45|67` | 8 | `n>=8` |
| 2 | 0 | 4 | alternating `C4` | `y=02|13` | 4 | `n>=4` |
| 3 | 1 | 3 | `P2` | `y=01|24` | 5 | `n>=5` |
| 3 | 0 | 2 | `P2 + P2` | `y=04|25` | 6 | `n>=6` |
| 4 | 0 | 2 | `P3 + P1` | `y=04|15` | 6 | `n>=6` |
| 5 | 0 | 3 | `P4` | `y=04|12` | 5 | `n>=5` |
| 6 | 0 | 1 | `P2 + P1 + P1` | `y=04|56` | 7 | `n>=7` |

Exhaustiveness is immediate from maximum degree two: with no common edge the
number `r` of degree-two vertices is 0,1,2,3, or 4; at `r=2` the two possible
component partitions are `P3+P1` and `P2+P2`, while all other `r` force the
displayed shape.  With one common edge, the remaining two edges are disjoint or
meet once.  Two common edges would mean `x=y` and is excluded.

Thus at `n=7` the disjoint-support order-2 subtype is absent but all five exact
orders `2,3,4,5,6` still occur.  At `n=8` that missing subtype first occurs; all
eight rows occur.  For every `n>=8` the table is stable.

## 2. Characterization of the selected order-3 relation

For a fixed matching `x=A|B`, a matching `z` satisfies `|xz|=3` in exactly one
of two ways:

1. `z` shares one whole edge of `x`, and its other edge meets the other edge of
   `x` in exactly one endpoint; or
2. `z` shares no edge, its support meets each edge of `x` in one endpoint, and
   each edge of `z` joins one such endpoint to a point outside `supp(x)`.

This is just the two order-3 rows of the exhaustive overlay table.  It makes the
following common-neighbour count a relation-theoretic invariant:

`q(x,y) = |{z in D : |xz|=3 and |yz|=3}|`.

Any permutation preserving the exact `R_3` edge set preserves `q`.

## 3. Hand count of `q` on the three unselected colours

The characterisation above gives complete lists for the three canonical pairs.
These lists also constitute a short independent certificate for the counts.

### Order 4

Take `x=01|23`, `y=04|15`, and put
`E={6,...,n-1}`.  The common order-3 neighbours are precisely

- `0u|i5`, where `i in {2,3}` and `u in {4} union E`;
- `1u|i4`, where `i in {2,3}` and `u in {5} union E`.

Hence

`q_4(n)=4(n-5)`.

### Order 5

Take `x=01|23`, `y=04|12`, put `E={5,...,n-1}`, and set `m=n-5`.
The common order-3 neighbours are precisely

- `04|23`;
- for each `u in E`, the three matchings `0u|23`, `04|2u`, `1u|34`;
- `0u|2v` for every ordered pair of distinct `u,v in E`.

Therefore

`q_5(n)=1+3m+m(m-1)=(n-4)^2`.

### Order 6

Take `x=01|23`, `y=04|56`, and put `E={7,...,n-1}`.  For each
`a in {2,3}` and `b in {5,6}`, the four internal common neighbours are

`01|ab`, `04|ab`, `14|ab`, `1b|a4`,

and for each `u in E` there is the additional neighbour `0u|ab`.  Thus

`q_6(n)=16+4(n-7)=4(n-3)`.

In each case, completeness follows by applying the two alternatives in Section 2
first relative to `x` and then relative to the displayed `y`; the surviving
choices are exactly those listed.

## 4. Separation, including exceptional degrees

For `n>=7`, the three values are pairwise distinct:

- `q_6-q_4=8`;
- `q_5-q_4=(n-6)^2>0`;
- `q_5-q_6=(n-6)^2-8`, which cannot vanish for integral `n` (its real roots are
  `6 plus/minus 2 sqrt(2)`).

The small degrees requested in the assignment are not inferred from a stable
range:

| `n` | order-2 subtype absent/present | `q_4` | `q_5` | `q_6` |
|---:|---|---:|---:|---:|
| 7 | disjoint-support subtype absent | 8 | 9 | 16 |
| 8 | all order-2 subtypes present | 12 | 16 | 20 |

At `n=9` the relative order of `q_5` and `q_6` reverses (`25>24`), but equality
never occurs.  The excluded boundary `n=6` has `q_4=q_5=4`, which explains why
the argument is stated only from `n=7` and is not silently extended downward.

## 5. Reconstruction of every exact colour

Let `tau` lie in `Aut_2(Gamma) intersect Aut_3(Gamma)`.  Because `D` and its
unordered-pair set are finite, the source's one-way condition implies
`tau(R_2)=R_2` and `tau(R_3)=R_3`.  Consequently `tau` preserves their complement.
Every pair in that complement has exact order 4, 5, or 6 by Section 1.  It also
preserves `q(x,y)`, since `tau` bijects the common `R_3`-neighbour sets.  The three
pairwise-distinct formulas in Section 4 therefore force `tau` to preserve each of
`R_4,R_5,R_6` separately.  It already preserves `R_2,R_3`, so it preserves every
exact occurring product-order colour.  Hence `tau in Aut(Gamma)`.

The reverse inclusion is definitional, proving the claimed equality for this
family.

## Reproducibility check and limits

The small checker
`Agents/Kourovka/problems/21.53/runs/2026-08-18-r11-alternating-double-transposition-two-colour/type_counts.py`
enumerates the exact finite matching model, not an automorphism group.  One run for
`7<=n<=15` returned respectively

- order 4: `q=8,12,16,20,24,28,32,36,40`;
- order 5: `q=9,16,25,36,49,64,81,100,121`;
- order 6: `q=16,20,24,28,32,36,40,44,48`,

agreeing with the formulas.  The proof does not depend on this bounded check.

This result does **not** establish Problem 21.53 for any other involution class,
any other finite simple group, or the excluded assertion in Problem 21.52.  Its
main possible failure points are an omitted four-edge overlay shape or an omitted
common-neighbour family; both are exposed as finite hand case splits above for
independent reconstruction.
