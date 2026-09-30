---
title: Triage — 150 B25 challenge words trivial in B_0(2,5)
status: conjectured
domain: group-theory
project: b25
claim: "All 150 words of b25_challenge_original_freelyreduced.json are trivial in B_0(2,5)=R(2,5)=B(2,5)/gamma_13 (order 5^34). NOT a claim about free B(2,5)."
claimant: Experimenter-B25
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, project/b25, status/conjectured, proof]
---

# Triage

## Claim (restated)
Each of the 150 words (letters 1=a,-1=a^-1,2=b,-2=b^-1; 32 empty; sha256 0679778…cd3cde) maps to 1 in B_0(2,5), equivalently lies in gamma_13(B(2,5)). Free B(2,5) is out of scope (Kourovka 11.48 open); finite-quotient triviality is necessary, not sufficient, for free-group triviality.

## Sub-claims
1. Model: the group used is B_0(2,5). Needs: 2-generated, exponent 5, order 5^34 (+ citation |B_0(2,5)|=5^34, Havas–Newman–Vaughan-Lee; any 2-gen exp-5 group of that order is a quotient of B_0 of equal order, hence = B_0).
2. Parsing/mapping: JSON words -> letters; empty words; order; images of a,b are the generators of that group.
3. Evaluation: each word = 1 in that group.

## Tools (probed 2026-09-30)
GAP 4.15.1 (/home/parallels/Research/mixer/gap-4.15.1/gap), anupq 3.3.2, nq 2.5.11, polycyclic 2.17 — all load.
Producer path: ANUPQ Pq (`PqEpimorphism`, exponent 5, class 12).

## Methods inventory
- Independent oracle: **nq** NilpotentQuotient with identical generator x and relation x^5 (nq manual § Identical Relations; uses Higman's lemma), on <a,b;x | x^5>. Different code base, different algorithm (nilpotent quotient over Z, polycyclic Pcp-group arithmetic) from ANUPQ p-quotient. Proves sub-claim 3 (sufficient within B_0) given sub-claim 1.
- My own JSON parser (python, stdlib) -> separate GAP word list; compare to their results.csv.
- Audit of their script (read-only).
- Hard limit: nothing here decides free B(2,5).

## Recommendation
Full verification path within B_0(2,5). Verdict ceiling for the stated claim: proven-in-B_0 conditional on the cited order theorem; free-group statement not addressed.
