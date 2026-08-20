---
title: "21.52 partial result — transvection flags in PSL_n(2)"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
strategy_id: LIN2-TRANSVECTION-FLAG
outcome: PARTIAL_RESULT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/projective-geometry
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
  - Agents/Kourovka/problems/21.52/ideas/2026-08-17-psln2-transvection-flag-reconstruction.md
---

# Scope and exact partial claim

Let `n>=3`, let `V=F_2^n`, let

\[
L=\operatorname{PSL}_n(2)=\operatorname{GL}_n(2),
\]

and let `D` be the single conjugacy class of rank-one transvections in `L`.
The candidate argument below claims that every permutation of `D` preserving `|xy|` for all
distinct `x,y in D` is the restriction of an automorphism of `L` stabilizing `D`.

This is an infinite-family partial result only. It says nothing about the other
involution classes of these groups or about any other finite nonabelian simple
group. In particular it does **not** prove the universal assertion in Problem
21.52, and the scope row `21.52-forall-L-D` remains uncovered.
`active_assignment_answered: no`.

# 1. The admissible transvection class

For an incident point--hyperplane flag `(P,H)` in `V`, there is a unique nonzero
vector `u` with `P=<u>` and a unique nonzero functional `f in V*` with
`H=ker(f)`: over `F_2` there is no nontrivial scalar ambiguity. Incidence says
`f(u)=0`. Put

\[
t_{u,f}=I+u\otimes f,\qquad (u\otimes f)(x)=f(x)u.
\]

Writing `A=u tensor f`, we have `A^2=f(u)A=0`, hence
`t_{u,f}^2=I`; it is nonidentity because `u,f` are nonzero. The flag-to-matrix
map is injective: the image and kernel of `t_{u,f}-I` recover `P` and `H`.

For `s in GL(V)`,

\[
s t_{u,f}s^{-1}=t_{su,\,f\circ s^{-1}}.
\]

The general linear group is transitive on incident point--hyperplane flags
(extend a basis of `P` to one of `H`, then to one of `V`, and map one such adapted
basis to another). Thus these matrices form one conjugacy class `D`. As a check
on the parametrization, it has

\[
|D|=(2^n-1)(2^{n-1}-1),
\]

because there are `2^n-1` points and `2^(n-1)-1` hyperplanes through each point.

Finally `F_2^*={1}`, so the determinant map is trivial and
`GL_n(2)=SL_n(2)`. Its centre consists only of the identity scalar, so
`PSL_n(2)=SL_n(2)=GL_n(2)`. The standard simplicity theorem for projective special
linear groups says that `PSL_n(q)` is simple for `n>=2` except `(n,q)=(2,2)` and
`(2,3)`; hence the groups here are finite simple for every `n>=3`. They are
nonabelian, for example `I+E_12` and `I+E_23` do not commute. Therefore `(L,D)`
satisfies the finite/nonabelian/simple and single-involution-class rows of the
active scope.

# 2. Exact product orders

Take two **distinct** flags `(u,f)` and `(v,g)` and set

\[
A=u\otimes f,\quad B=v\otimes g,\quad
a=f(v),\quad b=g(u).
\]

Here `A^2=B^2=0`, while

\[
AB=a\,u\otimes g,\qquad BA=b\,v\otimes f.
\]

The exact table is

| `(a,b)` | `|t_{u,f}t_{v,g}|` |
|---|---:|
| `(0,0)` | `2` |
| `(1,1)` | `3` |
| `(1,0)` or `(0,1)` | `4` |

All rows already occur in dimension `3`: with `e_i^*` the coordinate
functionals, one may take respectively
`(u,f;v,g)=(e_1,e_2^*;e_1,e_3^*)`,
`(e_1,e_2^*;e_2,e_1^*)`, and
`(e_1,e_2^*;e_2,e_3^*)` for `(0,0)`, `(1,1)`, and `(1,0)`; the `(0,1)` case
follows by swapping the two flags. These are hand checks only, not inputs to the
proof.

For `(a,b)=(0,0)`, `AB=BA=0`, and therefore

\[
(t_{u,f}t_{v,g})^2=(I+A+B)^2=I.
\]

The product is not `I`: that would give `A=B`, hence the same recovered image and
kernel and therefore the same flag, contrary to distinctness. Its order is exactly
`2`.

