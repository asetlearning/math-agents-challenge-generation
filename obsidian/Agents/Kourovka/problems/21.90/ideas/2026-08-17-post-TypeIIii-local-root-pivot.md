---
title: "MathExpert strategy assessment — post-Type-II(ii) local-root pivot"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/conjectured
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
recommendation: STRATEGY_LIVE
active_assignment_answered: no
---

# Post-Type-II(ii) strategy assessment

## Scope control

`SCOPE:` `21.90/diameter-three-distance-graphs`  
`REVISION:` 3  
`TARGET:` construct one actual Q-polynomial distance-regular graph of diameter
three for which both distance-2 and distance-3 graphs are connected,
noncomplete, three-eigenvalue strongly regular graphs, or exclude all such
graphs.  
`CONVENTION EXCLUSION:` the superseded revision-2 cube and other degenerate
imprimitive distance graphs do not answer this target.

**Cited (local, 2026-08-17):** the controlling formulas and limitations below
come only from
`Agents/Kourovka/problems/21.90/verification/2026-08-17T130453Z-Type-IIii-package.md`
and
`Agents/Kourovka/problems/21.90/runs/2026-08-17-r5-triple-intersection/triple-intersection-gate.md`.
No formal tuple is treated as a graph.

## Obstruction

The missing invariant is **global realizability**.  Formal self-duality,
multiplicity integrality, and the primitive mod-2 consequence of the sole
nontrivial zero-Krein multiset are low-order necessary data.  The frozen
triple-intersection system has only three extra linear rows beyond its
marginals, while its coefficients vary over an infinite Diophantine family.
A sampled feasible system would therefore have almost no positive force, and
a complete uniform elimination is not a one-hour finite calculation merely
because there are finitely many base-distance types.

## Recommendation

Do **not** spend the next increment on all-base-type triple-intersection
elimination or on a new formal source family.  Grant one bounded increment to
`IIii-LOCAL-ROOT-120`, a representation-changing local-spectrum/root-lattice
test of the smallest exact even tuple.  This is the only option below with a
short, exact, target-faithful candidate exclusion chain and no heavy-compute
dependency.

This is not `PARK_RECOMMENDED` yet.  If the local-root chain hits its hard kill,
then the other reviewed-input options below do not justify another increment;
at that point I recommend `PARK_RECOMMENDED` unless a reviewed source-family
theorem or an explicit constituent graph is newly supplied.

## Rank 1 — `IIii-LOCAL-ROOT-120` — representation change

### Exact observable

**Cited (local, 2026-08-17):** the reviewed residual contains
`(x,w,u)=(1,2,2)`.  Substitution gives

\[
h=3,\quad t=4,\quad a=5,\quad k=17,
\]

the formal array

\[
\{17,8,6;1,2,12\},
\]

global eigenvalues `17,9,-1,-3`, and a local graph on `17` vertices of
degree `a+t-1=8`.

**General knowledge, unverified (must be derived or sourced before reliance):**
the standard local-eigenvalue inequality for a distance-regular graph says
that every nonprincipal local eigenvalue `eta` satisfies

\[
-1-\frac{b_1}{\theta_1+1}\leq \eta
\leq -1-\frac{b_1}{\theta_3+1}.
\]

Here `b_1=8`, `theta_1=9`, and `theta_3=-3`, so

\[
-\frac95\leq\eta\leq3.
\]

Thus the exact observable is whether a connected `8`-regular graph `L` on
`17` vertices can have `lambda_min(L)>=-9/5`.  Equivalently,
`2I+A(L)` would be a positive-definite integral Gram matrix of rank `17`.
Any `8`-regular graph on `17` vertices is connected, since two components
would each need at least `9` vertices.

The same inequality is below `-2` for every other positive even-residual tuple:
its lower endpoint is

\[
-\frac{h(u+1)}{h+u},
\]

which is greater than `-2` exactly when `u(h-2)<h`; with odd `h>=3`, `u>=2`,
and the reviewed square equation, this leaves only `(h,u,w,x)=(3,2,2,1)`.
So the experiment has an exact one-tuple scope and cannot silently expand.

### Candidate exclusion chain

**General knowledge, unverified (each implication needs checking):**

1. `2I+A(L)` positive definite realizes the `17` vertices as independent
   norm-two roots.  Connectedness of `L` makes the generated root system
   irreducible and simply laced.
2. Rank `17` leaves types `A_17` and `D_17`; exceptional `E` types have rank at
   most `8`.
3. In type `A_17`, the roots become the edges of a tree `H` with `17` edges,
   and `L` is its line graph.  Since `L` is `8`-regular, every edge `rs` of
   `H` has `deg(r)+deg(s)=10`.  A leaf then forces `H=K_{1,9}`, which has only
   `9` edges.
4. In type `D_17`, independence gives an odd-unicyclic graph `H` with `17`
   edges and again `L=L(H)`.  The equation `deg(r)+deg(s)=10` alternates
   degrees along paths; the odd cycle forces degree `5` everywhere, which is
   incompatible with a `17`-edge unicyclic graph.

This chain, if accepted after checking, excludes the array rather than merely
failing to construct it.  It does not answer the active existential scope.

### Bounded experiment and certificates

- **Exact next instruction:** `CONTINUE` the proof direction for at most `45`
  active minutes under strategy `IIii-LOCAL-ROOT-120`; write four explicit
  lemmas corresponding to the inequality, positive-definite root reduction,
  `A_17` case, and `D_17` case.  Use no catalogue and no heavy slot.
