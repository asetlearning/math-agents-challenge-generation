---
title: "Kourovka 21.137 — PF-JORDAN-CAPACITY proof run"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: PF-JORDAN-CAPACITY
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/draft]
---

# PF-JORDAN-CAPACITY log

## 2026-08-17T12:45:49Z — active work start

- Scope cumulative baseline: 392 active minutes.
- This clean proof run: 0 active minutes used; cap 45 minutes.
- Method hard kill: stop at 30 active minutes if the common-flag analysis gives only dimension/order bounds; absolute stop at 45.
- Control message processed: `2026-08-17T124112Z__Lead__CORRECTION__reactivate-priority-window.md`; it supersedes the preceding park.
- Exclusions observed: no web or solution history, no p=2 or exponent-8 material, no wreath-shaped material, no unreviewed counterexample artifacts, and no heavy computation.

## Source and staleness gate

The configured source PDF was read at page 184 and the rendered page was visually
inspected. Correct active transcription:

> For an odd prime p, if the p-th powers in a finite p-group of exponent p^2 form
> a subgroup, must that subgroup be abelian?

The canonical target makes the implicit quantification and exact-exponent condition
explicit: for every odd prime p and finite same-p group G of exponent exactly p^2,
if the complete actual value set P={g^p:g in G} is a subgroup, prove P abelian.

`source_transcription_checked: yes`

`active_scope_checked: yes`

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

Clause matrix:

| source clause | equivalent formulation | active? | external-result status |
|---|---|---:|---|
| General powerfulness question | actual pth-power values form a powerful subgroup | no | excluded |
| Odd-prime exponent-p^2 clause | actual pth-power values form an abelian subgroup | yes | deferred |
| 2-group exponent-8 clause | actual squares form an abelian subgroup | no | excluded |

Admissibility reconciliation:

| constraint_id | required use in this proof run | result |
|---|---|---|
| 21.137-odd-forall-p-G | argument must be prime-uniform and quantify over all admissible G | pass |
| 21.137-odd-p-not-2 | p is odd | pass |
| 21.137-odd-finite-p-group | G is a finite p-group for that same p | pass |
| 21.137-odd-exponent-p2 | exponent is exactly p^2 | pass |
| 21.137-odd-power-set-definition | P denotes the complete actual value set, not merely G^p | pass |
| 21.137-odd-power-set-subgroup | closure of that value set is the hypothesis to exploit | pass |
| 21.137-odd-P-abelian | desired conclusion is [P,P]=1 | open |

The independent scope audit in the canonical record is `passed`.

## Strategy portfolio (current bounded increment)

1. Catalogue/small-case mode is excluded by the clean, prime-uniform assignment;
   no bounded catalogue result could meet this strategy's success certificate.
2. Structured-construction mode is excluded from this proof increment; any formal
   action system is used only as a failure certificate for the proposed lemma, not
   as a group or counterexample.
3. Theoretical mode: analyze a common invariant flag for the reviewed conditional
   root-action normal form, with N=A-I, N^p=D_a, and N(a)=0. Seek either a proper
   span of all admissible labels or a prime-uniform strict root-capacity deficit.
4. Certificate plan: a successful partial result must be a section-free block or
   flag calculation valid for arbitrary odd p, with every inner-lift and fixed-space
   row explicit. A spanning formal action system or a calculation that yields only
   a lower dimension/order bound kills the method.

## 2026-08-17T12:54:01Z — flag/Jordan calculation

For a nonzero label a, `N^p=D_a` has rank one and image the fixed line C.
Therefore `N^(p+1)=0`, N has exactly one `J_(p+1)` block, and the fixed
noncentral vector a forces at least one additional block. Together with the common
flag this reproduces `F_p<=Z(L)` and `dim L>=p+2`, but supplies no proper label
subspace.

An exact local saturation family was then derived on
`L=V direct-sum <c,z_1,...,z_(p-1)>`. For every label a and every lower-chain
correction w, the automorphism `I+N_(a,w)` has
`N_(a,w)^p=D_a`, fixes a, lowers the same flag, and has the same
`J_(p+1) direct-sum J_1^(dim(V)-1)` profile. There are `p^(p-1)` such ambient
operators per nonzero label, and the label union spans all V. Full details and
limitations are in `findings.md`.

This is deliberately not promoted to a group/action construction: multiplication
closure and extension realization are unproved and the excluded construction class
was not opened. The calculation is sufficient to show that the authorized
flag/rank/per-label observables alone return only the anticipated dimension bound.

## 2026-08-17T12:55:42Z — active work stop and strategy outcome

- Charged this clean run: 15 active minutes (including protocol/scope/source
  inspection, reasoning, and packaging).
- Scope cumulative total: 407 active minutes.
- Outcome: `STRATEGY_EXHAUSTED` for `PF-JORDAN-CAPACITY` only.
- Kill reason: an explicit prime-uniform local saturation family reaches every
  label in the same sharp common-flag/Jordan cell. The remaining possible source
  of a deficit is cross-root multiplication or extension coherence, neither of
  which is present in the named observable. Thus the method met its failure
  certificate before the 30-minute latest kill.
- Active assignment answered: no.
- State: `awaiting_lead`; the scope is not parked or aborted by this solver.

