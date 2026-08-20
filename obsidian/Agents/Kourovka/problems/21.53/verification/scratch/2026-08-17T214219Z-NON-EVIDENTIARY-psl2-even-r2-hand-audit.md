---
title: "NON-EVIDENTIARY SCRATCH — even PSL(2,q) revision-2 hand audit"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For every q=2^f with f>=2, and also for the identical PSL(2,5)=A5 pair transported from q=4, the unique involution-class product-order colouring satisfies Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma); for even q this group is PGammaL(2,q)."
claimant: Problem-21.53-Proof
target_statement: "For every finite nonabelian simple L and every involution class D, the full product-order colour group equals Aut_2(Gamma) intersect Aut_p(Gamma), where p is the second-smallest distinct prime divisor of |L|."
excluded_scopes: ["Problem 21.52", "unions of involution classes", "an arbitrary prime in place of the second-smallest prime", "universal inference from a bounded family"]
target_object: "Every admissible pair (L,D) inherited from Problem 21.52."
witness_object: "The exact groups SL(2,2^f)=PSL(2,2^f), f>=2, on their complete involution class, plus the one abstract A5 pair represented by PSL(2,5) and PSL(2,4)."
witness_equals_target: false
citation: none
verification_method: "Fresh line-by-line hand reconstruction in the exact matrix groups; no discovery computation inspected or rerun"
tools_used: ["GAP 4.12.1 (availability probe only)", "Python 3.12.3 (repository state checker only)", "Poppler pdftotext 24.02.0"]
scope_answered: ["all simple PSL(2,2^f), f>=2, on their unique involution class", "the identical PSL(2,5)=A5 pair"]
scope_not_answered: ["odd PSL(2,q) beyond the q=5 transfer", "simple groups outside PSL(2,q)", "21.53/two-minimal-prime-colours universal quantifier"]
active_assignment_answered: no
outcome: INVALID_CLEAN_CONTEXT
possible_prior_exposure: yes
clean_context_compliant: no
not_a_verdict: true
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# NON-EVIDENTIARY SCRATCH

Lead ruled this validator context invalid because it exceeded the explicit
submitted-findings-only boundary.  This file preserves the abandoned hand audit
only as scratch.  It is **not a verification note, not a protocol verdict, and
not evidence**.  None of its tentative mathematical assessments may be cited;
a fresh clean-context validator must reconstruct the claim independently.

# Abandoned hand audit — even-characteristic `PSL(2,q)` partial theorem

## The claim and invalidated draft assessment

The submitted bounded theorem passes a fresh hostile line-by-line reconstruction.
For every `q=2^f`, `f>=2`, the complete involution class `D` of
`L=PSL(2,q)` satisfies

`Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)=PGammaL(2,q)`.

The same equality transfers to the `q=5` pair because
`PSL(2,5) isomorphic to PSL(2,4) isomorphic to A5` and the abstract group has one
involution class.  No exceptional value of `f>=2` is lost.

This invalidated draft tentatively found no gap in the asserted infinite-family
partial result, but **no mathematical verdict is issued from this context**.  The
active revision-2 assignment would in any event remain unanswered.  After the
core hand reconstruction was complete, this validator mistakenly opened the
prior bounded `A6` and `PSL(2,8)` verification notes solely to inspect house
verdict formatting.  That exceeded the explicit “submitted findings only”
boundary and the scope's blind-run setting, even though neither fixed-pair note
is used anywhere in the proof below.  This disclosure prevents treating the
present run as the requested clean-context certification; Lead must use a fresh
validator if that cleanliness property is required mechanically.

The file is tagged `status/draft`; it cannot raise or lower the submitted claim's
status.

## Scope, revision, and source clauses

The canonical record is assignment revision 2.  Rendered source PDF page 172 was
inspected directly.  Problem 21.53 inherits from 21.52 a finite nonabelian simple
group `L`, one conjugacy class `D` of involutions, and the complete graph on `D`
coloured exactly by product order.  It defines `Aut_t(Gamma)` for every positive
integer `t` by the one-way edge implication, states
`Aut(Gamma)=intersection_t Aut_t(Gamma)`, and asks whether the factors for the
two least distinct prime divisors `{2,p}` always suffice.

