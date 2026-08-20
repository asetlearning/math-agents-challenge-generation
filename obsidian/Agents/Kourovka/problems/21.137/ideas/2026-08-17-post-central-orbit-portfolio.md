---
title: "Kourovka 21.137 — post-central portfolio and shear-orbit support gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
strategy_id: RANK4-H3-SHEAR-ORBIT-SUPPORT
direction: counterexample
active_assignment_answered: no
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - topic/power-maps
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r25-rank4-nonsplit-h3/lift-gate.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/fixed-family-outcome.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T220224Z-fixed-rank4-central-family-triage.md
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-post-cptr-pairing-cover-audit.md
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-post-min9-strategy-review.md
---

# Scope and evidence boundary

`scope_id`: `21.137/odd-prime-exponent-p2`  
`assignment_revision`: `2`

Exact target: for every odd prime `p` and finite same-`p` group `G` of exact
exponent `p^2`, if the literal value set

`P={g^p:g in G}`

is itself a subgroup, decide whether `P` must be abelian. The general
powerfulness clause, every `p=2` example, the exponent-eight sibling, and a
generated-power subgroup substituted for the literal set are excluded.

The submitted rank-four fixed-family outcome remains provisional while
Validator reconstructs it. I use its `135` versus `729` profile only as
motivation and as a proposed observable, not as a promoted fact. The selected
increment begins by independently reconstructing its own fixed matrices and
the earlier 56-equation lift system; it does not assume the submitted
`6,561`-row or `27`-class conclusions.

No web, solution-bearing history, wreath material, `p=2` material, experiment,
or computation was used here. Every new mechanism below is **general
mathematical knowledge, unverified** and needs independent checking before
reliance.

# Obstruction and direction assessment

The current obstruction is now sharply localized. One fixed automorphism lift
admits nonorthogonal cube labels and complete nonsplit extensions, but the
submitted literal cube image has a non-`3` cardinality and fails closure for
every central cohomology class. Varying central relators again cannot change
that boundary. The first untested datum is the automorphism lift/shear orbit
itself; a different quotient or a genuinely global proof invariant comes only
after that.

For the truth of the source assertion I retain the official near-even estimate
`0.52` in favor of truth pending Validator. The repeated conjunction failure
"noncommuting values but nonclosed image" weakly favors a theorem, but the
existence of a consistent nonsplit lift with two nonorthogonal labels keeps a
counterexample competitive. For the **next 55 active minutes**, the
counterexample-side pre-cohomology screen has higher expected certifiable value
than another proof manipulation: it has a finite frozen object and a
factor-independent target obstruction.

# Ranked genuinely different routes

## 1. `RANK4-H3-SHEAR-ORBIT-SUPPORT` — selected

Keep `p=3`, `K=3_+^(1+4) x C3^2`, quotient `H_3(3)`, the fixed symplectic
outer matrices `A,B,C`, the displayed center matrices `TX,TY,TZ`, and labels
`qX=f2`, `qY=e2`. Replace the single displayed shear triple by the **complete
19-dimensional affine solution space** of the 56 lift equations. Classify its
nonconjugate/support-relevant lift orbits before any central cochain is opened.

For a lift `L` and `h in H_3(3)`, let `M_h` be its fixed action on
`V=K/Z(K)`, and let `lambda_L(h)` be the unique inner label of
`alpha_h^3`. The factor-independent projected cube support from the root coset
`h` is proposed to be

`F_h(L)=lambda_L(h)+im(I+M_h+M_h^2) subset V`,

and the complete projected support is

`Sigma(L)=union_h F_h(L)`.

If the literal cube set were a subgroup, its image in `V` would have to be an
`F3`-subspace. If that subgroup were nonabelian, the symplectic form restricted
to this image would have to be nonzero. Thus the exact pre-cohomology gates are

1. `Sigma(L)` is a linear subspace;
2. `rank(omega|Sigma(L))>0`.

Why ranked first: it changes exactly the datum left open by the submitted
family exhaustion, yet avoids the 2,028-variable central cochain system. It is
not a catalogue of groups: the observable is an affine signature obtained
from 27 four-dimensional norm images.

Falsification: one orbit with subspace-shaped, nonisotropic `Sigma(L)` kills
this obstruction and becomes a principled input for one later cohomology row.
The likely failure is that the full conjugacy/lift-change quotient is not small
enough to classify in one increment, or that many support-pass orbits survive.

