---
agent: Problem-12.15
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
direction: proof
session_id: collaboration:/root/p1215_mixed_fibre
parent_session_id: 01a00a69-0cf7-73f0-8036-eb9ccf22ce10
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-17T08:18:15Z
cycle: 10
budget_hours: 1
active_budget_minutes: 60
active_minutes_used: 333
extensions_granted: 9
safety_stop_utc: 2026-08-17T09:18:15Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: approved
truth_likelihood: 0.72
alternate_direction: counterexample
run_dir: Agents/Kourovka/problems/12.15/runs/2026-08-17-r2-mixed-fibre
state: parked
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, project/kourovka, status/draft]
---

Legacy active-time ledger is preserved. The human's current resume instruction
authorizes one additional one-hour proof-direction cycle beyond the ordinary
extension cap. The clean proof-direction session passed source audit and is live.

## 2026-08-17T08:18:15Z — mixed-fibre proof increment

The human's distinct-problem concurrency instruction authorizes one further
one-hour increment beyond the ordinary cap. Use MathExpert strategy M2 only:
derive the convention-fixed central residual obtained from `[xy,g]`, compare the
four subgroup fibres for `x`, `y`, `xy`, and `xy^{-1}`, and determine whether their
closure kills one mixed commutator pairing. If it merely recovers the known
`{1,z}` residual, report the exact obstruction and await Lead; do not self-park.

## 2026-08-17T08:34:59Z — Lead pivot after M2 exact obstruction

M2 used seven active minutes and reached its stated kill: the plus and inverse
fibres carry the same order-two residual, already absorbed by every `Z`-saturated
defect subgroup. Lead accepts this as a method handoff, not a scope or direction
stop. Use the remaining 53 minutes on M1: classify the square-orbit homomorphism
in R3 for `A=C8`, `C4xC2`, and `C2^3`. Before routing M2 to Validator, correct the
two control-character/notation defects in its findings file.

## 2026-08-17T08:53:47Z — reviewed-dependency audit

The run ledger reached 18 charged minutes, so the scope cumulative ledger is 291
minutes and 42 minutes remain in this increment. M1 exposed a direct conflict:
the reviewed R3 row says `|D_G(c)|=16`, whereas `A<c><=C_H(c)` and `|G:H|=4`
give `|c^G|=|D_G(c)|<=8`. Stop the proof lane and route the exact dependency to
a fresh Validator. Resume only after the audit decides whether R3 is eliminated
or must be reformulated with `D_G(c)=A`.

## 2026-08-17T09:41:50Z — R3 eliminated; resume R1/R2

Fresh Validator reconstruction confirms that the old order-16/nonzero-line row is
sound and, together with the orbit bound at most 8, eliminates R3. Do not replace
`D_G(c)` by `A` and do not continue M1. Use the 42 preserved active minutes on
`R1R2-DEFECT-ORBIT-PACKING`: for every basic commutator in the 3-generator R2 and
4-generator R1 regimes, compute its normal closure, exact fibre subgroup, image in
`H/A`, and `E=G/H` orbit. Determine whether these fibres can jointly generate `H`
under the reviewed action-size rows. Stop with a complete compatible-pattern table
if orbit data alone do not contradict a regime; do not reopen central-lift search.

## 2026-08-17T10:05:00Z — central-layer polarization pivot

The R1/R2 packing pass used 11 active minutes and leaves 31 minutes in this
increment. Lead accepts only the bounded partial restriction that `E` acts
trivially on `V=H/A`; it is not yet promoted and must later receive independent
validation. Continue the proof lane on `R1R2-CENTRAL-LAYER-POLARIZATION`: use
`[H,G]<=A`, the exact fibre identities for `c=[x_i,x_j]`, Hall--Witt, and square
polarization to determine the induced bilinear/quadratic constraints on the
central commutators `[c,x_k]` and on the R2 lift-offset bit. Exhaust R1 and both
R2 centre types. A kill must cover every compatible packing; otherwise freeze
the complete residual central equations and identify the first genuinely free
parameter. Do not reopen HAP or a catalogue/extension search.

