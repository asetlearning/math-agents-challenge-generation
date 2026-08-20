---
title: "Verification — Kourovka 21.53 — q=7 Pasch-resolution obstruction"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "The displayed q=7 Pasch trade gives a nongeometric binary weight-three factor with the same Gram matrix; the geometric system has eight resolutions and this traded system has none, while the stated characteristic-three internal shell has empty R_3."
claimant: Problem-21.53-Proof
target_statement: "For every finite nonabelian simple L and every involution class D, Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma), where p is the second-smallest distinct prime divisor of |L|."
excluded_scopes: ["Problem 21.52", "multiple involution classes", "arbitrary p", "bounded-pair equality presented as universal"]
target_object: "The complete product-order-coloured graph on an arbitrary admissible involution class D."
witness_object: "The geometric and one Pasch-traded 21 by 28 binary incidence systems over F_7, plus the internal shell for q=3^f with f odd."
witness_equals_target: false
citation: none
verification_method: "hand finite geometry and trace calculation; independent Python 3.12.3 projective-chart/bitmask-DP checker"
tools_used: ["Python 3.12.3", "GAP 4.12.1 (availability probe only)", "GNU sha256sum 9.4"]
scope_answered: []
scope_not_answered: [21.53/two-minimal-prime-colours]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.53

## The claim

The bounded claim is correct.  For the conic `Y^2=XZ` over `F_7`, the four
displayed secant sections can be replaced by the four displayed noncollinear
triples without changing any entry of `XX^T`; the new factor is not a column
permutation of the geometric factor.  An independently organized exact-cover
calculation gives eight resolutions for the geometric 28-block system and zero
for this one traded system.  The characteristic-three empty-`R_3` statement
also has a direct trace/tangent proof.

This is a replicated **bounded method result**, not an answer to Problem 21.53.

## Scope, revision, and clause matrix

The rendered source page was read independently.  Revision 2 correctly retains
the inherited finite-nonabelian-simple/involution-class setting, the one-way
definition of every `Aut_t`, the full-colour intersection, and the universal
two-minimal-prime question.

```text
$ source _meta/agents/Kourovka/paths.env
$ pdftotext -f 172 -l 172 -layout "$KOUROVKA_PDF" -
21.53. In the notation of 21.52, let Aut_t(Gamma) be the set of permutations
tau in S_D such that (a,b) is equivalent to (a^tau,b^tau) whenever |ab|=t.
Clearly, Aut(Gamma) is the intersection of the Aut_t(Gamma). Is it true that
Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma), where {2,p} are the two
minimal prime divisors of |G|?
```

The mathematical symbols above are a faithful plain-text transcription of the
rendered formula, not a reliance on the corpus extraction.

| source clause | result of this verification |
|---|---|
| inherited product-order-coloured graph on one involution class | only the order-2 conic model used by the bounded reconstruction is checked |
| `Aut_t` for every positive integer, vacuously `S_D` when the t-edge set is empty | used correctly for characteristic three |
| `Aut(Gamma)` is the full intersection of colour stabilisers | not reconstructed |
| `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)` universally | neither proved nor refuted |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | independent result | evidence / limitation |
|---|---|---|---|
| `21.53-forall-L-D` | admissibility | not satisfied for scope closure | only two displayed `q=7` block systems and one characteristic subfamily statement are treated |
| `21.53-L-finite-nonabelian-simple` | admissibility | contextual only | no fixed-group equality or counterexample is asserted |
| `21.53-D-single-involution-class` | admissibility | contextual model reconstructed | trace-zero determinant-one lifts identify the nonsquare shell with involutions when `q=3 mod 4`; this verification does not claim a source-scope witness |
| `21.53-Gamma-product-order-colouring` | admissibility | incomplete | only exact order 2, and emptiness of order 3 in the stated subfamily, are addressed |
| `21.53-Aut-t-definition` | admissibility | pass for the claimed use | an empty relation imposes no condition, so its stabiliser is `S_D` |
| `21.53-two-minimal-primes` | admissibility | pass in the characteristic-three subfamily | `|PSL(2,q)|=q(q^2-1)/2` is even and divisible by 3, so the two smallest distinct primes are 2 and 3 |
| `21.53-full-colour-group-definition` | admissibility | not reconstructed | no full product-order matrix is supplied |
| `21.53-two-colours-determine-all` | target conclusion | unproved and unviolated | there is no separating permutation and no universal proof |

## Target versus witness

The source target is a universal permutation-group equality.  The checked
objects are two particular binary incidence factors on 21 projective points.
Neither factor is an automorphism of the order-2 graph, and neither is a
permutation of the involution class.  Consequently these factors are not target
witnesses; they only test a proposed reconstruction lemma.

## Subclaims and what each method proves

