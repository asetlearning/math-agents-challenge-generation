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
direction: proof
cycle: 20
strategy: PGL2Q-DIRECT-CHARACTER-FAMILY
outcome: PARTIAL_RESULT
active_assignment_answered: no
new_active_elapsed: "00:07:17"
detailed_cumulative_active: "07:44:01"
---

# Candidate family theorem for `PGL(2,q)`, odd `q`

## Outcome and exact limit

For every odd prime power `q>=5`, the generic ordinary character table and the
generic element inventory below give the candidate family theorem

> If `G=PGL(2,q)`, `chi in Irr(G)`, and `chi(x) != 0`, then
> `o(x) chi(1) | |G|`.

Both cosets of the socle `PSL(2,q)` are included.  This is only an
almost-simple-family partial: it does not answer the source quantifier over all
finite groups.

No computation or finite sampling is used.  The derivation uses the elementary
rank-one principal-series, Steinberg, and nonsplit-torus cuspidal constructions,
then checks their traces and completeness from the class inventory.

## 1. Exact conjugacy and order inventory

Put

`G=PGL(2,q)`, `N=PSL(2,q)`, and `|G|=q(q-1)(q+1)`.

Let `A=F_q^*` (cyclic of order `q-1`) and
`U={t in F_(q^2)^*: t^(q+1)=1}` (cyclic of order `q+1`).  Every element of `G`
has exactly one of the following types.

| type | parameter up to inversion | exact order | centralizer in `G` |
|---|---|---:|---:|
| identity | — | `1` | `|G|` |
| nonidentity unipotent `u` | one class | `p=char(F_q)` | `q` |
| split semisimple `s_r` | `r in A-{1}`, `r~r^-1` | `ord_A(r)` | `q-1`, except `2(q-1)` for `r=-1` |
| nonsplit semisimple `n_t` | `t in U-{1}`, `t~t^-1` | `ord_U(t)` | `q+1`, except `2(q+1)` for `t=-1` |

For the nonsplit line, take eigenvalues `alpha,alpha^q` and
`t=alpha^(q-1)`.  Projective order is the least `k` for which the eigenvalue
ratio has `k`th power one, hence exactly `ord_U(t)`.  A nonsemisimple matrix has
a repeated eigenvalue and, after projective scaling, is the displayed
unipotent; since its nilpotent part squares to zero and `p` is odd, its exact
order is `p`.  Thus the four lines are exhaustive.

There is one unipotent class because conjugation by `diag(c,1)` is transitive on
the nonzero upper-right entries.  There are `(q-1)/2` split classes and
`(q+1)/2` nonsplit classes.  Including identity and unipotent gives `q+2`
classes.  The exceptional centralizers at `-1` are the torus normalizers; they
also make the following uniform class-sum formula exact for every
inversion-invariant class function `f`:

```
sum_(g in G) f(g)
 = f(1) + (q^2-1) f(u)
   + q(q+1)/2 sum_(r in A-{1}) f(s_r)
   + q(q-1)/2 sum_(t in U-{1}) f(n_t).
```

### Socle versus diagonal outer coset

Let `eta` be the quadratic character of `A`.  The quotient character

`epsilon([M])=eta(det M)`

is well-defined because changing a representative multiplies the determinant
by a square, and `ker(epsilon)=N`.  Let `delta(t)=t^((q+1)/2)` be the quadratic
character of `U`.  Then

- `epsilon(u)=1`;
- `epsilon(s_r)=eta(r)`;
- `epsilon(n_t)=delta(t)`.

The nonsplit equality follows from
`eta(Norm(alpha))=alpha^((q^2-1)/2)=delta(alpha^(q-1))`.
Consequently the complete order separation is:

- inner split orders are precisely the divisors of `(q-1)/2`;
- outer split orders are precisely `d|q-1` with
  `v_2(d)=v_2(q-1)`;
- inner nonsplit orders are precisely the divisors of `(q+1)/2`;
- outer nonsplit orders are precisely `d|q+1` with
  `v_2(d)=v_2(q+1)`;
- all nonidentity unipotents (order `p`) lie in `N`.

Indeed, in a cyclic group of even order `m`, a nonsquare is an odd power of a
generator, and its order contains the full `2`-part of `m`; the converse is
obtained by choosing an odd exponent.  This explicitly includes every order in
the diagonal outer coset.

## 2. Complete ordinary irreducible-character inventory

