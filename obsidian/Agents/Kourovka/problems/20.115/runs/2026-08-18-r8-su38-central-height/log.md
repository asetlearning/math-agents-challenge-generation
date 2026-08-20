---
title: "Run log — Kourovka 20.115 — R8 SU3(8) central height"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
strategy: R8-SU38-CENTRAL-HEIGHT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Run log — `R8-SU38-CENTRAL-HEIGHT`

## Active target and boundary

Universal target: for every finite group `G`, every ordinary complex
irreducible character `chi`, and every `x in G`,

```text
chi(x) != 0  =>  o(x) chi(1) divides |G|,
```

where `o(x)` is the exact element order.  This run is authorized to test only
the bounded auxiliary datum `L=SU_3(8)=3.U3(8)` at `p=3`, with
`a=v_3(8+1)=2`.  It may at most establish the Proposition 3.2 bridge with all
of that proposition's hypotheses.  Brauer characters, reducible characters,
zero values, a prime-part conclusion, and finite evidence do not answer the
universal target.

Scope source and all six constraint rows are locked by
`Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json`,
revision 1.  The independently reviewed `q=5` bridge and the prior conditional
family reduction were read in full.  The present assignment forbids web use;
no external search is performed.  The canonical source transcription and
independent scope audit are already recorded as passed in the scope record.

## Strategy portfolio

1. **Exact installed-data gate (selected).** Resolve the literal CTblLib table
   identity, order, center, availability of ordinary 3-block data, and the exact
   height/defect inequality.  Negative outcome: an absent table/block field or
   unjustifiable defect representative kills this one-datum strategy.
2. **Bounded frozen checker (conditional).** Only after the gate passes, write
   and hash one checker that enumerates every ordinary 3-block, derives every
   character height from degrees and defects, constructs explicit defect groups,
   computes every quotient exponent, and tests all thresholds.  Request a Lead
   lease before its sole evidentiary run.
3. **Theoretical mode.** Use only the reviewed central-subgroup/Brauer-pair
   argument and height identity.  Do not assume the missing generic
   `SU_3(q)` block theorem.
4. **Certificate plan.** Preserve exact GAP/CTblLib versions and table identifier,
   all block membership/defect rows, explicit matrix or permutation generators for
   each distinct defect type, quotient exponents, all character-height rows, the
   frozen checker hash, verbatim output hash, and the exact retained hypotheses of
   Proposition 3.2.

## Active-time ledger

- `2026-08-18T00:35:01Z` — research start; inherited official cumulative active
  time `01:04:05`; run charge `00:00:00/00:35:00`.
- `2026-08-18T00:41:44Z` — research stop for Lead lease; run charge
  `00:06:43/00:35:00`; official cumulative active time `01:10:48`.

## Exact installed-data and structural gate

