---
title: "Partial results — parity exclusion of {39,25,10;1,5,30} and fixed-polar coclique computation"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/conjectured
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Partial result

## Stronger constituent-independent update

The entire intersection array `{39,25,10;1,5,30}` is arithmetically infeasible, independently of the distance-3 constituent. Indeed `a_1=39-25-1=13`, so every local graph would be 13-regular on 39 vertices, contradicting the handshake lemma because `39*13=507` is odd. The same contradiction follows directly from the frozen `M^2` identity by restricting `M` to a closed-neighbourhood row support. Full proof: `integral-obstruction.md`.

This remains only `PARTIAL_RESULT` for Problem 21.90 because the active existential target is not restricted to this array. `active_assignment_answered: no`.

## Exact bounded claim

I believe there is no distance-regular graph with intersection array `{39,25,10;1,5,30}` whose distance-3 graph is the explicit standard polar graph `NO_5^{-perp}(5)`. This excludes asymmetric as well as vertex-transitive fissions of that one constituent, subject to independent validation of the exact maximum-coclique computation.

It does **not** answer Problem 21.90: a nonisomorphic `srg(300,65,10,15)` distance-3 constituent or a different feasible array remains possible.

## Structural reduction

Let `B=A_3` be the fixed distance-3 adjacency matrix and `X=A_1` the proposed graph. The intersection array forces

\[
XB=10A_2+9B=10J-10I-10X-B.
\]

For any vertex `u`, the closed `X`-neighbourhood

\[
C_u=\{u\}\cup N_X(u)
\]

has 40 vertices. It is a coclique in `B`: support disjointness handles pairs involving `u`; and if `v in N_X(u)`, the `(u,v)` entry of `XB` is zero, so `v` has no `B`-neighbour anywhere in `N_X(u)`. Therefore any such fission requires `alpha(B)>=40`.

The stronger exact equivalence, including the binary matrix identities and the maximum-coclique compatibility CSP, is in `constraints.md`.

## Computation

Object: the 300 projective points of nonsquare quadratic type for

\[
Q(x)=x_1x_2+x_3x_4+x_5^2
\]

over `GF(5)`, adjacent in `B` when perpendicular under the polar form. This is the same explicitly reviewed standard constituent, reconstructed from coordinates.

Software: GAP 4.12.1, GRAPE 4.9.0. Exact bounded command:

```bash
timeout 55s gap -q Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/scratch/enumerate_coclique_orbits.g
```

Observed normal exit in about two seconds:

```text
vertices=300 degrees=[ 65 ] common_counts=[ 10, 15 ]
aut_order=9360000 vertex_orbit=300
orbit_representatives=0
maximum_coclique_size=30
trivial_group_size40_count=0
```

The script first performed an exact orbit-representative search for 40-cocliques under the full automorphism group, then used GRAPE's exact `MaximumClique` routine and found maximum size 30, and finally repeated the size-40 existence test with the trivial graph group. The last test prevents any accidental restriction to invariant cocliques. Full transcript: `scratch/enumerate_coclique_orbits.out`.

## Active-scope constraint matrix

| constraint_id | role | required condition | bounded result / proof use | evidence | result for full active target |
|---|---|---|---|---|---|
| 21.90-exists-Gamma | admissibility | one graph satisfying all rows | one fixed constituent is excluded; no graph constructed | this note | not established |
| 21.90-diameter-3 | admissibility | diameter exactly 3 | exact matrix system would force diameter 3, but has no solution for fixed `B` | `constraints.md` | not established globally |
| 21.90-Q-polynomial-distance-regular | admissibility | Q-polynomial distance-regular | any solution of the system would have `P=Q`; fixed `B` is excluded | `constraints.md` | not established globally |
| 21.90-distance-graph-definition | admissibility | `Gamma_i` are exact distance relations | proved for any solution of (F1)–(F2) | `constraints.md` | conditional only |
| 21.90-Gamma2-strongly-regular | admissibility | nontrivial strongly regular `Gamma_2` | any solution would give `srg(300,195,130,120)` | `constraints.md` | conditional only |
| 21.90-Gamma3-strongly-regular | admissibility | nontrivial strongly regular `Gamma_3` | fixed standard `B` is `srg(300,65,10,15)` | transcript and reviewed polar note | passes only in bounded subproblem |
| 21.90-existence-conclusion | target_conclusion | at least one such graph exists | neither proved nor violated by excluding one constituent | this note | open |

`active_assignment_answered: no`.

## What this does not establish

- It does not exclude other feasible intersection arrays in the source-paper families.
- It does not settle the full existential target.
- The maximum-coclique upper bound is a completed exact computation, not yet an independently checked hand proof or Validator replication.

## How this could be wrong

1. The coordinate graph could differ from the intended standard constituent, although the vertex count, SRG parameters, automorphism-group order, and prior reviewed construction all agree.
2. A GRAPE clique-search defect could give a false upper bound; Validator should repeat with an independent implementation or trusted graph file.
3. The `XB` identity could have an index-convention error; it follows directly from `A_1A_3=b_2A_2+a_3A_3=10A_2+9A_3` and should be checked independently.
4. The array exclusion could be mistakenly promoted to the full target; other parameter arrays remain open.

The older fixed-polar computation alone said nothing about a different `srg(300,65,10,15)` constituent. The new parity argument eliminates the array itself, so alternate constituents for this same array no longer need study.

