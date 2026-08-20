---
title: "Problem 19.30 counterexample-direction log — cycle 1"
problem_id: "19.30"
direction: counterexample
cycle: 1
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/characters
  - topic/kourovka
  - project/kourovka
  - status/draft
---

# Problem 19.30 — counterexample direction

## Active-time ledger

- 2026-08-12T05:13:13Z — work started; cumulative active time: 0 minutes.
- 2026-08-12T05:15:18Z — source/staleness gate and initial tool check completed; cumulative active time: 2 minutes.

## Inbox and direction gate

- Inbox `Agents/Kourovka/bus/inbox/Problem-19.30/` was read first and contained no messages.
- Assignment explicitly parks the paired proof direction. Only the counterexample direction is running.

## Source transcription

Source: configured Kourovka PDF, 19th Issue (2018), printed page 134 (the corpus record says page 133, an apparent one-page indexing mismatch). I inspected the rendered page at 180 dpi, not merely its extracted text.

> **19.30.** An element \(g\) of a finite group \(G\) is said to be vanishing if \(\chi(g)=0\) for some irreducible complex character \(\chi\in\operatorname{Irr}(G)\). Must a finite group and a finite simple group be isomorphic if they have equal orders and the same set of orders of vanishing elements?
>
> M. Foroudi Ghasemabadi, A. Iranmanesh.

`source_transcription_checked: yes`

In my own words: for a finite group \(X\), let \(\operatorname{Vo}(X)\) be the set of element orders occurring among conjugacy classes on which at least one ordinary irreducible complex character is zero. Given an arbitrary finite group \(G\) and a finite simple group \(S\), does \(|G|=|S|\) and \(\operatorname{Vo}(G)=\operatorname{Vo}(S)\) force \(G\cong S\)? The counterexample target is therefore an explicit nonsimple \(G\) and simple \(S\) of the same order with exactly equal sets \(\operatorname{Vo}\).

## Staleness check

Corpus record (`kourovka-20-corpus.jsonl`): `answered: false`, `has_editor_comment: false`, `has_later_comment: false`.

The configured current PDF still prints 19.30 without a star, answer, or later editor comment. Web searches made on 2026-08-12:

- exact queries `"Kourovka" "19.30" vanishing elements`, `"Problem 19.30" "Kourovka Notebook"`, and `"same set of orders of vanishing elements"` found the problem and partial affirmative results, but no general proof or counterexample;
- proposer/key-term query `Foroudi Ghasemabadi Iranmanesh "vanishing" element orders simple group` found the originating conjecture and later papers treating specified families;
- arXiv queries for `"orders of vanishing elements" finite simple group characterization` and the proposers found further family recognition results and unrelated structural work, but no closure of the general conjecture.

Relevant partial results located:

- M. Foroudi Ghasemabadi, A. Iranmanesh, M. Ahanjideh, *A new characterization of some families of finite simple groups*, Rend. Sem. Mat. Univ. Padova 137 (2017), 57–74, DOI 10.4171/RSMUP/137-3: affirmative for sporadic groups, alternating groups, \(L_2(p)\) for odd prime \(p\), and finite simple \(K_n\)-groups for \(n\in\{3,4\}\).
- M. Khatami and A. Babai, *Recognition of some families of finite simple groups by order and set of orders of vanishing elements*, Czech. Math. J. 68 (2018), 121–130: additional Suzuki and \(F_4\) families under number-theoretic hypotheses.
- S. Askary, *Characterization of some finite simple groups by the set of orders of vanishing elements and order*, Ukrainian Math. J. 73 (2022): further twisted orthogonal families under prime hypotheses.
- S. Zhang, *A new characterization of \(E_8(p)\) via its vanishing elements*, arXiv:2401.00767: a stronger recognition result for many \(E_8(p)\), not a general resolution.

Gate conclusion: no evidence that the exact general question is stale; bounded counterexample screening may proceed.

## Initial computational scope

- GAP is installed. SmallGroups library coverage/counts checked for the first simple-group orders: 60 (13 groups), 168 (57), 360 (162), 504 (202), 660 (40). These five complete order fibers are small enough for an exact initial screen.
- Larger tested simple-group orders 1092, 2448, 2520, 3420, 4080, 5616, 6048, 6072, 7800, and 7920 are not fully available through `SmallGroupsAvailable` in this installation, so a negative result on the first five orders cannot be extrapolated.