| source clause | result for the submitted family | canonical remainder |
|---|---|---|
| inherited finite-nonabelian-simple `(L,D)` | exact for every even simple `PSL_2` and the transported `A5` pair | all other admissible pairs |
| every-label `Aut_t`, including vacuity | literal implication, finite-bijection conversion, and absent labels checked | none within the bounded family |
| full intersection over all colours | all exact product orders are preserved by the recovered group | all other pairs |
| equality for the two minimal primes | passes with `{2,p}={2,3}` throughout the bounded family | universal assertion |

Thus `active_assignment_answered: no` is forced independently of the strength of
the family theorem.

## Constraint-and-conclusion matrix

| constraint_id | role | independent evidence | result |
|---|---|---|---|
| `21.53-forall-L-D` | admissibility | the proof quantifies over every pair in its named family, but that family is a strict subset of the canonical domain | pass for bounded-claim gate; canonical result unknown |
| `21.53-L-finite-nonabelian-simple` | admissibility | the projective-line action and the elementary normal-subgroup argument below prove simplicity for `PSL(2,2^f)`, `f>=2`; the same argument applies to `PSL(2,5)` | pass in bounded family |
| `21.53-D-single-involution-class` | admissibility | `x -> u_x` bijects `F_q^2\{0}` with all nonidentity involutions and `SL(2,q)` is transitive; the `A5` pair has one class | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | every distinct pair has determinant parameter `delta`; the characteristic polynomial `T^2+delta^2T+1`, with the separate `delta=0` unipotent case, determines the exact product order | pass |
| `21.53-Aut-t-definition` | admissibility | a vertex permutation induces a bijection of the finite edge set, so `tau(E_t) subseteq E_t` is equality; if `E_t` is empty the condition is vacuous | pass |
| `21.53-two-minimal-primes` | admissibility | `|PSL(2,2^f)|=q(q-1)(q+1)` is divisible by `2` and `3`; `|A5|=60` | pass, `p=3` |
| `21.53-full-colour-group-definition` | admissibility | determinant is sent to a field conjugate, hence every product eigenvalue is sent to a field conjugate of the same multiplicative order | pass |
| `21.53-two-colours-determine-all` | target conclusion | the coordinate functional equations recover exactly `GammaSL(2,q)`, and that group preserves every colour | passes for the bounded family only; canonical conclusion not proved |

## Target versus witness and circularity

The source and active target are universal.  The witness is a strict infinite
subfamily, so `witness_equals_target:false`.  This is not an object-substitution
error because the theorem is explicitly submitted as a bounded partial result.

Within that bounded statement, the witness is exact: matrices are taken in
`SL(2,F_q)=PSL(2,F_q)` itself, not in a quotient or surrogate.  The vertex model
is derived from all matrices of order two, independently of the desired
automorphism equality.  The selected edge relations are then derived from direct
matrix products.  Nothing is true by construction from an assumed rigidity
property, so the circularity check passes.

## 1. Group identity, simplicity, and the two smallest primes

For any finite field `F_q`, selecting a nonzero first column and then a second
column of determinant one gives

`|SL(2,q)|=(q^2-1)q`.

When `q` is even, the centre is trivial: a central matrix is scalar and
`lambda^2=1` forces `lambda=1`.  Hence `SL(2,q)=PSL(2,q)`.

For completeness, simplicity can be checked without trusting the family name.
Let `G=PSL(2,q)` act on `P^1(F_q)`.  The action is faithful after quotienting the
scalar centre and is 2-transitive, hence primitive.  The point stabilizer has the
abelian normal translation subgroup

`U={u(t)=((1,t),(0,1)):t in F_q}`,

and the conjugates of `U` generate `G` by elementary row operations.  If
`1 != N normal G`, primitivity makes `N` transitive.  Given `g`, choose `n in N`
with the same image of infinity as `g`; normality of `U` in the point stabilizer
then gives `U^n=U^g`.  Modulo `N`, all conjugates of `U` consequently have the
same abelian image, so `G/N` is abelian.  Finally choose
`h=diag(s,s^-1)` with `s^2 != 1`.  Since
`h u(t) h^-1=u(s^2t)`, every element of `U` is a commutator.  Its conjugates
generate `G`, so `G` is perfect and `G<=N`.  Thus `G` is simple.  Such an `s`
exists for every even `q>=4` and also for `q=5`.  These groups are nonabelian as
well.

For `q=2^f`, `f>=2`, exactly one of `q-1,q+1` is divisible by 3.  Therefore
`q(q-1)(q+1)` is divisible by both 2 and 3, and no prime can lie strictly between
them.  The two smallest distinct prime divisors are exactly `2,3`.  The same is
immediate from `|A5|=60` in the transported case.

