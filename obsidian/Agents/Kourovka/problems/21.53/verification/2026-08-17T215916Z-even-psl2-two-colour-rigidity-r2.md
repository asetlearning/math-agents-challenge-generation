---
title: "Verification — Kourovka 21.53 — even-characteristic PSL(2,q) rigidity, revision 2"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For every q=2^f with f>=2, the unique involution class D of PSL(2,q) satisfies Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)=PGammaL(2,q), and the q=5 pair is the identical A5 pair already covered at q=4."
claimant: Problem-21.53-Proof
target_statement: "For every finite nonabelian simple L and every involution conjugacy class D, Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma), where p is the second-smallest distinct prime divisor of |L|."
excluded_scopes: ["Problem 21.52's induction assertion", "unions of involution classes", "an arbitrary replacement prime", "promotion of a bounded family to the universal conclusion"]
target_object: "All pairs (L,D) with L finite nonabelian simple and D one complete involution conjugacy class."
witness_object: "All pairs with L=PSL(2,2^f), f>=2, on their unique involution class, plus the same abstract A5 pair presented as PSL(2,5)."
witness_equals_target: false
citation: "No external citation used; simplicity is derived by the Iwasawa argument below, and the exceptional A5 identifications are derived explicitly."
verification_method: "independent hand proof by exact matrix parametrization, affine-line reconstruction, and coordinate functional equations"
tools_used: ["GAP present but not invoked", "Python 3.12.3 version probe only; not used mathematically"]
scope_answered: ["21.53/even-characteristic-PSL2-family", "21.53/q5-identical-A5-pair"]
scope_not_answered: ["21.53/two-minimal-prime-colours", "odd-characteristic PSL(2,q) beyond the abstract q=5 transfer", "finite simple groups outside PSL(2,q)"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.53

## The claim

Let `q=2^f`, `f>=2`, let `L=PSL(2,q)`, and let `D` be its complete
involution class. On the complete graph on `D`, colour `{a,b}` by the exact
element order of `ab`. Then the two colours indexed by the two least prime
divisors of `|L|`, namely 2 and 3, determine every colour:

`Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)=PGammaL(2,q)`.

The assertion for `PSL(2,5)` is only the transfer of the `q=4` result through
the identical abstract pair
`PSL(2,4) isomorphic to A5 isomorphic to PSL(2,5)` and its unique involution
class. It is not an odd-characteristic-family argument.

## Scope, revision, and clause matrix

The locked scope is `21.53/two-minimal-prime-colours`, revision 2. Under the
Lead-imposed clean-context boundary, I did not reopen the source PDF or the
existing source-audit note; this verification uses the canonical revision-2
record, which records that independent source fidelity passed.

| clause | canonical requirement | result of this verification |
|---|---|---|
| inherited notation | finite nonabelian simple `L`; one complete involution class `D`; exact product-order colouring | established for every `PSL(2,2^f)`, `f>=2`, and the identical `A5` pair only |
| `Aut_t` | preserve the exact `t`-edge set; if it is empty, obtain all of `S_D` | used literally; the finite-permutation implication is upgraded to setwise equality below |
| full colour group | intersection of all exact occurring colour stabilizers | used literally; every exact product order is preserved |
| two minimal primes | use 2 and the least prime divisor above 2 | the latter is 3 throughout the bounded family |
| universal question | every finite nonabelian simple `L` and every involution class | not answered |

Consequently `active_assignment_answered:no` is mandatory even though the
bounded-family derivation below is complete.

## Constraint-and-conclusion matrix

| constraint_id | role | independent evidence | result |
|---|---|---|---|
| `21.53-forall-L-D` | admissibility | the proof quantifies over every `q=2^f`, `f>=2`, but not over every finite simple group | pass only for the bounded-claim gate; canonical row unknown |
| `21.53-L-finite-nonabelian-simple` | admissibility | `SL(2,q)=PSL(2,q)` and the Iwasawa argument below proves simplicity for `q>=4`; the transferred group is `A5` | pass for bounded claim |
| `21.53-D-single-involution-class` | admissibility | `x -> u_x` is a bijection from `F_q^2 minus {0}` onto all involutions, and conjugation is transitive | pass for bounded claim |
| `21.53-Gamma-product-order-colouring` | admissibility | for every distinct pair the product is taken in the exact matrix group and has characteristic polynomial `T^2+det(x,y)^2 T+1` | pass for bounded claim |
| `21.53-Aut-t-definition` | admissibility | a vertex permutation induces a bijection of the finite edge set, so one-way preservation of a fixed colour is setwise preservation; an absent colour imposes no condition | pass |
| `21.53-two-minimal-primes` | admissibility | `|L|=q(q-1)(q+1)`; 2 divides `q` and 3 divides one of `q-1,q+1` | pass; `p=3` |
| `21.53-full-colour-group-definition` | admissibility | the final semilinear maps induce actual automorphisms of `L`, hence preserve the exact order of every product | pass for bounded claim |
| `21.53-two-colours-determine-all` | target conclusion | affine-line recovery and the functional equations identify the two-colour intersection with the same semilinear group that preserves all colours | established for bounded claim only; canonical conclusion not established |

## Target vs witness

The canonical target is the class of all admissible pairs `(L,D)`. The submitted
witness is not one finite approximation or quotient: for each even prime power it
is the exact matrix group `SL(2,q)=PSL(2,q)` and its exact complete involution
class. Thus witness equality holds for each member of the claimed bounded family,
but the family is a strict subset of the canonical target. In the frontmatter,
`witness_equals_target:false` refers to this canonical mismatch.

There is no circularity. The vertices are derived from an arbitrary involution in
the matrix group, not manufactured from the desired graph relations. The order-2
and order-3 relations are then calculated from products in that group, and the
line-reconstruction argument begins only after those calculations.

## Sub-claims and what each method proves

| sub-claim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| exact group and class | elementary `2 x 2` algebra, counting, Iwasawa simplicity argument | admissibility and exact target object for every even `q>=4` | any odd family |
| selected colours | determinant/trace calculation and Cayley--Hamilton | exact order-2 and order-3 edge relations | yet that they determine other colours |
| rigidity | recovery of every affine line followed by coordinate functional equations | the entire two-colour intersection is determinant-one semilinear | preservation of other colours until the next step |
| all colours | induced matrix-group automorphism | exact preservation of every product order, including repeated-root cases | the universal all-simple-groups assertion |
| `q=5` | explicit exceptional-isomorphism and unique-class transfer | the identical abstract `(A5,D)` pair | a general odd-characteristic result |

## Evidence

### 1. The exact simple group and its two least prime divisors

Put `F=F_q`, `V=F^2`, and

`J = [[0,1],[1,0]]`.

In characteristic 2 the centre of `SL(2,q)` is trivial: a central scalar has the
form `cI` with `c^2=1`, hence `(c+1)^2=0` and `c=1`. Therefore
`SL(2,q)=PSL(2,q)`.

For completeness, simplicity for `q>=4` follows by the standard Iwasawa argument,
which is short in this case. The action on the projective line is faithful and
2-transitive, hence primitive. The subgroup

`U={u(t)=[[1,t],[0,1]] : t in F}`

is abelian and normal in a point stabilizer, and its conjugates (upper and lower
elementary matrices) generate `SL(2,q)`. The group is perfect: choose
`lambda in F^*` with `lambda != 1`. Since `q>=4` and the characteristic is 2,
`lambda^2 != 1`. For

`h=diag(lambda,lambda^(-1))`

one has

`h u(s) h^(-1) u(s)^(-1)=u((lambda^2-1)s)`.

Thus every element of `U` is a commutator, and the conjugates of `U` show that the
whole group is perfect. Finally, if `N` is a nontrivial normal subgroup in a
faithful primitive group, then `N` is transitive. For each `g`, choose `n in N`
with the same image of the fixed point as `g`; modulo `N`, `g` is represented by
an element of the point stabilizer and therefore normalizes the image of `U`.
Since the conjugates of `U` generate, the quotient by `N` is abelian. Hence the
commutator subgroup lies in `N`, and perfectness gives `N=G`. This proves
simplicity without importing a computational identification.

Counting determinant-one ordered bases gives

`|L|=|SL(2,q)|=(q^2-1)q=q(q-1)(q+1)`.

The prime 2 divides `q`. Since `q=2^f` is congruent to either 1 or -1 modulo 3,
the prime 3 divides `q-1` or `q+1`. There is no prime between 2 and 3, so the
second-smallest distinct prime divisor is exactly `p=3`.

### 2. Every involution, with no omission or duplication

For `0 != x in V`, define

`N_x=x(x^T J)` and `u_x=I+N_x`.

The alternating identity `x^T J x=0` gives `N_x^2=0`, while `tr(N_x)=0` and
`det(u_x)=1`. Hence `u_x^2=I`, and `N_x != 0`, so `u_x` is an involution.

The parametrization is injective. If `N_x=N_y`, equality of the rank-one images
first gives `y=cx`; then `N_y=c^2N_x`, so `c^2=1` and therefore `c=1` in
characteristic 2.

It is also exhaustive. If `g` is any involution, `N=g-I` is a nonzero rank-one
map with `N^2=0`, hence `im(N)=ker(N)=Fv` for some `v != 0`. Write `N=v phi`.
The functional `phi` and `v^T J` have the same kernel, so
`phi=c v^T J` for some `c != 0`. The finite field is perfect, so `c=d^2`; then
`N=N_{dv}`. Thus `x -> u_x` is a bijection from `V^*=V minus {0}` to all
involutions.

Every `A in SL(2,q)` preserves `J`, and direct substitution gives

`A u_x A^(-1)=u_{Ax}`.

Since `SL(2,q)` is transitive on nonzero vectors, all `q^2-1` involutions form
one conjugacy class `D`. This proves that the graph vertex set used below is the
complete required class.

### 3. The determinant dictionary for colours 2 and 3

For `x,y in V^*`, put `delta=det(x,y)=x^T J y`. A rank-one multiplication gives

`tr(u_x u_y)=delta^2`,

and the determinant is 1, so

`chi_(u_xu_y)(T)=T^2+delta^2 T+1`.                 (1)

Suppose throughout that `x != y`, as required for a graph edge.

If `delta=0`, then `y=cx` with `c != 0,1`, and

`u_xu_y=I+(1+c^2)N_x`

is a nonidentity unipotent of order 2. Conversely, an order-2 element of
`SL(2,q)` in characteristic 2 has trace 0, so (1) forces `delta=0`. Therefore

`|u_xu_y|=2  iff  x,y are linearly dependent`.     (2)

If `delta=1`, equation (1) and Cayley--Hamilton give
`(u_xu_y)^2+(u_xu_y)+I=0`, hence exact order 3. Conversely, a nonidentity
determinant-one element of order 3 has minimal polynomial `T^2+T+1`, hence trace
1. Equation (1) gives `delta^2=1`, and characteristic 2 then gives `delta=1`.
Thus

`|u_xu_y|=3  iff  det(x,y)=1`.                     (3)

Both selected colours occur for `q>=4`. If an arbitrary positive label `t` does
not occur, its edge set is empty and the revision-2 definition gives
`Aut_t=S_D` vacuously.

There is also no hidden reversal of the definition of `Aut_t`: a vertex
permutation induces a bijection on the finite set of unordered edges. If it maps
the `t`-edge set into itself, its restriction is an injection of that finite set
into itself and hence is onto. Thus the one-way source implication is equivalent
here to setwise preservation of the exact `t`-edge set.

### 4. Functional-equation derivation of the complete two-colour group

Use the bijection `x <-> u_x` to regard a permutation `tau` in
`Aut_2 intersect Aut_3` as a permutation of `V^*` preserving the relations in
(2) and (3) in both directions.

First recover all affine lines from these two relations.

- A line through 0 is `{0}` together with one dependence class in `V^*`.
  Since `q>=4`, it contains at least three nonzero points, and (2) makes its
  nonzero part an exact order-2 clique. Extend `tau` by `tau(0)=0`; it permutes
  all lines through 0.
- For `x != 0`, the order-3 neighbourhood is
  `H_x={y in V : det(x,y)=1}`. By (3),
  `tau(H_x)=H_(tau(x))`. Every affine line not through 0 has an equation
  `ell(y)=1` for a nonzero linear functional `ell`; nondegeneracy of the
  determinant form gives a unique `x` with `ell(y)=det(x,y)`. Hence the sets
  `H_x` are exactly all affine lines not through 0.

The extension of `tau` is therefore a bijection of the affine plane that maps
every affine line to an affine line. Disjoint lines remain disjoint, so parallel
classes are preserved.

Now the promised functional equations can be derived without evaluating a loop,
using a zero vector as a graph vertex, or assuming additivity. Let
`e_1=(1,0)`, `e_2=(0,1)`. Since `det(e_1,e_2)=1`, the matrix `A` with columns
`tau(e_1),tau(e_2)` has determinant 1. Replace `tau` temporarily by
`phi=A^(-1)tau`. Then `phi` still preserves the two relations, maps lines to
lines, and fixes `0,e_1,e_2`.

The two coordinate axes are fixed setwise. Parallelism then shows that there are
bijections `alpha,beta:F -> F`, both fixing 0 and 1, such that

`phi(a,b)=(alpha(a),beta(b))`.

The diagonal line is fixed because it contains 0 and `(1,1)`. Hence
`alpha(a)=beta(a)` for every `a`; call the common map `h`.

The line `y=ba` through 0 maps to the line of slope `h(b)`, so every point on it
gives the first functional equation

`h(ab)=h(a)h(b)`.                                      (4)

The line `y=a+b` is parallel to the diagonal and passes through `(0,b)`; its
image is therefore the line `y=a+h(b)`. Its points give the second equation

`h(a+b)=h(a)+h(b)`.                                    (5)

Together with bijectivity and `h(1)=1`, (4)--(5) say exactly that `h` is a field
automorphism `sigma` of `F`. Undoing the normalization,

`tau(x)=A x^sigma` with `A in SL(2,q)`.                 (6)

Conversely, every map in (6) preserves dependence and satisfies

`det(Ax^sigma,Ay^sigma)=det(x,y)^sigma`;

in particular it preserves determinant one. Therefore

`Aut_2(Gamma) intersect Aut_3(Gamma)=GammaSL(2,q)`.      (7)

This derivation covers the smallest claimed field `q=4`: its lines have three
nonzero points, so the dependence relation recovers them exactly, and every later
step remains valid. The sole smaller even field is `q=2`; there each origin line
has only one nonzero point and colour 2 is vacuous, so this reconstruction does
not apply. That is not a hidden exception to the claim because
`PSL(2,2) isomorphic to S_3` is not nonabelian simple and `f=1` is expressly
excluded. There are no other small-`f` exceptions.

### 5. Every product-order colour and the `PGammaL` name

For `tau` as in (6), define an actual automorphism of the exact matrix group by

`Phi(g)=A g^sigma A^(-1)`.

Because `A` has determinant one and `J` has entries in the prime field,

`Phi(u_x)=u_(A x^sigma)=u_(tau(x))`.

Consequently

`u_(tau(x))u_(tau(y))=Phi(u_xu_y)`.

An automorphism preserves exact element order. Thus every element of the group in
(7) preserves every occurring product-order colour, not merely the characteristic
polynomial. This last observation also disposes of any repeated-root concern.
Hence

`GammaSL(2,q) <= Aut(Gamma) <= Aut_2(Gamma) intersect Aut_3(Gamma)`,

and (7) proves equality throughout.

Finally, in even characteristic the squaring map on `F_q^*` is bijective. Every
projective semilinear class has a unique representative `(A,sigma)` with
`det(A)=1`: multiply an arbitrary matrix `B` by the unique scalar `c` satisfying
`c^2 det(B)=1`. These normalized representatives are closed under composition.
Thus their faithful action on the involutions identifies
`GammaSL(2,q)` with `PGammaL(2,q)`. This justifies the exact group name in the
claim rather than merely an equality of orders.

### 6. Exact `q=5` / `A5` transfer

For `q=4`, the already-proved simple group has order 60 and acts faithfully on
the five points of its projective line. Its image is an index-two subgroup of
`S_5`, hence `PSL(2,4) isomorphic to A_5`.

For `PSL(2,5)`, the order formula with the scalar centre gives order 60. The
classical exceptional identification can also be seen directly: in projective
images of `SL(2,5)`, take

`a=[[0,-1],[1,0]]`,  `b=[[0,-1],[1,1]]`.

Then `a` has projective order 2, `b` has projective order 3, and `ab` is, up to
the central scalar `-I`, the elementary unipotent `[[1,1],[0,1]]` of order 5.
The latter and its conjugate by `a` generate all upper and lower elementary
matrices over the prime field `F_5`, hence generate `PSL(2,5)`. The standard
icosahedral `(2,3,5)` presentation therefore gives a surjection from `A_5`, and
equality of orders makes it an isomorphism.

In `A_5`, every involution is a double transposition. There are 15 of them, and
the centralizer of one has order 4, so they form one conjugacy class. Any group
isomorphism between the two copies of `A_5` maps this entire class to the entire
class and satisfies

`|theta(a)theta(b)|=|theta(ab)|=|ab|`.

It therefore gives an isomorphism of the complete product-order-coloured graphs
and conjugates every `Aut_t` and the full colour group. Both copies have order 60,
whose two least prime divisors are 2 and 3. The `q=4` equality consequently
transfers exactly to the pair presented as `PSL(2,5)`.

### 7. Tool transcript

No mathematical computation was run: Lead required a frozen manifest and lease
before any computation, and none was needed. The mandatory availability probe was:

```text
$ which gap || true
$ which sage || true
$ which python3 || true
$ which magma || true
$ python3 --version 2>&1 || true
/usr/bin/gap
/usr/bin/python3
Python 3.12.3
```

GAP's version was not invoked and GAP was not used. Sage and Magma were not found.

## Verdict

`status/conjectured` under the certification state machine, with the following
mathematical finding: the bounded theorem for every simple `PSL(2,2^f)`, `f>=2`,
and the identical `PSL(2,5)=A5` pair passes this independent line-by-line hand
audit. The proof is certification-ready, but the protocol forbids assigning
`status/proven` until the human has seen the proof. That human-review gate is the
only reason the status is not raised in this note.

The universal revision-2 assignment is not answered.

## Why this verdict

The exact matrix object is the claimed bounded object; the involution model is
bijective and exhaustive; the selected colours are calculated as exact element
orders; the affine-line and functional-equation argument has no missing small
field in the claimed range; determinant-one semilinear maps induce actual group
automorphisms and therefore preserve all colours; and the `q=5` statement is an
exact abstract-pair transfer. No finite experiment, order comparison, or
characteristic-polynomial sufficiency assumption is being promoted to a theorem.

The status nevertheless stays at the default certification level because the
required human presentation has not occurred in this validator session.

## What is NOT established

- The canonical assertion for every finite nonabelian simple group is not proved.
- No general odd-characteristic `PSL(2,q)` rigidity lemma is proved. In particular,
  the odd orthogonal-shell step remains open.
- The finite `q=27` context is not evidence in this verification and yields no
  family inference.
- No simple group outside the stated even-characteristic family and the identical
  `A5` pair is covered.
- Problem 21.52's separate assertion is not addressed.
- `status/proven` has not been assigned because the human-review prerequisite is
  outstanding.

## What would upgrade it

Lead should present this bounded proof and verification note to the human. Once
that protocol gate is recorded, Validator may change the bounded claim to
`status/proven`; `active_assignment_answered` must still remain `no`. Closing the
active scope would additionally require a proof for every other admissible pair or
an admissible counterexample, neither of which is supplied here.
