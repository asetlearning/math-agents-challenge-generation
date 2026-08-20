---
title: "Frozen manifest — R4 common-root/opposite-center tuple"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: R4-NEW-OUTER-CENTER-LABEL-ORBIT
direction: counterexample
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

# Scope and evidence boundary

This run uses only `p=3`,
`K=3_+^(1+4) x C3^2`, `Q=H_3(3)`, the common long-root matrix
`M_X=M_Y=tau_e1`, opposite center chains `T,T^-1`, and the ordered
cube-label pair `(q_X,q_Y)=(e2,f2)`.  It derives `alpha_Z` as the exact
commutator.  It does not vary a lift, sign, shear, label, quotient, kernel, or
factor row.

The computation is only an automorphism-action and factor-independent
projected-support gate.  It does not construct a factor system, extension
group, exponent-nine object, or counterexample.

# Frozen coordinates

All arithmetic is over `F3`.  Column coordinates on
`V=<e1,e2,f1,f2>` and `Z=<c,s,t>` use

`omega(v,w)=v_e1 w_f1+v_e2 w_f2-v_f1 w_e1-v_f2 w_e2`.

For triples `(M,T,L):(v,z) |-> (Mv,Tz+Lv)`, composition and commutator are

```text
(M,T,L)(M',T',L')=(MM',TT',T L'+L M'),
[g,h]=g^-1 h^-1 g h.
```

The exact tuple is

```text
M=tau_e1=1020/0100/0010/0001,
T=110/011/001,                  T^-1=121/012/001,
a(v)=omega(e2,v),               b(v)=omega(f2,v),
LX=a t=0000/0000/0001,          LY=b t=0000/0000/0200,
alpha_X=(M,T,LX),               alpha_Y=(M,T^-1,LY),
alpha_Z=[alpha_X,alpha_Y].
```

The last-center-coordinate representatives `LX=a t` and `LY=b t` are the
canonical direct realizations of the prescribed ordered labels because
`aM=a`, `bM=b`, and both cyclic center norms send `t` to `c`.  No other
label-realizing shear is inspected.

# Frozen checker

Checker:
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/scratch/check_fixed_r4_tuple.py`

SHA-256:
`4d731654c33837df031fc6eeb45cd6d7b97dbe641a0fdc87b84d466eb4e5dc0e`.

Requested exact leased command:

```text
timeout 5s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/scratch/check_fixed_r4_tuple.py
```

Lease status: granted by
`Agents/Kourovka/bus/archive/2026-08-17T234903Z__Lead__DECISION__grant-r4-action-support-reproduction.md`.
The exact once-only invocation exited zero in runner chunk `2dfd31`, wall time
`0.198841454` seconds.  Its fresh stdout is in `leased-output.md`; slot 1 was
released immediately.

A subsecond probe was invoked before the subsequent Lead checkpoint required a
lease for this frozen checker.  That probe's stdout is quarantined and is not
evidence.  The later leased output is the sole computational evidence.

# Interpretation limit

A failed projected-support gate excludes this one exact action representative
before cohomology.  A pass would still not be a group or counterexample.
In every case `active_assignment_answered: no` unless all exact source rows are
later checked on a finite exponent-nine group.
