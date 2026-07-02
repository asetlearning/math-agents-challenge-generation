---
title: B(2,5) Centralizer — Full Enumeration (ITEM 2a)
date: 2026-06-26
author: maumayma
domain: group-theory
project: b25-commutator-reduction
status: complete-upper-bounds
type: pre-registration
scope_correction: "2026-06-26 — all GAP computation here is in the FINITE RESTRICTED quotient B₀(2,5) (EpimorphismPGroup(G,5,12), order 5^34), NOT the FREE B(2,5) (finiteness OPEN, Kourovka 11.48). The centralizer C(CoreA)=5^9, the LCS depths, and every 'in B(2,5)' statement below are statements about the restricted quotient B₀(2,5). Relocated from the algo_mixing repo to the vault; handle corrected from a git-login leak to maumayma."
tags: [agent/exp, user/maumayma, domain/group-theory, project/b25-reduce-core, status/pending, experiment]
---

> **Scope note (2026-06-26):** Everything below labelled "B(2,5)" / "B25" is the **finite restricted quotient B₀(2,5)** built by `EpimorphismPGroup(G,5,12)` (order 5^34), **not** the free Burnside group B(2,5) whose finiteness is OPEN (Kourovka 11.48). The centralizer enumeration is valid for B₀(2,5); it does not establish anything about the free group. See [[b25-q5-feasibility-verdict]] § CIRCULARITY ANALYSIS — RETRACTED IN FULL.

# Pre-Registration: B(2,5) Centralizer Full Enumeration (ITEM 2a)

**Assigned by**: Maria (2026-06-26 morning direction)
**Routed by**: Lead

## Hypothesis

Every element of C_{B25}(CoreA) has a word rep in {a,b,A,B} obtainable as a product of
gen_1^{e1} * ... * gen_9^{e9} (e_i ∈ {0..4}), and the length distribution of the
5^9 = 1,953,125 reduced word reps is computable. This unblocks ITEM 2b (reshape mechanism).

## Fixed Context

- CoreA = "ABabAbabABaBAbabABABabAbaBABaBAbabb" (35 chars)
- |C(CoreA)| = 5^9 = 1,953,125 (confirmed by Validator, prior Phase 1)
- Pcgs of centA: 9 generators, all order 5
- LCS depths: [1, 6, 7, 9, 9, 9, 10, 11, 12]

## Method

### Phase A — Extract 9 generator word reps (GAP)

Run 9 SEPARATE GAP processes, one per Pcgs generator. Each process:
1. Builds B25 via EpimorphismPGroup (preamble: lines 1-4386 of b25_conjugate_struct.g)
2. Computes centA = Centralizer(B25, coreA)
3. Gets pcgsA = Pcgs(centA)
4. Calls PreImagesRepresentative(phi, pcgsA[i]) for ONE generator i
5. Converts GAP FP word (h1, h2 notation) → compact {a,b,A,B} string
6. Prints to stdout, captured to file

Memory: -o 6g per process. Timeout: 20min per generator.

If PreImagesRepresentative still OOMs for individual calls → escalate to Lead immediately
with exact error, do NOT proceed.

### Phase B — Build 5^9 product words (Python)

For each exponent vector (e1,...,e9) with e_i ∈ {0..4}:
- Build word = gen_1_word * e1 + gen_2_word * e2 + ... + gen_9_word * e9 (concatenation)
- Apply free reduction: cancel aA, Aa, bB, Bb
- Apply power reduction: a^5 = b^5 = 1 etc.
- Optionally: apply greedy rule reduction from available B25 rule bank

### Phase C — Reduce (Python greedy + kbmag wordreduce)

Two-pass reduction:
1. Python free + power reduction (always fast, O(N))
2. Greedy rule application using rules loaded from .kbprog.live files

Rule bank candidates:
- experiments/burnside/b25_bias_bidir/runs/special-mixer-l2r-rpo-v3-0001/b25_test.kbprog.live (27.5M, 191K rules)
- runs/b25/fragment_seed_rules/20260625_235828/input.kbprog.live (10.4M)

