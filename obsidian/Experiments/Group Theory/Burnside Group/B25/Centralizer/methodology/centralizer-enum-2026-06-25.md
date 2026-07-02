---
title: B(2,5) Centralizer Enumeration as Guaranteed-Sound Rule Source
hypothesis: "C_G(CoreA) is a subgroup of order 5^9 in the restricted quotient B₀(2,5); every g ∈ C_G(CoreA) yields a sound reduction rule CoreA·g·CoreA⁻¹ → g by construction; extracting Pcgs generators + word representatives gives an immediately exploitable rule inventory."
pre_registration_date: 2026-06-25
author: maumayma
domain: group-theory
project: b25-commutator-reduction
status: pending
scope_correction: "2026-06-26 — the group built via EpimorphismPGroup(G,5,12) is the FINITE RESTRICTED quotient B₀(2,5) (order 5^34), NOT the FREE B(2,5) (finiteness OPEN, Kourovka 11.48). |B(2,5)|=5^34 as written below is the RESTRICTED group's order; the free group's order/finiteness is unknown. Centralizer rules CoreA·g·CoreA⁻¹→g are sound in B₀(2,5); soundness in the free group is not established by this. Relocated from the algo_mixing repo; handle corrected from a git-login leak to maumayma."
tags: [agent/exp, user/maumayma, domain/group-theory, project/b25-reduce-core, status/pending, experiment]
---

> **Scope note (2026-06-26):** "B(2,5)" / "B25" below = the **finite restricted quotient B₀(2,5)** (`EpimorphismPGroup(G,5,12)`, order 5^34), **not** the free Burnside group B(2,5) (finiteness OPEN, Kourovka 11.48). The centralizer result holds in B₀(2,5). See [[b25-q5-feasibility-verdict]] § CIRCULARITY ANALYSIS — RETRACTED IN FULL.

# Pre-Registration: B(2,5) Centralizer Enumeration

## Hypothesis

Every element g in C_G(CoreA) (the centralizer of CoreA in B(2,5)) commutes with CoreA, so the identity
CoreA·g·CoreA⁻¹ = g holds in B(2,5), making `CoreA·g·CoreA⁻¹ → g` a **sound reduction rule by construction**. Similarly for C_G(CoreB), but since CoreB = CoreA⁻¹, we have C_G(CoreA) = C_G(CoreB) — one subgroup, two rule contexts.

**Claim**: Validator has certified |C_G(CoreA)| = 5^9 = 1,953,125. The Pcgs (polycyclic generating sequence) of this subgroup has 9 generators. Extracting their word representatives in {a,A,b,B} gives a compact generating description of all centralizer-derived rules.

**Secondary claim**: Some centralizer elements appear as subwords in the 119 B(2,5) target words, making the corresponding rules immediately applicable without lengthening.

## Problem Set

- Group: B(2,5) = ⟨a,b | u^5 = 1 for all words u⟩, |B(2,5)| = 5^34
- Model: 4372-relator FP quotient via EpimorphismPGroup(G,5,12), identical to Validator's verified setup
- CoreA = "ABabAbabABaBAbabABABabAbaBABaBAbabb" (35 chars, Validator-certified)
- CoreB = CoreA⁻¹ = "BBABabAbabABaBAbabaBABabAbaBABaBAba" (35 chars, string-equality proof)
- Target set: 119 benchmark words from experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/words/

## Computation

### Phase 1 — GAP: Centralizer generators
- Build B25 via EpimorphismPGroup(G,5,12)
- Compute centA = Centralizer(B25, coreA)
- Verify |centA| = 5^9 (cross-check Validator's result)
- Get Pcgs(centA) — 9 generators
- Extract word reps via PreImagesRepresentative(phi, gen_i) for each generator
- Output: TSV of (generator_index, word_length, word_rep)

### Phase 2 — Python: Subword overlap check
- For each Pcgs generator word rep (and their powers/short products):
  - Check if it appears as substring in each of the 119 target words
  - Report matches: (target_word_name, generator_id, power, occurrence_start)
- Also do a full subword membership check: for each unique subword of length 5..50 across all 119 words, test membership in centA (GAP batch query)

### Phase 3 — Data artifacts
- Enumeration scheme: each element = gen_1^e_1 * ... * gen_9^e_9, e_i ∈ {0..4}
- Word rep of specific element: via PreImagesRepresentative(phi, product)
- Save: generators TSV, overlap hits, methodology note

## Baselines

Not a performance experiment — this is rule generation. Baseline metric: how many of the 119 target words contain a subword that is a centralizer element (0..119 range).

## Anti-patterns being avoided

- Length filter on centralizer elements: NONE — keeping all elements regardless of word length
- Abelianization as verification: FORBIDDEN — centralizer elements are in [G,G], abelianization blind
- Verification method: word equality in B(2,5) (full group computation in GAP)

## Seeds / Replication

N/A — centralizer computation is deterministic (exact group computation).

## Statistical test

N/A — this is an enumeration + search task.

## Validation gate

- Phase 1 output (centralizer size): Validator cross-check that |centA| = 5^9
- Phase 2 output (overlap hits): sample membership test [CoreA, g] = 1 for flagged g elements
- Any rule actually USED in a reduction claim: full word-equality verification in GAP + Validator sign-off

## Provenance

- GAP script: experiments/burnside/b25_centralizer_rules/scripts/b25_centralizer_enum.py
- Relator source: Agents/Validator/scratch/b25_conjugate_struct.g (lines 1-4386, unchanged)
- Git SHA: (recorded on run)
