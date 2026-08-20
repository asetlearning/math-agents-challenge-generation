---
title: "Kourovka 21.137 — post-MIN9 unrestricted strategy review"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
outcome: PARK_RECOMMENDED
active_assignment_answered: no
author: operator
tags: [agent/math-expert, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/conjectured]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T121228Z__Problem-21.137__PARTIAL_RESULT__min9-action-family-empty.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/findings.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T120743Z-nine-lift-histogram.md
---

# Post-MIN9 unrestricted strategy review

## Scope and evidence boundary

`scope_id`: `21.137/odd-prime-exponent-p2`  
`assignment_revision`: `2`

Exact target: for every odd prime `p` and every finite `p`-group `G` of exact
exponent `p^2`, if the *actual value set* `P={g^p:g in G}` is a subgroup, decide
whether `P` must be abelian. The general powerfulness clause, every `p=2`
example, and the exponent-8 sibling are excluded.

The submitted zero-survivor result is not promoted here. I use it only as the
conditional report that 2,398 prefusion action classes in the proposed `p=3`,
order-`3^9` equality model failed a necessary capacity gate. Even if Validator
upholds the whole dependency chain, it would raise only a direct `p=3` finite
floor. It would not answer this scope.

No web search or solution-bearing history was used. Statements attributed to the
four linked records report what those records say, not a new certification.
Every new mechanism or mathematical judgement below is **General mathematical
knowledge, unverified** and needs Validator reconstruction before reliance.

`active_assignment_answered: no`.

## Actual obstruction

This is now a **coherence-versus-observable mismatch**. Root actions give sharp
factor-independent necessary equations, but they do not encode associativity of
an extension or equality with the complete actual power set. Conversely, direct
proof rewrites of closure introduce an existentially chosen root of each product;
the reviewed affine and pair-transgression attempts report that the resulting
deep carry depends on the section. A larger finite-order screen can therefore
produce another floor, while a graded proof can silently discard the datum that
made closure meaningful.

## Route 1 — `PF-JORDAN-CAPACITY`

### Idea and exact observable

General mathematical knowledge, unverified: in the conditional
quotient-minimal normal form reported in the supplied findings, model the
class-two exponent-`p` group `P` on its underlying `F_p`-space `E`, put
`C=P'` and `V=P/Z(P)`, and let `A_x` be conjugation by a root `x` of
`a=x^p`. With `N_x=A_x-I`, the exact root-action rows are

`N_x^p=D_a` and `N_x(a)=0`,

where `D_a=Inn(a)-I`. A `p`-group action admits a common invariant flag. Record
for each action element the full rank tuple

`(rank N_x, rank N_x^2, ..., rank N_x^p)`,

the flag positions of `Z(P)` and `C`, and its unique/nonunique label set

`L(N_x)={abar in V : N_x^p=D_abar and N_x(abar)=0}`.

The target-relevant observable is the **label deficit**

`delta(A)=dim V-dim span(union_x L(N_x))`,

together with the root-fibre capacity for every nonzero label. A proof-strength
outcome would require `delta(A)>0`, or a strict capacity deficit, for every
compatible `p`-subgroup `A` at every odd `p`. Merely obtaining the expected
`J_(p+1)` block or a lower bound on `dim Z(P)` is only a size bound.

### Certificates, cost, and hard kill

- Success certificate: a section-free block calculation deriving
  `delta(A)>0` (or a uniform capacity shortfall) for arbitrary odd `p`, with all
  fixed-space and inner-lift rows included.
- Failure certificate: one explicit common-flag root-action system with
  `delta(A)=0`, or a derivation that stops at the already anticipated
  `J_(p+1)`/large-centre lower bound without an order-independent contradiction.
- Cost: 45 active minutes, hand linear algebra; no heavy slot. A `p=3`
  reweighting of the existing census would cost less, but would be only another
  finite floor and is not the purpose of this route.
- Hard kill: stop at 30 minutes if the flag supplies only a dimension bound;
  absolute stop at 45 without a proper-label-subspace lemma.

Most likely failure: enlarging `Z(P)` supplies room for the long unipotent chains,
and increasing `|G/P|` relaxes rather than tightens the capacity inequality. Thus
the order-`3^9` obstruction has no evident monotone path to arbitrary order or
arbitrary odd `p`.

## Route 2 — `O310-EQUIVARIANT-LABEL`

### Idea and exact observable

Do not enumerate descendants or central factor systems. First derive, rather than
assume, the complete list of possible pairs `(P,R=G/P)` at order `3^10` from the
reviewed minimal-counterexample inequalities. Only if that list is finite, inspect
homomorphisms `rho:R->Out(P)`, not merely image subgroups. For every `r in R`,
the nine-lift block equation gives a label set `ell(r)` and a central-fibre supply.
The new observable is the **equivariant labelled quotient profile**:

1. `ell(s^-1 r s)=rho(s)^-1 ell(r)` for every `r,s in R`;
2. the max-flow supply to every noncentral label, with the exact central-fibre
   demand inherited only after `P` is frozen;
3. the kernel size and quotient-relation multiplicities, so two abstractly equal
   image subgroups with different maps from `R` are not conflated.

This is sharper than rerunning the MIN9 subgroup histogram because it keeps the
quotient-element correlations that a later extension would have to respect.

### Certificates, cost, and hard kill

- Success certificate: a complete finite manifest of all derived `(P,R,rho)`
  rows and, for each, one failed equivariance or exact max-flow row; zero survivors
  would exclude only the stated order-`3^10` layer.
