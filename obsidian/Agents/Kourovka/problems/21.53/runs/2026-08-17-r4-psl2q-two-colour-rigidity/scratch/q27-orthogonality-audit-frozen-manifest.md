---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen manifest — `q=27` orthogonality audit

- Purpose: audit the symbolic odd-characteristic reduction at the first simple
  field for which the order-3 relation is empty; this is not family evidence.
- Script:
  `Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/scratch/q27_orthogonality_audit.g`
- Script SHA-256:
  `d5aac8823bbdf8a8fe59218ddc7cfe4d69cc9da5cfbc041f54f641b438dbc774`
- Exact one-shot command:
  `timeout 120s gap -q Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/scratch/q27_orthogonality_audit.g`
- Output target:
  `Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/scratch/q27_orthogonality_audit.out`
- Bound: one CPU, at most 1 GiB RAM, command timeout 120 seconds, one invocation.
- Expected information: compare the exact automorphism order of the commuting
  graph with `|PGammaL(2,27)|=27(27^2-1)*3=58968`.
- Limitation: equality of the two orders at this one field would only stress-test
  the rigidity lemma; it would not prove it. Strict inequality would require
  explicit generator inspection and a full separator before any counterexample
  conclusion.
