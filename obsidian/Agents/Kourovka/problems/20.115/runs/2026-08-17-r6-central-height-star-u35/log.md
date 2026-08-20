---
title: "Problem 20.115 SU3(5) central-height-star block bridge log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
strategy: R6-CENTRAL-HEIGHT-STAR-U35
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# R6-CENTRAL-HEIGHT-STAR-U35 log

## Active-time ledger

- Work start: `2026-08-17T23:07:19Z`; inherited cumulative active time
  `00:43:16`. This proof increment has at most 45 active minutes, an
  eight-active-minute installed-data prerequisite kill, research stop by
  increment minute 38, and packaging stop by minute 45.

## Locked target and route

The exact revision-1 source target remains universal: for every finite group
`G`, every ordinary irreducible complex character `chi`, and every `x in G`,
exact `chi(x) != 0` should imply the integer divisibility
`o(x)chi(1) | |G|`. This run is restricted to testing the sufficient block
condition `(double-dagger-star)` for `L=SU_3(5)=3.U3(5)`, `p=3`, and
`Z=Z(L)=C3`. Failure of that sufficient condition would not be a source
counterexample.

## Central-height identity — hand derivation

Let `B` be a `p`-block of a finite group `L`, let `D` be a defect group of
`B`, and let `Z <= Z(L)` be a central `p`-subgroup. Write

```text
|L|_p = p^a,    |D| = p^d,    |Z| = p^z.
```

Here is the needed central-subgroup step in Brauer-pair form. Let `b` be the
block idempotent in an algebraically closed field of characteristic `p`. Since
`Z` is central, `C_L(Z)=L`; consequently the Brauer homomorphism at `Z` retains
every group-basis coefficient and satisfies `Br_Z(b)=b != 0`. Thus `(Z,b)` is
a `B`-Brauer pair. Extending it to a maximal `B`-Brauer pair `(D,b_D)` shows
`Z <= D`; the first components of maximal `B`-Brauer pairs are precisely the
defect groups of `B`. Equivalently, central-`p` quotient theory sends `D` to the
quotient defect group `D/Z`. Hence `|D/Z|=p^(d-z)`.

By the definitions of block defect and character height, if
`theta in Irr(B)` has height `h(theta)`, then

```text
theta(1)_p = p^(a-d+h(theta)).
```

Therefore, using only exact `p`-parts,

```text
(|L:Z|/theta(1))_p
 = p^(a-z) / p^(a-d+h(theta))
 = p^(d-z-h(theta))
 = |D/Z| / p^h(theta).
```

This proves the proposed identity. In particular the paper's condition

```text
exp(D/Z) <= (|L:Z|/theta(1))_p
```

is equivalent, block row by block row, to

```text
p^h(theta) <= |D/Z| / exp(D/Z).
```

The fixed paper artifact `/tmp/2605.04513v1.pdf` has the expected SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.
Its displayed `(double-dagger-star)` is exactly the exponent inequality above,
with `Z=Z(L)_p`; here `Z(L)=C3`, so this is the present `Z`.

## Installed-data gate and frozen proposed check

Static inspection found that GAP's sanctioned `PrimeBlocks` operation computes
ordinary block membership, block defects, and heights directly from the stored
ordinary table. CTblLib stores a 3-modular table for the quotient `U3(5)` but
does not store a separate `MBT("3.U3(5)",3)` record; this is not itself fatal,
because `PrimeBlocks` uses the exact ordinary table.

For explicit representatives, the standard installed `SU(3,5)` constructor
and `SylowSubgroup` can supply the principal representative. The center itself
supplies every defect-one representative. For a defect-two block, the stored
ordinary table has only one noncentral order-three class; if a character in
that block is nonzero there, Theorem 3.5 of the fixed paper puts a representative
`x` of that class in a conjugate defect group. Then `<Z,x>` has order nine and
equals that defect group. The frozen gate script checks every one of these
conditions and refuses to proceed if any representative is not certified in
this way.

No mathematical GAP computation has been run. A shell-level `gap -h` help probe
was invoked before the freeze; it produced no mathematical data and is not used
as evidence. The frozen proposed script is
`scratch/central_height_gate.g`; any invocation requires an explicit Lead
lease.

