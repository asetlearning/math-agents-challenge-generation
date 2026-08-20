---
title: "Scope audit — Kourovka 21.137"
problem: "21.137"
audit_type: source-fidelity
scope_ids:
  - 21.137/odd-prime-exponent-p2
  - 21.137/two-group-exponent-8
scope_records:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/scopes/21.137-two-group-exponent-8.json
assignment_revisions:
  odd-prime-exponent-p2: 2
  two-group-exponent-8: 1
source_pdf_page: 184
source_transcription_checked: yes
audited_two_group_record_updated_utc: 2026-08-16T11:50:00Z
result: PASS
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/power-subgroups
  - project/kourovka
  - status/draft
---

# Scope audit — Kourovka 21.137

## Results by atomic scope

- **PASS — `21.137/odd-prime-exponent-p2`.** It correctly requires a finite `p`-group for the same prime `p`, `p != 2`, exponent exactly `p^2`, the set of actual `p`-th powers (not merely the subgroup they generate) to be a subgroup, and that very subgroup to be abelian. It explicitly marks the general powerfulness question and the exponent-8 2-group clause out of scope, and its exclusions rule out `p=2` and wrong exponent.
- **PASS — `21.137/two-group-exponent-8`.** It correctly requires a finite 2-group, exponent exactly 8, the set of actual squares (not merely the subgroup they generate) to be a subgroup, and that very subgroup to be abelian. It marks both the odd-prime clause and the opening broader powerfulness question out of scope and names both exclusions.

## Preflight correction

The exponent-8 record initially omitted the opening powerfulness clause from its clause inventory and exclusions. Lead corrected both omissions during this preflight; this PASS applies to the updated record identified above.

Both atomic records now pass. No solution material was reviewed.
