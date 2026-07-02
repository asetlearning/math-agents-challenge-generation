---
title: Stage 2 B0 Proxy Validation — Quotient-Distance GT Caveat Verdict
status: proven
domain: group-theory
project: b25
claim: "(1) d_Q(1,π(g)) ≤ d_B0(1,g) is a theorem — quotient distance is a rigorous lower bound; (2) Q4=B0/γ5 collapses weight-5 pcgs coordinates to zero — testing weight-5 features requires Q5=B0/γ6 at minimum."
claimant: Math-expert / B25 (Stage 2 pre-registration request)
verification_method: direct proof from quotient map properties; pcgs filtration analysis
tools_used: [first principles, GAP LCS receipt 2026-06-26-b25-lcs-dimensions-gap-receipt]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25, topic/proxy-validation, topic/quotient-distance, topic/pcgs-proxy, status/proven, proof]
---

# Validator Verdict — Stage 2 Quotient-Distance GT Caveats

## Summary

**Both claims APPROVED as stated.** One critical nuance added to Claim 1 (the zero-lower-bound trap for elements in the kernel), and the corpus design implication is spelled out explicitly. The proposed wording is mathematically sound for Stage 2 reporting.

---

## Claim 1: d_Q(1,π(g)) ≤ d_B0(1,g) — Rigorous Lower Bound

**#status/proven — this is a theorem.**

### Proof

Let φ: B0 → Q = B0/N be the quotient homomorphism. Let S = {a, b, a⁻¹, b⁻¹} be the standard generating set of B0 and S' = φ(S) the image generating set of Q.

Fix g ∈ B0 with d_B0(1,g) = n. By definition of Cayley distance, there exists a word w = s_{i₁}···s_{i_n} over S, |w| = n, with w =_{B0} g.

Apply φ: the word φ(w) = φ(s_{i₁})···φ(s_{i_n}) over S' has length n and satisfies φ(w) =_Q φ(g) = π(g).

Therefore d_Q(1, π(g)) ≤ |φ(w)| = n = d_B0(1,g).

Since this holds for every such w, and in particular for the shortest (the geodesic), we have:

**d_Q(1, π(g)) ≤ d_B0(1, g)** for all g ∈ B0. □

This is exact — no approximation, no assumption beyond φ being a group homomorphism and the generating sets being related by φ. It applies to any quotient of any group.

### Directional Inequality Only

The reverse direction d_B0(1,g) ≤ d_Q(1,π(g)) is FALSE in general. Elements of the kernel N = ker(φ) = γ_k(B0) (for Q = B0/γ_k) can provide "shortcuts" in Q that don't exist in B0. Specifically, two paths in B0 with the same Q-image but different B0-endpoints may allow Q to reach π(g) faster than B0 can reach g.

**Proposed label "quotient-GT" rather than "B0-GT"** is correct, necessary, and should be enforced in all Stage 2 reporting.

---

## CRITICAL NUANCE: The Zero-Lower-Bound Trap

**The lower bound d_Q(1, π(g)) is useful only when g ∉ ker(φ).**

For g ∈ N = ker(φ), d_Q(1, π(g)) = d_Q(1, 1_Q) = 0 exactly — regardless of d_B0(1,g). The lower bound is exactly zero and completely uninformative.

### Concrete consequences for Q4 and Q5

| Quotient | Kernel | Elements with d_Q = 0 (unconditionally) |
|---|---|---|
| Q4 = B0/γ5 | γ5(B0), order 5^26 | All elements of γ5(B0) — the entire LCS depth ≥ 5 |
| Q5 = B0/γ6 | γ6(B0), order 5^24 | All elements of γ6(B0) — LCS depth ≥ 6 |

For Q4: **any element at LCS depth ≥ 5 projects to d_Q4 = 0**. This includes all commutator-of-commutator-of-commutator elements and deeper. The Q4 distance is blind to all of the lower 26 dimensions (out of 34) of B0.

For Q5: **any element at LCS depth ≥ 6 projects to d_Q5 = 0**. This is blind to the lower 24 dimensions.

### Corpus design implication

If the generated-candidate corpus draws elements from γ5(B0) or below (possible, since [G,G] = γ2 ⊃ γ5), the Q4 ground truth evaluates to 0 for all hard-stratum words — the same structural blindness as the Stage 1 geodesic corpus trap. This is the same failure mode: constant ground truth → undefined correlation.

**Mitigation**: generate candidates that are provably NOT in the kernel of the chosen quotient.
- For Q4 GT: confirm d_Q4 > 0 before including a word in the stratum III test corpus (discard words in γ5).
- For Q5 GT: confirm d_Q5 > 0 (discard words in γ6).
- Or: pre-filter corpus to elements at the target LCS depth (γ5 \ γ6 for weight-5 testing with Q5).

This filtering is computationally feasible: project each candidate word to Q4/Q5 and check whether its image is identity. Discard those that project to identity.

---

## Claim 2: Q4 Collapses Weight-5 pcgs Coordinates

**#status/proven.**

### Analysis

