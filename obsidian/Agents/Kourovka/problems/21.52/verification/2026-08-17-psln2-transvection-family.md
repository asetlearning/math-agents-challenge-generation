---
title: "Verification — Kourovka 21.52 — PSL_n(2) rank-one transvection family"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
claim: "For every n>=3, the product-order colour automorphisms of the rank-one transvection class in PSL_n(2)=GL_n(2) are exactly the restrictions of automorphisms of PSL_n(2) stabilizing that class."
claimant: Problem-21.52-Proof
target_statement: "For every finite nonabelian simple group L and every conjugacy class D of involutions in L, every permutation of D preserving |ab| for every pair of distinct vertices a,b is induced on D by an automorphism of L stabilizing D setwise."
excluded_scopes: ["Problem 21.53", "unions of involution classes", "uncoloured complete graph", "colouring by conjugacy class of ab", "bounded-family inference to the universal assertion"]
target_object: "the universally quantified family of every admissible pair (L,D) in Problem 21.52"
witness_object: "for arbitrary n>=3, L=PSL_n(2)=GL_n(2) and D is its rank-one transvection class, modelled by incident point-hyperplane flags"
witness_equals_target: false
citation: "the standard simplicity theorem for PSL_n(q): PSL_n(q) is simple except for PSL_2(2) and PSL_2(3); all remaining steps are proved directly below"
verification_method: "independent line-by-line hand reconstruction in finite-dimensional F_2-linear algebra and projective incidence geometry"
tools_used: ["GAP 4.12.1 availability probe only", "Python 3.12.3 availability probe only", "pdftotext/pdftoppm 24.02.0 for source rendering"]
scope_answered: ["family partial: rank-one transvections in PSL_n(2), n>=3 (not a canonical universal scope)"]
scope_not_answered: ["21.52/involution-class-product-order-colouring", "all other finite nonabelian simple groups and all other involution classes"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/projective-geometry, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.52 — PSL_n(2) transvection family

## The claim and verdict

The routed **family partial is mathematically correct**. Independently rebuilding
the argument gives

\[
\operatorname{Aut}_{\mathrm{col}}(D,|xy|)
=\operatorname{res}_{D}
  \bigl(\operatorname{Stab}_{\operatorname{Aut}(L)}(D)\bigr)
\]

when \(L=\operatorname{PSL}_n(2)=\operatorname{GL}_n(2)\), \(n\ge3\), and
\(D\) is the rank-one transvection class. In fact, the colour-2 relation alone
already forces this equality.

All requested hostile checks pass. In particular:

1. the two asymmetric order-four cases have different nilpotent parts but both
   have nilpotency index exactly three;
2. every colour-2 clique lies in a unique candidate \(K_U\), and every \(K_U\)
   is independently maximal;
3. for \(n=3\) there are no intermediate-dimensional \(U\), so the minimum
   maximal cliques are still exactly point and hyperplane stars;
4. their intersection graph is connected, making its bipartition intrinsic up
   to one global swap;
5. the direct \(\mathbb F_2\)-representative construction is genuinely additive,
   including the zero and equal-vector cases; and
6. if function composition is written rightmost-first, a type-swapping incidence
   action \(\sigma\) is induced by \(\iota\circ c_s\), not by an ambiguous
   unordered phrase, where \(c_s(x)=sxs^{-1}\) and
   \(\iota(x)=(x^{-1})^T\).

This is not a verdict on the universal notebook assertion. The canonical
universal row remains `unknown`; accordingly the formal scope status stays
`status/conjectured` and `active_assignment_answered: no`.

## Scope, revision, and clause matrix

The active record is revision 1 of
`21.52/involution-class-product-order-colouring`. The rendered source on PDF page
172 asks about every finite nonabelian simple \(L\) and every one of its
involution classes \(D\).

| source clause | source requirement | result here |
|---|---|---|
| `c-objects` | arbitrary finite nonabelian simple \(L\), arbitrary single involution class \(D\) | only the stated \(\operatorname{PSL}_n(2)\) family and rank-one class |
| `c-colouring` | complete graph on \(D\), edge colour exactly \(|xy|\) | fully handled for this family |
| `c-colour-automorphism` | arbitrary permutation preserving every exact edge colour | fully handled for this family |
| `c-question` | every such permutation is induced by \(\operatorname{Aut}(L)\) for every admissible pair | proved for this family only; universal conclusion open |

Problem 21.53 and all other exclusions in the scope record remain outside this
verification.

## Canonical constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | independent evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible pair \((L,D)\) | only \(L=\operatorname{PSL}_n(2)\), \(n\ge3\), and rank-one transvections | direct comparison with the source quantifier | **unknown / uncovered** |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(L\) finite nonabelian simple | \(\operatorname{GL}_n(2)=\operatorname{PSL}_n(2)\), \(n\ge3\) | determinant, centre, explicit noncommuting elements, standard PSL simplicity theorem | pass for family |
| `21.52-D-single-involution-class` | admissibility | one class, every member order exactly 2 | rank-one maps \(I+u\otimes f\), \(u,f\ne0\), \(f(u)=0\) | exact parametrization and flag transitivity | pass for family |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered pairs of distinct vertices | all two-flag cases classified by \((f(v),g(u))\in\mathbb F_2^2\) | exhaustive four-case calculation | pass for family |
| `21.52-edge-colour-exact-product-order` | admissibility | colour is exactly \(|xy|\) | orders 2, 3, and 4 | direct product calculation below | pass for family |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary colour-preserving \(\tau\) | arbitrary \(\tau\) preserves order 2, hence the reconstructed incidence geometry | intrinsic clique/intersection reconstruction | pass for family |
| `21.52-tau-induced-by-AutL` | target conclusion | extension for every admissible pair | conjugation or inverse-transpose after conjugation | explicit action calculation below | pass for family; **not proved universally** |

The first row is deliberately kept `unknown`, not converted into a pass by the
infinite size of this one family. It mechanically forces
`active_assignment_answered: no`.

## Target versus witness and circularity

The source target is a universal assertion about all admissible pairs \((L,D)\).
The witness/model is the exact matrix class

\[
D=\{I+u\otimes f:u\in V\setminus\{0\},\ f\in V^*\setminus\{0\},\ f(u)=0\},
\qquad V=\mathbb F_2^n,
\]

for arbitrary \(n\ge3\). This model equals the claimed rank-one transvection
class, as proved below, but it is not equal to the universal source target.
Therefore `witness_equals_target: false` has a logical, not computational, cause.

There is no circular construction. The vertices come from an ordinary conjugacy
class in the independently specified linear group. The colour relation is then
computed from multiplication. Neither the group nor \(D\) was manufactured from
the desired extension property.

## Subclaims and what each method proves

| subclaim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| witness is exactly the claimed class | rank-one linear algebra and conjugacy | family admissibility | equality with the universal target |
| exact orders | noncommutative nilpotent expansion and a two-space calculation | full edge-colour table for this class | another class's table |
| all maximal order-2 cliques | span of point coordinates, then a separate maximality test | clique classification \(K_U\) | which cliques have minimum size |
| endpoint minimum, including \(n=3\) | closed cardinality formula | minimum cliques are point/hyperplane stars | connectedness |
| intrinsic incidence structure | clique intersections and direct paths | bipartition up to global swap and recovery of every flag | linear realization |
| type-preserving realization | direct \(\mathbb F_2\)-additivity | conjugation realizes the action | type swaps |
| type-swapping realization | explicit polarity and inverse-transpose, with \(\circ\) order fixed | every swap is induced on \(D\) | the universal target |

## Evidence

### Source and availability probe

The source was read using the configured path, not a hard-coded PDF location:

```bash
source _meta/agents/Kourovka/paths.env
pdftotext -f 172 -l 172 -layout "$KOUROVKA_PDF" -
```

Relevant verbatim output:

```text
21.52. Let L be a finite non-abelian simple group, and let D be a conjugacy class
of involutions in L. Consider the complete graph Γ with vertex set D. Define an
equivalence relation ∼ (graph coloring) on the set of edges as follows: (a, b) ∼ (c, d)
if and only if |ab| = |cd|. An automorphism of the coloured graph Γ is a permu-
tation τ ∈ SD such that (a, b) ∼ (aτ , bτ ) for every edge (a, b). Is it true that the
automorphism group of Γ is a subgroup of Aut(L)?                        I. B. Gorshkov
```

The same page was rendered with `pdftoppm` and inspected visually; the flattened
text is \(S_D,a^\tau,b^\tau\). The bounded availability probe returned:

```text
GAP 4.12.1: /usr/bin/gap
Python 3.12.3: /usr/bin/python3
Sage: unavailable
Magma: unavailable
pdftotext 24.02.0: /usr/bin/pdftotext
pdftoppm 24.02.0: /usr/bin/pdftoppm
```

No mathematical computation, catalogue, web search, or heavy job was used.

### 1. Exact family and class

Let \(A=u\otimes f\), where \(A(x)=f(x)u\). The incidence condition
\(f(u)=0\) gives

\[
A^2=f(u)A=0,
\qquad
(I+A)^2=I
\]

in characteristic two. Since \(u,f\ne0\), this is a nonidentity involution and
\(\operatorname{rank}A=1\). Conversely, the nilpotent part of a rank-one
transvection has one-dimensional image, so it is \(u\otimes f\) for nonzero
\(u,f\), and square zero forces \(f(u)=0\). Over \(\mathbb F_2\) there is no
nontrivial simultaneous rescaling of \(u\) and \(f\). Thus the matrices are in
bijection with incident point-hyperplane flags

\[
(P,H)=(\langle u\rangle,\ker f).
\]

Their image and fixed hyperplane are respectively
\(\operatorname{im}(t-I)=P\) and \(\ker(t-I)=H\), so the flag is recovered
from the matrix.

For \(s\in\operatorname{GL}(V)\),

\[
s(I+u\otimes f)s^{-1}
=I+(su)\otimes(f\circ s^{-1}).                         \tag{1}
\]

An adapted-basis argument shows that \(\operatorname{GL}(V)\) is transitive on
incident flags, hence these matrices form one conjugacy class \(D\). There are

\[
|D|=(2^n-1)(2^{n-1}-1)
\]

of them.

Every invertible matrix over \(\mathbb F_2\) has determinant one, and the only
nonzero scalar is one. Hence

\[
\operatorname{GL}_n(2)=\operatorname{SL}_n(2)
=\operatorname{PSL}_n(2).
\]

The standard simplicity theorem for projective special linear groups applies for
all \(n\ge3\). The group is nonabelian, for example because
\(I+E_{12}\) and \(I+E_{23}\) do not commute. Thus \((L,D)\) is admissible.

### 2. Exact product-order table, including both asymmetric cases

For distinct flags write

\[
A=u\otimes f,\quad B=v\otimes g,\quad
a=f(v),\quad b=g(u).
\]

Then

\[
A^2=B^2=0,\qquad AB=a\,u\otimes g,\qquad BA=b\,v\otimes f.       \tag{2}
\]

If \((a,b)=(0,0)\), then \(AB=BA=0\), so

\[
((I+A)(I+B))^2=(I+A+B)^2=I.
\]

The product is not the identity: otherwise \(A=B\), which would give the same
recovered flag. Its order is exactly two.

If \((a,b)=(1,1)\), then \(u,v\) are independent and the restrictions of
\(f,g\) to \(S=\langle u,v\rangle\) are independent. Hence

\[
V=S\oplus(\ker f\cap\ker g).
\]

The product fixes the second summand pointwise and sends

\[
u\longmapsto v,\qquad v\longmapsto u+v.
\]

This has order exactly three on \(S\).

Now suppose \((a,b)=(1,0)\). Set

\[
(I+A)(I+B)=I+N,\qquad N=A+B+AB.
\]

Here \(AB=u\otimes g\ne0\) and \(BA=0\). Expanding in the noncommutative
algebra, using \(A^2=B^2=BA=0\), gives

\[
N^2=AB\ne0,
\qquad
N^3=(A+B+AB)AB=0.                                      \tag{3}
\]

Thus \((I+N)^2=I+N^2\ne I\), while \((I+N)^4=I\), so the order is four.

For the other asymmetric case \((a,b)=(0,1)\), the actual nilpotent part is
different:

\[
N=A+B
\]

because \(AB=0\). Now \(BA=v\otimes f\ne0\), and

\[
N^2=BA\ne0,
\qquad
N^3=(A+B)BA=ABA+B^2A=0                         \tag{4}
\]

because \(AB=B^2=0\). This again gives exact order four. The asymmetry has not
been hidden by swapping the two vertices.

Therefore the exhaustive table is

| \((f(v),g(u))\) | product order |
|---|---:|
| \((0,0)\) | 2 |
| \((1,1)\) | 3 |
| \((1,0)\) or \((0,1)\) | 4 |

and two distinct flags \((P,H),(Q,J)\) have colour two exactly when

\[
P\le J\quad\text{and}\quad Q\le H.                    \tag{5}
\]

### 3. Converse and maximality of every \(K_U\)

For each nonzero proper subspace \(U<V\), define

\[
K_U=\{(P,H):P\le U\le H\}.
\]

Equation (5) makes \(K_U\) a colour-2 clique.

Conversely let \(C\) be any nonempty colour-2 clique and put

\[
U_C=\langle P:(P,H)\in C\rangle.
\]

Fix \((Q,J)\in C\). Its own incidence gives \(Q\le J\), and (5) gives
\(P\le J\) for every other point coordinate in \(C\). Hence \(U_C\le J\)
for every hyperplane coordinate \(J\) of \(C\), while every point coordinate
lies in \(U_C\). It follows that

\[
C\subseteq K_{U_C}.                                    \tag{6}
\]

Moreover \(U_C\ne0\) and \(U_C<V\), because it lies in every proper
hyperplane occurring in the nonempty clique. If \(C\) is maximal, (6) forces
\(C=K_{U_C}\).

The converse inclusion in the classification requires a separate maximality
argument. Suppose a vertex \((Q,J)\notin K_U\) were colour-2 adjacent to every
member of \(K_U\). For every hyperplane \(H\supseteq U\), choose a point
\(P\le U\); comparison with \((P,H)\) gives \(Q\le H\). Therefore

\[
Q\le\bigcap_{H\supseteq U}H=U.                         \tag{7}
\]

The equality holds because any vector outside \(U\) is separated from \(U\) by
a linear functional. Conversely, varying \(P\le U\) in the same comparisons
gives \(P\le J\) for every point of \(U\), hence \(U\le J\). Equations (7)
and \(U\le J\) put \((Q,J)\) in \(K_U\), a contradiction. Thus every
\(K_U\) is maximal, and

\[
\{\text{maximal colour-2 cliques}\}
=\{K_U:0<U<V\}.                                        \tag{8}
\]

The parameter is unique because the point coordinates occurring in \(K_U\) are
all the points of \(U\), whose span is \(U\).

### 4. Minimum cliques, especially \(n=3\)

If \(r=\dim U\), then

\[
|K_U|=(2^r-1)(2^{n-r}-1).                              \tag{9}
\]

The two factors count points in \(U\) and hyperplanes containing \(U\),
respectively. At \(r=1,n-1\), the value is \(2^{n-1}-1\). For an interior
dimension \(2\le r\le n-2\),

\[
\begin{aligned}
|K_U|-(2^{n-1}-1)
 &=2^{n-1}-2^r-2^{n-r}+2\\
 &=2(2^{r-1}-1)(2^{n-r-1}-1)>0.                        \tag{10}
\end{aligned}
\]

For \(n=3\) there is no integer \(r\) satisfying \(2\le r\le n-2\): every
nonzero proper subspace already has dimension one or two. Thus (8), not an
extrapolation of the strict inequality, shows that the minimum maximal cliques in
dimension three are still exactly the point and hyperplane stars. No exceptional
third kind appears.

### 5. Connectedness, intrinsic bipartition, and recovery of flags

Let \(\mathcal M\) be the minimum-size maximal colour-2 cliques. By (8)--(10),

\[
\mathcal M
=\{K_P:P\text{ a point}\}\ \dot\cup\
 \{K_H:H\text{ a hyperplane}\}.                        \tag{11}
\]

Define \(\Delta\) intrinsically on \(\mathcal M\) by joining two distinct
members when their subsets of \(D\) intersect. Distinct point stars are disjoint,
as are distinct hyperplane stars, while

\[
K_P\cap K_H=
\begin{cases}
\{(P,H)\},&P\le H,\\
\varnothing,&P\not\le H.
\end{cases}                                             \tag{12}
\]

Hence \(\Delta\) is exactly the point-hyperplane incidence graph.

It is connected for every \(n\ge3\). Two points lie in a common hyperplane
because their span has dimension at most two and \(2\le n-1\). Two hyperplanes
meet in dimension at least \(n-2\ge1\), hence contain a common point. Finally,
if a point \(P\) is not incident with a hyperplane \(H\), choose a point
\(Q\le H\) and a hyperplane \(J\) containing \(P,Q\); then

\[
P-J-Q-H
\]

is a path. A connected bipartite graph has exactly two bipartition classes, unique
up to their simultaneous global swap. Thus the point/hyperplane type split is
intrinsic; it is not selected by an external label.

Every original flag \((P,H)\) is the unique point of \(K_P\cap K_H\). A
product-order-preserving permutation of \(D\) preserves the colour-2 graph, so it
permutes its maximal cliques, their sizes, and their intersections. It therefore
induces an automorphism of \(\Delta\), and (12) shows that this incidence action
determines the original permutation of \(D\) exactly.

### 6. Direct \(\mathbb F_2\)-linearity for type-preserving actions

Let \(\phi\) be the point action of a type-preserving automorphism of
\(\Delta\). Lines are incidence-definable. For distinct points \(P,Q\),

\[
R\in\ell(P,Q)
\quad\Longleftrightarrow\quad
R\le H\text{ for every hyperplane }H\text{ containing }P,Q.     \tag{13}
\]

The reverse direction in (13) follows by separating any vector outside
\(P+Q\) with a functional vanishing on \(P+Q\). Therefore \(\phi\) preserves
projective lines, including when \(n=3\).

Every point over \(\mathbb F_2\) has a unique nonzero representative. Define
\(s(0)=0\), and for \(x\ne0\) let \(s(x)\) be the representative of
\(\phi(\langle x\rangle)\). If \(x,y\) are distinct nonzero vectors, they are
independent and their projective line consists of the three points represented by

\[
x,\quad y,\quad x+y.
\]

Line preservation and bijectivity force the third image to be the unique third
point, so

\[
s(x+y)=s(x)+s(y).                                       \tag{14}
\]

If one vector is zero, (14) follows from \(s(0)=0\); if \(x=y\), both sides
are zero. Thus (14) holds for every pair. The map \(s\) is additive and hence
\(\mathbb F_2\)-linear. It is invertible because \(\phi\) is bijective. The
hyperplane action must be \(H\mapsto sH\), since a hyperplane is determined by
its incident points.

Conjugation \(c_s:x\mapsto sxs^{-1}\) is an automorphism of \(L\), and (1)
shows that it induces precisely

\[
(P,H)\longmapsto(sP,sH).                                \tag{15}
\]

### 7. Type-swapping actions and the exact composition order

Fix the standard nondegenerate bilinear form and let \(X^\perp\) denote
orthogonal complement. The polarity

\[
\delta(P,H)=(H^\perp,P^\perp)                          \tag{16}
\]

is an involutory type-swapping incidence automorphism.

Now let \(\sigma\) be any type-swapping incidence automorphism. We use standard
rightmost-first function composition. Then

\[
\mu:=\delta\circ\sigma
\]

is type-preserving, so by the preceding section \(\mu=\mu_s\) for some
\(s\in\operatorname{GL}(V)\), where \(\mu_s(P,H)=(sP,sH)\). Since
\(\delta^2=1\),

\[
\sigma=\delta\circ\mu_s.                               \tag{17}
\]

On the group define

\[
\iota(x)=(x^{-1})^T.
\]

This is an automorphism because

\[
\iota(xy)=((xy)^{-1})^T=(x^{-1})^T(y^{-1})^T
=\iota(x)\iota(y).
\]

Identify a functional \(f\) with a column \(w\) by \(f(x)=w^Tx\). Since a
transvection here is its own inverse,

\[
\iota(I+uw^T)=I+wu^T.                                  \tag{18}
\]

The flag of (18) is

\[
(\langle w\rangle,\ker u^T)=(H^\perp,P^\perp),
\]

so \(\iota\) induces exactly \(\delta\). Conjugation \(c_s\) induces
\(\mu_s\). Combining this with (17), the group automorphism

\[
\boxed{\ \iota\circ c_s\ }
\]

induces \(\delta\circ\mu_s=\sigma\). Explicitly, one first conjugates by
\(s\), then applies inverse-transpose. This resolves the only notationally
delicate composition issue. Equivalently, starting instead from
\(\sigma\circ\delta\) would produce a generally different parameter \(s'\) and
the realization \(c_{s'}\circ\iota\); the two conventions must not be mixed.

### 8. Completion of the family argument

Let \(\tau\) be any product-order-colour-preserving permutation of \(D\). It
preserves colour two, hence reconstructs an incidence automorphism \(\sigma\) of
\(\Delta\). Sections 6--7 produce an automorphism \(\alpha\in\operatorname{Aut}(L)\)
inducing \(\sigma\) on point and hyperplane stars. Since each transvection flag
is the singleton intersection of its two stars, \(\alpha|_D=\tau\).

Conversely every automorphism of \(L\) stabilizing \(D\) preserves the orders of
all products. Therefore the two permutation groups are equal for this family.

## Verdict

**PASS — gap-free family partial, with canonical status `status/conjectured`.**

The PSL\(_n(2)\) rank-one transvection theorem is supported by a complete
independent hand proof. It is usable as a reviewed partial result, but it does not
answer or close the active universal scope.

## Why this verdict

Every internal implication has been reconstructed, including the low-dimensional
case and both directions of the clique classification. The matrix class is the
claimed class in the claimed group; the incidence structure is reconstructed
intrinsically from the exact product-order relation; and both incidence types are
realized by explicit group automorphisms. The sole failed target comparison is
intentional and explicit: this witness family is strictly narrower than the
source's universal target.

## What is NOT established

- The row `21.52-forall-L-D` is not established and remains `unknown`.
- No higher-rank involution class in \(\operatorname{PSL}_n(2)\) is treated.
- No other finite nonabelian simple family is treated.
- The universal assertion in Problem 21.52 is neither proved nor refuted.
- Problem 21.53 is not answered.
- No literature-priority or staleness claim is made.

## What would upgrade it

Closing the active scope still requires either a proof covering every admissible
pair \((L,D)\), or one fully checked admissible counterexample. A dedicated
family-partial scope record could separately record this theorem as closed, but it
would not change `active_assignment_answered: no` for revision 1 of the universal
scope.
