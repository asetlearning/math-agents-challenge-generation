---
title: "Problem 20.115 L4(3) prime-2 block-defect bridge log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
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

# L4(3) prime-2 block-defect bridge

## Active-time ledger

- Work start: `2026-08-17T20:58:51Z`; inherited cumulative active time: `00:27:45`. This bounded proof bridge has at most 40 active minutes and an eight-active-minute prerequisite kill.

## Locked target and finite bridge

- Exact source target: for finite `G`, ordinary irreducible complex `chi`, and `x in G`, exact `chi(x) != 0` should imply the integer divisibility `o(x)chi(1) | |G|`.
- Frozen finite object/prime: the centerless simple group represented by the ordinary table `L4(3)`, at `p=2`.
- Bridge prerequisite: exact ordinary 2-block membership and an explicit defect-group representative for every block, not merely its order. A failure of `exp(D_B) <= 2^def(chi)` would kill only this sufficient bridge, not refute the source conjecture.

## Prerequisite gate — passed within eight active minutes

- `PrimeBlocks(CharacterTable("L4(3)"),2)` returned exact ordinary-row
  membership and block defects `[7,2,0,0,0,0]` for six blocks.
- GAP's sanctioned constructor `PSL(4,3)` returned the standard degree-40
  permutation group of order `6065280`, center size `1`, and `IsSimpleGroup=true`.
- `SylowSubgroup(g,2)` gave an explicit principal-block defect group of order
  `128` and exponent `8`.
- The four defect-zero blocks have the explicit trivial representative.
- For the sole remaining defect-2 block, exact table row 16 is nonzero on class
  `4a`: `chi_16(4a)=16`. The table class is uniquely specified among order-4
  classes by centralizer order `1440`. An explicit order-4 permutation with
  centralizer `1440` was found inside the fixed Sylow subgroup. By Theorem 3.5 of
  the reviewed paper it lies in a conjugate of the block's defect group; since
  both cyclic subgroups have order four, its generated subgroup is an explicit
  defect-group representative.
- Gate completion timestamp: `2026-08-17T21:02:16Z`, 3 minutes 25 seconds after
  the work start and therefore before the eight-active-minute hard kill.

## Exact inequality check

Script:
`Agents/Kourovka/problems/20.115/runs/2026-08-17-r4-l43-2block-defect-bridge/scratch/bridge.g`.

Command:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 50s gap -q Agents/Kourovka/problems/20.115/runs/2026-08-17-r4-l43-2block-defect-bridge/scratch/bridge.g
```

Observed summary:

```text
BLOCK_DEFECTS=[ 7, 2, 0, 0, 0, 0 ]
CLASS4A_UNIQUENESS_POSITIONS=[ 8 ] NAME=4a ORDER=4 CENTRALIZER=1440
BLOCK2_SUPPORT_ROW=16 CLASS_POS=8 VALUE=16 NONZERO=true
BLOCK 1 ... D_SIZE=128 D_EXPONENT=8
BLOCK 2 ... D_SIZE=4 D_EXPONENT=4
BLOCK 3 ... D_SIZE=1 D_EXPONENT=1
BLOCK 4 ... D_SIZE=1 D_EXPONENT=1
BLOCK 5 ... D_SIZE=1 D_EXPONENT=1
BLOCK 6 ... D_SIZE=1 D_EXPONENT=1
ALL_BLOCK_EXPONENT_VS_CHARACTER_DEFECT_PASS=true
ELAPSED=2.14 MAX_RSS_KB=142208
```

The full terminal output listed each of the 29 ordinary rows with its block,
degree, exact character 2-defect, block-defect exponent, and passing inequality.
The exact representatives and complete grouped row table are in `findings.md`.
No process approached the heavy-compute threshold and no lease was needed.

## Proposition 3.2 bridge

For centerless `L=L4(3)`, Conditions `(double-dagger)` and
`(double-dagger-star)` coincide. Proposition 3.2 therefore makes the finite lemma
imply Condition (1.1) at 2 for every triple `(*)` with derived subgroup `L`:

`o(h Z(H))_2 | (|H:Z(H)|/chi(1))_2`.

Here `Z(H)=Z(L)=1`, so this becomes
`o(h)_2 | (|H|/chi(1))_2`. This is a bounded prime-2 nearly-simple reduction, not
the universal source conclusion.

## Outcome and stop

- Outcome: `PARTIAL_RESULT`, pending Validator reproduction.
- Findings: `Agents/Kourovka/problems/20.115/runs/2026-08-17-r4-l43-2block-defect-bridge/findings.md`.
- Work stop: `2026-08-17T21:05:52Z`.
- Charged active time for this bridge: `00:07:01`.
- New cumulative active time: `00:34:46` from the inherited `00:27:45`.
- Unused time returned from the 40-minute allowance: `00:32:59`.
- Universal scope remains open; the lane does not self-park.

## Post-stop Lead gate clarification and ledger correction

- Administrative work resumed at `2026-08-17T21:07:50Z` to process Lead's
  `defect-group-identification-gate` decision. No new mathematical route was
  started.
- The required exact block-theoretic certificate was already present within the
  original prerequisite window: Theorem 3.5 puts the explicit class-`4a` element
  inside a conjugate of the block-2 defect group, and equality follows because
  both the generated subgroup and that defect group have order four. A clarifying
  `REPORT` was sent to Lead.
- Administrative work stopped at `2026-08-17T21:08:52Z`, adding `00:01:02`.
- Corrected total charged time for this bridge turn: `00:08:03`.
- Corrected cumulative active time: `00:35:48`.
- Corrected unused time returned from the 40-minute allowance: `00:31:57`.
