---
title: "Verification — Kourovka 12.15 — order-128 R1/R2 eliminations"
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
claim: "Conditional on the reviewed order-128 R1/R2 reduction, R1 and both R2 centre types are impossible; the elementary-centre proof requires a corrected normalization, and the explicit local presentation exists but violates the source hypothesis."
claimant: Problem-12.15
target_statement: "For every finite 2-group G in which equality of normal closures implies conjugacy, G' is abelian."
excluded_scopes: []
target_object: "An arbitrary finite 2-group satisfying the exact source normal-closure-fibre hypothesis."
witness_object: "Arbitrary groups satisfying the reviewed order-128 R1 or R2 structural data; separately, the explicit elementary-centre group G0."
witness_equals_target: false
citation: "Direct conditional hand proofs in this note; no external citation."
verification_method: "line-by-line finite-group and commutator proof, including an independent semidirect-product model for G0"
tools_used: ["GAP 4.12.1 (availability/version probe only; no verification run)", "Python 3.12.3 (availability/version probe only)", "Poppler pdftotext 24.02.0", "rendered source PDF page 58"]
scope_answered: ["order-128 regime R1", "order-128 regime R2 with A=C4", "order-128 regime R2 with A=C2^2", "the explicit G0 presentation and its named fibre witness"]
scope_not_answered: ["possible least counterexamples of order greater than 128", "12.15/normal-closure-fibres"]
active_assignment_answered: no
partial_result_certifiable: yes
verdict: PASS_WITH_CORRECTION_BOUNDED_PARTIAL
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/2-groups, topic/commutator-calculus, project/kourovka, status/conjectured]
---

# Verification — Kourovka 12.15

## Verdict

**PASS WITH ONE REQUIRED CORRECTION, as a bounded `PARTIAL_RESULT`.**

The action-trivial dependency, the R1 elimination, the cyclic-centre R2
elimination, the universal elementary-centre R2 fibre obstruction, and the
existence/invariants of the single displayed group `G0` all admit independent
hand proofs.  However, the submitted elementary-centre normalization is false as
written: multiplying the outside lift by an element of `H` cannot change its
`A/Z`-valued residual.  The universal conclusion survives after changing the
proof order and replacing the **quotient complement vector** by its sum with a
kernel vector.  The corrected proof is given below.

This verdict eliminates only the reviewed R1/R2 portion of the order-128 branch.
Combined with the separate R3 verdict
`verification/2026-08-17T090657Z-r3-defect-size-correction.md`, it eliminates the
reviewed order-128 remainder.  It does not address any larger order and does not
answer the active source assignment.

The bounded hand result is mathematically checkable, but its note remains
`status/conjectured` because the protocol forbids `status/proven` before human
review.  No claim-check JSON was supplied because the routed artifacts are
`PARTIAL_RESULT` questions rather than a formal scope-closing `CLAIM`.

## Scope, revision, and clause matrix

The rendered issue-12 PDF page 58 has one clause: for a finite 2-group, does the
normal-closure-fibre hypothesis force the derived subgroup to be abelian?  The
canonical revision-1 scope faithfully records it.

| clause | active | what this verdict proves | what remains |
|---|---:|---|---|
| c1, all finite 2-groups satisfying the fibre hypothesis | yes | no group in any reviewed order-128 R1/R2 regime can be a counterexample | every possible larger-order regime; the unrestricted implication |

Thus `active_assignment_answered: no` mechanically, irrespective of the strength
of the bounded result.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | proof use / candidate value | evidence | result |
|---|---|---|---|---|---|
| 12.15-forall-G | admissibility | every admissible finite 2-group | only the reviewed order-128 R1/R2 cases are treated | clause boundary above | fail for full scope |
| 12.15-finite | admissibility | G finite | conditional regimes have order 128; `G0` has a hand-constructed 128-element model | proofs below | pass conditionally |
| 12.15-two-group | admissibility | G a 2-group | every conditional layer and every normal form in `G0` has 2-power order | structural data / model below | pass conditionally |
| 12.15-normal-closure-fibre | admissibility | equal normal closures imply conjugacy | R1 and cyclic R2 contradict necessary counterexample data; elementary R2 and `G0` have an explicit equal-closure/different-order pair | proofs below | no elementary R2 or `G0` object passes this row |
| 12.15-derived-abelian | target conclusion | G''=1 | no universal conclusion is proved; hypothetical R1/R2 counterexample regimes are eliminated | larger orders untouched | unproved globally |