The final frozen script SHA-256 is
`29d9def1adadeebc51599baf5c697650d6ac5a21bc806e1bf84b853b3e0ceec4`;
its output path was absent before the lease request. The exact requested
once-only command is

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.g
```

- Work stop for compute-lease wait: `2026-08-17T23:12:37Z`; charged
  `00:05:18`; cumulative active time `00:48:34`. The installed-data gate is
  feasible on paper before increment minute 8, but no block/representative
  result is asserted until the sanctioned frozen run executes. Compute-queue
  and lease waiting are uncharged.

- Hand-proof polish resume: `2026-08-17T23:13:58Z`; inherited cumulative
  active time `00:48:34`. The central containment step above was expanded from
  the standard theorem to the exact Brauer-homomorphism/maximal-pair argument.
- Hand-proof polish stop: `2026-08-17T23:14:18Z`; charged `00:00:20`;
  cumulative active time `00:48:54`. Compute-lease waiting resumes uncharged.

## Leased run — operational failure before the first mathematical datum

- Work resume under Lead lease slot 2: `2026-08-17T23:16:51Z`; inherited
  cumulative active time `00:48:54`.
- The approved hash rechecked exactly, and the output path was absent.
- The exact authorized command was invoked once. The shell process returned 0
  after 1.44 seconds and used 141824 KiB maximum RSS, but this is not a successful
  mathematical run: GAP entered a break loop at the first
  `CharacterTable("3.U3(5)")` call because `-A` disabled package autoloading and
  the frozen script omitted `LoadPackage("CTblLib")`.
- The transcript contains no `TABLE_IDENTIFIER`, `BLOCK_VECTOR`,
  `BLOCK_DEFECTS`, `CHARACTER_HEIGHTS`, group model, defect representative,
  quotient exponent, or threshold row. Its SHA-256 is
  `aa856a1ea1db8116454a1725255738ed79ebfe91ab6745b49071f143a1868a68`.
- Lead's lease decision explicitly prohibited a patch or rerun. The slot-release
  report was written immediately. No other GAP invocation occurred.
- Research stop: `2026-08-17T23:17:17Z`; charged `00:00:26`; cumulative active
  time `00:49:20`.

The finite `SU_3(5)` bridge is therefore untested. This is an operational
`BLOCKER`, not a failed height threshold and not `STRATEGY_EXHAUSTED` for the
mathematical route. The universal source target remains open, and
`active_assignment_answered: no`.

## Final accounting and handoff

- Blocker packaging stop: `2026-08-17T23:18:41Z`; charged `00:01:24` after the
  research stop; final cumulative active time `00:50:44`.
- Total charged to this R6 increment: `00:07:28` from inherited cumulative
  `00:43:16`; `00:37:32` of the 45-minute allocation is returned unused.
- Outcome: `BLOCKER`; finite application untested; state `awaiting_lead`.
- No script patch, rerun, substitute defect group, further table, or second GAP
  invocation occurred.

## Lead-authorized environmental repair — uncharged

Lead subsequently superseded the no-rerun hold with authority for exactly one
source change and no mathematics: copy the checker to a revision-2 filename and
insert `LoadPackage("CTblLib");` before the first character-table call. The
failed script remains unchanged. Its transcript was preserved as
`scratch/central_height_gate_r1.out`, with unchanged SHA-256
`aa856a1ea1db8116454a1725255738ed79ebfe91ab6745b49071f143a1868a68`;
this makes the repaired script's existing `LogTo` path absent without a second
source change.

The exact `diff -u` between the failed checker and
`scratch/central_height_gate_r2.g` contains one added line only. The repaired
checker SHA-256 is
`711c8e8c88d3dd8414e8cb4a11898209d5555d2642d6fd1f9bd975b4cacdf301`,
and `scratch/central_height_gate.out` is absent. Per Lead, this repair uses no
additional research minutes. No repaired invocation has occurred; a fresh lease
has been requested.

## Repaired leased run — all finite thresholds pass

Lead granted a fresh slot-2 lease for exactly the repaired command. Work resumed
at `2026-08-17T23:26:41Z` from cumulative `00:50:44`; the approved hash matched
and the repaired output path was absent. The command was invoked exactly once and
exited zero in 2.57 seconds with 142208 KiB maximum RSS.

Observed exact summary:

```text
BLOCK_DEFECTS=[ 3, 2, 1, 1, 1, 1, 1 ]
NUMBER_BLOCKS=7
GROUP_ORDER=378000 CENTER_ORDER=3 SYLOW3_ORDER=27
ALL_HEIGHT_THRESHOLDS_PASS=true
```

There are 40 row records and seven block records. Block 1 has `|D/Z|=9`,
`exp(D/Z)=3`, threshold 3, and heights 0 or 1. Block 2 has `|D/Z|=3`,
`exp(D/Z)=3`, threshold 1, and all heights zero. Blocks 3--7 have `D=Z`,
trivial quotient, threshold 1, and all heights zero. Every row passes. The
explicit matrices, full membership, rowwise height table, and defect-group
identification are packaged in `findings.md`.

The output path is `scratch/central_height_gate.out`, SHA-256
`2b040684b4eeaae215276bfd9d6e83ef59b4bc74da904322b3784472c161c1cf`.
Slot 2 was released immediately through the file bus. Research stopped at
`2026-08-17T23:27:00Z`; charged `00:00:19`; cumulative active time
`00:51:03`. Packaging then continued from that cumulative point.

This successful repaired run supersedes the earlier operational `BLOCKER` as
the current strategy outcome. It does not erase the failed first transcript,
which remains preserved for audit.

## Final accounting

- Final packaging stop: `2026-08-17T23:32:47Z`; charged `00:05:47` after the
  successful-run research stop.
- Final cumulative active time: `00:56:50`.
- Total charged to `R6-CENTRAL-HEIGHT-STAR-U35`: `00:13:34`, beginning from
  inherited cumulative `00:43:16`.
- Unused time returned from the 45-minute increment: `00:31:26`.
- Current outcome: `PARTIAL_RESULT`, finite `SU_3(5)` prime-three structural
  bridge only, provisional pending fresh validation.
- Universal scope: open; `active_assignment_answered: no`.
- State: `awaiting_lead`; no further computation, table, prime, or strategy is
  authorized in this increment.
