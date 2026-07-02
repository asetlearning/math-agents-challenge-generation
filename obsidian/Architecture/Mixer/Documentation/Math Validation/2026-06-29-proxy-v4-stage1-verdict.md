---
title: Proxy Validation v4 Stage 1 — Validator Verdict
status: proven
domain: group-theory
project: b25
claim: "Stage 1 B(3,3) result interpretation is mathematically sound: geodesic BFS corpus → Arms 1/3 constant zero on stratum III → correlation undefined; closure limited to exact tested configuration; no equality/proof claim beyond Cayley-BFS GT."
claimant: Math-expert (proxy-validation-v4-stage1-results-2026-06-29)
verification_method: logical analysis of geodesic→constant-zero chain; scope audit
tools_used: [Math-expert Stage 1 results note, v2 Cayley-BFS corpus provenance]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25, topic/proxy-validation, topic/b33, topic/patternboost, status/proven, proof]
---

# Validator Verdict — Proxy Validation v4 Stage 1

## Summary

**CONCUR.** The interpretation is mathematically sound on all three components: the logical chain from geodesic inputs to constant-zero outputs, the undefined-correlation claim, and the scope boundary of the closure. No equality or proof claim beyond Cayley-BFS ground truth is made. One structural observation added (pre-reg design incompatibility, confirming Math-expert's recommendation has mathematical weight).

---

## Assessment by Component

### (i) Geodesic → constant zero for length-reducing arms

**CORRECT.**

For any word already at geodesic length (`len(word) = d_Cayley(1,g)`), no rewriting can produce a shorter representative in the same group. This is the definition of geodesic in the Cayley graph.

- **Arm 1 (periodicity-excess K=4/8/12)**: measures excess repetition patterns above threshold K that could be contracted to reduce word length. For a geodesic word, no such contraction exists — any "excess" repetition is load-bearing (removing it would change the group element). Arm 1 score = 0 is exact, not approximate.
- **Arm 3 (bounded-descent shrink T=16/64)**: measures word-length reduction from T steps of descent. For a geodesic word, no descent step can produce a strictly shorter word representing the same group element. Arm 3 shrink = 0 exactly.

The inference `geodesic input → score = 0` is tight for both arms. Not an empirical observation — a logical implication.

The BFS corpus returns geodesic representatives by construction: BFS from identity finds shortest paths, so every stored word is at minimal length. The constant-zero finding on stratum III was therefore predictable from corpus design. This is noted below as a structural observation.

### (ii) Undefined correlation, not zero correlation

**CORRECT.**

Spearman and Pearson correlations require nonzero variance in at least one variable. A constant-zero feature has variance exactly 0. The denominator in both formulas vanishes; the correlation is undefined. Reporting "undefined" is the mathematically correct choice. Reporting ρ=0 would be wrong — it implies a defined statistic that happens to be null, when the statistic cannot be computed.

The note correctly reports "0/80 nonzero coverage" as the primary fact and derives undefined correlation from it.

### (iii) Scope of closure — not-closed list

**CORRECT AND COMPLETE.**

Closed by Stage 1:
- Arm 1 K=4/8/12 periodicity-excess on the B(3,3) v2 BFS stratum III [G,G] corpus
- Arm 3 T=16/64 bounded-descent shrink on the same corpus

Not closed (correctly enumerated):
- Stage 2+ B₀(2,5) generated-candidate corpus — not run; held pending Maria direction
- B(3,3) higher pcgs layers (π₃, π₄) — untested
- B(3,3)-native quotient ensemble — untested
- Prefix-path, Hall polynomial, subgroup-depth, Magnus/Zassenhaus spelling, rewrite-potential — none pre-registered or run

The Stage 1 negative justifies no broad proxy-track closure. The exact tested configuration is closed; nothing beyond it is touched.

### Scope and proof claims

**CLEAN.** No free B(2,5) claim appears. No word-equality claim. Ground truth is explicitly "exact Cayley/geodesic distance from v2 Cayley-BFS corpus" — a finite-group BFS computation, not a theorem about B(2,5) or B₀(2,5). Stage 2+ is explicitly not run and not inferred from this result.

---

## Structural Observation (Validator Addition)

**The constant-zero outcome on stratum III was predictable from the pre-reg design.**

The pre-reg combined (a) testing length-reducing arms with (b) using BFS representative spellings as the hard-stratum corpus. These are logically incompatible: BFS produces geodesic representatives, and length-reducing proxies score 0 on geodesic inputs by definition. The null result on stratum III was guaranteed by corpus design, independently of any property of Arms 1 or 3.

This is not a reason to discount the closure: the arms ARE correctly closed on the tested configuration. But it means the Stage 1 negative is uninformative about whether Arms 1/3 would show signal on non-geodesic spellings of [G,G] elements — it only says they show no signal when there is nothing to reduce.

**What the pre-reg should have required for length-reducing proxy testing on [G,G] elements**: non-geodesic spellings — words of the form `g·r` where `g` ∈ [G,G] is a group element and `r` is a nontrivial relator product making the spelling strictly longer than the geodesic. Such words represent elements of [G,G] but are NOT at minimal length, so length-reducing arms have something to measure.

Math-expert's recommendation ("avoid using already-geodesic representative words as the sole hard-stratum test for length-reducing proxies") has mathematical weight. It is the correct fix. The Validator confirms this is not merely pragmatic advice — it addresses a logical incompatibility in the corpus design.

---

## Secondary Stratum II Observation

Preserved for completeness: Arm 1 shows weak-but-nonzero Spearman ρ=0.205 on stratum II (random non-identity elements, not exclusively [G,G]). This is informative as a pointer:

- Arms 1/3 show some signal on words NOT deep in [G,G] (stratum II), but zero signal on [G,G] stratum III.
- This is consistent with the abelianization-blind pattern: length-reducing proxies may detect length-reducibility above the [G,G] barrier but are vacuous below it.
- The secondary signal does NOT rescue the pre-reg decision (primary criterion required stratum III ρ ≥ 0.20; stratum III correlation is undefined). It remains "not supported."
- It IS a design pointer: a future arm targeting [G,G]-depth signal needs to be something other than a length-reducing proxy on geodesic inputs — it needs a feature that varies even for words at minimal length (e.g., an algebraic invariant of the group element, not a spelling feature).

---

## Verdict

**#status/proven** — the interpretation is mathematically correct.

- Geodesic → constant zero → undefined correlation: logically exact.
- Scope boundary: correct and complete.
- Proof/equality claims: none beyond Cayley-BFS GT from v2. Clean.
- Pre-reg design incompatibility: confirmed (structural observation, not a correction).

Stage 1 Arms 1/3 are closed on the exact tested configuration. No broader closure follows.

## Notes for Downstream

- **Math-expert**: pre-reg for the next [G,G]-targeting design should require non-geodesic spellings as the hard-stratum corpus if testing length-reducing proxies. Alternatively: switch to an algebraic (non-spelling) feature for [G,G] depth.
- **Lead**: Stage 1 result is interpretively sound. No math issue blocks Stage 2+ if Maria's direction GO arrives.
- **Experimenter-B25**: if Stage 2+ proceeds (B₀(2,5) generated candidates), the corpus design lesson applies there too — generate candidates that are NOT at their B₀-geodesic length, so length-reducing proxy arms have non-zero inputs.

Verified by [[Architecture/Mixer/Documentation/Math Validation/2026-06-29-proxy-v4-stage1-verdict]]
