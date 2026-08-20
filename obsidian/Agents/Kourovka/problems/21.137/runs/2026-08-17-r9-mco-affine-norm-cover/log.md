---
title: "Run log — 21.137 — MCO-AFFINE-NORM-COVER"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: MCO-AFFINE-NORM-COVER
direction: proof
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# MCO-AFFINE-NORM-COVER

## Scope lock

`scope_id`: `21.137/odd-prime-exponent-p2`  
`assignment_revision`: `2`

Exact target: for every odd prime `p` and every finite `p`-group `G` of exponent
exactly `p^2`, if the actual value set `P={g^p:g in G}` is a subgroup, then `P`
is abelian.

Required throughout: arbitrary odd `p`; a finite group for that same prime;
exponent exactly `p^2`; `P` is the actual value set, not only its generated
subgroup; actual-value closure; and the conclusion `P` abelian. In the reviewed
hypothetical minimum counterexample, `N=P'=C_p<=Z(G)`, `exp(P)=p`,
`A=P/N`, and `P` is abelian exactly when `beta:A x A -> N` is zero.

Excluded: the general powerfulness clause, all `p=2` and exponent-8 material,
other exponents, wreath-shaped material, the exhausted `UT_7(F_3)` template,
web/history, compute, delegates, matrices, catalogues, Hall-span enlargement, and
split ansatzes.

## Active-time ledger

- `2026-08-17T05:00:49Z`: work start at cumulative active minute `190`; this run
  is authorized for exactly 50 active minutes. Only the three curated refs in the
  SPAWN message were read. Hard proof-attempt kill is cumulative minute `234`;
  absolute stop is cumulative minute `240`.
- `2026-08-17T05:07:41Z`: cumulative active minute `197`; gates 0--3 and the full
  coordinate setup are written, with the degenerate-pairing caveat preserved.
- `2026-08-17T05:19:16Z`: cumulative active minute `208`; gate 4, lift changes,
  exact factor identities, and the nondegenerate-`beta` separator are written.
  The proof attempt continues only on the degenerate radical-shear obstruction.

## Gate 0 — reduced hypotheses and exact actual-value union

Work is conditional in the Validator-reviewed hypothetical minimum counterexample.
No witness or existence assertion is being made. Put `H=G/P`. For each `h in H`,
choose `x_h in G` with `x_h P=h`, and set

`Phi_h(k)=(x_h k)^p` and `S_h=Phi_h(P)`.

Every `g in G` has one and only one coset `h=gP` and can be written `g=x_h k`
for a unique `k in P`. Hence, elementwise,

`Pow_p(G)={g^p:g in G}=union_{h in H} S_h`.

Under the active actual-value-subgroup hypothesis `Pow_p(G)=P`, so the exact cover
condition is `union_h S_h=P`, equivalently `M(t)>0` for every `t in P`, where
`M(t)=#{(h,k):Phi_h(k)=t}`. This is not a generated-subgroup surrogate.

If `x'_h=x_h u` with `u in P`, then
`{(x'_h k)^p:k in P}={(x_h(uk))^p:k in P}=S_h`; changing a lift only
reparametrizes the input. Thus the support itself is lift-independent.

## Gates 1--2 — action and projected norm

Use the reviewed convention `y^x=x^{-1}yx`. Identify `N` additively with
`F_p`. Because `p` is odd and `P` has class two and exponent `p`, choose standard
coordinates

`P=A x F_p`,

`(a,z)(b,w)=(a+b,z+w+(1/2)beta(a,b))`.

Then `[(a,z),(b,w)]=(0,beta(a,b))`. This coordinate choice is available for an
exponent-`p` central extension at odd `p`; it does not assume that `beta` is
nondegenerate.

Let `alpha_h(k)=k^{x_h}`. Since `N<=Z(G)`, `alpha_h` fixes `N` pointwise, so in
these coordinates there are a linear beta-isometry `L_h:A->A` and a linear
central shear `ell_h:A->F_p` such that

`alpha_h(a,z)=(L_h a,z+ell_h(a))`.

Write `x_h^p=(c_h,d_h)`. The exact full-action identities, stronger than their
projection, are

`alpha_h^p=iota_(c_h,d_h)`, `alpha_h(c_h,d_h)=(c_h,d_h)`.

Consequently, with `D_h=L_h-I` and
`N_h=I+L_h+...+L_h^(p-1)`,

`L_h^p=I`, `D_h^p=0`,

`ell_h(N_h a)=beta(a,c_h)` for every `a`, and

