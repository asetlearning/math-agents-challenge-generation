---
title: "Working log — R4 new outer/center/label orbit"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: R4-NEW-OUTER-CENTER-LABEL-ORBIT
direction: counterexample
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

## 2026-08-17T23:38:36Z — work start

Official cumulative active ledger: `703` minutes.  Exact scope rechecked:
odd prime, finite same-prime group, exponent exactly `p^2`, literal power set
itself a subgroup, ask abelianity; the `p=2` sibling is excluded.  Started only
the Lead-authorized frozen `p=3` common-root/opposite-center datum.

## 2026-08-17T23:39:00Z — exact action gate

Froze the canonical direct label representatives
`LX=omega(e2,-)t` and `LY=omega(f2,-)t`; no other shear was inspected.
Hand triple multiplication gave
`Z_L=(omega(e2,-)+omega(f2,-))s-omega(e2,-)c`, with
`X^3=J_e2`, `Y^3=J_f2`, `Z^3=1`,
`[X,Z]=J_(e2+f2)`, and `[Y,Z]=J_(-e2-f2)`.
All `H_3(3)` words are inner.  The prescribed labels are nonorthogonal.

The orbit separator is `rank(M_z-I)`: zero for the new tuple versus one for
the exhausted transverse row.  This survives inner lift changes, center
shears, simultaneous kernel conjugacy, and inversion of the central quotient
generator.

## 2026-08-17T23:40:00Z — exact fixed checker

Ran once:

```text
python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/scratch/check_fixed_r4_tuple.py
```

Observed exit code `0`, wall time `0.181562254` seconds, chunk `a6d31a`.
After this invocation, a Lead checkpoint required a lease for the frozen
checker.  The probe is therefore quarantined and not used as evidence.  Its
stdout remains in `checker-output.md` for audit, and the frozen hash and an
exact `timeout 5s` command were sent to Lead in a lease request.

## 2026-08-17T23:41:00Z — projected-support hard kill

All 27 norm images are zero.  Their exact singleton union has size seven:
`{0,+/-e2,+/-f2,+/-(e2-f2)}`.  Its span has symplectic rank two, but the union
is not a subspace: `e2,f2` occur and `e2+f2` does not.  The Lead kill criterion
fires by hand before factor systems or groups; final packaging waits for the
requested leased reproduction.

## 2026-08-17T23:49:00Z — leased reproduction and release

Lead granted slot 1 for exactly one invocation of the hash-matched frozen
checker.  Ran the authorized command once:

```text
timeout 5s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/scratch/check_fixed_r4_tuple.py
```

Observed exit code `0`, runner chunk `2dfd31`, wall time `0.198841454`
seconds.  The fresh stdout in `leased-output.md` reproduces every hand action
word, the orbit separator, all 27 supports, and the outsider
`0001+0100->0101`.  Reported slot 1 released at `23:50:10Z`.

## 2026-08-17T23:50:10Z — stop and package

Final outcome: `STRATEGY_EXHAUSTED` for the single frozen representative.
Official charge is 14 active minutes, cumulative `703--717`; waiting for the
lease is excluded.  Return 31 unused minutes to Lead and enter
`awaiting_lead`.  The universal odd-prime source scope remains unanswered;
`active_assignment_answered: no`.
