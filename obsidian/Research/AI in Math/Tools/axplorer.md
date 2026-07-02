---
title: "axplorer — PatternBoost Reference Implementation"
url: "https://github.com/AxiomMath/axplorer"
domain: ai
author: maumayma
stars: 169
language: Python
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/patternboost
  - topic/computational-search-group-theory
  - topic/mathematical-discovery
  - topic/algorithm-portfolio
  - type/reference
  - status/draft
related:
  - "[[charton-2024-patternboost]]"
  - "[[patternboost-v1-lineage]]"
---

# axplorer — PatternBoost Reference Implementation

> **Integration target for B(2,5)/Mixer PatternBoost loop.** axplorer is the clean Python implementation of the PatternBoost paradigm ([[charton-2024-patternboost]]): alternating local search + global transformer training. To wire B(2,5) word reduction into this loop, implement `BurnsideDataPoint(DataPoint)`. See § Extension point for B(2,5).

## Repository

GitHub: AxiomMath/axplorer — 169 stars, pure Python, DataPoint ABC architecture, resumable training, GPU support.

## What axplorer does

axplorer implements the [[charton-2024-patternboost]] training loop in pure Python:

1. **Local search phase**: each `DataPoint` runs `local_search()` to improve itself (domain-specific; for graph problems: delete edges violating constraints, then greedy re-add)
2. **Scoring**: `calc_score()` returns a float — how good is this construction?
3. **Filtering**: keep top N% of scored constructions (typically 10–25%, per PatternBoost paper ablations)
4. **Transformer training**: fine-tune the transformer on the filtered pool
5. **Inference**: sample 100k–500k new constructions from the trained transformer
6. **Reseeding**: validated samples become seeds for the next local search round
7. **Repeat** until performance plateaus

## Core Abstraction: DataPoint ABC

Every domain implements this abstract base class:

```python
class DataPoint(ABC):
    def calc_score(self) -> float:
        """How good is this construction? Higher = better."""
        ...

    def local_search(self) -> DataPoint:
        """One step of local search from this point. Returns improved DataPoint."""
        ...

    def tokenize(self) -> list[int]:
        """Tokenize this DataPoint for transformer input."""
        ...
```

To apply axplorer to a new domain: implement these three methods. The training loop, checkpoint management, and transformer architecture are handled by axplorer.

## Tokenizers

- **`SparseTokenizerSequenceKTokens` (k=1)**: one symbol = one token, no BPE merging. Correct for domains where each element in the sequence is independently meaningful. **This is the right tokenizer for B(2,5) Burnside words** — each generator letter (a, b, A, B) maps to a distinct integer token.
- Additional domain-specific tokenizers are available in the repo for graphs and point sets. Check axplorer source for the full list.

## Configuration

Pass a DataPoint class + config dict or YAML to `axplorer/run.py` (or equivalent entry point). Key hyperparameters:
- Top-K filtering percentage
- Number of transformer inference samples per generation
- Transformer architecture: 2–6 layers, 4–8 attention heads, 16–256 embedding dimensions (from PatternBoost paper ablations)
- Checkpoint path (resumable training)

## Training and Checkpointing

- Checkpoints saved after each training round
- Training paused and resumed from any checkpoint
- GPU via standard PyTorch CUDA

## Extension Point for B(2,5) / Mixer

Implement `BurnsideDataPoint(DataPoint)`:

```python
class BurnsideDataPoint(DataPoint):
    def __init__(self, word: str):
        self.word = word  # Burnside group word, e.g. "aAbB..."

    def calc_score(self) -> float:
        # Score = reduction ratio or KB convergence speed
        # See integration options A and B below

    def local_search(self) -> BurnsideDataPoint:
        # One local search step, e.g., apply a KB rule or one beam search step

    def tokenize(self) -> list[int]:
        # SparseTokenizerSequenceKTokens k=1
        # Each letter in {a, b, A, B} -> one integer token
        ALPHABET_MAP = {'a': 0, 'b': 1, 'A': 2, 'B': 3}
        return [ALPHABET_MAP[c] for c in self.word]
```

### Integration Option A — subprocess wrap (lightweight)

`calc_score()` calls `kbprog` as a subprocess and returns exit metrics (convergence time, rule count at termination).

- Pros: minimal code; no changes to Mixer protocol
- Cons: subprocess overhead on every eval (seconds per word); loop latency is high

### Integration Option B — Mixer JSON-lines protocol (recommended)

`local_search()` and `calc_score()` communicate via JSON-lines protocol with a running Mixer agent. The Mixer agent runs KB search; axplorer scores the results and reseeds.

- Pros: respects the existing Mixer transport layer; enables live rule injection; full cascade feedback available
- Cons: requires Developer effort to wire the JSON-lines protocol; Mixer agent must be running throughout the training loop

**Lead/Developer decision gate required.** Option B is the correct long-term architecture. Option A is a usable starting point to validate the loop before the protocol integration work is scheduled.

## Open Risks

> ⚠️ **RISK 1 — Sequence length**: Raw B(2,5) words can be hundreds of characters. Typical transformer `max_len` (often 512 tokens) may truncate long words silently. **Mitigation**: limit training corpus to words below a length threshold; or implement chunking. Ablation needed to find the cutoff.

> ⚠️ **RISK 2 — Score signal sparsity**: KB reduction costs seconds per word. PatternBoost generates 100k–500k candidates per round — scoring all of them is infeasible at that cost. **Mitigation**: graduated scoring (fast proxy score for all, expensive exact score for top-K only); or batching multiple kbprog calls; or running local search for fewer steps per candidate before scoring.

> ⚠️ **RISK 3 — Unpinned PyTorch**: `environment.yml` lists `torch` without a version pin. A PyTorch update could silently break training or produce silent numerical differences. **Mitigation**: pin to a known-good version before first use (e.g., `torch==2.3.0`). Check axplorer repo for any pinning recommendation before doing so.

## Relationship to v1

The predecessor repo (zawagner22/transformers_math_experiments, 39 stars — [[patternboost-v1-lineage]]) used Julia for local search and Python for the transformer, communicating via file-based IPC. axplorer replaced Julia with Python, IPC with in-process calls, BPE with domain-specific tokenizers, and added resumable training and GPU support. The core loop is the same; axplorer is the production-quality implementation.