Write characters of the two cyclic tori multiplicatively.  The rows are:

1. `1_G` and `epsilon`, of degree `1`;
2. `St` and `St*epsilon`, of degree `q`;
3. `X_mu`, of degree `q+1`, for
   `mu in Irr(A)-{1,eta}`, modulo `mu~mu^-1`;
4. `Y_nu`, of degree `q-1`, for
   `nu in Irr(U)-{1,delta}`, modulo `nu~nu^-1`.

Their exact values are

| row | `1` | `u` | `s_r` | `n_t` |
|---|---:|---:|---|---|
| `1_G` | `1` | `1` | `1` | `1` |
| `epsilon` | `1` | `1` | `eta(r)` | `delta(t)` |
| `St` | `q` | `0` | `1` | `-1` |
| `St*epsilon` | `q` | `0` | `eta(r)` | `-delta(t)` |
| `X_mu` | `q+1` | `1` | `mu(r)+mu(r)^-1` | `0` |
| `Y_nu` | `q-1` | `-1` | `0` | `-(nu(t)+nu(t)^-1)` |

All entries are exact cyclotomic integers.

### Construction and completeness check

For `B` the upper-triangular subgroup, inflate `mu` by
`diag(a,d) -> mu(a/d)`.  Mackey's two-double-coset calculation gives
`End_G(Ind_B^G(mu))=C` exactly when `mu^2!=1`; hence these are the irreducible
`X_mu`, with `X_mu=X_(mu^-1)`.  Counting fixed eigenlines gives the displayed
four values.  At `mu=1`, the permutation character on `P^1(F_q)` is
`1_G+St`, giving the Steinberg row.  At `mu=eta`, the induced character is its
`epsilon`-twist, `epsilon+St*epsilon`.

For the nonsplit construction, the map
`F_(q^2)^*/F_q^* -> U`, `alpha -> alpha^(q-1)`, is an isomorphism and Frobenius
acts as inversion.  The rank-one finite-field cuspidal construction attached to
`nu!=nu^-1` therefore gives one irreducible `Y_nu=Y_(nu^-1)`.  Its elementary
trace calculation is: degree `q-1`, value `-1` on the nontrivial unipotent
class, zero on a split torus, and minus the two Frobenius-conjugate torus values
on `n_t`, exactly as in the table.

There are `(q-3)/2` principal rows and `(q-1)/2` cuspidal rows, so the list has
`q+2` rows, matching the class count.  Independently, the degree squares give

```
2 + 2q^2 + (q-3)/2 (q+1)^2 + (q-1)/2 (q-1)^2
 = q(q^2-1) = |G|.
```

Thus no additional ordinary irreducible row is available.  As an exact check on
the trace formulas, substituting them into the class-sum formula above reduces
all row inner products to cyclic-character orthogonality.  For example,

```
sum_(r in A-{1}) |mu(r)+mu(r)^-1|^2 = 2(q-3),
sum_(t in U-{1}) |nu(t)+nu(t)^-1|^2 = 2(q-1),
```

for the allowed parameters; these give norm one.  Distinct inversion orbits
give respectively `-4` after deleting the identity term, which cancels the
identity-plus-unipotent contribution.  Principal and cuspidal rows are
orthogonal because their only simultaneous nonzero columns are `1,u`, where
`(q+1)(q-1)-(q^2-1)=0`.

## 3. Every parameter-dependent cancellation and the split rows

The only variable cancellations are exact:

- `X_mu(s_r)=0` iff `mu(r)^2=-1`; all `X_mu(n_t)` are identically zero.
- `Y_nu(n_t)=0` iff `nu(t)^2=-1`; all `Y_nu(s_r)` are identically zero.
- the two Steinberg rows vanish exactly on the nonidentity unipotent class.
- the linear rows never vanish.

There is also exactly one PGL row whose restriction to `N=PSL(2,q)` splits:

- if `q=1 mod 4`, the unique inversion orbit satisfying `mu^2=eta` gives a
  principal row `X_mu` of degree `q+1`; it is fixed by twisting with `epsilon`
  and restricts as two exceptional rows of degree `(q+1)/2`;
- if `q=3 mod 4`, the unique inversion orbit satisfying `nu^2=delta` gives a
  cuspidal row `Y_nu` of degree `q-1`; it is fixed by twisting with `epsilon`
  and restricts as two exceptional rows of degree `(q-1)/2`.