`G0` is therefore an `OUT_OF_SCOPE_EXAMPLE` as a counterexample to the source:
it is useful because it proves local pc consistency and displays exactly why that
local table fails the source hypothesis.

## Target versus witness and circularity

The source target is an arbitrary qualifying finite 2-group.  R1 and R2 are
necessary cases only after importing the reviewed least-counterexample and
order-128 reductions.  They are not equal to the unrestricted target.  None of
the arguments below infers the source hypothesis from a quotient condition or
from pc consistency.  In the elementary-centre case the source hypothesis is
tested upstairs by an exact equality of two normal closures in `G`.

The explicit presentation was not constructed by imposing the desired source
hypothesis: it fails that hypothesis.  Its existence can support local
consistency only, never sufficiency for admissibility.

## Tool evidence and hard limit

The availability probe returned, verbatim,

```text
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftotext
/usr/bin/pdftoppm
4.12.1
Python 3.12.3
pdftotext version 24.02.0
```

Sage and Magma were not found.  No compute lease was granted and no GAP
verification was run.  The claimant's GAP transcript is not used as independent
evidence.  All mathematical verification below is by hand.

## Dependency 1 — the action on V is trivial

Put

\[
H=G',\qquad A=Z(H),\qquad V=H/A\cong C_2^2,\qquad E=G/H.
\]

Suppose the image of `E` on `V` were generated by a transvection `T`, and write
`F=ker(T-1)`, its one-dimensional fixed space.  Choose a basis
`e_0,e_1,...` of `E` with `e_0` active and all `e_i`, `i>0`, in the action
kernel.  The reviewed order-128 rows include `H=Phi(G)`, so lifts `x_i` of this
basis generate `G`.  Put

\[
w_{ij}=[x_i,x_j]A\in V.
\]

Projecting Hall--Witt to `V` gives

\[
\chi(e_k)(T-1)w_{ij}+\chi(e_i)(T-1)w_{jk}
 +\chi(e_j)(T-1)w_{ki}=0. \tag{1}
\]

For `i,j>0`, the triple `(e_0,e_i,e_j)` gives
`(T-1)w_{ij}=0`.  For an active-kernel pair, use the exact identity

\[
[x_0^2,x_i]=[x_0,x_i]^{x_0}[x_0,x_i]. \tag{2}
\]

Since `x_0^2 in H` and `x_i` acts trivially on `V`, the left side projects to
zero; the right side projects to `(T-1)w_{0i}`.  Hence every basic commutator
image lies in `F`.  But `G'` is the normal closure of the basic commutators, so
their `E`-orbits must span `G'A/A=V`.  A fixed line cannot span the two-dimensional
`V`, a contradiction.

Therefore

\[
[H,G]\le A \quad\text{in both R1 and R2}. \tag{3}
\]

This verifies the action-trivial dependency used by all three eliminations.  The
additional numerical packing rows in the earlier claimant note are not needed
for this verdict and are not promoted here.

## R1 — quotient-trivial actions on D8 and Q8

Here `A=Z(H)=H'=<z>` and `H` is `D8` or `Q8`.  Let
`b:H/A x H/A -> A` be the nondegenerate commutator form.  If an automorphism
`alpha` acts trivially on `H/A`, then

\[
\alpha(h)=h z^{f(hA)}
\]

for a linear functional `f` on `H/A`.  Nondegeneracy gives `tA` with
`f(v)=b(v,tA)`.  Thus `alpha(h)=h^t`, so `alpha` is inner.  This proves directly,
for both `D8` and `Q8`, that the kernel of
`Aut(H)->Aut(H/A)` is `Inn(H)`.

By (3), conjugation by every quotient lift has this form.  After multiplying each
lift by a suitable element of `H`, it centralizes `H`; hence

\[
G=H C_G(H).
\]

Set `C=C_G(H)`.  Cross commutators vanish, `H'<=A`, and

\[
C'\le C\cap G'=C\cap H=Z(H)=A.
\]

Consequently

\[
G'=H'C'\le A,
\]

contrary to the defining R1 row `G'=H` with nonabelian `H`.  This argument is
independent of all square, commutator-lift, and factor-set offsets.  R1 is
eliminated.