The pcgs (polycyclic generating system) for B0 = B0(2,5) has weight ordering:
- Weight-k generators lie in γ_k(B0) \ γ_{k+1}(B0)
- Weight-5 generators span γ5(B0)/γ6(B0) ≅ (F5)^2 (2-dimensional, per GAP LCS receipt [[2026-06-26-b25-lcs-dimensions-gap-receipt]])

The projection π4: B0 → Q4 = B0/γ5(B0) maps the kernel γ5(B0) to identity. The weight-5 generators all lie in γ5(B0), so all weight-5 pcgs coordinates project to 0 in Q4.

**Any weight-5 feature evaluated in Q4 is identically zero for every element of B0.**
Testing a weight-5 proxy using Q4 ground truth is therefore circular and uninformative — the feature is constant zero, undefined correlation.

### Minimum quotient requirement for weight-5 testing

Q5 = B0/γ6(B0) has kernel γ6(B0). Weight-5 generators lie in γ5(B0) \ γ6(B0) — outside the kernel. Therefore weight-5 pcgs coordinates are NOT collapsed in Q5.

For g ∈ γ5(B0) \ γ6(B0): π5(g) ∈ γ5/γ6 ≅ (F5)^2 is a nonzero vector in Q5. Testing a weight-5 feature against d_Q5 is meaningful.

**Minimum quotient for weight-5 feature testing: Q5 = B0/γ6(B0), order 5^10.**

More generally: to test a weight-k feature (coordinates in γ_k/γ_{k+1}), the minimum quotient that preserves it is B0/γ_{k+1}(B0).

### LCS weight table (from GAP receipt)

| Weight k | dim(γ_k/γ_{k+1}) | Minimum Q for weight-k testing |
|---|---|---|
| 1 | 2 | Q1 = B0/γ2, order 5^2 |
| 2 | 1 | Q2 = B0/γ3, order 5^3 |
| 3 | 2 | Q3 = B0/γ4, order 5^5 |
| 4 | 3 | Q4 = B0/γ5, order 5^8 |
| **5** | **2** | **Q5 = B0/γ6, order 5^10** |
| 6 | 4 | Q6 = B0/γ7, order 5^14 |
| ... | ... | ... |
| 9 | 6 | Q9 = B0/γ10, order 5^28 |

For Stage 2, the feasible quotients are Q4 (5^8 ≈ 390,000 elements) and Q5 (5^10 ≈ 9.8M elements). Both are tractable for BFS or direct pcgs evaluation.

---

## Approved Wording for Stage 2 Reporting

**Quotient-distance wording (approved):**

> "Ground truth: d_{Q_k}(1, π_k(g)) — Cayley distance in the quotient Q_k = B0(2,5)/γ_{k+1}(B0) under the natural quotient map π_k, with generating set images of {a,b}. This satisfies d_{Qk}(1,π_k(g)) ≤ d_{B0}(1,g) by the quotient-map inequality (theorem). It is a rigorous lower bound on true B0 Cayley distance, not equal to it in general. Labeled quotient-GT (not B0-GT)."

**Weight-5 pcgs testing (approved):**

> "Weight-5 pcgs features (π5 coordinates in γ5/γ6 ≅ (F5)^2) require Q5 = B0/γ6 at minimum. In Q4 = B0/γ5, all weight-5 coordinates collapse to zero — Q4 is insufficient for weight-5 feature validation."

**Kernel-zero caveat (must appear in any Stage 2 result using quotient GT):**

> "Candidates with d_Qk = 0 (i.e., those projecting to identity in Qk, equivalently those in γ_{k+1}(B0)) provide no quotient-GT signal and must be excluded from the correlation computation or reported separately as 'Q_k-invisible.' Failing to exclude them produces artificially inflated zero-fractions and undefined correlation."

---

## Verdict Summary

| Claim | Status | Notes |
|---|---|---|
| d_Q ≤ d_B0 (lower bound theorem) | **PROVEN** | Exact; applies to any quotient |
| "Quotient-GT" label rather than "B0-GT" | **APPROVED** | Required in all Stage 2 results |
| Q4 collapses weight-5 to zero | **PROVEN** | Testing weight-5 in Q4 → undefined correlation |
| Q5 minimum for weight-5 testing | **PROVEN** | Q5 = B0/γ6, order 5^10 |
| Kernel-zero caveat | **ADDED** (not in original request) | Mandatory for corpus soundness |

**Stage 2 reporting is mathematically scoped if all four conditions appear:** (1) quotient-GT label, (2) quotient inequality stated, (3) Q5 used for weight-5 features, (4) kernel-zero candidates excluded or flagged.

## Notes for Downstream

- **Math-expert / Experimenter-B25**: add the kernel-zero corpus filter before running Stage 2. Discard any generated candidate whose projection to the chosen Q_k is identity. A corpus with many γ_{k+1}-deep elements will reproduce the Stage 1 constant-GT trap.
- **Lead**: these caveats are binding on Stage 2 result interpretation. Any report using "B0 distance" instead of "Q_k distance" is mathematically overclaiming.
- **Developer**: implementing d_Qk correctly requires (i) building Q_k = EpimorphismPGroup(G,5,k) in GAP or equivalent, (ii) projecting each candidate word, (iii) computing Cayley BFS in Q_k under image generators. Q4 BFS is ~390k nodes (feasible); Q5 BFS is ~9.8M nodes (feasible with care).
