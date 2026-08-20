---
title: "Scope audit — Kourovka 21.90"
problem: "21.90"
audit_type: source-fidelity
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 1
source_pdf_page: 177
source_transcription_checked: yes
result: PASS
activation_blocker: unresolved-strongly-regular-convention
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/draft
---

# Scope audit — Kourovka 21.90

## Result

**PASS for source fidelity; the convention blocker remains.** The record faithfully reproduces the visually rendered statement on PDF page 177: the definition of each distance graph on the same vertex set, adjacency exactly at distance `i`, existence of a Q-polynomial distance-regular graph of diameter exactly 3, and strong regularity of both `Gamma_2` and `Gamma_3`.

The source does not define “strongly regular.” The rendered page alone does not decide whether a nontrivial/connected convention is intended or whether imprimitive cases such as matchings or disjoint cliques are allowed. The JSON correctly preserves that ambiguity and is correctly parked. This PASS must not be treated as resolving the convention or authorizing activation.

No convention was silently selected and no solution material was reviewed.
