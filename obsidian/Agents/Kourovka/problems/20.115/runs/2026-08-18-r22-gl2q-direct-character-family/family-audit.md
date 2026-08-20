---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
strategy: GL2Q-DIRECT-CHARACTER-FAMILY
outcome: PARTIAL_RESULT
active_assignment_answered: no
started_utc: 2026-08-18T11:25:34Z
stopped_utc: 2026-08-18T11:32:07Z
new_active_elapsed: "00:06:33"
detailed_cumulative_elapsed: "08:02:07"
---

# Direct ordinary-character audit for `GL(2,q)`

## Outcome and exact limitation

Candidate family theorem: for every prime power `q`, every ordinary irreducible
complex character `chi` of `G = GL(2,q)`, and every `x in G`,

`chi(x) != 0  =>  o(x) chi(1) divides |G|`.

The argument below is uniform, not a finite-parameter sample.  It covers the
nonsolvable range `q >= 4` and separately audits `q = 2,3` (and the first
nonsolvable value `q = 4`).  It is only a family partial for scope 20.115: it
does not address arbitrary finite groups.

No prior rank-one-family result and no computation is used.

## 1. Conjugacy classes and exact element orders

Write `q = p^f`, let `F = F_q`, let `E = F_{q^2}`, and set

`|G| = (q^2-1)(q^2-q) = q(q-1)^2(q+1)`.

Rational canonical form gives exactly the following four types.  In the last
row, `t(z)` is multiplication by `z` on the two-dimensional `F`-space `E`.

| type | representative/parameter | parameter identification | centralizer order | exact element order |
|---|---|---|---:|---|
| scalar | `c(a)=aI`, `a in F^*` | none | `|G|` | `d_a := o(a)` |
| Jordan | `u(a)=a(I+N)`, `N^2=0`, `N!=0` | none | `q(q-1)` | `p d_a` |
| split regular | `s(a,b)=diag(a,b)`, `a!=b` | `{a,b}` unordered | `(q-1)^2` | `lcm(d_a,d_b)` |
| nonsplit regular | `t(z)`, `z in E^* \ F^*` | `{z,z^q}` | `q^2-1` | `d_z := o_E(z)` |

This is complete: the numbers of classes of the four types are respectively

`q-1`, `q-1`, `(q-1)(q-2)/2`, `q(q-1)/2`,

whose sum is `q^2-1`.  The order in the Jordan row is exact because the scalar
part has order `d_a | q-1`, the nontrivial unipotent part has order `p`, the
parts commute, and `gcd(p,d_a)=1`.  The split and nonsplit orders are exact from
their eigenvalues.  In particular,

- scalar and split orders divide `q-1`;
- Jordan orders are exactly `p d_a` with `d_a | q-1`;
- nonsplit orders divide `q^2-1`.

## 2. Complete ordinary irreducible families

Let `X = Hom(F^*, C^*)` and `Y = Hom(E^*, C^*)`.  For `theta in Y`, write
`theta^q(z)=theta(z^q)`.  The four families are:

1. `L_alpha = alpha o det`, `alpha in X`, of degree `1`;
2. `S_alpha = St tensor L_alpha`, `alpha in X`, of degree `q`;
3. `P_{alpha,beta} = Ind_B^G(alpha tensor beta)`, for `alpha!=beta`, with
   `{alpha,beta}` unordered, of degree `q+1`;
4. `C_theta`, for `theta!=theta^q`, with `theta` identified with `theta^q`,
   of degree `q-1`.

The principal-series values come directly from the action on the `q+1` lines:
a scalar fixes all lines, a Jordan element fixes one, a split-regular element
fixes its two eigenlines, and a nonsplit element fixes none.  For
`alpha=beta`, that induced character is `L_alpha + S_alpha`, which gives the
Steinberg row.  The rank-one anisotropic-torus cuspidal construction
`C_theta = -R_T^G(theta)` gives the fourth row.  Thus the complete value table is

