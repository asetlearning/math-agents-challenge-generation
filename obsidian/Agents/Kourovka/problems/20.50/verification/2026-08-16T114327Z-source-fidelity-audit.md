---
title: "Scope audit — Kourovka 20.50"
problem: "20.50"
audit_type: source-fidelity
scope_id: 20.50/four-involution-universal-group
scope_record: Agents/Kourovka/scopes/20.50-four-involution-universal-group.json
assignment_revision: 1
source_pdf_page: 151
source_transcription_checked: yes
audited_record_updated_utc: 2026-08-16T11:48:00Z
result: PASS
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/involutions
  - project/kourovka
  - status/draft
---

# Scope audit — Kourovka 20.50

## Result

**PASS.** The corrected record is complete and faithful to the visually rendered statement on PDF page 151.

It fixes `m=4`, requires four specified generators that are involutions of exact order 2, and—crucially—imposes `(xy)^4=1` for every pair of involutions anywhere in `G_4`, not merely pairs among the four chosen generators. It targets the largest/universal object and asks for its exact order; the known `m=3` value is correctly contextual and out of scope. The exclusions correctly reject generator-pair-only groups and unproved finite quotients.

The initially weaker “order dividing 2” generator wording was corrected by Lead during this preflight; this PASS applies to the updated record identified above. No solution material was reviewed.
