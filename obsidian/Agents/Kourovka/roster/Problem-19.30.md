---
agent: Problem-19.30
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
direction: none
session_id: collaboration:/root/p1930_a6
parent_session_id: collaboration:/root/p1930_psl27
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-17T15:39:24Z
cycle: 3
budget_hours: 1
active_budget_minutes: 34
active_minutes_used: 158
extensions_granted: 0
safety_stop_utc: 2026-08-17T16:34:25Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: parked
truth_likelihood: 0.56
alternate_direction: proof
run_dir: Agents/Kourovka/problems/19.30/runs/2026-08-17-r3-a6-order360
state: parked
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, project/kourovka, status/draft]
---

## 2026-08-17T16:06:14Z — release A6 screen and route bounded partial

Release slot 2. The single frozen GAP stage completed all 162 order-360 rows:
`A6=[360,118]`, target vanishing-order set `[2,3,4,5]`, equality rows `[118]`,
and no nonisomorphic collision. The wrapper's nonzero exit is confined to its
Python parser rejecting one GAP-wrapped header; the raw result is complete at
SHA-256 `6142ece4f7daa7b08d330bce798fceade8e4de45a6b4a27637ff0364d051421e`.
Charge cumulative minute 158 and route only this fixed-A6 claim to a fresh
Validator. The universal Problem 19.30 remains open with 22 minutes preserved.

The counterexample direction stopped at 76 cumulative active minutes. The fresh
proof direction used 30 minutes and packaged a restricted prime-power separator
theorem. Validator's hand audit retained exactly the four-extra-hypothesis subclass,
with corrected `status/conjectured`, `witness_equals_target:false`, and
`active_assignment_answered:no`. MathExpert prescribed one exact proof experiment:
close the five hand-checkable rows specializing the separator to `(A5,5)`. The
The bounded five-row experiment stopped at 126/180. A hostile Validator found no
gap in the fixed order-60 recognition argument, while retaining
`status/conjectured`, `witness_equals_target:false`, and
`active_assignment_answered:no`. MathExpert judged the result meaningful but local
and recommended parking because no non-repetitive exact experiment fits the
remaining 54 minutes. Lead accepts that scheduling recommendation; the universal
scope remains open.

## 2026-08-17T14:43:13Z — second fixed target unpark gate

The human's standing concurrency policy requires a third distinct live problem,
and the recorded park gate asked for a fully specified second target. Fix
`S=PSL(2,7)` of order 168. Use the preserved 54 active minutes on
`PSL27-ORDER168-VANISHING-COLLISION`: freeze a complete script over every
SmallGroups representative of order 168; compute each complete actual
vanishing-element order set from irreducible complex characters; and compare it
with the corresponding set for `S`.

Before any GAP call, freeze the script, exact command, output paths, hash,
coverage count, timeout, CPU/RAM estimate, and request a Lead lease. A nonisomorphic
collision must be materialized and checked row by row; zero collisions give only
a fixed-`PSL(2,7)` bounded partial. Do not infer an infinite family, use web/history,
or reuse the A5 proof by analogy. Report and return to Lead rather than self-park.

## 2026-08-17T14:53:55Z — slot 1 lease for the frozen order-168 screen

Lead independently matches the frozen 210-line GAP script at SHA-256
`5f85824f542f1b7f7b8f9eb23200cead236fc6029b45fc1d821fe9ff246023af`
and the runner at
`47f9052e54901dbedc5476f89436d82e3b245d36b6456319939bb0f3660af55a`.
Grant slot 1 through `2026-08-17T15:13:55Z` for exactly one invocation of the
frozen runner. One process, expected under 512 MiB and conservatively below
1.5 GiB; GAP is capped at 900 seconds plus a 30-second kill grace. No rerun or
change of target/order/coverage is authorized. Release immediately on exit with
the exit code, wall time, complete summary, collision rows, and artifact hashes.

## 2026-08-17T14:59:40Z — release slot 1 and repair coverage constant

The sole leased run exited 2 after about 1.5 seconds. Its guard reports
`NumberSmallGroups(168)=57`, not the frozen 42, and stopped before target
construction or any group row. Slot 1 is released; completed mathematical coverage
is 0/57, so this is an implementation checkpoint only.

Use the sanctioned runtime count to freeze a corrected manifest with expected
coverage 57 and no other conceptual enlargement. Retain the target `PSL(2,7)`,
all exact character/value rows, and the existing target-ID/isomorphism guards.
Record new hashes and request a fresh lease before running. If the next guard
reveals another false frozen constant, stop and return rather than patching live.

