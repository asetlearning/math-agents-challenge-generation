---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/word-maps
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: NOTT3-N2-N15-EDGE
outcome: STRATEGY_EXHAUSTED
---

# Degree-7/8 cube projection and degree-14 bracket

Use only the frozen carrier

`f_a(t)=t+a_3t^3+...+a_14t^14 mod t^15`

over `F_3`, with orientation `(f_a*f_b)(t)=f_a(f_b(t))`.

## Exact composition through degree 8

Modulo `t^9`, if `g=t+k` with `k in t^3R`, then

- `g^3=t^3`;
- `g^4=t^4+b_3t^6+b_4t^7+b_5t^8`;
- `g^5=t^5+2b_3t^7+2b_4t^8`;
- `g^6=t^6`, `g^7=t^7`, and `g^8=t^8`.

Consequently the coordinates of `f_a*f_b` through degree 8 are

```
c_3 = a_3+b_3
c_4 = a_4+b_4
c_5 = a_5+b_5
c_6 = a_6+b_6+a_4b_3
c_7 = a_7+b_7+a_4b_4+2a_5b_3
c_8 = a_8+b_8+a_4b_5+2a_5b_4.
```

For `s=a*a`, this gives

```
s_3=2a_3,  s_4=2a_4,  s_5=2a_5,
s_6=2a_6+a_4a_3,
s_7=2a_7+a_4^2+2a_5a_3,
s_8=2a_8.
```

Apply the same law to `s*a=a^3`.  The degree-6, -7, and -8 coordinates are

```
(a^3)_6 = 3a_6+3a_4a_3 = 0,
(a^3)_7 = 3a_7+3a_4^2+6a_5a_3 = 0,
(a^3)_8 = 3a_8+6a_4a_5 = 0.
```

The degree-3, -4, and -5 coordinates are also `3a_i=0`.  Thus the exact
degree-7/8 projection of every literal cube is

`pi_7,8(a^3)=(0,0)`.

In fact every cube lies in `K_8`, i.e. is congruent to `t mod t^9`.

## Induced degree-14 commutator form

For hypothetical depth-6/7 elements

`F=t+x_7t^7+x_8t^8+...` and `G=t+y_7t^7+y_8t^8+...`,

the nonlinear degree-14 coefficient in `F*G` is

`x_7y_8+2x_8y_7`,

whereas in `G*F` it is

`y_7x_8+2y_8x_7`.  Their degree-14 difference is the alternating form

`B(x,y)=x_8y_7-x_7y_8`.

The actual cube projection is the zero subspace, hence is isotropic for `B`.
More strongly, since actual cubes start in degree 9, every first substitution
cross term between two cube values has degree at least `9-1+9=17`, beyond the
`mod t^15` carrier.  Therefore all literal cube values commute in the frozen
carrier regardless of whether their set is multiplicatively closed.

## Route outcome

The early +5 gate fails: constraint `21.137-odd-P-abelian` cannot be violated by
this carrier.  `NOTT3-N2-N15-EDGE` is therefore `STRATEGY_EXHAUSTED`.  No script
was written or executed and no lease is requested.  This does not park or answer
the unrestricted revision-2 scope, and no N16 or parameter variant is opened.

## Active-time ledger

- N15 active work began `2026-08-17T16:00:10Z` after the authoritative N14 ledger
  correction was filed.
- The degree projection, bracket, sign/orientation audit, and packaging ended
  `2026-08-17T16:02:20Z`; cumulative N15 charge is 3 of 27 active minutes after
  rounding up, so 24 minutes are returned to Lead.
