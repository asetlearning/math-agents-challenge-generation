---
title: "Exact stdout — fixed R4 action/support checker"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: R4-NEW-OUTER-CENTER-LABEL-ORBIT
evidence_status: quarantined_unleased_probe
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

**QUARANTINED:** this subsecond probe ran before the later Lead checkpoint
required a lease for the frozen checker.  It is preserved for audit but is not
used as evidence.  A fresh authorized invocation has been requested.

Probe stdout, verbatim:

```text
field=3
M=1020/0100/0010/0001
T=110/011/001
Tinv=121/012/001
LX=0000/0000/0001
LY=0000/0000/0200
X^3_label=0100
Y^3_label=0001
omega_labels=1
Z_M=1000/0100/0010/0001
Z_T=100/010/001
Z_L=0002/0201/0000
Z^3_label=0000
[X,Y]Z^-1=identity
[X,Z]_label=0101
[Y,Z]_label=0202
orbit_separator_rank_Mz_minus_I_new=0
orbit_separator_rank_Mz_minus_I_exhausted=1
exhausted_Mz=1020/0100/0010/0001
support_table_begin
h=000 lambda=0000 W=0 F=0000
h=001 lambda=0000 W=0 F=0000
h=002 lambda=0000 W=0 F=0000
h=010 lambda=0001 W=0 F=0001
h=011 lambda=0001 W=0 F=0001
h=012 lambda=0001 W=0 F=0001
h=020 lambda=0002 W=0 F=0002
h=021 lambda=0002 W=0 F=0002
h=022 lambda=0002 W=0 F=0002
h=100 lambda=0100 W=0 F=0100
h=101 lambda=0100 W=0 F=0100
h=102 lambda=0100 W=0 F=0100
h=110 lambda=0000 W=0 F=0000
h=111 lambda=0000 W=0 F=0000
h=112 lambda=0000 W=0 F=0000
h=120 lambda=0102 W=0 F=0102
h=121 lambda=0102 W=0 F=0102
h=122 lambda=0102 W=0 F=0102
h=200 lambda=0200 W=0 F=0200
h=201 lambda=0200 W=0 F=0200
h=202 lambda=0200 W=0 F=0200
h=210 lambda=0201 W=0 F=0201
h=211 lambda=0201 W=0 F=0201
h=212 lambda=0201 W=0 F=0201
h=220 lambda=0000 W=0 F=0000
h=221 lambda=0000 W=0 F=0000
h=222 lambda=0000 W=0 F=0000
support_table_end
Sigma=0000,0001,0002,0100,0102,0200,0201
Sigma_size=7
Sigma_span_basis=0001,0100
Sigma_span_dimension=2
Sigma_is_subspace=false
Sigma_symplectic_rank=2
additive_outsider=0001+0100->0101
```
