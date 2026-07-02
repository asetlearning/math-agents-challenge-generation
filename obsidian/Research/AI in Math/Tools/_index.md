---
title: "Research/AI in Math/Tools/ — Reference notes for mathematical-discovery tools"
domain: ai
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/patternboost
  - convention
  - status/draft
---

# Research/AI in Math/Tools/ — What this subtree is for

This subtree holds **reference notes** (`#type/reference`) for tools, libraries, and software infrastructure relevant to AI-guided mathematical discovery. These are not paper summaries — they document tools we may actually run.

Distinct from:
- `Research/AI in Math/ML/` — paper summaries for ML-for-math publications
- `Research/AI in Math/RL/` — paper summaries for RL-guided search publications
- `Concepts/` — cross-domain concept hubs

## Contents

| Note | What it covers |
|---|---|
| [[axplorer]] | PatternBoost reference implementation (Python, DataPoint ABC); B(2,5)/Mixer extension point |
| [[patternboost-v1-lineage]] | Historical v1 Julia+Python PoC — context only |

## Relationship to ML/ subdirectory

The paper that introduced PatternBoost ([[charton-2024-patternboost]]) lives in `Research/AI in Math/ML/`. This Tools/ subtree holds the implementation notes needed to actually run the PatternBoost loop. The two subdirs are complementary.
