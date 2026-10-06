---
title: "PatternBoost Generation — experiment type"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: patternboost-generation
author: asetlearning
status: pending
tags: [agent/human, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/trivial-words, topic/hard-instance-generation, project/challenge-gen, status/pending, experiment-type]
---

# PatternBoost Generation (B(2,5))

**Generate words that are trivial in the free B(2,5) by construction**, steered toward target words by a PatternBoost loop ([[charton-2024-patternboost]]). A transformer proposes *factor words* (products of conjugates of relators w⁵). C++ beam local search improves them, a scorer ranks them against target "challenge" words, and the best re-train the model. The factor word is the triviality certificate, so no word-problem solver is needed.

This is the **generation** use of PatternBoost. Do not confuse it with the `#project/b25` PatternBoost line in `Experiments/Group Theory/Burnside Group/B25/PatternBoost/` (maumayma), which uses PatternBoost to *reduce* challenge words.

- Methodology: [[patternboost-generation-methodology]]
- Data and constants: [[patternboost-generation-data]], [[patternboost-generation-constants]]
- Results: [[patternboost-generation-results]]
- Project: [[project-challenge-gen]] · Progress: [[Challenge Generation/_progress]]
