---
title: "PatternBoost: Constructions in Mathematics with a Little Help from AI"
authors:
  - "François Charton"
  - "Jordan S. Ellenberg"
  - "Adam Zsolt Wagner"
  - "Geordie Williamson"
year: 2024
venue: "arXiv preprint (math.CO)"
url: "https://arxiv.org/abs/2411.00566"
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
cites:
  - "[[romera-paredes-2023-funsearch]]"
  - "[[2506.13131]]"
cited_by: []
related:
  - "[[Research/AI in Math/Tools/axplorer]]"
quality_notes: "arXiv:2411.00566, November 2024. math.CO. Content fetched via WebFetch from arXiv HTML. Authors: Charton (META FAIR), Ellenberg (U. Wisconsin), Wagner (Tel Aviv), Williamson (U. Sydney). Notably: the paper explicitly does not compare against FunSearch or AlphaEvolve — the authors emphasize accessibility over raw compute. The 30-year conjecture disproved is the Graham conjecture on spanning subgraphs of hypercubes."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/funsearch
  - topic/patternboost
  - topic/mathematical-discovery
  - topic/extremal-combinatorics
  - topic/algorithm-portfolio
  - paper
  - status/draft
status: draft
---

# PatternBoost: Constructions in Mathematics with a Little Help from AI

> **This IS the method behind the first Mixer/B(2,5) computational-discovery experiment.** The local-search + learned-global-reseeding loop is the structural analog of the Mixer's KB rule-injection strategy. Read alongside [[romera-paredes-2023-funsearch]] (FunSearch) and [[2506.13131]] (AlphaEvolve) as one paradigm family.

## Abstract

"We introduce PatternBoost, a flexible method for finding interesting constructions in mathematics. Our algorithm alternates between two phases. In the first 'local' phase, a classical search algorithm is used to produce many desirable constructions. In the second 'global' phase, a transformer neural network is trained on the best such constructions. Samples from the trained transformer are then used as seeds for the first phase, and the process is repeated."

## TL;DR

PatternBoost: classical local search generates constructions → top constructions train a small transformer → transformer samples reseed local search → repeat. Applied to extremal combinatorics problems. Key result: disproves a 30-year-old conjecture of Graham on spanning subgraphs of hypercubes. Also finds new constructions for triangle-free graphs, Sperner systems, and isosceles-triangle-free point sets.

## The PatternBoost Method

### Two-Phase Architecture

**Phase 1 — Local search:** A classical search algorithm (problem-specific) generates many mathematical constructions. For graph problems: "down and up" — repeatedly delete edges violating constraints (e.g., triangles), then greedily add edges while preserving validity.

**Phase 2 — Global transformer:**
- Takes as input: the top K constructions from Phase 1 (top 10–25%)
- Tokenization: adjacency matrices flattened row-by-row with delimiters; Byte-Pair Encoding (BPE) reduces sequences to ~72–200 tokens; integer encoding for point sets
- Architecture: Makemore (GPT-2 style decoder-only), typically 2–6 layers, 4–8 attention heads, 16–256 embedding dimensions
- Training: fine-tuned on top constructions each generation
- Output: 100,000–500,000 candidate sequences per iteration, decoded and validated before feeding to Phase 1

**Iteration:** Generated samples seed the next Phase 1 local search. Invalid constructions (35–90% depending on problem) are discarded by the validator. The loop repeats until performance plateaus.

**Key insight:** The transformer learns the GLOBAL PATTERN of what good constructions look like (statistical structure across many examples), while local search handles the LOCAL REFINEMENT (exploiting structure within a single construction). This division of labor is the core contribution.

### Comparison with FunSearch and AlphaEvolve

PatternBoost vs. [[romera-paredes-2023-funsearch]] (FunSearch):
- **Same family:** both alternate ML model + evaluator-filtered search; both make genuine mathematical discoveries
- **Key difference:** FunSearch's LLM proposes *code* (programs encoding strategies); PatternBoost's transformer proposes *instances* (specific constructions). FunSearch discovers generalizable algorithms; PatternBoost discovers specific solutions.
- **Scale:** FunSearch uses large LLMs (requiring industry compute); PatternBoost uses small transformers (runs on a single GPU in hours). PatternBoost is intentionally more accessible.

PatternBoost vs. [[2506.13131]] (AlphaEvolve):
- AlphaEvolve extends FunSearch to 67+ problems using Gemini; PatternBoost covers a narrower but distinct problem set in extremal combinatorics
- Both demonstrate the local-global alternation paradigm; neither is clearly dominant

**The paper does not directly benchmark against FunSearch or AlphaEvolve.** The authors note: "we do not require extensive expertise in machine learning or access to industry-level computing power."

## Results: Problems Solved

