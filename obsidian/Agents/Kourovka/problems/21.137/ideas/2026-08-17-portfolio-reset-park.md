---
title: "MathExpert portfolio reset — 21.137 — no minute-300 certificate route"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: PORTFOLIO-RESET-PARK-2
direction: none
active_assignment_answered: no
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# Portfolio reset conclusion

Recommend `PARK_RECOMMENDED`: no new phase presently meets the requirement that
cumulative minute 300 end with a standalone mathematical certificate. This is a
scheduling recommendation only. It does not answer or retire revision 2.

The exact target remains: for arbitrary odd prime `p`, a finite same-`p` group
`G` of exponent exactly `p^2`, whose complete actual value set
`P={g^p:g in G}` is itself a subgroup, must have abelian `P`. The general
powerfulness question, `p=2`, exponent `8`, and every stopped method in Lead's
request remain excluded.

## Obstruction

The remaining obstruction is global compatibility. The reviewed
minimum-counterexample reduction encodes nonabelianity by a nonzero alternating
pairing `beta` and encodes actual-power coverage by cyclic norm supports. The
reviewed pointwise cover shows that the local action-power identities and
coverage can coexist formally with `beta != 0`; only the simultaneous
factor-system equations can still force a contradiction. No choice-free
consequence of those equations is currently isolated.

## Closest candidate and why it fails the gate

`GLOBAL-OBSTRUCTION-CLASS` would use normalized central-extension data
`(H,A,N,beta,L,ell,r,s)` satisfying the reviewed equations `(C1)--(C5)`.

- **Proposed observable:** a section-independent class whose pointwise value is
  `Omega(h,j)=beta(kappa(h),kappa(j))`, where the reviewed projected cover makes
  `kappa:H -> A/[A,H]` surjective. Vanishing of every such value would force
  `beta=0` on the covered quotient and would be directly target-facing.
- **Success certificate:** a line-by-line derivation from `(C1)--(C5)` that
  `Omega=0`, together with the exact surjectivity-to-`beta=0` implication.
- **Failure certificate:** one complete simultaneous associative extension datum
  with `beta != 0`, surjective `kappa`, and `Omega != 0`, or an exact
  section-change calculation showing that the proposed `Omega` is not an
  invariant consequence of `(C1)--(C5)`.
- **Would-be hard kill:** stop after 30 active minutes if `Omega` cannot be
  expressed choice-freely from `(C1)--(C5)`, reserving 10 minutes to package an
  exact identity or counterdatum.

This is not authorizable now. `H` and `A` are unbounded, there is no frozen
cochain complex or finite row set, and failure to derive `Omega=0` would be only
an unsuccessful manipulation, not the required failure certificate. Freezing a
complete counterdatum is itself the unresolved extension-construction problem.
Calling that phase 1 would merely rename the parked global-compatibility gap.

## Other modes assessed

1. **Center-branch transfer/root orbits.** General mathematical knowledge,
   unverified: one might try to eliminate `|Z(G)|=p^2` or `Z(G)=N` by transfer or
   orbit counting. The reviewed central-root calculation already supplies the
   cheap falsification: in the order-`p^2` center branch, multiplication by a
   central root fills every `N`-fibre automatically, so the available root-fibre
   observable is blind to `beta`. No replacement invariant is frozen.
2. **Jennings/restricted-Lie filtration.** General mathematical knowledge,
   unverified: nonzero `[G^p,G^p]` should force deep nonzero filtered data. The
   likely certificate is another class/order lower bound, while stronger
   reviewed bounds already exist; closure of the complete actual value set would
   not enter the proposed observable. This does not justify another increment.
3. **Structured construction.** Every currently concrete bounded family is on
   the stop list or belongs to the parked NS3 repair. No distinct associative
   finite object with an exact power-set observable is presently frozen.

## Smallest missing mathematical input and unpark gate

The smallest missing input is a choice-free lemma coupling the central cocycle
equation `(C4)` and cyclic carry equation `(C5)` to the alternating pairing,
stated strongly enough that surjective `kappa` forces `beta=0` (or stated with a
finite, exact counterdatum that refutes that implication). Reconsider the proof
direction only after such a lemma has an explicit formula and a bounded
line-by-line derivation. Reconsider construction only after a structurally new,
non-wreath, non-UT7 associative presentation and a finite exact row count are
already frozen.

Retain the scheduling truth estimate `0.52`; this reset produced no mathematical
evidence that warrants changing it.
