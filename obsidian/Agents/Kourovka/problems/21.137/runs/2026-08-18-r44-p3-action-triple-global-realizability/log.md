---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
cycle: 32
strategy: P3-ACTION-TRIPLE-GLOBAL-REALIZABILITY
context_mode: clean
---

# Cycle 32 log — fixed action-triple global realizability

## Active-time ledger

- `2026-08-18T10:36:31Z`: work start, official cumulative active minute `912`.
- `2026-08-18T10:46:01Z`: protocols, scope, roster, decision, current inbox, and source gate completed; approximately 10 newly active minutes, cumulative `922`.

## Staleness and source gate — 2026-08-18T10:46:01Z

Rendered source page 184 was inspected directly, as well as its text extraction. The in-scope source clause is:

> For `p != 2`, if the `p`-th powers in a `p`-group of exponent `p^2` form a subgroup, must that subgroup be abelian?

`source_transcription_checked: yes`. The visual formula is `p^2`, not `p2`. The canonical scope record agrees. `active_scope_checked: yes`.

Clause matrix:

| source clause | in active scope? | treatment |
|---|---:|---|
| General powerfulness question | no | excluded |
| Odd-prime, exponent exactly `p^2`, actual power set a subgroup, ask abelian | yes | active revision-2 target |
| `p=2`, exponent 8, squares | no | explicitly excluded |

