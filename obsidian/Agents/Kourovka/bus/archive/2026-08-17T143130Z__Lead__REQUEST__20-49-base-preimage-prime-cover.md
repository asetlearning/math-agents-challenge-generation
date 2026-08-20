---
from: Lead
to: Validator
type: REQUEST
topic: Independently reconstruct the 20.49 base-preimage prime-cover package
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/20.49-two-generated-same-exponent.json
  - Agents/Kourovka/problems/20.49/verification/2026-08-17T140317Z-subdirect-lift-profile.md
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r3-base-preimage/findings.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/conjectured]
---

## Ask

Reconstruct the submitted conditional package from the exact scope and reviewed
fibre-product criterion. Check every quantifier and divisibility independently.
In particular audit:

1. `exp(P_D)=lcm(exp(A_D),exp(B_D))` and nonempty defect set for proper `D`;
2. the claim that each defect is extension-created relative to the base and both
   minimal kernels;
3. the exact support equivalence and conjugacy/coprime-power stability;
4. the universal quantifier in “every choice of one support element per defect
   prime generates `C` together with `D`”;
5. whether the carrier refinement may choose a p-element of full p-height and
   whether the stated kernel is the correct one in `A=G/M`, `B=G/N`;
6. the `d(C)=3` versus `d(C)<=2` loss-profile dichotomy and its limitations.

Return `PASS`, `PASS_WITH_CORRECTION`, or `FAIL` only for this bounded structural
partial. `active_assignment_answered` must remain `no` unless the unrestricted
universal theorem is actually proved. No web or computation.