| character | degree | `c(a)` | `u(a)` | `s(a,b)` | `t(z)` |
|---|---:|---|---|---|---|
| `L_alpha` | `1` | `alpha(a^2)` | `alpha(a^2)` | `alpha(ab)` | `alpha(z^{q+1})` |
| `S_alpha` | `q` | `q alpha(a^2)` | `0` | `alpha(ab)` | `-alpha(z^{q+1})` |
| `P_{alpha,beta}` | `q+1` | `(q+1)alpha(a)beta(a)` | `alpha(a)beta(a)` | `alpha(a)beta(b)+alpha(b)beta(a)` | `0` |
| `C_theta` | `q-1` | `(q-1)theta(a)` | `-theta(a)` | `0` | `-(theta(z)+theta(z^q))` |

Here `z^{q+1}` is the determinant/norm of `t(z)`.  The constructions give
irreducibles with only the displayed parameter identifications: the rank-one
Mackey endomorphism calculation makes `P_{alpha,beta}` irreducible exactly when
`alpha!=beta`, and regular anisotropic parameters give irreducible
`-R_T^G(theta)` with Frobenius orbit `{theta,theta^q}`.  Completeness also has
two numerical audits.  Their number is

`2(q-1) + (q-1)(q-2)/2 + q(q-1)/2 = q^2-1`,

the number of conjugacy classes, and their degree squares sum to

```
(q-1)(1+q^2)
+ ((q-1)(q-2)/2)(q+1)^2
+ (q(q-1)/2)(q-1)^2
= q(q-1)^2(q+1) = |G|.
```

## 3. Exact support and cancellation audit

All character values in the scalar column are nonzero.  In every displayed
nonzero monomial, character values are roots of unity and hence nonzero.  The
only sums in the table have the following exact cancellation criteria.

For `gamma = alpha beta^{-1}` and `a!=b`,

```
P_{alpha,beta}(s(a,b))
= alpha(b)beta(a) (1 + gamma(a/b)),
```

so this value is zero exactly when `gamma(a/b)=-1`.  For a nonsplit parameter
`z`,

```
C_theta(t(z)) = -theta(z)(1 + theta(z^{q-1})),
```

so it is zero exactly when `theta(z^{q-1})=-1`.  There are no other possible
cancellations.  Therefore the complete support inventory is:

| family | scalar | Jordan | split regular | nonsplit regular |
|---|---|---|---|---|
| `L_alpha` | always nonzero | always nonzero | always nonzero | always nonzero |
| `S_alpha` | always nonzero | identically zero | always nonzero | always nonzero |
| `P_{alpha,beta}` | always nonzero | always nonzero | nonzero iff `gamma(a/b)!=-1` | identically zero |
| `C_theta` | always nonzero | always nonzero | identically zero | nonzero iff `theta(z^{q-1})!=-1` |

## 4. Cell-by-cell divisibility audit

It suffices to divide the exact quotient `|G|/chi(1)` by each exact order on
the nonzero support.  The cancellations above can only remove cells and do not
create a new order type.

| family | exact quotient `|G|/chi(1)` | nonzero class types | divisibility check |
|---|---:|---|---|
| `L_alpha` | `q(q-1)^2(q+1)` | all four | every displayed exact element order divides `|G|` (equivalently, Lagrange) |
| `S_alpha` | `(q-1)^2(q+1)=(q-1)(q^2-1)` | scalar, split, nonsplit | scalar/split order divides `q-1`; nonsplit order divides `q^2-1` |
| `P_{alpha,beta}` | `q(q-1)^2` | scalar, Jordan, and the noncancelled split cells | scalar/split order divides `q-1`; for Jordan, `p d_a` divides `q(q-1)^2` since `(q/p)((q-1)/d_a)(q-1)` is integral |
| `C_theta` | `q(q-1)(q+1)=q(q^2-1)` | scalar, Jordan, and the noncancelled nonsplit cells | scalar order divides `q-1`; `p d_a` divides the quotient since `(q/p)((q-1)/d_a)(q+1)` is integral; `d_z` divides `q^2-1` |

