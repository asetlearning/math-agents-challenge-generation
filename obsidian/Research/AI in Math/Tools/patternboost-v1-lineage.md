---
title: "PatternBoost v1 — Julia/Python Proof-of-Concept (zawagner22)"
url: "https://github.com/zawagner22/transformers_math_experiments"
domain: ai
author: maumayma
stars: 39
language: "Julia + Python"
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/patternboost
  - topic/mathematical-discovery
  - type/reference
  - status/draft
related:
  - "[[charton-2024-patternboost]]"
  - "[[axplorer]]"
---

# PatternBoost v1 — Julia/Python Proof-of-Concept (zawagner22)

> **Historical lineage only.** v1 is the original proof-of-concept for the PatternBoost paradigm ([[charton-2024-patternboost]]). Use [[axplorer]] for any actual implementation. This note exists to document what changed between the PoC and the production implementation.

## What it was

GitHub: zawagner22/transformers_math_experiments — 39 stars. Original proof-of-concept implementing the PatternBoost alternating-search loop:

- **Julia** handled local search (mathematical computation)
- **Python** handled transformer training
- **IPC**: file-based (write/read files between the two processes)
- **Tokenization**: BPE (byte-pair encoding) over mathematical strings
- **Environment spec**: none — no `requirements.txt` or `pyproject.toml`
- **Entry point**: manual orchestration of Julia local search + Python training scripts

## Key differences from axplorer

| Feature | v1 (zawagner22) | axplorer (AxiomMath) |
|---|---|---|
| Local search language | Julia | Python |
| IPC mechanism | File-based | In-process calls |
| Tokenization | BPE | Domain-specific (`SparseTokenizer`, etc.) |
| Resumable training | No | Yes (checkpoints) |
| GPU support | Not documented | Standard PyTorch CUDA |
| Extension path | Manual orchestration | `DataPoint` ABC |
| Environment spec | None | `environment.yml` (torch unpinned — see [[axplorer]] Risk 3) |

## Why we use axplorer instead

axplorer is the clean Python reimplementation of the same core loop. It removes the Julia dependency (our Mixer infrastructure is Python/Rust, not Julia), eliminates file-based IPC overhead, and provides the `DataPoint` ABC as the documented extension point for new domains. There is no B(2,5)-specific code in v1 that cannot be done via axplorer's `DataPoint` interface.
