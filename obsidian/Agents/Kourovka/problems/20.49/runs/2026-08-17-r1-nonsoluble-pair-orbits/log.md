---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - project/kourovka
  - status/draft
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
direction: counterexample
run: 2026-08-17-r1-nonsoluble-pair-orbits
---

# Problem 20.49 counterexample reconnaissance, revision 1

## Active-time ledger

- 2026-08-17T11:48:39Z — START, cumulative active minutes 0. Protocol and assignment loaded; begin source gate and reconnaissance.

## 2026-08-17T11:50:35Z — Staleness and source gate

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
No open-web search or solution-bearing historical artifact was consulted.

Corpus record inspected: `Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl`, line 1139. Flags are `answered: false`, `has_editor_comment: false`, and `has_later_comment: false`. The corpus record says `page: 153`, while the canonical scope points to PDF page 151. The source statement itself occurs on the rendered PDF page labelled 151, and the canonical pointer is therefore the operative one.

Source commands:

```text
source _meta/agents/Kourovka/paths.env
pdftotext -f 151 -l 153 -layout "$KOUROVKA_PDF" -
pdftoppm -f 151 -l 151 -png -r 160 "$KOUROVKA_PDF" /tmp/kourovka-20-49-page
```

I visually inspected `/tmp/kourovka-20-49-page-151.png` at original resolution, including the complete statement and both contextual sentences.

Corrected transcription from the rendered PDF:

> **20.49.** Is it true that any finite group contains a 2-generated subgroup with the same exponent?
>
> An affirmative answer is known for soluble groups. It is also known that any finite group contains a 3-generated subgroup with the same exponent (E. Detomi, A. Lucchini, *J. London Math. Soc.* (2), 87, no. 3 (2013), 689–706). — A. Lucchini

`source_transcription_checked: yes`

Clause matrix:

| source clause | equivalent formulation | active scope? | treatment in this discovery-blind run |
|---|---|---:|---|
| Any finite group contains a 2-generated subgroup with the same exponent | For every finite `G`, there are `x,y in G` with `exp(<x,y>)=exp(G)` | yes | exact target |
| Affirmative answer is known for soluble groups | A counterexample, if one exists, is nonsoluble | no | accepted source context; used only to prune the search |
| Every finite group contains a 3-generated subgroup with the same exponent | Generator bound three is known | no | excluded weaker clause |

`active_scope_checked: yes`

Admissibility checklist reconstructed from the rendered source and reconciled with the canonical record:

| constraint id | required condition | reconciliation |
|---|---|---|
| `20.49-forall-finite-G` | one finite ambient `G` must fail the asserted existential statement to disprove it | matches |
| `20.49-G-finite` | `G` finite | matches |
| `20.49-H-subgroup` | `H <= G`, not necessarily proper | matches |
| `20.49-H-at-most-two-generated` | `H=<x,y>` for some `x,y in G`; one-generated cases are included by allowing one generator to be redundant | matches |
| `20.49-exponent-equality` | exact equality of least-common-multiple exponents | matches |
| `20.49-universal-existence-conclusion` | every finite `G` has at least one eligible `H` | matches; this is the conclusion a counterexample must violate |

No statement/scope mismatch was found.

## 2026-08-17T11:51:00Z — Exact counterexample predicate and immediate exclusions

For a fixed finite group `G`, define

```text
P(G) :<=> for every ordered pair (x,y) in G^2,
           exp(<x,y>) != exp(G).
```

Since `<x,y> <= G`, `exp(<x,y>)` divides `exp(G)`. Thus the inequality in `P(G)` is equivalently strict divisibility, or numerically `exp(<x,y>) < exp(G)`. A finite `G` is a counterexample exactly when `P(G)` holds.

Two immediate exclusions:

1. A soluble ambient group cannot be a counterexample by the affirmative soluble-group clause printed in the source.
2. A two-generated ambient group cannot be a counterexample: if `G=<x,y>`, choose `H=G`, which is permitted because `H` need not be proper, and then `exp(H)=exp(G)` tautologically.

The second observation is only a pruning rule. Failure to generate all of `G` does not imply failure of the exponent condition: a proper two-generated subgroup can still have full exponent.

## 2026-08-17T11:52:00Z — Ranked strategy portfolio