`L_h c_h=c_h`, `ell_h(c_h)=0`.

Here inner conjugation by `(c_h,d_h)` sends `(a,z)` to
`(a,z+beta(a,c_h))`; this checks the sign in the shear identity. Since in
characteristic `p`

`1+T+...+T^(p-1)=(T-1)^(p-1)`,

we have the exact projected norm identity

`N_h=D_h^(p-1)`.

Finally,

`(x_h k)^p=x_h^p alpha_h^(p-1)(k) ... alpha_h(k) k`.

Therefore its `A`-coordinate is

`c_h+N_h a=c_h+D_h^(p-1)a`.

This proves gate 2 elementwise for every odd prime and keeps the actual-value
support, rather than only its span.

## Gate 3 — isotropy with signs and degeneracy checked

Invariance of `beta` gives, without choosing an adjoint and without assuming
nondegeneracy,

`beta(D_h u,v)=beta(u,(L_h^(-1)-I)v)`.

Iterating and using `L_h^(-1)-I=-L_h^(-1)D_h`, with `p-1` even, gives

`beta(D_h^(p-1)u,D_h^(p-1)v)`

`=beta(u,L_h^(-(p-1))D_h^(2p-2)v)=0`,

because `D_h^p=0`. Thus `W_h=im D_h^(p-1)` is beta-isotropic. The argument is
an identity of pairings and remains valid when `rad(beta)` is nonzero.

There is also a useful pointwise restriction that counting alone misses. From
`ell_h(N_h a)=beta(a,c_h)`, every `a in ker N_h` is orthogonal to `c_h`, so

`c_h in (ker N_h)^(perp_beta)`.

When `beta` is nondegenerate, self-adjointness of `N_h` identifies this space with
`im N_h=W_h`, so the projected support is an isotropic linear support through
zero. With degenerate `beta`, the safe conclusion is only the displayed
orthogonality: `im N_h+rad(beta)` can be a proper subspace of
`(ker N_h)^(perp_beta)` if `im N_h` meets the radical beyond `N_h(rad(beta))`.
No unjustified quotient-by-the-radical step is used. Even in the nondegenerate
case a union of isotropic linear supports can cover the whole space, so this is
not a separator.

## Gate 4 — full central coordinate, including the shear

Fix `h` temporarily and abbreviate `L=L_h`, `D=D_h`, `ell=ell_h`,
`c=c_h`, and `d=d_h`. For `i>=0` put

`E_i=I+L+...+L^(i-1)` with `E_0=0`.

For `k=(a,z)`, exact iteration gives

`alpha^i(k)=(L^i a,z+ell(E_i a))`.

Multiplying the norm factors in their actual order
`alpha^(p-1)(k)...alpha(k)k` gives central coordinate

`sum_(i=0)^(p-1) ell(E_i a)
 +(1/2) sum_(0<=j<i<=p-1) beta(L^i a,L^j a)`.

The input `z` contributes `p z=0`, so it really disappears rather than being
silently discarded. Two characteristic-`p` weighted-sum identities simplify the
display:

`sum_i E_i=D^(p-2)`,

`sum_(0<=j<i<=p-1) beta(L^i a,L^j a)=beta(D^(p-2)a,a)`.

For the first, the coefficient of `D^m` is `binom(p,m+2)`, which vanishes modulo
`p` except at `m=p-2`. For the second, invariance changes the double sum to
`-sum_(r=1)^(p-1) r beta(L^r a,a)`; differentiating
`1+T+...+T^(p-1)=(T-1)^(p-1)` gives
`sum rL^r=-L D^(p-2)`. The extra `D^(p-1)` term in
`L D^(p-2)=D^(p-2)+D^(p-1)` has zero pairing with `a`, because
`D^(p-1)` is self-adjoint for `beta` and `p` is odd.

Multiplication on the left by `x_h^p=(c,d)` would add
`(1/2)beta(c,D^(p-1)a)`. This term is also exactly zero: the norm operator
`D^(p-1)=sum L^i` is self-adjoint, while `Lc=c` implies
`D^(p-1)c=0`.

Thus the complete support, with no central coordinate suppressed, is

`S_h={(c_h+D_h^(p-1)a,
       d_h+ell_h(D_h^(p-2)a)
          +(1/2)beta(D_h^(p-2)a,a)):a in A}`.                 `(4.1)`

Accordingly the exact multiplicity observable is

`M(u,z)=p sum_(h in H) #{a in A:
 c_h+D_h^(p-1)a=u,
 d_h+ell_h(D_h^(p-2)a)+(1/2)beta(D_h^(p-2)a,a)=z}`.          `(4.1M)`

