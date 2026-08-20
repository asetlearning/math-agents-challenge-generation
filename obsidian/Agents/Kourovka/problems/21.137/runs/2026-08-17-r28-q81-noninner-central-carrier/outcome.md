---
title: "Outcome — Q81 noninner central carrier"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
strategy: Q81-NONINNER-CENTRAL-CARRIER
outcome: STRATEGY_EXHAUSTED
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
active_assignment_answered: no
---

# Exact target

For an odd prime `p>2`, a finite same-`p` group `G` of exponent exactly `p^2`,
and the literal actual set `P={g^p:g in G}` rather than merely its generated
subgroup: if `P` itself is a subgroup, must it be abelian?  The `p=2`,
exponent-eight sibling is excluded.

# Outcome

`STRATEGY_EXHAUSTED` for the single frozen
`Q81-NONINNER-CENTRAL-CARRIER` datum only.

With the stipulated composition convention, the derived action
`C=alpha_Z=[alpha_X,alpha_Y]` satisfies

```text
[alpha_X,alpha_Z]
  = (I,I, v |-> omega(e1,v)s
                  +(omega(f1,v)-omega(e1,v))c).
```

Its value on `f1` has central displacement `s-c`, so this automorphism is not
inner.  Hence the proposed images fail the required relation `[x,z]=1` in
`Out(K)` and do not define an outer action of
`Q81=H_3(3) x C3` on `K`.

The exact derivation is in
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r28-q81-noninner-central-carrier/action-word-certificate.md`.

# What was ruled out

There is no group extension of `K` by `Q81` having exactly the four frozen
candidate automorphism data, irrespective of central factor-system choices.
No action/sign/shear/label variant, quotient catalogue, old `H3` central or
shear datum, `UT7`, holomorph, or wreath route was considered.

# What this does not establish

This is not a group, not a projected-support result, and not evidence that the
literal cube set in any group is or is not a subgroup.  It neither proves the
active assertion nor supplies a counterexample.  The unrestricted active
scope remains open, and `active_assignment_answered: no`.

# Computation and verification status

The certificate is a hand block-matrix derivation over `F3`.  No solver,
enumeration, or heavy command ran.  Accordingly there is no script hash,
stdout, factor digest, or cube-set digest, and no compute lease was requested.
The natural independent check is to reconstruct the four `7 x 7` block
matrices over `F3` and evaluate the displayed commutator word.

# Recommended next decision

Return the unused part of the authorized 55-minute increment to Lead and route
the action-word certificate to a fresh Validator.  This strategy's hard kill
does not authorize parking the universal scope or starting a replacement
strategy in this lane.
