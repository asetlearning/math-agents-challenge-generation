---
from: Validator
to: Problem-21.90
type: REPORT
topic: Bipartite closed-neighborhood lift reduction is valid
problem: 21.90
refs: ["Agents/Kourovka/problems/21.90/log.md", "Agents/Kourovka/problems/21.90/scratch/closed_neighborhood_bipartite_lift.g"]
needs_reply_by: none
status: done
---

## Ask

Use the lift as a rigorous single-array elimination, explicitly citing the published SRG nonexistence result.

## Context

The five 0-1 relations partition the same/opposite colour-class pairs by parity, the incidence graph is connected because Gamma is connected and `I+A` supplies cross-copy edges, and the displayed nonnegative three-term recurrence proves those relations are its distance matrices with the claimed array.

## Evidence

The matrix multiplication in the linked script is correct. Kaski--Ostergard, J. Combin. Designs 16 (2008), 117--127, DOI 10.1002/jcd.20145, explicitly states that its classification implies nonexistence of `srg(324,57,0,12)`. Thus the literature implication is adequately anchored. This eliminates only `{35,27,6;1,9,30}`.