This follows directly from `X_mu*epsilon=X_(mu eta)` and
`Y_nu*epsilon=Y_(nu delta)`, followed by index-two Clifford theory.  In either
case the split row is zero on the entire outer coset, both abstractly from
`chi=chi*epsilon` and entrywise: on an outer relevant torus element its
parameter square is `-1`, so the two cyclotomic terms cancel.  Hence the
exceptional PSL constituents and their fusion in PGL introduce no omitted
outer-coset cell.

## 4. Source divisibility, row by row

Let `n=o(x)` and suppose the indicated row is nonzero at `x`.

| degree | possible nonzero types | exact order containment | required quotient |
|---:|---|---|---:|
| `1` | every type | `n||G|` by Lagrange | `|G|` |
| `q` | identity or semisimple | `n|q-1` or `n|q+1` | `|G|/q=(q-1)(q+1)` |
| `q+1` | identity, unipotent, or split | `n=1`, `n=p|q`, or `n|q-1` | `|G|/(q+1)=q(q-1)` |
| `q-1` | identity, unipotent, or nonsplit | `n=1`, `n=p|q`, or `n|q+1` | `|G|/(q-1)=q(q+1)` |

In every line `n` divides the displayed quotient.  Multiplying by the row degree
gives `o(x)chi(1)| |G|`.  The split/nonsplit coset distinction does not weaken
the argument: outer orders are still exact divisors of the corresponding full
torus order, and the exceptional self-twist row actually deletes all outer
cells.  The additional cyclotomic cancellations only shrink these supports.

## 5. Small exceptional isomorphism audit

### `q=5`

Here `PGL(2,5)=S_5`, `|G|=120`.  The generic class inventory gives

- inner orders `1,5,2,3` (identity, unipotent, split, nonsplit);
- outer split order `4` and outer nonsplit orders `2,6`.

The degrees are `1,1,5,5,6,4,4`.  The degree-six principal row is the unique
split-restriction row: with a generator `a` of `C_4` and `mu(a)=i`, it is zero
on the outer order-four class and has value `-2` on the inner split involution.
Its nonzero support orders divide `120/6=20`.  Each degree-four cuspidal row is
supported only on identity, order-five unipotents, and nonsplit orders dividing
six, all dividing `120/4=30`.  The Steinberg support orders divide
`120/5=24`.  Thus the exceptional `S_5/A_5` fusion is already exactly the
generic argument.

### `q=9`

Here `|PGL(2,9)|=720`, the socle is `PSL(2,9)=A_6`, and the diagonal extension
has outer split elements of order `8` (so no `S_6` isomorphism shortcut is being
silently used).  The generic classes are identity, unipotent order `3`, four
split classes from `C_8`, and five nonsplit classes from `C_10`.  Outer split
orders are `8`; outer nonsplit orders are `2,10`; inner torus orders divide
`4` and `5`, respectively.

The degrees are `1,1,9,9`, three rows of degree `10`, and four rows of degree
`8`.  The unique split-restriction row is the degree-ten principal row with
`mu^2=eta`; it vanishes on all outer classes.  Degree-ten support orders divide
`720/10=72=9*8`; degree-eight support orders divide
`720/8=90=9*10`; and degree-nine semisimple support orders divide
`720/9=80`.  Thus the exceptional `A_6` socle causes no extra row or class.

## 6. Six-row constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate use/evidence | result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | all finite triples | The derivation covers all triples only when `G=PGL(2,q)`, odd `q>=5`; it does not cover every finite group. | **partial only** |
| `20.115-G-finite` | admissibility | `G` finite | `PGL(2,q)` has exact finite order `q(q-1)(q+1)`. | pass in family |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex `chi` | Principal, Steinberg, linear, and nonsplit cuspidal constructions give all `q+2` ordinary rows; class count and degree-square sum audit completeness. | pass in family |
| `20.115-x-in-G` | admissibility | `x in G`, exact `o(x)` | The identity, unique unipotent, split-torus, and nonsplit-torus inventory is exhaustive and records exact orders, including both socle cosets. | pass in family |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x)!=0` | The complete cyclotomic table records all structural zeros and the exact cancellation criteria `mu(r)^2=-1`, `nu(t)^2=-1`. | pass in family |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1)||G|` | The four degree/support lines in section 4 establish the divisibility for every nonzero family cell. | established in family |

`active_assignment_answered: no`, because the universal first row remains open.
