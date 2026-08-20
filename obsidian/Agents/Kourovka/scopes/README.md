---
title: "Kourovka canonical scope records"
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, project/kourovka, status/reference]
---

# Canonical scope records

This directory is the target-and-revision authority for Kourovka work. The board is
the human-readable scheduling view; it must agree with these records.

Create one JSON file per atomic target from
`_meta/agents/Kourovka/templates/scope-template.json`. The filename must equal
`<scope_key>.json`. Split multi-part statements, parameter regimes, and equivalent
questions whenever one part could be answered without answering another.

The `constraints` list is a hard admissibility contract. Transcribe every
quantifier, object class, parameter restriction, exclusion, exponent/order
condition, hypothesis, and required conclusion from the rendered PDF. Mark source
conditions `role: admissibility` and desired conclusions
`role: target_conclusion`. A proposed witness with even one failed or unknown
admissibility row is an `OUT_OF_SCOPE_EXAMPLE`, not a counterexample; a proof must
establish, and a counterexample must violate, the applicable conclusion rows.

Every routed claim also has a machine-readable
`Agents/Kourovka/problems/<id>/claim-checks/<claim-id>.json`, created from
`_meta/agents/Kourovka/templates/claim-check-template.json`. The checker proves only
that no canonical row was omitted and no self-declared failure was marked ready;
Lead and Validator must still inspect the mathematical evidence independently.

Legacy board and roster entries are migrated when a scope is next selected,
rescoped, or resumed. Do not invent current mathematical status during migration.

Check consistency from the vault root:

```bash
python3 _meta/scripts/kourovka-state-check.py
python3 _meta/scripts/kourovka-state-check.py --render
```

The first command exits nonzero on contradictions. Missing scope fields in legacy
rosters are warnings during migration; new or revised assignments must be clean.
