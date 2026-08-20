---
title: "Post-shear portfolio — quotient-changing order-81 carrier"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/power-maps
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/outcome.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T222238Z-fixed-rank4-central-family.md
---

# Scope and evidence status

Scope `21.137/odd-prime-exponent-p2`, revision `2`: for an odd prime `p`, a
finite same-`p` group `G` of exponent exactly `p^2`, and the literal image
`P={g^p:g in G}`, decide whether the hypothesis that `P` itself is a subgroup
forces `P` to be abelian.  The `p=2` exponent-eight sibling, generated verbal
subgroups in place of the literal image, and groups of the wrong exponent are
excluded.

**Internally cited evidence.**  The fixed-central-family verification note
records a bounded exclusion for all 6,561 central rows in one frozen
rank-four-kernel/`H_3(3)` action-lift family.  The later shear outcome reports a
projected-support exclusion over `3^19` shears of that same frozen outer datum,
but that later report is treated here as provisional pending its current
Validator review.  Neither item answers the unrestricted scope.

**General mathematical knowledge, unverified.**  Every proposed mechanism and
every new matrix/action datum below is a conjectural work proposal.  In
particular, no compatibility, factor-system existence, power-image closure, or
target witness is asserted here.

# Actual obstruction

The construction obstruction is no longer a shortage of central correction
rows.  In the frozen rank-four/`H_3(3)` architecture, nonadditivity already
appears in the factor-independent projection of the literal cube image, so a
central factor or another shear cannot repair it.  A counterexample attempt
must change data visible before that projection: the quotient carrier, its
outer/center action, or the label orbit.

The proof obstruction is complementary.  Literal-image closure supplies a
root of each product of power values, but it supplies neither a canonical root
nor a multiplicative section.  The exhausted affine-cover, pair-root,
triple-root, and mark arguments show why support or equivariance alone does not
remove this fibre freedom.  A new proof observable must use actual fibre
multipities or a genuinely different prime-uniform identity.

# Ranked portfolio

## 1. `Q81-NONINNER-CENTRAL-CARRIER` — selected

**Mode:** structured counterexample construction; quotient-changing, not a
catalogue and not another fixed-`H_3` shear/central row.

**Idea (general mathematical knowledge, unverified).**  Keep the explicit
rank-four kernel

`K=3_+^(1+4) x C3^2`, with `V=<e1,e2,f1,f2>` and
`Z(K)=<c,s,t>`, but replace the quotient by the tightly frozen exponent-three
group

```text
Q81=<x,y,z,w | x^3=y^3=z^3=w^3=1,
                 [x,y]=z, z and w central>
   = H_3(3) x C3.
```

The fourth carrier is not inert.  With
`omega(e_i,f_j)=delta_ij`, freeze the following candidate automorphism data:

```text
tau_u(v)=v+omega(v,u)u,
T(c)=c, T(s)=s+c, T(t)=t+s,
alpha_X=(tau_e1,T, v |-> omega(e1,v)t),
alpha_Y=(tau_e2,T, v |-> omega(f1,v)t),
alpha_W=(I,I,       v |-> omega(e1,v)s),
alpha_Z=[alpha_X,alpha_Y].
```

Here `(M,T,L)` denotes `(v,z) |-> (Mv,Tz+Lv)`.  The formulas, signs,
commutator convention, and anticipated nonorthogonal cube-label orbit are
inputs to be reconstructed, not claims.  The point of `alpha_W` is that it is
a new central-shear outer class whose commutators with the other lifts may be
inner and nontrivial; mixed `w`-cosets can therefore alter the 81-coset
projected support instead of merely tripling the old one.

**Why it might work (general mathematical knowledge, unverified).**  The prior
failure is factor-independent but architecture-specific.  Enlarging the
nonabelian exponent-three quotient from 27 to 81 cosets and adding a
non-inner central carrier changes the set of affine norm translates before
any cocycle is chosen.  The frozen labels suggested by the displayed `L`
maps lie in a potentially nonisotropic orbit, so a support-pass group would
already retain the only projected mechanism needed for noncommuting cubes.

**Cheap falsifier.**  Derive the action words exactly.  Kill immediately if
they do not define the displayed `Q81` action in `Out(K)`, if the derived cube
labels are zero or mutually orthogonal, or if the complete projected literal
cube support over the 81 quotient cosets is not an `F3`-subspace.  Exhibit one
pair `a,b` with `a,b` in the support and `a+b` absent as the preferred kill
certificate.

