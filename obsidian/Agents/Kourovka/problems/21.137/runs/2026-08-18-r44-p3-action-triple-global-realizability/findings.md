---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
cycle: 32
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# PARTIAL_RESULT — minimal action-image exclusion and action-cover method test

## Active target

Scope: `21.137/odd-prime-exponent-p2`  
Assignment revision: 2  
Target: for odd `p`, a finite `p`-group of exponent exactly `p^2` whose literal `p`-th-power set is a subgroup must have that subgroup abelian.

## Bounded claim

At `p=3`, there is an exact compatible nonorthogonal action triple on `P=H_3(3) x C3^2`, and:

1. its minimal action image has only seven of the nine required inner cube labels, so no extension with exactly that conjugation image can have literal cube set `P`; and
2. one canonical full-translation action completion has action-cube set exactly `Inn(P)`.

The first item is an exact bounded exclusion. The second is only an action-cover method test: it is not an associative ambient-group witness. The completion is recognizably wreath-shaped and therefore excluded from discovery-blind evidentiary credit by the canonical scope record. The unrestricted odd-prime scope remains unanswered.

## Exact construction and hand obstruction

Use coordinates `(x,y,u,v,z)` on `P`, with `u,v,z` central and `[x,y]=z`. Put

`T(u)=u+v`, `T(v)=v+z`, `T(z)=z`,

and define

- `alpha(x)=x`, `alpha(y)=y+u`, `alpha|Z=T`;
- `beta(x)=x+u`, `beta(y)=y`, `beta|Z=T`.

Then `alpha^3=Inn(-x)`, `beta^3=Inn(y)`, and `(alpha beta)^3=Inn(-x+y)`; the product action fixes `-x+y-u-v`.

For `A=<alpha,beta>`, a four-dimensional translation-module normal form gives `|A|=3^5`, `Inn(P)<=A`, and `|A/Inn(P)|=27`. Its exact cube labels in `P/Z(P)` are

`(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)`.

The missing labels are `(1,1),(2,2)`. If an ambient group had action image exactly `A` and literal cube set `P`, functoriality of cubes under its conjugation map would force `A^(3)=Inn(P)`, contradicting `7 != 9`. This argument is independent of every factor system.

The canonical missing-label action is

`gamma(x)=x+u`, `gamma(y)=y+2u`, `gamma|Z=T`.

It has `gamma^3=Inn(x+y)` and fixes `x+y`. The completed action group

`B=<alpha,beta,gamma>=Hom(F_3^2,F_3^3) semidirect <T>`

has order `3^7` and literal cube set exactly `Inn(P)` (nine elements), so the action-only gate passes.

## Blind-boundary correction

After the action-cover gate passed, an ambient split-holomorph checker was run under the earlier Lead authorization but before the later blind-boundary stop reached this context. Lead then ordered the wreath-shaped route stopped and its ambient output not interpreted as a target candidate. The script and observed stdout remain preserved as a quarantined process artifact; neither is used as mathematical evidence in this finding. No rerun, alternate completion, or factor-system family was opened.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed model / evidence | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | universal assertion over all admissible `p,G` | only one exact action-image family is excluded | not answered |
| `21.137-odd-p-not-2` | admissibility | odd prime | action work is over `F_3` | pass for method test |
| `21.137-odd-finite-p-group` | admissibility | finite 3-group | no target ambient candidate is asserted | not established |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly 9 | no target ambient candidate is asserted | not established |
| `21.137-odd-power-set-definition` | admissibility | designated `P` equals all actual cubes | the minimal action image fails the necessary projected equality; the completion is action-only | not established |
| `21.137-odd-power-set-subgroup` | admissibility | literal cube set is a subgroup | no target ambient candidate is asserted | not established |
| `21.137-odd-P-abelian` | target conclusion | counterexample requires nonabelian literal cube subgroup | the displayed `P` is nonabelian, but it is not established as an ambient literal cube set | not violated |

`active_assignment_answered: no`.

## Reproducibility

- Local/minimal/completed action audit: `scratch/action_group.py`, SHA-256 `7b479044e2bf7921da8389da34cfd6637bf26bc50461636d7dd5d8b55263fd04`.
- Quarantined, non-evidentiary process artifacts after the blind-boundary stop: `scratch/full_translation_holomorph_audit.py` and `scratch/full_translation_holomorph_audit.out`. They are preserved for audit only and are not relied on above.

The completion is recognizably `J_3`/wreath-shaped. The canonical scope already records filename-only prior exposure, so no clean-discovery credit is claimed for this bounded reconstruction.

## What this does not establish

It does not exclude a realization with action image strictly larger than the minimal `A`, a nonsplit realization, another kernel, another prime, or the unrestricted source target. No alternate completion or factor-system family was opened.
