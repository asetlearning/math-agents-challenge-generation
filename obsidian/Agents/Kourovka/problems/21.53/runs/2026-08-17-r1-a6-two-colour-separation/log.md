---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/graph-automorphisms
  - project/kourovka
  - status/draft
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: counterexample
run_dir: Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation
---

# Problem 21.53 — fresh A6 two-colour separation run

## Active-time ledger

- 2026-08-17T18:53:01Z — active work started; cumulative active minutes: 0.
- 2026-08-17T18:56:00Z — source/staleness gate recorded; cumulative active minutes: 3.

## Staleness check

Date: 2026-08-17. Scope revision 2. This is a discovery-blind run: open-web search and solution-bearing local history are forbidden by the canonical scope. Accordingly, `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. I did not inspect Problem 21.52 work, historical Problem 21.53 logs/findings/verification, synthesis prose, archived research messages, or web results.

Source read: the configured rendered Kourovka PDF, page 172, headed “New Problems (21st issue, 2026)”. I rendered the page at 180 dpi and visually checked the complete statements of 21.52 and 21.53, including symbols, subscripts, quantifiers, and the intersection over all `t`. The page presents 21.53 as a new problem and contains no editor or later-answer comment. The vault only contains the issue-20 corpus JSONL, so there is no issue-21 corpus row from which `answered`, `has_editor_comment`, or `has_later_comment` flags could be read; those three corpus flags are therefore unavailable, not silently inferred. The current configured source itself shows no answer annotation. No plausible stale match arose within the permitted resources.

`source_transcription_checked: yes`

Corrected transcription: In the notation of 21.52, `L` is a finite non-abelian simple group, `D` is one conjugacy class of involutions in `L`, and `Gamma` is the complete graph on `D`, with two edges equivalent precisely when the products of their endpoints have equal order. For every positive integer `t`, `Aut_t(Gamma)` is the set of `tau in S_D` such that a `t`-edge is sent to an equivalent (hence `t`) edge. The source states `Aut(Gamma) = intersection_t Aut_t(Gamma)` and asks whether, for every finite simple group `G` in this inherited notation, `Aut(Gamma) = Aut_2(Gamma) intersection Aut_p(Gamma)`, where `{2,p}` are the two smallest prime divisors of `|G|`. Revision 2's independently audited identification `G=L` and inherited non-abelian-simple restriction is used; no solution-bearing 21.52 material was consulted.

### Clause matrix

| source clause | equivalent formulation | in active scope? | stale-result status |
|---|---|---:|---|
| inherited notation of 21.52 | one involution conjugacy class `D` in finite non-abelian simple `L`; complete product-order-coloured graph | yes | no permitted external result inspected; current source has no answer comment |
| definition of `Aut_t` | permutations preserving the `t`-edge set; if the set is empty, the condition is vacuous | yes | same |
| `Aut(Gamma)=intersection_t Aut_t(Gamma)` | full colour-preserving group | yes | same |
| two-minimal-prime equality question | `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)` for second-smallest prime `p` | yes | same |

`active_scope_checked: yes`

### Admissibility reconciliation

| constraint id | rendered-source / audited-scope check | result |
|---|---|---|
| 21.53-forall-L-D | universal pair `(L,D)` inherited from 21.52 and 21.53's “for every” | match |
| 21.53-L-finite-nonabelian-simple | explicit in inherited 21.52 notation | match |
| 21.53-D-single-involution-class | explicit in inherited 21.52 notation | match |
| 21.53-Gamma-product-order-colouring | visually checked equivalence iff product orders agree | match |
| 21.53-Aut-t-definition | visually checked for every positive integer label `t`; nonoccurring labels are vacuous | match |
| 21.53-two-minimal-primes | visually checked `{2,p}` are the two minimal prime divisors | match |
| 21.53-full-colour-group-definition | visually checked intersection over all `t` | match |
| 21.53-two-colours-determine-all | exact equality asked | target conclusion |

No mismatch between the rendered source and canonical revision 2 was found. Mathematics may begin only after this gate.

## Strategy portfolio

Ranked by expected information in the 45-minute reconnaissance:

1. **Catalogue/small-case — A6 class 2A incidence encoding.** Reconstruct `A6` as even permutations of six letters and `D` as the 45 double transpositions. First count exact occurring product orders. If at most three colours occur, preservation of the 2- and 3-edge sets determines the remaining edge set by complementation, so this instance is rejected as tautological and the lane switches to `PSL(2,8)` as assigned. If at least four occur, encode the 2- and 3-edge relations as a vertex-coloured incidence graph and ask nauty for its automorphisms. A negative result proves only equality for this one pair.
2. **Structured construction — support-intersection action.** Classify ordered pairs of double transpositions by the overlap pattern of their fixed-point pairs/matchings. Try to design a permutation of the 45 matchings that fixes the relations corresponding to product orders 2 and 3 but swaps the 4/5 relations. This may expose an exceptional outer-automorphism geometry without a catalogue expansion.
3. **Theoretical — relation recovery.** Determine whether the 4- and 5-relations are first-order/combinatorially reconstructible from the 2- and 3-relation graphs through common-neighbour counts. If so, equality follows for this pair and explains an exact singleton equality without promoting it to the universal statement.
4. **Certificate plan.** A counterexample candidate must identify all 45 double transpositions, the full 45-by-45 product-order matrix, `p=3` from `|A6|=360`, and an explicit permutation of vertex indices. A standalone verifier will exhaustively check every 2- and 3-edge and exhibit a concrete edge whose order changes. The nauty search and verifier will be frozen with hashes and require a Lead compute lease before execution.

Initial kill rule: if A6 has at most three occurring colours, switch immediately to `PSL(2,8)`; if the exact two-colour group equals the full-colour group and relation-recovery statistics explain this, return bounded singleton evidence rather than enlarge an unleased catalogue.

## A6 hand reconstruction before exact computation

2026-08-17T19:00:24Z; cumulative active minutes: 7.

`|A6|=6!/2=360=2^3*3^2*5`, so its two smallest distinct prime divisors are 2 and `p=3`. Every nonidentity involution in `A6` has cycle type `2^2 1^2`: one transposition is odd and three transpositions are odd, while two are even. This `S6` class does not split in `A6` because its centraliser contains odd permutations, hence it is one `A6` class `D` of size `6!/(2^2 2! 2!)=45`.

Fix `x=(12)(34)`, with fixed points 5,6. For another double transposition `y`, the intersection of its four-point support with `{1,2,3,4}` has size 2, 3, or 4.

- Intersection 4: the two other matchings on the same support commute with `x`, giving two order-2 products.
- Intersection 2: there are 18 choices. If the common pair is one of `{1,2}` or `{3,4}`, one matching commutes and two give order 4, contributing 2 of order 2 and 4 of order 4. If the common pair takes one point from each `x`-pair, one matching gives order 4 and two give order 3 for each of four supports, contributing 4 of order 4 and 8 of order 3.
- Intersection 3: there are eight supports (choice of the omitted old point and included fixed point). For each, the matching sharing the complete old transposition gives order 3, and the other two yield an alternating five-vertex path and hence a 5-cycle product. This contributes 8 of order 3 and 16 of order 5.

Thus each vertex has colour degrees `(k_2,k_3,k_4,k_5)=(4,16,8,16)`, summing to 44, and all four colours 2,3,4,5 occur. The assigned at-most-three-colour tautology rejection does **not** fire; `PSL(2,8)` is therefore not entered. For comparison, if only three colours occurred, preserving the 2- and 3-edge sets would preserve their complement, the third colour, automatically. Four colours leave the union of the 4- and 5-edges as one complement and do not distinguish its two parts.

The exact computation is frozen but has not been run. Manifest: `scratch/compute-manifest.md`. Frozen SHA-256 values: generator `b23f6a8e09f6ff8a4957484eec3de527664ab9556a9a5e682f7603397746195a`, parameter input `e0b6ecf6752967c10a2d04009ce044ca3b0b5c89d36d04a3b4f6e5a893e966c5`, wrapper `61d85e072dc93ef60b60f63a1b508308438d030407d9c7380f12f73d1ecf2a6e`. No finite-model computation has been executed.

## Structural expectation while lease is pending

2026-08-17T19:01:41Z; cumulative active minutes: 9. Lease waiting time begins after this entry and is uncharged.

A double transposition has a useful flag model. For `x=(ab)(cd)` with fixed duad `ef`, let its syntheme be the partition `{ab,cd,ef}` of the six points. Thus the 45 vertices are exactly the incident flags `(duad, syntheme)` in the 15-by-15 duad–syntheme incidence geometry.

The four order-2 neighbours found above have a precise interpretation: two flags share the fixed duad and two share the syntheme. Hence the colour-2 graph is the line graph of the connected bipartite incidence graph between 15 duads and 15 synthemes, each of degree three. Its maximal triangles recover the 30 incidence-graph vertices, so every colour-2 automorphism induces an automorphism of that incidence graph.

Any incidence-graph automorphism either preserves its bipartition or swaps the two parts. A bipartition-preserving automorphism restricts on duads to an automorphism of the disjointness graph on the 2-subsets of a 6-set: two duads lie in a common syntheme exactly when they are disjoint. The six maximum independent 5-sets consisting of all duads through one point recover the six underlying points, giving at most `6!=720` such automorphisms. Allowing a part swap gives the hand upper bound `|Aut_2(Gamma)| <= 1440`.

This strongly predicts singleton equality: the standard fact `|Aut(A6)|=1440` would give 1440 faithful product-order-preserving permutations on the unique involution class, forcing the colour-2 group already to equal the full-colour group. I am treating this as a theoretical expectation, not certified evidence: the leased exact comparison will independently determine the two relevant group orders, and a Validator route should either justify the standard automorphism-group fact or reconstruct all 1440 incidence symmetries.

## Leased exact A6 determination

Lease waiting from 2026-08-17T19:01:41Z to 2026-08-17T19:02:13Z was uncharged. Lead granted slot 1 through 2026-08-17T19:04:13Z for one invocation only. The exact authorized command was run once from the vault root:

`timeout 55s bash Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/run_a6_exact.sh`

The outer command exited 0 after 0.36 wall seconds. File timestamps place the completed outputs at 2026-08-17T19:03:10Z. Both nauty stderr files have size zero. Slot 1 was released to Lead at 2026-08-17T19:03:29Z.

Observed build summary:

- software: Python 3.12.3 standard library and dreadnaut/nauty 2.8.8;
- exact object: all 360 even permutations of six points and all 45 cycle-type `2^2 1^2` elements;
- the enumerated conjugation orbit of one vertex is the complete 45-element list;
- `p=3`; product-order colours `[2,3,4,5]`;
- common degrees by colour `(4,16,8,16)` and unordered edge counts `(90,360,180,360)`;
- complete matrix SHA-256 `e16df34378e87aa57e4bac7b6094eab1507b27e66fe36e7939ba9fb26d8f2932`;
- vertex-list SHA-256 `e2c3f4358d7363675978f3d43a0663f0d875e53f15707960d9d7290c6e14870d`;
- two-colour dreadnaut input SHA-256 `49d1c023fa08d54f0148d4bb3d53ac3790eaf0d9eaad2ae61caf23b515da2e1c`;
- full-colour dreadnaut input SHA-256 `76718524627e2939c73484d44683590b215dbd8102321dd38898ed926a1a09df`;
- two-colour nauty output SHA-256 `e0e929d8b3046d7541ea45c209c25ed4faa8868f4496cab0e7f4c84f15d562fa`;
- full-colour nauty output SHA-256 `afd912b1389cade3d561bfd60f8275715e42fbe3e059108a9611500e4b141434`.

The 495-vertex incidence encoding for the 2- and 3-edge sets reports `3 orbits; grpsize=1440; 6 gens; 16 nodes; maxlev=4`. The 1035-vertex encoding with separate cells for all four edge colours reports `5 orbits; grpsize=1440; 6 gens; 16 nodes; maxlev=4`. Each auxiliary vertex has a unique unordered pair of original neighbours and auxiliary cells are separated by edge colour, so restriction to the first 45 vertices identifies the augmented-graph groups exactly with `Aut_2(Gamma) intersection Aut_3(Gamma)` and `Aut(Gamma)`, respectively. The latter is a subgroup of the former; equal finite order 1440 therefore gives equality for this one pair.

No explicit separating permutation exists in the computed two-colour group, so the counterexample-candidate gate does not open. This is **bounded evidence only** for `(A6,2A)` and does not establish the source's universal assertion.

## Cycle outcome

`PARTIAL_RESULT`: a complete reproducible finite determination for `(L,D)=(A6,2A)`, supported by the exact matrix, two independently specified relation encodings, equal nauty group orders, and the duad–syntheme structural explanation. The named A6 separation strategy is exhausted: it yields equality, not a counterexample. The assigned fallback to `PSL(2,8)` was conditional only on A6 having at most three colours; because A6 has four, I do not pivot there without a new Lead decision.

- 2026-08-17T19:04:21Z — charged inspection completed; cumulative active minutes: 12.
- 2026-08-17T19:04:21Z — active research stopped in `awaiting_lead`; 33 of the allocated 45 active minutes returned unused.

## Ledger correction after required handoff writing

The 2026-08-17T19:04:21Z stop was provisional: writing `findings.md` and the Lead/Validator handoff messages is charged work and resumed immediately. Final stop: 2026-08-17T19:06:30Z; cumulative active minutes: 14. The lane is `awaiting_lead`, and 31 of 45 allocated active minutes are returned unused.