## Exact bounded screen — observed output

Script: `Agents/Kourovka/problems/19.30/scratch/screen_smallgroups.g`, followed by the range-controlled `screen_one_order.g`. Software: GAP 4.12.1. The test constructs each named `SmallGroup(n,i)`, obtains its ordinary character table, and defines
\[
\operatorname{Vo}(G)=\{\operatorname{ord}(C_j): \chi(C_j)=0\text{ for at least one }\chi\in\operatorname{Irr}(G)\}.
\]
Equality with the simple target's set is then exact equality of GAP integer sets. Observed completed coverage:

| Order | Complete library fiber | Simple target | Exact target \(\operatorname{Vo}\) | Nonsimple matches |
|---:|---:|---|---|---|
| 60 | all 13 groups | `SmallGroup(60,5) = A5` | `[ 2, 3, 5 ]` | none |
| 168 | all 57 groups | `SmallGroup(168,42) = PSL(3,2)` | `[ 2, 3, 4, 7 ]` | none |
| 360 | all 162 groups (ranges 1–80 and 81–162) | `SmallGroup(360,118) = A6` | `[ 2, 3, 4, 5 ]` | none |

The first combined run timed out after printing the order-360 target, so that incomplete portion was not counted; both subsequent disjoint range runs completed and printed `MATCH_IDS_IN_RANGE=[ ]`. Attempts on order 504 and 660 hit the explicit 55-second cap before printing a completed range and therefore establish nothing about those fibers. A proposed all-named-character-table-library screen also hit its 55-second cap before producing output and establishes nothing.

What the completed screen proves: no counterexample exists whose simple member has order 60, 168, or 360. All isomorphism classes at those orders in the installed SmallGroups library were checked, and those fibers are complete.

What it does not prove: it says nothing about any larger order, about interrupted ranges, or about completeness/correctness beyond the installed GAP 4.12.1 libraries. It is bounded evidence only, and the three negative orders are already covered by published affirmative family results.

## Compute-protocol correction

- 2026-08-12T05:27:11Z — further GAP work stopped; cumulative active time: 14 minutes.
- I noticed after the initial runs that common protocol §4 categorically treats GAP jobs as heavy even when individually below 60 seconds. The completed jobs had been launched without a lease. I disclosed this to Lead and requested a 30-minute slot before any further GAP computation. No GAP process remains running. Waiting time from this point is not charged.

## Further literature triage while compute is parked

- C. Shao and Q. Jiang, *A New Characterization of PSL(2,q) by Group Order and the Set of Vanishing Element Orders*, Algebra Colloquium 26 (2019), 459, DOI 10.1142/S1005386719000336, appears from its title/abstract indexing to cover the full `PSL(2,q)` family. Thus continued brute-force work at orders 504 and 660 would only replicate known affirmative cases.
- Search results also show a 2026 paper by B. Ebrahimzadeh and A. Shabani on simple groups \({}^2D_4(2^n)\), and 2024–2025 family-specific recognition papers. This ongoing stream of special-family results, together with the unchanged current Notebook entry, is evidence that the general question remains open rather than stale.
- Counterexample-search implication: prioritize simple targets not already covered by the 2017 theorem (sporadic, alternating, `L2(p)`, and simple groups with only 3 or 4 prime divisors), the 2019 `PSL(2,q)` theorem, or the later named family papers. Screening order fibers already known affirmatively is useful only as software validation.

- 2026-08-12T05:28:03Z — literature triage stopped pending compute lease; cumulative active time: 15 minutes.

## Resume dispatch and redesigned target

- 2026-08-12T17:01:39Z — resumed at cumulative active minute 15 and processed Lead's dispatch; counterexample direction remains the only running direction.
- Lead declined screening orders 504 and 660 because those `PSL(2,q)` targets are already covered affirmatively. The expired generic request is replaced by the following exact finite target.

Target: the simple group `L3(9) = PSL(3,9)`, of order
\[
9^3(9^3-1)(9^2-1)=42{,}456{,}960=2^7 3^6\cdot5\cdot7\cdot13.
\]
It lies outside the located `PSL(3,p)` theorem because 9 is not prime, and outside the 2017 simple-\(K_n\) theorem because its order has five distinct prime divisors. Exact web searches for `"PSL(3, 9)" "vanishing elements" recognition` and `"PSL(3,9)" "orders of vanishing elements"` found no recognition result for this target.