The leading factor `p` is the number of central input coordinates, all of which
give the same value. Thus `M(u,z)>0` is exactly the actual-value cover condition.

Every `(a,z) in P` maps to the displayed value for `a`, independently of `z`,
so `(4.1)` is exactly the actual support from the whole `P`-coset. The earlier
setwise reparametrization proves lift-independence even though `L_h,ell_h,c_h,d_h`
individually change with the lift.

For completeness, if `x'_h=x_h u` with `u=(r,s)`, those changes are

`L'_h=L_h`,

`ell'_h(a)=ell_h(a)+beta(L_h a,r)`,

`(c'_h,d'_h)=(c_h+D_h^(p-1)r,
 d_h+ell_h(D_h^(p-2)r)+(1/2)beta(D_h^(p-2)r,r))`.            `(4.2)`

The last row is simply formula `(4.1)` evaluated at `r`; the central coordinate
`s` again disappears. Formula `(4.2)` translates the parameter in `(4.1)` and
leaves `S_h` unchanged. It also records the exact shear introduced by the factor
`u_(h,j)` when the product lift `x_hx_j` is compared with `x_(hj)`.

## Cross-coset extension compatibility

Normalize `x_1=1` and define the exact right factor

`x_h x_j=x_(hj) u_(h,j)`, where `u_(h,j)=(r_(h,j),s_(h,j)) in P`.

Because conjugation is a right action, comparison on `P` gives

`alpha_j alpha_h=iota_(u_(h,j)) alpha_(hj)`.                 `(5.1)`

In coordinates this is the pair

`L_(hj)=L_j L_h`,                                             `(5.2)`

`ell_h(a)+ell_j(L_h a)
 =ell_(hj)(a)+beta(L_(hj)a,r_(h,j))`.                         `(5.3)`

Associativity gives the nonabelian factor identity

`u_(hj,k) alpha_k(u_(h,j))=u_(h,jk)u_(j,k)`.                 `(5.4)`

Its two coordinate rows are

`r_(hj,k)+L_k r_(h,j)=r_(h,jk)+r_(j,k)`,                    `(5.5)`

`s_(hj,k)+s_(h,j)+ell_k(r_(h,j))
 +(1/2)beta(r_(hj,k),L_k r_(h,j))
 =s_(h,jk)+s_(j,k)+(1/2)beta(r_(h,jk),r_(j,k))`.             `(5.6)`

Finally `H` has exponent `p`, since every `g^p` lies in `P`. Repeatedly applying
the factor identity along the cyclic subgroup generated by `h` yields the exact
power compatibility

`(c_h,d_h)=u_(h^(p-1),h) alpha_h(u_(h^(p-2),h)) ...
             alpha_h^(p-2)(u_(h,h))`.                        `(5.7)`

Thus the central heights `d_h` are not free in one extension; they are tied to
the full factor system. Also, since `x_hx_j` is another lift of `hj`,

`S_(hj)={((x_hx_j)k)^p:k in P}`.                             `(5.8)`

Conjugating actual powers gives the additional exact support equivariance

`alpha_j(S_h)=S_(h^j)`, where `h^j=j^(-1)hj`.                `(5.9)`

Equations `(5.1)`--`(5.9)` are the written cross-coset constraints used below;
no independent affine supports are being mistaken for extension data.

## What the first cross-coset identity does prove

Let `[A,H]=span{(L_h-I)A:h in H}`. Equation `(5.2)` makes the `L_h` an
anti-representation of the finite `p`-group `H` (equivalently `h -> L_(h^-1)`
is a representation). Hence `[A,H]` is proper: the dual `p`-group action fixes a
nonzero covector, which annihilates `[A,H]`.

If `beta` were nondegenerate, the pointwise identity
`c_h in (ker D_h^(p-1))^perp` would sharpen to
`c_h in im D_h^(p-1)`. Therefore

`pi_A(S_h) subset im D_h^(p-1) subset [A,H]`

for every `h`. Any `a_* notin [A,H]` (and every central coordinate over it) would
be missing from every support, contradicting the exact cover. Consequently a
hypothetical minimum counterexample must have

`0 != rad(beta)`.

This is a target-relevant conditional reduction, but it is not the requested
separator under the only target assumption `beta!=0`.

## Degenerate obstruction exposed by the exact shear identity

Let `R=rad(beta)`. Pass to the nondegenerate quotient `B=A/R` and choose a
nonzero `H`-fixed vector `v_bar in B` using the invariant form and the fixed
covector argument. For a lift `v in A`, every `D_h v` lies in `R`. Hence

