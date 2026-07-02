---
title: "B(3,3) LCS-Weight-2 Proxy — Math Soundness Verdict (Proxy D gate)"
status: conjectured
domain: group-theory
project: b25-patternboost
claim: "The LCS-weight-2 proxy (balanced-mod-3 L1 norm of the gamma2/gamma3 exponent vector) is a mathematically sound necessary-condition distance for B(3,3), conditional on two implementation amendments; whether it correlates with geodesic distance on [G,G] is the empirical v2 question."
claimant: "B25 Experimenter (proposed proxy D for v2 B(3,3) proxy-validation study, 2026-06-17)"
verification_method: "GAP 4.15.1 coset enumeration + LCS membership checks + algebraic derivation (Hall 1933 basic commutator theory)"
tools_used:
  - "GAP 4.15.1"
author: maumayma
tags:
  - agent/validator
  - user/maumayma
  - domain/group-theory
  - project/b25-patternboost
  - topic/b33
  - topic/patternboost
  - topic/lower-central-series
  - topic/burnside
  - status/conjectured
  - proof
---

# Verification — B(3,3) LCS-Weight-2 Proxy (Proxy D Gate)

Routed from Lead (routed from Maria) as a pre-registration gate for the B(3,3) proxy-validation study v2. Three sub-questions on the algebraic definition of proxy D. GAP 4.15.1 used for all computational checks.

**Group confirmed:** B(3,3) = free Burnside group of rank 3 and exponent 3. Order 2187 = 3^7, verified earlier in this session via explicit coset enumeration.

**LCS structure (GAP-confirmed):**

| Level | Size | Generators in pcgs |
|---|---|---|
| γ₁ = G | 3^7 = 2187 | f1,f2,f3,f4,f5,f6,f7 |
| γ₂ = [G,G] | 3^4 = 81 | f4,f5,f6,f7 |
| γ₃ | 3^1 = 3 | f7 |
| γ₄ | 1 | — |

Abelianization: G/γ₂ ≅ (Z/3Z)³. Weight-2 layer: γ₂/γ₃ ≅ (Z/3Z)³. Weight-3 layer: γ₃ ≅ Z/3Z.

---

## Q1 — Well-definedness of weight-2 exponent vector

### The claim
(e₄,e₅,e₆) in the LCS-adapted pcgs normal form is a well-defined invariant of the GROUP ELEMENT (representative-independent).

### Verdict

**#math-verdict/sound** — domain-qualified.

### Evidence

GAP computation: two different word representatives of the same group element give identical exponent vectors.

```gap
# Comm(b,a) and b^-1*a^-1*b*a are the same element in B(3,3):
Comm(gb, ga) -> ExponentsOfPcElement(pcgs, ...) = [ 0, 0, 0, 1, 0, 0, 0 ]
gb^-1*ga^-1*gb*ga  -> ExponentsOfPcElement(pcgs, ...) = [ 0, 0, 0, 1, 0, 0, 0 ]
Same? true
```

In a polycyclic group, the normal form with respect to a fixed pcgs is unique: every group element has exactly one exponent vector. Therefore (e₄,e₅,e₆) is determined by the group element, not by any choice of word representative.

### Domain qualification

The map g ↦ (e₄,e₅,e₆) is a **group homomorphism** only when restricted to γ₂ → γ₂/γ₃ ≅ (Z/3Z)³, where it is the canonical projection with kernel γ₃.

For g ∉ γ₂ (abelianization ≠ 0): (e₄,e₅,e₆) is still a well-defined set function of g, but NOT a homomorphism from G. The non-abelian collector introduces weight-1/weight-2 mixing — e.g., the product ba has e₄=1 (from commuting b past a), while ab has e₄=0.

**Correct domain for the proxy's "necessary condition" interpretation: γ₂ = [G,G].** For words outside γ₂, the weight-2 exponents carry no clean "distance from γ₃" meaning. The proxy still has well-defined values for all g ∈ G, but the interpretation changes.

---

