---
title: "21.137 — MCO-AFFINE-NORM-COVER failure certificate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: MCO-AFFINE-NORM-COVER
direction: proof
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

# Outcome

`STRATEGY_EXHAUSTED` for `MCO-AFFINE-NORM-COVER` at cumulative active minute
`240`. The exact arbitrary-odd-prime support and cross-coset identities were
derived, but no common point excluded from every support under merely
`beta!=0` was obtained. The unrestricted target remains unanswered.

Exact target: for every odd prime `p` and finite `p`-group `G` of exponent exactly
`p^2`, if the actual value set `P={g^p:g in G}` is a subgroup, then `P` is
abelian.

## Constraint-and-conclusion matrix

| constraint_id | role | use in this run | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | Worked conditionally from an arbitrary hypothetical minimum counterexample; no universal conclusion was reached. | unresolved |
| `21.137-odd-p-not-2` | admissibility | `p` remained arbitrary odd; `1/2`, parity of `p-1`, and characteristic-`p` norm identities were used. | pass |
| `21.137-odd-finite-p-group` | admissibility | Retained from the reviewed reduction; `H=G/P` is a finite `p`-group. | pass conditionally |
| `21.137-odd-exponent-p2` | admissibility | Retained exactly; the reviewed reduction supplies `exp(P)=p`, and `H` has exponent `p`. | pass conditionally |
| `21.137-odd-power-set-definition` | admissibility | Used the elementwise equality `Pow_p(G)=union_h S_h`, never a generated subgroup. | pass conditionally |
| `21.137-odd-power-set-subgroup` | admissibility | Used as the exact cover `union_h S_h=P`, equivalently `M(t)>0` for all `t in P`. | pass as hypothesis |
| `21.137-odd-P-abelian` | target conclusion | Equivalent in the reviewed reduction to `beta=0`; no proof was obtained. | unresolved |

# Exact formulas reached

Work in the reviewed minimum-counterexample setup

`N=P'=C_p<=Z(G)`, `exp(P)=p`, `A=P/N`, `H=G/P`.

In standard odd-prime class-two coordinates,

`P=A x F_p`,

`(a,z)(b,w)=(a+b,z+w+(1/2)beta(a,b))`.

For a lift `x_h`, write

`alpha_h(a,z)=(L_h a,z+ell_h(a))`, `D_h=L_h-I`,
`x_h^p=(c_h,d_h)`.

Then, with all signs checked under `y^x=x^(-1)yx`,

`L_h^p=I`, `D_h^p=0`,

`ell_h(D_h^(p-1)a)=beta(a,c_h)`,

`L_hc_h=c_h`, `ell_h(c_h)=0`,

and

`I+L_h+...+L_h^(p-1)=D_h^(p-1)`.

The exact support from the whole coset `x_hP` is

`S_h={(c_h+D_h^(p-1)a,
       d_h+ell_h(D_h^(p-2)a)
          +(1/2)beta(D_h^(p-2)a,a)):a in A}`.                 `(F1)`

The input central coordinate disappears because it contributes `p z=0`; no
central coordinate is suppressed. Hence

`M(u,z)=p sum_h #{a:
 c_h+D_h^(p-1)a=u,
 d_h+ell_h(D_h^(p-2)a)+(1/2)beta(D_h^(p-2)a,a)=z}`.          `(F2)`

The weighted identities behind `(F1)` are

`sum_i(I+...+L_h^(i-1))=D_h^(p-2)`

and

`sum_(j<i) beta(L_h^i a,L_h^j a)=beta(D_h^(p-2)a,a)`.

Also `im D_h^(p-1)` is `beta`-isotropic. The proof uses

`beta(Du,v)=beta(u,(L^(-1)-I)v)`

and `D^p=0`; it does not assume that `beta` is nondegenerate.

# Cross-coset identities

Normalize `x_1=1` and set

`x_hx_j=x_(hj)u_(h,j)`, `u_(h,j)=(r_(h,j),s_(h,j))`.

Then

`alpha_j o alpha_h=iota_(u_(h,j)) o alpha_(hj)`,

`L_(hj)=L_jL_h`,

`ell_h(a)+ell_j(L_ha)=ell_(hj)(a)+beta(L_(hj)a,r_(h,j))`,    `(C1)`

and associativity is

`u_(hj,k)alpha_k(u_(h,j))=u_(h,jk)u_(j,k)`.                 `(C2)`

Its `A`-coordinate is

`r_(hj,k)+L_kr_(h,j)=r_(h,jk)+r_(j,k)`,                    `(C3)`

while its central coordinate, including the cocycle term, is

`s_(hj,k)+s_(h,j)+ell_k(r_(h,j))
 +(1/2)beta(r_(hj,k),L_kr_(h,j))
 =s_(h,jk)+s_(j,k)+(1/2)beta(r_(h,jk),r_(j,k))`.             `(C4)`

