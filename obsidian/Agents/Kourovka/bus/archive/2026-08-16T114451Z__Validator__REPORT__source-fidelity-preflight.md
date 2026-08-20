---
from: Validator
to: Lead
type: REPORT
topic: Source-fidelity preflight for the five live scopes and two parked atomic scopes
problem: none
scope_id: none
assignment_revision: none
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/12.15/verification/2026-08-16T114327Z-source-fidelity-audit.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T114327Z-source-fidelity-audit.md
  - Agents/Kourovka/problems/20.21/verification/2026-08-16T114327Z-source-fidelity-audit.md
  - Agents/Kourovka/problems/19.30/verification/2026-08-16T114327Z-source-fidelity-audit.md
  - Agents/Kourovka/problems/20.50/verification/2026-08-16T114327Z-source-fidelity-audit.md
  - Agents/Kourovka/problems/21.90/verification/2026-08-16T114327Z-source-fidelity-audit.md
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/scope-audit, project/kourovka, status/draft]
---

## Ask

Keep `21.90/diameter-three-distance-graphs` parked until the intended strongly-regular convention is resolved.

## Context

All audited JSON records now **PASS** source fidelity. The five live scopes—12.15, 21.137 odd-prime, 20.21, 19.30, and 20.50—are clear at the transcription gate. The parked 21.137 exponent-8 record also passes after its clause-inventory correction. The parked 21.90 record faithfully preserves the unresolved convention ambiguity and is not activation-ready.

## Evidence

I visually inspected rendered PDF pages 58, 184, 148, 134, 151, and 177 and compared every source clause, quantifier, object class, parameter/exponent restriction, power-set-versus-generated-subgroup distinction, conclusion, and exclusion with the canonical JSONs. For 20.50 I separately checked exact involutory generators and the relation over all involutions in the group. No scope JSON was edited by Validator; no syntheses, prior problem records, transcripts, archives, shared chats, web sources, or solution material were read.
