---
title: "Frozen manifest — PSL(2,7), order-168 vanishing-set collision screen"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
strategy: PSL27-ORDER168-VANISHING-COLLISION
frozen_utc: 2026-08-17T14:50:47Z
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Frozen run manifest

No GAP call, mathematical probe, or other mathematical computation preceded this
freeze. The script and runner below are immutable for the requested lease. Any
change requires a new hash and a new Lead lease.

## Scope and exact invariant

- Fixed simple target: `S = PSL(2,7)`.
- Frozen target order: `168`.
- Candidate family: every library representative `SmallGroup(168,i)` for
  `1 <= i <= NumberSmallGroups(168)`.
- Frozen coverage count: `NumberSmallGroups(168) = 42`; the script emits the
  library-reported count and aborts unless it is exactly 42.
- Vanishing definition: a conjugacy class is vanishing exactly when at least one
  ordinary irreducible complex character has exact value zero on it.
- Recorded invariant: the set of the element orders of all vanishing classes.
  Multiplicities are discarded.
- Collision criterion: a representative with index different from the target's
  `IdGroup` index has exactly the same recorded set as `PSL(2,7)`.

## Frozen files and hashes

| file | SHA-256 |
|---|---|
| `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/screen.g` | `5f85824f542f1b7f7b8f9eb23200cead236fc6029b45fc1d821fe9ff246023af` |
| `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/run.sh` | `47f9052e54901dbedc5476f89436d82e3b245d36b6456319939bb0f3660af55a` |

The same two lines are frozen in `hashes.sha256`.

## Exact command

From the vault root:

```bash
/bin/bash Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/run.sh
```

The runner invokes exactly:

```bash
/usr/bin/timeout --signal=TERM --kill-after=30s 900s /usr/bin/gap -q Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/screen.g
```

with the persistent redirections and exit-status write named below.

## Persistent outputs

| artifact | path |
|---|---|
| standard output | `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/stdout.txt` |
| standard error | `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/stderr.txt` |
| process exit code | `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/exit-status.txt` |
| frozen hashes | `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/hashes.sha256` |

A timeout, nonzero exit, missing final `SUMMARY` row, or completed count other
than 42 is not a bounded-negative result. Partial stdout remains evidence only of
the explicitly completed prefix.

## What the script checks and records

1. It emits the GAP version and the runtime `NumberSmallGroups(168)` count, and
   hard-aborts unless that count is 42.
2. It constructs `PSL(2,7)`, checks size 168 and simplicity, computes its
   `IdGroup`, and hard-aborts unless the identifier is `[168,42]`.
3. It checks that this constructed target is isomorphic to `SmallGroup(168,42)`
   and that the two representations produce the same vanishing-order set.
4. For every `i=1,...,42`, it reconstructs `SmallGroup(168,i)`, checks the
   identifier `[168,i]`, computes the ordinary irreducible character table, and
   records class orders, class sizes, all irreducible degrees, every irreducible
   character-value row, zero-witness character indices by class, vanishing class
   indices, and the exact vanishing-order set.
5. For every table it checks that the class sizes sum to 168 and that the squares
   of all irreducible degrees sum to 168.
6. For any non-target collision it independently asks GAP for a group
   isomorphism to the target and requires `fail`, materializes an isomorphic
   permutation group, prints its permutation generators, rechecks its order and
   `IdGroup`, and recomputes the colliding invariant in that representation.
7. Only after all 42 rows complete does it emit a final `SUMMARY` with expected,
   actual, and completed coverage, target identifier and set, collision count,
   and collision indices.

The run is deterministic and uses no random seed or randomized search.

## Resource and lease request parameters

- Heavy slots requested: 1.
- CPU: one process / approximately one CPU core.
- Expected wall and CPU time: under 10 minutes; hard timeout 900 seconds.
- Expected RAM: under 512 MiB; conservative maximum estimate 1.5 GiB.
- Timeout behavior: `TERM` at 900 seconds, forced kill 30 seconds later.
- Requested lease duration: 20 minutes, including output inspection and release.

## Interpretation gates

- Success: a printed `COLLISION` row for an index other than 42, with a completed
  42/42 summary and exit code zero. This is only a prospective universal-scope
  counterexample until every canonical row and the materialization are packaged
  and independently reviewed.
- Bounded negative: exit code zero, completed 42/42 summary, and zero
  nonisomorphic collisions. This excludes only the fixed target `S=PSL(2,7)`
  among the complete SmallGroups library representatives of order 168, pending
  independent validation. It does not prove the universal recognition statement.
- No family extrapolation, A5 analogy, literature/history lookup, or web search is
  part of this run.

## Validator reconstruction plan

For a collision, Validator can reconstruct either `SmallGroup(168,i)` or the
printed permutation generators, independently recompute its ordinary irreducible
character table and target table, check exact zero entries and class orders, and
check nonisomorphism. For a bounded negative, Validator can rerun a separately
written loop over all 42 identifiers and compare the exact sets without trusting
the parsing or constants in this script.