`D_h^(p-1)v in R`,

and self-adjointness shows that the linear part `D_h^(p-1)A` of every projected
support is killed by the quotient covector `beta(v,-)`. But the translation is

`beta(v,c_h)=ell_h(D_h^(p-1)v)`.                             `(6.1)`

There is no pointwise reason for the right side to vanish: it records a central
shear on a long radical Jordan chain. Thus the first desired cross-coset
implication

`L_(hj)=L_jL_h  ==>  all c_h lie in one proper annihilator`

fails at `(6.1)`. Equations `(5.3)`--`(5.7)` retain these shear values as part of
the full extension factor system; they do not eliminate them. Proving that they
vanish or omit one common scalar would amount to solving a new global extension
cocycle problem, not a consequence of isotropy or the first action identity.

The obstruction is concrete already for one pointwise datum. Take a symplectic
plane `<e,f>` with `beta(e,f)=1` and a radical chain
`r_(p-2) -> ... -> r_0 -> 0`. Define `D f=r_(p-2)`,
`D r_i=r_(i-1)`, `D e=0`, put `L=I+D`, choose `c=e`, and take the shear
`ell(r_0)=beta(f,e)`, zero on the other displayed basis vectors. Then

`D^p=0`, `L` preserves `beta`, `Lc=c`, `ell(c)=0`, and
`ell(D^(p-1)a)=beta(a,c)` for all `a`, but

`c notin [A,<L>]=im D`.

So even a genuine cyclic action satisfying every gate-1 pointwise compatibility
can translate a support across the coinvariant separator through a radical
shear. This datum is diagnostic only; it is not asserted to be the data of the
active target group.

## Further exact consequence before the hard kill

The same calculation gives a quantitative necessary condition. Keep a nonzero
common fixed vector `v_bar in B=A/R` and its nonzero covector
`psi(-)=beta(v,-)` on `B`. Exact projected covering supplies a support containing
some `a_*` with `psi(a_*)=1`. For that `h`, the norm direction is annihilated:

`psi(D_h^(p-1)a)=beta(D_h^(p-1)v,a)=0`,

because `D_h v in R` and hence `D_h^(p-1)v in R`. Therefore

`1=psi(a_*)=psi(c_h)=ell_h(D_h^(p-1)v)`.

In particular `D_h^(p-1)v != 0`. Since `D_h^p=0`, the vectors

`v,D_hv,...,D_h^(p-1)v`

form a length-`p` nilpotent chain; its final `p-1` vectors lie in `R`. Thus every
hypothetical minimum counterexample satisfying the exact cover has

`dim_Fp rad(beta) >= p-1`, and `dim_Fp A >= p+1`.

Hence `|P|=p^(dim A+1)>=p^(p+2)`. The element `h` above acts nontrivially, so
`|H|>=p` and consequently `|G|>=p^(p+3)` in this hypothetical minimum
counterexample.

There is also a class consequence. Let `x=x_h` for the support above and choose
`y in P` with image `v`. With `[u,x]=u^(-1)u^x`, the `A`-coordinate of the
left-normed iterated commutator `[y,_(m) x]` is `D_h^m v`. At `m=p-1` this is the
nonzero radical vector `r=D_h^(p-1)v`, fixed by `L_h`; one more commutator is

`[ [y,_(p-1) x],x]=(0,ell_h(r)) != 1`.

It has weight `p+1`, so `class(G)>=p+1`.

This lower bound is still compatible with the permitted radical-shear mechanism,
so it does not supply a common missing point.

## Exact coinvariant form of the failed cross-coset implication

Put `C=A/[A,H]`, which is nonzero for the finite `p`-group action. Every
`D_h^(p-1)A` dies in `C`, so the projection of `S_h` to `C` is the singleton

`kappa(h)=c_h+[A,H]`.

Exact covering therefore forces `kappa:H->C` to be surjective. Reducing `(5.5)`
modulo `[A,H]` makes `r_bar_(h,j)` an ordinary normalized 2-cocycle for the
trivial `H`-module `C`, and the `A`-coordinate of `(5.7)` becomes

`kappa(h)=sum_(m=1)^(p-1) r_bar_(h^m,h)`.                    `(6.2)`

Equation `(6.2)` is the usual `p`th-power/carry value in the corresponding
central extension. It is not forced to vanish. For example, purely as quotient
factor data, take `H=C_p`, `C=F_p`, and the normalized carry cocycle obtained by
lifting residues `0,...,p-1` to `C_(p^2)`: its value is `1` exactly when the
integer sum crosses `p`. Then `(6.2)` sends residue `i` to `i`, hence is
surjective while satisfying the cocycle identity.

