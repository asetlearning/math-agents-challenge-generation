---
title: B0(2,5) LCS Dimensions — GAP Receipt and Filtration Verdict
status: proven
domain: group-theory
project: b25
claim: "In B0(2,5) = EpimorphismPGroup(G,5,12), the LCS dimension dim(γ₅/γ₆) = 2 (not 6 as suggested by the free-Lie Witt formula) and |B0/γ₆| = 5^10."
claimant: Math-expert (initial); Validator (correction chain)
verification_method: direct GAP LowerCentralSeries computation
tools_used: [GAP 4.x, Agents/Validator/scratch/b25_lcs_of_B0_v2.g]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25, topic/lower-central-series, topic/pcgs-proxy, status/proven, proof]
---

# Verification — B0(2,5) LCS Dimensions

## The Claim

In B0(2,5) = EpimorphismPGroup(G,5,12) (where G = F(2)/⟨w^5 : w freely reduced, |w|≤7⟩), the lower central series has dimension dim(γ₅/γ₆) = 2 at weight 5, giving |B0/γ₆| = 5^10.

This is DIFFERENT from what the Witt formula would predict (d₅=6 for the free Lie algebra on 2 generators).

## Method

Direct computation of LowerCentralSeries(B0) in GAP:

1. Generate all 4372 freely reduced words over {a, a⁻¹, b, b⁻¹} of length 1–7 (confirmed: exactly 4372 words, matching the kbmag_source/standalone/kb_data/b25_gen comment).
2. Build G = F(2) / ⟨w^5 : w in the list⟩.
3. Compute B0 = EpimorphismPGroup(G, 5, 12). Result: |B0| = 5^34. ✓
4. Compute LCS = LowerCentralSeries(B0). Result: 13 terms (nilpotency class 12).

Script: `Agents/Validator/scratch/b25_lcs_of_B0_v2.g`
Output: `Agents/Validator/scratch/b25_lcs_of_B0_v2.out`

## Evidence — Full LCS

```
LCS dimensions of B0(2,5):
  dim(γ₁/γ₂) = 2   (|γ₁| = 5^34)
  dim(γ₂/γ₃) = 1   (|γ₂| = 5^32)
  dim(γ₃/γ₄) = 2   (|γ₃| = 5^31)
  dim(γ₄/γ₅) = 3   (|γ₄| = 5^29)
  dim(γ₅/γ₆) = 2   (|γ₅| = 5^26)  ← KEY
  dim(γ₆/γ₇) = 4   (|γ₆| = 5^24)
  dim(γ₇/γ₈) = 4   (|γ₇| = 5^20)
  dim(γ₈/γ₉) = 4   (|γ₈| = 5^16)
  dim(γ₉/γ₁₀) = 6  (|γ₉| = 5^12)
  dim(γ₁₀/γ₁₁) = 3 (|γ₁₀| = 5^6)
  dim(γ₁₁/γ₁₂) = 2 (|γ₁₁| = 5^3)
  dim(γ₁₂/γ₁₃) = 1 (|γ₁₂| = 5^1)
  |γ₁₃| = 1 = {e}

Sum: 2+1+2+3+2+4+4+4+6+3+2+1 = 34 ✓
```

Key derived values:
- |B0/γ₆| = 5^34 / 5^24 = **5^10**
- dim(γ₅/γ₆) = **2** (not 6)

## Verdict

**#status/proven** (conditional on B0 ≅ B(2,5); see Task #14 / [[b25-q5-feasibility-verdict]])

### Why This Verdict

The GAP computation is direct: LowerCentralSeries(B0) is an exact computation on the polycyclic group B0. The output is unambiguous. This is not a heuristic or an approximation.

The result contradicts the Witt formula prediction (d₅=6), but this is EXPECTED: the Witt formula counts dimensions in the FREE Lie algebra on 2 generators. B(2,5)'s associated graded Lie ring (= graded ring of B0 if B0≅B(2,5)) satisfies additional Burnside relations from the law x^5=1 for all products. These relations eliminate 4 of the 6 free-Lie weight-5 elements, leaving dim = 2.