Finite search universe: every nonduplicate ordinary character table among the installed CTblLib names. The script loads every named table, selects precisely those of order 42,456,960, and compares each nonsimple table's exact vanishing-order set with that of `L3(9)`. This is a finite character-table-library screen; it is not asserted to enumerate every abstract group of that order. Any match would nevertheless give an explicit table-level counterexample candidate requiring identification and certification.

Reproducible command: `timeout 600s gap -q Agents/Kourovka/problems/19.30/scratch/screen_l3_9_ctbllib.g > Agents/Kourovka/problems/19.30/scratch/screen_l3_9_ctbllib.out 2>&1`.

Resource estimate: one CPU, under 1 GB RAM, at most 600 seconds wall time, one process. Requested lease duration: 15 minutes. Success criterion: the script reaches and prints `NONSIMPLE_EQUAL_VO_MATCHES`; kill criterion: timeout, memory error, missing `L3(9)` table, or no nonsimple same-order tables/matches, after which this target is abandoned rather than repeatedly widened.

### Pre-compute static-metadata triage and superseding target

Without invoking GAP, I parsed CTblLib's compressed static `attr_size.json.gz` and `attr_asinfo.json.gz`. The installed metadata contains 2,613 named tables and 154 simple main-table names. `L3(9)` is the only named table of order 42,456,960, so its proposed library comparison has no candidate partner and should not consume a lease.

More importantly, the metadata identifies the pair `O7(3)` and `S6(3)`, both marked simple and both of order 4,585,351,680. These are the nonisomorphic simple groups of types \(B_3(3)\) and \(C_3(3)\). The problem's first group is only required to be finite, not nonsimple; hence if these two groups have equal vanishing-order sets, either one paired with the other is a counterexample to the claimed recognition.

This pair is outside the 2017 simple-\(K_n\), \(n\le4\), theorem because
\[
4{,}585{,}351{,}680=2^9 3^9\cdot5\cdot7\cdot13
\]
has five distinct prime divisors. Neither belongs to the alternating, sporadic, or `PSL(2,q)` families. No computation has yet been run on the pair.

Superseding exact command: `timeout 60s gap -q Agents/Kourovka/problems/19.30/scratch/compare_o7_3_s6_3.g > Agents/Kourovka/problems/19.30/scratch/compare_o7_3_s6_3.out 2>&1`. Resource estimate: one CPU, under 512 MB RAM, at most 60 seconds wall time, one process, five-minute lease. It loads exactly the two ordinary tables, computes each exact vanishing-order set, prints equality and both set differences. A positive equality is an immediate explicit counterexample candidate; inequality kills this pair conclusively at the character-table level.

Targeted literature search for `"S6(3)" "O7(3)" isospectral`, `"Sp6(3)" "O7(3)" "same spectrum"`, and both names with `vanishing elements` found no prior vanishing-order comparison. It did confirm that the pair is a standard ambiguity for weaker recognition invariants: published work calls them 2-fold recognizable by order plus prime-graph degree pattern, and work on orders of solvable subgroups identifies \(O_{2n+1}(q),S_{2n}(q)\) for odd \(q\) as the exceptional same-order pair. This strengthens the mathematical reason to test them, but does not imply equality of vanishing-order sets.

- 2026-08-12T17:05:35Z — redesigned target and focused literature check completed; cumulative active time: 19 minutes. Computation parked pending Lead lease; waiting time is not charged.

## Replacement slot-1 run — `O7(3)` versus `S6(3)`

- 2026-08-13T11:21:07Z — resumed under operator-supplied accounting baseline 15/180 active minutes; read inbox oldest-first. MathExpert independently endorsed the `O7(3)`/`S6(3)` target and suggested `O9(3)`/`S8(3)` only if the first pair failed. The original Lead lease had expired before delivery; Lead's replacement slot-1 lease was valid through 2026-08-13T12:30:00Z.
- Ran exactly the authorized command: `timeout 60s gap -q Agents/Kourovka/problems/19.30/scratch/compare_o7_3_s6_3.g > Agents/Kourovka/problems/19.30/scratch/compare_o7_3_s6_3.out 2>&1`.
- Exit status: 0. Software: GAP 4.12.1, CTblLib 1.3.7. Exact observed output is preserved in `scratch/compare_o7_3_s6_3.out`.

