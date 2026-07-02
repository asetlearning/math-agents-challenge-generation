---
title: B(2,5) Progress Note
domain: group-theory
project: b25
instance: B(2,5)
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/kbmag, topic/proof-search, project/b25, status/inconclusive, experiment]
last_updated: 2026-06-30 (PatternBoost/axplorer B(2,5) loop pre-reg CO-AUTHORED and routed to Lead Dev for Maria GO gate. Developer + B25 Experimenter sign-off complete. Scope: comm_13_10 compressed (260 chars, baseline=258), cooperation gain > 0 metric, GAP-verified. Awaiting Maria.)
---

# B(2,5) Standing Progress Note

Last updated: 2026-06-25 by B25 Experimenter. Bridge Cancellation Line complete. See [[Agents/Experimenter-B25/output/b25-bridge-cancellation-2026-06-25]]. Previous: Compressed KB Option (a) — see [[Compressed KB/methodology/compressed-kb-option-a-biased-2026-06-23]].

---

## Current question

**REFRAMED 2026-06-26 (Validator verdict)**: ALL 119 HWW benchmark words are IDENTITY in B(2,5). Confirmed by Validator via GAP EpimorphismPGroup: word_7245 = 1, comm_12_9 (original) = 1, 30/30 sampled benchmark words = 1.

The problem is NOT geodesic distance from identity to a non-trivial element. It IS:

> **Dehn-function / relator-complexity**: given a word w that equals identity in B(2,5), find the shortest word w' such that w' = 1 in B(2,5) and w' can be derived from w by a bounded-length proof sequence. Equivalently: what is the minimum-length identity certificate for comm_12_9?

This reframes word_7245 (7,245 chars) as: "a 7,245-char identity certificate — can we find a shorter one?" The Dehn function of B(2,5) bounds the answer: is there a polynomial-length proof that word_7245 = 1?

**Maria's pivot decision is pending**: (a) find non-trivial B(2,5) elements, or (b) accept the Dehn-function reframing and redirect all shortening work accordingly.

---

## What's been tried