1. **Catalogue/small-case mode — `SG255-ALL-PAIRS`.** Enumerate every SmallGroups isomorphism representative of order `1..255`, discard the soluble representatives, and for every remaining group evaluate all ordered pairs. For each group record the exact exponent histogram of the generated subgroups and a first full-exponent pair if one exists. This is the cheapest certifiable experiment. A negative search result excludes counterexamples only through order 255; it does not address the universal statement.
2. **Structured-construction mode — `MONOLITHIC-RADICAL-EXPONENT-SPLIT`.** Design a nonsplit or monolithic extension `1 -> R -> G -> S -> 1` in which no two lifts can simultaneously realize every prime-power component contributed by `R` and `S`. Direct products are unlikely to help: full-exponent pairs in the factors can be paired coordinatewise, and their generated subgroup projects onto both full-exponent factor subgroups.
3. **Theoretical mode — `PRIME-POWER-DEFECT-REDUCTION`.** Rewrite `P(G)` as: for each pair `(x,y)`, at least one prime-power divisor of `exp(G)` is absent from `exp(<x,y>)`. Seek a minimal counterexample and use quotient/radical information to force a cover of `G^2` by these prime-power defect sets. This may expose an obstruction in an almost-simple quotient or in an irreducible radical layer.
4. **Certificate plan.** Catalogue completeness comes from SmallGrp's complete irredundant lists. The frozen computation names every `[order,index]`, checks all `|G|^2` ordered pairs, verifies exponent divisibility, and records an exponent histogram. A hit is reconstructible as `SmallGroup(order,index)` plus the full pair count and histogram; Validator can independently rerun all pairs or replace them by automorphism orbits. A bounded exclusion needs only one explicit full-exponent pair per isomorphism type, but the first script deliberately records all pairs as a stronger audit.

Kill criterion for `SG255-ALL-PAIRS`: if the complete layer has no hit and its near-miss histograms reveal no group with very few full-exponent pairs, stop enlargement and ask Lead for a representation-changing pivot rather than raising the order bound mechanically.

## 2026-08-17T11:53:00Z — Installed static catalogue metadata

No GAP process was invoked. Static files show:

- `/usr/share/gap/pkg/SmallGrp/PackageInfo.g`: SmallGrp version 1.5.3, dated 16 May 2023.
- `/usr/share/gap/pkg/SmallGrp/doc/chap1.txt`: for each available order the library gives a complete and irredundant list of isomorphism-type representatives; it contains all groups of order at most 2000 except 1024.

Therefore the proposed bounded layer is precisely **all nonsoluble finite groups of order at most 255, one representative per isomorphism type**. Every order `1..255` is within the documented complete range. The script nevertheless checks `SmallGroupsAvailable(n)` for every order and iterates indices `1..NumberSmallGroups(n)` rather than trusting a filtered selection call.

## 2026-08-17T11:52:29Z — Frozen compute request

Frozen script: `scratch/sg255_all_pairs.g`

SHA-256:

```text
63c90b1de2144002ce001900880a23616f9ee90e850c0300fc4ece8c7d9a55bd
```

Frozen command (not yet run):

```text
timeout --signal=TERM --kill-after=30s 20m gap -q -T Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_all_pairs.g
```

Primary output is hard-coded as `scratch/sg255_all_pairs.out`. Estimate: one CPU core; 2–10 CPU minutes expected, hard wall cap 20 minutes; under 512 MiB expected and 1 GiB requested ceiling; requested lease duration 30 minutes. No GAP call has been made.

## 2026-08-17T12:15:48Z — Leased run exited; slot released

Lead granted slot 2 for the exact frozen command. It was run exactly once. The shell exit code was `124`, so the 20-minute `timeout` terminated the computation before the bound 255 was completed.

There was also an output-routing defect in the frozen script: GAP interpreted `Print(out, ...)` as ordinary printing of the stream object followed by the data, rather than writing into the stream. Consequently, the intended output file is empty:

```text
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  scratch/sg255_all_pairs.out
0 lines, 0 bytes
```

The GAP process stdout was visible in the supervised tool stream. I preserved the completed group records, explicitly labelled as a manual transcription rather than raw output, in `scratch/sg255_all_pairs.observed-partial.txt`.

Exact completed coverage inferred from the sequential script and observed markers:

- every catalogue index at every order `1..239` was classified;
- all six nonsoluble representatives encountered there, `[60,5]`, `[120,5]`, `[120,34]`, `[120,35]`, `[168,42]`, and `[180,19]`, received complete `|G|^2` ordered-pair scans;
- at order 240, five further nonsoluble representatives `[240,89]` through `[240,93]` received complete ordered-pair scans;
- 11 nonsoluble representatives and 395,424 ordered pairs were completed in total;
- every completed representative had many full-exponent pairs; no candidate record occurred in the completed portion.

