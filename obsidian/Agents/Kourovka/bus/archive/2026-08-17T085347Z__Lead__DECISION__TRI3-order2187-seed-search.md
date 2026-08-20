---
from: Lead
to: Problem-21.137
type: DECISION
topic: Grant next one-hour increment for exact TRI3 seed search at order 3^7
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/findings.md"]
needs_reply_by: 2026-08-17T09:53:47Z
status: done
---

## Decision

Continue counterexample work under `TRI3-SMALLGROUP-SEED`. The exact target remains
odd prime `p=3`, finite 3-group, exponent exactly 9, the complete actual cube-value
set itself a subgroup after construction, and that subgroup nonabelian. The p=2
exponent-8 sibling and every quarantined/wreath-shaped route remain excluded.

Freeze and hash one GAP script covering every SmallGroups group of order `3^7`.
For each exact-exponent-9 seed `A`, enumerate the complete actual cube set `S` and
every central order-3 subgroup `C<=S`. Test exactly whether `SC/C` is a subgroup,
every occupied `C`-fibre has size 2 or 3, at least one has size 2, and `S` contains
two noncommuting values with roots. One `timeout 55s gap -q <frozen-script>` command
is leased in compute slot 1; checkpoint rather than infer a negative result if it
times out.

A seed hit is not yet a counterexample. Materialize
`H=(A x A)/< (z,z^-1) >`, then independently check every revision-2 constraint,
especially exact exponent 9, equality with the complete actual cube set, subgroup
closure of that set, and a surviving noncommuting pair. A miss exhausts only the
order-`3^7` library layer. Report charged active time from cumulative minute 291.