The light probe

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_identity_probe.g
```

first exposed a local variable-name error (`Z` is read-only in GAP) after the
table data printed.  After changing only that variable name to `Cen`, the second
invocation exited zero in `2.57` seconds with maximum RSS `142080` KB and printed:

```text
GAP_VERSION=4.12.1
CTBLLIB_VERSION=1.3.7
TABLE_ID=3.U3(8)
TABLE_ORDER=16547328
NR_CLASSES=82
NR_IRR=82
NR_3BLOCKS=10
DEFECT_VECTOR=[ 5, 2, 2, 2, 1, 1, 1, 1, 1, 1 ]
MATRIX_GROUP_ORDER=16547328
CENTER_ORDER=3
CENTER_STRUCTURE=C3
QUOTIENT_ORDER=5515776
END_SU38_IDENTITY_PROBE
```

Thus the installed ordinary table is literally `3.U3(8)`, its order equals
the standard matrix group `SU(3,8)` and the formula
`8^3(8^3+1)(8^2-1)=16547328`, and its full center has order
`gcd(3,8+1)=3`.  `PrimeBlocks(t,3)` is installed and returns ten ordinary
3-blocks with the displayed defects.  This is an identity/availability gate,
not a universal result.

The second light probe enumerated only the 3-power table classes and a Sylow
subgroup.  It exited zero in `3.90` seconds with maximum RSS `142208` KB.  It
found center class positions `1,2,3`; six order-nine classes `9a`--`9f` with
centralizer order `4536`; nine further order-nine classes with centralizer
order `81`; a Sylow subgroup `P` of order `243`, exponent `9`, containing the
center; and

```text
|P/Z|=81, exp(P/Z)=9.
```

Every one of blocks 2, 3, and 4 has nonzero ordinary-character support on each
of classes `9a`--`9f`.  Blocks 5--10 have defect one.

An attempted hand diagonal matrix of order nine was not an element of GAP's
chosen unitary form, and its full-group centralizer computation reached the
45-second timeout.  It is quarantined and is not evidence.  A replacement
probe chose directly inside `P` an order-nine matrix whose minimal polynomial
over `GF(64)` has degree two.  It exited zero in `2.30` seconds with maximum
RSS `141824` KB and found 18 such elements; the first has nontrivial central
cube and generates a cyclic order-nine subgroup containing `Z`.

Because the element order is prime to characteristic two, it is semisimple.
Minimal-polynomial degree two in dimension three gives two distinct eigenvalues
with multiplicities `2+1`.  Its eigenspaces are nondegenerate for the unitary
form, so its centralizer in `SU_3(8)` is
`S(U_2(8) x U_1(8))`, of order

```text
|U_2(8)| = 8(8-1)(8+1)^2 = 4536.
```

It therefore lies in one of table classes `9a`--`9f`.  The reviewed Theorem
3.5 support criterion then places it in a conjugate defect group for each of
blocks 2--4.  Since those blocks have defect two and the element has order
nine, the cyclic subgroup it generates is an explicit representative (after
conjugation) for each; its quotient by `Z` has order and exponent three.
Defect-one blocks have representative exactly `Z` by central containment.
The principal block has representative `P`.

## Exact defect-height criterion

For any ordinary 3-block of `L`, the reviewed central Brauer-pair argument gives
`Z<=D`.  Write `|L|_3=3^A`, `|D|=3^d`,
`|Z|=3`, `exp(D/Z)=3^e`, and let `theta` have height `h`.  Here
`A=v_3(16547328)=5`.  From

```text
theta(1)_3 = 3^(A-d+h)
```

one obtains the exact equivalence

```text
exp(D/Z) <= (|L:Z|/theta(1))_3
iff 3^h <= |D/Z|/exp(D/Z)
iff h <= d-1-e.
```

The explicit quotient data therefore give threshold powers
`[9,1,1,1,1,1,1,1,1,1]`: principal-block height at most two, and height zero
in every other block.

## Frozen checker and lease hold

The checker was frozen without an evidentiary run at
`scratch/su38_central_height_frozen.g`, 192 lines, 7433 bytes, SHA-256
`1f0610791c3cd7f7671804123cbc42076ea38091316807ac734b85c185f89d3b`.
It will audit all ten blocks, all 82 ordinary characters, degree-derived
defects and heights, the three explicit defect types and quotient exponents,
and every threshold.  A lease request was sent to Lead.  Waiting time is not
charged.

## Leased frozen audit

- `2026-08-18T00:46:28Z` — Lead's slot-2 lease checked current; research
  resumed at run charge `00:06:43`, official cumulative `01:10:48`.

The frozen hash still matched and its output path was absent.  The exact
authorized command was invoked once.  It exited `1` in `3.87` seconds with
maximum RSS `141952` KB.  This was an intentional mathematical-gate exit after
all 82 rows printed, not an execution or data-availability error.

The ten defect representatives and quotient exponents passed.  The threshold
vector was

```text
[9,1,1,1,1,1,1,1,1,1].
```

Exactly six rows failed: principal-block rows 35--40, all of degree `189`,
`v_3(degree)=3`, and height `3`, have

```text
3^h=27 > 9=|P/Z|/exp(P/Z).
```

The other 76 rows pass.  Therefore Condition `(‡*)` does not hold for every
ordinary 3-block of `SU_3(8)`.  The conjectural generic input isolated by the
previous family run is already false at this next datum: the principal-block
maximum height is 3, not at most `v_3(9)=2`.  This kills the named family-bridge
strategy at `q=8`; it does not refute Proposition 3.2 and implies nothing by
itself about the universal source conclusion.

Complete output is 294 lines and 14508 bytes, SHA-256
`2e8545a02303a51cb63261f1ead9a52af086aa3b0bd4192de070992e6b2e8768`.
The lease was released immediately by file-bus report.  The bounded result is
packaged in `findings.md` for independent Validator replay.

- `2026-08-18T00:50:37Z` — research/reporting stop; second charged interval
  `00:04:09`; total run charge `00:10:52/00:35:00`; official cumulative active
  time `01:14:57/03:00:00`.  Outcome `PARTIAL_RESULT`; named strategy stopped
  in `awaiting_lead`; `active_assignment_answered: no`.
