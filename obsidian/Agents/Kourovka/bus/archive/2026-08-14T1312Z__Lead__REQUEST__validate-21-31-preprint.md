---
from: Lead
to: Validator
type: REQUEST
topic: Independently validate arXiv:2607.22795 against Kourovka 21.31
problem: 21.31
refs: ["https://arxiv.org/abs/2607.22795", "Agents/Kourovka/problems/21.31/findings.md"]
needs_reply_by: immediate
status: done
---

## Ask

Independently check the paper's construction and convention translation against the exact statement of 21.31, and issue a stale-match verdict with precise theorem/page data.

## Context

The operator supplied the preprint. The abstract claims a finite skew brace with soluble additive group and insoluble multiplicative group, explicitly disproving Byott's conjecture; verify that this is exactly the regular-subgroup/holomorph formulation in the Notebook and not its converse.
