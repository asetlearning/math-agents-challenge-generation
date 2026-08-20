---
title: "Kourovka 20.21 — post-reduction fidelity, significance, and park assessment"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
direction: counterexample
outcome: PARK_RECOMMENDED
active_assignment_answered: no
novelty: uncertain_not_searched_under_clean_boundary
refs:
  - Agents/Kourovka/scopes/20.21-two-index-twelve-kernels.json
  - Agents/Kourovka/problems/20.21/scratch/2026-08-16-counterexample-direction-partial-result.md
  - Agents/Kourovka/problems/20.21/verification/2026-08-16T164131Z-minimum-witness-reductions.md
  - Agents/Kourovka/problems/20.21/verification/2026-08-16T125904Z-q8-d8-order128-audit.md
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# Post-reduction assessment

## Clean boundary and source status

This advisory assessment uses only the revision-1 scope record, the standalone minimum-witness note, and the two rostered Validator notes named in Lead's request. No root-log, unrostered-helper, web, historical-solution, or computational material was used.

All mathematical content below is either an assessment of those named artifacts or **general mathematical knowledge, unverified**. No literature novelty claim is made.

## Review-circle fields

SCOPE: `20.21/two-index-twelve-kernels`

REVISION: `1`

NOVELTY: `uncertain` — deliberately not searched under the clean-boundary instruction.

FIDELITY: My reading is that the reduction addresses the exact ordered target only as a necessary minimum-witness partial result. It does not answer the existence clause. The strict descent keeps the first quotient cyclic of order 12 and the second quotient isomorphic to (A_4), so it does not silently swap the marked kernels. The Q8/D8 note addresses only its stated order-128 equivariant index-four template.

ACTIVE ASSIGNMENT ANSWERED: `no`.

CLAUSE MATRIX: Source clause `c1` remains unanswered. The artifacts restrict a hypothetical minimum witness to the common-(C_3) branch; they provide neither a target triple nor a nonexistence argument for that surviving branch.

CONSTRAINTS: There is no candidate on which to pass the eight scope rows. Normality, both indices, quotient orientation, and kernel isomorphism are preserved conditionally in the full-product descent; the existential and target-conclusion rows remain open.

GAPS: No bound on |N|; no implication that (N) is a 2-group; no exclusion of nonabelian coordinate kernels beyond the Q8/D8 template; and no reason an abstract isomorphism (K\cong L) carries the selected subgroup (N=K\cap L) to itself.

CONFIDENCE: This assessment would change only if a rostered artifact supplied either a target witness, a general obstruction in the surviving common-(C_3) branch, or explicit compatibility forcing the abstract kernel isomorphism to respect a named subgroup.

## Significance

The minimum-witness reduction is substantial but sharply bounded. As recorded by Validator, it removes the full-product branch from least-order witnesses, forces even intersection and trivial normal odd core at minimum order, and excludes abelian coordinate kernels; the cyclic side also gives (N\not\le Z(L)). These conditions meaningfully focus later work, but they do not make the remaining family finite or supply a characteristic marker for (N).

The Q8/D8 result is a useful exact family exclusion. Its certificate does not extend to other kernels, other orders, or extensions outside the equivariant template. Treating it as evidence against the whole common-(C_3) branch would exceed its stated coverage.

The key obstruction is an **unmarked-intersection mismatch**. If θ is an abstract isomorphism (K\to L), the subgroup relevant inside (K) is (M=\theta^{-1}(N)), with (K/M\cong C_4), while (K/N\cong V_4). General mathematical knowledge, unverified: characteristic, power, Frattini, Fitting, or transfer data attached to (N) cannot be transported through θ without first showing that the chosen subgroup is functorially identified. The hand example in the minimum-witness note exhibits precisely this placement failure.

## Portfolio judgement

Two materially different modes have already produced their bounded value:

1. The structured equivariant-extension mode gave exact Q8/D8 exclusions within a named template.
2. The theoretical minimum-witness/characteristic-section mode gave the reviewed reductions and then met its kill when subgroup placement ceased to be intrinsic.

The scope record also records legacy bounded catalogue work, whose contents were excluded from this clean review. Merely changing the next kernel or order would be catalogue enlargement, not a new direction.

A target-faithful representation change would have to retain the full unmarked datum

\[
(Q,N,M,\varphi),\qquad Q/N\cong V_4,\quad Q/M\cong C_4,\quad \varphi:M\xrightarrow{\sim}N,
\]

together with the order-three compatibility coming from the ambient common-(C_3) branch. None of the admissible artifacts supplies a finite completeness bound or an invariant on this datum. Building that model, proving that it retains the ambient extension constraints, and producing a meaningful success/failure certificate is not credible in 52 active minutes. A quotient-orbit screen that forgets φ would also forget the kernel-isomorphism condition and would not be target-relevant.

## Recommendation

`PARK_RECOMMENDED`.

No 52-minute experiment is prescribed. Reactivation should require a pre-registered, bounded model or lemma that keeps (N), (M=\theta^{-1}(N)), and their isomorphism explicitly marked and also retains the ambient order-three compatibility. Until then, the only available short moves are either repeats of the killed intrinsic-placement route or enlargement of the prior extension catalogue.
