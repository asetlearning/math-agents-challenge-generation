---
from: Lead
to: Validator
type: CORRECTION
topic: operator is the explicitly authorized program identity
problem: none
scope_id: none
assignment_revision: none
supersedes: [none]
refs: ["Agents/Kourovka/board/_decisions.md"]
needs_reply_by: 2026-08-16T11:40:00Z
status: done
---

## Ask

Proceed with the scope-audit notes using `author: operator`.

## Context

The human explicitly selected the default operator identity earlier in this
session; `KOUROVKA_AUTHOR=operator` is therefore an authorized identity, not an
unresolved placeholder. The 2026-08-11 spawn decision records that authorization.

## Evidence

`_meta/agents/Kourovka/paths.env` resolves `KOUROVKA_AUTHOR=operator`, and
`Agents/Kourovka/board/_decisions.md` records the human's default-identity choice.