### Phase D — Stream to disk and build histogram

- Stream reduced reps to runs/b25_cent_enum/<timestamp>/cent_reps.tsv (one per line)
- Build length histogram incrementally
- Count distinct reps (verify = 1,953,125 distinct elements → all mapped to distinct reps)

## Metric

Full length distribution histogram (min / median / max / mode / full histogram by length).
Count of distinct reduced reps.

## Statistical test

None — this is an exact enumeration.

## Anti-patterns being avoided

- Not using GAP for reduction (tool discipline: GAP = algebra only)
- Not assuming OOM "because it happened before" — individual calls may differ; test first
- Not reporting partial results as "the distribution" — must complete all 5^9

## Spot-check protocol (GAP)

After enumeration: pick 10 random exponent vectors (e1,...,e9).
For each: compute Image(phi, reduced_word) in GAP and verify it equals the intended
element gen_1^e1 * ... * gen_9^e9 in centA.

## Provenance

- GAP relator source: Agents/Validator/scratch/b25_conjugate_struct.g (unchanged)
- B25 build: EpimorphismPGroup(G,5,12) on 4372-relator presentation
- Scripts: experiments/burnside/b25_centralizer_rules/scripts/
- Output: runs/b25_cent_enum/<timestamp>/

---

## Amendment 2026-06-26 — Actual implementation

**Deviation from pre-registered method (Phase A, B, C)**:

Phase A (GAP word reps): GAP `PreImagesRepresentative` was abandoned after discovering it
gives 572K-char words for depth-7+ elements. Instead, B25 Pcgs generator word reps were
built INDUCTIVELY via the PURE COMMUTATOR CHAIN verified from `b25_comm_structure.log`:
- g_k = Comm(g_i, g_j) = inv(g_i)*inv(g_j)*g_i*g_j (exact, purely algebraic)
- Each g_k reduced to near-NF using symmetric shortlex rules before building g_{k+1}

Phase B (product words): Implemented in Rust (cent_enum.rs) not Python.

Phase C (reduction rule bank): Switched from l2r-rpo rules (191K, `b25_test.kbprog.live`
from `special-mixer-l2r-rpo-v3-0001`) to **symmetric shortlex rules** (199K,
`b25_test.kbprog.live` from `special-mixer-shortlex-v3-0001`).

**Reason for switch**: l2r-rpo rules use `B→bbbb` expansions giving NF in {a,b}^* only.
Deep B25 Pcgs gen NFs reach 15K chars in that ordering, making the 1.95M enumeration
infeasible. Symmetric shortlex (`ordering := "shortlex"`, `generatorOrder := [a,A,b,B]`,
AAA→aa etc.) gives NF in {a,A,b,B}^* with deep gen NFs at 5K-21K chars and achieves
~810 elements/sec (ETA ~40 min total).

**Upper-bound caveat**: 3000 iters per element with non-confluent rules — lengths are
upper bounds on true symmetric-shortlex NF lengths. Hypothesis validity unaffected (it's
about computability and shape of distribution, not exact NF values).

**Provenance triple (run)**:
- git SHA: `5aeee6a90275c5583d367e534e2ded952dbfe545`
- uv.lock SHA-256: `250813458846e22a4c1322ecbc3aab7165de3ba41174d805f8fa8c6cc1b44fc7`
- b25_test.reduce FSA SHA-256: `265426cf72371a7089d375e7584d147744991010a5f9d7ccb4c324fedd0ede46`
- Binary: `experiments/burnside/burnside_bidirectional/src/bin/cent_enum.rs`
- Rules: `experiments/burnside/b25_bias_bidir/runs/special-mixer-shortlex-v3-0001/b25_test.kbprog.live`
- Output: `runs/b25_cent_enum/1782476409/`
- Wall-clock: 2461.2s