| subclaim | method | pass proves | pass does not prove |
|---|---|---|---|
| point and secant data | direct arithmetic in `F_7` | exactly the six classifications and four complete supports | a larger-field theorem |
| Pasch identity | tetrahedral multiplicity count | equality of the two four-column outer-product sums | uniqueness/nonuniqueness of every possible completion criterion |
| nongeometric factor | four nonzero determinants and support comparison | the traded factor is not a column permutation | a graph automorphism or counterexample |
| 8 versus 0 | independent memoized bitmask DP | exact resolution counts for these two block sets | classification of all Gram factors |
| characteristic-three emptiness | trace-square and tangent-line derivation | `R_3` is empty on the stated internal shell | `Aut(Gamma)=Aut_2` or any field-uniform recovery theorem |

## Hand reconstruction over F_7

The nonzero squares are `1,2,4`, so the nonsquares are `3,5,6`.  Directly,

| point | `P` | `A` | `B` | `C` | `D` | `R` |
|---|---:|---:|---:|---:|---:|---:|
| coordinates | `(1,0,1)` | `(3,1,1)` | `(5,2,1)` | `(2,0,1)` | `(4,0,1)` | `(6,4,1)` |
| `Q=Y^2-XZ` | 6 | 5 | 6 | 5 | 3 | 3 |

Thus all six points are internal.

Parameterize the conic by `c_t=(t^2,t,1)` and
`c_infinity=(1,0,0)`.  Substitution gives:

| line | conic parameters | displayed internal points on it |
|---|---|---|
| `l_1: X=2Y+Z` | roots `4,5` of `t^2-2t-1` | `P,A,B` |
| `l_2: Y=0` | `0,infinity` | `P,C,D` |
| `l_3: X=Y+2Z` | roots `2,6` of `t^2-t-2` | `A,C,R` |
| `l_4: X=4Y+4Z` | roots `1,3` of `t^2-4t-4` | `B,D,R` |

On a secant through finite conic points `c_a,c_b`,

`Q(lambda c_a + mu c_b)=-lambda mu (a-b)^2`.

For `q=7`, exactly the three projective ratios with `lambda mu` a square
therefore give nonsquare `Q`.  The line `Y=0` gives the same count directly:
its nonconic affine points have `Q=-X`, and `X=1,2,4` give `P,C,D`.
Hence each displayed old triple is the **complete** internal section of its
secant.

The six points are the six pairwise line intersections:

`P=p_12, A=p_13, B=p_14, C=p_23, D=p_24, R=p_34`.

The old triples are the four stars of `K_4`; the new triples

`PAC, PBD, ABR, CDR`

are its four triangular faces.  Their raw-coordinate determinants are,
respectively, `6,1,3,1` modulo 7, all nonzero.  Thus none is collinear and none
is a geometric secant section.

For the outer-product identity, every `p_ij` occurs twice among the stars and
twice among the faces.  Two distinct `K_4` edges occur together once on each
side precisely when they share an endpoint; disjoint edges occur together zero
times on each side.  This checks every diagonal and off-diagonal entry, including
zeros.  Rows outside these six points are zero on both four-column sums.
Therefore replacing the four stars by the four faces preserves every entry of
`XX^T`.

Since every original column is a collinear secant section and all four new
supports are noncollinear, the resulting 28-column binary weight-three matrix
cannot be obtained from the geometric matrix by permuting columns.

### The displayed Gram matrix

The relation to `7I+J-A^2` can also be recovered directly.  Put

`M_v=[[Y,X],[-Z,-Y]]` for `v=(X,Y,Z)`.

Then `det(M_v)=-Q(v)` and `M_v^2=Q(v)I`.  Since both `-1` and every internal
`Q(v)` are nonsquares in `F_7`, choose `s_v^2=-Q(v)` and set
`I_v=s_v^{-1}M_v`.  Its image in `PSL(2,7)` is an involution.  If

`B(v,w)=2Y_vY_w-X_vZ_w-Z_vX_w`

is the polar form, then
`tr(I_vI_w)=B(v,w)/(s_vs_w)`.  Thus two distinct shell involutions have product
order 2 exactly when `v` and `w` are orthogonal.

Off the diagonal, `(A^2)_{vw}` is 1 exactly when the pole of the line `vw` is
internal.  An internal--internal joining line is never tangent; a secant has an
exterior pole and an external line has an internal pole.  Hence the secant
incidence entry is `1-(A^2)_{vw}`.  On the diagonal an internal point lies on
four secants and has four orthogonal internal neighbours, so both sides equal
`4=7+1-4`.  Therefore the geometric factor satisfies

`XX^T=7I+J-A^2`,

and the star/face identity gives the same equality for the traded factor.

## Independent resolution computation

The independent checker uses the disjoint projective charts

`(1,y,z)`, `(0,1,z)`, `(0,0,1)`

instead of generating all nonzero triples and quotienting them as the claimant
did.  It encodes each block by a 21-bit mask.  Its memoized recurrence selects
the least uncovered point and branches over the still-disjoint blocks through
that point.  Every exact cover has a unique block at each pivot, so every
resolution is counted once; seven blocks are automatic because every block has
weight three and all 21 points are covered.

The submitted checker itself hashes to its claimed frozen value:

```text
$ sha256sum Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/scratch/q7_pasch_audit.py
87abf88b48cd189708b19d61442c1deaa6ee60cd1b4e0fb31b218582297ed33f  Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/scratch/q7_pasch_audit.py
```

For transparency, the first frozen checker stopped before enumeration because
it compared exact `Q` values after changing projective representatives:

```text
$ timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.py
Traceback (most recent call last):
  File "Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.py", line 84, in <module>
    assert tuple(q(v) for v in SIX) == (6, 5, 6, 5, 3, 3)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

The Python-emitted machine prefix on the traceback path is normalized above to
the vault-relative path required by the crew protocol; all mathematical output
is otherwise transcribed exactly.

No count was produced.  Lead authorized only a one-hunk repair: exact values
are checked on the raw vectors, then normalized representatives are checked by
square class.  Version 3 was frozen at SHA-256
`39dbeed498d716e32799dabc8430c47fb2cfa53e178312542c4a194d3a358973`
and run exactly once under the replacement lease:

```text
$ timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp_v3.py
projective_points=57
conic_points=8
internal_points=21
geometric_blocks=28
traded_blocks=28
new_determinants=[1, 6, 4, 6]
gram_equal=True
geometric_resolutions=8
traded_resolutions=0
```

The normalized determinants differ from the raw determinants by nonzero square
row scalings; only nonvanishing is invariant and required.  The eight geometric
resolutions include the eight pencils of seven secants through a conic point;
the exact count shows there are no others.  The zero count exhausts possible
seven-block partitions in this one traded system.

One implementation detail does not affect that conclusion: in the frozen
`gram_signature`, Python's integer-valued `and` multiplies the `(i,j)`
off-diagonal count by the fixed bit `2^j` instead of coercing it to `0` or `1`.
For each fixed entry this multiplier is the same and nonzero on both sides, so
signature equality is equivalent to actual Gram-entry equality.  The preceding
star/face argument independently checks the unscaled entries.

## Characteristic-three audit

Let `q=3^f` with `f` odd.  Then `q=3 mod 4`, so `-1` is a nonsquare and the
trace-zero determinant-one construction above uses exactly the nonsquare
`Q`-shell.  For distinct shell points `v,w`, put

`u=tr(I_vI_w)^2=B(v,w)^2/(Q(v)Q(w))`.

In characteristic three, a nonidentity projective element has order three
exactly when it is unipotent, equivalently its determinant-one lift has
`tr^2=4=1`.  Distinct involutions exclude the scalar identity case.  Thus an
order-three product would require `u=4`.

But `u=4` is exactly

`B(v,w)^2-4Q(v)Q(w)=0`,

the zero-discriminant condition saying that the joining line `vw` is tangent
to the conic.  At `c_t=(t^2,t,1)` the tangent is
`X-2tY+t^2Z=0`; substituting its equation gives

`Q(X,Y,Z)=(Y-tZ)^2`.

At `c_infinity` the tangent is `Z=0` and `Q=Y^2`.  Hence every nonconic point
on every tangent has square `Q`, while the shell points have nonsquare `Q`.
No joining line of two distinct shell points is tangent, so `u` never equals
4 and `R_3` is empty.

The case `f=1`, `q=3`, is outside the nonabelian-simple range; for odd `f` in
that range one has `f>=3`, `q>=27`.  Since the group order is even and divisible
by 3, `p=3` is the second-smallest distinct prime.  The source's one-way
definition therefore gives `Aut_3(Gamma)=S_D` vacuously and

`Aut_2(Gamma) intersection Aut_3(Gamma)=Aut_2(Gamma)`.

This is only a reduction of the desired equality in that subfamily, not a proof
of `Aut(Gamma)=Aut_2(Gamma)`.

## Verdict

`status/replicated` for the bounded partial result.

The hand certificate independently establishes the point, secant, Pasch,
Gram, and nongeometric claims.  The separately designed leased bitmask DP agrees
with the submitted 8-versus-0 counts.  The characteristic-three statement has
an independent direct proof.  The source conclusion remains open.

## What is NOT established

- No permutation in `Aut_2(Gamma)` outside or equal to the full colour group is
  constructed.
- The fixed `PSL(2,7)` two-colour equality is not decided.
- The traded factor is only one competing Gram factor; all binary factorizations
  are not classified.
- The resolution criterion rejects this competitor and may still select the
  geometric factor uniquely; that stronger joint criterion is not analyzed.
- No `q=3 mod 4` family theorem follows from the `q=7` trade.
- Empty `R_3` does not prove `Aut(Gamma)=Aut_2(Gamma)` in characteristic three.
- No conclusion is obtained for the universal revision-2 source target or for
  Problem 21.52.

## What would upgrade it

A source-scope result still requires either a universal proof covering every
admissible `(L,D)` or a reconstructible separating permutation for one
admissible pair.  For the characteristic-three branch specifically, one needs
an intrinsic, field-uniform recovery of all product-order colours from the
order-2 relation; the present Gram data and one resolution audit do not supply
that recovery.
