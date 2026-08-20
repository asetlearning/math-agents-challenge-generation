---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/finite-groups
  - project/kourovka
  - status/draft
---

# Problem 20.21 working log

## Active-time ledger

- 2026-08-11T15:49:23Z — work started; cumulative active minutes: 0.

## Staleness check

### 2026-08-11T15:49Z–15:54Z

- Loaded `_meta/agents/Kourovka/paths.env`: configured PDF resolves; `KOUROVKA_AUTHOR=operator`.
- Corpus record: `answered: false`, `has_editor_comment: false`, `has_later_comment: false`. The older issue-20 corpus records PDF p. 150; the configured/current PDF places the statement on physical page 148, as recorded by the synthesis.
- Read physical PDF page 148 using:

  ```bash
  source "_meta/agents/Kourovka/paths.env"
  pdftotext -f 148 -l 148 -layout "$KOUROVKA_PDF" -
  pdftoppm -f 148 -l 148 -png -r 150 "$KOUROVKA_PDF" Agents/Kourovka/problems/20.21/scratch/source-page
  ```

- Visually inspected `scratch/source-page-148.png`, not merely its extracted text.
- Corrected/source-faithful transcription: “Does there exist a finite group \(G\) with two normal subgroups \(K\) and \(L\), each with index 12 in \(G\), such that \(K\) is isomorphic to \(L\), but \(G/K\) is isomorphic to \(C_{12}\), while \(G/L\) is isomorphic to \(A_4\)?” Attribution: G. Verret; proposer: M. Conder.
- `source_transcription_checked: yes`.
- Searches performed: exact phrases `"Kourovka 20.21"` and `"Problem 20.21" "Kourovka"`; proposer/attribution plus `finite group normal subgroups index 12 C12 A4`; arXiv-focused search for the quotient pair and isomorphic normal subgroups; current Notebook No. 21.
- Exact-match paper found: Ihechukwu Chinyere, *On the non-existence of finite groups with certain normal subgroups*, arXiv:2601.01080 (submitted 2026-01-03; v2 dated 2026-01-07). Its abstract says no such group exists, but arXiv marks it **withdrawn** and the author states: “We have discovered an error in Section 3.4 that affects the main arguments, and we wish to withdraw the paper until it can be corrected.” No PDF is available for the current version. This is not a valid solution citation.
- The configured/current Notebook No. 21 prints 20.21 unstarred with no answer/comment. Search also found a 2026 workshop proceedings item stating a minimal-counterexample proposition (attributed to Conder and Maslova): if a least-order example exists and \(M=KL\), \(N=K\cap L\), then \(M\) is a 2-group, \([G:M]=3\), \([G:N]=48\), and \(G/N\cong C_4\times A_4\). This is context, not a closure.
- Conclusion: no sound published solution located; problem remains live as of this check.

## Statement in my own words

Find (or rule out) a finite group admitting two epimorphisms onto the two non-isomorphic groups of order 12, \(C_{12}\) and \(A_4\), whose kernels are abstractly isomorphic. Both kernels must be normal automatically and have the same order \(|G|/12\); the additional content is abstract isomorphism, not equality or automorphic equivalence.

## Structural reduction and first bounded computation

### 2026-08-11T15:55Z–15:59Z

- Put \(N=K\cap L\). The diagonal map embeds \(G/N\) as a subdirect product of \(G/K\cong C_{12}\) and \(G/L\cong A_4\). By Goursat's lemma, the gluing quotient must be a common quotient of \(C_{12}\) and \(A_4\). Since the only nontrivial proper quotient of \(A_4\) is \(A_4/V_4\cong C_3\), the only possibilities are the trivial gluing (full product, order 144) or gluing over \(C_3\) (order 48). In the latter case the fiber product is \(C_4\times A_4\): identify \(C_{12}\cong C_4\times C_3\) and match its \(C_3\)-coordinate to the abelianization of \(A_4\). This independently explains the quoted minimal-case quotient, except that excluding the full-product case uses minimality and has not yet been proved here.
- GAP 4.12.1 is installed. Created `scratch/search-small.g`, which exhaustively iterates every `SmallGroup(n,i)` for multiples of 12 through 240, finds all normal subgroups of index 12, exactly identifies their quotients using `IdGroup`, and tests kernel isomorphism using `IdGroup` (all tested kernels lie in the SmallGroups range).
- Exact command: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/search-small.g' > 'Agents/Kourovka/problems/20.21/scratch/search-small.out' 2>&1`.
- The cap stopped the computation while processing order 144. Full observed output is in `scratch/search-small.out`. It completed all groups of orders 12, 24, ..., 132. No hit appeared. Five near misses appeared before order 144; the first is `SmallGroup(48,31)`, with the \(C_{12}\)-quotient kernel `SmallGroup(4,2)` and the \(A_4\)-quotient kernel `SmallGroup(4,1)`.
- What this proves: no example exists among all SmallGroups of order at most 132 whose order is divisible by 12. What it does not prove: anything about larger groups or even all groups of order 144, because that order did not finish.
- The attempted range exceeded the light-compute threshold. No further enumeration will run without a leased slot.

## Active-time ledger (continued)

- 2026-08-11T16:00:30Z — work stopped pending the requested compute lease / next cycle turn; cumulative active minutes: 11. This is not an Hour-3 report and no terminal outcome has been issued.
- 2026-08-11T22:34:34Z — work resumed under fresh slot-1 lease; cumulative active minutes: 11. Fresh lease and safety stop: 2026-08-11T23:30:40Z.

### 2026-08-11T22:34Z–22:44Z — leased bounded enumeration

