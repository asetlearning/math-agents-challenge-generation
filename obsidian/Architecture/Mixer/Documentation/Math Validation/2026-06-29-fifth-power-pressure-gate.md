---
title: 'Reducible-Fifth-Power Pressure' — Math Object Gate
status: proven
domain: group-theory
project: b25
claim: "The 'reducible-fifth-power pressure' scoring object is mathematically sound for use as a B0(2,5) spelling-heuristic triage feature; collapse savings are correct; feature is B0-internal with no free-B(2,5) assumption; three pre-reg parameters must be declared."
claimant: Math-expert (object gate request, Lead relay 2026-06-29)
verification_method: first-principles exponent-5 law analysis; computational complexity estimate
tools_used: [exponent-5 law in B0(2,5), free-group cancellation conventions]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25, topic/proxy-validation, topic/fifth-power-pressure, status/proven, proof]
---

# Validator Gate — 'Reducible-Fifth-Power Pressure' Math Object

## Gate Decision

**APPROVED** — with three required pre-reg parameters declared before any run, and one mandatory labeling requirement. The object is mathematically sound as a B0(2,5) spelling heuristic.

---

## Gate Q1 — Collapse-Saving Correctness

### Exact u^5 block: saving = 5|u| ✓

In B0(2,5), x^5 = 1 for every group element x. For a freely reduced word w, a literal contiguous substring u·u·u·u·u of length 5|u| represents the group element u^5 = 1_B0. The substring can be deleted, saving exactly 5|u| characters. This is exact — no approximation, no assumption beyond the exponent-5 law.

**Proof**: The word w = α·(u^5)·β with α,β the surrounding subwords represents the same B0 element as α·1·β = α·β. The rewriting is: delete the u^5 substring, concatenate α and β (then freely reduce if needed). Net length reduction = 5|u|. □

### Conjugated block p·u^5·p^{-1}: saving = 5|u| + 2|p| ✓

In B0, p·u^5·p^{-1} = p·1·p^{-1} = 1. A literal substring p·u·u·u·u·u·p^{-1} of length 5|u|+2|p| can be deleted in its entirety. Saving = 5|u| + 2|p|. Also exact.

**'Bounded shell visible' — interpretation**: this is a computational search bound (|p| ≤ K for declared threshold K), NOT a mathematical condition for the law to hold. The equality p·u^5·p^{-1} = 1 in B0 is unconditional for any p, any u. Bounding |p| limits which conjugated patterns the feature *finds* when scanning the word — it does not affect mathematical correctness of the instances it does find. The saving formula is exact for every found instance regardless of |p|.

### u^6 — EXACT, not near-block

u^6 = u·u^5 = u·1 = u in B0. Therefore a literal u^6 substring (length 6|u|) represents the same group element as u (length |u|). The saving from removing u^5 from u^6 = 5|u|. This is exact — same category as u^5, not a near-block approximation.

**Design recommendation**: the pre-reg should distinguish u^6 (exact saving 5|u|, same as u^5 category) from u^4 (heuristic near-block only). Grouping them both as "near-blocks" understates the u^6 contribution.

### u^4 — heuristic pressure only

u^4 is one step away from u^5. No guaranteed saving — if u^4 appears and one adjacent rewriting can produce one more u, then u^5 = 1 applies. The "pressure" interpretation is: u^4 signals potential opportunity. This is a valid heuristic signal. The score contribution for u^4 should be labeled as heuristic pressure, not an exact saving.

### Summary of savings table

| Pattern | Saving | Exactness |
|---|---|---|
| u^5 (literal) | 5\|u\| | **Exact** — theorem in B0 |
| p·u^5·p^{-1} (bounded shell) | 5\|u\| + 2\|p\| | **Exact** for each found instance |
| u^6 (literal) | 5\|u\| | **Exact** — u^6 = u in B0 |
| u^4 (literal) | heuristic (0 guaranteed) | **Heuristic** — near-block pressure |

---

## Gate Q2 — Well-Defined and Cheaply Computable

### Well-defined, pending three declared parameters

The mathematical concept is unambiguous. The feature is fully determined once:

1. **Overlap downweighting convention** — if two u^5 patterns overlap (e.g., ababababababab where ababab overlaps), applying one might destroy the other. The convention (e.g., greedy left-to-right, or maximum-non-overlapping packing) must be stated in the pre-reg before any run. Any deterministic convention is mathematically acceptable; what matters is that it is declared.

2. **Shell threshold K** — the maximum |p| for searching conjugated blocks p·u^5·p^{-1}. Larger K = more patterns found = higher coverage but slower scan. Must be declared.

3. **Cyclic-rotation convention** — if "cyclic-rotation handling" means checking rotations of the word, the rotation scheme (all 2n rotations? some subset?) must be stated. If it means handling u where u wraps around the word boundary (closed-curve convention), that too must be declared.

Once these three are declared, the feature is a deterministic function of the input word — well-defined.

### Computational complexity

For |u| ≤ 4 over generators {a, b, a^{-1}, b^{-1}} (4 generators):
- Distinct u-strings: 4^1 + 4^2 + 4^3 + 4^4 = 4 + 16 + 64 + 256 = 340
- For each u, scanning a word of length n for 5 consecutive occurrences: O(n)
- Total for exact u^5 blocks: O(340n)
- Conjugated blocks |p| ≤ K: O(340 · 4^K · n) — linear in n for any fixed K

**Overall: O(n) per candidate word** (with constant factor depending on |u|_max and K). Computationally cheap. A standard string-scan implementation suffices.

---

## Gate Q3 — B0-Internal, No Free-B(2,5) Assumption

**Completely B0-internal. No free-B(2,5) assumption. No [CONDITIONAL] tag required for the feature itself.**

The exponent-5 law u^5 = 1 for all u is a definitional axiom of B0(2,5) — it's what makes B0 an exponent-5 group. This holds in B0 unconditionally, independently of:
- Whether B(2,5) is finite (Kourovka 11.48 — open)
- HWW 1974 (which establishes B0's structure, not B(2,5)'s finiteness)
- Any citation

The [CONDITIONAL: B0 ≅ B(2,5)] tag applies only if results are claimed to extend to free B(2,5). The feature as a B0 triage score carries no such claim.

---

## Mandatory Labeling Requirement

**This feature is a SPELLING HEURISTIC, not a B0 group invariant.**

Two words representing the same element of B0 with different spellings can have different pressure scores. The score depends on which literal string patterns appear in the input word, not only on the group element the word represents.

This is acceptable — and expected — for a triage/proxy feature. The requirement is that the pre-reg and any result report explicitly say:

> "Reducible-fifth-power pressure is a spelling heuristic: it measures literal pattern occurrences in the input word, not an intrinsic property of the group element. Two words representing the same B0 element may score differently."

Failing to include this label would allow the feature to be misread as a B0 group-theoretic invariant (comparable to pcgs coordinates, which ARE group invariants). The distinction matters for interpreting correlations.

---

## Approval Conditions Summary

| Condition | Status |
|---|---|
| Collapse savings mathematically correct | **APPROVED** — exact for u^5, u^6, conjugated; heuristic for u^4 |
| Feature well-defined | **APPROVED** pending 3 declared pre-reg parameters (overlap convention, K, rotation scheme) |
| B0-internal, no free-B(2,5) assumption | **CONFIRMED** — no [CONDITIONAL] tag on feature itself |
| Spelling-heuristic label required | **MANDATORY** — must appear in pre-reg and all result reports |
| u^6 reclassification | **RECOMMENDED** — treat as exact saving (= u^5 category), not near-block; update scoring weight |

**GATE: OPEN for use as a B0/Q5 triage feature**, subject to the above conditions.

## Notes for Downstream

- **Math-expert**: declare the three parameters (overlap convention, K, rotation scheme) in the pre-reg before any run. Add the spelling-heuristic label. Consider reclassifying u^6 as exact rather than near-block.
- **Experimenter-B25**: the feature scans the input word string — ensure inputs are freely reduced before scoring (kbmag normal-form words are freely reduced; raw beam candidates may not be).
- **Lead / Maria**: this gate covers the mechanism-score only. The compound `z(-Arm1) + 0.5·z(layer)` uses existing features and needs no new gate; this note covers only the fifth-power pressure object.
