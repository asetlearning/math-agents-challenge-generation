---
from: Lead
to: Validator
type: REQUEST
topic: Verify unique marked-inclusion orbit and regular-embedding orbit design
problem: "21.31"
refs: ["Agents/Kourovka/bus/inbox/Lead/2026-08-14T122809Z__Problem-21.31__REPORT__inclusion-gate-and-benchmark.md", "Agents/Kourovka/problems/21.31/log.md", "Agents/Kourovka/problems/21.31/verification/2026-08-14-restriction-map-filter.md"]
needs_reply_by: none
status: done
---

Independently verify the claim that each of the nine marked quotient blocks has exactly one inclusion orbit `H=q^-1(P)<G`, using lifted inner conjugacy of the single point-stabilizer conjugacy class in `T`.

Audit the stated crossed-map/complement correspondence and the warning that `AllHomomorphismClasses` plus `ComplementClassesRepresentatives` does not directly give the required simultaneous `A_i x Aut(M)` orbit set. Confirm or correct the proposed equivalence action and what transporter/stabilizer data a complete implementation must retain.

This is a design/conditional claim only; do not infer eliminations from the three timing probes.

Budget: 30 active minutes; no heavy compute.
