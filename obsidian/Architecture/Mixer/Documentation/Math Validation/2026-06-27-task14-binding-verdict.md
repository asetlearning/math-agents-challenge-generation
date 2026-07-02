---
title: Task #14 Binding Verdict — HWW 1974 Scope, 119 Benchmark Words, 2a Gate
status: proven
domain: group-theory
project: b25
claim: "HWW 1974 proves |R(2,5)| = 5^34 for the restricted Burnside group only; 119 benchmark words are pcps relators of B₀(2,5) — trivial by construction; 2a proxy runs on generated candidates in B₀ are mathematically sound; Stage 1 B(3,3) is #14-independent."
claimant: Lead (gate resolution request 2026-06-27)
verification_method: literature vault + Researcher sourcing (VAULT-GROUNDED, local PDF confirmed)
tools_used: [Researcher deliverable [[task14-hww-citation-and-119-words]], [[havas-wall-wamsley-1974]] vault note, benchmark words filesystem]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25, topic/restricted-burnside, topic/benchmark-words, status/proven, proof]
---

# Binding Verdict — Task #14 (Gate Resolution)

## Authority Note

This is a Validator binding verdict. It answers three gate questions from Lead. The verdict on (a)–(c) is binding; the gate call is Validator's alone. Human override only.

---

## Source

Researcher's deliverable: [[task14-hww-citation-and-119-words]] (2026-06-26). Evidence class: VAULT-GROUNDED. Local PDF `docs/papers/1974hww.pdf` confirmed present. WebSearch not required for Q1 or Q2 — vault note contains full citation and content.

Full citation confirmed:

> Havas, G., Wall, G.E., Wamsley, J.W. (1974). "The two generator restricted Burnside group of exponent five." *Bull. Austral. Math. Soc.* **10**, 459–470.

---

## Verdict on Claims (a)–(c)

### (a) HWW 1974 scope: restricted group only

**CONCUR.**

HWW 1974 proves |B₀(2,5)| = 5^34 and nilpotency class = 12 for the **restricted** Burnside group R(2,5) = B₀(2,5). The paper title explicitly says "restricted Burnside group." The vault note confirms: *"Addresses the restricted B(2,5) only — the largest finite quotient. The unrestricted B(2,5) (whether infinite) is NOT addressed."*

Two independent methods (Lie-algebraic + p-quotient algorithm) both converge on 5^34, class 12. The mutual convergence is the within-paper verification. Prior bounds: Kostrikin (1955) established 5^31 ≤ |B₀(2,5)| ≤ 5^34; HWW 1974 pins the exact order.

HWW 1974 does **not** prove:
- That free B(2,5) is finite
- That B(2,5) ≅ B₀(2,5) = R(2,5)

### (b) B₀(2,5) ≅ free B(2,5) is open — Kourovka 11.48

**CONCUR.**

The identification B₀(2,5) ≅ B(2,5) holds IF AND ONLY IF the free Burnside group B(2,5) is finite of order 5^34. This is unproven — it is exactly Kourovka Problem 11.48 (open). All [CONDITIONAL: B₀ ≅ B(2,5)] tags in the synthesis are correct and must remain. They reflect the actual state of the literature, not overcaution.

No upgrade path available within this project: proving B(2,5) finite would require resolving Kourovka 11.48, which is far beyond scope. The conditional is a permanent feature of any claim involving the free group.

### (c) The 119 benchmark words: trivial in B₀ by construction

**CONCUR — with the following precision.**

The 119 words `comm_i_j` = [c_i, c_j] (written as free-group words in {a,b}) derive from the **HWW 1974 pcps** generator numbering. They are pcps commutator relators of B₀(2,5): their triviality in B₀ follows because they **are** axioms of B₀'s group presentation (the power-commutator scheme [c_j, c_i] = c_{k₁}^{α₁}···c_{k_r}^{α_r} is literally the definition of the group structure).

**The circularity risk (per [[project_b25_benchmark_words_trivial]]) is confirmed:**
Testing `comm_i_j = 1 in GAP's B₀` is circular — GAP builds B₀ from the same pcps whose relators are exactly these commutators. The check always passes trivially. It measures nothing about proof difficulty, reduction hardness, or proxy quality.

**Precise category assignment:**
- *In B₀(2,5)*: category (b) in Researcher's taxonomy — the specific coefficients (α values) were established by HWW machine computation, so the triviality is not purely algebraic-logical; it required real computational work. But once the pcps is fixed, they are AXIOMS of B₀ and testing them = 1 is circular.
- *In free B(2,5)*: category (c) — open. If B(2,5) is infinite, these words may NOT be identity there.

**No Kuznetsov named test set:** the 119 comm_i_j words are this project's own collection of HWW pcps relators as reduction targets. No Kuznetsov/Shlepkin paper introduces this specific set. Kuznetsov (2009/2010) uses length-s minimal word sets (P_s) and divergence-candidate words (973 specific words) — neither overlaps the comm_i_j set.

---

## Gate Decisions