Computed table invariants:

- `O7(3)`: order 4,585,351,680; `IsSimple=true`; 58 conjugacy classes; vanishing-order set
  `[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20 ]`.
- `S6(3)`: same order; `IsSimple=true`; 74 conjugacy classes; vanishing-order set
  `[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20, 24, 30, 36 ]`.
- GAP printed `EQUAL_ORDER=true EQUAL_VO=false`, `A_MINUS_B=[ ]`, and `B_MINUS_A=[ 24, 30, 36 ]`.

Conclusion: this same-order simple pair is conclusively not a counterexample at the installed ordinary-character-table level. Vanishing orders 24, 30, and 36 distinguish `S6(3)` from `O7(3)`. This computation concerns the exact library tables named above, not constructed group objects; CTblLib's table identifiers and simplicity metadata identify the intended finite simple groups.

- 2026-08-13T11:22:00Z — command inspected and slot 1 released; cumulative active time under the operator's resumed baseline: 16 minutes.

## Lead-assigned next structural pair — `O9(3)` versus `S8(3)`

- 2026-08-13T16:57:24Z — resumed at the operator-supplied baseline 16/180 active minutes and processed Lead's dispatch. The counterexample direction remains running; the proof direction remains parked.
- Read-only inspection of CTblLib static metadata confirmed that both ordinary tables are installed: `attr_size.json.gz` lists `O9(3)` and `S8(3)` with equal order 65,784,756,654,489,600, and `attr_asinfo.json.gz` marks each as its own simple socle/main table (`[1,1]`). This check did not invoke GAP and consumed no compute slot.
- Structural reason: these are the next odd-characteristic dual-type pair \(B_4(3)\) and \(C_4(3)\), analogous to the tested \(B_3(3)/C_3(3)\) pair. Their equal orders and dual root data make matching vanishing-order sets plausible enough for one exact falsification test. Per Lead, separation kills this direction; no unrelated enumeration follows.

Exact proposed command: `timeout 120s gap -q Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.g > Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.out 2>&1`.

Resource estimate: one CPU, under 1 GB RAM, at most 120 seconds wall time, one process, five-minute lease. The script loads exactly the two installed ordinary tables, computes exact class-order sets on which at least one ordinary irreducible character is zero, and prints equality plus both symmetric differences. Success criterion: complete output through both set differences. Kill criterion: timeout/error, or any nonempty symmetric difference; the latter stops the \(B_n/C_n\) counterexample direction as instructed.

- 2026-08-13T16:58:13Z — table-presence check and exact design completed; cumulative active time: 17 minutes. Parked pending lease; waiting time is not charged.

## Slot-1 run — `O9(3)` versus `S8(3)`

- 2026-08-13T17:31:08Z — read fresh Lead lease first; valid through 2026-08-13T19:30:00Z. Ran exactly the authorized command: `timeout 120s gap -q Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.g > Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.out 2>&1`.
- Exit status: 0. Software: GAP 4.12.1, CTblLib 1.3.7. Exact observed output is preserved in `scratch/compare_o9_3_s8_3.out`.

Computed table invariants:

- `O9(3)`: order 65,784,756,654,489,600; `IsSimple=true`; 218 conjugacy classes; vanishing-order set `[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20, 21, 24, 26, 28, 30, 36, 39, 40, 41, 42, 45, 52, 60 ]`.
- `S8(3)`: same order; `IsSimple=true`; 278 conjugacy classes; vanishing-order set `[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20, 21, 24, 26, 28, 30, 36, 39, 40, 41, 42, 45, 52, 60, 72, 78, 84, 90 ]`.
- GAP printed `EQUAL_ORDER=true EQUAL_VO=false`, `A_MINUS_B=[ ]`, and `B_MINUS_A=[ 72, 78, 84, 90 ]`.

Conclusion: the exact ordinary tables are separated by vanishing orders 72, 78, 84, and 90. Together with the analogous strict inclusion for `O7(3)`/`S6(3)`, this triggers Lead's kill criterion: stop the \(B_n/C_n\) counterexample direction and do not enumerate unrelated pairs without a new structural reason.

- 2026-08-13T17:31:54Z — output inspected and slot 1 released; cumulative active time: 18 minutes.