| Experiment type | Status | Top-line outcome | Vault note |
|----------------|--------|-----------------|-----------|
| **KBMag** (RPO+shortlex mixing) | #status/inconclusive | Both agents stayed in EXPLORATION; no cascade at 30min; 3 injections (2,263 rules total). v2 (bisect) is 10x more memory-efficient and 15x faster injections. | [[KBMag/methodology/kbmag-overlap-scoring-b25-2026-05-22]] |
| **Rust Bidirectional** (dual-RPO, beam) | #status/inconclusive | 9 surviving runs across 3 passes (2026-03-20 through 2026-03-30). Targets: comm_22_3, comm_11_1_kyr, comm_13_10, lifted comm_12_9. Best reductions: comm_22_3 4162→4156, comm_13_10 2500→2494, lifted comm_12_9 1772→544 (gen_braid only). No words proved. Code deleted from disk; configs at git bc3cba2. | [[Rust Bidirectional/methodology/rust-bidirectional-b25-2026-05-22]] |
| **Reduce Core** (pipeline: power→braid→rules→beam) | #status/inconclusive | comm_12_9: **7,245 chars** (74.7% reduction, abelianization (0,0) ✓). Previous "3,707" result INVALIDATED (braid_reduce_fast bug). | [[Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22]] |
| **Biased KB Agents** (kbprog biased on target patterns) | #status/inconclusive | 12 surviving rule banks (run4, run5, weq series). ALL on INVALID targets (word_3705/3707). 1.8M rules largest single bank (run4-sl-k12). Valid runs on word_7245 not yet performed. | [[Biased KB Agents/methodology/biased-kb-agents-b25-2026-06-03]] |
| **RL Mixer** (PPO-trained word reduction agent) | #status/inconclusive | 3 trained checkpoints (comm_12_7, comm_16_2, rpo); no evaluation results preserved. | [[RL Mixer/_progress]] |
| **PatternBoost** (transformer + local search alternating loop) | #status/pending | Deliverable #1 GO (r=0.949). Pre-reg co-authored with Developer 2026-06-30. Awaiting Maria GO for first run. Seed: comm_13_10 compressed (260 chars, baseline=258). Metric: cooperation gain > 0, GAP-verified. | [[PatternBoost/methodology/patternboost-b25-loop-prereg-2026-06-30]] |
| **Compressed KB** (6-gen {a,b,m,M} alphabet, CoreA=m, CoreB=M) | #status/inconclusive | Two runs (unbiased + biased). Biased run (k=5, sp=0.5, 90s): 109 m/M-in-LHS rules (median LHS=8), NONE fire on compressed target. Fundamental mM→ε rule exists but requires adjacent CoreA·CoreB in word_7245 (not present). Both guards held. | [[Compressed KB/methodology/compressed-kb-option-a-biased-2026-06-23]] |
| **Bridge Cancellation Line** (junction rule CoreA·X·CoreB→X for each bridge X) | #status/replicated | 17 bridge patterns enumerated from 153 junctions in word_7245. GAP EpimorphismPGroup (B(2,5) order=5^34 exact): ALL [CoreA,X] non-identity order-5. No bridge is in C_{B(2,5)}(CoreA). Zero reduction possible. **Validator replicated** (2026-06-25, two independent GAP runs). | [[Agents/Experimenter-B25/output/b25-bridge-cancellation-2026-06-25]] |
| **Centralizer Beam Reduction** (beam-reduce all 34 small centralizer elements) | #status/conjectured | 34 non-trivial elements of C_{B0(2,5)}(CoreA) with FSA len <20K. **True min: 4998 chars (gen_8)**. 27/34 improved. Structural: gen_k^3=gen_k^{-2} and gen_k^4=gen_k^{-1} confirmed by beam (greedy FSA missed these). gen_8^4→4998 (saved 14,988!), gen_1→8549, gen_7→5138, gen_4→6867, gen_5→7745. All 7 unchanged elements are pure gen_8/gen_9 products. 27 shortened words pending GAP word-equality. **ITEM 2b signal**: min confirmed element ≥4998 chars — too long for most reshape operations. | [[Centralizer/results/cent-beam-reduce-results-2026-06-26]] |
| **Fragment Shortening Hunt** (REOPEN of bridge line — full finite enumeration) | #status/complete | 318 connector fragments from all 119 words → 326 junction tests. 500K shortlex KB (leftmost) + beam (16384 width, ≤300s): **31 seed rules** (junction-level reductions, all GAP-verified). word_7245: 0 savings. 648 chars across 37/119 other words. All beam null results. | [[Agents/Experimenter-B25/output/b25-fragment-seed-rules-2026-06-25]] |
| **Proxy Validation** (B(3,3) lab → B(2,5) transfer) | #status/completed | v2 ran 2026-06-18: H1 NOT SUPPORTED, H2 NOT SUPPORTED. LCS-weight-2 (proxy D) gives ρ=0.079 on γ₂\γ₃ (threshold 0.40; far below). D is completely blind on [G,G] just like A and B. Transfer decision: keep Option B. LCS approach to [G,G] blind class fails at B(3,3) lab level. | [[Proxy Validation/results/b33-proxy-results-v2-2026-06-18]] |
| **Proxy Validation v3 pilot** (C2 quotient ensemble + Arm 1 periodicity + Arm 3 descent) | #status/failed-distortion | Pilot COMPLETE 2026-06-19: ALL 119 benchmark words give d=0 in Q2,Q3,Q4. Words live in γ₅ — beyond Q4=B(2,5)/γ₅. Q4 actual diam=**19** (not ~80–200 estimated). Arm 1 and Arm 3 also give 0. GATE B cannot be evaluated: no words in target length regime AND identity-collapse on actual pool. C2 proxy (Q2–Q4) structurally fails on the actual corpus. Need Q5=B(2,5)/γ₆. | [[Agents/Experimenter-B25/output/proxy-validation-v3-pilot-2026-06-19]] |
| **Proxy Validation v4 / quotient-metric** (ALL approaches targeting 119 HWW words) | **#status/disproven** | **FROZEN 2026-06-26** (Validator GAP verdict). ALL 119 HWW benchmark words = identity in B(2,5). word_7245 = 1. Cayley distance from identity = 0 for ALL words → no quotient metric can apply. Corpus augmentation fix, v4 Stage-1, R1, R3 all HALT. Q5 feasibility question → Validator (already routed; answer: moot if all words are identity). B(3,3) lab survival as INDEPENDENT study pending Maria's reframing decision. | [[Proxy Validation/methodology/proxy-validation-stalled-state-review-2026-06-26]] |
| **Proxy Validation v4 Stage 1** (B(3,3) Arms 0,1,3 lab — independent of frozen B(2,5) stream) | #status/complete | **2026-06-27 COMPLETE.** All 80 stratum III ([G,G]) corpus words are at geodesic length (len=dist, 80/80). Arms 0 (greedy KB), 1 (period-excess), 3 (bounded-descent) all score 0 on all stratum III words → ρ=NaN on stratum III. H4-1 (total_shrink_T16 ρ≥0.20 on stratum III) FALSIFIED. On stratum II: Arm1 ρ=0.205 (passes threshold), Arm0 ρ=0.104, Arm3 ρ=0.085. Blind spot is STRUCTURAL: corpus words are shortlex NF → irreducible by construction. | [[Proxy Validation/results/b33-proxy-v4-stage1-results-2026-06-27]] |
| **Proxy Validation v4 Stage 2** (B₀(2,5)/Q5 Arms 0,1,3 + PC lab) | #status/complete | **2026-06-29 COMPLETE.** Q5 diameter=20. 3609 words, 324 stratum-III non-geodesic [G,G] words. **Arm0**: blind (seed rules too long for corpus). **Arm1**: ANTI-correlated ρ=−0.292 on stratum III (K=8) — sign INVERTED vs hypothesis; high periodicity-excess → CLOSER to identity (words collapse under u^5=1). **Arm3 shrink**: ρ=+0.110, 81% blind. **PC first_nonzero_layer**: ρ=+0.210 (ONLY arm passing H5 threshold ≥0.20). All 5 H5 hypotheses fail on pre-specified thresholds. Open questions for Lead: Arm1 sign-flip; PC extension; Stage 3. | [[Proxy Validation/results/b0-proxy-v4-stage2-results-2026-06-29]] |
| **Proxy Validation v4 Stage 2b** (−arm1 periodicity-deficit confirmatory; target=reducer_delta) | #status/complete | **COMPLETE 2026-06-29.** H6-1: FAIL (ρ=−0.358, anti-correlated). H6-3: FAIL (ρ=−0.289). Fresh-corpus ρ(−arm1_K4, d_Q5)=−0.082 — Stage 2 in-sample +0.33 does NOT replicate. Reducer blind rate = 0% on stratum III (100% of [G,G] words reduced). **KEY FINDING**: braid_reduce is effective EXACTLY on words close to identity (high periodicity-excess) — OPPOSITE direction from d_Q5 proxy. Proxy retired: Q5 direct measurement (9.77M table persisted, 214MB) is better than any proxy. | [[Proxy Validation/results/b0-proxy-v4-stage2b-results-2026-06-29]] |