The run does **not** cover the remaining order-240 representatives or orders `241..255`. The empty raw output artifact and manual transcription also mean this partial computation should not be treated as independently certifiable without a corrected rerun or Validator replication.

Slot 2 is released immediately on process exit. No rerun has been made.

## 2026-08-17T12:17:13Z — Approximately 30-minute self-check

- **Target:** revision 1, one finite nonsoluble `G` for which every two-generated subgroup has exponent strictly below `exp(G)`.
- **Current hypothesis:** no evidence for a counterexample in the low-order layer. Each of the 11 completed nonsoluble representatives has abundant full-exponent pairs (the observed proportions range from 6,840/14,400 to 23,400/32,400 in the groups below order 240, and from 27,360/57,600 to 36,480/57,600 in the five completed order-240 groups).
- **Evidence quality:** the pair counts themselves were actually observed, but the intended raw artifact is empty; the manually transcribed partial is not a certification-grade substitute. Any bounded result must be rerun with correct output routing or independently replicated.
- **Representation audit:** full exponent histograms for every noncandidate consume almost all runtime while adding no information needed to exclude that group. The productive exact predicate is witness-first: stop a group on the first full-exponent pair; only a group with no witness naturally reaches all `|G|^2` pairs and thereby produces the required counterexample certificate. The observed first witnesses occur early enough that this changes the cost by orders of magnitude.
- **Decision point:** do not rerun or enlarge autonomously. Recommend either (A) Lead-authorized corrected witness-first completion of the same frozen layer, with persistent `AppendTo` output, or (B) stop catalogue work and pivot to the monolithic-radical structural construction. Alternative (A) is the cheapest way to turn the partial reconnaissance into a complete bounded exclusion, but it requires a new frozen script and lease.

## 2026-08-17T12:19:00Z — Hand reduction for a least-order counterexample

Assume counterexamples exist and choose one, `G`, of least order. Then all of the following hold.

**(R1) Every proper subgroup has smaller exponent.** If `L<G` and `exp(L)=exp(G)`, minimality says `L` is not a counterexample. Hence `L` contains a subgroup generated by at most two elements whose exponent is `exp(L)=exp(G)`, and the same subgroup witnesses the property in `G`, contradiction.

**(R2) Every nontrivial proper quotient has smaller exponent.** Let `1 != N normal G`. If `exp(G/N)=exp(G)`, minimality supplies `aN,bN` whose generated subgroup in `G/N` has exponent `exp(G/N)`. For arbitrary lifts `a,b`, the group `<a,b>` maps onto that subgroup, so its exponent is divisible by `exp(G/N)=exp(G)`. Since it is a subgroup of `G`, its exponent also divides `exp(G)`, giving equality and a contradiction.

**(R3) `G` requires exactly three generators.** It is not two-generated, because otherwise `H=G` is an allowed witness. The source records the known fact that every finite group has a three-generated full-exponent subgroup `L`. By (R1), that subgroup cannot be proper, so `L=G`. Thus `d(G)=3`.

**(R4) `G` is nonsoluble and directly indecomposable.** Nonsolubility follows from the source's affirmative soluble case. For direct indecomposability, first note the closure lemma: if `A` and `B` each possess full-exponent two-generated subgroups `<a1,a2>` and `<b1,b2>`, then

```text
H = <(a1,b1),(a2,b2)> <= A x B
```

projects onto both of them. Therefore both `exp(A)` and `exp(B)` divide `exp(H)`, while `exp(H)` divides `exp(A x B)=lcm(exp(A),exp(B))`; equality follows. If the least counterexample split nontrivially as `A x B`, minimality would give the property in both smaller factors and the closure lemma would contradict that it is a counterexample.

Consequently, existence of any counterexample implies existence of a finite nonsoluble, directly indecomposable, exactly three-generated group for which every proper subgroup and every nontrivial proper quotient has strictly smaller exponent. This is an exact existence reduction, not a proof that such a group exists.

- 2026-08-17T12:18:58Z — STOP/`awaiting_lead`, cumulative active minutes 30. The leased implementation hit its wall cap; operational report and strategy-choice checkpoint filed. No replacement computation or method starts without Lead's decision.