- Failure certificate: one explicit label-complete `(P,R,rho,ell)` row. Such a
  row is not a group and not a counterexample; it is the hard stop for this
  no-factor-system strategy.
- Cost: 19 minutes to freeze the structural list, then at most 60 further active
  minutes and one bounded heavy job only if the list and manifest are exact.
- Hard kill: stop after the initial 19 minutes if order `3^10` does not force a
  short finite list. If any equivariant label-complete row survives, do not open
  cocycles or descendants under this strategy.

Most likely failure: the extra quotient factor makes capacity less restrictive,
and a surviving action profile still says nothing about extension associativity,
exact exponent, or the complete actual cube set. Even a zero-survivor result would
remain `p=3`-only. This is therefore poor marginal use of another hour.

## Route 3 — `ZASSENHAUS-DEPTH-PUSH`

### Idea and exact observable

General mathematical knowledge, unverified: use the Zassenhaus filtration
`D_n(G)` and choose the first degree in which the nontrivial minimal normal
commutator `C=P'` has a nonzero symbol. Translate

`x^p y^p=z^p`

for an existential product root `z` into the associated restricted Lie algebra.
The exact observable is not merely the leading restricted `p`-map. It is the
residual class

`rho_n = symbol([x^p,y^p]) mod A_n`,

where `A_n` is explicitly generated by every permitted change of the root `z`,
section, and lift through degree `n`. The hoped-for depth push is that closure
forces `rho_n=0` and hence `C<=D_(n+1)`; iteration would contradict separation of
the finite filtration.

### Certificates, cost, and hard kill

- Success certificate: a line-by-line, prime-uniform identity showing that the
  ambiguity subspace `A_n` cannot contain the commutator symbol, or that the
  symbol is forced one level deeper for arbitrary `n`.
- Failure certificate: an explicit filtered/restricted-Lie formal model with
  nonzero commutator symbol satisfying all leading closure equations, or a
  calculation showing `A_n` already fills the relevant component.
- Cost: 60 active minutes, no heavy slot.
- Hard kill: at 30 minutes if the product-root symbol cannot be made
  section-independent; absolute stop at 60 without one filtration-depth push.

Most likely failure: the associated graded object forgets precisely the deep carry
and root-choice data. The supplied records report this failure mode in the affine
cover and CPTR routes, so changing filtrations without a new invariance lemma is
not a genuinely live proof mechanism beyond the reviewed low-class result.

## Route 4 — `ROOT-FIBRE-MARKS`

### Representation change and exact observable

General mathematical knowledge, unverified: regard the power map
`pi:G->P`, `pi(x)=x^p`, as a conjugation-equivariant map of finite `G`-sets.
For every subgroup `H` relevant to the minimal normal form and every `a in P`,
record the mark

`m_H(a)=|{x in C_G(H):x^p=a}|`.

Surjectivity onto the actual subgroup requires `m_1(a)>0` for every `a`, while
conjugation, orbit-stabilizer divisibilities, restriction to centralizers, and
Möbius inversion impose integral congruences among the marks. The exact test is
integer feasibility of the complete mark system after the nonabelian class-two
`P` orbit structure is inserted.

### Certificates, cost, and hard kill

- Success certificate: an explicit integer linear combination of the mark
  equalities, inequalities, and divisibilities yielding an impossible congruence
  whenever `P'!=1`; this would be prime-uniform and independent of a section.
- Failure certificate: a nonnegative integral formal mark vector satisfying every
  imposed row for the smallest abstract nonabelian `P`. It need not arise from a
  group; it shows that marks are too coarse.
- Cost: 45 active minutes for the symbolic system and hand congruence audit; a
  small exact feasibility check is justified only after all rows are frozen.
- Hard kill: stop at 30 minutes if multiplication in `P` never enters the mark
  equations or if the formal relaxation is feasible; absolute stop at 45.

Most likely failure: Burnside marks see equivariance and divisibility but not the
multiplication law connecting different root fibres. A formal equivariant
surjection can therefore survive even when no exponent-`p^2` group realizes it.

## Selection

**Recommendation: `PARK_RECOMMENDED`. Do not spend the remaining 19 minutes and
do not request another one-hour extension on the current evidence.**

The four modes have distinct observables, but none currently has both a live
mechanism and a target-level certificate:

- Route 1 is likely to return only a prime-uniform size bound; at larger order its
  capacity gate weakens.
- Route 2 is a bounded `p=3` floor computation whose first survivor immediately
  reopens the unbounded coherence stage.
- Route 3 lacks a section-independent residual and risks repeating the reviewed
  deep-carry failure.
- Route 4 deliberately forgets multiplication and is likely feasible as a formal
  `G`-set problem.

The unvalidated zero-survivor report does not improve any of those marginal
mechanisms; promotion would change the finite floor, not this recommendation.
No `p=2`, exponent-8, wreath-shaped, or filename-derived route was considered,
and no `p=3`-only computation is being mistaken for evidence on arbitrary odd
primes.

Reopen only on one of four concrete triggers: a uniform proper-subspace lemma for
root labels; a fully frozen order-`3^10` quotient map with a binary obstruction
before factor systems; a filtration lemma making root-choice ambiguity one degree
deeper; or a non-wreath, prime-parametric construction with a closed formula for
the complete actual `p`th-power set. Until then the scope remains unanswered and
the better portfolio decision is to move the solver lane elsewhere.
