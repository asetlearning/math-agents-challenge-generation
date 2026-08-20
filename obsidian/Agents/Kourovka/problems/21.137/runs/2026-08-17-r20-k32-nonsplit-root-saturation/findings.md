---
title: "K32-NONSPLIT-ROOT-SATURATION — 73-label hard failure"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: K32-NONSPLIT-ROOT-SATURATION
direction: counterexample
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
active_minutes_charged: 15
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# K32-NONSPLIT-ROOT-SATURATION outcome

## Outcome

`STRATEGY_EXHAUSTED` for exactly the frozen K32 outer action, the single
lexicographically fixed `<c>`-correction row, and the central root `z^3=c`.
The K32 and extension-consistency gates pass, but the complete actual cube-label
set in `P/<c>` has only `73` of `81` labels. In particular
`(X0,Y0,z1,z2)=(0,0,0,1)` is absent. The central root changes only the `<c>`
coordinate and cannot repair this missing label.

Moreover, a subgroup image in the elementary abelian group `P/<c>` must have
3-power order. Since the full actual cube set has quotient image of size `73`,
the actual cube set itself cannot be a subgroup. Thus this fixed model is an
`OUT_OF_SCOPE_EXAMPLE`, not a counterexample. The unrestricted revision-2 scope
remains unanswered.

## Exact frozen object

Let `K=F_3^6` on the ordered basis

`X0,X1,X2,Y0,Y1,Y2`,

with `N(X_i)=X_(i-1)`, `N(Y_i)=Y_(i-1)` for positive indices and `N(X0)=N(Y0)=0`.
Put `U=I+N`. Let

`W=<z>_9 x <z1,z2>_3`, with `c=z^3`,

and extend `U` by `U(z)=z`, `U(z1)=z1+c`, `U(z2)=z2+z1`.

The one frozen alternating pairing `B:K x K -> <c,z1,z2>` has zero same-chain
values and the cross table `B(Y_i,X_j)`

| `i\j` | `0` | `1` | `2` |
|---:|---|---|---|
| `0` | `c` | `z1` | `z2` |
| `1` | `z1` | `c+z1+2z2` | `z1+2z2` |
| `2` | `z2` | `2c+z1+2z2` | `0` |

and reverse values fixed by alternation. There is no second row.

Define

`(k,w)(l,v)=(k+l,w+v+2B(k,l))`

and adjoin `u` of order `3` so right conjugation by `u` is `U`. This gives a
unique coordinate normal form

`G={(k,w,i): k in K, w in W, i in F_3}`

of order `3^11=177147`. The subgroup

`P=<X0,Y0,c,z1,z2>`

has order `3^5`; `B(Y0,X0)=c`, so `[X0,Y0]` has the nontrivial `c` coordinate
up to the displayed commutator orientation. The root-free extension `G0` has
`W0=<c,z1,z2>` and order `3^10=59049`.

## Gate record

### +10 outer-action gate — pass

The quotient outer group has the five-coordinate normal form

`x2^a x1^b y2^d y1^e u^i`, all coordinates in `F_3`,

and relations: the first four generators commute; all five generators have
order dividing `3`; `u^-1 x2 u=x2 x1`, `u^-1 y2 u=y2 y1`; and `u` fixes
`x1,y1`. Hence its order is `3^5`, exponent is `3`, and its central
commutator image has the independent generators `(1,0,0,0)` and
`(0,0,1,0)`. This is the required `K32` structure.

### +24 extension-obstruction gate — pass

The leased checker verifies alternation, the bilinear cocycle equation, and
`U`-equivariance for the displayed `B`. It also verifies the fixed actions
`U,S_(R_f),S_(R_e)` and obtains

`A_f^3=X0`, `A_e^3=Y0`

with no non-`<c>` discrepancy. The coordinate multiplication is therefore a
complete consistent extension presentation with the orders above.

### +42 complete quotient-label gate — fail

For `g=(k,w,i)`, put `A=U^(-i)`. The frozen closed cube formula is

`g^3 = q A(q) A^2(q)`,

with K-label `(I+A+A^2)k` and central correction

`2(B(k,Ak)+B(k,A^2k)+B(Ak,A^2k))`.

The `W`-norm changes only `<c>` modulo `<c>`. For
`k=(x0,x1,x2,y0,y1,y2)`, the two nonzero `u` rows reduce modulo `<c>` to:

