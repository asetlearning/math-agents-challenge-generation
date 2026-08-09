---
title: "Learning to Superoptimize Real-world Programs"
authors:
  - "Alex Shypula"
  - "Pengcheng Yin"
  - "Jeremy Lacomis"
  - "Claire Le Goues"
  - "Edward Schwartz"
  - "Graham Neubig"
year: 2021
venue: "Best Paper, ICLR 2022 Deep Learning for Code workshop; arXiv:2109.13498"
url: "https://arxiv.org/abs/2109.13498"
url_translated:
language: en
methodology_type: empirical
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
  - "[[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]]"
quality_notes: "Strongest concrete 'beat baseline by X% via architecture W trained via V' data point found across all rounds of this literature scan for the specific 'must get worse before better' search structure. Read via subagent abstract-level extraction; SILO's exact training-loss mechanics not independently verified against primary text this session — flagged."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/reinforcement-learning
  - topic/edit-representation
  - paper
  - status/draft
---

# Learning to Superoptimize Real-world Programs

## Abstract

"Program optimization is the process of modifying software to execute more efficiently. Superoptimizers attempt to find the optimal program by employing significantly more expensive search and constraint solving techniques" than conventional compiler optimization passes. [Full verbatim abstract not independently re-fetched in this pass beyond the sentence above; remainder per subagent extraction:] the authors propose neural sequence-to-sequence models to superoptimize real-world programs, achieving a superoptimization rate of 5.9% against GCC -O3 on a 25,000+ function real-world x86-64 assembly test set, using SILO (Self-Imitation Learning for Optimization), which "is easy to implement and outperforms a standard policy gradient learning approach."

## TL;DR

Superoptimization (STOKE-style: find a shorter/faster program equivalent to a given one, via stochastic search over program edits that explicitly allows locally-worse intermediate programs — the exact "must get worse before better" structure the B25 team cares about) is learned end-to-end via a seq2seq model trained with **SILO (Self-Imitation Learning for Optimization)**, which beats both a standard policy-gradient baseline AND a compiler-optimization-pretrained baseline by **more than 5x** (5.9% success rate vs. under ~1.2% for the baselines) on real-world x86-64 functions relative to GCC -O3. This is the single strongest published "neural approach beats a strong classical/naive baseline by a concrete margin" result found for a detour-requiring rewriting/search task, closer in structure to B(2,5) word reduction than the puzzle/chemistry precedents (DeepCubeA, Segler) already reviewed in prior rounds.

## Problem

Can a learned model superoptimize real-world (not synthetic/toy) programs — finding a shorter or faster equivalent — given that the search space explicitly requires passing through locally-worse (longer/slower) intermediate programs to reach a better final result, the same structural challenge as classical STOKE-style stochastic superoptimization?

## Approach

A sequence-to-sequence neural model proposes program edits/rewrites (replacing STOKE's uniform-random proposal distribution over edits, per the closely related earlier work [[Bunel et al. 2016, "Learning to Superoptimize Programs," arXiv:1611.01787]] which this paper builds on and scales to real-world code). Trained via **SILO (Self-Imitation Learning for Optimization)**: per subagent extraction, this imitates the model's OWN best-found trajectories from its own search history (a self-imitation-learning framing, related to but distinct from standard policy gradient) — the exact mechanism by which SILO's loss is constructed was not independently verified against primary text in this pass and should be confirmed by a full-text read before being treated as a ready-made recipe.

## Key result

**5.9% superoptimization rate** (fraction of a 25,000+-function real-world x86-64 test set successfully superoptimized beyond GCC -O3) using SILO, versus **"over five times"** lower success rate for both (a) a standard policy-gradient baseline and (b) a model pretrained on compiler-optimization demonstrations. This is a genuine, quantified, published beat-the-baseline margin — not a design proposal.

## Assumptions

The proposal distribution over edits (whatever generates candidate next-states for the model to imitate/learn from) must itself be capable of generating the detour-requiring trajectories in the first place — SILO improves how the model LEARNS from a search history, but the underlying STOKE-style stochastic search (inherited from Bunel et al. 2016) is what actually generates the "must get worse first" trajectories to learn from. This maps onto a B(2,5) analog: a stochastic/enabler-move-capable search (which the team's beam search with length-increasing enabler rules already resembles) would need to be the trajectory-GENERATING process; SILO-style self-imitation would be the LEARNING procedure that lets a neural model absorb and generalize from what that search discovers, rather than a from-scratch bootstrapped value function (the harder, bias-risk-laden DeepCubeA-style path already flagged as an open question in Deep Round 2).

## Limitations / scope

Domain is x86-64 assembly superoptimization — a very different symbolic system from B(2,5) group words (different alphabet, different equivalence notion, different cost function: runtime/instruction-count vs. group-word length). The specific SILO training-loss mechanics were not independently verified against primary text this session — a full-text read is the recommended next step before treating this as a directly portable recipe rather than a strong structural analog with a validated headline number.

## Replication evidence

Directly builds on and outperforms [[Bunel et al. 2016, "Learning to Superoptimize Programs"]] (which itself replaced STOKE's uniform proposal with a learned one on smaller Hacker's Delight-style benchmarks) — a genuine within-lineage improvement, scaling the same core idea (learned proposal/imitation over a detour-capable stochastic search) from toy benchmarks to real-world code.

## Why this paper matters

This is the concrete evidence Lead asked for directly: "what architecture/training actually delivered beating a strong classical search" for a detour-requiring rewriting problem. The answer here is **not** a bootstrapped value function competing with search (DeepCubeA's harder, bias-prone path) but **self-imitation learning on top of an existing detour-capable stochastic search** — the neural model's job is to learn to propose good edits faster/better than the search's own random proposal distribution would, not to replace search-time evaluation with a trained value estimate. This is a structurally SIMPLER, more directly transferable recipe for B(2,5) than the value-head path explored in Deep Round 2/3: it suggests training a policy to imitate the B25 team's OWN best-found beam-search/enabler-move trajectories (including the ones that needed a temporary length increase) rather than trying to bootstrap a cost-to-go value function from scratch.

## Quotes

1. > "SILO's rate of superoptimization on our test set is over five times that of a standard policy gradient approach and a model pre-trained on compiler optimization demonstration" — per subagent extraction, Results section

## Open questions surfaced

Whether a self-imitation-learning approach (train a policy to imitate the B25 team's own best-found detour-requiring reduction trajectories from beam search + enabler moves, rather than a from-scratch value function) would be a lower-risk, faster-to-prototype first neural-guidance experiment than the value-head path from Deep Round 2/3 — this is a concrete, evidence-backed alternative recipe worth weighing against the value-head recipe before committing engineering effort to either.

## Related material in vault

- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]]