Cost: exactly 55 active minutes; small exact linear algebra and, only after a
frozen manifest, a bounded bespoke orbit checker. No group construction and no
central cohomology in this increment.

## 2. `FIBRE-UNIFORMITY-135` — proof direction

Abstract the submitted `135` versus `729` phenomenon through the projection
`pi:K->V`. For an actual cube set `S`, define

`d(v)=|S intersect pi^-1(v)|`.

General mathematical knowledge, unverified: if `S` is a subgroup, then
`pi(S)` is a subspace and every nonempty fibre is one coset of `S intersect
Z(K)`; hence all nonempty `d(v)` are the same `3`-power. The fresh task would
derive `d(v)` symbolically from the action and factor equations and ask whether
two nonorthogonal cube labels force either a nonconstant fibre profile or a
non-`3` factor, independently of the frozen shear and central cochain. This
would turn the observed `135=27*5` into an actual obstruction rather than a
cardinality report.

Why ranked second: it could explain an entire class of near misses and points
toward a theorem. It is global subgroup-fibre uniformity, not the exhausted
pointwise affine cover, pair-root, triple-root, or mark observable.

Falsification and hard kill: stop by 30 minutes if the factor `5` depends on
the exact frozen lift/cochain, or if the only conclusion is the already-known
Lagrange check `135` is not a `3`-power. Success would require a displayed
formula for all `d(v)` in a lift-independent structural family. Cost at most
45 hand minutes, no heavy slot.

Most likely failure: central cocycles can change the fibre union while leaving
the projected support fixed, so no lift-independent `d(v)` formula may exist.

## 3. `RANK4-Q81-CARRIER` — different exponent-three quotient

Replace the order-27 quotient by the explicitly frozen nonabelian exponent-three
group

`Q81=<x,y,z,w | x^3=y^3=z^3=w^3=1, [x,y]=z, z,w central>`

`   ~= H_3(3) x C3`.

Keep the rank-four kernel. A sharply bounded first action row sends
`x,y,z,w` to the outer classes of `alphaX,alphaY,alphaZ,alphaZ`, respectively;
the extra central quotient direction therefore has a fixed action but may
carry an independent nonsplit lift. Before any factor system, compute all 81
projected norm-label supports and require their union to be a nonisotropic
subspace. This is different from the old NS3 row: that row used kernel
`H_3(3) x C3^2` and failed one misaligned representative equation before a
group existed, whereas this row uses the rank-four kernel and a specified
order-81 quotient map.

Falsification: kill immediately if the four lift representatives violate a
single action relation, or if the extra generator merely duplicates the
order-27 projected support without adding a possible central-fibre degree of
freedom. A success certificate is one exact 81-row affine-support table and a
nonorthogonal pair; it is not yet a group. Cost: 15 minutes for the action gate
and at most 45 further minutes only after a finite cohomology dimension is
frozen.

Most likely failure: the redundant outer action enlarges cohomology without
repairing the projected closure defect, recreating a larger compatibility
problem.

## 4. `POWER-MEASURE-FOURIER` — independent route

In the reviewed hypothetical minimal quotient, put

`m(a)=|{x in G:x^p=a}|` for `a in P`

and form the central group-algebra element

`W=sum_(a in P) m(a)a = sum_(x in G) x^p in Z(ZP)`.

For each irreducible character of the class-two exponent-`p` group `P` lying
over a nontrivial character of `P'`, the exact observable is the scalar Fourier
coefficient

`mu_chi=(1/chi(1))*sum_(x in G) chi(x^p)`.

The route asks whether exponent `p^2`, root-orbit divisibility, and full support
`m(a)>0` impose a congruence on these nonabelian Fourier coefficients that is
impossible when `P'!=1`. Unlike root-fibre marks, this observable includes the
multiplication law through non-linear irreducible representations.

Falsification: a nonnegative full-support class function on the smallest
reviewed nonabelian `P` satisfying all derived orbit divisibilities and Fourier
scalar rows kills the representation. Hard kill at 25 minutes if the only rows
are equivalent to conjugacy/mark divisibility or if no identity links
`mu_chi` to exponent `p^2`. Absolute cost 40 hand minutes, no heavy slot.