## Cyclic-centre R2 — every square lies in A

Now `A=Z(H)=<a>\cong C_4`, `z=a^2`, and the nonzero character
`psi:E->C_2` records inversion on `A`.  By (3), for `h in H`, `x in G`,

\[
c=[h,x]\in A,\qquad h^x=hc.
\]

If `psi(xH)=1`, then `c^x=c^{-1}`, so

\[
h^{x^2}=(hc)^x=hcc^x=h.
\]

If `psi(xH)=0`, then `x` fixes `A`.  Comparing

\[
(h^2)^x=(h^x)^2=h^2c^2
\]

with the fixed left side gives `c^2=1`; again `h^{x^2}=h`.  Thus every `x^2`
centralizes `H`.  Since `E` is elementary abelian, `x^2 in H`, whence

\[
x^2\in C_H(H)=A\qquad(x\in G). \tag{4}
\]

The quotient `G/A` has exponent two and is therefore abelian.  Hence `G'<=A`,
contrary to `G'=H` and `H/A\cong C_2^2`.  This eliminates **every** cyclic-centre
R2 row, including both `B=A` and the formerly free all-`B=Z` offset.  The full
earlier polarization table is unnecessary; (4) is the exact sufficient
critical-pair consequence.

## Elementary-centre R2 — corrected universal proof

Assume

\[
A=Z(H)=\langle a,z\rangle\cong C_2^2,\qquad H'=\langle z\rangle,
\qquad V=H/A\cong C_2^2,
\]

\[
E\cong C_2^3,\qquad G'=H,
\]

with (3), `A^E=<z>`, and the nonzero shear character
`psi:E->C_2`, where an element outside `K=ker(psi)` sends `a` to `az`.
Let `b` be the nondegenerate commutator form on `V`.

### The canonical residual map

For `e in E`, choose any lift `x`, and for `v in V` choose any lift `h in H`.
The value

\[
\bar\tau_e(v)=[h,x]Z\in A/Z
\]

is independent of both choices.  Changing `h` by `A` or `x` by `H` changes the
commutator only by an element of `Z`.  Composition of conjugations shows that
`e mapsto \bar\tau_e` is linear.  Hence there is a canonical linear map

\[
\Theta:E\longrightarrow V,qquad
\bar\tau_e(v)=b(v,\Theta(e)). \tag{5}
\]

This exposes the submitted normalization error: multiplying an outside lift by
an element of `H` does **not** change (5), so it cannot make a nonzero
`\bar\tau_e` vanish.

### First prove that Theta restricted to K is an isomorphism

Let `s(e)=x^2A in V`; this is independent of the lift.  If `e in K`, conjugation
by `x` fixes `A` and is trivial on `V`, so its square is the identity on `H`.
As `x^2 in H`, this gives

\[
s(e)=0\qquad(e\in K). \tag{6}
\]

If `psi(e)=1`, write `[h,x]=a^\epsilon z^\sigma`.  Applying conjugation twice
multiplies `h` by `z^\epsilon`, whereas conjugation by `x^2` multiplies it by
`z^{b(v,s(e))}`.  Therefore

\[
s(e)=\Theta(e)\qquad(\psi(e)=1). \tag{7}
\]

In `G/A`, the subgroup `V` is central.  Square polarization for `e` outside `K`
and `k in K`, using (6)--(7), gives

\[
[x_e,x_k]A=\Theta(k). \tag{8}
\]

For `k_1,k_2 in K`, the same calculation gives

\[
[x_{k_1},x_{k_2}]\in A. \tag{9}
\]

Commutators involving `H` already lie in `A`.  Since `G'=H`, equations (8)--(9)
must span `H/A=V`.  Thus

\[
\Theta|_K:K\overset{\sim}{\longrightarrow}V. \tag{10}
\]

### Correct normalization

Choose any `e_0` outside `K`.  By (10), there is a unique `k_0 in K` with
`\Theta(k_0)=\Theta(e_0)`.  Replace the complement vector by

\[
e=e_0+k_0.
\]

Then `psi(e)=1` and `\Theta(e)=0`.  Choose a lift `r` of this new complement.
Now, and only now,

\[
\bar\tau_r=0.
\]

Equation (7) gives `r^2 in A`.  Since `r` commutes with its square and the fixed
subgroup of its shear on `A` is `<z>`,

