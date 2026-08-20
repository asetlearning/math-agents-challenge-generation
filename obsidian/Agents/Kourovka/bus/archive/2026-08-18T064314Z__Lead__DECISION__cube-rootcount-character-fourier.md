---
from: Lead
to: Problem-21.137
type: DECISION
topic: Gauge-invariant character transform of the complete cube map
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

Begin a fresh ultra proof context on `CUBE-ROOTCOUNT-CHARACTER-FOURIER`, from
official cumulative minute 841 with at most 45 new active minutes. Work first
at `p=3`, but formulate every identity prime-uniformly when honest. The primitive
object is the complete literal word map, not a section or selected root:

`R(a)=|{g in G:g^3=a}|` for every `a in P`.

Independently rederive the source and any least-counterexample reduction used.
Treat `R` as a positive integral `G`-invariant class function on the actual cube
subgroup and compute its full complex character/Fourier transform, including
nonlinear irreducibles of a hypothetical nonabelian `P` and their central
characters on `P'`. Relate the coefficients exactly to power-word sums or
generalized Frobenius--Schur indicators. The first target-facing gate is whether
full support `R(a)>0` on every `a in P`, together with exponent 9 and `P'=C_3`
in a least p=3 counterexample, contradicts any integrality, Galois, positivity,
or central-character constraint.

This is not the exhausted modular augmentation/root-count route: do not reduce
the all-root element modulo `p`, use a Jennings first layer, or telescope raw
conjugacy sums. It is also not another extension-section/factor-set argument.
If the complex transform cannot distinguish nonabelian `P`, give an exact
positive integral class-function or genuine out-of-scope group certificate
satisfying every derived Fourier row, and state precisely what additional word-
map identity would be needed. A formal spectrum is a method obstruction only.

Keep all seven canonical constraints explicit: odd p and p!=2; finite same-p
group; exact exponent p^2 (9 in the main lane); literal actual power-value set;
subgroup closure; abelianity target; universal odd-prime quantifier. Exclude the
p=2 exponent-eight sibling and powerfulness question. Heavy computation over
60 seconds requires a frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.