This carry datum is not a group with the required nonabelian `P`, and is not a
counterexample. It pinpoints why the first exact cross-`h` identity supplies no
common missing coinvariant: cross compatibility permits precisely the translations
which the exact cover requires. Any separator would need a new identity coupling
this extension class to `beta` and to the central formula `(4.1)`; none has been
derived.

The reviewed center dichotomy also blocks a purely vertical rescue. In the branch
`Z(G)=<z>` of order `p^2`, with `z^p` generating `N`, every actual value `t=y^p`
comes with all central translates

`t(z^p)^m=(yz^m)^p` for `m in F_p`.

Thus, in that branch, once an `A`-coordinate occurs, every central coordinate over
it occurs (possibly through different `H`-cosets). In the branch `Z(G)=N`, the
exact shear term in `(4.1)` can already vary on radical norm chains. No common
central coordinate has emerged from `(5.1)`--`(5.9)` in either branch.

## Explicit formal pointwise cover (not an extension and not a witness)

This construction is only a family of support data. It deliberately has no group
`H`, no factors `u_(h,j)`, and no claim of cross-coset compatibility.

Fix arbitrary odd `p`. Let `A=B direct_sum R`, where `B` is a symplectic plane
and `R=rad(beta)` has dimension `p`; let `P=A x F_p` have the standard law above.
Then `beta!=0` and `P'=F_p`.

Index formal supports by every pair `(c,d) in A x F_p`, writing `c=b+r` with
`b in B`, `r in R`.

- If `b=0`, take `D=0`, `L=I`, and `ell=0`. Since `c` is radical,
  `alpha^p=I=iota_c`, while `Lc=c` and `ell(c)=0`.
- If `b!=0`, choose `f in B` with `beta(f,b)!=0`. In `R`, choose a chain
  `w_(p-2),...,w_0` spanning a complement to `r` (or any `(p-1)`-space if
  `r=0`). Define

  `D f=w_(p-2)`, `D w_i=w_(i-1)`, `D w_0=0`,

  and let `D` kill `b`, `r`, and the remaining fixed radical direction. Put
  `L=I+D`, define `ell(w_0)=beta(f,b)`, and let `ell` vanish on the other chosen
  basis vectors. Then `D^p=0`, `L` preserves `beta`, `Lc=c`, `ell(c)=0`, and

  `ell(D^(p-1)a)=beta(a,c)` for every `a`.

Thus every indexed datum satisfies all pointwise action-power identities and the
full formula `(4.1)`. Moreover, its support contains its index point `(c,d)`, by
taking input `a=0`. Consequently the union of these formal supports is exactly
`A x F_p`, despite `beta!=0`.

The construction can also make the central shear visible rather than relying on
the chosen `d`: in the second case, input `a=t w_(p-2)` has
`D^(p-1)a=0` and `ell(D^(p-2)a)=t beta(f,b)`, so one support contains every
central coordinate over its projected point `c`.

This is the required non-witness failure datum. It proves only that gates 1--4,
isotropy, central-coordinate bookkeeping, and set covering **pointwise** cannot
force `beta=0`. The omitted cross identities are exactly what prevents it from
being treated as a group, much less an in-scope counterexample.

## Hard kill and cycle outcome

- `2026-08-17T05:23:00Z`: Lead-directed hard proof-attempt stop recorded at
  cumulative active minute `234`. No common `(a,z)` excluded from every `S_h`
  under the target-level assumption `beta!=0` was found. Mathematical exploration
  stopped here; only failure-certificate packaging follows.

Outcome: `STRATEGY_EXHAUSTED` for `MCO-AFFINE-NORM-COVER`, with conditional
`PARTIAL_RESULT` candidates (nondegenerate `beta` excluded; radical, order, and
class lower bounds) awaiting Validator reconstruction. The unrestricted target is
unanswered. The formal cover above is explicitly non-witness data.

Validator attack surface: norm-factor order and signs; the two weighted sums in
`(4.1)`; self-adjointness with degenerate `beta`; factor conventions in
`(5.1)`--`(5.7)`; the conditional lower-bound chain; and strict separation of the
pointwise formal cover from any one extension.

- `2026-08-17T05:25:04Z`: final six-minute packaging window closed at cumulative
  active minute `240`; `findings.md` and the Lead `REPORT` were written. Work
  stopped at the assignment ceiling.