Most likely failure: support without uniform fibres allows enough freedom in
`m` to satisfy every character constraint. This ranks last because no live
indicator identity is currently isolated.

# Sole selected increment

Authorize exactly one fresh ultra solver increment:

`RANK4-H3-SHEAR-ORBIT-SUPPORT`, **55 active minutes maximum**.

This is the first post-validation pivot only. Starting from cumulative minute
`648`, it can reach at most minute `703`; unless the full source scope is solved,
the human minimum still requires at least `62` further active minutes through
minute `765`. A hard kill or early certificate returns unused minutes to Lead
for a fresh reviewed route; it does not authorize parking.

## Prerequisites and frozen object

1. Treat the submitted `6,561`/`27`/`135`/`729` outcome as provisional until
   Validator reports. It is motivation, never an input to the new certificate.
2. Independently re-enter `K`, `H_3(3)`, `A,B,C`, `TX,TY,TZ`, `qX=f2`, and
   `qY=e2`, with the fixed commutator/right-action conventions.
3. Reconstruct the complete 56-by-36 affine shear system and require exact
   coefficient and augmented rank `17`, hence affine dimension `19`. A mismatch
   stops the route and is reported; it is not patched by changing data.
4. Freeze `mathcal L` to **all** solutions of that one system. No alternate
   center action, label pair, quotient, central relator, factor system, group
   enumeration, UT7 row, holomorph, affine cover, root pair/triple, or `p=2`
   object enters this increment.

## Orbit and observable contract

Derive explicitly the affine action on `mathcal L` generated by:

- admissible changes of the three quotient-generator lifts by inner
  automorphisms that preserve the frozen label row; and
- simultaneous kernel conjugations in the stabilizer of the frozen
  `(A,B,C,TX,TY,TZ,qX,qY)` data.

No two shear rows may be identified without a displayed transformation, and
the orbit-size sum must equal `3^19`. Alongside the full orbit quotient, form
the support-signature map

`Phi(L)=(lambda_L(h)+W_h)_(h in H_3(3))`,

where `W_h=im(I+M_h+M_h^2)`. Row-reduce the image and kernel of `Phi` before
enumerating representatives; rows in `ker Phi` have identical projected
supports and are batched only for this necessary gate, not declared isomorphic.

For every genuine orbit representative, record the 27 affine supports,
`|Sigma|`, whether `Sigma` is an `F3`-subspace, and the rank of
`omega|Sigma`.

## Timebox and hard kills

- minutes `0--10`: independent matrix and 56-equation reconstruction;
- minutes `10--22`: derive the exact lift-change/stabilizer action and prove
  the orbit equivalence used;
- minutes `22--38`: compute the affine signature quotient and the complete
  orbit/support manifest;
- minutes `38--45`: replay canonical representatives and finish the bounded
  certificate;
- minutes `45--55`: package only; no new research.

Hard kill immediately if the matrix reconstruction differs, if `alpha_h^3`
is not inner for a retained row, or if `Phi` is not invariant under a claimed
support equivalence. Kill at minute 22 if orbit completeness is not explicit.
Also kill before categorical enumeration if the reduced signature image has
dimension greater than eight or the exact representative count exceeds 729;
that returns a dimension certificate and prevents a disguised large catalogue.
Absolute research stop is minute 45.

## Certificates and interpretation

Success for this increment is either:

1. a complete orbit manifest showing that every shear orbit has non-subspace
   or isotropic projected cube support, which exhausts this fixed-center
   automorphism-lift family before cohomology; or
2. one or more explicitly listed nonconjugate support-pass orbits, each with a
   27-row support table and nonorthogonal pair, which justifies at most one
   later separately authorized cohomology experiment.

The second outcome is not a group and not a candidate counterexample. The
first is a bounded family exclusion, not an answer to the universal source
scope. In every outcome `active_assignment_answered: no` unless a later exact
finite group passes all seven canonical rows through the full review circle.

# Recommendation

Select route 1. It is the nearest untested structural boundary, directly tests
a necessary image-subgroup condition, and cannot accidentally reopen the
exhausted 18 central-relator rows. Keep routes 2--4 as backups only; authorize
none of them in parallel in this scope lane. After this one increment, preserve
the active scope and choose the next evidence-gated increment needed to reach
cumulative minute `765` unless the source target has actually been answered.
