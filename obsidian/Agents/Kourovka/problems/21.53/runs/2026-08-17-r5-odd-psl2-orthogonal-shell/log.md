---
title: "Run log — odd PSL(2,q) orthogonal-shell rigidity"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: proof
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/draft]
---

# Run 5 — `ODD-PSL2-ORTHOGONAL-SHELL-RIGIDITY`

## Active-time ledger

- `2026-08-17T22:28:55Z` — resumed at official cumulative active minute 59; bounded increment cap 45 minutes (stop research by cumulative 97, package by cumulative 104).

## Scope and reviewed input

The active target is revision 2 of `21.53/two-minimal-prime-colours`.  This run
uses only the canonical scope, the reviewed even-characteristic theorem and odd
trace reduction, its Validator note, and the current inbox verdict.  The exact
remaining target in this lane is the odd-shell lemma

`Aut(D;R_2,R_3)=PGammaO(3,q)` for odd `q>=7`,

where `D` is the `chi(Q)=chi(-1)` orbit in `P(sl_2(q))`, `R_2` is
orthogonality, and `R_3` is `B(x,y)^2=Q(x)Q(y)`.  The universal all-simple-group
scope remains open, Problem 21.52 remains excluded, and
`active_assignment_answered:no` is retained.  External staleness work is not
reopened in this discovery-blind continuation.

## Strategy portfolio

1. **Incidence completion (selected):** calculate common-neighbour data in the
   induced orthogonality graph and try to reconstruct missing projective points,
   lines, the conic and polarity.
2. **Nonempty-`R_3` pivot:** use mixed `R_2/R_3` intersection numbers to recover
   tangent-sharing among exterior points and then reconstruct the conic as the
   maximum cliques of a triangular graph.
3. **Coordinate alternative:** normalize an orthogonal frame and derive field
   operations from the two preserved angle relations.  This is secondary because
   it obscures the empty-`R_3` case.
4. **Certificate plan:** a hand reconstruction with every exceptional
   characteristic separated; no family inference from the reviewed `q=27`
   stress test and no unleased computation.

## Common-neighbour calculation

Write `epsilon=chi(-1)`.  For distinct `x,y in D`, put

`u(x,y)=B(x,y)^2/(Q(x)Q(y))`

and let `Delta=4Q(x)Q(y)-B(x,y)^2`.  The two polar lines meet in the
single projective point `z=<x,y>^perp`.  In the standard `sl_2` model the
determinant square class of `B` is that of `-2`.  In an orthogonal basis
adapted to `<x,y>+<z>` this gives

`chi(Q(z))=epsilon chi(Delta)=epsilon chi(4-u)`.

Consequently

`|N_2(x) intersect N_2(y)| = 1` iff `chi(4-u)=1`, and it is `0` otherwise
(`chi(0)=0`).  In particular every `R_2` edge (`u=0`) lies in a unique
`R_2` triangle.

The sections of a polar line have the following sizes, obtained by restricting
`Q` to the binary space `z^perp`:

| type of pole `z` | `|D intersect z^perp|` |
|---|---:|
| `z in D` | `(q-epsilon)/2` |
| `chi(Q(z))=-epsilon` | `(q+epsilon)/2` |
| `Q(z)=0` | `q` if `epsilon=1`, and `0` if `epsilon=-1` |

Thus for `q=3^f`, `f` odd, the conic points have tangent polars completely
disjoint from `D`.  Moreover `R_3` is empty, so the graph reveals the
`D`-polar sections as neighbourhoods but has no vertices or blocks at all on
those tangent lines.  A pair with zero `R_2` codegree has an exterior pole, but
the graph does not yet say when two such pairs have the same pole.  That would
require a classification of the large pairwise-zero-codegree sets
`D intersect e^perp` (size `(q-1)/2`) and exclusion of non-collinear competitors.
This is the precise incidence-completion obstruction; the reviewed `q=27`
calculation does not supply that classification.

## First-route decision

