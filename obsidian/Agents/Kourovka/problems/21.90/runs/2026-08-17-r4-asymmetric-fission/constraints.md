---
title: "Exact asymmetric-fission constraints for {39,25,10;1,5,30}"
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
bounded_target: "Fissions of one fixed srg(300,65,10,15), especially the explicit standard polar constituent"
---

# Exact asymmetric-fission constraints

## Bounded target and limitation

Fix a labelled graph with adjacency matrix `B` satisfying

\[
B^2=50I+15J-5B,
\]

so `B` is `srg(300,65,10,15)` with spectrum `65^1,5^195,(-10)^104`. For the intended first experiment, `B` is the explicit standard 300-vertex nonsquare-type perpendicularity graph reviewed in `Agents/Kourovka/problems/21.90/verification/2026-08-12-polar-fission.md`.

This note asks only whether that fixed `B` can be the distance-3 relation of a (possibly asymmetric) distance-regular graph with intersection array

\[
\{39,25,10;1,5,30\}.
\]

A negative result would not cover nonisomorphic `srg(300,65,10,15)` constituents and would not settle Problem 21.90.

## Distance algebra

Write `X=A_1` for the unknown adjacency matrix and

\[
A_2=J-I-X-B.
\]

The array gives distance valencies

\[
(k_0,k_1,k_2,k_3)=(1,39,195,65)
\]

and `a_1=13,a_2=24,a_3=9`. Exact fission is equivalent to the following binary/support conditions and two matrix identities:

\[
\begin{aligned}
&X=X^T,\quad X_{uu}=0,\quad X_{uv}\in\{0,1\},\quad X\circ B=0,\\
&X^2=34I+8X+5J-5B,\tag{F1}\\
&XB=10J-10I-10X-B.\tag{F2}
\end{aligned}
\]

The diagonal of (F1) forces every row of `X` to have weight 39. Entrywise, (F1) says that two vertices have respectively 13, 5, or 0 common `X`-neighbours according as their pair lies in `X`, `A_2`, or `B`. Equation (F2) says that `N_X(u)` meets `N_B(v)` in respectively 0, 10, or 9 vertices in those same three cases.

Conversely, (F1)–(F2) give

\[
XA_2=25X+24A_2+30B.
\]

Thus `X,A_2,B` are exactly the distance-1, distance-2, and distance-3 relations of a connected diameter-3 graph and have the required intersection numbers. In particular, a `B`-pair has no walk of length at most 2 and has a walk of length 3.

## Maximum-coclique form

Set

\[
M=I+X.
\]

Then the exact system becomes

\[
\begin{aligned}
&M=M^T,\quad M_{uu}=1,\quad M_{uv}\in\{0,1\},\quad M\circ B=0,\tag{C0}\\
&M(B+10I)=10J,\tag{C1}\\
&M^2=25I+10M+5J-5B.\tag{C2}
\end{aligned}
\]

Equation (C1) forces row weight 40. If `C_u={v:M_{uv}=1}`, then `C_u` is a 40-coclique of `B`: vertices inside `C_u` have zero `B`-neighbours in it and vertices outside have exactly 10. The Hoffman bound

\[
\alpha(B)\le \frac{300\cdot10}{65+10}=40
\]

shows that every `C_u` is maximum. Conversely, every maximum 40-coclique of `B` has this `0/10` equitable property, so (C1) is automatic once all rows are chosen from the maximum-coclique family.

For distinct `u,v`, (C2) is exactly

\[
|C_u\cap C_v|=
\begin{cases}
15,&v\in C_u,\\
5,&B_{uv}=0\text{ and }v\notin C_u,\\
0,&B_{uv}=1.
\end{cases}\tag{C3}
\]

Symmetry means `v in C_u` iff `u in C_v`. Notice that for a `B`-edge, intersection zero follows already from symmetry plus the coclique property: a common point `w` would put the adjacent pair `u,v` together in `C_w`.

Hence the fixed-constituent fission problem is exactly:

> Choose, for every vertex `u`, a maximum 40-coclique `C_u` containing `u`, so that incidence is symmetric and every non-`B` pair of chosen cocliques intersects in 15 points when incident and 5 points otherwise.

No transitivity or automorphism assumption occurs in this formulation.

## Finite compatibility CSP

Let `F` be the complete family of maximum 40-cocliques of `B` and

\[
D_u=\{C\in F:u\in C\}.
\]

The variables are one choice `C_u in D_u` for each of 300 labelled vertices. Candidates `(u,C)` and `(v,D)` are compatible precisely when all of the following hold:

1. `v in C` iff `u in D`;
2. if `B_uv=1`, then `|C intersect D|=0`;
3. if `B_uv=0` and `v in C`, then `|C intersect D|=15`;
4. if `B_uv=0` and `v notin C`, then `|C intersect D|=5`.

Seeking one candidate from every part `D_u` with all pairs compatible is a finite 300-partite clique/CSP and is equivalent to (C0)–(C2). Arc consistency and smallest-domain branching are sound. A satisfying assignment directly outputs `M`; an exhaustive empty search is a fixed-constituent nonexistence certificate provided the family `F` was exhaustively enumerated.

## Spectral and Q-polynomial certificate

Any solution has

\[
\operatorname{Spec}(X)=\{39^1,14^{39},(-1)^{195},(-6)^{65}\}.
\]

The eigenmatrix in the distance ordering is

\[
P=Q=
\begin{pmatrix}
1&39&195&65\\
1&14&-5&-10\\
1&-1&-5&5\\
1&-6&15&-10
\end{pmatrix}.
\]

Thus the resulting scheme is formally self-dual; its Krein array equals the intersection array, giving the required Q-polynomial ordering. Moreover,

\[
A_2^2=75I+10A_2+120J,
\]

so `A_2` is the connected noncomplete `srg(300,195,130,120)` with three eigenvalues `195,15,-5`, while the fixed `B=A_3` is the connected noncomplete `srg(300,65,10,15)` with three eigenvalues `65,5,-10`. Therefore a solution of the exact system passes the revision-3 nontrivial strong-regularity convention.

## Bounded construction gate and observed result

Stage A is an exact orbit-representative enumeration of the 40-cocliques of the standard polar `B` under `Aut(B)`, using `scratch/enumerate_coclique_orbits.g`. It does not assume the desired fission is invariant: had orbit representatives existed, every orbit would have been expanded to form the full row-domain family `F`.

The frozen script completed far below the heavy-job threshold, so no lease was requested. Exact command:

```bash
timeout 55s gap -q Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/scratch/enumerate_coclique_orbits.g
```

With GAP 4.12.1 and GRAPE 4.9.0 it exited normally in about 2 seconds. It reconstructed `B`, checked 300 vertices, degree 65, common-neighbour values 10 and 15, and automorphism-group order 9,360,000. It then returned:

```text
orbit_representatives=0
maximum_coclique_size=30
trivial_group_size40_count=0
```

The full transcript is `scratch/enumerate_coclique_orbits.out`. The last line is a second exact size-40 search after replacing the graph group by the trivial group, so the absence is not an artifact of forcing an invariant coclique. `MaximumClique` also supplied an explicit 30-coclique.

Therefore the required 40-coclique row domain is empty for this fixed standard polar constituent. Subject to independent validation of the exact clique computation, this is a structural inconsistency excluding **all** fissions over this constituent, asymmetric as well as vertex-transitive.

The gate in general remains:

- no representative after an exact completed search: no fission over this constituent;
- a manageable full family: build the exact compatibility CSP above;
- an unmanageably large family or timeout: abandon coclique enumeration as the current implementation route and encode (C0)–(C2) directly in an approved SAT/CP solver.

This stage cannot prove nonexistence after a timeout and cannot claim the full Kourovka target after this negative fixed-constituent result. Nonisomorphic `srg(300,65,10,15)` constituents and all other feasible arrays remain open.

