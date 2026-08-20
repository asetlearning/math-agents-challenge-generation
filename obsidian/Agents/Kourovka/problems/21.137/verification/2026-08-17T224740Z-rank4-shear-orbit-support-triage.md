---
title: "Triage — Kourovka 21.137 — rank-four H3 shear-orbit support"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For the frozen p=3 rank-four kernel/H3-quotient action and fixed labels qX=f2, qY=e2, every compatible shear class has a non-additively-closed factor-independent projected literal-cube support."
claimant: Problem-21.137-Counterexample
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

# Claim and scope lock

The rendered source on page 184 asks whether, for odd `p`, the literal set of
`p`-th powers in a finite `p`-group of exponent `p^2`, when a subgroup, must be
abelian.  The active revision-2 target matches that clause.  The general
powerful-subgroup question and the separate `p=2`, exponent-eight clause are
excluded.

The submitted claim is only a finite linear-algebra exclusion for one frozen
`p=3` automorphism/lift family.  Its computed object is an affine solution
space of shear triples, not a finite group and not the source target.

# Clause matrix

| source clause | active? | what the claim addresses | status |
|---|---:|---|---|
| General powerfulness question | no | nothing | excluded |
| Odd-prime, exponent-`p^2`, abelian literal-power-set question | yes | one frozen `p=3` pre-cohomology family only | pending bounded verification; universal target unanswered |
| `p=2`, exponent-eight square-set question | no | nothing | excluded |

`active_assignment_answered: pending` at triage; even a complete pass will
force `active_assignment_answered: no` because the claim is not universal.

# Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | independent reconstruction | triage status |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every odd prime and every qualifying finite same-prime group | not addressed universally |
| `21.137-odd-p-not-2` | admissibility | `p` is an odd prime | bounded family fixes `p=3`; pass only there |
| `21.137-odd-finite-p-group` | admissibility | `G` is a finite `p`-group | no witness group is submitted |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | not tested; pre-cohomology exclusion only |
| `21.137-odd-power-set-definition` | admissibility | the literal image `{g^p}`, not its generated subgroup | projected cosetwise norm union is the claimed observable; pending |
| `21.137-odd-power-set-subgroup` | admissibility | that literal set itself is a subgroup | claimed impossible throughout the frozen family by a projected closure defect; pending |
| `21.137-odd-P-abelian` | target conclusion | the literal power-set subgroup is abelian | not reached or established |

# Target versus witness

- Source target: all finite odd-prime groups satisfying the exact exponent and
  literal-power-set subgroup hypotheses.
- Active assignment: exactly the source's odd-prime clause.
- Computed witness: the affine `F3` solution space of three `3 x 4` shears for
  fixed `A,B,C,TX,TY,TZ,qX,qY`.
- Witness equals target: **false**.  The witness is a bounded parameter family
  used to exclude possible extensions; it is not a group.

# Subclaims

1. The frozen matrices obey the asserted order, commutator, symplectic, and
   label identities.
2. The lift constraints are exactly a `56 x 36` affine system of coefficient
   and augmented rank 17.
3. The twelve inner-lift and twelve kernel-shear translations are all
   admissible, all 24 displayed generators are present, and their span has rank
   18.
4. The complete residual discrete stabilizer consists of precisely the nine
   pairs `(D_a,U_d)`.
5. Its action on the one-dimensional affine quotient yields exactly three
   orbits covering all `3^19` solutions.
6. For every quotient word, the projected literal-cube fibre is
   `lambda_h + im(I+M_h+M_h^2)` independently of central factor coordinates.
7. All 27 words for each of the three representatives are complete and have
   the reported supports, including the common `e2+f2` closure failure.
8. The projected failure cannot be repaired by central cohomology.

# Clean-room derivations already completed

Before opening the claimant checker, I derived from the triple law

`(M,T,L)^-1=(M^-1,T^-1,-T^-1 L M^-1)`

and

`(M,T,L)^3=(M^3,T^3,T^2 L+T L M+L M^2)`.

Conjugation by a compatible kernel automorphism gives

`L_i -> U^-1(L_i D+T_i R-R M_i)`;

for `D=U=I` its translation is `T_i R-R M_i`.  For the submitted particular
solution I also multiplied the mixed word `h=(1,1,0)`: its triple is
`alphaX alphaY`, with shear `TX LY+LX B`, and the displayed cube-shear sum is
zero.  Hence its independently derived mixed-word label is
`lambda(1,1,0)=0000`, agreeing with the submitted table without using its code.

# Tools and methods inventory

- Available: GAP 4.12.1, Python 3.12.3, GNU `sha256sum` 9.4.
- Unavailable on the probe: Sage and Magma.
- Hand matrix algebra checks the transformation rules, equation count,
  stabilizer reduction, projected norm formula, and central-factor
  independence.  A pass proves those symbolic implications only.
- A separately written exact `F3` checker can reconstruct all residuals from
  the triple law, row-reduce the systems, enumerate the 27 quotient words and
  the at-most-three quotient representatives, and audit all support tables.  A
  pass can replicate the bounded finite certificate, but cannot prove the
  source's universal statement or the existence of any extension group.
- Direct inspection of the claimant checker is deferred until after the clean
  derivations above and an independent run; any later inspection will be
  documented separately.

# Hard limits and recommendation

No finite extension, cocycle, exponent-nine group, or universal odd-prime
argument is submitted or needed for this necessary projected gate.  Recommend
full hostile verification of the bounded affine certificate only.  If a
nontrivial independent computation is needed, freeze its checker and manifest,
request a Lead lease, and do not run before authorization.
