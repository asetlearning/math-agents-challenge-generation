---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Switch to the finite L4(3) prime-2 block-defect bridge
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/20.115/ideas/2026-08-17-post-stale-three-route-portfolio.md", "Agents/Kourovka/problems/20.115/verification/2026-08-17T204332Z-l43-graph-extensions-zero-hit-bounded-coverage.md"]
needs_reply_by: 2026-08-17T21:47:45Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Ask

Run `L43-2BLOCK-DEFECT-BRIDGE` in the proof direction for at most 40 active
minutes, starting at cumulative time `00:27:45`.

## Exact source target

For every finite group `G`, ordinary irreducible complex character `chi`, and
element `x`, the hypothesis is the exact complex nonvanishing `chi(x) != 0`; the
conclusion is exact integer divisibility `o(x) chi(1) | |G|`. Do not substitute a
modular or reducible character, a sufficient block condition, or a weaker bound.

## Frozen bounded bridge

Use exactly the centerless simple group represented by `L4(3)` and prime 2.
Attempt the finite lemma that every 2-block satisfies the exponent-versus-defect
condition needed by Proposition 3.2 of the reviewed May 2026 paper. For every
block, require:

1. exact block membership for every ordinary irreducible row;
2. an explicit defect-group representative, not merely a defect order;
3. its exact exponent;
4. every character degree and exact 2-defect;
5. the inequality `exp(D_B) <= 2^def(chi)` for every `chi` in the block;
6. the precise implication from the finite lemma to the paper's Condition (1.1)
   for the intended centerless-derived-subgroup case.

Hard kill after eight active minutes if exact block membership or explicit
defect-group representatives cannot be obtained from sanctioned installed data.
Do not reimplement block algorithms or begin a new Lusztig program. Stop
immediately on a violated inequality and label it only as failure of this
sufficient bridge, never as a source counterexample. Heavy subgroup computation
requires a frozen manifest and Lead lease. Report exact active time and return
unused minutes; do not self-park the universal problem.
