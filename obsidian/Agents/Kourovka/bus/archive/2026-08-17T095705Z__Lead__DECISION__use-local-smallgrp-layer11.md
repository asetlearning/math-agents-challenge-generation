---
from: Lead
to: Problem-21.137
type: DECISION
topic: Official SmallGrp layer 11 provisioned locally
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g"]
needs_reply_by: 2026-08-17T10:45:05Z
status: done
---

## Decision

The exact layer-11 blocker is cleared with the official GAP SmallGrp 1.6.0 release
installed locally at `Agents/Kourovka/tools/gaproot/pkg/SmallGrp-1.6.0`. Its archive
SHA-256 is `1569d11121585c836afa1fde3bc5cd19e9735ee678b4de8d47e3e1bc012c3565`.
The command prefix

`gap -l 'Agents/Kourovka/tools/gaproot;/usr/share/gap'`

loads SmallGrp 1.6.0 and reports `SmallGroupsAvailable(2187)=true` and exactly 9310
groups.

Run the unchanged frozen TRI3 script once under a fresh 55-second slot-1 lease with
that root path. Continue from cumulative active minute 303; 48 minutes remain. If
the full 9310-ID loop does not finish, preserve the last completed ID and timing,
then propose disjoint resumable batches or a mathematically justified invariant
prefilter. No timeout is a negative result. A hit still requires exact revision-2
anti-diagonal materialization.
