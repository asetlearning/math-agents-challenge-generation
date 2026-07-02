---
title: B(2,5) Centralizer — Full Enumeration Results (ITEM 2a)
date: 2026-06-26
author: maumayma
domain: group-theory
project: b25-commutator-reduction
status: complete
type: results
scope_correction: "All computation here is in the FINITE RESTRICTED quotient B₀(2,5) (EpimorphismPGroup(G,5,12), order 5^34), NOT the FREE B(2,5) (finiteness OPEN, Kourovka 11.48). C(CoreA) = 5^9 and the word-length statistics below are statements about the restricted quotient. See [[b25-q5-feasibility-verdict]] § CIRCULARITY ANALYSIS."
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b25, project/b25-reduce-core, status/complete, results]
---

> **Scope note:** "B(2,5)"/"B25" here = the **finite restricted quotient B₀(2,5)** (order 5^34), not the free Burnside group. The centralizer and its elements are objects of B₀(2,5).

# Centralizer Full Enumeration — Results

**Pre-registration:** [[cent-full-enum-2026-06-26]]
**Run:** `runs/b25_cent_enum/1782476409/` (git `5aeee6a`, wall-clock 2461s).
**Method:** all 5^9 exponent vectors over the 9 Pcgs generators of C(CoreA); each product reduced under symmetric-shortlex rules (199K-rule bank, ~3000 iters/element). Lengths are **UPPER BOUNDS** on true symmetric-shortlex NF length (non-confluent reduction).

---

## Headline statistics (1,953,125 centralizer elements)

| Statistic                         | Value                                            |
| --------------------------------- | ------------------------------------------------ |
| Total elements enumerated         | **1,953,125** (= 5^9, complete ✓)                |
| Identity (length 0)               | 1                                                |
| **Shortest non-identity element** | **4,998 chars**                                  |
| Longest element                   | **433,834 chars**                                |
| Distinct lengths observed         | 274,379 (elements spread thinly — ~1 per length) |
| Elements < 20,000 chars           | **34**                                           |
| Elements < 10,000 chars           | **5**                                            |
| Elements < 5,000 chars            | **1** (the single ~4,998-char minimum)           |

**Caveat (do not over-read):** these are reduction **upper bounds** under a non-confluent symmetric-shortlex bank (3000 iters/element). The TRUE shortest centralizer element could be shorter than 4,998 — the reduction did not reach confluent NF. A confluent/deeper reduction (or a different ordering) might lower these substantially. So "shortest is ~5,000 chars" is "shortest *found by this run*," not "shortest *possible*."

Artifacts: `enum_results.tsv` (46.5M, all reps), `length_histogram.tsv` (length→count), `centA_gen_words.tsv` (the 9 generators).

---

## What this means for ITEM 2b (the reshape mechanism) — OPEN, not closed

The reshape idea: use rules to steer a target B(2,5) word so a region adjacent to CoreA *becomes* a centralizer element `g`; then `CoreA·g·CoreB → g` fires (sound by construction, since `g` commutes with CoreA). This enumeration was the feasibility input for it.

**What the data says — and what it does NOT say:**

- The centralizer elements found are all **large** (≥ ~5,000 chars under this reduction). So there are no *short* centralizer elements to drop into a word directly.
- **This does NOT mean the reshape is infeasible.** Maria's framing (the live hypothesis): it may actually be **easier** to apply length-increasing / reshaping rules to a target word until it reaches one of these ~1.95M centralizer elements than to reduce the target further. Reasons it remains open:
  1. The centralizer is a **defined attractor set of 1.95M concrete targets** — reaching ANY one unlocks a CoreA cancellation. That is a much larger "win set" than a single shortest form.
  2. The reductions here are upper bounds; true shortest centralizer elements may be smaller, and/or a target's natural reshaped form may land near a centralizer element of comparable size.
  3. "Increase length to enable a bigger cancellation" is a normal reduction move; large intermediate ≠ failure.

**Status: OPEN.** This enumeration provides the centralizer inventory (the attractor set) for ITEM 2b. It does NOT establish that reshape-to-centralizer is or isn't viable. The viable test is the actual reshape experiment (ITEM 2b): can a beam/rule search drive a target word onto a centralizer element? Pre-register and run it before any verdict — do NOT close ITEM 2b on these length statistics alone.

---

## Next step

ITEM 2b — design the reshape/attractor experiment using this 1.95M-element inventory as the target attractor set: score rewrites of B(2,5) target words by proximity to the centralizer, allow length-increasing moves, fire the CoreA·g·CoreB cancellation on arrival. Pre-reg + Maria gate before running. Any rule used in a reduction claim → full GAP word-equality (not abelianization; centralizer elements are in [G,G]).

## Related

- Pre-registration: [[cent-full-enum-2026-06-26]]
- Rule-source framing: [[centralizer-enum-2026-06-25]]
- Scope / restricted-vs-free: [[b25-q5-feasibility-verdict]]