- 2026-08-17T12:20:47Z — START, cumulative active minutes 33 (Lead roster ledger). Lead selected refinement A: freeze `SG255-WITNESS-FIRST` with persistent shell-redirection output; do not run before a new hash-matched lease.

## 2026-08-17T12:20:47Z — Corrected witness-first design

The new script preserves the original layer exactly: every catalogue index at orders `1..255`, with only nonsoluble groups entering the pair loop. For a negative row it writes the group ID, ambient exponent, exact element-list coordinates, the two element orders, subgroup size, subgroup exponent, and the number of tested pairs as soon as the first equality occurs. If no equality exists, the loops necessarily reach all `|G|^2` ordered pairs and write the complete exponent histogram plus exact pair count as a candidate certificate. `ORDER_START`/`ORDER_DONE` rows make any interrupted frontier explicit.

The primary artifact is now plain GAP standard output, captured by shell redirection, and standard error has its own path. No GAP process has been invoked for this refinement.

## 2026-08-17T12:22:22Z — Frozen `SG255-WITNESS-FIRST` lease request

Frozen script: `scratch/sg255_witness_first.g` (132 lines, 4,334 bytes).

SHA-256:

```text
50351b6a13abfc7f44e46cd7854e92d81fe0a0b5bc86749b3b2fa0afa9f9b756
```

Frozen command (not yet run):

```text
timeout --signal=TERM --kill-after=30s 10m gap -q -T Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.g > Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.out 2> Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.err
```

Estimate: one CPU core; under 2 CPU minutes expected from the observed early witness positions, with a 10-minute hard wall cap; under 512 MiB expected and 1 GiB requested ceiling; 15-minute lease. A true candidate can legitimately consume more time because only it reaches all pairs. No GAP call has been made.

- 2026-08-17T12:23:14Z — STOP/awaiting compute lease, cumulative active minutes 36. Frozen request filed; no GAP invocation pending Lead approval.

- 2026-08-17T12:25:29Z — START, cumulative active minutes 36. Hash-matched slot-2 lease read; begin the exact one-shot witness-first command.

## 2026-08-17T12:25:39Z — `SG255-WITNESS-FIRST` completed; slot released

The exact leased command ran once and exited `0` in 8.20 seconds of shell wall time (GAP reported 9,908 ms runtime). Slot 2 is released immediately. The script hash still matches the frozen value.

Artifacts:

```text
50351b6a13abfc7f44e46cd7854e92d81fe0a0b5bc86749b3b2fa0afa9f9b756  scratch/sg255_witness_first.g
64ef89dd5574be75ed803d0e84311debe7e9e574ac95400f86afc85c3abe6e26  scratch/sg255_witness_first.out
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  scratch/sg255_witness_first.err
```

The output has 531 lines and 32,180 bytes; the error file has 0 lines and 0 bytes. It contains `ORDER_DONE order=255` and the terminal summary:

```text
SUMMARY total_catalogue_groups=7012 soluble_groups=6998 nonsoluble_groups=14 pairs_tested=5932 candidate_groups=0 runtime_ms=9908
```

The 14 nonsoluble representatives are `[60,5]`; `[120,5]`, `[120,34]`, `[120,35]`; `[168,42]`; `[180,19]`; and `[240,89]`, `[240,90]`, `[240,91]`, `[240,92]`, `[240,93]`, `[240,94]`, `[240,189]`, `[240,190]`. Every one has a persisted exact full-exponent witness row. No candidate occurred.

Exact interpretation: using SmallGrp 1.5.3 under GAP 4.12.1, every nonsoluble group of order at most 255 has a subgroup generated by at most two elements with the same exponent. Together with the source's known soluble case, this rules out a counterexample of order at most 255. It does not address any group of order at least 256 and does not prove the universal statement. The catalogue/library and computation still require independent review before certification.

- 2026-08-17T12:25:39Z — STOP after leased computation/report preparation, cumulative active minutes 37.

- 2026-08-17T12:27:15Z — START, cumulative active minutes 39 after charging the raw-output consistency inspection. Prepare the bounded partial-result note and strategy handoff.

## 2026-08-17T12:27:15Z — Independent transcript-consistency inspection

A non-GAP `awk` pass over the raw output returned:

```text
order_starts=255
order_dones=255
last_order_done=255
summed_catalogue=7012
summed_soluble=6998
summed_nonsoluble=14
group_rows=14
summed_pairs=5932
candidate_rows=0
fatal_rows=0
summary_rows=1
```

This checks internal completeness and arithmetic of the transcript; it is not an independent group-theoretic replication.

