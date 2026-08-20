---
title: "Verification — Kourovka 17.76 — stale match"
problem: 17.76
claim: "The cited affirmative results answer the exact source-PDF statement of Problem 17.76."
claimant: Problem-17.76
target_object: "finite groups of order greater than two with exactly one element that is not a commutator"
witness_object: "groups asserted in arXiv:2509.17587 and arXiv:2511.00541"
witness_equals_target: proven-with-citation
citation: "Skresanov, arXiv:2509.17587; Hatem–Siniora, arXiv:2511.00541"
verification_method: source-text and primary-abstract exact-match comparison
tools_used: ["pdftotext 24.02.0", "web retrieval"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/commutators, project/kourovka, status/replicated]
---

# Verification — Kourovka 17.76

## The claim

The current Notebook's affirmative annotation is an exact bibliographic answer to 17.76.

## Target vs witness

PDF page 110 asks whether a finite group `G`, `|G|>2`, can have exactly one element that is not a commutator. Both primary abstracts restate that same question. Skresanov asserts an infinite family; Hatem–Siniora explicitly says it answers Problem 17.76 and gives two examples.

## Sub-claims and what each method proves

Direct text comparison proves exact problem identity and affirmative answer direction. It does not independently verify every construction or the minimal-order result.

## Evidence

The configured PDF says: `Yes, such group do exist, and there are infinitely many examples`, citing Skresanov and Hatem–Siniora. The primary abstracts retrieved at `https://arxiv.org/abs/2509.17587` and `https://arxiv.org/abs/2511.00541` repeat the defining property and affirmative answer.

## Verdict

`status/replicated` for the bibliographic exact-match claim. The problem is stale/already answered; only the human may apply `status/solved`.

## Why this verdict

The source statement and two independent primary records match exactly in quantifiers and property.

## What is NOT established

This review does not line-by-line certify either construction or Hatem–Siniora's minimality claim.

## What would upgrade it

Independent construction checks would certify the exhibited examples, but are unnecessary to confirm staleness.