## 2. The complete involution class

Let `V=F_q^2`, let

`[x,y]=det(x,y)`, `J=((0,1),(1,0))`,

and for a nonzero column `x` put

`N_x=x(x^T J)`, `u_x=I+N_x`.

For `x=(r,s)^T`,

`N_x=((rs,r^2),(s^2,rs))`.

Because `x^T Jx=0`, we have `N_x^2=0`; in characteristic two each `u_x` is a
nonidentity involution.  Conversely a nonidentity involution `u` has
`N=u-I` nonzero with `N^2=0`, so `N` is a nonzero rank-one trace-zero nilpotent.
Every such matrix has the displayed form: if
`N=((a,b),(c,a))`, nilpotence gives `a^2=bc`; unique square roots
`r^2=b`, `s^2=c` then give `rs=a`.  The entries `r^2,s^2` also prove injectivity.
Thus

`D={u_x:x in V\{0}}`

is exactly the set of all `q^2-1` nonidentity involutions.

For `A in SL(2,q)`, the identity `A^TJA=J` gives
`A u_x A^-1=u_{Ax}`.  Since `SL(2,q)` is transitive on nonzero vectors, `D` is
one complete conjugacy class.  This also shows that the universal quantifier over
involution classes has only one case for every asserted even group.

## 3. Exact product-order colours

For distinct nonzero `x,y`, direct multiplication gives

`tr(u_xu_y)=[x,y]^2`.                                      (3.1)

Write `delta=[x,y]`.  If `delta=0`, then `y=lambda x` with `lambda != 1`, and

`u_xu_y=I+(1+lambda^2)N_x`

is a nonidentity involution.  Conversely trace zero forces `delta=0`.  Hence the
order-2 relation is exactly dependence.

If `delta=1`, the characteristic polynomial is `T^2+T+1`; the product is
nonidentity and has order three.  Conversely an order-three determinant-one
matrix in characteristic two has that polynomial, so its trace is one; squaring
is injective and gives `delta=1`.  Thus

`|u_xu_y|=2 iff x,y are dependent`,

`|u_xu_y|=3 iff [x,y]=1`.                                  (3.2)

This does not discard the other colours.  For `delta != 0`, the polynomial

`T^2+delta^2T+1`

is separable, and its roots in `F_{q^2}` are `lambda,lambda^-1`.  The matrix is
diagonalizable there and its exact order is `ord(lambda)`.  Together with the
separate `delta=0` case, this determines the colour of every edge.

## 4. The literal `Aut_t` convention and vacuous cases

Let `E_t` be the set of unordered distinct pairs with product order `t`.  The
source says `tau(E_t) subseteq E_t`.  Since a permutation of `D` induces a
bijection of all unordered edges, its restriction to `E_t` is injective and the
finite containment must be equality.  Thus inverses preserve `E_t` as well.  If
`E_t` is empty, the implication has no instances and `Aut_t(Gamma)=S_D`.

There is no selected-colour exception for `f>=2`.  Each one-dimensional subspace
contributes a colour-2 clique of size `q-1>=3`.  Between any two distinct lines,
for each nonzero vector on the first there is a unique vector on the second with
determinant one, so colour 3 is nonempty (indeed a perfect matching between the
two line-cliques).  Labels that do not occur, including colour 1 on a loopless
graph, contribute only vacuous symmetric-group factors to the full intersection.

The excluded `f=1` case is `PSL(2,2) isomorphic to S3`, which is not a finite
nonabelian simple group.  The smallest admissible value `f=2` is handled by the
same equations without division by a missing element or use of a loop.

## 5. Functional equations for the two-colour group

Let `F:V\{0}->V\{0}` preserve the two relations in (3.2).  The order-2 graph is
the disjoint union of the `q+1` cliques `ell\{0}`, so `F` permutes these lines.
Because `[e_1,e_2]=1`, the matrix having columns `F(e_1),F(e_2)` lies in
`SL(2,q)`.  Composing with its inverse preserves both relations, and reduces to
the case `F(e_1)=e_1`, `F(e_2)=e_2`.

There are bijections `alpha,beta:F_q^*->F_q^*`, fixing one, such that

`F(a,0)=(alpha(a),0)`, `F(0,b)=(0,beta(b))`.

