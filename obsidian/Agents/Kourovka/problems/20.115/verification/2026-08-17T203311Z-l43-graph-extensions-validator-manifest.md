---
title: "Frozen validator manifest — L4(3) graph-cover extension scan"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
frozen: true
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Frozen validator manifest — L4(3) graph-cover extension scan

- Exact inputs: installed CTblLib `1.3.7` ordinary tables
  `2.L4(3)`, `L4(3)`, `2.L4(3).2_2`, `2.L4(3).2_3`, and their two named
  central quotients; the three quotient outer tables are touched only for the
  naming/nonduplication gate.
- Scan grid: exactly the faithful ordinary rows and independently reconstructed
  outer-coset columns of `2.L4(3).2_2` and `2.L4(3).2_3`; no catalogue query,
  tuning, or extension to another table.
- Predicate: retain exact values unequal to cyclotomic zero and test
  `RemInt(Size(table), chi[1]*OrdersClassRepresentatives(table)[class]) = 0`.
- Script:
  `Agents/Kourovka/problems/20.115/verification/scratch/l43_graph_extensions_validator.g`
- Frozen script SHA-256:
  `817b5fdeca74eb1a2f9b9dff4d475fb308de39131fc57a6e0c6be780e69ce94a`
- Exact command:
  `timeout 30s gap -q -b Agents/Kourovka/problems/20.115/verification/scratch/l43_graph_extensions_validator.g > Agents/Kourovka/problems/20.115/verification/scratch/l43_graph_extensions_validator.out`
- Wall cap: 30 seconds. Estimated use: under 10 CPU seconds and under 300 MB RAM.
  This is a bounded light job, not a heavy job under the common protocol's
  `>60 s CPU or >1 GB RAM` definition, so no compute-slot lease is required.
- Required process result: exit zero, every structural assertion passes, exactly
  869 pair records are serialized, exactly 120 are exact nonzero values, and no
  retained nonzero pair has nonzero remainder.
- Hard stop: any timeout, assertion failure, unexpected table identifier/version,
  extra/missing pair, or nonzero remainder ends the run without widening scope.