### Gate Q1: Binding verdict on (a)–(c)?

CONCUR with all three. See above. No corrections needed to Researcher's sourcing.

**One flag on Kourovka number**: Researcher cites problem 11.48. Validator cannot independently verify the exact Kourovka edition/problem number without a fresh PDF read of the notebook — but this does not affect the gate. The mathematical substance (B(2,5) finiteness is open) is established by Researcher's vault citation and is consistent with the mathematical literature as known to Validator. If the exact Kourovka number matters for a publication, request a fresh Kourovka PDF read; for this gate, it is not required.

### Gate Q2: Are 2a proxy runs sound on generated candidates, B₀-scoped, conditional-tagged?

**YES — 2a runs CLEAR for generated candidates.**

The circularity in (c) is **specific to the benchmark word corpus** (pcps relators). It does NOT extend to generated candidates, which are:
- Words produced by a generative process (random walk, beam search, etc.) not designed to produce pcps relators
- Generically non-trivial in B₀(2,5) — the probability that a random intermediate-length word is a pcps relator is negligible
- Subject to a well-defined Cayley distance in B₀(2,5) = R(2,5), a concrete finite group of order 5^34

Proxy experiments on generated candidates ask: *does the proxy correlate with Cayley distance (or reduction progress) in B₀(2,5)?* This is a legitimate mathematical question about a well-defined finite group. The metric is clean.

**Conditions for CLEAR status** (all must hold):
1. Scope: results claimed about **B₀(2,5)** only; the phrase "in B(2,5)" triggers the conditional tag.
2. Corpus: **generated candidates**, not the 119 comm_i_j benchmark words. If any benchmark words appear in the corpus, exclude them or label them separately.
3. Ground truth metric: **Cayley distance in B₀** (word length after normal-form reduction in B₀) — NOT the identity-test circularity.
4. Conditional tag on any output invoking the free group: [CONDITIONAL: B₀ ≅ B(2,5) / Kourovka 11.48 open].

All four conditions are under Math-expert / Experimenter control and are standard hygiene for this project. No new math issue.

### Gate Q3: Is Stage 1 (B(3,3) Arms 1/3) #14-independent?

**YES — Stage 1 UNCONDITIONALLY CLEAR.**

B(3,3) = free Burnside group rank 3, exponent 3. This group is **finite and its structure is completely known** (|B(3,3)| = 3^9 = 19683, nilpotency class 3, proved by Levi-van der Waerden 1933 and classical methods). No connection to B(2,5), B₀(2,5), or the HWW pcps exists.

Arms 1/3 (periodicity-excess and bounded-descent) require:
- A finite group to test in: B(3,3) ✓
- A corpus of candidate words: B(3,3) generated candidates ✓
- No quotient tables from B(2,5): correct — Arms 1/3 do not use quotient embeddings ✓

Stage 1 has zero dependency on Task #14. It can run immediately and unconditionally.

---

## Summary Gate Table

| Gate | Verdict | Conditions |
|---|---|---|
| (a) HWW scope correct? | **CONFIRMED** | No correction needed |
| (b) [CONDITIONAL] tags stay? | **CONFIRMED** | All [CONDITIONAL: B₀ ≅ B(2,5)] tags remain |
| (c) 119 benchmark words circular? | **CONFIRMED** | Words trivial in B₀ by construction; exclude from proxy scoring corpus |
| 2a proxy runs (generated candidates, B₀-scoped) | **CLEAR** | 4 conditions above; standard hygiene |
| Stage 1 B(3,3) Arms 1/3 | **CLEAR, unconditional** | No #14 dependency at all |

**Overall gate for 2a run queue: OPEN.** Task #14 no longer blocks. Stage 1 can start immediately. B₀-scoped generated-candidate runs proceed under the four conditions above.

---

## What is Still NOT Cleared

- **119 benchmark words as proxy scoring targets**: permanently blocked pending either (i) a proof that B(2,5) is finite (Kourovka 11.48) or (ii) a reformulation that makes the benchmark words non-circular in B₀. The current benchmark-word reduction results tell us about reduction in B₀ starting from pcps relators — a circular measurement of reduction from identity.
- **Claims about free B(2,5)**: any result that says "in B(2,5)" (not "in B₀(2,5)") requires the [CONDITIONAL] tag. This is a permanent tagging requirement, not a gate.

---

## Notes for Downstream

- **Lead**: gate open; relay to Maria. Stage 1 immediate start. 2a runs proceed under B₀-scope + generated-candidate conditions.
- **Math-expert**: pre-regs for 2a runs must (i) state "results in B₀(2,5)" not "B(2,5)", (ii) exclude comm_i_j corpus, (iii) specify Cayley-distance ground truth in B₀.
- **Experimenter-B25**: the comm_i_j benchmark words are not a valid proxy-scoring target. Use generated candidates or a fresh corpus of words verified non-trivial in B₀.
- **Researcher**: Task #14 deliverable is confirmed correct. No revision required. The Kourovka problem number (11.48) should be confirmed if needed for a publication-facing document.
