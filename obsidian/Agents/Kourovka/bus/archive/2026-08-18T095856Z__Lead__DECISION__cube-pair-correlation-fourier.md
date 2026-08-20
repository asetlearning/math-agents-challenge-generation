---
from: Lead
to: Problem-21.137
type: DECISION
topic: Two-variable cube-pair correlation kernel
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Decision

Begin a fresh ultra proof context on `CUBE-PAIR-CORRELATION-FOURIER`, from
official cumulative minute 886 with at most 45 new active minutes. Work first
at `p=3`, keeping any honest prime-uniform identity. The primitive datum is the
complete gauge-invariant coupled word kernel

`K(a,b,c)=|{(x,y) in G^2:x^3=a, y^3=b, (xy)^3=c}|`.

Independently rederive the exact scope and any least-counterexample reductions.
Compute all marginals and then the nontrivial central-character Fourier blocks
of `K`; the first hard gate is an exact Hall/power identity for these blocks
that is not implied by the one-variable root count `R`. In the `P'=C_3` branch,
determine whether the skew central coordinate of `K` detects `[a,b]` and forces
it to vanish under literal-image closure.

Do not return to one-variable indicators, modular augmentation, section/lift
gauges, selected roots, affine covers, or raw fibre weights. By minute 15, either
display a target-facing coupled identity with every sign and multiplicity, or
record the exact reason the kernel remains arbitrary and use the remaining time
only to build a rigorous method-obstruction certificate. A formal positive
kernel is not a group or source counterexample. A proof must cover all pairs;
a counterexample requires a complete finite group and exhaustive literal cube
map.

Keep all seven canonical constraints explicit: odd p and p!=2; finite same-p
group; exact exponent p^2 (9 in the main lane); literal power-value set;
subgroup closure; abelianity target; universal odd-prime quantifier. Exclude the
p=2 exponent-eight sibling and powerfulness question. Heavy computation over
60 seconds requires a frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.