The run is discovery-blind (`blind_run.enabled: true`, `open_web: false`), so `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. No solution-bearing historical artifact was read. The local corpus directory contains issue data only through issue 20, so there is no issue-21 JSON flag record to inspect in this clean run.

Canonical admissibility/conclusion checklist:

| constraint_id | requirement at the fixed test prime |
|---|---|
| `21.137-odd-forall-p-G` | A single admissible `p=3` witness would refute the universal assertion. |
| `21.137-odd-p-not-2` | Fix the odd prime `p=3`. |
| `21.137-odd-finite-p-group` | The ambient object must be a finite 3-group. |
| `21.137-odd-exponent-p2` | Its exponent must be exactly 9. |
| `21.137-odd-power-set-definition` | `P` must equal the complete literal set `{g^3:g in G}`. |
| `21.137-odd-power-set-subgroup` | That literal set must itself be a subgroup. |
| `21.137-odd-P-abelian` | A counterexample must violate this: two literal cubes must not commute. |

## Strategy portfolio — 2026-08-18T10:46:01Z

1. **Assigned structured construction (work first).** Put an explicit coordinate model on `P=H_3(3) x C3^2`; derive automorphisms whose cubes in a putative extension are conjugations by two noncommuting values, and impose the product-root action identity. First exact gate: the three inner automorphisms must be compatible with multiplication in one outer action, not merely individually realizable.
2. **Global presentation gate.** If the action triple survives, freeze one quotient/presentation and derive all associativity/relator conditions before any enumeration. A formal action array or factor system is only a method test.
3. **Theoretical obstruction.** Use the universal identity `conj(g^3)=conj(g)^3` and the homomorphism `G -> Out(P)` (available only if the eventual cube subgroup `P` is normal) to detect whether prescribed root actions can coexist. In particular, compare `(alpha beta)^3` with `alpha^3 beta^3` including commutator corrections.
4. **Certificate plan.** A positive result would require a finite presentation/normal form and a complete all-element cube computation independently checkable by direct multiplication. A negative result must name exactly the frozen action triple or family and exhibit one unavoidable relator defect.

No catalogue enlargement and no heavy computation are planned without a Lead lease.

## Exact local action triple — 2026-08-18T10:50:00Z

Write `P` in Lie/Heisenberg coordinates on the basis `(x,y,u,v,z)`, with `u,v,z` central and `[x,y]=z`; this is `H_3(3) x C3^2`. Let `T` act on the center by

`u -> u+v`, `v -> v+z`, `z -> z`.

Define bracket-preserving linear automorphisms

- `alpha: x->x, y->y+u`, with central restriction `T`;
- `beta: x->x+u, y->y`, with central restriction `T`.

Direct multiplication over `F_3` gives

- `alpha^3 = Inn(-x)`;
- `beta^3 = Inn(y)`;
- `(alpha beta)^3 = Inn(-x+y)` and `alpha beta` fixes the exact representative `-x+y-u-v`.

Thus the three nonorthogonal labels `-x`, `y`, and `-x+y` are individually and multiplicatively action-compatible. This is only a local action triple, not an ambient group.

The exact checker `scratch/action_group.py` independently multiplies the displayed matrices. Observed output includes `alpha^3_is_inn_minus_x True`, `beta^3_is_inn_y True`, `(alpha beta)` order 9, and `product_label_fixed True`.

## First global gate: complete minimal action image — 2026-08-18T10:54:50Z

Let `A=<alpha,beta> <= Aut(P)` and `I=Inn(P)`. There is a short hand normal form. If `ell=y^*-x^*` and `M` is the four-dimensional translation module generated by `u ell` under `T` together with `z y^*`, then

`A = M <alpha>`, `|A|=3^5`, `I<=A`, and `|A/I|=27`.

For a normal-form element `m alpha^k`, `k in F_3`, the `u`-component of its shear is

`k y^* + a(y^*-x^*) = -a x^* + (k+a)y^*`.

For `k=0` its cube is trivial. For `k=1,2`, the central norm is

`1+T^k+T^(2k)`, which maps `u` to `z` and kills `v,z`. Therefore the exact inner labels of cubes in `A` are

`(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)`

in `(x,y)` coordinates. The two labels `(1,1)` and `(2,2)` are absent. Hence the literal cube set of `A` has 7 elements, whereas `I` has 9.

This gives a factor-system-independent obstruction for the **exact minimal action image**. If an ambient `G` had literal cube set `P` and conjugation image on `P` equal to `A`, then, for `theta:G->A`,

`theta({g^3:g in G})={a^3:a in A}`.

The left side is `theta(P)=Inn(P)=I`, while the right side has size 7. Contradiction. Thus no associative extension having exactly this action image can satisfy literal cube equality, regardless of its factor system. A strictly larger action image is not excluded.

The same checker observed `A_order 243`, `I_order 9`, `A_literal_cube_count 7`, and the two missing labels above.

As a separate fully associative method test, `scratch/holomorph_cube_audit.py` exhaustively audited the fixed semidirect product `H=P semidirect A` of order `3^10`. It has exponent exactly 9, but its literal cube set has 55 elements, is not closed (the checker records one explicit product defect), and contains no noncommuting pair. This `H` is an `OUT_OF_SCOPE_EXAMPLE`, not a witness.

## Strategy-boundary self-check — 2026-08-18T10:54:50Z

- Exact active scope/revision: `21.137/odd-prime-exponent-p2`, revision 2.
- The local triple exists, but the minimal complete action image fails the necessary literal-cover identity `A^(3)=Inn(P)`.
- This rules out exactly the frozen minimal action image and its factor systems; it does not rule out an overgroup of actions containing the triple.
- The representation remains productive only if Lead authorizes one canonical action completion. The natural completion adds one root action for either missing diagonal label, generating the full six-dimensional translation module; this repairs the action-level cube cover but opens a genuinely new extension-obstruction problem.
- No canonical target witness exists. `active_assignment_answered: no`.

## Lead-authorized canonical completion — 2026-08-18T10:57:35Z

Lead authorized exactly one missing-diagonal action and, only if its complete action cube set equals `Inn(P)`, the one split holomorph. No alternate generator, nonsplit factor system, or family search was authorized.

Take `gamma(x)=x+u`, `gamma(y)=y+2u`, and `gamma|Z=T`. Then `gamma^3=Inn(x+y)` and `gamma` fixes `x+y`. Exact enumeration gives

`B=<alpha,beta,gamma>` of order `3^7`, with its complete literal cube set equal to the nine-element `Inn(P)`. Thus the action-only gate passes.

The canonical completion is visibly a two-`J_3` full-translation semidirect action, hence wreath-shaped. This was reported immediately to Lead because the canonical blind-run record excludes any wreath-shaped result from clean-discovery credit.

## Complete authorized split-holomorph audit — 2026-08-18T11:00:59Z

The exact group `H=P semidirect B` has order `3^12`. `scratch/full_translation_holomorph_audit.py` uses the derived coordinate laws (not a matrix-group catalogue) and enumerates all 531,441 elements once. The observed run took 2.79 seconds and 14,720 KiB RSS, below the heavy-compute threshold.

The complete cube set has 75 elements and sorted-set SHA-256 `46b121c21f36b8fc44868a0e88cf691ab538f40bf9f0fe5f5972017b425da248`. Every cube has cube 1 and some cubes are nontrivial, so `H` has exponent exactly 9. The cube set projects onto all nine inner actions but has fibre sizes `3,9,9,9,9,9,9,9,9`; it is not the embedded `P` of size 243.

The checker exhaustively found no noncommuting cube pair and found the explicit closure defect recorded in `findings.md`. Therefore this split completion fails both literal equality and literal-set subgroup closure. It is an `OUT_OF_SCOPE_EXAMPLE`.

## Cycle outcome and stop — 2026-08-18T11:00:59Z

Outcome: `PARTIAL_RESULT`. The fixed minimal action image and the single authorized canonical full-translation split completion are exactly excluded. The unrestricted scope is unanswered. Charge 25 newly active minutes, official cumulative `912 -> 937`, and return 20 unused minutes. Research stops at the authorized strategy boundary in `awaiting_lead`; no alternate completion or factor-system family was opened.

## Blind-boundary correction — 2026-08-18T11:02:45Z

Lead's later stop reached this context after the previously authorized split-holomorph command had completed. Because the full-translation completion is wreath-shaped, its ambient checker and stdout are now quarantined as non-evidentiary process artifacts and are not interpreted as a target candidate or credited as clean discovery. The packaged mathematical outcome is narrowed to the exact minimal-image seven-of-nine exclusion plus the action-only nine-of-nine completion test. The unrestricted target remains unanswered. No further research is performed.
