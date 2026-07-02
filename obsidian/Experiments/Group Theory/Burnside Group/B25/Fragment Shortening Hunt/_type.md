---
title: Fragment Shortening Hunt on B(2,5)
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: fragment-shortening-hunt
status: complete
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/beam-search, project/b25, status/complete, experiment-type]
---

# Experiment Type — Fragment Shortening Hunt on B(2,5)

## What this technique is

The Fragment Shortening Hunt is a systematic, finite enumeration method for finding length reductions in the CoreA/CoreB segment representation of B(2,5) benchmark words.

### Background: CoreA/CoreB structure

Words in the 119-word benchmark corpus (comm_12_9, comm_16_2, etc.) can be decomposed into a sequence of segments:

```
w = prefix? · CoreX · frag₁ · CoreY · frag₂ · CoreZ · ... · suffix?
```

where:
- **CoreA** = `ABabAbabABaBAbabABABabAbaBABaBAbabb` (35 chars)
- **CoreB** = `BBABabAbabABaBAbabaBABabAbaBABaBAba` (35 chars)

The "connector fragments" are the strings appearing between consecutive core occurrences. The "junction" for fragment F with orientation X→Y is the full string `CoreX · F · CoreY`.

### The technique

Given the corpus decomposition:
1. **Enumerate** all distinct connector fragments from all 119 benchmark words.
2. **Build junction words** of the form `CoreX · F · CoreY` for each (fragment, orientation) pair.
3. **Test** each junction for length reduction under:
   - A large shortlex KB rule bank (leftmost reduction, longest-LHS first)
   - The `braid_reduce` beam search (forward rules + braid shortenings)
4. **Verify** any reduction using GAP full word-equality (not abelianization — B(2,5) is non-abelian and abelianization is blind on the commutator subgroup).
5. **Promote** confirmed reductions to "seed rules" (LHS→RHS patterns applicable to all words in the corpus).

### What "success" means

A junction reduction `CoreX · F · CoreY → shorter` constitutes a rewriting rule that shortens any benchmark word containing that fragment in that orientation context. Aggregate effect: total chars saved across the 119-word corpus.

### Null results are upper bounds only

A junction that does not reduce under bank B and beam budget T is reported as "no shortening found at bank B, T seconds". This is **not** an irreducibility claim — it is an upper bound on what methods B and T can find. Irreducibility would require proof that no shorter representative of the junction exists in B(2,5), which requires a completed KB system or other theoretical tool.

### Relationship to other B25 experiment types

- **Reduce Core**: provides the 119-word corpus and the word_7245 current best; Fragment Shortening Hunt targets the connectors within those words.
- **KBMag / Biased KB Agents**: the rule banks used here come from those experiments (the 499,864-rule shortlex bank). Fragment Shortening Hunt is a consumer of those banks.
- **Bridge Cancellation Line**: predecessor. Bridge Cancellation tested whether `CoreA · X · CoreB → X` for specific "bridge" connector patterns X in word_7245. Fragment Shortening Hunt generalizes: all 318 connectors from all 119 words, all orientation types, Y≠X allowed.

## Relevant files

- **Rules (durable)**: `experiments/burnside/b25/fragment_seed_rules/b25_seed_rules_2026-06-25.json` and `.kbprog`
- **Run output**: `runs/b25/fragment_seed_rules/20260625_235828/` (per-word table, provenance)
- **Beam binary**: `experiments/burnside/burnside_bidirectional/target/release/braid_reduce`
- **Corpus**: `experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/best_words/` (119 .txt files)

## Literature

- [[havas-wall-wamsley-1974]] — B(2,5) presentation and structure; benchmark words comm_i_j are generators of the lower central series derived from this presentation.
- [[havas-robertson]] — KB completion framework; the shortlex rule bank (499,864 rules) used here is a KB partial completion in shortlex ordering.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes; any reduction of a benchmark word toward identity is progress on problem 11.48.