- Processed and archived both Lead lease messages oldest first; the 22:30Z message superseded the expired earlier lease.
- Ran the exact approved command:

  ```bash
  timeout 600s gap -q Agents/Kourovka/problems/20.21/scratch/search-small.g > Agents/Kourovka/problems/20.21/scratch/search-small-leased.out 2>&1
  ```

- The command exited normally with status 0. Verbatim output is `scratch/search-small-leased.out` (69 lines).
- Final observed line: `SUMMARY tested=2761 with_both_quotients=31 hits=0`.
- Exact coverage: every `SmallGroup(n,i)` in GAP 4.12.1 for each multiple of 12 from 12 through 240 inclusive. This is 2,761 groups. For each group, all normal subgroups were enumerated; index-12 quotients were exactly identified as `IdGroup(CyclicGroup(12)) = [12,2]` or `IdGroup(AlternatingGroup(4)) = [12,3]`; kernel types were compared by `IdGroup`.
- Result: 31 ambient groups possess normal kernels giving both quotient types; none of those groups possesses an isomorphic cross-pair of kernels. The output records all 31 as near misses and their exact SmallGroup kernel IDs.
- What this establishes: there is no requested example of order at most 240. What it does not establish: nonexistence at any larger order. It is bounded data, not a general proof.
- Compute wait time was not charged. Active time used for launch, monitoring decisions, and inspection: 4 minutes; cumulative active minutes: 15.

### 2026-08-11T22:44Z–22:48Z — audit of the withdrawn proof

- Read the cached full text of arXiv:2601.01080v1 via ResearchGate. Its section 3.4 puts `X=H intersect f(H)` for an isomorphism `f:K -> L`, and reduces to two equal-order normal subgroups of `L/X` with quotients `C4` and `V4`. The paper then claims a GAP check excludes every such pair in a finite order list.
- Two independent defects occur in the appendix test:
  1. It filters both subgroups to be non-characteristic, but the preceding argument establishes only that they are normal. Indeed, `H/X` or `f(H)/X` may be characteristic in `L/X`.
  2. It tests `StructureDescription(L_1/h) = "V4"`, but observed GAP 4.12.1 output for `StructureDescription(ElementaryAbelianGroup(4))` is `C2 x C2`. Thus its `Hv4` list is empty under that GAP naming convention.
- Created `scratch/check-withdrawn-gap.g`, replacing string matching by exact `IdGroup` checks and removing the unsupported characteristic filters. Exact command: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/check-withdrawn-gap.g' > 'Agents/Kourovka/problems/20.21/scratch/check-withdrawn-gap.out' 2>&1`.
- The 60-second light-compute cap stopped the corrected diagnostic during order 96, so it was not exhaustive over the paper's whole list. Before stopping it observed 2,580 qualifying pairs in 185 distinct groups. The first occurs in `SmallGroup(8,2)` with order-2 kernels: the `C4`-quotient kernel is non-characteristic and the `V4`-quotient kernel is characteristic. `SmallGroup(16,10)` already supplies pairs where both are non-characteristic.
- Conclusion: the withdrawn proof's finite exclusion is false, and its GAP script cannot support Theorem 1. This does **not** give an example for Problem 20.21: the local pair in `L/X` need not lift to an ambient `G` with isomorphic index-12 kernels.
- Math Expert independently replied that Goursat supports only the 48-or-144 dichotomy, not exclusion of the full-product case; both extension cases must remain live. Message processed and archived.
- Active analysis/inspection: 5 minutes; cumulative active minutes: 20.

### 2026-08-11T22:48Z — near-miss structure

- Created and ran `scratch/analyze-nearmisses.g` on exactly the 31 ambient SmallGroup IDs reported by the completed bounded search. Exact command: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/analyze-nearmisses.g' > 'Agents/Kourovka/problems/20.21/scratch/analyze-nearmisses.out' 2>&1`; exit 0.
- It analyzed all 57 cross-pairs of a `C12`-quotient kernel and an `A4`-quotient kernel in those groups.
- Except for pairs in the direct-product group `SmallGroup(144,155)` with trivial intersection and quotient of order 144, every pair has `G/(K intersection L) = SmallGroup(48,31)`, confirming computationally that this is the `C4 x A4` fiber product.
- Observed summary: `SUMMARY pairs=57 same_abelianization=0`. Thus every near miss through order 240 is already separated by the abelian invariants of its two kernels. This is a useful discriminator but not a universal obstruction.
- A package probe observed that GAP's `hap` package is unavailable, while `polycyclic` and `smallgrp` load. No HAP-dependent method has been adopted; bounded SmallGroups work remains available.
- Active analysis and computation: 7 minutes; cumulative active minutes: 27.

### Structural observations retained for the next proof attempt

- Exact GAP identifications observed: `SmallGroup(48,31)` has structure description `C4 x A4`; `SmallGroup(144,155)` has structure description `C12 x A4`.
- The full-product branch cannot be silently discarded. In that branch `K/N` is `A4` and `L/N` is `C12`; in the fiber-product branch they are `V4` and `C4`. The withdrawn proof's section 3.4 switches only to the latter pair without excluding the former when `X < H`, which is an additional logical gap.
- Cheap invariant suggested by the bounded data: compare `K/K'` and `L/L'`. It separates every pair through order 240, but no argument found forces separation for arbitrary extensions. Treating it as universal would be an unsupported extrapolation.

## Active-time ledger (continued)

