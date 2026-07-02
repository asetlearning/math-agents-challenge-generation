---
title: "B(5,3) Proxy Validation — experiment type root"
domain: group-theory
project: b25
instance: B(5,3) → B(2,5)
experiment_type: proxy-validation
status: pending
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/proxy-validation, topic/patternboost, project/b25, status/pending, experiment-type]
---

# Proxy Validation Study (B(5,3) lab → B(2,5) transfer)

Use B(5,3) as a finite, solvable lab to validate a score proxy for "distance to identity"
that is structurally general (defined identically in any Burnside group). The validated
proxy is then transferred to B(2,5) as the PatternBoost objective function.

## Motivation

The current B(2,5) PatternBoost proxy (reduction_ratio, Option B) was found by Validator
to be blind on ~43% of words: products-of-conjugates like `(aba)^5` get ratio=0.000 because
no shortlex rule fires on them. We cannot diagnose this on B(2,5) (no ground truth).
B(5,3) is finite (order 2187), completely solvable, and the shortlex KB runs in 1.7s —
perfect for proxy validation.

## Experiment phases

| Phase | Name | Status |
|---|---|---|
| Step A | Regenerate B(5,3) ground truth (153/153) | `#status/complete` (2026-06-17) |
| Step B | Define candidate proxies (structurally general) | `#status/complete` (pre-reg 2026-06-17) |
| Step C | Correlation study: proxy vs ground truth | Pending Validator gate + corpus generation |
| Step D | Transfer: winning proxy → B(2,5) | Pending Step C |

## Related material

- [[_progress|B(2,5) Progress Note]] — standing progress note
- [[PatternBoost/_type]] — downstream consumer of the winning proxy
- [[methodology/b53-proxy-validation-study-2026-06-17]] — full pre-registration
- [[Agents/maumayma/Experimenter-B25/output/b53-step-a-ground-truth-2026-06-17]] — Step A evidence