## Q2 — Implementation soundness: IsomorphismPcGroup vs. LCS-adapted pcgs

### The claim
`Image(IsomorphismPcGroup(G))` with default pcgs, reading positions 4–6 as weight-2 exponents, correctly extracts the γ₂/γ₃ layer.

### Verdict

**#math-verdict/qualified → sound with guard.**

### Evidence

GAP verification of LCS membership for each pcgs generator:

```gap
# After IsomorphismPcGroup on B(3,3):
# pcgs[1..3]: LCS weight 1  (not in lcs[2])
# pcgs[4..6]: LCS weight 2  (in lcs[2], not in lcs[3])
# pcgs[7]:    LCS weight 3  (in lcs[3])
LCS weight of each pcgs generator:
  pcgs[1] has LCS weight 1
  pcgs[2] has LCS weight 1
  pcgs[3] has LCS weight 1
  pcgs[4] has LCS weight 2
  pcgs[5] has LCS weight 2
  pcgs[6] has LCS weight 2
  pcgs[7] has LCS weight 3
```

For B(3,3) specifically, GAP's `IsomorphismPcGroup` produces an LCS-adapted pcgs. This happens because the p-quotient algorithm (used internally for p-groups) aligns with the LCS for Burnside groups of exponent p.

### Required amendment — D-FIX-1 (assertion guard)

This LCS-adaptation is **not documented as a guarantee** in GAP's API. The implementation must include a one-time assertion:

```gap
lcs := LowerCentralSeries(H);
Assert(0, ForAll([4,5,6], i -> pcgs[i] in lcs[2] and not pcgs[i] in lcs[3]));
Assert(0, pcgs[7] in lcs[3]);
```

Without this guard, any change in how B(3,3) is constructed (different presentation, different GAP version, different coset enumeration path) could silently produce a non-LCS-adapted pcgs and corrupt all proxy values.

### Additional finding — D-FIX-2 (basis declaration)

The pcgs weight-2 generators f4,f5,f6 are NOT the basic commutators [b,a],[c,a],[c,b]. They are a triangular transform of the commutator basis:

```gap
[b,a] -> [ 0, 0, 0, 1, 0, 0, 0 ]   # f4      (f4  = [b,a])
[c,a] -> [ 0, 0, 0, 1, 1, 0, 0 ]   # f4*f5   (f5 ≠ [c,a]; f5 = f4⁻¹·[c,a])
[c,b] -> [ 0, 0, 0, 1, 2, 1, 0 ]   # f4*f5²*f6
```

The "nonzero ↔ not in γ₃" property is basis-independent (it is a property of the entire layer γ₂/γ₃, not any particular basis). However, the **specific gradient values** for individual words — which drive H2 — depend on which basis is in use. The pre-registration must declare: "proxy D uses the GAP pcgs basis (f4,f5,f6), not the commutator basis {[b,a],[c,a],[c,b]}." If the commutator basis is intended, a change-of-basis matrix must be applied.

---

## Q3 — Balanced-mod-3 L1 norm as a legitimate necessary-condition distance

### The claim
Balanced-mod-3 L1 norm of (e₄,e₅,e₆) is a sound necessary-condition proxy (nonzero ⟹ g ∉ γ₃ for g ∈ γ₂), analogous to abelianization distance (nonzero ⟹ g ∉ γ₂).

### Verdict

**#math-verdict/sound.**

### Evidence

For g ∈ γ₂: the map g ↦ (e₄,e₅,e₆) is the surjective homomorphism γ₂ → γ₂/γ₃ ≅ (Z/3Z)³ with kernel exactly γ₃. Therefore:

> g ∈ γ₃ ⟺ (e₄,e₅,e₆) = (0,0,0)  
> (e₄,e₅,e₆) ≠ (0,0,0) ⟹ g ∉ γ₃   (necessary condition — sound)

GAP verification — all elements of γ₃ and their weight-2 exponents:

```gap
gamma3 has size: 3
Elements of gamma3 and their weight-2 exponents:
  [ 0, 0, 0, 0, 0, 0, 0 ] -> weight-2: [ 0, 0, 0 ]   # identity
  [ 0, 0, 0, 0, 0, 0, 1 ] -> weight-2: [ 0, 0, 0 ]   # f7
  [ 0, 0, 0, 0, 0, 0, 2 ] -> weight-2: [ 0, 0, 0 ]   # f7²
[b,a] weight-2 exponents: [ 1, 0, 0 ]
Is [b,a] in gamma3? false
```

The balanced-mod-3 representation: each eᵢ ∈ {0,1,2} maps to {0,1,-1} (since 2 ≡ -1 mod 3). L1 norm = Σ|balanced(eᵢ)| = number of nonzero components (both 1 and 2 contribute 1). Values in {0,1,2,3}. This is a valid norm on (Z/3Z)³.

### Known blind spot (not a blocker — report as limitation)

Proxy D cannot distinguish γ₃ ∖ {1} from the identity. γ₃ has exactly 2 non-identity elements (f7 and f7²), and both score 0 on the weight-2 proxy. These are the deepest non-identity elements in the LCS. Closing this gap requires reading the weight-3 exponent e₇ as a separate proxy ("proxy E"), which would then satisfy: nonzero e₇ ⟹ g ≠ 1 for g ∈ γ₃. That is a separate discussion for the pre-registration.

---

## Overall verdict

| Question | Tag | Condition |
|---|---|---|
| Q1 — well-definedness | #math-verdict/sound | Domain = γ₂ for homomorphism; well-defined set function on all G |
| Q2 — implementation | #math-verdict/qualified | → sound with D-FIX-1 (assertion guard) + D-FIX-2 (basis declaration) |
| Q3 — metric | #math-verdict/sound | Necessary condition verified; γ₃ blind spot is a known limitation |

**Proxy D overall status: #status/conjectured.**

The math properties (Q1, Q3) are proven; Q2 is sound with the required guards. What remains conjectured is whether the proxy *correlates* with geodesic distance on [G,G] in B(3,3). That is the empirical question the v2 run is designed to answer.

DO NOT read this note as "the proxy works." It reads as: "the proxy is mathematically computable, its values are group-element invariants, and nonzero ↔ not in γ₃ is a valid necessary condition. Whether nonzero correlates with 'far from identity' in the word metric is open."

---

## Gate status for v2 run

**Blocked until:** D-FIX-1 and D-FIX-2 land in the pre-registration (Lead has confirmed both are now in the amended pre-reg as of 2026-06-17).

**Not blocked:**
- Q2(a) oracle false negatives: possible (non-confluent rule set gives no completeness guarantee)
- Q2(b) oracle false positives: impossible (all KB rules are valid equations; rewriting to ε is a sound proof)
- Corpus seeding with γ₂ words: [aᵢ,aⱼ] for all pairs is confirmed non-identity, order 3 each

---

## Notes for downstream agents

**B25 Experimenter:** Report correlation results for both the full corpus AND the γ₂ slice (abelianization = 0 words) separately. The proxy's gradient is only interpretable as "distance from γ₃" on the γ₂ slice; conflating the two inflates r on the full corpus while obscuring the signal on the blind class. Also report whether γ₃ elements (proxy = 0, geodesic distance > 0) appear in the corpus — they are the known false zeros.

**Transfer caveat (B(3,3) → B(2,5)):** The structural generality of the LCS-weight construction transfers in principle: B(2,5) also has a lower central series with weight layers, and the same proxy definition applies (using the LCS of B(2,5) rather than B(3,3)). However, B(3,3) and B(2,5) differ in rank (3 vs 2), exponent (3 vs 5), and finiteness (finite vs open). The lab correlation in B(3,3) is not a proof that the proxy is useful in B(2,5) — it is a structural-analogy argument. This caveat must appear in the pre-registration.

Verified by [[2026-06-17-b33-lcs-weight-proxy-verdict]] (this note).
