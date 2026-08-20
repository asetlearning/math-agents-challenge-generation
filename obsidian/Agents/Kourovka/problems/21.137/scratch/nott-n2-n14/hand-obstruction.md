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
strategy_id: NOTT3-N2-N14-CUBESET
outcome: STRATEGY_EXHAUSTED
---

# Exact early G4 obstruction

Work only in `R=F_3[t]/(t^14)` with the frozen composition convention
`(f*g)(t)=f(g(t))`.  Write an arbitrary carrier element as

`f(t)=t+h(t)`, where `h(t)=a_3t^3+...+a_13t^13`.

## 1. Every cube lies in `K_6`

Reduce first modulo `t^7`; terms of `h` above degree 6 cannot contribute.  In
characteristic three,

`(t+h)^3=t^3`,

`(t+h)^4=t^4+a_3t^6`,

`(t+h)^5=t^5`, and `(t+h)^6=t^6` modulo `t^7`.  Hence

`h(t+h)=h+a_3a_4t^6 (mod t^7)`.

Put `q=h+h(t+h)=2h+a_3a_4t^6`, so that `f^2(t)=t+q(t)`.  The leading
coefficient of `q` is `2a_3`, and the same four expansions with `q` in place
of `h` give

`h(t+q)=h+2a_3a_4t^6 (mod t^7)`.

Therefore

`f^3(t)-t=q+h(t+q)=3h+3a_3a_4t^6=0 (mod t^7)`.

Thus every literal cube is of the form `t+A(t)` with `A in t^7R`, i.e. every
cube lies in `K_6` (indexing `K_m` by agreement with `t` through degree `m`).

## 2. `K_6/K_13` is abelian in the frozen truncation

Take `u=t+A` and `v=t+B` with `A,B in t^7R`.  Modulo `t^14`, the only
possible substitution cross term is the degree-7/degree-7 term:

`A(t+B)=A(t)+a_7b_7t^13 (mod t^14)`,

because `(t+B)^7=t^7+7t^6B=t^7+b_7t^13 (mod t^14)`, while for every
degree `i>=8` the first cross term has degree at least `i+6>=14`.  Symmetrically,

`B(t+A)=B(t)+b_7a_7t^13 (mod t^14)`.

The two cross terms are equal in `F_3`, so

`u(v(t))=t+A+B+a_7b_7t^13=v(u(t)) (mod t^14)`.

Hence all elements of `K_6` commute in this carrier (equivalently
`[K_6,K_6] <= K_13`, which is invisible modulo `t^14`).

## Consequence for the active counterexample route

The complete literal cube set is pairwise commuting, independently of whether it
is closed under multiplication and independently of the carrier exponent.  Thus
this frozen carrier can never violate constraint `21.137-odd-P-abelian`.  It meets
the early G4 impossibility kill and cannot be a counterexample to revision 2.

No program was launched, the heavy lease was withheld, and no enumerated output is
claimed.  The frozen but unexecuted script has SHA-256
`b47c33a29577e7462b8f36a9cb0c1ebc6c65194db01ac63b27a4c0bba0d059cd`.

## Constraint-and-conclusion matrix for the stopped carrier

| constraint_id | role | carrier implication | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | A single `p=3` carrier could refute the universal assertion only if every remaining row passed. | not reached |
| `21.137-odd-p-not-2` | admissibility | Frozen prime is `3`. | pass |
| `21.137-odd-finite-p-group` | admissibility | Frozen carrier has `3^11` tuples, subject to the unrun carrier checks. | not computationally checked |
| `21.137-odd-exponent-p2` | admissibility | Exact exponent 9 gate was not run. | not checked |
| `21.137-odd-power-set-definition` | admissibility | The intended `P` is the literal complete cube image; it was not enumerated. | definition frozen, not enumerated |
| `21.137-odd-power-set-subgroup` | admissibility | Closure gate was not run. | not checked |
| `21.137-odd-P-abelian` | target conclusion | Every cube lies in the abelian layer `K_6/K_13`; hence every pair of actual cube values commutes. | cannot be violated |

## Active-time ledger

- `2026-08-17T15:42:49Z`–`2026-08-17T15:49:35Z`: froze the exact carrier code,
  hash, command, and lease request; cumulative charged time rounded up to 7 minutes.
- Lease wait was uncharged.  No process ran.
- `2026-08-17T15:52:00Z`–`2026-08-17T15:57:30Z`: checked and packaged the two
  filtration calculations above, including the orientation/sign audit; cumulative
  charged time rounded up to 13 minutes.
- Strategy stops with 27 of the 40 allocated active minutes unused and returned to
  Lead.  This is only a stop for `NOTT3-N2-N14-CUBESET`, not a scope park.