- 2026-08-11T22:49:23Z — work stopped while awaiting the requested second compute lease; cumulative active minutes: 29. Compute-wait time excluded. Cycle 1 remains active with 151 minutes available; no Hour-3 terminal outcome has been issued.
- 2026-08-12T17:00:50Z — cycle resumed at cumulative active minute 29. Lead's delivered slot-1 lease had already expired at 2026-08-12T16:48:03Z, so the authorized heavy command was not launched. New process safety stop supplied by the operator/dispatch: 2026-08-12T18:48:03Z. Requested a fresh lease and continued non-heavy analysis.

### 2026-08-12T17:01Z–17:03Z — fill omitted small orders

- Audited the order ranges and noticed that the pending script begins at 288, leaving orders 252, 264, and 276 unchecked after the completed through-240 search. GAP reports respectively 46, 39, and 10 catalogued groups (95 total).
- Created `scratch/search-gap-252-276.g` with the same exact quotient/kernel predicate. Ran: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/search-gap-252-276.g' > 'Agents/Kourovka/problems/20.21/scratch/search-gap-252-276.out' 2>&1`; exit 0.
- Verbatim summary: `SUMMARY tested=95 with_both=0 hits=0`. Thus none of those 95 groups even has both required quotient types.
- Combining this with the earlier completed run establishes no example among every SmallGroup whose order is divisible by 12 from 12 through 276 inclusive. It remains bounded evidence only.
- Active work: 3 minutes; cumulative active minutes: 32.

## Active-time ledger (continued)

