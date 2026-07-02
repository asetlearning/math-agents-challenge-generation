---
title: Compressed KB Results
domain: group-theory
project: b25
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/b25, topic/knuth-bendix, project/b25, results, experiment-type/compressed-kb]
---

# Compressed KB — Results Table

| Run | Date | k | sp | me cap | Rules | m/M-in-LHS | Fire (comp) | Delta | Verdict | Output |
|-----|------|---|----|--------|-------|------------|-------------|-------|---------|--------|
| Unbiased baseline | 2026-06-23 | — | — | 200K | 199,555 | 126 (med LHS=27) | 0 | 0 | NO-GO | [[b25-compressed-kb-first-run-2026-06-23]] |
| Biased (Option a) | 2026-06-23 | 5 | 0.5 | ~194K (90s) | 193,870 | 109 (med LHS=8) | 0 | 0 | NO-GO | [[b25-compressed-kb-option-a-2026-06-23]] |

## Key observation

Biasing (99.7% special) dramatically shortens rule LHS lengths (27→8 chars median), which is the right direction per Part-4 reconciliation. However, the compressed word_7245's m/M symbols are spaced 2–84 raw chars apart (mean 12.3), while the generated rules require alternating patterns with 0–1 raw chars between compressed symbols.

**Fundamental gap**: `mM→ε` (delta=-2, free-group identity) would fire if word_7245 contains CoreA immediately followed by CoreB. This needs to be checked in the raw word.