\[
r^2\in\langle z\rangle. \tag{11}
\]

Choose a basis `k,l` of `K` and representatives `u,v in H` so that

\[
\Theta(k)=uA,qquad \Theta(l)=vA.
\]

By (10), these vectors are independent, so `b(uA,vA)=1`.

### The order toggle

Every `h in H` has `h^2 in A`; because `A` has exponent two and `[H,G]<=A`, its
square is fixed by `E`, hence lies in `A^E=<z>`.  For the section
`s(alpha u+beta v)=u^alpha v^beta`, write

\[
s(t)^2=z^{q(t)},\qquad [s(t),r]=z^{\rho(t)}.
\]

The map `q` is quadratic with polar form `b`, and `rho` is linear.  Thus
`d=q+rho` satisfies

\[
d(u+v)=d(u)+d(v)+1. \tag{12}
\]

Among `u,v,u+v`, at least one has `d=1`: the four possibilities for
`(d(u),d(v))` are respectively handled by `uv,v,u,u`.  Choose the corresponding
nonidentity `h=s(t)` and put

\[
x=r,\qquad y=rh.
\]

The exact square identity gives

\[
y^2=r^2h^2[h,r]=r^2z. \tag{13}
\]

By (11), exactly one of `x,y` has order two and the other order four.  They cannot
be conjugate.

### Exact normal closures

By (8), the normal closure of `r` contains elements `U,V_0` with images `uA,vA`.
It then contains

\[
[U,V_0]=z.
\]

Because `\bar\tau_l(uA)=b(uA,vA)=1`, normality also gives
`[U,l] in aZ`.  Hence the normal closure contains `a,z,U,V_0`, and therefore all
of `H`.  Its image in the abelian quotient `E` is `<rH>`, so

\[
\langle r\rangle^G=\langle r,H\rangle. \tag{14}
\]

For `y=rh`, the factors `[h,k]` and `[h,l]` lie in `A`; therefore

\[
[y,k]A=uA,\qquad [y,l]A=vA.
\]

The same argument gives first `z`, then an element of `aZ`, then all of `H`.
Finally `r=yh^{-1}` lies in the normal closure, and hence

\[
\langle y\rangle^G=\langle r,H\rangle=\langle x\rangle^G. \tag{15}
\]

Equations (13)--(15) are inside `G` and do not depend on any central square,
commutator, or factor-set offset.  This direct structural proof covers every
actual pc-consistent elementary-centre R2 group.  It is stronger and safer than
checking that the ambient binary parameter cube has no omitted offset type.

## Independent hand construction of the displayed group G0

Let

\[
H=\langle z,a,u,v\mid z,a\in Z(H),\ z^2=a^2=u^2=v^2=1,
\ [u,v]=z\rangle\cong D_8\times C_2.
\]

Define involutory automorphisms of `H` (all fixing `z`) by

\[
R:a\mapsto az,\ u\mapsto u,\ v\mapsto v,
\]

\[
K:a\mapsto a,\ u\mapsto u,\ v\mapsto va,
\]

\[
L:a\mapsto a,\ u\mapsto uaz,\ v\mapsto v.
\]

Form \(N=H\rtimes\langle r\rangle\) using `R` and `r^2=1`.  Define maps on `N` by

\[
\widehat K|_H=K,\quad \widehat K(r)=ru,
\qquad
\widehat L|_H=L,\quad \widehat L(r)=rv.
\]

They are involutory automorphisms.  The compatibility checks are

\[
KR=\operatorname{Inn}(u)RK,qquad
LR=\operatorname{Inn}(v)RL.
\]

For the first identity the only nontrivial generator check is
`KR(v)=va=(vaz)^u`; for the second it is
`LR(u)=uaz=(ua)^v`.  All other generators are immediate.  Moreover
`widehat K^2(r)=(ru)u=r` and `widehat L^2(r)=(rv)v=r`.
The two automorphisms commute on `H`, and on `r` both composites give `ruva`;
for the second order one uses `vu=uvz`, with the `z` in `L(u)=uaz` cancelling
exactly.  Hence

\[
G_0=N\rtimes\langle k,l\rangle,qquad \langle k,l\rangle\cong C_2^2,
\]

