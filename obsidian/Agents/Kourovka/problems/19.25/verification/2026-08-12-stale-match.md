---
title: "Verification — Kourovka 19.25 — stale match"
problem: 19.25
claim: "The current Notebook annotation and cited Monticone result answer the exact statement of Problem 19.25 negatively."
claimant: Problem-19.25
target_object: "pairs of equal-order finite groups with equal totient-order sums, one simple and the other queried for simplicity"
witness_object: "counterexamples announced by Monticone and described in arXiv:2607.17477"
witness_equals_target: proven-with-citation
citation: "Current Kourovka PDF p.133; van Doorn–Judin–Monticone–Morrison, arXiv:2607.17477"
verification_method: source-text and primary-abstract exact-match comparison
tools_used: ["pdftotext 24.02.0", "web retrieval"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/finite-simple-groups, project/kourovka, status/replicated]
---

# Verification — Kourovka 19.25

## The claim

The configured current Notebook's negative annotation is an exact answer to 19.25.

## Target vs witness

PDF page 133 asks whether equality of group order and the statistic `sum phi(|g|)` forces `H` simple when `G` is simple. Its annotation says no and cites Monticone. The abstract of arXiv:2607.17477 states that it gives examples showing precisely that group order together with this statistic does not determine simplicity.

## Sub-claims and what each method proves

Direct statement comparison proves the target/result match and answer direction. It does not independently verify the concrete groups or their statistic calculations.

## Evidence

Source extraction records the exact question and `No, it need not be`. Primary search retrieved `On Some Problems from the Kourovka Notebook`, arXiv:2607.17477, whose abstract describes the same counterexample result.

## Verdict

`status/replicated` for the bibliographic exact-match claim. The problem is stale/already answered; only the human may apply `status/solved`.

## Why this verdict

The current source annotation and later primary record agree on the exact invariant and negative answer.

## What is NOT established

The concrete counterexample and its finite calculations were not independently checked in this review.

## What would upgrade it

Retrieve the full preprint and independently check the displayed groups, orders, simplicity statuses, and totient sums.