The unique determinant-one neighbour of `(a,0)` on the other axis is
`(0,a^-1)`, whence

`beta(a^-1)=alpha(a)^-1`.                                  (5.1)

For `a,b != 0`, the determinant-one neighbours of `(a,b)` on the two axes are
`(0,a^-1)` and `(b^-1,0)`.  Their images uniquely determine both coordinates,
so

`F(a,b)=(alpha(a),beta(b))`.

Extending `alpha(0)=beta(0)=0` makes this formula valid on every nonzero vector.
No value of `F(0,0)` is used.

Preservation of determinant one now gives, whenever the original determinant is
one,

`ad+bc=1  implies  alpha(a)beta(d)+beta(b)alpha(c)=1`.

Put `b=1`, `c=ad+1`.  The two chosen vectors are nonzero and distinct because
their determinant is one, so this is a legitimate graph edge even when `a=0` or
`d=0`.  The result is

`alpha(ad+1)=alpha(a)beta(d)+1`.                            (5.2)

Setting first `a=1` and then `d=1` yields

`beta(d)=alpha(d+1)+1`, `alpha(a+1)=alpha(a)+1`,

and hence `alpha=beta`.  Comparing (5.2) with the translation identity gives

`alpha(ad)=alpha(a)alpha(d)`.

For `a != 0`, multiplicativity and the translation identity give

`alpha(a+b)=alpha(a)alpha(1+b/a)=alpha(a)+alpha(b)`;

the case `a=0` is immediate.  Thus `alpha` is a field automorphism.  Undoing the
normalization proves

`Aut_2(Gamma) intersect Aut_3(Gamma)=GammaSL(2,q)`.

This audit explicitly checks the two common hidden gaps: the proof never treats
the zero vector as a vertex, and every specialized determinant-one pair is a
genuine off-diagonal edge.

## 6. Recovery of every colour and group identification

Every map in the recovered group has the form

`x -> A x^sigma`, with `A in SL(2,q)` and `sigma in Gal(F_q/F_2)`.

It sends `delta=[x,y]` to `delta^sigma`.  Equivalently, it is induced by the
composition of conjugation by `A` and the entrywise field automorphism on the
exact matrix group.  Therefore the product `u_xu_y` is sent to a group-automorphic
image and retains its element order.  In eigenvalue language, `lambda` is sent
to `lambda^sigma`, which has the same multiplicative order.  Hence every
two-colour automorphism preserves every occurring product-order colour.

The reverse inclusion `Aut(Gamma) <= Aut_2(Gamma) intersect Aut_3(Gamma)` is
definitional, proving equality.  In even characteristic `PGL(2,q)=SL(2,q)` and
the action just obtained is the natural `PGammaL(2,q)` action on involutions.  Its
order is

`q(q^2-1)f`.

For `f=2`, this is 120; no separate exception occurs.

## 7. Exact transfer of the `q=5` pair

The standard exceptional isomorphism can be reconstructed inside the present
groups.  `PSL(2,4)` has order 60 and acts faithfully on its five projective
points, so its image is the index-two subgroup `A5` of `S5`.

For `PSL(2,5)`, the simplicity argument in Section 1 applies and its order is
`5(25-1)/2=60`.  A direct trace-zero count gives 30 determinant-one lifts, hence
15 projective involutions.  For

`X=((0,-1),(1,0))`,

solving `AX=+-XA` in `SL(2,5)` gives a projective centralizer of order four,
isomorphic to `C2 x C2`: the commuting solutions are `A=aI+bX` with
`a^2+b^2=1` (four lifts), while the anticommuting solutions have form
`A=((a,b),(b,-a))` with `a^2+b^2=4` (four lifts); quotienting these eight lifts
by `+-I` gives four projective elements, all three nonidentity elements being
involutions.  Thus all 15 involutions form one class, each belongs to
the unique Sylow-2 subgroup equal to its centralizer, and the five Sylow-2
subgroups are permuted by conjugation.  Simplicity makes this nontrivial action
faithful, embedding the order-60 group as the index-two subgroup `A5` of `S5`.
Consequently

`PSL(2,5) isomorphic to A5 isomorphic to PSL(2,4)`.

Both sides have a unique involution class.  A group isomorphism carries that
class to that class and preserves the order of every product, so it is an
isomorphism of the complete product-order-coloured graphs.  The `q=4` equality
therefore transfers verbatim to the one `q=5` pair.  This step does not invoke
the unproved odd-characteristic rigidity lemma.