is a group of order `16*2*4=128` satisfying precisely the displayed relations,
including `[u,l]=az`, `[r,k]=u`, and `[r,l]=v`.

Conversely, those relations make `H` normal of order at most 16 and make the
quotient by `H` a quotient of `C_2^3`, so the presented group has order at most
128.  The constructed model is a 128-element quotient of the presentation;
therefore the presentation and model are isomorphic.  This independently proves
pc consistency and exact order without running the claimant's script.

The quotient by `H` is abelian, while the commutators

\[
[r,k]=u,\quad [r,l]=v,\quad [v,k]=a,\quad [u,v]=z
\]

generate `H`; hence `G_0'=H` has order 16.  If a central element is written
`h r^epsilon k^eta l^theta`, its action on `A` first forces `epsilon=0`.  The
`aZ` components in the actions of `k` on `v` and `l` on `u` cannot be cancelled
by an inner automorphism of `H`, which only contributes `Z`; hence
`eta=theta=0`.  The element then lies in `Z(H)=A` and must be fixed by `R`, so it
lies in `<z>`.  Thus

\[
Z(G_0)=\langle z\rangle.
\]

Also `gamma_2=H`, `gamma_3=A`, `gamma_4=<z>`, and `gamma_5=1`, so the claimed
nilpotency class four follows.

Finally set `x=r`, `y=ruv` (the claimant's `ruv^{-1}` is the same because
`v^2=1`).  The element `r` centralizes `u,v`, so

\[
x^2=1,\qquad y^2=(uv)^2=z;
\]

their orders are two and four.  For `x`, the commutators with `k,l`, followed by
`[v,k]` and `[u,v]`, give all of `H`, so

\[
\langle x\rangle^{G_0}=\langle r,H\rangle.
\]

Direct collection gives

\[
[y,a]=z,\qquad [y,k]=uaz,\qquad [y,l]=va,
\]

and `[uaz,l]=az`.  These elements recover `a,z,u,v`, and then
`r=y(uv)^{-1}`.  Therefore

\[
\langle y\rangle^{G_0}=\langle r,H\rangle
=\langle x\rangle^{G_0}.
\]

This verifies the named pair and its nonconjugacy independently of the transcript.
The transcript's optional centralizer generating sets are unnecessary for the
claim and are not promoted by this verdict.

## Necessary versus sufficient checks

| check | logical force |
|---|---|
| reviewed least-counterexample core and order-128 R1/R2 split | necessary-case reduction only |
| action-trivial proof (1)--(3) | necessary restriction within R1/R2 |
| R1 innerness contradiction | sufficient to eliminate R1, conditional on the imported R1 data |
| cyclic square argument (4) | sufficient to eliminate every cyclic-centre R2 group, not merely the displayed tables |
| local Hall--Witt/polarization or pc consistency | necessary consistency checks; never sufficient for the source fibre hypothesis |
| one materialized `G0` | proves one local row exists and fails; not universal coverage by itself |
| corrected structural proof (5)--(15) | sufficient to eliminate every actual elementary-centre R2 group, independent of offsets |
| elimination of all order-128 regimes | excludes that order only; it does not imply the unrestricted source conclusion |

## Why this verdict

Every routed bounded conclusion now has a self-contained hand derivation.  The
only false step in the submission was the mechanism used to normalize the
elementary-centre outside lift.  The canonical residual-map argument both exposes
that error and repairs it without a new hypothesis, a computation, or a parameter
search.  The proof thereafter establishes exact equality of normal closures, not
merely equality modulo `A` or `H`.

## What is NOT established

- No group of order greater than 128 is treated.
- The active universal source statement is not proved, and no qualifying
  counterexample is supplied.
- This verdict does not re-audit the entire least-counterexample core or the
  earlier order-spectrum proof; it uses their routed order-128 R1/R2 data as the
  explicit hypothesis requested by Lead.
- The complete earlier single-commutator packing table and full central-offset
  polarization table were not needed and are not certified wholesale here.
- The claimant's GAP transcript is not independently replicated; the requested
  `G0` facts are instead established by the hand model above.

## What would upgrade it

Human review may promote this bounded hand result above `status/conjectured`.
Closing `12.15/normal-closure-fibres` still requires a valid argument excluding
all larger-order least-counterexample regimes (or a reconstructible qualifying
counterexample), followed by the remaining review circle and human decision.