| `i` | `X0` | `Y0` | `z1` | `z2` |
|---:|---|---|---|---|
| `1` | `x2` | `y2` | `2x0y2+2x1y2+x2y0+x2y1` | `2x1y2+x2y1` |
| `2` | `x2` | `y2` | `x0y2+2x2y0` | `x1y2+2x2y1` |

This is the actual value-map image, not the subgroup it generates. Its union
over every `k in F_3^6` and `i in F_3` has `73` labels. Eight labels are
missing; the first in lexicographic order is `(0,0,0,1)`. This fires the exact
hard kill.

### +50 fibre/exponent gate — not reached

The label failure stops the construction before the scheduled fibre audit.
For scope bookkeeping only, the already displayed coordinate law and cube
formula show the candidate group has exact exponent `9`: every cube lies in
the exponent-three coordinate subgroup `P`, while `z` has order `9`. No
`GATE_3=PASS` is claimed because the frozen program correctly exited first.

### +55 certificate gate — failure certificate only

This note and the immutable stdout are the exact failure certificate. No
success certificate, claim check, or Validator-ready counterexample exists.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | frozen candidate / evidence | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | universal assertion over admissible `p,G` | one fixed failed construction cannot refute the universal assertion | not established |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | `p=3` | pass |
| `21.137-odd-finite-p-group` | admissibility | finite 3-group | coordinate normal form has order `3^11` | pass |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `9` | cube formula puts cubes in exponent-three `P`; central `z` has order `9` | pass for the failed model |
| `21.137-odd-power-set-definition` | admissibility | complete actual cube-value set | closed formula evaluates every coordinate element; quotient image has 73 labels | pass |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube set is a subgroup | its quotient image has non-3-power size `73` | **fail** |
| `21.137-odd-P-abelian` | target conclusion | power-value subgroup is abelian | subgroup hypothesis fails, so the conclusion is not violated | not violated |

## Exact run record

- artifact SHA-256:
  `0120923226d69921e25d8cb3d971b939d4d54210d9dc16c77e7c320ef195507c`;
- command: `timeout 120s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r20-k32-nonsplit-root-saturation/scratch/k32_nonsplit_frozen.py`;
- executions: exactly one; reruns: zero;
- exit code: `2` (the programmed quotient-label hard kill);
- wall time: `0.31164281` seconds;
- stderr: empty;
- stdout SHA-256:
  `a63aa1f4b07b6f69be74ecf000df0ba5545e2ec98c6b55970c4118ed89a14d1a`;
- stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- metadata SHA-256:
  `49bf99b1471a76dee49c420f7be5c5a059ba732ecc1ecfcd5f1ede7686e0cceb`;
- compute slot 1 released at `2026-08-17T15:25:02Z`.

## Exact active-time ledger

- `2026-08-17T15:08:06Z`--`2026-08-17T15:17:06Z`: `9` active minutes
  freezing and writing the sole exact coordinate artifact. The earlier `+0`
  pre-computation note is corrected here: no command had run, but mathematical
  reasoning and artifact writing are charged by protocol.
- `2026-08-17T15:17:06Z`--`2026-08-17T15:24:35Z`: lease wait, `0` charged
  minutes.
- `2026-08-17T15:24:35Z`--`2026-08-17T15:30:35Z`: `6` active minutes for
  hash verification, the single supervised run, output inspection,
  preservation, the 73-not-a-3-power closure deduction, and this report.

Total this run: exactly `15` active minutes, `+15/55`. Scope cumulative ledger:
`470+15=485` active minutes. The remaining balance in this authorized
55-minute window is exactly `40` active minutes. The hard failure occurred
early; no time was spent on another row or strategy.

## What this rules out

It rules out exactly the frozen outer action with exactly the displayed
lexicographic correction row and the central root `z^3=c`. It does not rule out
another nonsplit extension, correction row, representative, outer action,
prime, or construction family. None was opened.

## What this does not establish

- It does not answer Problem 21.137 or the active revision-2 scope.
- It does not establish that every nonsplit K32 extension misses a label.
- It does not replace the actual cube set by its generated subgroup.
- It does not use or say anything about `p=2`, exponent `8`, wreath-shaped or
  hidden material, a second cocycle ansatz, or a PF-generator variant.
