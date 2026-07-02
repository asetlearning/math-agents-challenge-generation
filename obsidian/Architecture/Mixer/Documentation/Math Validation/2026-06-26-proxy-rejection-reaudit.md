---
title: Proxy Rejection Re-Audit — Validator Verdict
status: active
domain: group-theory
project: b25
claim: "For each prior proxy rejection in the B(2,5) proxy-validation track, is the negative a genuine exhaustive result or an artifact of (i) restricted-vs-free conflation, (ii) premature close, or (iii) wrong corpus?"
claimant: Lead / Math-expert (co-owner: 2b re-audit 2026-06-26)
verification_method: independent re-audit against Math-expert draft, B0/free distinction, corpus audit
tools_used: [Math-expert draft proxy-rejection-reaudit-2026-06-26, vault notes, GAP LCS receipt 2026-06-26-b25-lcs-dimensions-gap-receipt]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25, topic/proxy-validation, status/active, proof]
---

# Validator Verdict — Proxy Rejection Re-Audit (Thread 2b)

## Scope and Authority

Validator owns math verdicts. Math-expert's labels are independent; where they agree with mine, the label is confirmed. Where I disagree, this note's verdict is binding on math correctness. No experiment may run from this verdict without a separate Maria GO.

**Baseline correction that drives all verdicts**: All finite-quotient / EpimorphismPGroup computations are labeled as results about **B0(2,5)** (the finite group computed via GAP from the 4372-relator FP group) until the HWW 1974 citation is confirmed. The identification B0(2,5) ≅ free B(2,5) is argued but not yet cited (task #14 live). Any negative phrased as "identity/distance = 0 in B(2,5)" is re-scoped accordingly.

---

## ~~Critical Math Issue: EpimorphismPGroup(G,5,5) ≠ B0(2,5)/γ₆~~ — SUPERSEDED

**SUPERSEDED by GAP LCS receipt 2026-06-26. See [[2026-06-26-b25-lcs-dimensions-gap-receipt]].**

The original "Critical Math Issue" section in this note was WRONG. It was written before running LowerCentralSeries(B0) directly and incorrectly applied the free-Lie Witt formula (d₅=6) to B(2,5)'s LCS.

**CORRECTED FINDINGS (from direct GAP LCS computation):**

```
LowerCentralSeries(B0) dimensions: [2, 1, 2, 3, 2, 4, 4, 4, 6, 3, 2, 1]
dim(γ₅/γ₆) = 2  (NOT 6)
|B0/γ₆|    = 5^10  (NOT 5^14)
```

The Witt formula (d₅=6) applies to the FREE Lie algebra on 2 generators. The associated graded Lie ring of B(2,5) satisfies additional Burnside relations from the law (xy)^5=1, eliminating 4 of those 6 elements. d₅=2 is the correct dimension in B0.

**EpimorphismPGroup(G,5,5) = B0/γ₆(B0) — SAME GROUP, same order 5^10.**

These are equal because B0 is an exponent-5 group, so its p-central series equals its LCS: P_k(B0) = γ_k(B0). Therefore EpimorphismPGroup(G,5,5) = EpimorphismPGroup(B0,5,5) = B0/γ₆(B0) = 5^10.

My prior claim that "EpimorphismPGroup(G,5,5)=5^10 ≠ B0/γ₆=5^14" was wrong in both its numbers and its inequality.

**CORRECTED Stage 4 construction guidance:**

- Q5 = B0(2,5)/γ₆(B0) has order **5^10** (not 5^14)
- dim(γ₅/γ₆) = **2** (not 6); the weight-5 pcgs feature is a **2-dimensional vector** over F₅
- EpimorphismPGroup(G, 5, 5) IS the correct construction for Q5 (gives the same group as the LCS route)
- Stage 4 can use either: `EpimorphismPGroup(G, 5, 5)` or `NaturalHomomorphismByNormalSubgroup(B0, LCS(B0)[6])`

```gap
# Either route gives the same Q5 = 5^10 with dim(γ₅/γ₆) = 2:
# Route A (already available):
phi5 := EpimorphismPGroup(G, 5, 5);
Q5 := Image(phi5);  # order = 5^10 ✓
# Route B (explicit LCS):
B0 := Image(EpimorphismPGroup(G, 5, 12));
lcs := LowerCentralSeries(B0);
Q5 := B0 / lcs[6];  # order = 5^10 ✓
```

**First weight with dimension 6: weight 9** (dim(γ₉/γ₁₀) = 6). If a higher-dimensional pcgs feature is desired, weight-9 is the right target.

---

## Verdict Table

| Prior rejection / negative | Math-expert label | **Validator verdict** | Math basis |
|---|---|---|---|
| Abelianization as [G,G] proxy | STANDS | **STANDS** | Algebraic fact: ab = [G,G] → all commutators map to 0 in G/[G,G]. Independent of B0 vs free. |
| LCS-weight-2 / proxy D in B(3,3) | STANDS | **STANDS** | B(3,3) lab used correct finite group; ρ=0.079 on stratum III is a genuine lab negative for weight-2. Conflation does not affect B(3,3). |
| Higher-weight pcgs norm (weight-5 analogue) | WRONGLY-REJECTED if treated as covered by weight-2 | **WRONGLY-REJECTED** | Weight-2 failure does not exhaust weight-k for k≠2. The relevant layer for B0(2,5) benchmark-like words is weight ≥5. Untested. |
| Q2/Q3/Q4 on 119 benchmark words in B0(2,5) | STANDS for B0/benchmark corpus | **STANDS with precision note** | d=0 in Q4=B0(2,5)/γ₅ is valid unconditionally for words in γ₅ (free or B0). d=0 in Q12=B0(2,5) is ONLY a B0 statement. The negative STANDS for its stated scope. The words are in γ₅ of B0(2,5); whether they're in γ₅ of free B(2,5) or trivial there is pending task #14. |
| Q2/Q3/Q4 as a general proxy family | WRONGLY-REJECTED if closed globally | **WRONGLY-REJECTED** | Pilot tested the wrong corpus (giant benchmark words ≥2500 chars) and drew a global conclusion. For generated candidates 100-2000 chars with non-trivial free-B(2,5) images, the quotient family is untested. |
| Q5 feasibility/proxy | NEEDS-RETEST with corrected scope | **NEEDS-RETEST** — scope clarified | ~~EpimorphismPGroup(G,5,5)=5^10 ≠ B0(2,5)/γ₆=5^14~~ CORRECTED: both equal 5^10 (same group). BFS on Q5=5^10 has ~10^7 elements — feasibility verdict from prior analysis stands (feasible). Pcgs coordinate extraction (no BFS) is the cleaner approach. See [[2026-06-26-b25-lcs-dimensions-gap-receipt]]. |
| Arm 1 periodicity-excess | NEEDS-RETEST | **NEEDS-RETEST** | Only observed on giant benchmark words in B0 corpus; never run on B(3,3) lab or 100-2000 char generated candidates. Not exhausted. |
| Arm 3 bounded-descent | NEEDS-RETEST | **NEEDS-RETEST** | Same as Arm 1 — never run on B(3,3) lab or correct candidate corpus. |
| B(3,3) lab for Arms 1/3 | WRONGLY ABANDONED | **WRONGLY ABANDONED** | Gate B failure (on B(2,5) quotient pilot) wrongly closed the B(3,3) lab for Arms 1/3. Arms 1/3 need no quotient tables; B(3,3) lab is the correct falsification venue. |
| B(3,3)-appropriate quotient ensemble | NEEDS-RETEST | **NEEDS-RETEST** | v3 used B(2,5) quotients on B(3,3) words — wrong quotients. Native B(3,3)/γ₂ and B(3,3)/γ₃ were not tested. |
| Option B as proximity-to-identity proxy | STANDS | **STANDS with clarification** | Option B (braid+power ratio) was never designed as a Cayley-distance proxy. It was accepted as a compression-progress scorer. The claim "Option B estimates proximity to identity" was never formally pre-registered. The B(3,3) stratum-III blind result (if it covers Option B) supports rejection of the distance-proxy reading. The compression-progress reading (r=0.949) was accepted and is separately assessed below. |
| Option B as compression-progress scorer on generated candidates | NEEDS-RETEST | **NEEDS-RETEST** | Accepted result (r=0.949) used benchmark words ≥2500 chars, not 100-2000 char generated candidates. The correct corpus was never built. Acceptance is provisional pending retest on the correct corpus. |
| B(5,3) v1 combined proxy transfer | NEEDS-RETEST | **NEEDS-RETEST (no math input)** | Insufficient data in vault to make a binding math verdict on B(5,3) transfer. Flagging for Math-expert to specify what exactly was tested. |
| Proxy A (reduction ratio) on stratum III | See Option B above | **NEEDS-RETEST** | Proxy A was blind on B(3,3) stratum III, but the relevant stratum for B(2,5) is depth-≥5 (γ₅), not depth-2 (γ₂/γ₃). Not tested on the correct stratum. |
| Combined proxy A+B (abelianization blind class) | STANDS | **STANDS** | The (aba)^5 motivating example and the B(3,3) stratum-III result show combined A+B is 0 on [G,G]-words. Independent of B0/free conflation. |
| All untested items (Hall polynomial, B(2,4) lab, random-walk, subgroup-depth, Magnus-style, prefix-path, relator-exposure) | NEEDS PRE-REG | **NEEDS PRE-REG** | No pre-registration exists; no verdicts possible. |

---

## Summary Counts

| Verdict | Count | Items |
|---|---|---|
| **STANDS** | 5 | Abelianization; LCS-weight-2 in B(3,3); Q2/Q3/Q4 on B0 benchmark corpus; Combined A+B blind; Option B as proximity-to-identity (clarified) |
| **WRONGLY-REJECTED** | 3 | Higher-weight pcgs norm; Q2/Q3/Q4 as general family; B(3,3) lab for Arms 1/3 |
| **NEEDS-RETEST** | 9 | Arms 1/3; B(3,3) quotient ensemble; Q5 (scope corrected); Option B compression-progress; Proxy A; B(5,3) transfer; Q2/Q3/Q4 general; Option B as compression scorer |
| **NEEDS PRE-REG** | 8+ | All unfiled items |

---

## Key Disagreements with Math-expert

1. ~~**Q5 order**: Math-expert uses "Q5" without distinguishing EpimorphismPGroup(G,5,5)=5^10 from B0(2,5)/γ₆=5^14. The relevant Q5 is the LCS-based quotient, order 5^14.~~ **RETRACTED.** GAP LCS receipt confirms Math-expert was correct: B0/γ₆ = 5^10 (not 5^14), dim(γ₅/γ₆) = 2 (not 6). EpimorphismPGroup(G,5,5) = B0/γ₆ (same group). See [[2026-06-26-b25-lcs-dimensions-gap-receipt]].

2. **Q2/Q3/Q4 on benchmark words — d=0 in Q4**: d=0 in Q4 is valid even for non-trivial words in γ₅ (free B(2,5)). It's not purely a B0 artifact — it's the CORRECT answer for any word in γ₅. I add this nuance to the Math-expert's "STANDS for B0/benchmark corpus."

3. **Option B proximity-to-identity label**: Math-expert says STANDS citing "Validator's earlier counterexample." That counterexample is unclear to me; I add the clarification that Option B was a compression-progress proxy, not a proximity-to-identity proxy. The framing matters.

---

## 2a Pre-Reg Math Vetting — Ready Position

When Math-expert delivers finalized pre-regs, I will vet each stage for:
1. **Corpus soundness**: generated candidates (100-2000 chars, non-trivial in B0(2,5)), not benchmark relators.
2. **Rule provenance**: any word-equality rule must be Validator-cleared via full GAP word-equality. Abelianization check FORBIDDEN as equality oracle.
3. **Scope labels**: any GAP quotient result is scoped to B0(2,5) unless HWW 1974 citation is confirmed.
4. **Quotient construction**: weight-5 projection uses Q5 = B0(2,5)/γ₆ = **5^10**, dim(γ₅/γ₆) = **2**. EpimorphismPGroup(G, 5, 5) = 5^10 IS the correct Q5 construction (equals B0/γ₆ since B0 is exponent-5). The prior demand to use the LCS route instead is retracted — both routes give the same group.
5. **Magnus features**: classical Magnus coefficients may be used as SPELLING features only (not group invariants of B(m,5)). Jennings/Zassenhaus features are valid in B0(2,5) but must be explicitly labeled.

### Stage-specific gates (now):

**Stage 4 (pcgs/Jennings) — CONDITIONAL PASS** *(updated post-GAP-receipt)*
The hypothesis and feature design are mathematically sound in principle. Corrected construction:
- Q5 = B0(2,5)/γ₆ has order **5^10**, dim(γ₅/γ₆) = **2** (not 6, not 5^14)
- EpimorphismPGroup(G, 5, 5) IS the correct construction; mandatory LCS-route demand retracted
- The weight-5 pcgs feature is a **2-dimensional vector** over F₅, not 6-dimensional
- State explicitly: "results are in B0(2,5) scope only" (HWW 1974 / Task #14 gates free B(2,5) claim)
- Pcgs basis must be weight-ordered; basis choice declared before any run
- If a 6-dimensional weight-k layer is desired for richer features, use **weight 9** (dim(γ₉/γ₁₀) = 6)
CONDITIONAL on scope labelling: **APPROVE for Stage 1 B(3,3) analogue run**.

**Stage 9 (Magnus-style) — APPROVE WITH GATE**
Classical Magnus features: APPROVE as spelling-only heuristics. Explicit language must appear in any result: "These are not group invariants of B(2,5); they do not respect the exponent-5 law."
Jennings/Zassenhaus features: APPROVE pending Validator clearance of the specific implementation (group ring filtration in B0(2,5) is well-defined; implementation must be GAP-verified before any claim).

---

## Task #14 Current Status (Live, Not Dropped)

**Q1 — Is b25_gen 4372-relator set a proven complete presentation of free B(2,5)?**

ANSWER: The 4372 relators are NOT a complete presentation in the usual sense (they are a finite subset of the infinite exponent-5 relations). However, combined with the EpimorphismPGroup p-class-12 computation, they produce B0(2,5) of order 5^34. The mathematical argument that B0(2,5) = free B(2,5) is documented (Agents/Validator/scratch/b25_circularity_analysis.md) and requires:
- The HWW 1974 theorem |B(2,5)| = 5^34 (CITATION NOT YET CONFIRMED in this session).
- The surjection G → B(2,5) (established from N ⊆ N_{B(2,5)}).
- The equal-order surjection → isomorphism argument.

Citation needed: Havas, G., Newman, M.F., Wall, G.E. (1974) — the paper establishing |B(2,5)| = 5^34 by machine computation. Without this citation, B0(2,5) and free B(2,5) are formally treated as distinct.

**Q2 — Source paper for the 119 commutators:**
NOT YET FOUND. Researcher needed with web access. The question: are the comm_i_j words (a) definitional polycyclic relators (trivial by construction), (b) commutator elements [c_i, c_j] whose triviality was established by HWW, or (c) words whose triviality is genuinely conjectured?

**Q3 — Retract 'proven' framing:**
DONE. Verdict note updated (2026-06-26). Finds held as "under review" pending task #14 resolution.

**Q4 — What does the GAP run establish:**
"The 119 benchmark words equal identity in B0(2,5) = EpimorphismPGroup(F(2)/(length-≤7 relators), 5, 12), a finite group of order 5^34. Whether B0(2,5) = free B(2,5) is argued (see b25_circularity_analysis.md) but requires the HWW 1974 citation to be confirmed."

---

## Notes for Downstream

- No experiment should run based on this audit alone; Maria GO is required per Stage.
- The B(3,3) Arms 1/3 v4 run (Stage 1 of the 2a pre-reg queue) is the correct first run: uses known correct group, pre-existing corpus, no B0/free ambiguity.
- Stage 4 pcgs/Jennings is CONDITIONAL on fixing the Q5 construction (LCS-based, not PQ-class-5). Add to v4 runner if Experimenter can implement the correct quotient.
- Task #14 (#1 and #2) requires Researcher with web access. Route there before any claim about free B(2,5) identity is restored.