### The 30-Year-Old Conjecture (Graham conjecture on hypercube spanning subgraphs)

**Conjecture (Graham, ~1994):** The minimum number of edges in a spanning subgraph of the d-dimensional hypercube Q_d that maintains diameter d equals 2^d + C(d, ⌊d/2⌋) - 2.

**PatternBoost result:** For d = 6, PatternBoost discovered a spanning subgraph of Q_6 with diameter 6 and **81 edges** — the conjectured minimum was 82. This is the first progress on this problem in 30 years and disproves Graham's conjecture.

**How:** PatternBoost ran local search (greedy edge deletion while preserving diameter d) and its transformer learned the pattern of near-optimal subgraphs. The transformer reseeded local search into previously unexplored regions of the construction space.

### Other Extremal Combinatorics Problems

| Problem | PatternBoost result |
|---|---|
| C₄-free (no 4-cycle) graphs on n=33 vertices | Found 96-edge graph (optimal); scaled to n=55 |
| 312-avoiding permanents (25×25 matrices) | Achieved 5,101,230 |
| Isosceles triangles in [64]² | 110-point construction (no 3 isosceles) |
| Saturated 8-Sperner systems | Size-108 family; improved ε bound to 0.04085 |
| Cross-Sperner families | Beat prior bounds for (n,k)=(7,3) and others |
| Double box covers of {0,1,2}⁵ | 41 boxes |

**For C₄-free graphs:** pure local search peaked at 81 edges; PatternBoost reached 96 (the known optimum). The transformer learned that "good C₄-free graphs look like X" and reseeded the search near the optimal region.

### Verification

Every construction is verified formally (checked against the mathematical definition) by the evaluator. Invalid outputs are discarded. All claimed results are verifiable independently from the stated constructions.

## Technical Details

**Tokenization strategy:** Adjacency matrices are flattened to sequences; BPE is applied. Choice of tokenization is important — the paper notes that poor tokenization limits the transformer's ability to learn patterns.

**Failure modes:** PatternBoost struggles when constraints propagate globally (e.g., global cycle constraints in C₄-free graphs need careful tokenization). "There are problems where the pattern of the best constructions seems complicated for humans — PatternBoost can be useful there."

**When it works best:** (1) rapid mechanical evaluation exists, (2) global structure emerges from local constraints, (3) tokenization captures relevant patterns.

## Assumptions

- A fast formal evaluator must exist (PatternBoost cannot be applied to problems without one).
- Local search must be able to improve starting from random seeds.
- The transformer can learn useful global patterns from a few thousand examples.

## Relevance to Mixer/B(2,5)

**THIS IS THE DIRECT METHODOLOGICAL MODEL** for the Mixer/B(2,5) first computational-discovery experiment. The Mixer's KB rule-injection strategy follows the PatternBoost architecture:
- **Local phase** = KB completion run (KBMAG/kbprog) starting from a seeded rule bank
- **Global phase** = ML model (or overlap-score heuristic) learns from successful rule banks, reseeds the next run
- **Evaluator** = KB convergence time / rule count at termination
- **Mathematical discovery** = new B(2,5) rewrite rule sequences not previously known

The v10d Mixer experiment (b80_at20k, overlap-scored injection of 80 rules at 20k RPO rules → 13.7s cascade) is structurally a single-iteration PatternBoost step: local KB run + global scoring + reinjection. A full PatternBoost loop would iterate: run → score rules → train transformer → resample → reinject → run → repeat.

The SAT-encoding methodology in [[Research/Group theory/Open problems/Group rings/gardam-semidecidable-2021]] (Gardam's unit-conjecture search) is a complementary technique in the same "algorithmic search for algebraic objects" paradigm.

## Open Questions Surfaced

- Can PatternBoost discover new results in group theory (e.g., new short relators for B(2,5), new KB rule orderings)?
- Can the transformer component be replaced by a fine-tuned code LLM to get FunSearch-style interpretable programs?
- What is the right tokenization for KB rewrite rules?

## Related material in vault

- Cites: [[romera-paredes-2023-funsearch]] (FunSearch — same paradigm family), [[2506.13131]] (AlphaEvolve — same paradigm family)
- Related AI-for-math: [[1701.06972]] (Loos et al. 2017 — deep-network heuristics steering a classical prover's search; earlier instance of the learned-guidance-over-classical-search pattern PatternBoost iterates)
- Gardam bridge: [[Research/Group theory/Open problems/Group rings/gardam-semidecidable-2021]] (SAT-based search = complementary computational-search paradigm)
- MOC: [[_synthesis-ml-for-math]]
- [[2306.15626]] — LeanDojo (retrieval-augmented theorem proving): a contrasting AI-for-math paradigm — formal proof search vs PatternBoost's construction search