For `(a,b)=(1,1)`, `u,v` are linearly independent. The restrictions of `(f,g)`
to `S=<u,v>` have matrix `[[0,1],[1,0]]`, so

\[
V=S\oplus(\ker f\cap\ker g).
\]

Both transvections fix the second summand pointwise. On the ordered basis `(u,v)`
of `S`, their product sends

\[
u\longmapsto v,\qquad v\longmapsto u+v.
\]

It consequently has order exactly `3` on `S` and hence on `V`.

For `(a,b)=(1,0)`, write

\[
t_{u,f}t_{v,g}=I+N,\qquad N=A+B+AB.
\]

Here `BA=0`. Expanding and using `A^2=B^2=0` gives

\[
N^2=AB=u\otimes g\ne0,\qquad N^3=0.
\]

Thus `(I+N)^2=I+N^2` is nonidentity, while `(I+N)^4=I`; the order is exactly
`4`. In the remaining asymmetric case `(a,b)=(0,1)`, now `AB=0` and
`N=A+B`, so

\[
N^2=BA=v\otimes f\ne0,\qquad N^3=0,
\]

and the same conclusion follows.

Consequently two distinct vertices `(P,H)` and `(Q,J)` have colour `2` exactly
when

\[
P\le J\quad\hbox{and}\quad Q\le H. \tag{*}
\]

# 3. All maximal colour-2 cliques

For every nonzero proper subspace `U<V`, define

\[
K_U=\{(P,H): P\le U\le H\}.
\]

Condition `(*)` shows at once that `K_U` is a colour-2 clique.

Conversely, let `C` be a colour-2 clique and set

\[
U=\langle P:(P,H)\in C\rangle.
\]

For each `(Q,J) in C`, its own incidence gives `Q<=J`, and `(*)` gives
`P<=J` for every other point coordinate `P` occurring in `C`. Hence `U<=J` for
every hyperplane coordinate `J` in `C`; by construction every point coordinate
lies in `U`. A maximal clique is nonempty, so `U!=0`; and `U` lies in any one of
the proper hyperplanes occurring in `C`, so `U<V`. Therefore
`C` is contained in `K_U`. If `C` is maximal, this forces `C=K_U`.

Each `K_U` is itself maximal. Indeed, suppose a vertex `(Q,J)` outside `K_U` is
adjacent in colour `2` to every member of `K_U`. For each hyperplane `H>=U`,
choose any point `P<=U` and compare `(Q,J)` with `(P,H)`; similarly, for each
point `P<=U`, choose any hyperplane `H>=U`. Condition `(*)` then gives

\[
Q\le \bigcap_{H\supseteq U}H=U
\]

and every point of `U` lies in `J`, whence `U<=J`. (The displayed intersection
equals `U` because a vector outside `U` can be separated from `U` by a linear
functional.) Thus `(Q,J) in K_U`, a contradiction.

The two inclusions give the candidate classification

\[
\{\text{maximal colour-2 cliques}\}
=\{K_U:0<U<V\}. \tag{1}
\]

The parameter `U` is unique: the point coordinates occurring in `K_U` are all
the points of `U`, and their span is `U`.

If `r=dim(U)`, then over `F_2` the number of points in `U` is `2^r-1`, and the
number of hyperplanes containing `U` is the number of nonzero functionals on
`V/U`, namely `2^(n-r)-1`. Hence

\[
|K_U|=(2^r-1)(2^{n-r}-1). \tag{2}
\]

The endpoint value, for `r=1` or `r=n-1`, is `2^(n-1)-1`. If
`2<=r<=n-2`, put `a=r-1>=1` and `b=n-r-1>=1`; then

\[
\begin{aligned}
|K_U|-(2^{n-1}-1)
 &=2^{n-1}-2^r-2^{n-r}+2\\
 &=2(2^a-1)(2^b-1)>0.
\end{aligned}
\]

Thus for `n>=4` the unique dimensions giving minimum-size maximal cliques are
`r=1,n-1`. For `n=3` these are the only possible dimensions, so the same
description of the minimum cliques holds.

# 4. Intrinsic recovery of point--hyperplane incidence