- 2026-08-12T17:03:00Z — work stopped pending a fresh compute lease; cumulative active minutes: 32. The expired dispatch remains `status: blocked` in the inbox and Lead has been sent a `BLOCKER`. Waiting time is not charged. No terminal cycle outcome issued.
- 2026-08-12T17:12:28Z — fresh Lead slot-1 lease read and accepted; it expires 2026-08-12T18:01:19Z and supersedes the expired dispatch. Work resumed at the audited cumulative count of 32 active minutes (the dispatch's 29-minute figure predates the logged 3-minute light check).

### 2026-08-12T17:12Z–17:17Z — fresh-leased focused enumeration

- Marked the fresh lease and superseded dispatch done, then archived both.
- Ran exactly the authorized command:

  ```bash
  timeout 600s gap -q Agents/Kourovka/problems/20.21/scratch/search-next.g > Agents/Kourovka/problems/20.21/scratch/search-next.out 2>&1
  ```

- Process exited normally with status 0, well before lease expiry. Full verbatim output is `scratch/search-next.out`.
- Exact orders and catalogue sizes observed: 288 (1,045 groups), 300 (49), 312 (61), 324 (176), 336 (228), 348 (12), 360 (162).
- Final observed line: `SUMMARY tested=1733 with_both=17 hits=0`.
- Exact meaning: all 1,733 GAP SmallGroups at those seven orders were tested; 17 ambient groups had at least one normal index-12 kernel with quotient `C12` and at least one with quotient `A4`; no cross-pair had equal `IdGroup` kernel identifiers.
- Together with `search-small-leased.out` (orders 12 through 240) and `search-gap-252-276.out`, this gives continuous exhaustive SmallGroups-library coverage of every multiple of 12 from 12 through 360 inclusive: 4,589 ambient groups total, no requested example. This is bounded evidence, not a proof for arbitrary finite groups.
- Active launch/inspection/reporting: 5 minutes; cumulative active minutes: 37. Compute runtime/wait excluded.

## Frattini-layer assignment

### 2026-08-13T18:04Z — setup and finite falsification criterion

- Resumed at cumulative active minute 37; safety stop 2026-08-13T19:47:56Z. Read Lead's assignment and Math Expert's `ideas/2026-08-13-c3-frattini-module.md`; processed and archived the dispatch.
- Work in the cited minimal-counterexample shape: `M=KL` is a normal 2-group of index 3, `M/K isomorphic C4`, and `M/L isomorphic V4`. A complement `C3` acts trivially on the first quotient and irreducibly on the second.
- On `V=M/Phi(M)`, the `C4` quotient contributes only its Frattini quotient `C2`: `K Phi(M)/Phi(M)` has codimension 1 with trivial `C3` quotient. Since `V4` is elementary abelian, `Phi(M) <= L` and `L/Phi(M)` has codimension 2 with irreducible `C3` quotient.
- This difference in ambient embeddings does not itself contradict `K isomorphic L`: an abstract isomorphism need not respect the ambient `C3` action or `K intersection L`.
- **Finite falsification criterion stated before compute:** restrict the recorded near misses to minimal-shape pairs (`|G|=3*2^n` and `M=KL` a 2-group). Compute ordinary Frattini dimensions `d(K)=dim_F2 K/Phi(K)` and `d(L)`. If any pair has `d(K)=d(L)`, the proposed universal first-layer generator-dimension obstruction is falsified. If all differ, that is bounded support only; a proof must still derive the inequality for arbitrary extensions. Separately compute induced `C3` module multiplicities/fixed dimensions as construction diagnostics, but do not treat their mismatch as an abstract-isomorphism obstruction.
- No compute lease requested: the recorded near-miss set is finite and the diagnostic is designed to finish under a 60-second light cap.

### 2026-08-13T18:05Z–18:08Z — falsification result and surviving identity

- Created `scratch/frattini-nearmisses.g`. Exact command: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/frattini-nearmisses.g' > 'Agents/Kourovka/problems/20.21/scratch/frattini-nearmisses.out' 2>&1`; exit 0.
- Exact scope: 25 recorded near-miss ambient IDs of orders 48, 96, and 192 (the orders of form `3*2^n`), all normal index-12 cross-pairs with the two target quotient IDs, retaining exactly those for which `M=KL` has index 3 and is a 2-group.
- Observed summary: `SUMMARY minimal_shape_pairs=48 equal_d=3`. Therefore the predeclared falsifier fired: ordinary first-layer dimension does not always distinguish the kernels.
- Equal-dimension cases observed:
  - In `SmallGroup(96,69)`, `K=SmallGroup(8,4)=Q8`, `L=SmallGroup(8,2)=C4 x C2`, and `d(K)=d(L)=2`.
  - In `SmallGroup(192,996)`, two symmetric subgroup pairs have `K=SmallGroup(16,12)=C2 x Q8`, `L=SmallGroup(16,10)=C4 x C2 x C2`, and `d(K)=d(L)=3`.
- Created `scratch/frattini-equal-pairs.g`. Its first run exited 0 at shell level but GAP aborted after reporting the first pair because `FrattiniSeries` is not an assigned GAP 4.12.1 function. The verbatim aborted output was overwritten by the corrected rerun; the observed error text was: `Error, Variable: 'FrattiniSeries' must have an assigned value`. Replaced it with an explicit iteration of `FrattiniSubgroup`.
- Corrected exact command: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/frattini-equal-pairs.g' > 'Agents/Kourovka/problems/20.21/scratch/frattini-equal-pairs.out' 2>&1`; exit 0. Full output is retained.
- Both equal-dimension types have matching full Frattini-series and lower exponent-2 central-series size sequences: `[8,2,1]` on the order-8 pair and `[16,2,1]` on the order-16 pair. Thus even all ordinary layer dimensions in these short series fail to separate them. Their lower central series do separate them because the `Q8` factor makes one kernel nonabelian while the other is abelian.
- For a Sylow-3 generator acting by conjugation, recorded equivariant Frattini signatures `[layer dimension, fixed dimension, irreducible multiplicity]` are:
  - `Q8`: `[[2,0,1],[1,1,0]]`; `C4 x C2`: `[[2,2,0],[1,1,0]]`.
  - `C2 x Q8`: `[[3,1,1],[1,1,0]]`; `C4 x C2 x C2`: `[[3,3,0],[1,1,0]]`.
  These distinguish the embeddings but are not invariants of the abstract groups without the action, so they cannot obstruct `K isomorphic L`.
- Surviving exact identity: put `d(X)=dim X/Phi(X)`, `eK=dim((K intersect Phi(M))/Phi(K))`, and `eL=dim(Phi(M)/Phi(L))`. Since `K Phi(M)/Phi(M)` has codimension 1 and `L/Phi(M)` has codimension 2 in `M/Phi(M)`,
  `d(K)=d(M)-1+eK` and `d(L)=d(M)-2+eL`.
  Hence an isomorphism `K isomorphic L` necessarily forces `eL=eK+1`. The three equal-dimension near misses realize exactly `eK=0,eL=1`, showing this cancellation is possible absent further structure.
- Assessment: the bare semisimple Frattini/Jennings-layer obstruction is falsified. A live refinement would have to prove that an actual isomorphic-kernel minimal counterexample cannot satisfy the correction equality, using power/commutator maps or extension compatibility; layer multiplicities alone are insufficient.
- Active reasoning, scripting, inspection, and reporting: 4 minutes; cumulative active minutes: 41.

## Active-time ledger (continued)

- 2026-08-13T18:08:06Z — stopped after completing the assigned structural test and reporting it through the bus; cumulative active minutes: 41. Cycle 1 remains nonterminal with 139 minutes available.

## Correction-equality continuation

### 2026-08-13T18:14:31Z — predeclared falsifier

- Began the explicitly authorized 30-active-minute continuation; safety stop 2026-08-13T19:00:00Z. Read and processed Lead's dispatch.
- Scope remains the 48 already recorded minimal-shape pairs; no SmallGroups order extension.
- Necessary correction equality for isomorphic kernels: `eL=eK+1`.
- **Predeclared finite falsifier:** among recorded pairs satisfying that equality, test whether derived- and square-subgroup orders necessarily distinguish the kernels. If any such pair has both `|K'|=|L'|` and `|K^2|=|L^2|`, the proposed power/commutator refinement is falsified. If all differ, this remains bounded support until an exact structural implication is derived.

### 2026-08-13T18:15Z–18:16Z — correction refinement result

- Modified only the existing recorded-pair diagnostic; no new ambient groups or orders were enumerated. Exact command: `timeout 60s gap -q 'Agents/Kourovka/problems/20.21/scratch/frattini-nearmisses.g' > 'Agents/Kourovka/problems/20.21/scratch/correction-refinement.out' 2>&1`; exit 0.
- Exact correction-equality population remained the three previously identified pairs: one in `SmallGroup(96,69)` and two symmetric pairs in `SmallGroup(192,996)`.
- In every one, observed derived orders are `[2,1]`, while square-subgroup orders are `[2,2]`.
- **Exact falsification:** the power-map refinement is false on all three correction-equality near misses: `|K^2|=|L^2|=2`. Thus equality of the correction terms plus the square-subgroup order does not force a contradiction.
- The conjunction `(derived order, square order)` still separates these three pairs only because `|K'|=2` and `|L'|=1`. This is bounded evidence, not a structural lemma.
- Reason no commutator lemma is claimed: `eK,eL` measure indices inside Frattini subgroups, while `Phi(X)=X^2 X'`; the correction equality does not separately control the power and commutator factors or their intersection. The observed cases themselves show identical square sizes alongside different derived sizes. No valid implication from `eL=eK+1` to `|K'| != |L'|` was derived.
- Verdict on assigned route: **dead at this level**. Bare layers were already falsified; adding square-subgroup data is now falsified; the remaining commutator mismatch is an unproved pattern from three pairs.
- Best genuinely different direction: classify compatible extension classes of the common normal subgroup `N` by `C4 x A4` (and retain the full-product branch unless minimality is independently proved), while allowing an abstract kernel isomorphism that need not preserve `N`. Equivalently, search for an isomorphism between the two preimage extensions, not for another characteristic-layer invariant. This is extension data, not an increased SmallGroups bound.
- Active work this continuation: 2 minutes. Continuation budget used 2/30; stopped early because the requested refinement was decisively falsified and no honest structural lemma survived.

## Active-time ledger (continued)

- 2026-08-13T18:16:13Z — continuation stopped and terminal route report sent to Lead; cumulative lifetime active minutes: 43. Safety stop respected.

## Counterexample direction — fresh-session cycle 1 continuation

Scope: `20.21/two-index-twelve-kernels`  
Assignment revision: `1`  
Direction: counterexample (theoretical nonexistence)  
Shared-ledger budget inherited: 105/180 active minutes used; 75 active minutes remain.  
Assignment `STARTED_UTC`: `2026-08-16T13:24:01Z`  
Acknowledged `SAFETY_STOP_UTC`: `2026-08-16T15:24:23Z`

### Active-time record

- `2026-08-16T13:25:21Z` — work start after reading the common protocol, canonical scope, and Lead's wall-clock correction; inherited cumulative total 105 active minutes.
- `2026-08-16T13:29:44Z` — running tally approximately 4 minutes in this continuation, approximately 109 cumulative. Work interval remains open.

### Context and resource boundary

- Discovery-blind boundary in force: no web search, no ordinary synthesis, no historical `log.md` inspection, no old transcripts/messages, no shared-chat material, and no pretrained recollection used as evidence.
- No delegation or subagent mechanism used.
- No GAP, Sage, solver, cohomology enumeration, catalogue search, or other heavy computation launched.
- Read `_meta/agents/Kourovka/_common-kourovka.md` in full, then the canonical scope record.
- Read only the supplied current inbox correction and the two extant named reviewed notes: the source-fidelity audit and scope-wide Goursat audit.
- The third authorized path, `Agents/Kourovka/problems/20.21/verification/2026-08-16T125904Z-q8-d8-order128-exclusions.md`, does not exist. A `QUESTION` was sent to Lead; similarly timestamped files were listed but not opened.
- Inbox archive move incident: after marking Lead's safety-stop correction `status: done`, `mv ... Agents/Kourovka/bus/archive/` returned `Read-only file system`. The processed file therefore remains in the inbox with `status: done`; Lead was already acknowledged by a separate `REPORT`.

## Staleness check

`source_transcription_checked: yes`  
`active_scope_checked: yes`  
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

### Source and rendered-form check

Machine-local path resolution command and observed output:

```text
$ source _meta/agents/Kourovka/paths.env && kv_now && printf 'AUTHOR=%s\\nPDF_RESOLVES=%s\\n' "$KOUROVKA_AUTHOR" "$([ -f "$KOUROVKA_PDF" ] && echo yes || echo no)"
2026-08-16T13:25:21Z
AUTHOR=operator
PDF_RESOLVES=yes
```

Navigation/transcription command:

```text
$ source _meta/agents/Kourovka/paths.env && pdftotext -f 148 -l 148 -layout "$KOUROVKA_PDF" -
20.21. (G. Verret). Does there exist a finite group G with two normal subgroups
K and L, each with index 12 in G, such that K is isomorphic to L, but G/K is
isomorphic to C12, while G/L is isomorphic to A4?                    M. Conder
```

I separately rendered physical PDF page 148 to `/tmp/kourovka-20-21-148.png` with `pdftoppm -f 148 -l 148 -png -r 180` and visually inspected the image. The typography confirms subscripts (C_{12}), (A_4), the two quotient assignments, both exact index-12 conditions, finiteness, normality, and abstract isomorphism. The problem is unstarred and has no displayed answer or comment.

Corrected transcription: **Does there exist a finite group (G) with two normal subgroups (K) and (L), each with index (12) in (G), such that (K\cong L), but (G/K\cong C_{12}), while (G/L\cong A_4)?**

Corpus record command: `rg -n ... Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl`. Observed flags: `answered: false`, `has_editor_comment: false`, `has_later_comment: false`. The corpus navigation field says page 150 while the canonical record and rendered PDF locate the statement on page 148; the mathematical text agrees exactly, so this is recorded as a corpus navigation-metadata discrepancy, not a target mismatch.

No web, arXiv, current-edition, or local solution-bearing search was performed. This is the mandated negative disclosure for the discovery-blind run.

### Clause matrix

| source clause | equivalent formulation | active scope? | literature result coverage |
|---|---|---:|---|
| Existence of finite (G\) with normal (K,L\), both index 12, (K\cong L\), (G/K\cong C_{12}\), (G/L\cong A_4\) | Existence of two epimorphisms (G\twoheadrightarrow C_{12},A_4\) whose kernels are abstractly isomorphic | yes: `20.21/two-index-twelve-kernels` | Deferred; no literature accessed in this discovery-blind run |

### Admissibility checklist reconciled to the scope record

| constraint_id | rendered-source requirement | reconciliation |
|---|---|---|
| `20.21-exists-GKL` | one existential triple ((G,K,L)) | exact match |
| `20.21-G-finite` | (G) finite | exact match |
| `20.21-KL-normal` | both (K,L\triangleleft G) | exact match |
| `20.21-both-index-12` | ([G:K]=[G:L]=12) | exact match |
| `20.21-kernels-isomorphic` | abstract (K\cong L) | exact match |
| `20.21-quotient-K-C12` | (G/K\cong C_{12}) | exact match; orientation checked |
| `20.21-quotient-L-A4` | (G/L\cong A_4) | exact match; orientation checked |
| `20.21-existence-conclusion` | at least one such triple exists | exact match |

No constraint mismatch was found. Excluded are unequal indices, merely equal kernel orders, wrong quotient types, and nonnormal subgroups.

## Strategy portfolio (written before sustained mathematics)

Ranked by expected certifiable information per active hour:

1. **Theoretical / characteristic-section descent (active).** Start from the reviewed Goursat alternatives ((K/N,L/N)=(A_4,C_{12})) or ((V_4,C_4)), (N=K\cap L). Test derived, power, Frattini, Fitting, transfer, and minimal-counterexample descent only where they are intrinsic under an arbitrary isomorphism (K\cong L). Kill if the argument needs the isomorphism to preserve (N), or if a concrete arbitrary extension defeats every quotient-forced invariant.
2. **Structured adversarial construction (falsification mode).** Design the smallest abstract group having both relevant quotient types with isomorphic quotient kernels. This does not pursue a witness outside the assigned direction; it stress-tests whether an alleged invariant really survives arbitrary extensions. A hand-checkable near miss kills overstrong obstruction claims.
3. **Catalogue/small-case mode.** No leased catalogue search is authorized. The only admissible bounded probe is hand classification of the tiny subdirect quotient/characteristic sections already forced by Goursat. A negative tiny-case result would exclude only that exact section, never all finite (N).
4. **Certificate plan.** A successful nonexistence argument must be a line-by-line finite minimal-counterexample proof: define a strictly smaller triple, verify all eight scope rows, and exhibit the strict order decrease. Any characteristic-section lemma must specify the functor, prove it is preserved by every abstract isomorphism, and show how Validator can reconstruct the contradiction without computation.

First named test: **full-product self-similar descent**, followed by **common-(C_3) intrinsic 2-section test**. At the 30-minute self-check, retain the route only if a quotient-forced invariant survives the fact that an isomorphism (K\cong L) need not carry (N) to itself.

### `2026-08-16T13:39:19Z` — candidate reductions from the first theoretical test

Running tally: approximately 14 active minutes in this continuation, approximately 119 cumulative. These are self-audited hand derivations and remain uncertified pending Validator review.

#### Candidate Lemma A — full-product strict descent

Assume a hypothetical witness is in the reviewed full-product branch. Thus, for (N=K\cap L),

\[
K/N\cong A_4,\qquad L/N\cong C_{12}.
\]

Choose an abstract isomorphism \(\theta:K\to L\), and inside the strictly smaller finite ambient group \(Q=K\) define

\[
K_1=\theta^{-1}(N),\qquad L_1=N.
\]

- (N\triangleleft L), so (K_1\triangleleft Q); also (L_1=N\triangleleft Q).
- Restriction of \(\theta\) gives (K_1\cong N=L_1).
- (Q/K_1\cong L/N\cong C_{12}).
- (Q/L_1=K/N\cong A_4).
- Both indices are 12 and (|Q|=|K|=|G|/12<|G|).

Hence every full-product witness contains a strictly smaller witness to the *same* active index-12 target. If any witness exists, a minimum-order one exists; it cannot be full-product and therefore lies in the common-(C_3) branch. Equivalently, existence for the active scope reduces to existence in the common-(C_3) branch. This does **not** say that no larger full-product witness could exist after a common-(C_3) witness exists.

I sent the exact normality/orientation/minimality question to Validator at `Agents/Kourovka/bus/inbox/Validator/2026-08-16T133345Z__Problem-20.21__QUESTION__minimal-witness-descent.md`.

#### What the common-(C_3) branch induces

Here

\[
K/N\cong V_4,\qquad L/N\cong C_4.
\]

With the same \(\theta\), put (M=\theta^{-1}(N)\triangleleft K). Then the smaller group (Q=K) has isomorphic normal subgroups (N,M) of index 4 with

\[
Q/N\cong V_4,\qquad Q/M\cong C_4.
\]

This index-four condition is consistent in isolation: take

\[
Q_0=\langle a\rangle\times\langle b\rangle\cong C_4\times C_2,
\quad N_0=\langle a^2\rangle,
\quad M_0=\langle b\rangle.
\]

Then (N_0\cong M_0\cong C_2), (Q_0/N_0\cong V_4), and (Q_0/M_0\cong C_4). This is **not** a witness to the active index-12 scope and is logged only as an adversarial hand-check. It shows that an obstruction based solely on the abstract index-four pair, or one silently requiring \(\theta(N)=N\), cannot work.

#### Candidate Lemma B — odd intersection kernels are excluded

If (|N|) is odd in the common-(C_3) branch, a Sylow 2-subgroup (P\le K) has order 4 and (P\cap N=1). Its image in (K/N\) therefore also has order 4, so (P\cong V_4). Likewise every Sylow 2-subgroup of (L) is isomorphic to (C_4). This is incompatible with (K\cong L), since an isomorphism carries Sylow 2-subgroups to Sylow 2-subgroups. Thus a common-(C_3) witness must have even (|N|). No catalogue or Schur–Zassenhaus input is needed.

#### Candidate Lemma C — an intrinsic odd-core reduction

In the common-(C_3) branch both (K/N) and (L/N) are 2-groups. Therefore

\[
O_{2'}(K)=O_{2'}(N)=O_{2'}(L)=:O.
\]

Indeed any normal odd-order subgroup of (K) or (L) maps trivially to the respective 2-group quotient and lies in (N); conversely (O_{2'}(N)) is characteristic in (N\triangleleft G), hence normal in (K,L). The common subgroup (O) is characteristic in both (K,L), so every \(\theta:K\to L\) satisfies \(\theta(O)=O\). If (O\ne1), the quotient triple ((G/O,K/O,L/O)) satisfies all active constraints and is strictly smaller. Consequently a minimum-order witness must satisfy

\[
O_{2'}(N)=1.
\]

This does not imply that (N) is a 2-group; odd composition factors can occur without a normal odd-order subgroup.

#### Candidate Lemma D — central intersection kernels are excluded

Assume additionally (N\le Z(G)). Because (L/N\cong C_4) is cyclic and (N\le Z(L)), (L) is abelian. Hence (K\cong L) makes (K) abelian too.

Let (g\in G) have image a 3-cycle in (G/L\cong A_4). In the common-(C_3) branch, conjugation by (g) fixes (N) pointwise, acts on (K/N\cong V_4) as the order-three automorphism cycling its three nonidentity elements, and acts trivially on (L/N\cong C_4).

For (V=K/N), define

\[
\delta:V\longrightarrow N/N^2,\qquad \delta(xN)=x^2N^2.
\]

Because (K) is abelian, this is a well-defined homomorphism of elementary abelian 2-groups. It is invariant under conjugation by (g), since (g) fixes (N) pointwise. The natural order-three action on (V\) has no nonzero invariant homomorphism to a trivial module: if the three nonzero vectors are (v,w,v+w) and all have common image (c), then (c=\delta(v+w)=c+c=0). Hence \(\delta=0\).

Choose lifts (x,y\in K) of a basis of (V). Since \(\delta=0\), write (x^2=n_x^2\), (y^2=n_y^2\) with (n_x,n_y\in N). Then (xn_x^{-1}) and (yn_y^{-1}) are commuting involutions whose images form a basis of (V). They generate a complement (V_4), so

\[
K\cong N\times V_4.
\]

Let (d_2(A)) denote the minimum number of generators of the Sylow 2-subgroup of a finite abelian group (A). The direct product gives (d_2(K)=d_2(N)+2). But (L/N\cong C_4) lets one generate the Sylow 2-subgroup of (L) using generators of the Sylow 2-subgroup of (N) plus one lift, so (d_2(L)\le d_2(N)+1). This contradicts (K\cong L). Therefore any common-(C_3) witness must have (N\not\le Z(G)).

The same calculation gives a weaker representation-changing statement when merely (N\le Z(KL)): the order-three conjugation acts on (N/N^2), and \(\delta\) is equivariant. If \(\delta=0\), the same generator-rank contradiction follows. Hence such a witness would force a nonzero (therefore injective) copy of the natural 2-dimensional \(\mathbf F_2C_3\)-module inside (N/N^2). I have not established that this remaining module case is impossible.

#### Intrinsic-invariant audit so far

- **Derived subgroup:** in the full branch, (K'N/N\cong V_4) while (L'\le N); in the common branch both derived subgroups lie in (N). Isomorphism preserves the abstract orders/types of (K',L'), but not their positions relative to the unpreserved (N), so this alone gives no contradiction.
- **Power subgroup:** in the common branch (K^2\le N), while (L^2N/N\cong C_2). The adversarial (C_4\times C_2) example realizes exactly this positional mismatch, so the square subgroup alone is not an obstruction.
- **Frattini subgroup:** for finite 2-groups, Φ commutes with quotients, but the same (C_4\times C_2) example has Φ equal to the kernel of the (V_4) quotient and not the kernel of the (C_4) quotient. Again, the isomorphism need not preserve the selected kernel.
- **Fitting subgroup and composition factors:** both quotient pairs have compatible composition factors; images of Fitting subgroups give only necessary inclusions and need not fill the quotient.
- **Transfer:** transfer maps depend on the selected subgroup and therefore are not intrinsic to the abstract group (K\cong L); the index-four adversarial example prevents treating their target placement as invariant.

Current judgement: full-product descent and the odd-core/central-kernel exclusions are checkable partial reductions. A scope-wide characteristic obstruction has not survived arbitrary (N); the remaining leverage is the external order-three action on characteristic 2-sections of (N), not the quotient pair alone.

### `2026-08-16T13:42:03Z` — correction/strengthening of Candidate Lemma D

Running tally: approximately 17 active minutes in this continuation, approximately 122 cumulative.

The preceding central-(N) argument is superseded for use by the following stronger and cleaner candidate lemma. The earlier special-case derivation remains a valid consistency check, but the new argument needs neither (N\le Z(G)) nor a choice of square roots.

#### Candidate Lemma D′ — the two kernels cannot be abelian

Assume a common-(C_3) witness and choose θ as above. Set

\[
Q=K,\qquad M=\theta^{-1}(N).
\]

Then (N,M\triangleleft Q), (N\cong M), and there are quotient maps

\[
f_N:Q\twoheadrightarrow V_4\quad(\ker f_N=N),
\qquad
f_M:Q\twoheadrightarrow C_4\quad(\ker f_M=M).
\]

Suppose (Q) is abelian. Choose (g\in G) whose image in (G/L\cong A_4) is a 3-cycle. Conjugation by (g) restricts to an automorphism τ of (Q=K), preserves (N\triangleleft G), and induces on (Q/N\cong V_4) the order-three automorphism that cyclically permutes all three nonzero elements. Thus this quotient is an irreducible τ-module over ℝ? No: over \(\mathbf F_2\).

For (j\ge1), write

\[
Q[2^j]=\{x\in Q:x^{2^j}=1\}.
\]

This is a characteristic subgroup of the finite abelian group (Q). Hence (f_N(Q[2^j])) is a τ-invariant subgroup of the irreducible (V_4), and therefore

\[
|f_N(Q[2^j])|\in\{1,4\}.
\]

On the other hand,

\[
|N[2^j]|=\frac{|Q[2^j]|}{|f_N(Q[2^j])|},\qquad
|M[2^j]|=\frac{|Q[2^j]|}{|f_M(Q[2^j])|}.
\]

Because (N\cong M), the left sides are equal for every (j); consequently

\[
|f_N(Q[2^j])|=|f_M(Q[2^j])|\quad\text{for every }j.
\]

Surjectivity of (f_M) supplies a 2-power-order element mapping to a generator of (C_4), so there is a least (j\ge2) with (f_M(Q[2^j])=C_4). If (x\in Q[2^j]) maps to a generator, then (x^2\in Q[2^{j-1}]) maps to the unique involution of (C_4). By minimality of (j),

\[
|f_M(Q[2^{j-1}])|=2.
\]

This contradicts the equality with the corresponding (f_N)-image, whose order can only be 1 or 4. Therefore (K\cong L) cannot be abelian in a common-(C_3) witness.

Since (L/N\cong C_4) is cyclic, (N\le Z(L)) would make (L) abelian. Thus every witness must in particular satisfy

\[
N\not\le Z(L),
\]

and the earlier exclusion of (N\le Z(G)) follows. This still does not exclude nonabelian kernels, and it does not claim that (N) is characteristic under θ.

Typographical correction to the module sentence above: “irreducible τ-module over ℝ?” is a drafting artifact; the field is exactly \(\mathbf F_2\), as stated immediately after it. This appended clarification preserves the log's append-only rule.

### `2026-08-16T13:44:24Z` — early kill-criterion checkpoint

Running tally: approximately 19 active minutes in this continuation, approximately 124 cumulative.

Lead's unread strict-kill decision and corrected curated-note path appeared on the inbox poll and were processed. The authorized third note, `Agents/Kourovka/problems/20.21/verification/2026-08-16T125904Z-q8-d8-order128-audit.md`, was read. Its certified boundary is exactly the Q8/D8 common-kernel order-128 equivariant template; it explicitly does not cover abelian order-eight kernels, larger auxiliary groups, or the whole scope. Nothing in this fresh run promotes those bounded exclusions to global evidence.

Self-check against Lead's criterion:

- Active scope/revision: `20.21/two-index-twelve-kernels`, revision 1.
- New checkable facts: full-product strict descent; evenness of (N) in a minimum/common-(C_3) witness; removable common (O_{2'}(N)); exclusion of abelian coordinate kernels via the 2-power torsion filtration.
- Current named strategy: characteristic-section obstruction across the Goursat branches.
- Ruled out: quotient-only derived/power/Frattini/Fitting arguments; any argument requiring θ to preserve (N); abelian (K\cong L); odd (N); central (N).
- Bottleneck: for nonabelian kernels, no characteristic subgroup has been shown to coincide as an actual subgroup of both (K) and (L) for arbitrary (N).
- Alternative 1: return to the uncovered structured construction families with abelian common kernel (N) but nonabelian coordinate kernels.
- Alternative 2: a separately authorized equivariant extension/module analysis of the order-three action on characteristic 2-sections of (N).
- Recommended next experiment: none in this direction; close it as `PARTIAL_RESULT` and let Lead reschedule the remaining shared ledger.
- Kill criterion: met. There is no arbitrary-common-kernel obstruction eliminating an entire Goursat branch; the valid descent is a reduction, not nonexistence.
- Admissibility: no proposed triple exists in this direction, so there is no constraint matrix for a candidate and `active_assignment_answered: no`.

The same decision summary was sent to Lead as a `CHECKPOINT`. Only cheap proof auditing and outcome packaging continue; no new mathematical route will be opened.

## Cycle outcome — `PARTIAL_RESULT`

`2026-08-16T13:48:35Z` — active work stop. This continuation used approximately 23 active minutes (from `2026-08-16T13:25:21Z`), bringing the shared cumulative ledger from 105 to approximately 128/180 active minutes. Approximately 52 active minutes remain for Lead to schedule. The wall-clock safety cap was not approached.

Exactly one outcome is reported for this stopped direction: **`PARTIAL_RESULT`**.

The clean computation-free write-up is:

`Agents/Kourovka/problems/20.21/scratch/2026-08-16-counterexample-direction-partial-result.md`

Result boundary:

- A minimum-order witness must be common-(C_3), with ((K/N,L/N)\cong(V_4,C_4)).
- It must have even (|N|) and (O_{2'}(N)=1).
- Its isomorphic coordinate kernels (K,L) must be nonabelian; in particular (N\not\le Z(L)).
- The active existence target remains unanswered. No witness was constructed and no nonexistence result was obtained.
- The characteristic-section strategy met Lead's kill criterion because no invariant valid for arbitrary (N) eliminates the surviving common-(C_3) branch.
- A representation-changing pivot did occur: quotient-position tests were replaced by strict self-descent and the intrinsic 2-power torsion filtration. The remaining nonabelian arbitrary-extension case survives that pivot.
- Validator questions on the full-product descent and abelian-kernel exclusion were pending at stop; all new mathematics remains `status/conjectured`.

No claim-check JSON or state-check invocation was made because this is not `CLAIM` or `STALE_MATCH`. A final `REPORT` with this exact outcome was sent to Lead. Work on this direction is stopped.