Thus every nonzero cell in every ordinary irreducible row of `GL(2,q)` has
`o(x) | |G|/chi(1)`.

## 5. Small parameters

The generic construction includes every prime power `q>=2`; the low values are
recorded explicitly to exclude hidden degeneration.

### `q=2`

`GL(2,2)` has order `6`.  There is one scalar class (order `1`), one Jordan
class (order `2`), no split-regular class, and one nonsplit class (order `3`).
The character families reduce to

- `L_1`, degree `1`, values `(1,1,1)`;
- `S_1`, degree `2`, values `(2,0,-1)`;
- one `C_theta`, degree `1`, values `(1,-1,1)`.

For the last value, if `z` generates `F_4^*` and `theta(z)=omega`, then
`-(omega+omega^2)=1`.  The nonzero products `o(x)chi(1)` are respectively
subsets of `{1,2,3}`, `{2,6}`, and `{1,2,3}`, all dividing `6`.

### `q=3`

`|GL(2,3)|=48`.  The four family counts/degrees are `2x1`, `2x3`, `1x4`,
and `3x2`.  Scalar orders are `1,2`; Jordan orders are `3,6`; the sole split
class has order `2`; and nonsplit orders are `4` or `8`.  On their respective
nonzero supports the quotients are `48`, `16`, `12`, and `24`, so each listed
order divides the relevant quotient.  This covers every cell even before the
two possible sum cancellations remove cells.

### `q=4` (first nonsolvable parameter)

`|GL(2,4)|=180`.  The family counts/degrees are `3x1`, `3x4`, `3x5`, and
`6x3`.  Scalar/split orders divide `3`, Jordan orders are `2` or `6`, and
nonsplit orders divide `15`.  The Steinberg, principal-series, and cuspidal
quotients are respectively `45`, `36`, and `60`, containing exactly their
support orders.  This also checks the characteristic-two scalar--unipotent
least-common-multiple effect in the first nonsolvable case.

For every `q>=4`, `GL(2,q)` is nonsolvable because the image of `SL(2,q)`
modulo its scalar center is `PSL(2,q)`, which is nonabelian simple.  Hence the
uniform argument above covers the entire requested nonsolvable range, not just
solvable low parameters.

## 6. Required six-row constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple `(G,chi,x)` | restricted here to every `G=GL(2,q)` | Sections 1--5 | **PARTIAL only**; universal active assignment remains unanswered |
| `20.115-G-finite` | admissibility | `G` finite | `GL(2,q)` is finite of order `q(q-1)^2(q+1)` | Section 1 | pass within family |
| `20.115-chi-complex-irreducible` | admissibility | ordinary complex irreducible `chi` | all four ordinary irreducible families, with parameter identifications and completeness audits | Section 2 | pass within family |
| `20.115-x-in-G` | admissibility | `x in G`, exact `o(x)` | all four rational-canonical-form class types and exact orders | Section 1 | pass within family |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x)!=0` | full support table and both root-of-unity cancellation criteria | Section 3 | pass within family |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) divides |G|` | exact quotient check for every family/support type | Section 4 and small cases in Section 5 | pass within family only |

## 7. Handoff status

This is a candidate infinite-family partial suitable for independent character-
table and divisibility review.  It does not answer scope 20.115 for every finite
group, so `active_assignment_answered: no`.

Active-time ledger: work began at `2026-08-18T11:25:34Z` and stopped at
`2026-08-18T11:32:07Z`, charging exactly `00:06:33`.  Added to the inherited
detailed cumulative time `07:55:34`, this reaches `08:02:07`.  The cycle-22 cap
and wall safety stop were both respected.
