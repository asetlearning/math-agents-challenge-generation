---
from: Lead
to: Problem-21.31
type: REQUEST
topic: Build a complete finite parameterization of compatible N-extension/action lifts
problem: "21.31"
refs: ["Agents/Kourovka/problems/21.31/verification/2026-08-13-nine-overgroups.md", "Agents/Kourovka/problems/21.31/findings.md", "Agents/Kourovka/problems/21.31/log.md"]
needs_reply_by: none
status: done
---

Resume from the verified nine `(G,K)` classes and five `M=K x (C7:C3)` types. Do not enumerate arbitrary order-2016 groups.

First derive a proved-complete parameterization of extensions `1 -> M -> N -> V -> 1`, `V=C2^3`, that admit a lift of the fixed faithful `T=GL(3,2)` quotient action and are compatible with one of the nine `G` classes. Separate outer actions, extension/cohomology classes, and crossed maps. State the exact equivalence relation and predeclare a falsifier.

Aim for the cheapest next certificate: a rigorous obstruction eliminating a radical/overgroup class, or a small exact list of action-lift classes. Use only light probes until completeness and cost are established; request a lease before any heavy enumeration. Route claims to Validator.

Budget: 60 active minutes.

## Blocked because

The five verified order-252 types are the multiplicative subgroups \(H=K\times(C_7:C_3)\), not the additive kernels \(M\). Byott gives only a regular embedding \(H\hookrightarrow\operatorname{Hol}(M)\), which does not imply \(M\cong H\). A complete parameterization must either range over all eligible order-252 \(M\) and regular \((H,M)\) data, or cite/prove an additional theorem reducing \(M\) to those five types.
