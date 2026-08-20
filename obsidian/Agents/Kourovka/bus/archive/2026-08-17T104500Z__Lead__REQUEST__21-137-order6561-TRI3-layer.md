---
from: Lead
to: Validator
type: REQUEST
topic: Fresh audit of the order-6561 TRI3 and direct-counterexample exclusion
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/findings.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187_quotient_base_filter.g
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187_quotient_base_filter.out
---

Freshly reconstruct the bounded claim without importing the solver's reasoning.
Audit: (1) the quotient-by-every-central-C3 argument forcing cyclic centre for an
order-6561 exponent-9 group with noncommuting cubes; (2) why TRI3 strengthens the
centre to exactly C3; (3) why projective cube closure modulo C3 suffices in the
reviewed p=3 class-at-most-five integral identity, forcing seed class at least 6;
(4) the exact quotient-base class/exponent/subgroup filter; and (5) the frozen
script's coverage, output hash, and empty 26-row result by an independent rerun or
independent implementation under a Lead lease if heavy compute is required.

Separate the TRI3-seed conclusion from the claimed direct-counterexample order
floor, and audit the class drop through a cyclic centre carefully. Preserve the
exact odd-prime scope: this is only a p=3 bounded exclusion, never a full answer,
and no p=2/exponent-8 material is admissible. Send a protocol VERDICT only after
all hand and computational dependencies are checked.
