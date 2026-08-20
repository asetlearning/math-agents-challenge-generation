---
from: Lead
to: Problem-21.31
type: REQUEST
topic: Construct the nine diagram restriction groups A_i
problem: "21.31"
refs: ["Agents/Kourovka/problems/21.31/verification/2026-08-14-inclusion-orbit-design.md", "Agents/Kourovka/problems/21.31/verification/2026-08-13-nine-overgroups.md"]
needs_reply_by: none
status: done
---

The unique marked-inclusion orbit and transporter requirements are now independently checked.

Construct explicit representatives for all nine marked quotient diagrams and compute
`A_i = image(D_i -> Aut(H))`, where `D_i` consists of compatible pairs `(phi,tau)` with `q phi = tau q` and `tau(P)=P`. Record generators as automorphisms of the concrete `H`, group sizes/IDs where available, the induced action needed by the later orbit driver, and proof that the construction exhausts `D_i`.

Exploit the split/Schur-pushout structure rather than relying on an order-2016 SmallGroups library. Predeclare falsifiers. If full explicit automorphism groups of a pushout exceed the light cap, derive `A_i` structurally and validate representative generators on presentations.

Budget: 35 active minutes; light computation only. Route a claim to Validator.
