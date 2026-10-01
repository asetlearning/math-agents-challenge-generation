---
title: 150 B25 challenge words are trivial in B_0(2,5) — independent nq check
status: replicated
domain: group-theory
project: b25
claim: "All 150 words of b25_challenge_original_freelyreduced.json are trivial in B_0(2,5)=R(2,5)=B(2,5)/gamma_13 (order 5^34, class 12). NOT a claim about free B(2,5)."
claimant: Experimenter-B25
verification_method: independent oracle — nq NilpotentQuotient with identical relation x^5 (class bound 13); own JSON parser; script audit
tools_used: [GAP 4.15.1, nq 2.5.11, polycyclic 2.17 (verifier); anupq 3.3.2 Pq (producer)]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, project/b25, status/replicated, proof]
---

# Verification — 150 challenge words in B_0(2,5)

Triage: [[2026-09-30-b25-b0-challenge-triviality-triage]]. Producer run: `/media/psf/algo-mixer/runs/b25/b0-challenge-triviality/20260930T200842Z/`.

## Claim
Each of the 150 words maps to 1 in B_0(2,5) (equivalently lies in gamma_13(B(2,5))). Group computed in: **restricted B_0(2,5)**, never free B(2,5).

## Method
1. **Model.** nq on `<a,b; x | x^5>` (identical generator x: all fifth powers, via Higman's lemma, nq manual § Identical Relations), `class:=13`. Result: Pcp-group of order **5^34**, class **12** (class bound 13 did not add a layer, so the quotient stabilised), lower central factors 2,1,2,… sizes (log5) `34 32 31 29 26 24 20 16 12 6 3 1 1`. Images of a,b generate it (true); orders of a,b = 5; 20000 random words' 5th powers = 1. Any 2-generator exponent-5 group of order 5^34 is a quotient of B_0(2,5) of the same order, hence equals it — **premise cited**: |B_0(2,5)|=5^34 (Havas–Newman–Vaughan-Lee 1990; I did not re-derive it; the producer's ANUPQ run gives the same order from a separate code path).
2. **Parsing.** My own python parser of the raw JSON (sha256 067977857d…cd3cde confirmed): 150 keys R1..R150, letters only ±1,±2, all freely reduced, 32 empty, max length per `lens.txt`. Emitted `words_validator.g`; evaluated with my own letter map.
3. **Evaluation.** All 150 words evaluated in nq's group: **150/150 = identity**.
4. **Discrimination controls** (same pipeline): a, a^4, [a,b] nontrivial; a^5, (ab)^5 trivial; random weight-12 left-normed commutators nontrivial in 22/200 samples; weight-13 trivial in 200/200. So the test can return "nontrivial" and the class-12 boundary behaves as theory predicts.
5. **Comparison** with producer `results.csv`: same 150 ids, same lengths, all `yes` in both — **0 disagreements**.
6. **Script audit** (`b0_challenge_triviality.g`): letter map `idx(l)`: 1→a, -1→a^-1, 2→b, -2→b^-1 correct; word read left to right, product in that order; empty word → One(P), handled; images of a,b are `Image(epi,F.i)` of the generators of the Range, and generation checked; order 5^34 and class 12 checked; controls run. Their `words.g` parsed independently equals the raw JSON (150/150 words, order preserved). Minor: their "EXPONENT5_ON_PCGS" check only tests pcgs elements (weak); exponent 5 rests on `Exponent:=5` in Pq, cross-certified here by nq's law + order agreement. No error found.

## Artifacts
`Agents/asetlearning/Validator/scratch/b0-challenge/`: `nq_oracle.g`, `ctrl.g`, `words_validator.g`, `nq_results.csv`, `nq_stdout.log`, `lens.txt`.

## Verdict
**#status/replicated** for: "all 150 words are trivial in B_0(2,5)". Two independent exact computations (ANUPQ p-quotient; nq nilpotent quotient) agree on the group (order 5^34, class 12) and on every word. Not upgraded to `proven` per doctrine (computational claim; order of B_0(2,5) taken from literature). No dispute.

### Limits
Says nothing about free B(2,5): triviality in the finite quotient B_0(2,5) is necessary, not sufficient, for triviality in free B(2,5) (Kourovka 11.48 open). Equivalent phrasing allowed: each word lies in gamma_13(B(2,5)).
