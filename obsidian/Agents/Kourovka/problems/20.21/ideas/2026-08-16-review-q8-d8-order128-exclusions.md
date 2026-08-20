---
title: "MathExpert review: Q8/D8 exclusions at order 128 for 20.21"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/extensions
  - project/kourovka
  - status/conjectured
problem: 20.21
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
active_assignment_answered: no
---

# Boundary and sourcing

This is a clean-context review only of Validator's
`2026-08-16T125904Z-q8-d8-order128-audit.md`. Everything beyond that audit is
**General knowledge, unverified** or fresh hand assessment. No web, historical
solution material, ordinary findings, or catalogue output was consulted.

# Assessment of the exclusions

I found no additional conceptual gap in the two exclusions at their stated
scope. For an order-\(128\) auxiliary group in the equivariant template, the
common extension kernel \(N\) has order \(8\). The audit treats \(N\cong Q_8\)
and \(N\cong D_8\), the two nonabelian groups of that order. Its outer-action
lists and restricted factor-set lists are exhaustive for those two cases, and
the center invariant separates the coordinate preimages in every listed case.

The useful aggregate conclusion is therefore exactly

\[
  |P|=128\text{ and the equivariant template succeeds}
  \quad\Longrightarrow\quad
  N\text{ is abelian}.
\]

The surviving order-eight possibilities are

\[
  C_8,\qquad C_4\times C_2,\qquad C_2^3.
\]

These are common extension kernels, not a claim that the two isomorphic
coordinate kernels must themselves be abelian. In particular, an abelian
\(N\) may still support nonabelian coordinate preimages.

# Direction judgment

These bounded negative families do **not** justify replacing the construction
program by a global theoretical-nonexistence program.

1. They concern one auxiliary order, two kernel isomorphism types, and the
   sufficient equivariant template. The audit expressly leaves witnesses
   outside that template and larger auxiliary groups untouched.
2. The separating invariant is a center calculation for very specific
   restricted extensions. It is not stable under adding a larger kernel layer:
   higher extensions can change both the size and exponent of the centers.
3. At the same order, three abelian kernels remain. Thus the negative evidence
   has removed a branch of the construction tree, not the tree itself.

A theoretical pivot is justified only in the narrower sense of replacing more
blind order-\(128\) catalogue search by a complete hand/cohomological treatment
of the three abelian kernels. If those also fail, the resulting theorem would
still be “no order-\(128\) witness in this template,” not nonexistence for
Problem 20.21.

# Qualitatively different next approach

Classify the abelian-kernel cases as equivariant module extensions rather than
as another group catalogue.

- For \(N=C_8\) and \(N=C_4\times C_2\),
  \(\operatorname{Aut}(N)\) has no element of order \(3\). Hence the order-three
  lift acts trivially on \(N\). Equivariance then forces any action homomorphism
  from the cyclically permuted \(V_4\) to \(\operatorname{Aut}(N)\) to be
  trivial: its values on all three nonzero elements would be equal, while the
  homomorphism law forces that common value to be the identity. The remaining
  data reduce to the commuting \(C_4\)-action and the \(C_3\)-fixed part of the
  extension class.
- For \(N=C_2^3\), order-three automorphisms do exist. This is a genuinely
  different linear problem: first classify the compatible
  \(C_4\times A_4\)-module structures on the three-dimensional
  \(\mathbf F_2\)-space, and only then compare the restrictions of the
  corresponding extension classes to \(V_4\) and \(C_4\).

In both branches the success certificate is one compatible global extension
class whose two coordinate restrictions give isomorphic groups and which
admits the prescribed order-three lift. The kill certificate is exhaustion of
these three abelian module-and-cohomology cases. Center, exponent, Frattini
quotient, and derived subgroup are suitable early restriction invariants, but
none alone should be assumed complete.

# Scope conclusion

Retain the Q8/D8 result as a strong bounded `PARTIAL_RESULT`. Continue the
construction direction through the uncovered abelian kernels. Do not promote
the current evidence to theoretical nonexistence beyond order \(128\) or
beyond the equivariant template.