**Most likely failure.**  The added `w`-cosets may only repeat the three old
support translates, or the proposed central shear may fail a `z`/`w`
commutation word before any factor exists.  Even a projected subspace is only
a necessary gate: central fibres can still destroy literal closure, as the
135-versus-729 fixed-family result illustrates.

**Cost.**  Exactly 55 active minutes, one frozen coordinate model, and at most
one leased heavy job (10-minute wall cap, 4 GB RAM).  No action variants,
shears, central-row family, cohomology classification, or quotient catalogue
are allowed.

## 2. `FIBRE-MULTIPLICITY-AFFINE-OBSTRUCTION`

**Mode:** proof/reduction, abstracting the repeated affine-support defects
without freezing an action.

**Idea (general mathematical knowledge, unverified).**  In a hypothetical
minimum counterexample, take the first elementary normal section `V` on which
the image of `[P,P]` is nonzero.  For every quotient root class `q`, retain not
only its affine projected support
`S_q=lambda_q+im(1+M_q+...+M_q^(p-1))`, but also the actual root multiplicity
on each point, weighted by the corresponding norm kernel.  Derive the section-
independent weighted incidence function

`mu(v)=sum_q #{roots in the q-fibre with projected pth power v}`.

Seek a universal consequence of literal-image subgroup closure saying that
`mu` is constant on cosets of a subspace containing the support radical.  A
nonzero alternating pairing on the image of `[P,P]` would then have to be
compatible with those equal fibres.

**Why it might work (general mathematical knowledge, unverified).**  The
formal affine cover and root-mark model could fake support, but neither
retained the multiplicities forced by an actual finite power map.  Weighted
fibres are therefore information not consumed by the exhausted routes.

**Cheap falsifier.**  If section change introduces an uncontrolled weight, or
if the exact double count yields only conjugacy invariance already present in
the root-mark certificate, kill the route.  A compatible abstract affine
system with subspace union, arbitrary nonconstant positive weights, and a
nonisotropic image is also a method-failure certificate.

**Most likely failure.**  Closure is a support condition and may impose no
useful equality on fibre sizes; deeper kernel factors may absorb every proposed
uniformity equation.  This is the main conceptual risk, so this route is not
the selected 55-minute increment.

**Cost.**  A 35--45 minute hand derivation of one weighted identity; no
computation.  It becomes executable only after the selected increment is
reviewed.

## 3. `R4-NEW-OUTER-CENTER-LABEL-ORBIT`

**Mode:** structured construction with the old kernel and quotient but a new
datum visible in projection.

**Idea (general mathematical knowledge, unverified).**  Retain
`K=3_+^(1+4) x C3^2` and `Q=H_3(3)`, but replace the frozen simultaneous outer
orbit by a common-long-root pair
`M_X=M_Y=tau_e1`, use opposite center chains `T` and `T^-1`, and prescribe the
candidate nonorthogonal label pair `e2,f2`.  Derive `alpha_Z` from the
commutator word.  Classify only this one exact outer/center/label tuple through
its factor-independent 27-coset support.  Do not vary shears or central
relators.

**Why it might work (general mathematical knowledge, unverified).**  A common
outer image line and opposite center chains belong to different raw action
data from the transverse fixed row, so their norm supports need not have the
same missing sum.

**Cheap falsifier.**  Kill on action-word incompatibility, isotropic derived
labels, or the first explicit additive defect in the 27-coset support.

**Most likely failure.**  The tuple may be conjugate to a previously excluded
orbit after inner lifts, or it may be just one more parameter point with no
coverage bridge.  That makes it lower value than changing the quotient.

**Cost.**  45 active minutes and no factor system unless the projected support
passes.  This comparison is not authorization to run it now.

## 4. `PRIME-UNIFORM-ROOTCOUNT-AUGMENTATION`

**Mode:** independent prime-uniform proof/reduction.

**Idea (general mathematical knowledge, unverified).**  For arbitrary odd
`p`, form the central group-algebra element

`R=sum_(g in G) g^p = sum_(a in P) r(a)a`,

where `r(a)` is the exact number of `p`th roots.  Work in `F_p G` and its
augmentation filtration.  Use `P` being a normal subgroup and exponent `p`
to ask whether the first noncentral graded component of `R` can coexist with
support exactly `P`.  The desired first lemma is a congruence forcing the
lowest nonzero image of `[P,P]` one filtration layer deeper; it must be derived
from cyclic orbit counting in the expansion, not from choosing product roots.

**Why it might work (general mathematical knowledge, unverified).**  This
observable uses all roots simultaneously, is independent of `p=3`, and avoids
the terminal-root gauge that killed the pair/triple-root routes.