Let `M` be the set, defined from the colour-2 graph alone, of its minimum-size
maximal cliques. By (1)--(2), its members are the endpoint cliques. When `U=P`
is one-dimensional, `K_U` is exactly the set of all flags with point
coordinate `P`; when `U=H` is a hyperplane, `K_U` is exactly the set of all flags
with hyperplane coordinate `H`. Therefore

\[
\mathcal M=\{K_P:P\text{ a point}\}\ \dot\cup\
           \{K_H:H\text{ a hyperplane}\}.
\]

Make a graph `Delta` on `M` by joining two members when their intersections as
subsets of `D` are nonempty. Distinct point stars are disjoint, as are distinct
hyperplane stars, while

\[
K_P\cap K_H=
\begin{cases}
\{(P,H)\},&P\le H,\\
\varnothing,&P\not\le H.
\end{cases} \tag{3}
\]

Therefore `Delta` is exactly the point--hyperplane incidence graph of
`PG(n-1,2)`. It is connected for `n>=3`: two points lie in a common hyperplane,
two hyperplanes contain a common point, and a nonincident point--hyperplane pair
is joined by a path through a point of the hyperplane and a hyperplane containing
the two points. Hence its two bipartition classes are intrinsic up to a global
swap.

An original flag `(P,H)` lies among the minimum cliques exactly in `K_P` and
`K_H`, and it is the unique element of their intersection in (3). A permutation
of `D` preserving all product orders preserves the colour-2 graph, hence permutes
its maximal cliques, their cardinalities, and their intersections. It therefore
induces an automorphism of `Delta`. The images of `K_P` and `K_H`, together with
their singleton intersection, recover the image of `(P,H)`; thus the induced
incidence action determines the original permutation of `D` exactly.

# 5. Realization by automorphisms of L

This final step uses the following precise form of the fundamental theorem of
projective geometry. For a projective space of dimension at least `2` over a
field, every bijection of points taking projective lines to projective lines is
induced by an invertible semilinear transformation. A type-preserving automorphism
of the point--hyperplane incidence graph takes lines to lines: the line through
two distinct points is the intersection, on point sets, of all hyperplanes
containing them, equivalently

\[
R\in\ell(P,Q)\quad\Longleftrightarrow\quad
(R\le H\text{ for every hyperplane }H\text{ with }P,Q\le H).
\]

Here the projective dimension is `n-1>=2`, and `F_2` has no
nonidentity field automorphism. The hypotheses include the low-dimensional case
`n=3`, where hyperplanes are projective lines themselves.

In fact, over `F_2` the needed conclusion also has a direct check. Each projective
point has a unique nonzero vector representative. If `phi` is the point action,
define `s(0)=0` and let `s(x)` be the unique vector representing `phi(<x>)` for
`x!=0`. Two distinct nonzero vectors `x,y` are independent, and the projective
line through them consists of the three points represented by `x,y,x+y`.
Line preservation therefore gives

\[
s(x+y)=s(x)+s(y).
\]

The same identity is immediate when one vector is zero or when `x=y`. Thus `s`
is additive, hence `F_2`-linear, and it is invertible because `phi` is bijective.
Its action on hyperplanes is `H -> sH`, because a hyperplane is determined by the
set of its incident points. This directly supplies the semilinear-theorem
conclusion with no hidden field automorphism.

Conjugation by `s` is an automorphism of `L`, and on flags it acts as

\[
t_{u,f}\longmapsto s t_{u,f}s^{-1}
=t_{su,\,f\circ s^{-1}},
\]

which is precisely `(P,H) -> (sP,sH)`.

For the type-swapping case, fix the standard nondegenerate bilinear form and write
`X^perp` for its orthogonal complement. The map

\[
(P,H)\longmapsto(H^\perp,P^\perp)
\]

is a fixed type-swapping incidence automorphism: orthogonal complementation
reverses inclusions, so `P<=H` is equivalent to `H^perp<=P^perp`, and
nondegeneracy makes double complementation the identity. Composing any type-swapping
incidence automorphism with this fixed one produces a type-preserving incidence
automorphism, so the preceding theorem accounts for all type-swapping actions as
well. On the group, the fixed swap is realized by the graph automorphism

\[
\iota:L\longrightarrow L,\qquad \iota(x)=(x^{-1})^T.
\]

