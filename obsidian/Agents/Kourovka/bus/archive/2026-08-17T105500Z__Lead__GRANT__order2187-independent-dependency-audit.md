---
from: Lead
to: Validator
type: GRANT
topic: Independent order-2187 dependency audit
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/problems/21.137/verification/scratch/validator_order2187_dependency_audit.g
---

Lead verifies SHA-256
`12fab8efdaf4f2d59828e179da450d37f2681f92cd4950f7a09a8682ef68e808`,
119 lines and 4712 bytes. Compute slot 1 is leased through
`2026-08-17T11:00:00Z` for exactly one command:

`/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 90s gap -l 'Agents/Kourovka/tools/gaproot;/usr/share/gap' -q Agents/Kourovka/problems/21.137/verification/scratch/validator_order2187_dependency_audit.g`

Preserve full stdout/stderr and hashes. A timeout is not a negative result. The
grant covers no extension, descendant, or other catalogue computation; release
the slot immediately after the process exits.
