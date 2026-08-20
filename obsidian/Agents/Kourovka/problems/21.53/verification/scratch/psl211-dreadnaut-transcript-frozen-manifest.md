---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
validator: Validator-21.53-PSL211
freeze_revision: 1
frozen_utc: 2026-08-17T20:56:38Z
supersedes: [none]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Frozen concise-transcript duplicate audit

The first authorized dreadnaut invocations completed in under 0.1 seconds and each
returned group order 1320, but default output printed thousands of generator
cycles. This separately frozen duplicate audit uses the **identical hashed graph
inputs** with dreadnaut option `a` toggled off solely to suppress generator
printing and make the complete decisive stdout auditable in the verification
note. No graph, partition, algorithm, parameter, or target is changed.

## Commands

```bash
timeout 60s dreadnaut -o a < Agents/Kourovka/problems/21.53/verification/scratch/psl211/two_relations.dre
timeout 60s dreadnaut -o a < Agents/Kourovka/problems/21.53/verification/scratch/psl211/full_colours.dre
```

Exactly one invocation of each. Tool: nauty/dreadnaut 2.8.8. Expected below 10
CPU seconds and 256 MiB each; no heavy slot is required. Any timeout ends this
route without retry.

## Inputs unchanged

- `two_relations.dre` SHA-256:
  `ddb8f7a97b5065c99b056b6abc40d13c137c3982b8cb28c1f165802ff8ac9b4b`.
- `full_colours.dre` SHA-256:
  `ea6abf00ed463527105d8bde521f3d7f53579b53c25663504b27d3ee56c3e8d7`.

The leading `'.' is illegal` diagnostic is expected and harmless: the semicolon
on the final vertex line automatically exits dreadnaut graph-entry mode, so the
following explicit period is redundant. Dreadnaut then accepts the frozen
partition (`[fixing partition]`), runs, and exits zero.
