---
title: "Partial result — no order-168 vanishing-set collision with PSL(2,7)"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
outcome: PARTIAL_RESULT
target_object: "Every finite group G of order 168 against the fixed simple target S=PSL(2,7)"
witness_object: "The 57 GAP SmallGroups representatives SmallGroup(168,i), i=1,...,57"
witness_equals_target: false
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/conjectured]
---

# Fixed-target computational partial result

## Active target

Canonical scope: `19.30/vanishing-order-simple-recognition`, assignment revision
1. The source asks universally over every finite simple target. This package
covers only the fixed target `S=PSL(2,7)` and therefore does not answer the active
universal assignment.

## Candidate partial statement

The completed exact GAP 4.12.1 enumeration supports the fixed-target implication

\[
 |G|=168\quad\text{and}\quad V_o(G)=V_o(\operatorname{PSL}(2,7))
 \quad\Longrightarrow\quad G\cong \operatorname{PSL}(2,7),
\]

for every finite group `G`, where `V_o` is the set of element orders attained by
vanishing elements and has no multiplicities. This is a `PARTIAL_RESULT` pending
independent reconstruction, not a solution of the universal problem.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed-target computational use | evidence | result |
|---|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | every admissible pair `(G,S)` | `S` is fixed to `PSL(2,7)` | manifest and final summary | not established universally |
| `19.30-G-finite` | admissibility | `G` finite | all 57 finite SmallGroups representatives of order 168 | `COVERAGE` and 57 `GROUP` rows | pass in fixed subcase |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | script constructs `PSL(2,7)`, checks size 168 and `IsSimpleGroup=true` | `TARGET` row | pass |
| `19.30-vanishing-definition` | admissibility | zero of some irreducible complex character | `Irr(CharacterTable(G))`; class marked iff an exact entry equals zero | complete `IRR_VALUES` and zero-witness rows | pass computationally |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | target and every enumerated representative have order 168 | target and identifier guards | pass |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets, not multisets | exact GAP sets compared; only identifier `[168,42]` returns true | all `GROUP` rows and `SUMMARY` | pass for the implication test |
| `19.30-isomorphic` | target conclusion | `G isomorphic S` | the unique equal-set representative is the target's own identifier `[168,42]` | zero non-target collisions | established only computationally for fixed `S` |

Because the universal row is not established, `witness_equals_target: false` and
`active_assignment_answered: no` are mandatory.

## What was computed in

The exact command, run once under Lead lease, was:

```bash
/bin/bash Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/run-v3.sh
```

It invoked GAP 4.12.1 on `SmallGroup(168,i)` for every integer `i` from 1 through
`NumberSmallGroups(168)=57`. It did not enumerate presentations outside the GAP
SmallGroups library or make a theoretical classification argument. The coverage
claim is precisely the library's complete list of isomorphism-type
representatives at order 168.

For each representative the run persisted:

- class orders and class sizes;
- every ordinary irreducible degree and complete exact character-value row;
- all zero-witness character indices by class;
- vanishing class indices and the set of their element orders;
- identifier, structure description, and equality-to-target Boolean.

Each table passed the internal sums `sum(class sizes)=168` and
`sum(character degree squares)=168`. The deterministic script completed with
exit status zero and empty stderr.

## Exact target data

The constructed target has:

- `IdGroup(PSL(2,7)) = [168,42]`;
- SmallGroups structure description `PSL(3,2)`;
- class orders `[1,2,3,4,7,7]`;
- class sizes `[1,21,56,42,24,24]`;
- irreducible degrees `[1,3,3,6,7,8]`;
- zero-witness indices by class
  `[[],[6],[2,3,4],[4,6],[5],[5]]`;
- `V_o(PSL(2,7)) = [2,3,4,7]`.

The script separately constructed `SmallGroup(168,42)`, checked it isomorphic to
the target construction, and required both representations to give the same set.

## Coverage and outcome

Persistent summary:

```text
EXPECTED_COVERAGE 57
ACTUAL_COVERAGE 57
COMPLETED 57
TARGET_ID [168,42]
TARGET_VANISHING_ORDER_SET [2,3,4,7]
NONISOMORPHIC_COLLISION_COUNT 0
COLLISION_INDICES []
```

There are exactly 57 `GROUP` rows. Text inspection finds exactly one
`EQUALS_TARGET_SET=true` row, namely group 42, the target itself. Thus the fixed
counterexample search met its bounded-negative gate and the named strategy is
exhausted at order 168.

## Persistent evidence and hashes

- Manifest: `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/manifest.md`
- Script SHA-256: `bcbfe6475fda465da72a7cf4fe91d18984b659a735f52f8ded78e2ba15156b7c`
- Runner SHA-256: `1f2e22c80e078d5974b6d3ec6819817d4a429656b02013af88e5bf98d0407179`
- `stdout.txt` SHA-256: `c425a731a710c0d029a7a770cfcf36766ec21338f55f934952790dfd225095f2`
- `stderr.txt` SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `exit-status.txt` SHA-256: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

The v1 guard failure and v2 withdrawal are preserved separately and are not
counted as coverage evidence.

## What this does not establish

- It does not establish the universal Kourovka 19.30 implication.
- It covers no simple target other than `PSL(2,7)`.
- It supplies no family-level argument and authorizes no extrapolation from `A5`
  or from order 168.
- It is a single implementation using GAP's SmallGroups and character-table
  machinery; it is not yet independently replicated.
- The internal degree/class checks catch incomplete tables but do not independently
  certify GAP's algorithms or library classification.
- It does not prove a structural theorem explaining why no collision occurs.

## Independent validation plan

Validator should write a separate script rather than reuse `screen-v3.g`:

1. independently confirm `NumberSmallGroups(168)=57` and target identifier;
2. reconstruct all 57 representatives;
3. compute ordinary irreducible character zeros and class orders by an independent
   loop/data representation;
4. confirm the target set `[2,3,4,7]`, the single true equality row 42, and zero
   non-target collisions;
5. recompute hashes and record GAP/package versions.

Until that reconstruction, the fixed-target statement remains
`status/conjectured`.

Verified by [[Agents/Kourovka/problems/19.30/verification/2026-08-17T152916Z-psl27-order168-zero-collision]].
