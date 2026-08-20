---
title: "R4-NEW-OUTER-CENTER-LABEL-ORBIT — projected-support hard kill"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: R4-NEW-OUTER-CENTER-LABEL-ORBIT
direction: counterexample
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/conjectured]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/action-word-certificate.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/manifest.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/checker-output.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/leased-output.md
---

# Outcome

`STRATEGY_EXHAUSTED` for exactly the frozen canonical
`R4-NEW-OUTER-CENTER-LABEL-ORBIT` representative.

The tuple passes every `H_3(3)` action word modulo inner automorphisms.  Its
ordered cube labels are `e2,f2`, with `omega(e2,f2)=1`.  It is genuinely
outside the exhausted transverse orbit because the invariant
`rank(M_z-I)` is `0` here and `1` there.

The hand-computed complete factor-independent 27-coset literal-cube projection
then hard-kills the route.  Every norm image is zero and the exact union is

`Sigma={0,+/-e2,+/-f2,+/-(e2-f2)}`.

Thus `|Sigma|=7`; although its span has symplectic rank two, `Sigma` is not an
`F3`-subspace.  Explicitly `e2,f2 in Sigma` while
`e2+f2 notin Sigma`.  No central factor system can repair a defect already
visible in this quotient projection.

# Constraint-and-conclusion matrix

| constraint_id | role | required condition | result in this run |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd `p,G` | not universal; one `p=3` action representative only |
| `21.137-odd-p-not-2` | admissibility | odd prime | pass for parameter `p=3` |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | no group constructed; conditional pre-extension exclusion only |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | not tested because the projected subgroup gate already fails |
| `21.137-odd-power-set-definition` | admissibility | literal actual power set | pass for the full projected literal support over all 27 quotient cosets; no generated closure used |
| `21.137-odd-power-set-subgroup` | admissibility | literal set itself a subgroup | impossible for this representative: its image `Sigma` is not additively closed |
| `21.137-odd-P-abelian` | target conclusion | literal-power subgroup abelian | not reached and not established |

# What was ruled out

Any central factor system realizing this exact frozen automorphism tuple is
incapable of producing a literal cube-set subgroup, because a subgroup's image
in `V` would be a subspace.  No claim is made about another label-realizing
shear, action, quotient, kernel, or odd prime.

# What was not opened

No factor system, cohomology, central-row family, finite group, exponent-nine
test, or group enumeration.  The exact source scope remains unanswered and
`active_assignment_answered: no`.

The earlier subsecond checker probe remains quarantined.  The fresh exact
once-only leased invocation independently reproduces the hand table and is the
sole computational evidence.