The Burnside Engel identity ad(x)^4 = 0 (which holds in restricted Lie algebras of groups with exponent 5; attributed to Kostrikin's resolution of the Burnside problem) is one source of these additional relations. At weight 5, four additional relations emerge from the multilinear expansion of the exponent law (xy)^5 = 1 applied to pairs of generators.

## Filtration Clarification (Resolving the Filtration Mismatch)

Three filtrations were in play during this analysis:

| Filtration | Object | d₅ value | Order of "Q5" |
|---|---|---|---|
| Free Lie algebra (Witt formula) | Abstract algebra | 6 | — |
| Lower p-central series of G (EpimorphismPGroup(G,5,5)) | FP group G | 2 (the layer P₅/P₆ of G) | 5^10 |
| LCS of B0 (LowerCentralSeries(B0)) | pcGroup B0 | **2** | **5^10** |

The last two agree: EpimorphismPGroup(G,5,5) = B0/γ₆(B0) = 5^10. This equality holds because B0 is an exponent-5 group, so its p-central series equals its LCS (P_k(B0) = γ_k(B0)), and EpimorphismPGroup(G,5,k) = EpimorphismPGroup(B0,5,k) for k ≤ 12.

The earlier confusion arose from applying the free-Lie Witt formula to B(2,5)'s LCS without accounting for Burnside relations. The synthesis must be corrected: **d₅ = 2, Q5 = B0/γ₆ = 5^10**.

## Correction Chain (for the Record)

1. Math-expert's assessment: dim(γ₅/γ₆) = 2 (Q5=5^10) — CORRECT intuition, reasoning by p-central series analogy.
2. Validator's initial verdict (same session): Incorrectly said synthesis d₅=6 / Q5=5^14 is correct; retracted Q1 claim.
3. Lead reported d₅=2 to Maria, then retracted on Validator's (incorrect) correction.
4. This GAP computation confirms dim(γ₅/γ₆) = 2 definitively. Lead's d₅=2 is RESTORED.

## Implications for Stage 4 (pcgs/Jennings Proxy)

- Weight-5 projection π₅: B0 → γ₅(B0)/γ₆(B0) ≅ (F₅)² — **2-dimensional vector**, not 6.
- EpimorphismPGroup(G,5,5) = 5^10 is the CORRECT construction for Q5 (either this or NaturalHomomorphismByNormalSubgroup(B0, LCS(B0)[6]) gives the same result).
- Stage 4 design should reflect d₅=2; the pre-reg's d₅=6 language must be corrected.
- The most informative weight-5 feature is a 2-dim vector over F₅.
- First weight with dimension 6 is weight 9 (γ₉/γ₁₀). Weight-9 pcgs layer may be more expressive.

## Conditional Note (Task #14)

This computation is on B0(2,5) = EpimorphismPGroup(G,5,12). All statements above are proven for B0. Whether B0 ≅ free B(2,5) depends on HWW 1974 (Task #14, live). If B0 ≅ B(2,5), these are dimensions of the real B(2,5). If not, they describe a finite group of order 5^34 that may differ.

## Notes for Downstream Agents

- **Researcher**: Correct the b25-gg-proxy-literature-synthesis to d₅=2, Q5=5^10. Add a note: 'Witt formula gives d₅=6 for the free Lie algebra; Burnside relations reduce this to 2 in B(2,5).'
- **Math-expert**: Stage 4 Lab A in B(3,3) analogue — if B(3,3) analogue aims at weight-2 or weight-3 pcgs layers, re-check their dimensions using LowerCentralSeries(B(3,3)).
- **Experimenter-B25**: The weight-5 proxy is 2-dimensional (not 6); BFS on Q5=5^10 is the correct target (already determined feasible in prior sessions).
- **Lead**: d₅=2 confirmed; restore this number in all synthesis docs and reports.
