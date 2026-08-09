---
title: "Defining and Characterizing Reward Hacking"
authors:
  - "Joar Skalse"
  - "Nikolaus H. R. Howe"
  - "Dmitrii Krasheninnikov"
  - "David Krueger"
year: 2022
venue: "arXiv:2209.13085 (NeurIPS 2022); revised March 2025"
url: "https://arxiv.org/abs/2209.13085"
url_translated:
language: en
methodology_type: theoretical
domain: ai
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
  - "[[agostinelli-2019-deepcubea]]"
quality_notes: "Formal-theory backing for Validator's finding that a value head trained on braid_reduce labels will structurally entrench the reducer's blind spots. Key theorem: for the set of ALL stochastic policies, two reward functions are unhackable only if one is constant — i.e. essentially any imperfect proxy is hackable in full generality; unhackability requires restricting the policy/search class, not better training of the proxy itself. This formally supports the two-tier design (learned V guides search, real reducer/oracle certifies) as the structurally correct fix, not a training-time workaround."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/value-network
  - paper
  - status/draft
---

# Defining and Characterizing Reward Hacking

## Abstract

"We provide the first formal definition of reward hacking, a phenomenon where optimizing an imperfect proxy reward function leads to poor performance according to the true reward function, building on a foundation of partial monitoring theory. We show that our definition captures the intuitive meaning of reward hacking and enables us to analyze the conditions under which reward hacking can occur. In particular, we identify four sufficient conditions for reward hacking to occur, and we present nine potential approaches to designing unhackable proxies. We provide formal results establishing when unhackable proxies exist, and when they don't. In particular, we show two important negative results: 1) for the set of all stochastic policies, two reward functions can only be unhackable if one of them is constant, and 2) unless we have a very high level of task-specific prior knowledge, it is impossible to construct unhackable proxies from partial observations."

## TL;DR

Formal, theoretical (not empirical) characterization of exactly the failure mode Validator flagged for the B25 value head: optimizing an imperfect proxy (a value network trained on `braid_reduce` labels, which is systematically blind to ~43% of the state space — products-of-conjugates) reliably leads to poor performance on the TRUE objective (actual distance to identity), because search will preferentially move toward regions the proxy scores well, which — precisely where the proxy is blind — are NOT the regions that are actually closest to the goal. The paper's two negative results are the load-bearing content: (1) for the full space of stochastic policies, no non-trivial proxy is unhackable — meaning "train a better value net" cannot, in general, fully close this gap, and (2) building an unhackable proxy from PARTIAL observations (exactly our case — a value net sees only a word, not the true distance-to-identity ground truth) is impossible without strong task-specific prior knowledge.

## Problem

When does optimizing against an imperfect/proxy reward or value function lead to bad outcomes according to the TRUE objective, and can proxies be designed to avoid this ("unhackable" proxies)?

## Approach

Formalizes reward hacking using partial monitoring theory: a proxy reward is "unhackable" (relative to a policy class and a true reward) if increasing expected proxy return can never decrease expected true return. Derives four sufficient conditions under which hacking occurs, and analyzes nine candidate strategies for designing unhackable proxies, proving formal existence/non-existence results for each under different policy-class restrictions.

## Key result

Two negative results, both directly load-bearing for our case:
1. **"for the set of all stochastic policies, two reward functions can only be unhackable if one of them is constant"** — i.e., over the FULL space of possible search/generation policies, essentially no non-trivial proxy reward/value function is safe from being hacked. This means restricting the POLICY/SEARCH CLASS (not just improving the proxy) is necessary for safety — directly supporting a two-tier design where the search process itself is constrained (e.g., candidates the value net favors still get certified by the real reducer before being trusted) rather than trusting the value net's ranking unconditionally.
2. **"unless we have a very high level of task-specific prior knowledge, it is impossible to construct unhackable proxies from partial observations"** — a value head trained on a WORD (partial information relative to the true, expensive-to-compute distance-to-identity) cannot in general be made unhackable through better training alone; the partial-observation structure itself is the obstruction, not a fixable training detail.

## Assumptions

Formal RL framing (policies, reward functions, partial monitoring) — abstracts away from any specific domain, which is both the strength (generality) and limitation (no B(2,5)-specific or even game/puzzle-specific empirical content) of this paper.

## Limitations / scope

Purely theoretical — no experiments, no B(2,5) or group-theory content, no direct empirical demonstration of the DeepCubeA/Segler-style systems hacking their own value estimates (those systems' proxies happen to be well-behaved because Rubik's Cube / retrosynthesis training data isn't documented as having a KNOWN systematic blind spot the way `braid_reduce`'s 43% zero-fire class is — this is a genuine disanalogy worth noting: the flagship value-network precedents in R1 don't have a DOCUMENTED adversarial blind spot in their training signal the way B(2,5) does, so this paper's warning applies MORE sharply to our case than to the precedents we're drawing on).

## Why this paper matters

This is the formal justification for why Validator's "value-as-score is DISPROVEN, only two-tier is sound" finding is not just an empirical caution but a theoretically expected outcome: a value head trained on `braid_reduce` labels is optimizing against a proxy with a KNOWN, structured blind spot (products-of-conjugates, 43% zero-fire), and per Skalse et al.'s first negative result, no amount of retraining the value net alone (without restricting what the surrounding search/generation process is allowed to trust it for) can be guaranteed to avoid entrenching that blind spot — because the value net will learn "far from identity" precisely in the region it can't see progress in, which is exactly what Lead's addendum describes. The correct structural response, per this paper's own framing, is restricting the POLICY CLASS around the proxy (i.e., exactly the two-tier design: value net proposes/ranks, but the real reducer or a GAP oracle certifies before anything is trusted) — not attempting to train away the bias.

## Quotes

1. > "for the set of all stochastic policies, two reward functions can only be unhackable if one of them is constant" — Abstract
2. > "unless we have a very high level of task-specific prior knowledge, it is impossible to construct unhackable proxies from partial observations" — Abstract

## Open questions surfaced

Which of the paper's nine candidate "unhackable proxy design" strategies (not enumerated in the abstract; would need a full-text read of the paper's technical sections) might apply to constraining the B(2,5) search/generation policy class specifically — this is a concrete follow-up read for Validator/Math-expert if the two-tier value-head design proceeds past this literature-scan stage.

## Related material in vault

- Related: [[agostinelli-2019-deepcubea]] (a value-network precedent whose training signal, unlike B(2,5)'s, has no documented adversarial blind spot — the disanalogy that makes this paper's warning sharper for us)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
