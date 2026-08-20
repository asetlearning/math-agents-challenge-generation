---
title: "Verification — Kourovka 20.115 — L4(3) prime-2 block-defect bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "All six ordinary 2-blocks of centerless L4(3) satisfy the block-exponent condition, so Malle--Navarro--Tiep Proposition 3.2 gives Condition (1.1) at 2 for precisely the Conjecture-2.3 triples with derived subgroup L4(3)."
claimant: Problem-20.115-Proof
target_statement: "For every finite group G, every ordinary irreducible complex character chi of G, and every x in G, if chi(x) is nonzero then o(x)chi(1) divides |G|."
excluded_scopes: ["Brauer or modular characters as source characters", "rows with chi(x)=0", "reducible characters", "the solvable-only known result", "the weaker fourth-power/fifth-power bound", "odd-prime parts of the proposed nearly-simple bridge", "any bounded block calculation presented as a universal proof"]
target_object: "All admissible triples (G,chi,x) over every finite group in the canonical universal scope."
witness_object: "The six ordinary 2-blocks in CTblLib 1.3.7 data for centerless PSL_4(3), explicit subgroups in GAP's degree-40 projective-line model, and the Proposition-3.2 family of Conjecture-2.3 triples H with [H,H]=PSL_4(3)."
witness_equals_target: false
bounded_witness_identification: proven-for-the-GAP-PSL-model; replicated-from-Atlas-and-Modular-Atlas-library-data-for-the-character-and-block-tables
citation: "Malle--Navarro--Tiep, Zeros of characters and orders of elements in finite groups, arXiv:2605.04513v1, Proposition 3.2 and Theorem 3.5; GAP 4.12.1 Reference Manual, Section 50.2-12."
verification_method: "Rendered-source audit, line-by-line primary-PDF theorem audit, decomposition-matrix support components, Cartan elementary divisors, explicit permutation-subgroup checks, and independent 29-row 2-adic arithmetic."
tools_used: ["GAP 4.12.1", "CTblLib 1.3.7", "Python 3.12.3 for the state gate", "Poppler 24.02.0", "sha256sum"]
scope_answered: ["Bounded partial lemma: p=2 and Conjecture-2.3 triples with derived subgroup centerless PSL_4(3)"]
scope_not_answered: ["20.115/nonzero-character-order-divisibility universal scope", "odd-prime parts even for the stated nearly-simple family", "finite groups outside the stated Proposition-3.2 family"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
fixed_partial_verdict: replicated
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Verification — `L4(3)` prime-2 block-defect bridge

## Verdict

**The exact bounded prime-2 bridge is `status/replicated`.** A separately written
checker reconstructs the six blocks from connected components of the decomposition
matrix, reconstructs their defects from Cartan elementary divisors, verifies the
printed principal Sylow representative and the printed order-4 element inside the
documented `PSL(4,3)` permutation model, and independently recomputes all 29
character defects. Its results agree with every claimed row and inequality.

The delicate block-2 step is mathematically valid: Theorem 3.5, rather than a
same-order guess, places the explicit class-`4a` element in a conjugate of a block-2
defect group. Both cyclic subgroup and defect group then have order four, so they
are equal. Proposition 3.2 also applies with exactly the restrictions stated below.

**The canonical revision-1 scope remains `status/conjectured`.** This lemma supplies
only the (2)-part of the target divisibility for a proper nearly-simple family.
Thus `witness_equals_target: false` and `active_assignment_answered: no`.

## The claim

Let (L=\operatorname{PSL}_4(3)), (p=2), and let (B) range over the ordinary
(2)-blocks of (L). The bounded claim is

\[
   \exp(D_B)\leq 2^{\operatorname{def}_2(\theta)}
   =\left(\frac{|L|}{\theta(1)}\right)_2
   \quad(\theta\in\operatorname{Irr}(B)).
\]

Since (Z(L)=1), this is both Condition ((\ddagger)) and Condition
((\ddagger^\star)) of the cited paper. Proposition 3.2 is then claimed to imply

\[
  o(h)_2\mid\left(\frac{|H|}{\chi(1)}\right)_2
\]

for every triple ((H,h,\chi)) satisfying the paper's condition ((*)) and having
([H,H]=L). No odd-prime or universal conclusion is claimed.

## Scope, revision, and clause matrix

The canonical record is `20.115/nonzero-character-order-divisibility`, revision 1.
I visually inspected rendered source page 161. It asks whether, for every finite
(G), ordinary complex irreducible (\chi), and (x\in G), exact nonvanishing
(\chi(x)\ne0) forces (o(x)\mid |G|/\chi(1)).

| source clause | active? | bounded claim | remainder |
|---|---:|---|---|
| universal exact divisibility | yes | one prime for a proposition-defined family with derived subgroup (L_4(3)) | every other prime/family and the universal quantifier |
| known solvable case | no, context | not used | excluded |
| weaker ((o(x)\chi(1))^4\mid |G|^5) | no, context | not used | excluded |

## Constraint-and-conclusion matrix

This matrix was reconstructed from the rendered source, not inherited from the
claim-check.

| constraint id | role | requirement | independent result |
|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | **not established**; the theorem bridge has a strict family and prime restriction |
| `20.115-G-finite` | admissibility | (G) finite | pass for the bounded groups (H) in Conjecture 2.3; (L=\operatorname{PSL}_4(3)) is finite of order (6065280) |
| `20.115-chi-complex-irreducible` | admissibility | ordinary (\chi\in\operatorname{Irr}(G)) | pass in the bounded theorem: Proposition 3.2 and all block rows use ordinary `Irr` characters |
| `20.115-x-in-G` | admissibility | (x\in G), exact order | pass in the bounded theorem for (h\in H); the conclusion concerns exact quotient order, which becomes exact (o(h)) because (Z(H)=1) |
| `20.115-character-value-nonzero` | admissibility | exact (\chi(x)\ne0) | pass as the hypothesis (\chi(h)\ne0) in Conjecture 2.3; exact value (16\ne0) is used separately in the block-2 certificate |
| `20.115-order-degree-divisibility` | target conclusion | full integer divisibility | proved only at the prime 2 for the bounded family, conditional on the replicated library data; not universal |

The repaired claim-check contains all six IDs, explicitly marks a bounded partial
claim and `active_assignment_answered: false`, and the state checker reports zero
errors. The matrix above independently reaches the same scope result.

## Target versus witness and circularity

- **Source/active target:** all admissible triples over every finite group.
- **Finite data witness:** the ordinary and characteristic-2 tables stored under
  `L4(3)` and `L4(3)mod2`, plus explicit permutations in `PSL(4,3)`.
- **Theorem family:** finite (H) satisfying every Conjecture-2.3 hypothesis and
  ([H,H]=L).
- **Witness equals universal target:** false.

GAP Reference Manual §50.2-12 states that `PSL(d,q)` constructs a group isomorphic
to the determinant-one (d\times d) matrices modulo their center; without an
explicit filter it returns the action on projective lines. Thus `PSL(4,3)` is the
claimed group model, not merely a group with a suggestive name or order. Its degree
is (40=(3^4-1)/(3-1)), and the exact order formula gives

\[
 |\operatorname{PSL}_4(3)|
 =\frac{3^6(3^2-1)(3^3-1)(3^4-1)}{\gcd(4,3-1)}
 =6065280=2^7 3^6\cdot5\cdot13.
\]

The runtime model has center size 1 and is simple. CTblLib identifies its ordinary
table as `L4(3)`, with Atlas origin; its stored source record also names
`psl(4,3)`. The modular table reports Modular-Atlas origin. These tables predate
and are independent of the desired inequality, so the check is not true by
construction. Both claimant and Validator nevertheless read the same installed
library data; that shared provenance is the reason for the `replicated`, rather
than `proven`, finite-data verdict.

## Exact audit of the cited paper

The fixed 28-page artifact has SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.
The relevant definitions and both results were checked in the rendered PDF as well
as extracted text.

### Condition ((*)), Conjecture 2.3, and the block conditions

The paper's ((H,h,\chi)) condition requires all of the following:

1. (H) is finite and (h\in H).
2. (L=[H,H]) is quasi-simple.
3. (Z(L)=Z(H)) is cyclic.
4. (H=L\langle h\rangle).
5. (\chi\in\operatorname{Irr}(H)) is faithful and (\chi(h)\ne0).

Conjecture 2.3 asks, under these hypotheses, for

\[
 o(hZ(H))\mid |H:Z(H)|/\chi(1).
\]

For a (p)-block (B) with defect group (D), Condition ((\ddagger)) is

\[
 \exp(D)\leq (|G|/\theta(1))_p
 \quad\text{for every }\theta\in\operatorname{Irr}(B),
\]

while ((\ddagger^\star)) replaces (D) by (D/Z(G)_p) and (|G|) by
(|G:Z(G)|). The paper explicitly says the two coincide when (p\nmid |Z(G)|).

### Theorem 3.5

The exact statement is: for a (p)-block (B) of a finite group (G), a chosen
defect group (D), and a (p)-element (x\in G), (x) lies in some conjugate of
(D) if and only if at least one ordinary (\chi\in\operatorname{Irr}(B)) is
nonzero at (x). There is no solvability, simplicity, faithfulness, or block-type
hypothesis.

Every hypothesis needed here is met:

- (G=L=\operatorname{PSL}_4(3)) is finite and (p=2).
- (B_2) is the reconstructed second ordinary (2)-block and has defect 2.
- The explicit (x) has order 4, hence is a (2)-element.
- Row 16 belongs to (B_2) and has exact value (\chi_{16}(4a)=16\ne0).
- The explicit (x) is the unique table class with the pair
  `(order, centralizer)=(4,1440)`, namely `4a`.

Therefore Theorem 3.5 puts (x) in a conjugate (D^g) of a block-2 defect group.
The defect is 2, so (|D^g|=2^2=4). Since (|\langle x\rangle|=4) and
(\langle x\rangle\leq D^g), equality follows:

\[
 D^g=\langle x\rangle\cong C_4.
\]

This is the required theorem-based certificate. Finding a subgroup of order four
without this inclusion would not identify it as a defect group.

### Proposition 3.2

The exact proposition starts with **(H) as in Conjecture 2.3**. If every
(p)-block of (L=[H,H]) satisfies ((\ddagger^\star)), it concludes that
((\ddagger^\star)) holds at (p) for every (\chi\in\operatorname{Irr}(H))
whose restriction to (L) is irreducible, and consequently Conjecture 2.3 holds
for (H) at (p).

Its proof uses a defect group (D_0\leq D) below the restricted character and
(|D:D_0|\leq |H:L|_p), obtaining

\[
o(hZ(H))_p
 \leq \exp(D/Z(H)_p)
 \leq |H:L|_p\exp(D_0/Z(L)_p)
 \leq \left(\frac{|H:Z(H)|}{\chi(1)}\right)_p.
\]

The last sentence invokes the earlier observation that, under Conjecture 2.3's
hypotheses, (\chi(h)\ne0) and (H=\langle L,h\rangle) force
(\chi|_L\) irreducible.

For the present (L), (Z(L)=1), so ((\ddagger)=(\ddagger^\star)). Because the
proposition assumes (Z(H)=Z(L)), it also forces (Z(H)=1). Hence its conclusion
is exactly

\[
 o(h)_2\mid\left(\frac{|H|}{\chi(1)}\right)_2.
\]

The claimant's application is therefore correct **only with all of the stated
Conjecture-2.3/((*)) hypotheses retained**. It is not a statement about every
finite group having derived subgroup (L) under arbitrary character hypotheses.

## Independent reconstruction of the six blocks

The claimant used `PrimeBlocks`. The Validator instead took the (29\times12)
decomposition matrix of `L4(3)mod2`, formed connected components of its bipartite
ordinary-row/Brauer-column support graph, and obtained exactly six components.
For each component it formed (C=D^\mathsf{T}D). By the standard Cartan elementary-
divisor theorem, the largest elementary divisor is the order of a defect group.

| block | ordinary rows | Brauer columns | Cartan elementary divisors | defect |
|---:|---|---|---|---:|
| 1 | 1--15, 20--22, 27--29 | 1--7 | (1,1,1,8,8,8,128) | 7 |
| 2 | 16--19 | 8 | (4) | 2 |
| 3 | 23 | 9 | (1) | 0 |
| 4 | 24 | 10 | (1) | 0 |
| 5 | 25 | 11 | (1) | 0 |
| 6 | 26 | 12 | (1) | 0 |

This independently reconstructs the claimant's row membership and defects from
the decomposition matrix. It is a different computation path, though the matrix
itself remains Modular-Atlas/CTblLib data.

## Explicit defect groups and exponents

### Principal block

Block 1 contains ordinary row 1, the trivial character, so it is the principal
block and its defect groups are Sylow (2)-subgroups. In the documented degree-40
model, the claimant's three printed permutations are

```text
(2,10)(3,8)(4,9)(5,6)(14,15)(17,40)(18,39)(19,38)(20,26)(21,28)(22,27)(23,25)(29,36)(30,35)(31,37)(33,34)
(2,26)(3,28)(4,27)(5,34)(6,33)(7,32)(8,21)(9,22)(10,20)(11,13)(14,15)(17,40)(18,38)(19,39)(30,31)(35,37)
(1,39)(2,8)(3,15)(4,27)(5,11)(6,24)(7,18)(9,36)(10,33)(12,21)(13,30)(14,34)(16,35)(17,31)(19,20)(22,23)(25,29)(26,37)(28,32)(38,40)
```

All lie in `PSL(4,3)`. They generate a subgroup (D_1) of order (128=|L|_2),
so (D_1) is Sylow. Exhaustive enumeration of its 128 elements gives

```text
order 1: 1 element; order 2: 43; order 4: 68; order 8: 16.
```

Thus (\exp(D_1)=8) exactly.

### Block 2

The explicit element is

```text
(1,11,12,13)(2,14,20,17)(3,35,34,39)(4,29,27,25)(5,37,28,19)(6,31,21,38)(7,16,32,24)(8,30,33,18)(9,36,22,23)(10,15,26,40)
```

It lies in `PSL(4,3)` (indeed in the displayed (D_1)), has order 4, and its
ambient centralizer has order 1440. The library table has exactly one class with
those two invariants: position 8, named `4a`. Row 16 is in block 2 and has value
16 on that class. The Theorem-3.5 chain above proves that
(D_2=\langle x\rangle\cong C_4) is a valid conjugate defect-group representative,
with exponent 4.

### Blocks 3--6

Each has defect zero, hence defect-group order (2^0=1). The unique representative
is the trivial subgroup, with exponent 1.

The certified exponent list is therefore

```text
[8, 4, 1, 1, 1, 1].
```

## All 29 ordinary-character defects

Here

\[
\operatorname{def}_2(\theta)
=v_2(|L|/\theta(1))=7-v_2(\theta(1)).
\]

The independent script computes this by repeated exact division of each integral
codegree, rather than by copying `PrimeBlocks.height` or the claimant's valuations.
Every row 1--29 appears exactly once:

| rows | block | degree | (\operatorname{def}_2\) | (2^{\operatorname{def}_2}) | (\exp(D_B)) | result |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 7 | 128 | 8 | pass |
| 2, 3 | 1 | 26 | 6 | 64 | 8 | pass |
| 4 | 1 | 39 | 7 | 128 | 8 | pass |
| 5 | 1 | 52 | 5 | 32 | 8 | pass |
| 6, 7 | 1 | 65 | 7 | 128 | 8 | pass |
| 8 | 1 | 90 | 6 | 64 | 8 | pass |
| 9, 10 | 1 | 234 | 6 | 64 | 8 | pass |
| 11--13 | 1 | 260 | 5 | 32 | 8 | pass |
| 14 | 1 | 351 | 7 | 128 | 8 | pass |
| 15 | 1 | 390 | 6 | 64 | 8 | pass |
| 16--19 | 2 | 416 | 2 | 4 | 4 | pass |
| 20 | 1 | 468 | 5 | 32 | 8 | pass |
| 21, 22 | 1 | 585 | 7 | 128 | 8 | pass |
| 23 | 3 | 640 | 0 | 1 | 1 | pass |
| 24 | 4 | 640 | 0 | 1 | 1 | pass |
| 25 | 5 | 640 | 0 | 1 | 1 | pass |
| 26 | 6 | 640 | 0 | 1 | 1 | pass |
| 27 | 1 | 729 | 7 | 128 | 8 | pass |
| 28 | 1 | 780 | 5 | 32 | 8 | pass |
| 29 | 1 | 1040 | 3 | 8 | 8 | pass |

The tight rows are 16--19 and 29. All 29 inequalities hold.

## Library output versus mathematical certification

| item | status of this audit |
|---|---|
| Exact meaning and applicability of Theorem 3.5 | checked from the primary artifact; the block-2 inclusion/equality argument is mathematically valid |
| Exact meaning and applicability of Proposition 3.2 | checked from the primary artifact; the prime-2 conclusion follows with all Conjecture-2.3 hypotheses retained |
| GAP permutation model | identified by the documented constructor, not by order/name alone; explicit subgroup calculations are exact finite computations |
| Ordinary table, Brauer table, decomposition matrix, class labels/values | pre-existing Atlas/Modular-Atlas CTblLib data; independently queried and cross-checked, but not rederived from a presentation |
| Six-block partition, Cartan defects, 29 valuations and inequalities | independently recomputed from that library data and explicit group certificates; agrees with the claimant |
| Universal Kourovka statement | not established |

Thus the logical bridge is certified conditional on the exact finite data, while
the finite data reach the protocol's computation-replication threshold, not the
first-principles proof threshold.

## Evidence

### Claim-check gate

Command:

```text
python3 _meta/scripts/kourovka-state-check.py
```

Relevant terminal summary:

```text
Kourovka state check: 11 scope(s), 17 roster(s), 11 v2 board row(s), 5 claim check(s), 0 benchmark manifest(s), 0 error(s), 7 warning(s).
```

The seven warnings concern legacy roster/revision records outside this claim; no
state-check error was reported.

### Frozen independent run

- Formal lease decision:
  `Agents/Kourovka/bus/archive/2026-08-17T214215Z__Lead__DECISION__lease-l43-2block-validator.md`
  (slot 2, one invocation, 45-second cap, under 300 MiB).
- Manifest:
  `Agents/Kourovka/problems/20.115/verification/2026-08-17T212730Z-l43-2block-validator-manifest.md`.
- Script:
  `Agents/Kourovka/problems/20.115/verification/scratch/l43_2block_validator.g`.
- Script SHA-256:
  `3067ca1baa200701f3868dda1ee3974de49bc6b6b7d70c4eb7665d14a84c888c`.
- Verbatim output:
  `Agents/Kourovka/problems/20.115/verification/scratch/l43_2block_validator_leased_slot2.out`.
- Output SHA-256:
  `7dc2e75352faf3dde83fcc2fd1cbea104c004b34c1b7bd8f117621e014318bd9`.

Exact command:

```text
timeout 45s gap -q -b Agents/Kourovka/problems/20.115/verification/scratch/l43_2block_validator.g
```

The checker hash was verified before execution. The one permitted invocation exited
0 in 2.1578 seconds. Slot 2 was released immediately by a timestamped `REPORT`.
The transcript contains 29 `ROW=` records, six `BLOCK=` records, no failed row,
and ends:

```text
ALL_29_INEQUALITIES_PASS=true
ALL_ASSERTIONS_PASS=true
```

GAP emitted one static top-level closure warning for the already-assigned variable
`newcols`; evaluation proceeded, every structural assertion was reached, and the
process exited zero. The full warning and output are preserved verbatim.

### Key exact output

```text
GAP_VERSION=4.12.1
CTBLLIB_VERSION=1.3.7
TABLE_ID=L4(3) TABLE_ORDER=6065280 NIRR=29 NBRAUER=12
MODEL=PSL(4,3)_PROJECTIVE_LINES DEGREE=40 ORDER=6065280 CENTER=1 SIMPLE=true
RECONSTRUCTED_BLOCK_COUNT=6
D1_GENERATORS_IN_G=true D1_SIZE=128 D1_EXPONENT=8
X_IN_G=true X_IN_D1=true X_ORDER=4 X_CENTRALIZER=1440
MATCHING_TABLE_CLASSES=[ 8 ] CLASS_NAME=4a
BLOCK2_SUPPORT_ROW=16 VALUE_ON_4A=16 ROW_BLOCK=2
ALL_29_INEQUALITIES_PASS=true
ALL_ASSERTIONS_PASS=true
```

The claimant's different script has SHA-256
`5504e55a8ca78b0f3e73d776b8f0c3310e024c5b473d9d7b19288388938fa8bc`.

## Why this verdict

The claimant and Validator use materially different block reconstructions:
`PrimeBlocks` versus decomposition-support components and Cartan elementary
divisors. They agree on all six blocks, every ordinary-row membership, every block
defect, both nontrivial defect-group exponents, all 29 character defects, and all
29 inequalities. The explicit permutation certificates also pass, and the two
cited paper results have exactly the hypotheses needed for the stated bounded
implications.

This meets `status/replicated` for the fixed partial lemma. It does not meet
`status/proven` from first principles because the character and decomposition
tables were not independently derived from the group, and it cannot promote the
universal scope because its witness domain is strictly smaller.

## What is NOT established

- The universal assertion in Kourovka 20.115 is neither proved nor refuted.
- No odd-prime part is established by this bridge, even for the stated (H).
- Nothing is proved for groups or characters omitting any Conjecture-2.3/((*))
  hypothesis, including faithfulness, (H=L\langle h\rangle), or
  (Z(H)=Z(L)).
- Condition ((\ddagger)) is only sufficient here; failure of that condition in
  another block would not be a counterexample to Wilde's conjecture.
- The Atlas ordinary table and Modular-Atlas decomposition matrix were not
  reconstructed from a presentation or representations of (\operatorname{PSL}_4(3)).

## What would upgrade it

For a first-principles proof of the finite block lemma, supply an independently
checkable derivation/certificate for the ordinary and modular block data from the
group model. To answer the active assignment, one must instead prove the full
integer divisibility for every finite group (equivalently finish every required
prime/family after the paper's reduction) or exhibit and verify one admissible
counterexample.