## 2026-08-17T15:06:34Z — slot 1 lease for exact-only coverage-57 v3

The direction ledger is 16/54 minutes, so the scope total is now 142/180 with 38
minutes remaining. Lead diffed v3 against the first frozen script: apart from
labels and paths, the only mathematical change is `expectedCoverage: 42 -> 57`.
The 210-line script hash is
`bcbfe6475fda465da72a7cf4fe91d18984b659a735f52f8ded78e2ba15156b7c`;
the runner hash is
`1f2e22c80e078d5974b6d3ec6819817d4a429656b02013af88e5bf98d0407179`.

Grant slot 1 through `2026-08-17T15:26:34Z` for exactly one v3 runner
invocation, one process, conservative 1.5 GiB ceiling, 900-second GAP cap plus
30-second kill grace. No rerun or other change. Release immediately with complete
coverage/collision output and hashes.

## 2026-08-17T15:13:30Z — release v3 and route fixed-target partial

The exact v3 runner completed in about 14.2 seconds and exited 0. It records all
57/57 SmallGroups representatives of order 168, target identifier `[168,42]`,
target vanishing-order set `[2,3,4,7]`, and zero nonisomorphic collisions. Only
the target row has equality. Persistent stderr is empty and the full stdout hash
is `c425a731a710c0d029a7a770cfcf36766ec21338f55f934952790dfd225095f2`.

Release slot 1. Stop research at local 20/54 minutes, hence scope cumulative
146/180 with 34 minutes preserved, and route the fixed-`PSL(2,7)` bounded negative
to a fresh Validator. This is not an infinite-family or universal claim.

## 2026-08-17T15:34:25Z — third fixed target: A6 at order 360

Validator independently replicates all 57 order-168 rows and the zero-collision
conclusion for `PSL(2,7)`, while retaining `active_assignment_answered:no`.
Use the 34 preserved active minutes on one new exact target,
`A6-ORDER360-VANISHING-COLLISION`. Construct `A6` independently, freeze a full
same-order SmallGroups screen and exact vanishing-order-set comparison, and request
a Lead lease before any GAP call. A collision may answer the target negatively;
zero collisions are only a third singleton partial. Kill if exact complete
coverage cannot be frozen within 12 minutes or the run cannot fit the remainder.

## 2026-08-17T15:50:35Z — slot 2 lease for frozen A6 screen

The complete dynamic catalogue coverage, target construction, invariant, collision
criterion, output verifier, hashes, and resource limits were frozen by +8 active
minutes. Lead matches manifest SHA-256
`49eb981620fb1f03ddbaf26d56c9c86edf8755c3b809726d337594388b26157c`
and all three listed file hashes. Grant slot 2 through
`2026-08-17T16:08:35Z` for exactly one invocation of the frozen wrapper: one GAP
process, 2 GiB virtual-address ceiling, 870 CPU-second cap, and 960-second outer
wall timeout. Release immediately on exit; no rerun or live patch.

## 2026-08-17T16:45:30Z — fixed A6 partial replicated; final portfolio review

Validator independently recomputes all 162 order-360 rows through a different
actual-class-representative data flow and finds exact row-by-row agreement:
`A6=[360,118]`, target set `[2,3,4,5]`, equality only at row 118, no collision.
Accept this as a fixed-target replicated partial only. With 22 minutes preserved,
route the accumulated A5, PSL(2,7), A6, and restricted separator evidence to a
fresh MathExpert. It must choose one nonrepetitive structural increment that fits
22 minutes or recommend a reviewed park; no fourth singleton catalogue screen.

## 2026-08-17T16:53:53Z — park after family-level portfolio review

Accept MathExpert's `PARK_RECOMMENDED` with the universal target unanswered and
22 active minutes preserved. The fixed A5, PSL(2,7), and A6 results are reviewed
subcases only; they do not update the universal truth estimate. Neither the
equal-order Lie-type-pair counterexample route nor the defect-zero/chief-factor
proof route currently has the complete ordinary-character input and uniform bridge
needed for a bounded target-facing increment.

Restart only with either a source-grounded complete vanishing-order formula for a
named equal-order nonisomorphic family, including exceptions, or a named simple
family with a uniform vanishing order witness plus a chief-factor exclusion for
every nonsimple same-order group and a discriminator for all simple order twins.