## 2026-08-17T10:44:00Z — surviving-table pc consistency pivot

Central-layer polarization used 10 active minutes and leaves 21 minutes in this
increment. It eliminates the all-`B=Z`, `A=C2^2` subtable but leaves R1 `D8/Q8`,
both R2 `B=A` tables, and one cyclic-centre offset. These are candidate partial
restrictions pending independent review.

Continue on `R1R2-PC-CONSISTENCY-AND-FIBRE-WITNESS`. Translate each surviving
table into convention-fixed pc relations for the lifts of a basis of `E`, impose
all collection/associativity critical pairs, and compare the resulting group with
the full normal-closure-fibre hypothesis, not merely the basic commutators. Start
with R1. A useful endpoint is either one explicit inconsistent critical pair or a
materialized consistent order-128 group together with an explicit pair of
nonconjugate elements having the same normal closure. Use the verified bounded
order-128 exclusion only as a diagnostic guarantee that some obstruction exists;
do not cite it in place of the missing hand mechanism and do not start a new
catalogue search.

## 2026-08-17T10:58:00Z — elementary-centre universal witness gate

The pc-consistency pass used 12 active minutes and leaves nine. It submits two
structural eliminations pending review: R1 by innerness of every quotient-trivial
automorphism of `D8/Q8`, and cyclic-centre R2 by the action-square critical pair.
One explicit elementary-centre R2 presentation is consistent but fails the source
hypothesis through elements of orders 2 and 4 with the same normal closure.

On the next available solver slot, use the final nine minutes on
`R2-EA-UNIVERSAL-FIBRE-WITNESS`: express every surviving `A=C2^2` pc table in the
same central-offset coordinates and prove that some pair `r, r h` has equal
normal closure but different order (or otherwise is nonconjugate). If the witness
depends on a parameter, enumerate the finite parameter cases by hand and state
the exact uncovered rows. Do not infer universal coverage from the one materialized
group and do not begin another catalogue search.

## 2026-08-17T11:10:40Z — increment exhausted; bounded package to Validator

The final nine minutes reached cumulative minute 333 and submit a universal
different-order/equal-normal-closure witness for every elementary-centre R2 pc row.
Together with the proposed R1 innerness and cyclic-centre R2 critical-pair
eliminations, the bounded order-128 package now awaits fresh Validator
reconstruction. This is not a larger-order or whole-scope claim.

## 2026-08-17T14:25:48Z — complete order-128 verdict and strategy review

Fresh Validator hand reconstruction passes the trivial quotient-action row, the
R1 and cyclic-centre R2 eliminations, and the universal elementary-centre R2
fibre witness. One submitted normalization was false: changing an outside lift by
an element of `H` cannot alter the residual map. The proof is repaired by first
showing `Theta|ker(psi)` is an isomorphism and changing the quotient complement
vector. Together with the earlier R3 verdict, every reviewed order-128 remainder
is eliminated. This is a bounded partial only; larger orders and the unrestricted
scope remain open.

Pause research at 333 active minutes and request a clean MathExpert comparison of
one larger-order structural lift, one genuinely new normal-closure-fibre invariant,
and parking. Do not extend the order-128 pc tables or treat the bounded theorem as
the source conclusion.

## 2026-08-17T14:34:00Z — park after post-order-128 review

Accept MathExpert's `PARK_RECOMMENDED`. The order-128 exclusion is a substantial
bounded partial, but its small quotient, centre, rank, and action data do not lift
to larger order, and the current residual/square/order-toggle invariants do not
bridge arbitrary `G'' != 1` to a forbidden normal-closure fibre.

Restart only if one of two exact gates is supplied: an order-independent
least-counterexample lemma that controls a parameter growing beyond order 128, or
a concrete conjugacy invariant with a universal bridge from `G'' != 1` to two
nonconjugate elements with equal normal closure. A restart receives one 60-minute
hand audit, killed at 30 minutes without the exact lemma/bridge. The unrestricted
scope remains open.