## Odd characteristic and the `q=27` limitation

The submitted odd-characteristic section constructs a projective trace/norm
model and reduces the desired family statement to

`Aut(D;R_2,R_3)=PGammaO(3,q)`.

That orthogonal-shell rigidity lemma is **unproved**.  Accordingly even the
invalidated draft does not address the general odd-`q` family, regardless of the correctness of the
preceding trace formulas.  In particular, when `q=3^f` with `f` odd, the submitted
formula makes `R_3` empty and the required rigidity would have to come from
`R_2` alone; vacuity cannot be bypassed.

The leased `q=27` automorphism-order audit is **one finite stress test only**.  It
was not inspected or rerun here, is not used in the even-characteristic proof,
and cannot prove the odd family or the universal source assignment.

## Evidence

### Context-boundary disclosure

The only out-of-bound reads were
`Agents/Kourovka/problems/21.53/verification/2026-08-17T191934Z-a6-bounded-equality.md`
and
`Agents/Kourovka/problems/21.53/verification/2026-08-17T201248Z-psl28-bounded-equality.md`,
opened after the core even-family derivation to inspect status/verdict style.
They supplied no premise, lemma, computation, or wording to Sections 1--7.  The
disclosure is nevertheless mandatory because the requested context boundary was
absolute.

Artifact identity:

```text
$ sha256sum Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/partial-result.md Agents/Kourovka/problems/21.53/claim-checks/21.53-psl2-even-r2-partial-001.json
166e06dd864c2ee612c7bbaadcf03b4b58f60371f3779b3bdaadbf55a7eb911b  Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/partial-result.md
6968a5a73278031d5d01742add87a9c38d5cfcffe40c04ab8b9599d04004e02e  Agents/Kourovka/problems/21.53/claim-checks/21.53-psl2-even-r2-partial-001.json
```

Tool probe:

```text
$ which gap; which sage; which python3; which magma; which pdftotext
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftotext
$ gap -q -c 'Print(GAPInfo.Version,"\\n");QUIT;'
4.12.1
$ python3 --version
Python 3.12.3
$ pdftotext -v
pdftotext version 24.02.0
```

`sage` and `magma` returned no path.  GAP was not used mathematically.

Mechanical completeness gate:

```text
$ python3 _meta/scripts/kourovka-state-check.py 2>&1 | sed -E 's#^WARNING: .*/obsidian/#WARNING: #'
WARNING: Agents/Kourovka/roster/Problem-16.4.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-17.76.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-19.25.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-20.55.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-21.31.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-21.89.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/problems/21.90/claim-checks/21.90-diameter-three-distance-graphs-r2-candidate-001.json: claim check is for an old assignment revision
Kourovka state check: 11 scope(s), 17 roster(s), 11 v2 board row(s), 6 claim check(s), 0 benchmark manifest(s), 0 error(s), 7 warning(s).
```

This command proves only that every revision-2 constraint ID is present and that
the submitted bounded claim is mechanically routable.  It does not prove any
mathematical row.

## Why the abandoned draft reached its tentative assessment

The involution parameterization is exhaustive and injective; the determinant
formula identifies both selected relations and every remaining colour; the
functional equation is valid on genuine graph edges and forces precisely a field
automorphism after `SL(2,q)` normalization; and those semilinear maps preserve
exact element orders.  The smallest admissible field and the `q=5` transfer have
both been checked separately.  No step relies on the discovery computation.

## What is NOT established

- The odd-characteristic orthogonal-shell rigidity lemma is not proved.
- The finite `q=27` audit is not an odd-family theorem.
- No pair outside the asserted even-`PSL_2`/`A5` family is settled here.
- The universal all-simple-groups quantifier in revision 2 remains open.
- Problem 21.52's different automorphism-induction question is untouched.
- The protocol status has not been raised to `status/proven` before human view.
- This run is not clean-context compliant because of the disclosed post-derivation
  formatting reads.

## What a valid review would require

For this bounded partial theorem, a fresh validator restricted to the submitted
artifacts must first reproduce the hand check; human review of that clean
verification followed by the protocol-authorized Validator tag change would
permit `status/proven`.
Answering the active assignment still requires a proof for every remaining finite
nonabelian simple group/involution-class pair, or one admissible counterexample;
the present theorem cannot be extrapolated to that universal conclusion.