This is a group automorphism because
`((xy)^(-1))^T=(x^(-1))^T(y^(-1))^T`. If `f(x)=w^T x`, then, since
`t_{u,f}^{-1}=t_{u,f}`,

\[
\iota(t_{u,f})=I+w u^T,
\]

Here `u^T w=f(u)=0`, so this is again a transvection, whose flag is
`(<w>,ker(u^T))=(H^perp,P^perp)`. Compositions of `iota` with
conjugations therefore realize every type-swapping incidence automorphism on `D`:
explicitly, if `sigma` swaps types and `delta` denotes the displayed fixed swap,
then `delta sigma` preserves types and is induced by some `s`; hence
`sigma=delta s` is induced by `iota` composed with conjugation by `s`. At the
minimum-clique level, conjugation sends `K_P,K_H` to `K_{sP},K_{sH}`, while
`iota` sends them to `K_{P^perp},K_{H^perp}` in the opposite types, so these
realizations agree with the reconstructed incidence action, not merely with its
point projection.

It follows that every product-order-colour-preserving permutation of this `D` is
the restriction of an automorphism of `L` stabilizing `D`. Conversely, any such
group automorphism preserves product orders, so for this family the two typed
permutation groups agree. In fact the reconstruction used only the order-`2`
relation, so the candidate statement is stronger: every automorphism of the
commuting graph on this transvection class is induced in the same way.

Equivalently, with the restriction map interpreted as in the canonical scope,

\[
\operatorname{Aut}_{\mathrm{col}}(\Gamma)
=\operatorname{res}_D\bigl(\operatorname{Stab}_{\operatorname{Aut}(L)}(D)\bigr)
\]

for this stated family and no broader one.

# Gate outcome

- `G0 — admissibility`: candidate pass for every `n>=3` and precisely the
  rank-one transvection class.
- `G1 — order table`: candidate pass; the only orders for distinct flags are
  exactly `2,3,4` as tabulated.
- `G2 — intrinsic reconstruction`: candidate pass; all maximal colour-2 cliques
  are the `K_U`, and only endpoint dimensions minimize their size.
- Incidence-recovery gate: candidate pass; minimum cliques and their nonempty
  intersections reconstruct the connected point--hyperplane incidence graph and
  every original flag.
- `G3 — realization`: candidate pass; type-preserving actions are conjugations,
  and type-swapping actions are compositions with inverse-transpose.
- `G4 — universal scope`: deliberately **not passed**. The universal Problem
  21.52 statement remains open after this family partial.

# Constraint-and-conclusion matrix for the partial family result

| constraint_id | role | use/result in this note |
|---|---|---|
| `21.52-forall-L-D` | admissibility | **Uncovered**: only the stated infinite family and class are treated. |
| `21.52-L-finite-nonabelian-simple` | admissibility | Passes for `L=PSL_n(2)`, `n>=3`. |
| `21.52-D-single-involution-class` | admissibility | Passes for the rank-one transvection class. |
| `21.52-Gamma-complete-on-D` | admissibility | Distinct pairs throughout are precisely the edges used above. |
| `21.52-edge-colour-exact-product-order` | admissibility | The exact orders `2,3,4` are derived in Section 2. |
| `21.52-tau-preserves-all-edge-colours` | admissibility | Such a `tau` preserves colour 2 and hence the reconstructed geometry. |
| `21.52-tau-induced-by-AutL` | target conclusion | The candidate argument supplies this only for the stated family/class, by conjugation and inverse-transpose. |

# What this does not establish / possible failure modes

- It does not address higher-rank involutions in `PSL_n(2)` or any other simple
  family, so it does not answer the universal notebook question.
- Although colour `2` alone reconstructs this particular transvection family, no
  claim is made about the separate universal question in Problem 21.53.
- Validator should independently check that point--hyperplane incidence recovers
  projective lines and that the direct `F_2` additivity argument works at `n=3`.
- Validator should independently expand the asymmetric nilpotence calculations and
  check that no equal-vertex case entered the edge table.
- No literature priority or staleness claim is made in this discovery-blind lane.

# Evidence mode

This artifact is a hand derivation. No group catalogue, enumeration, computer
algebra system, bespoke script, or numerical experiment was used.
