---
from: Lead
to: Problem-21.137-Proof
type: DECISION
topic: Use returned 24 minutes on minimal-weight power-image proof route
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md
  - Agents/Kourovka/problems/21.137/scratch/nott-n2-n15-edge/projection-obstruction.md
needs_reply_by: 2026-08-17T16:58:05Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/word-maps, project/kourovka, status/draft]
---

Start `GRAD-PIMAGE-MINIMAL-WEIGHT` with exactly 24 active minutes, taking the
priority ledger from 501 to at most 525. The only live scope has odd `p>2`, finite
same-`p` group, exponent exactly `p^2`, literal value set
`P={g^p:g in G}` itself a subgroup, and target `P` abelian. The exponent-8
two-group clause, `p=2`, generated-power-subgroup substitutes, and wrong-exponent
objects are excluded.

Assume a hypothetical counterexample. Record first that closure gives `P=G^p`
and exponent `p^2` gives `exp(P)|p`. Use the reviewed class-at-most-`p+1`
theorem, then choose the least lower-central weight at which `[P,P]` survives and
pass to the corresponding central quotient. Translate the existence, for every
two power values, of a root of their product into the leading Hall/associated-
graded identity. By +8 minutes either prove the exact leading-term vanishing
lemma or isolate the precise coefficient/term that invalidates it. If it works,
push central-quotient induction toward the full theorem. If it fails, use all
remaining time to derive the strongest exact obstruction datum or repair inside
this universal proof direction. Do not self-park early, revisit a bounded carrier,
or perform unleased computation. A full proof or admissible counterexample
candidate stops immediately for the review circle; otherwise report at +24.