**Cheap falsifier.**  Expand only through the first layer where `[P,P]` can
appear.  Kill if cyclic cancellation removes that term identically, if the
coefficient depends on root counts not controlled by support, or if the result
is exactly the already exhausted Zassenhaus pair ambiguity.

**Most likely failure.**  The support hypothesis may be too weak to constrain
the coefficients `r(a)` modulo `p`; the group-algebra identity may see only
the generated subgroup `G^p`, which would miss the literal-set condition.

**Cost.**  35--45 active minutes by hand, no heavy slot.  It is ranked fourth
because the target-facing bridge is less immediate than the finite carrier.

# Selected executable increment: exactly 55 active minutes

Select only `Q81-NONINNER-CENTRAL-CARRIER`.  Start from the displayed `K`,
`Q81`, and four candidate automorphisms; no search or alternate sign row is
authorized.  The phases and hard gates are:

1. **Minutes 0--12 — action certificate.**  Reconstruct all generator action
   words, including cubes, `[X,Y]Z^-1`, commutators with `Z`, and the three
   commutators with `W`.  Record every inner label.  **Kill** on any non-inner
   quotient relator, wrong order, or an orthogonal/zero cube-label pair.
2. **Minutes 12--25 — factor-independent literal-support gate.**  Enumerate the
   81 quotient coordinates only and derive, for each `q`,
   `lambda_q+im(I+M_q+M_q^2)` in `V`.  Take their exact union `Sigma`.
   **Kill** unless `Sigma` is an `F3`-subspace and its restricted symplectic
   rank is positive.  A size alone is not a pass.
3. **Minutes 25--40 — one canonical extension, not a family.**  Solve the full
   normalized central factor equations once and choose the lexicographically
   first solution in a fixed row-reduced order (all free coordinates zero).
   Construct the exact crossed product `K x Q81`.  **Kill** if no factor exists,
   associativity fails, the order is not `3^11`, or the exponent is not exactly
   nine.  Do not enumerate cohomology classes or central correction rows.
4. **Minutes 40--50 — target gates.**  Evaluate the cubes of all `3^11`
   elements.  Deduplicate the literal set, test exact Cayley closure inside the
   set, and only after closure exhibit a noncommuting pair.  **Success** requires
   every scope row: `p=3`, finite `3`-group, exact exponent nine, literal cube
   set itself a subgroup, and nonabelian literal cube subgroup.  Otherwise
   record an explicit closure outsider or the complete commutator-zero result.
5. **Minutes 50--55 — package and stop.**  Freeze inputs, code hash, stdout,
   factor digest, cube-set digest, and a constraint-and-conclusion matrix.
   Stop at minute 55 even if no target object has emerged.  If no exact group
   exists by minute 48, stop construction and use the remaining minutes only
   to package the earliest failed gate.

The success certificate is a reconstructible multiplication law for the one
`3^11` group, all 177,147 ninth-power checks with a nontrivial cube witness,
the complete literal-cube digest and cardinality, an exact closure certificate,
and an explicit pair of cube values with nonidentity commutator.  A failure
certificate is the earliest exact action word, missing support sum, factor
inconsistency, exponent witness, literal closure outsider, or all-cube
commutator certificate.  A heavy job requires a Lead lease; proposed cap is
10 wall-clock minutes and 4 GB RAM.

# Ledger plan through the mandatory minute 765

The official starting ledger is `675/765`.  This recommendation supplies one
55-minute increment, so a full run ends at minute `730` and leaves exactly 35
mandatory active minutes.

- A target-equal claim is the only early-stop exception: route it immediately
  through a fresh Validator and do not infer any passed row from projected
  support alone.
- If the 55-minute stop is `STRATEGY_LIVE` because `Sigma` passed and only the
  canonical factor or exact cube test remains, spend the remaining 35 minutes
  after review on that same single group.  Do not enlarge the action, factor,
  or quotient family.
- If the full 55-minute run kills or completes without a witness, use the final
  35 minutes on exactly the first weighted identity of
  `FIBRE-MULTIPLICITY-AFFINE-OBSTRUCTION`: section covariance, one double count,
  and its explicit kill certificate.  It is a proof-direction reset, not a
  repair of the killed carrier.
- If a hard kill stops the selected run after only `t<55` charged minutes, the
  live ledger is `675+t`, not 730.  Route the certificate, allocate 35 minutes
  to the weighted-fibre identity after review, and return all additional
  remainder `55-t` to Lead for a fresh ultra route choice among ranks 3 and 4
  or another genuinely new architecture.  No parking recommendation is made
  before the official ledger reaches 765.

This plan preserves the distinction between an exhausted strategy and the
still-open unrestricted source scope.