---

## What's worked

- **X-core compression**: the 35-char pattern X = `ABabAbabABaBAbabABABabAbaBABaBAbabb` appears ~34× in comm_13_10 (2,500 chars) and allows lifting comm_12_9 from 28,652 to 544 chars. The compression is ~98% before re-expansion. This dramatically reduces the search space.
- **Pipeline reduction**: power + braid + greedy rules + Rust beam achieves 74.7% reduction of comm_12_9 (28,652 → 7,245). This is the best validated result.
- **Large rule bank**: merging 12+ KB runs (multiple orderings, multiple sessions) into a 25.7M rule master bank. Biased runs (kbprog seeded on target word) add domain-specific rules.
- **v2 mixing (bisect)**: 10x less memory than Aho-Corasick at 13M rules, enabling sustained long runs on B(2,5) that were previously memory-limited.

---

## What's stuck

| Problem | What would unblock it |
|---------|----------------------|
| comm_12_9 plateaus at 7,245 chars | **REFRAMED**: word_7245 is an identity certificate. Shortening it = finding a shorter proof that comm_12_9 = 1. Dehn-function tools and identity-certificate compression are the correct frame. |
| ~~Compressed KB rules don't fire~~ | **SHELVED 2026-06-25** (Lead directive). ADR filed. |
| KBMag: no cascade observed | Longer runs with v2 (bisect); Researcher input on B(2,5) Dehn function / KB cascade theory. |
| Rust Bidirectional: no surviving outputs | Recover from git + re-run; word_7245 is target. **Reframed**: not finding geodesic, but compressing identity proof. |
| All biased KB runs were on INVALID targets (word_3705/3707) | Restart biased KB on word_7245. **Still valid**: identity-certificate compression is still a KB-based task. |
| **Proxy-quotient / PatternBoost proxy for [G,G]** | **FROZEN** (#status/disproven 2026-06-26). All 119 benchmark words are identity in B(2,5) — Cayley distance = 0 for all. No quotient metric applies. Pivot decision from Maria pending: (a) find non-trivial elements, or (b) reframe proxy as Dehn-complexity estimator. |
| comm_12_9 identity proof | Still open — **word_7245 IS an identity certificate but at 7,245 chars, far from minimal**. The goal is a shorter (ideally much shorter) proof that comm_12_9 = 1. Dehn function of B(2,5) bounds feasibility. |

---

## Critical bug (RESOLVED 2026-05-22)

`braid_reduce_fast` in Python had non-abelian inverse order error. All words derived from this function before the fix are INVALID (wrong group element). The 3,707-char "record" was invalidated. The corrected chain is documented in `experiments/b25_reduce_core/corrected/README.md`.

**Invalidated artifacts** (do not use):
- word_4882, word_3732, word_3707 (all in b25_bias_bidir/archive and b25_reduce_core/archive)
- Rule banks: `b25_bias_bidir/rules/3705_run4_*/`, `3705_run5_*/`, `weq_*/`
- `ui/comm_12_9_reduced_data.json#final_word` (contains 3707)
- Any beam/bidir run outputs derived from these

**Valid current best**: `experiments/b25_reduce_core/corrected/final_beam.txt` — 7,245 chars, abelianization (0,0).

---

## Next (prioritized)

0. **[TOP PRIORITY — 2026-06-30, AWAITING MARIA GO]** PatternBoost/axplorer B(2,5) loop first run. Pre-reg complete (Developer + B25 Experimenter sign-off 2026-06-30). Routed to Lead Dev for Maria GO gate. Seed: comm_13_10 compressed (260 chars). Baseline: braid_reduce --no-beam (plateau=258). Developer deliverables post-approval: (1) train.py loop, (2) m/M vocab extension, (3) calc_score() --rules-file. Pre-reg: [[PatternBoost/methodology/patternboost-b25-loop-prereg-2026-06-30]].

1. ~~Route `corrected/final_beam.txt` (7,245 chars) to Validator~~ — **DONE. `#status/conjectured` 2026-05-22.** See [[Architecture/Mixer/Documentation/Math Validation/2026-05-22-comm-12-9-7245-final]].
2. ~~GATE: Await Validator B(5,3) gates A+B~~ — **BOTH SOUND 2026-06-17. GATE CLEARED.**
3. ~~Run Step C~~ — **INCONCLUSIVE 2026-06-17.** Study could not be executed as pre-registered (non-confluent KB, binary-oracle GT substitution, commutator-subgroup blind-spot). See [[Proxy Validation/results/b53-proxy-results-2026-06-17]].
4. **COMPLETED 2026-06-18**: B(3,3) proxy validation v2 ran. H1 NOT SUPPORTED, H2 NOT SUPPORTED. LCS-weight-2 proxy D gives ρ=0.079 on γ₂\γ₃ (threshold 0.40; far below). Keep Option B. Results: [[Proxy Validation/results/b33-proxy-results-v2-2026-06-18]].
5. **COMPLETED 2026-06-25**: Fragment Shortening Hunt. 31 seed rules persisted at `experiments/burnside/b25/fragment_seed_rules/`. Rules promoted. word_7245 held for centralizer analysis (Lead direction). See [[Agents/Experimenter-B25/output/b25-fragment-seed-rules-2026-06-25]].
6. **NEXT (Lead direction)**: Centralizer analysis for word_7245's connector elements. The 9 connectors (`a, A, aBA, abA, abaBABA, ababABA, ababbABBABA, ababbaBABA, ababbaBBABA`) are invariant under all shortlex KB methods — investigate their centralizer structure in B(2,5) (GAP, PcGroup).
7. **PARALLEL CANDIDATE**: Apply 31 seed rules to the 37 affected words (biased KB or beam). Start with comm_16_2 (saves 41 chars, highest impact). Pre-register before running.
8. Run biased kbprog on raw word_7245 (valid 7,245-char target). Previous biased runs were on INVALID targets (word_3707) — restart from scratch. Pending Lead gate.
9. Run overnight benchmark with corrected pipeline on all 119 words.
10. Restore B(2,5) Rust Bidirectional configs from git (`bc3cba2`), re-run dual-RPO targeting 7,245-char word.

---

## Open literature questions for Researcher

- Is there published theory on whether KB with RPO must cascade (eventually) for finite Burnside groups? References beyond Adian-Novikov?
- What is known about the Dehn function of B(2,5)? Is it polynomial, exponential, or unknown? For a finite group of order 5^34, the Dehn function is bounded but the bound may be enormous.
- What is the minimum-length identity certificate for a word of Dehn-complexity k in B(2,5)? Is the Dehn function super-polynomial?
- Kyr's construction for B(2,5) words (referenced in `b25_comm_11_1_kyr.txt`): what is this and is it published?
- ~~Q5 feasibility for proxy quotient~~ — **MOOT** (all benchmark words are identity; Validator routing already sent).
- Are there papers on the "area" or "filling length" of relators in finite p-groups, specifically free Burnside groups? This reframes word_7245 as a topological problem (filling area in the Cayley complex).
- **NEW (2026-06-26)**: Are there published non-trivial B(2,5) elements (non-identity elements, i.e., elements of order 5 that are NOT relators) that could serve as new reduction targets? The Havas-Wall-Wamsley generators c_1 through c_34 are all order 5 — are canonical representatives (as words in {a,b}) known?

---

## FREEZE LOG (2026-06-26)

**Validator verdict**: ALL 119 HWW benchmark words = identity in B(2,5). #status/disproven for proxy-quotient metric approach on this corpus.

**Frozen items** (Lead-enforced, await Maria's pivot decision):
- Corpus augmentation fix for v4 proxy validation
- v4 Stage-1 B(3,3) lab GO
- R1 (Hamming-weight proxy on 119 words)
- R3 (Q5 collapse-check on 119 words)
- B(3,3) lab as proxy-for-the-119 (reframing question for Maria)
- Q5 feasibility Validator routing (sent, but answer is now moot given identity result)

**NOT frozen**:
- ITEM 2b centralizer-RESHAPE work (valid: compressing identity certificate is still a reduction task)
- All KB, beam, biased-KB work on word_7245 (reframed: identity certificate compression)
- Fragment seed rules and their application (reframed: reduce the length of the identity proof)

---

## Open math claims for Validator

- **CLAIM UPGRADED (`#status/proven` — 2026-06-26)**: the word `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars) represents the IDENTITY element of B(2,5) (= the same element as `[c12, c9]` = 1). Validator GAP verdict 2026-06-26: word_7245 = 1 in B(2,5), confirmed via EpimorphismPGroup (order 5^34). Previously `#status/conjectured` (Sub-claim C unverified — now VERIFIED by Validator). See Validator verdict note. **Reframing**: word_7245 is now understood as a 7,245-char identity certificate, not a geodesic path to a non-trivial element.

- **CLAIM CLOSED (`#status/disproven` — 2026-06-02)**: `corrected/final_7245_lifted_reduced.txt` (563 chars) was a candidate for a new lift-space best. Validator confirmed: abelianization (0,0) ✓ (valid representative of [c12,c9]), but expanding back to {a,b} yields **7,249 chars** — longer than word_7245. The 563-char form achieves 5.9× notational compression in {a,b,m} but is not a genuine length reduction. The complete undocumented circuit in `corrected/` is: final_beam.txt (7,245) → lift → 3,325 → KB → 563 → expand → 7,249 → reduce → 7,245 ≡ final_beam.txt. word_7245 remains the shortest-known form. See [[2026-06-02-b25-lift-reduce-circuit]].

Verified by [[2026-05-22-comm-12-9-7245-final]], [[2026-06-02-b25-lift-reduce-circuit]]

---

## Literature

- [[havas-wall-wamsley-1974]] — establishes |B(2,5)| = 5^34 and class 12; provides the generator numbering (generators 1–34) that defines every target word in these experiments (comm_12_9, comm_13_10, comm_11_1_kyr, etc.).
- [[havas-newman-1980]] — survey of computer-assisted Burnside results; contextualizes the p-quotient algorithm that generated the B(2,5) presentation and establishes that applying multiple independent computational techniques to the same group is the right strategy.
- [[havas-robertson]] — computational framework for finitely presented groups: coset enumeration (§2.1), KB completion (§2.9), and Tietze transformation (§2.3); the technique classes used across all three B(2,5) experiment types.
- [[kourovka-2022]] — Kourovka Notebook No. 20 (2022); houses problem 11.48 (Kostrikin 1990) asking whether B(2,5) is infinite; no resolution note as of 2022.
- [[kourovka-11.48-kostrikin-1990]] — dedicated note on problem 11.48: the open theoretical question all B(2,5) word-reduction and KB work is ultimately in service of.
- [[problems-people]] — project planning document listing all B(2,5) algorithms and named implementers in the algo_mixing effort; confirms KB, coset enumeration, Cayley-graph search, and bidirectional KB as the full portfolio of approaches.
