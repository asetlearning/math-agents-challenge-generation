---
title: "Scope audit — Kourovka 20.49"
problem: "20.49"
audit_type: source-fidelity
scope_id: 20.49/two-generated-same-exponent
scope_record: Agents/Kourovka/scopes/20.49-two-generated-same-exponent.json
assignment_revision: 1
source_pdf_page: 151
source_transcription_checked: yes
audited_record_updated_utc: 2026-08-17T11:35:23Z
result: PASS
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - project/kourovka
  - status/draft
---

# Scope audit — Kourovka 20.49

## Result

**PASS.** Revision 1 is complete and faithful to the visually rendered statement
on PDF page 151.

The source asks whether every finite group contains a 2-generated subgroup with
the same exponent. It then records two known results: the answer is affirmative
for soluble groups, and every finite group has a 3-generated subgroup with the
same exponent. The JSON correctly keeps the universal 2-generated question in
scope and both known results as out-of-scope context; neither comment weakens the
universal target.

## Clause and convention audit

| Source item | Canonical treatment | Audit |
|---|---|---|
| “any finite group” | Universal quantification over every finite group `G` | exact |
| “contains a … subgroup” | Some `H <= G`; no properness condition, so `H=G` is allowed | exact |
| “2-generated” | There are `x,y in G` with `H=<x,y>`; this is generation by at most two elements, allowing a redundant or identity generator | exact |
| “with the same exponent” | `exp(H)=exp(G)`, where group exponent is the least common multiple of all element orders | exact |
| soluble-groups comment | Recorded as known context and excluded from the active universal scope | exact |
| 3-generated-subgroup comment | Recorded as a weaker known theorem and excluded from the active 2-generated scope | exact |

There is no source requirement that `H` be proper, that either group be
nontrivial, or that `G` lie in a prime-dependent or soluble class. “Exponent” is
the group exponent, not the maximum element order. The six canonical constraint
rows explicitly cover the universal quantifier, finiteness of `G`, the subgroup
relation, generation by at most two elements, exact exponent equality, and the
universal existence conclusion. Their roles and required flags are complete.

The four exclusions are also sound. The soluble restriction and the
three-generator theorem are source-supplied nearby statements, not the target;
maximum element order is not a substitute for group exponent; and a bounded
catalogue pass is correctly identified as insufficient for the universal
conclusion. The last exclusion is methodological rather than a separate source
clause, but it does not alter the source meaning.

This is a source-fidelity audit only. No mathematical claim, literature status,
history, or candidate solution was reviewed.