Since `H` has exponent `p`, the exact cyclic factor identity is

`(c_h,d_h)=u_(h^(p-1),h) alpha_h(u_(h^(p-2),h)) ...
             alpha_h^(p-2)(u_(h,h))`.                        `(C5)`

Finally `alpha_j(S_h)=S_(h^j)`. These are the written compatibility conditions;
the failure below does not treat independent supports as one extension.

# Conditional partial results exposed by the strategy

Let `[A,H]=span_h (L_h-I)A`. It is proper because a finite `p`-group module over
`F_p` has a nonzero trivial quotient.

If `beta` is nondegenerate, the pointwise action-power identity gives

`c_h in (ker D_h^(p-1))^perp=im D_h^(p-1)`.

Thus every projected support lies in `[A,H]`, contradicting exact covering.
Therefore a hypothetical minimum counterexample must have `rad(beta)!=0`.

More precisely, choose a nonzero common fixed vector in the nondegenerate module
`A/rad(beta)`. Exact covering forces some `h` and lift `v` with

`D_h^(p-1)v!=0` and `ell_h(D_h^(p-1)v)!=0`.

Consequently

`dim rad(beta)>=p-1`, `dim A>=p+1`,

`|P|>=p^(p+2)`, `|G|>=p^(p+3)`, and `class(G)>=p+1`.

These are conditional `PARTIAL_RESULT` candidates only, at
`status/conjectured`, pending independent reconstruction.

# First failed cross-coset implication

Put `C=A/[A,H]`. Each norm direction dies in `C`, so exact covering forces

`kappa(h)=c_h+[A,H]`

to be surjective. Reducing `(C3)` gives an ordinary trivial-module 2-cocycle,
and `(C5)` becomes

`kappa(h)=sum_(m=1)^(p-1) r_bar_(h^m,h)`.                   `(X1)`

This cross identity does not force a missing coinvariant. The standard carry
cocycle for `C_(p^2)->C_p`, used only as formal quotient data, satisfies `(X1)`
and makes `kappa(i)=i`, hence surjective. It is not a target group or a
counterexample.

The exact degenerate obstruction is

`beta(v,c_h)=ell_h(D_h^(p-1)v)`.

Long radical shear chains can make this scalar nonzero, so the invariant-covector
separator from the nondegenerate branch does not survive. Equations `(C1)`--`(C5)`
retain this as the unresolved full extension cocycle problem rather than forcing
it to vanish.

# Explicit pointwise formal cover — not a group

Fix arbitrary odd `p`. Let `A=B direct_sum R`, with `B` a symplectic plane and
`R=rad(beta)` of dimension `p`. For every `(c,d) in A x F_p`, write `c=b+r`.

If `b=0`, use `L=I`, `ell=0`. If `b!=0`, choose `f in B` with
`beta(f,b)!=0` and a radical chain

`w_(p-2) -> ... -> w_0 -> 0`

in a complement to `r`. Set `Df=w_(p-2)`, let `D` shift the chain, kill `b,r`,
put `L=I+D`, and set `ell(w_0)=beta(f,b)`, zero elsewhere. Then every pointwise
identity above holds: `D^p=0`, `L` preserves `beta`, `Lc=c`, `ell(c)=0`, and

`ell(D^(p-1)a)=beta(a,c)`.

Formula `(F1)` contains `(c,d)` at input `a=0`; hence the union of all these
formal supports is exactly `A x F_p` with `beta!=0`. In the second case the
central shear itself fills a complete vertical fibre by varying the top chain
coordinate.

There is deliberately no multiplication on the index set and no factors
`u_(h,j)`. This is not an extension, not a finite target group, and not a
counterexample. It is the required certificate that every pointwise formula,
isotropy, cardinality, and full central bookkeeping can coexist with a cover.

# Limitations and validator attack surface

- Recheck existence and signs of the standard `A x F_p` coordinates and the
  order of the norm factors.
- Recheck the two weighted characteristic-`p` identities in `(F1)`.
- Recheck self-adjointness of `D^(p-1)` without assuming nondegeneracy.
- Reconstruct `(C1)`--`(C5)` from the chosen right-factor convention.
- Audit the nondegenerate separator and the radical-dimension, order, and class
  lower bounds independently.
- Verify that the formal cover satisfies pointwise identities only and cannot be
  mistaken for cross-compatible extension data.

No web/history, computation, delegate, matrix catalogue, Hall-span enlargement,
split ansatz, wreath material, `p=2` case, or excluded exponent was used. A future
route would need a genuinely new cohomological obstruction coupling `(C4)` and
`(X1)` to `beta`; that pivot was not begun in this run.

Detailed derivations and the active ledger are in
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r9-mco-affine-norm-cover/log.md`.