The common-neighbour data canonically recovers only the polar lines whose poles
are already in `D`.  In the empty-`R_3`, `epsilon=-1` case it does not recover
the conic or the concurrency classes representing exterior poles.  I therefore
pivot, within the assigned lane, to the nonempty-`R_3` cases and first treat
`epsilon=1`, where mixed intersections recover the missing tangent relation.

## One-hour checkpoint (official cumulative minute 71)

- **Target:** revision 2, odd `PSL(2,q)` orthogonal-shell lemma; the universal
  all-simple-group assignment remains unanswered.
- **New facts:** exact `R_2` codegree and polar-section formulas; a precise
  empty-`R_3` completion obstruction; and a candidate hand proof of
  `Aut(D;R_2,R_3)=PGammaO(3,q)` for every odd `q>=9` with `q=1 mod 4`.
- **Current strategy:** derive the tangent-sharing relation from mixed
  intersections, reconstruct the conic as the maximum-star completion of a
  triangular graph, then use harmonic quadruples to reconstruct the field.
- **Ruled out:** common `R_2` neighbours alone do not expose conic points when
  `q=3^f`, `f` odd; their tangent polars contain no vertex of `D`.
- **Bottleneck:** for `epsilon=-1`, grouping zero-codegree pairs into the unique
  exterior-pole line sections requires a genuine extremal/concurrency
  classification, not merely the intersection numbers.
- **Alternatives:** (i) prove that classification by a finite-geometric bound;
  (ii) use the modular row space/eigenspace of the orthogonality incidence matrix
  to reconstruct the quadratic Veronese embedding.
- **Recommended bounded experiment:** test the hand classification argument on
  abstract incidence counts only; abandon it if no proof excluding non-collinear
  competitors appears before the research stop.
- **Admissibility:** this is an exact infinite subfamily of the canonical object,
  with the exact relations and `p=3`, but it does not pass the universal
  `21.53-forall-L-D` or universal conclusion rows.  Outcome can only be
  `PARTIAL_RESULT`; `active_assignment_answered:no`.

## Empty-`R_3` matrix reduction

For `epsilon=-1`, partition the full polarity matrix by isotropic points `C`,
the shell `D`, and the other anisotropic orbit `E`.  Since the full matrix obeys
`M^2=qI+J` and the `D`--`C` block is zero, its `D`--`D` block gives

`M_DE M_DE^T=qI+J-A_2^2`.

Thus the `R_2` graph determines the Gram matrix of the missing incidence with
`E`.  The columns have weight `(q-1)/2`, rows have weight `(q+1)/2`, and every
zero-codegree pair occurs together in exactly one column.  The unresolved step
is uniqueness/canonicity of this binary factorization (equivalently the
geometric clique decomposition).  Once the columns are available, each conic
point should appear as a resolution of them into `q` disjoint supports covering
`D`; proving that all such resolutions are geometric is a second explicit
completion lemma.  This refines the obstruction without using `q=27` as proof.

## Research stop and outcome

- `2026-08-17T22:45:04Z` — stopped mathematical research at official cumulative
  active minute 75, before the assigned research cutoff.
- Outcome: `PARTIAL_RESULT`.
- Exact new bounded claim: the odd orthogonal-shell lemma for every `q>=9` with
  `q=1 mod 4`, routed to Validator as `status/conjectured`.
- Exact unresolved family: `q=3 mod 4`, including the empty-`R_3` family
  `q=3^f`, `f` odd.  Equation `M_DE M_DE^T=qI+J-A_2^2` reduces the first
  completion step to a canonical binary factorization/block-decomposition
  theorem, followed by uniqueness of the geometric resolutions.
- No computation was run, so no manifest or Lead lease was needed.
- The all-simple-groups target remains open and
  `active_assignment_answered:no`.
- `2026-08-17T22:45:59Z` — packaging complete at official cumulative active
  minute 76; 17 minutes charged in this increment and 28 minutes returned
  unused.  Entering `awaiting_lead`.
