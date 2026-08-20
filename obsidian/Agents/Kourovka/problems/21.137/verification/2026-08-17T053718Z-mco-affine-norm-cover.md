---
title: "Verification — Kourovka 21.137 — MCO affine-norm cover"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Conditional on the reviewed minimum-counterexample reduction, the submitted affine norm-support and cross-coset identities are exact, the stated lower-bound implications are valid but nonnew or weaker than reviewed bounds, and the formal pointwise cover is only a failure certificate, not a group or witness."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual value set P={g^p:g in G} is a subgroup, then P is abelian."
excluded_scopes: ["general powerfulness clause", "21.137/two-group-exponent-8", "every p=2 case", "odd-prime groups whose exponent is not exactly p^2", "quarantined wreath-shaped material"]
target_object: "Every finite p-group in the rendered odd-prime, exact-exponent-p^2 clause."
witness_object: "No exhibited witness; a hypothetical reviewed minimum counterexample and a separate family of pointwise formal support data without extension compatibility."
witness_equals_target: false
citation: "none"
verification_method: "Independent line-by-line hand derivation from the rendered source, canonical scope, assigned refs, and Lead-authorized comparisons with three already reviewed local partial bounds."
tools_used: ["Poppler 24.02.0 for visual source rendering", "Python 3.12.3 availability probe only", "read-only POSIX shell utilities"]
scope_answered: ["conditional affine norm-support identities in the reviewed minimum-counterexample model", "pointwise-formula insufficiency as a formal non-extension certificate"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
outcome: STRATEGY_EXHAUSTED
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137 — MCO affine-norm cover

## The claim

The submission does **not** claim a proof or counterexample.  It claims exact
local and cross-coset formulas in the already reviewed hypothetical
minimum-counterexample model, several conditional necessary bounds, and two
failure certificates showing why the chosen separator does not follow from the
identities obtained.  It reports `STRATEGY_EXHAUSTED` and
`active_assignment_answered: no`.

That characterization is accurate.  The formulas survive independent hand
reconstruction, but the lower bounds are rederivations or weaker than existing
reviewed bounds.  The active universal assertion remains unanswered.

## Scope, revision, and clause matrix

Rendered source page 184 was inspected visually.  The canonical record locks
`21.137/odd-prime-exponent-p2`, assignment revision `2`, and faithfully selects
only the middle source question.

| source clause | active? | result of this submission |
|---|---:|---|
| If the `p`th powers in a finite `p`-group form a subgroup, must it be powerful? | no | excluded and unanswered |
| For `p != 2`, exponent exactly `p^2`, actual `p`th powers a subgroup; must it be abelian? | yes | conditional identities and failure certificate only; unanswered |
| For a `2`-group of exponent `8`, square values a subgroup; must it be abelian? | no | excluded and unanswered |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independent audit | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | the work starts conditionally from an arbitrary hypothetical minimum counterexample and never eliminates it | unresolved |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | oddness is used for `1/2`, for the alternating self-pairing argument, and in the characteristic-`p` identities | pass |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | retained from the reviewed reduction; the finite `p`-group module argument is used | conditional-pass |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | retained from the reviewed reduction; it gives `exp(P)=p` and `exp(G/P)=p` | conditional-pass |
| `21.137-odd-power-set-definition` | admissibility | `P` is the actual value set | the identity `Pow_p(G)=union_h S_h` is elementwise, not a generated-subgroup substitute | conditional-pass |
| `21.137-odd-power-set-subgroup` | admissibility | the actual value set is a subgroup | used exactly as `union_h S_h=P` | pass as hypothesis |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | equivalent here to `beta=0`; it is not established | unresolved |

No claim-check JSON is required: the routed artifact is a
`STRATEGY_EXHAUSTED`/conditional-`PARTIAL_RESULT` submission, not a `CLAIM` or
`STALE_MATCH`.

## Target versus witness

The target is the universal source class.  There is no computed or exhibited
group.  The first object is only a hypothetical minimum counterexample, and the
second is explicitly a collection of pointwise affine data with no group on its
index set and no factor system.  Thus `witness_equals_target: false`; neither
object is an in-scope counterexample.

## 1. Class-two coordinates and signs

Retain the reviewed reduction

`N=P'=C_p <= Z(G)`, `exp(P)=p`, `A=P/N`, and `H=G/P`.

For odd `p`, the class-two exponent-`p` group `P` has standard coordinates

`P=A x F_p`,

`(a,z)(b,w)=(a+b,z+w+(1/2)beta(a,b))`.

The inverse of `(a,z)` is `(-a,-z)`, and direct multiplication gives

`[(a,z),(b,w)]=(0,beta(a,b))`.

Fix the convention `y^x=x^(-1)yx`.  For a lift `x_h`, put
`alpha_h(k)=k^(x_h)` and `x_h^p=(c_h,d_h)`.  Since `N<=Z(G)`,

`alpha_h(a,z)=(L_h a,z+ell_h(a))`,

where `L_h` preserves `beta` and `ell_h` is linear.  Inner conjugation by
`(c,d)` has the exact sign

`(a,z)^(c,d)=(a,z+beta(a,c))`.

Consequently `alpha_h^p=iota_(c_h,d_h)` and
`alpha_h(c_h,d_h)=(c_h,d_h)` give, with `D_h=L_h-I`,

`L_h^p=I`, `D_h^p=0`,

`ell_h((I+L_h+...+L_h^(p-1))a)=beta(a,c_h)`,

`L_hc_h=c_h`, and `ell_h(c_h)=0`.

In characteristic `p`, polynomial division of
`T^p-1=(T-1)^p` gives

`I+L_h+...+L_h^(p-1)=D_h^(p-1)`.

All signs in this block pass.

## 2. Ordered norm factors and the complete central coordinate

The right-action convention gives `kx_h=x_h alpha_h(k)`.  Induction therefore
gives the factor order

`(x_hk)^p=x_h^p alpha_h^(p-1)(k) ... alpha_h(k) k`.

The factors are genuinely in descending action order; reversing them would
reverse the alternating cocycle contribution.

Abbreviate `L=L_h`, `D=L-I`, `ell=ell_h`, and set
`E_i=I+L+...+L^(i-1)`, with `E_0=0`.  For `k=(a,z)`,

`alpha^i(k)=(L^i a,z+ell(E_i a))`.

Multiplying the displayed norm factors in their actual order yields projected
coordinate `D^(p-1)a` and central coordinate

`sum_(i=0)^(p-1) ell(E_i a)
 +(1/2)sum_(0<=j<i<=p-1) beta(L^i a,L^j a)`.

The input central coordinate contributes `pz=0`, so no fibre coordinate has
been suppressed.

### First weighted identity

Expanding `L=I+D`, the coefficient of `D^m` in `sum_i E_i` is

`sum_(q=m)^(p-2) (p-1-q) binom(q,m)=binom(p,m+2)`.

This vanishes modulo `p` for `0<=m<=p-3` and equals `1` for `m=p-2`.
Hence

`sum_i E_i=D^(p-2)`.

### Second weighted identity

Invariance of `beta` gives

`sum_(j<i) beta(L^i a,L^j a)
 =sum_(r=1)^(p-1)(p-r)beta(L^r a,a)
 =-sum_(r=1)^(p-1)r beta(L^r a,a)`.

Differentiating
`1+T+...+T^(p-1)=(T-1)^(p-1)` in characteristic `p` gives

`sum_(r=1)^(p-1) rL^r=-L D^(p-2)`.

Thus the double sum is `beta(LD^(p-2)a,a)`.  The norm
`D^(p-1)=sum_i L^i` is self-adjoint for `beta`, because
`sum_i L^(-i)=sum_i L^i`.  Therefore

`beta(D^(p-1)a,a)=beta(a,D^(p-1)a)=-beta(D^(p-1)a,a)=0`

at odd `p`.  Since `LD^(p-2)=D^(p-2)+D^(p-1)`, the second identity is

`sum_(j<i) beta(L^i a,L^j a)=beta(D^(p-2)a,a)`.

Finally, left multiplication by `(c_h,d_h)` contributes the possible term
`(1/2)beta(c_h,D_h^(p-1)a)`.  Self-adjointness and `L_hc_h=c_h` give

`beta(c_h,D_h^(p-1)a)=beta(D_h^(p-1)c_h,a)=0`.

Therefore the exact support is

`S_h={(c_h+D_h^(p-1)a,
       d_h+ell_h(D_h^(p-2)a)
          +(1/2)beta(D_h^(p-2)a,a)):a in A}`.                 `(F1)`

For each admitted `a`, all `p` choices of `z` give the same output.  Hence

`M(u,z)=p sum_h #{a:
 c_h+D_h^(p-1)a=u,
 d_h+ell_h(D_h^(p-2)a)+(1/2)beta(D_h^(p-2)a,a)=z}`.          `(F2)`

Both formulas pass for every odd prime, including `p=3`.

## 3. Isotropy and the nondegenerate branch

No nondegeneracy is needed for the adjoint identity

`beta(Du,v)=beta(u,(L^(-1)-I)v)`.

Since `L^(-1)-I=-L^(-1)D`, `p-1` is even, and `D^p=0`,

`beta(D^(p-1)u,D^(p-1)v)
 =beta(u,L^(-(p-1))D^(2p-2)v)=0`.

Thus `im D^(p-1)` is `beta`-isotropic even when `beta` is degenerate.

The action-power identity also gives

`c_h in (ker D_h^(p-1))^(perp_beta)`.

If `beta` is nondegenerate, self-adjointness identifies the right side with
`im D_h^(p-1)`.  Hence every projected support lies in

`im D_h^(p-1) <= (L_h-I)A <= [A,H]`.

The anti-representation `L_(hj)=L_jL_h` of the finite `p`-group has a nonzero
fixed covector on `A^*`; equivalently `[A,H]` is proper.  Exact covering is then
impossible.  The submitted nondegenerate contradiction passes.  In the
degenerate case, only the orthogonality statement is justified; the submission
correctly does not replace it by `c_h in im D_h^(p-1)`.

## 4. Cross-coset identities and factor order

Normalize `x_1=1` and define the right factor

`x_hx_j=x_(hj)u_(h,j)`, `u_(h,j)=(r_(h,j),s_(h,j))`.

For right conjugation,

`alpha_j alpha_h(k)=k^(x_hx_j)
 =iota_(u_(h,j))(alpha_(hj)(k))`.

The coordinate rows are therefore

`L_(hj)=L_jL_h`,

`ell_h(a)+ell_j(L_ha)
 =ell_(hj)(a)+beta(L_(hj)a,r_(h,j))`.                         `(C1)`

Associating `x_hx_jx_k` in the two ways and using
`u x_k=x_k alpha_k(u)` gives

`u_(hj,k)alpha_k(u_(h,j))=u_(h,jk)u_(j,k)`.                 `(C2)`

Its two coordinates are exactly

`r_(hj,k)+L_kr_(h,j)=r_(h,jk)+r_(j,k)`,                    `(C3)`

`s_(hj,k)+s_(h,j)+ell_k(r_(h,j))
 +(1/2)beta(r_(hj,k),L_kr_(h,j))
 =s_(h,jk)+s_(j,k)+(1/2)beta(r_(h,jk),r_(j,k))`.             `(C4)`

The order in `(C5)` also passes.  Indeed,

`x_h^2=x_(h^2)u_(h,h)`,

`x_h^3=x_(h^3)u_(h^2,h)alpha_h(u_(h,h))`,

and induction gives, because `h^p=1` in `H`,

`(c_h,d_h)=u_(h^(p-1),h) alpha_h(u_(h^(p-2),h)) ...
             alpha_h^(p-2)(u_(h,h))`.                        `(C5)`

Thus neither the factor list nor its action exponents may be reversed.  Finally,
conjugating actual powers gives `alpha_j(S_h)=S_(h^j)`.  These are necessary
cross-coset identities; the audit makes no converse existence claim.

## 5. Conditional lower-bound chain

Let `R=rad(beta)` and `B=A/R`.  The finite `p`-group action on the nonzero
nondegenerate module `B` has a nonzero common fixed vector `v_bar`.  For a lift
`v`, every `D_hv` lies in `R`, hence so does `D_h^(p-1)v`.  The functional

`psi(a)=beta(v,a)`

is nonzero and kills `D_h^(p-1)A`, because the norm is self-adjoint and its value
on `v` lies in `R`.

Choose `a_*` with `psi(a_*)=1`.  Exact projected covering places `a_*` in some
`c_h+D_h^(p-1)A`, so

`1=psi(c_h)=ell_h(D_h^(p-1)v)`.

Therefore `D_h^(p-1)v!=0`.  The vectors

`v,D_hv,...,D_h^(p-1)v`

are linearly independent; the last `p-1` lie in `R`.  Since the nondegenerate
alternating quotient `B` has dimension at least `2`, this proves

`dim R>=p-1`, `dim A>=p+1`, and `|P|=p^(dim A+1)>=p^(p+2)`.

The chosen `h` acts nontrivially, so `|H|>=p` and
`|G|=|P||H|>=p^(p+3)`.

For the class calculation, choose `y in P` with image `v` and set `x=x_h`.
Under `[u,x]=u^(-1)u^x`, the `A`-coordinate of `[y,_(m)x]` is `D_h^m v`.
At `m=p-1` this is the nonzero `L_h`-fixed radical vector
`r=D_h^(p-1)v`, and the next commutator is

`[[y,_(p-1)x],x]=(0,ell_h(r))!=1`.

It has weight `p+1`, so this argument proves `class(G)>=p+1`.

Every implication in that chain is valid.  None of its numerical conclusions is
new relative to already reviewed local work:

| submitted consequence | prior reviewed comparison | classification |
|---|---|---|
| `beta` must be degenerate; `dim R>=p-1` | `2026-08-16T124523Z-common-flag-center-audit.md` proves `dim Z(Q)>=p` in its notation; under the Lead-specified translation that `Q` is the present `P`, and `Z(P)/N=R`, this is `dim R>=p-1` | rederived |
| `dim A>=p+1`, `|P|>=p^(p+2)` | follows from that same radical bound and the nonzero symplectic quotient | rederived consequence |
| `|G|>=p^(p+3)` | `2026-08-16T124226Z-identity-coset-refinement-audit.md` already proves `|G|>=p^(2p+3)` | valid but strictly weaker |
| `class(G)>=p+1` | `2026-08-16T144312Z-class-p-plus-one-hall-lemma.md` proves every exponent-dividing-`p^2` group of class at most `p+1` has commuting `p`th powers; an actual counterexample must therefore have class at least `p+2` | valid but strictly weaker |

The last comparison is independent of the new commutator-chain validation: this
audit accepts exactly the chain's `class(G)>=p+1`, while the stronger
`class(G)>=p+2` comes from the separate reviewed theorem.

## 6. Coinvariant and carry-cocycle obstruction

Put `C=A/[A,H]`.  Every `D_h^(p-1)A` vanishes in `C`, so exact cover makes

`kappa(h)=c_h+[A,H]`

surjective.  Reducing `(C3)` gives a normalized ordinary `2`-cocycle
`r_bar` with trivial action, and the `A`-coordinate of `(C5)` gives

`kappa(h)=sum_(m=1)^(p-1) r_bar_(h^m,h)`.                   `(X1)`

For `H=C_p` and `C=F_p`, choose residue representatives in `C_(p^2)` and let
`r_bar(i,j)` be `1` exactly when their integer sum crosses `p`.  It satisfies
the normalized cocycle identity.  Adding residue `i` successively around its
length-`p` cycle has total carry `i`, so `(X1)` gives `kappa(i)=i`, which is
surjective.

This calculation is exact, but its logical reach is narrow: `(C3)` plus the
projected part of `(C5)` does not force a missing coinvariant.  It does not
satisfy or test `(C1)`, `(C4)`, nonzero `beta`, or the full extension problem,
and it is not a target group.

## 7. Formal pointwise cover

Let `A=B direct_sum R`, where `B` is a symplectic plane and `dim R=p`.  For each
formal index `(c,d)`, write `c=b+r`.

If `b=0`, take `D=0`, `L=I`, and `ell=0`.  Then `c in R`, so
`iota_c=I=alpha^p`, and `(F1)` contains `(c,d)`.

If `b!=0`, choose `f in B` with `beta(f,b)!=0`.  Choose radical vectors
`w_(p-2),...,w_0` spanning a complement to `r` (or any `(p-1)`-space if
`r=0`) and define

`Df=w_(p-2)`, `Dw_i=w_(i-1)`, `Dw_0=0`,

while killing `b`, `r`, and the remaining radical basis vector.  Put `L=I+D`,
set `ell(w_0)=beta(f,b)`, and set `ell=0` on the other basis vectors.

Then `D^p=0`.  Because `im D<=R`, `L` preserves `beta`.  Also `Dc=0` and
`ell(c)=0`.  Writing an arbitrary vector's `B`-part as `lambda b+mu f` gives

`ell(D^(p-1)a)=mu beta(f,b)=beta(a,b+r)=beta(a,c)`.

Thus all pointwise action-power identities hold.  Formula `(F1)` contains the
index point `(c,d)` at input `a=0`, so the union over all formal indices is
`A x F_p`.  Moreover, for `a=t w_(p-2)`,

`D^(p-1)a=0`, `D^(p-2)a=t w_0`,

and the quadratic pairing vanishes because the chain lies in `R`; varying `t`
fills the whole vertical fibre over `c`.  This remains correct at the edge case
`p=3`, where the chain is `w_1 -> w_0 -> 0`.

The construction has no multiplication on its index set, no single family
`u_(h,j)`, and no simultaneous satisfaction of `(C1)`--`(C5)`.  It is not
cross-compatible extension data, not a group, not a finite target object, and
not a counterexample.  It proves only that the pointwise formulas, isotropy,
central bookkeeping, and set cover do not by themselves force `beta=0`.

## Subclaims and what each method proves

| subclaim family | method | what a pass proves | what it does not prove |
|---|---|---|---|
| `(F1)`, `(F2)` | ordered class-two hand collection | exact value supports in the conditional model | a common missing value |
| isotropy/nondegenerate branch | degenerate-safe bilinear algebra | nondegenerate `beta` is impossible in a hypothetical minimum counterexample | the degenerate branch |
| `(C1)`--`(C5)` | direct right-action reassociation | necessary factor-system equations with the displayed signs/order | existence or sufficiency |
| radical chain | linear algebra and iterated commutators | the displayed necessary bounds | novelty or the active conclusion |
| carry datum | explicit hand cocycle | the projected cocycle equations alone permit surjective `kappa` | full compatibility with `beta` |
| formal cover | explicit basis construction | pointwise local conditions admit a cover with `beta!=0` | any group or witness |

## Evidence

No mathematical computation, web search, literature search, solution-bearing
history search, delegate, quarantined wreath material, or `p=2` argument was
used.  Lead later authorized only the explicit comparison with three already
reviewed local partial bounds named above.

The tool probe was:

```text
$ for t in gap sage python3 magma pdftoppm pdftotext; do command -v "$t" || true; done
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftoppm
/usr/bin/pdftotext
$ python3 --version
Python 3.12.3
$ pdftoppm -v
pdftoppm version 24.02.0
$ pdftotext -v
pdftotext version 24.02.0
```

The configured PDF page 184 was rendered with Poppler and inspected visually.
The mathematical evidence is the hand reconstruction printed in Sections 1--7.

## Verdict

`STRATEGY_EXHAUSTED` is upheld.  The affine-support identities, cross-coset
identities, nondegenerate contradiction, conditional implication chain,
coinvariant obstruction, and formal pointwise cover all pass the requested hand
audit, with the logical ceilings stated above.

Overall certification remains `status/conjectured`; no status tag is raised.
The accepted lower bounds are nonnew or weaker than reviewed results, and
`active_assignment_answered: no`.

## Why this verdict

The exact right-action convention fixes all inner-conjugation and factor-system
signs.  Direct collection recovers both weighted characteristic-`p` identities
and the missing-candidate central terms, which vanish for proved reasons rather
than by omission.  The radical argument is valid without a hidden
nondegeneracy assumption.  The two formal obstructions are correctly limited to
the identities they actually satisfy.

None of this supplies the absent global compatibility argument forcing
`beta=0`, and no target-equal object exists to validate as a counterexample.

## What is NOT established

- The actual `p`th-power subgroup is not proved abelian for arbitrary admissible
  `G`.
- No admissible finite group or counterexample is constructed.
- The formal supports are not shown to arise simultaneously from one extension.
- The carry cocycle is not coupled to `(C1)`, `(C4)`, or nonzero `beta`.
- No new numerical lower bound survives comparison with the already reviewed
  center, order, and class results.
- The general powerfulness clause, every `p=2` case, and the exponent-8 clause
  are untouched.

## What would upgrade it

A new global compatibility argument would have to combine the factor-system
equations, especially `(C4)`, with `(X1)` and the alternating pairing strongly
enough to force `beta=0`; alternatively, an explicit finite group would have to
pass every revision-2 admissibility row and have nonabelian actual power
subgroup.  Neither is present.