- 2026-08-17T12:28:29Z — STOP/`awaiting_lead`, cumulative active minutes 40. Bounded partial result sent for Validator review; catalogue strategy complete; next representation-changing experiment requested from Lead.

- 2026-08-17T12:47:21Z — START, cumulative active minutes 40. Lead authorized at most 30 active minutes on `MONOLITHIC-SOCLE-GATE`, by hand only.

## 2026-08-17T12:49:05Z — `MONOLITHIC-SOCLE-GATE` obstruction

The gate fails at the stated inference level. The dihedral group

```text
D=<r,s | r^15=s^2=1, srs=r^(-1)>
```

has order 30 and exponent 30; every proper subgroup and every nontrivial proper quotient has smaller exponent; it is directly indecomposable; yet it has two distinct minimal normal subgroups of orders 3 and 5. Full details are in `monolithic-socle-gate.md`.

This example is soluble and two-generated, hence out of scope as a counterexample. It freezes the exact obstruction: exponent-criticality plus direct indecomposability does not force monolithicity. The extra least-counterexample facts `G` nonsoluble and `d(G)=3` would need genuinely new use. Accordingly, no unique-socle abelian/nonabelian case split is justified from the present reductions, and this named method stops under Lead's criterion.

- 2026-08-17T12:50:11Z — STOP/`awaiting_lead`, cumulative active minutes 43. Obstruction checkpoint filed; no new method begins without Lead's decision.

- 2026-08-17T12:51:55Z — START, cumulative active minutes 43. Lead authorized at most 25 active minutes on `THREE-PAIR-DEFECT-HYPERGRAPH`, hand work only.

## 2026-08-17T12:56:50Z — Prime-power defect outcome

The complete hand derivation is in `three-pair-defect-hypergraph.md`. The strongest exact consequences are:

1. a counterexample exponent has at least three distinct prime divisors;
2. if it has exactly three, maximal pure prime-power elements form an irredundant generating triple whose three pair defects are forced to be the three distinct omitted primes;
3. an abelian minimal normal `p`-subgroup lowers the quotient's maximal `p`-power exponent by exactly one step, and in a split extension the missing step is equivalent to a nonzero norm for a maximal-order `p`-element of the complement;
4. for a general chosen full-exponent triple, edge-defect localization is not invariant under Nielsen changes. An explicit irredundant pair-deficient example changes one nonempty edge defect from 7 to 3 under `x -> x+y`.

Accordingly the strategy cannot canonically attach three defect primes to an arbitrary generating triple. The exact three-prime and abelian-chief-factor subcases remain reusable reductions; the unrestricted localization method stops at the instructed non-invariance obstruction.

- 2026-08-17T12:58:09Z — STOP/`awaiting_lead`, cumulative active minutes 49. Outcome checkpoint filed; no new method begins without Lead's decision.

- 2026-08-17T13:00:01Z — START, cumulative active minutes 49. Lead authorized at most 30 active minutes on `THREE-PRIME-ABELIAN-CHIEF-NORM`, split case and hand work only.

## 2026-08-17T13:05:43Z — Split norm gate outcome

The exact norm calculation and compatible failure pattern are in `three-prime-abelian-chief-norm.md`.

For a split elementary abelian `p`-layer that raises the `p`-exponent from `p^(a-1)` to `p^a`, some quotient `p`-element `u` of order `m=p^(a-1)` must have nonzero norm `T_u=1+u+...+u^(m-1)=(u-1)^(m-1)`. Hence the restricted action has a Jordan block of length `m` and `dim(N)>=m`.

This does not force a partner for the lifted maximal `p`-element. An explicit soluble split group

```text
F3^3 semidirect (A4 x (C25 semidirect C4))
```

with the coordinate-permutation `A4` module has exponent 900 and a pure generating triple of orders 9, 4, 25 with the three distinct pair defects. The order-9 element has no single partner of full complementary 4- and 25-parts, because its `B=C25 semidirect C4` projection is trivial and every one-generated subgroup of `B` has order dividing 25 or 4, never both. This is a compatible action-pattern failure certificate, not a counterexample (the group is soluble).

Thus the restricted norm method stops: it yields a sharp Jordan-block constraint but cannot force the desired mixed pair without an additional nonsoluble/almost-simple restriction on the quotient.

- 2026-08-17T13:07:12Z — STOP/`awaiting_lead`, cumulative active minutes 56. Failure-pattern checkpoint filed; no new method begins without Lead's decision.