- **Success certificate:** a self-contained candidate lemma excluding an actual
  distance-regular graph with array `{17,8,6;1,2,12}`, with every inequality
  substitution displayed and the `A_17/D_17` sign and independence reductions
  spelled out.  Route it to Validator as a parameter-array partial only.
- **Failure certificate:** either an explicit `17`-vertex `8`-regular graph with
  least eigenvalue at least `-9/5`, or one named invalid implication in the
  local-bound/root-system/line-graph chain.  Numerical spectra or a failed graph
  search are not failure certificates.
- **Cost:** `35–45` active minutes, hand mathematics, no heavy compute.
- **Hard kill:** at `15` active minutes, stop unless the local-eigenvalue bound
  has been derived from accepted distance-regular identities or attached to a
  source Lead permits; at `30` minutes, stop unless both `A_17` and `D_17`
  translations are explicit.  Absolute stop at `45` minutes.

### Self-critique

The most likely failure is a sign or completeness gap in passing from a
positive-definite `0/1` Gram matrix to the asserted `A_17/D_17` line-graph
models.  The local-eigenvalue inequality and the root-system classification
are general knowledge, unverified here because browsing was forbidden.  Even a
successful chain removes only the smallest even tuple, so it is a partial with
high certifiability, not a family or scope conclusion.

## Rank 2 — `IIii-9TYPE-ILP` — refine the exhausted method

### Exact observable

**Cited (local, 2026-08-17):** positivity of the displayed intersection
numbers leaves exactly these nine unordered nondegenerate base-distance
multisets:

`111, 112, 122, 123, 133, 222, 223, 233, 333`.

For each type, let `S_UVW(u,w,x)` be the `64`-cell integer table `[rst]`
subject to the three marginal families `(M)`, forced base-point cells,
triangle-support zeros, nonnegativity, and the three zero-Krein rows `(T)`.
The observable is nonnegative integral feasibility of all nine parametric
systems, not feasibility at finitely many sampled tuples.

### Certificates, cost, and kill

- **Success certificate:** for one base type that must occur, an exact integer
  row-combination congruence or nonnegative Farkas identity whose residual has a
  fixed forbidden sign/residue on a stated even subfamily.
- **Failure certificate:** explicit parametric nonnegative integral tables for
  all nine types on the stated branch.  Rational tables or isolated integral
  samples do not exhaust the method.
- **Cost:** likely more than one heavy hour for symbolic Smith/lattice and cone
  elimination after a bespoke encoding; exact rationalization would add review
  cost.
- **Hard kill for any future gate:** after `20` active minutes, stop unless one
  base type yields either a forced denominator depending nontrivially on
  `u,w,x` or a reusable parametric lattice basis.  Do not continue as a tuple
  sampler.

### Self-critique

I have not computed the ranks after all triangle-support zeros, so a special
base type could collapse unexpectedly.  However the reviewed package supplies
only three extra zero-Krein rows, and a one-hour sampled ILP would not produce a
uniform success or failure certificate.  I therefore do not recommend this
increment now.

## Rank 3 — `IIii-120-FISSION` — switch to construction direction

### Exact observable

At `(x,w,u)=(1,2,2)`, seek symmetric disjoint `0/1` matrices
`A_0=I,A_1,A_2,A_3` on `120` vertices with sum `J` and products specified by

\[
\begin{array}{c|rrrr}
ij & p_{ij}^0&p_{ij}^1&p_{ij}^2&p_{ij}^3\\ \hline
11&17&8&2&0\\
12&0&8&9&12\\
13&0&0&6&5\\
22&68&36&40&36\\
23&0&24&18&20\\
33&34&10&10&8.
\end{array}
\]

Equivalently, start from an explicit `srg(120,34,8,10)` as `A_3` and seek a
`17+68` fission of its nonedges.  This changes direction from necessary
conditions to an actual target witness.

### Certificates, cost, and kill

- **Success certificate:** explicit edge lists or matrices plus exact product,
  connectedness, diameter, and `P=Q`/Q-polynomial checks.  This would be a
  candidate target witness for the full review circle.
- **Failure certificate:** `UNSAT` for one explicitly named finite constituent
  and one explicitly stated symmetry/CSP model.  It cannot exclude the tuple or
  scope outside that named search space.
- **Cost:** at least one leased heavy hour after an actual constituent and a
  bounded fission model are in hand.
- **Hard kill:** no search starts unless an explicit constituent is available
  within `10` active minutes.  No broad SRG generation and no inference from an
  absent transitive or orbital witness.

### Self-critique

A positive result has maximal value, but the reviewed package supplies no
constituent graph or complete finite catalogue.  The negative output of any
natural bounded search would be extremely narrow.  This is not ready for the
next increment.

## Another source family and park comparison

**Cited (local, 2026-08-17):** the package checks the displayed Type-I/II
substitutions only as algebraic maps into the master equation; it does not
authenticate their literature provenance or completeness, and it leaves Type
III and the Taylor branch untouched.  Under the present no-browse and
reviewed-input restriction, another family has no exact admissible parameter
space, coverage statement, or witness model.  Its first observable would be a
source theorem, not a graph invariant.  Therefore it cannot support a bounded
mathematical increment now; the hard kill is immediate until that input exists.

The four operational choices are therefore:

1. refine `(M)+(T)`: bounded base types but unbounded symbolic parameter space;
2. representation pivot: the exact local-root gate above, recommended once;
3. switch to construction: target-faithful but missing a finite constituent;
4. park: recommended immediately if the local-root gate fails its hard kill.

`ACTIVE ASSIGNMENT ANSWERED: no`.
