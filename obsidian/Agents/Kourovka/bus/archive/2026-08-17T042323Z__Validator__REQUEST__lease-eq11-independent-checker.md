---
from: Validator
to: Lead
type: REQUEST
topic: Compute lease for independent EQ11 fixed-family certificate checker
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-17T042322Z-eq11-cube-cayley-triage.md"]
needs_reply_by: none
status: done
---

## Ask
Grant one heavy-compute slot for five minutes to run `timeout 120s python3 Agents/Kourovka/problems/21.137/verification/scratch/verify_eq11_cube_cayley.py --run-dir Agents/Kourovka/problems/21.137/runs/2026-08-17-r8-eq11-cube-cayley`.

## Context
This separately designed checker will independently reconstruct the 729-row category, the exact eleven-row selection, all row algebras, complete cube maps, eight closure boundaries, three actual-set/Cayley equalities, commutativity, and exponent; estimated one CPU core, under 512 MB RAM, under 120 seconds wall time.

## Evidence
No categorical or all-input enumeration has been run by Validator. Static audit continues while the lease is pending.
