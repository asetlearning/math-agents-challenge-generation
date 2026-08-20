---
agent: Problem-20.115-Proof
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
direction: proof
session_id: collaboration:/root/p20115_psl2_field_ext
parent_session_id: collaboration:/root
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-18T11:35:26Z
cycle: 23
budget_hours: 1
active_budget_minutes: 45
active_minutes_used: 482
extensions_granted: 9
safety_stop_utc: 2026-08-18T12:35:26Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: active
truth_likelihood: 0.70
alternate_direction: counterexample
run_dir: Agents/Kourovka/problems/20.115/runs/2026-08-18-r23-psl2-prime-field-extension-clifford
state: running
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
---

## 2026-08-18T11:35:26Z — prime field-extension Clifford reset

The `GL(2,q)` lane charges `00:06:33`, reaching detailed cumulative time
`08:02:07`, and submits a candidate uniform family theorem. Preserve it only as
an unreviewed partial. Restore the third live solver slot on a more target-facing
almost-simple extension: `PSL(2,p^r)` extended by its field automorphism of prime
degree `r`. Derive the full Clifford/Shintani support and exact semilinear element
orders before testing the source predicate; prior rank-one results are not
premises.

## 2026-08-18T11:22:19Z — direct GL(2,q) nonsolvable-family reset

The `SL(2,q)` lane charges `00:11:33`, reaching detailed cumulative time
`07:55:34`, and submits a candidate theorem for the full quasisimple family.
Preserve it only as an unreviewed partial. Restore the third live solver slot on
the independent nonsolvable family `GL(2,q)`, deriving the full ordinary table,
central scalar factors, exact Jordan/tori element orders, and all support
cancellations before auditing the exact source predicate.

## 2026-08-18T11:04:43Z — direct SL(2,q) quasisimple reset

The `PGL(2,q)` lane charges `00:07:17`, reaching detailed cumulative time
`07:44:01`, and submits a candidate theorem for every odd `q>=5`. Preserve it
only as an unreviewed partial. Restore the third live solver slot on the
independent quasisimple central-cover family `SL(2,q)`, deriving all ordinary
characters, central lifts, and exact element orders before auditing the source
predicate. No prior rank-one family theorem is a premise.

## 2026-08-18T10:53:20Z — direct PGL(2,q) almost-simple reset

The small-Ree lane charges `00:21:32`, reaching detailed cumulative time
`07:36:44`, and submits a candidate defect-zero family theorem. Preserve it only
as an unreviewed partial. Restore the third live solver slot on the more
target-facing almost-simple family `PGL(2,q)` for odd prime powers `q>=5`,
deriving its complete ordinary characters and both socle and outer-coset element
types before auditing the exact source predicate. Earlier simple-family results
are not premises.

## 2026-08-18T10:31:11Z — direct small-Ree character-family reset

The Suzuki lane charges `00:11:21`, reaching detailed cumulative time
`07:15:12`, and submits a candidate theorem for every simple `Sz(q)`. Preserve
it only as an unreviewed partial. Restore the third live solver slot on the
independent simple small-Ree family `^2G_2(q)`, using a complete generic
ordinary-character and element-type inventory to test the exact source
predicate. No finite sampling or unreviewed family theorem is a premise.

## 2026-08-18T10:19:07Z — direct Suzuki character-family reset

The direct `PSL(2,q)` lane charges `00:08:57`, reaching detailed cumulative
time `07:03:51`, and submits a candidate theorem for that infinite simple
family. Preserve it only as an unreviewed partial. Restore the third live solver
slot on the independent simple Suzuki family `Sz(q)`, deriving the complete
ordinary character and element-type formulas before auditing the exact source
divisibility. No finite-parameter sampling or reuse of the unreviewed `PSL(2,q)`
result is authorized.

## 2026-08-18T10:03:24Z — direct PSL(2,q) character-family reset

The defect-zero Clifford lane reports a candidate lemma but overruns both its
45-minute active cap and wall safety stop, reaching detailed cumulative time
`06:54:54`; the overrun is disclosed and the candidate remains unreviewed.
Restore the third live solver slot in a fresh independent context on the simple
family `PSL(2,q)`, using its complete ordinary character and element-type
formulas to prove or refute the exact source divisibility. The new lane must
respect its active-time cap.

## 2026-08-18T06:48:50Z — defect-zero Clifford-scalar reset

The component-cycle lane stops at detailed cumulative time `03:44:05` with an
unreviewed exact overlap inequality and one uncovered almost-simple corner.
Restore the third live solver slot in a fresh context on the sharp remaining
theorem: whether an invariant `p`-defect-zero simple-group character can carry
a nontrivial `p`-part in its Clifford extension obstruction. A proof or exact
counterexample must be tied back to the ordinary source transfer.

## 2026-08-18T06:19:56Z — component-cycle trace reset

The minimal-normal lane stops at detailed cumulative time `03:15:05` after
refuting the proposed three-input package and correcting the kernel factor.
Restore the third live solver slot in a fresh context on a nonabelian minimal
normal subgroup `S^t`. Derive the exact tensor-permutation trace cycle by cycle
and test whether its nonzero component values supply the corrected kernel
factor, including scalar-lift deficiency. The universal target remains open.

## 2026-08-18T05:51:21Z — minimal-normal full-lift reset

The standalone projective gate stops at detailed cumulative time `02:47:01`
with an unreviewed exact transfer criterion but no universal bridge. Restore
the third live solver slot in a fresh context on a least counterexample and a
proper minimal normal subgroup. Independently prove or refute the scalar-kernel
size, full-order-lift, and kernel multiplicity divisibility inputs together.
The universal ordinary-character target remains open.

## 2026-08-18T05:30:10Z — projective order-degree proof reset

The 6.A7 audit remains an unreviewed bounded candidate and is not a premise.
Restore the third live solver slot in a fresh proof context on the exact
projective order-degree lemma exposed by the structural route.  Prove or refute
that lemma with a full central-extension and order-lift audit, and state exactly
whether any failure transfers to the ordinary source problem.  Start from
detailed cumulative time `02:26:38`; at most 45 new active minutes are granted.

## 2026-08-18T05:14:03Z — 6.A7 candidate partial handed off

Charge `00:18:37`, reaching detailed cumulative time `02:26:38`. The immutable
40-by-40 audit reports 1,044 exact nonzero cells and zero violations; the
wrapper's header-wrap rejection and posthoc hash-pinned salvage remain explicit.
Route only as an unreviewed bounded candidate and stop this context pending
fresh validation.

## 2026-08-18T05:06:00Z — release rejected 6.A7 v2; format-only v3

The sole v2 invocation exits GAP cleanly but the runner rejects a 1,602-line TSV:
GAP wrapped only the long header after `group_orde\`, while all 1,600 data rows
retain eleven fields. Release slot 2 and treat v2 as `FAILED_RUN_NO_RESULT`.
Authorize only a wide-screen/output-format repair under wholly new v3 paths,
hashes, manifest, and fresh lease.

## 2026-08-18T05:02:17Z — definitive 6.A7 slot 2 lease

Lead matched checker `68d94b82...`, runner `f6c807bb...`, and manifest
`419ae657...`; `bash -n` passes and all four outputs are absent. Grant slot 2
through `05:07:17Z` for exactly one outer-55-second/inner-45-second invocation,
with immediate release and no patch, rerun, or table expansion.

## 2026-08-18T04:47:50Z — exact 6.A7 counterexample reset

The generalized-Fitting lane stops after `00:14:25`, detailed cumulative time
`02:08:01`, with an unreviewed structural partial and a precise projective
order-lift obstruction. Restore the third solver slot in a fresh counterexample
context on exactly the ordinary table of `6.A7`. Verify the table identity and
audit every irreducible-row/class pair against the exact source predicate. A
hit needs a complete explicit certificate; a miss is bounded evidence only.

## 2026-08-18T04:31:37Z — generalized-Fitting refinement

The induction lane stops after `00:26:17`, detailed cumulative time `01:53:36`,
with an unreviewed structural partial and unused budget. Continue the same solver
context for at most 45 active minutes on `FSTAR-QUASIPRIMITIVE-OUTSIDE-NORMALS`.
Re-derive every candidate prerequisite used; seek a primewise inequality or an
exact central almost-simple reduction. Kill on uncontrolled element-order lifts,
mere homogeneity without divisibility, or an unprovided classification theorem.

## 2026-08-18T04:04:12Z — primitive-character proof reset

The bounded SU3(8) lane ends at detailed cumulative time `01:27:19` with no
counterexample in its six-row domain. Start a clean 45-minute proof lane on
`IRREDUCIBLE-INDUCTION-PRIMITIVE-REDUCTION`. It must audit cancellation in the
induced-character formula, prove or refute inheritance of the exact
nonzero-value divisibility implication, and state the strongest legitimate
primitive-character consequence for a minimal counterexample. It may not rely
on the unreviewed SU3(8) result or present the known solvable case as progress on
the universal target.

## 2026-08-18T01:09:36Z — direct six-row source-predicate pivot

Independent validation confirms exactly six degree-189 principal-block rows
fail the proposed sufficient height bridge. That says nothing about their actual
character values. Begin one fresh 25-minute counterexample lane on rows 35--40
of `3.U3(8)`: test the exact source predicate against every class, using exact
cyclotomic nonzero tests and integer divisibility. No other row, table, prime, or
catalogue is authorized. A hit needs a complete source-witness certificate; a
miss is fixed-table bounded evidence only.

## 2026-08-18T01:17:40Z — frozen six-row direct lease

Grant slot 1 for exactly one invocation of the 175-line frozen GAP checker,
SHA-256 `3fe4d2f930749168e2cc87a8945e6810cdd253e2576fdd708badc8a6200a0c02`,
under the exact 45-second timeout command. The output path was absent at grant.
No patch, rerun, extra row, table, or catalogue is authorized; release
immediately after the invocation or failure.

## 2026-08-18T01:20:45Z — release slot 1; bounded direct miss

The sole frozen invocation exited zero in 1.61 seconds, with maximum RSS 141952
KB. Across exactly six rows and 82 classes it audited 492 cells: 198 exact
nonzero values, 294 zeros, and zero failed source divisibilities. Output
SHA-256 `71a042d39e3d732ac4ab98686cb15b449eb3dbc08dc47bb17ab79b98af9f51e5`.
Release slot 1. This is bounded evidence only; the universal target remains open.

## 2026-08-18T00:53:01Z — SU3(8) bridge obstruction routed

The sole leased checker audited all 82 ordinary rows. Seventy-six pass the
proposed sufficient threshold, while principal-block rows 35--40 have degree
189 and height three, giving `27>9`. Charge `00:10:52`, cumulative
`01:14:57`; release slot 2 and route the complete bounded claim to a fresh
Validator. This refutes the attempted generic height bridge, not the source
statement and not Proposition 3.2.

## 2026-08-18T00:33:44Z — next unitary datum

Keep the exact generic-block theorem blocker on record and do not assume it.
Begin one bounded 35-minute proof lane on `SU_3(8)=3.U3(8)` at prime three,
where `v_3(q+1)=2`. The first gate is exact table/block availability and group
identity; any computation needs a frozen checker and Lead lease. A success is
only the fully audited bounded Proposition 3.2 bridge for this datum.

## 2026-08-18T00:43:44Z — frozen checker lease

Grant slot 2 for one exact 45-second invocation of the frozen checker with
SHA-256 `1f0610791c3cd7f7671804123cbc42076ea38091316807ac734b85c185f89d3b`.
No patch, rerun, alternate table, or expanded family is authorized.

## 2026-08-18T00:02:43Z — uniform family gate stops

Charge `00:07:15`, reaching cumulative `01:04:05`. The exact reduction gives
`|P/Z|=3^(2a)`, `exp(P/Z)=3^a`, and the block criterion `h<=d-1-e`, but a uniform
family theorem needs unprovided generic `SU_3(q)` 3-block data. No family claim
was made; the strategy awaits Lead.

## 2026-08-17T23:55:28Z — unitary-family proof lane

The `SU_3(5)` prime-three bridge is independently replicated, but it remains a
bounded family result. Begin a fresh 45-active-minute proof lane on
`A2-UNITARY-CENTRAL-HEIGHT-FAMILY`: test whether the exact defect/height
inequality extends uniformly to `SU_3(q)` with `3 | (q+1)`. The first gate is a
self-contained parameter-level defect and block-height reduction. If the needed
generic block theorem cannot be justified, stop this strategy with the precise
missing statement. No direct-table catalogue expansion and no universal claim.

## 2026-08-17T23:35:00Z — SU3(5) central-height bridge routed

Charge `00:13:34`, reaching cumulative active time `00:56:50`, and return
`00:31:26`.  The repaired once-only gate reports seven ordinary 3-blocks,
explicit defect representatives, quotient exponents `3,3,1,1,1,1,1`, and all
40 central-height thresholds passing.  This is a provisional finite bridge for
`SU_3(5)` at prime three only; the universal source target remains open and all
structural and installed-data claims now go to fresh validation.

Fresh 45-minute counterexample reconnaissance. No mathematics begins before a
recorded current staleness check. Exact ordinary complex values and integer
divisibility are mandatory; no floating point or modular-character substitute.

## 2026-08-17T18:53:29Z — partial-stale finding routed

The mandatory gate found arXiv:2605.04513, which appears to state the exact
conjecture and prove a reduction and many cases while leaving the universal scope
open. Charge five minutes and hold further mathematics for fresh validation.

## 2026-08-17T19:10:16Z — partial-stale verdict accepted

Validator confirms the paper is a substantial exact-subject partial, not a
solution. Route its explicit residual map to a fresh MathExpert for one bounded,
nonduplicative next strategy; the broad CTblLib lane remains withdrawn.

## 2026-08-17T19:27:13Z — direct L4(3) residual screen

MathExpert selects one 20-minute exact table, not a catalogue: verify that the
prime-2 `L4(3)` case is not already covered, certify the table identity, then test
the direct source predicate with exact ordinary character values. A miss is one
bounded partial only.

## 2026-08-17T19:41:00Z — L4(3) zero-hit routed

Charge 5 minutes 26 seconds, cumulative active time `00:10:26`, and preserve
14 minutes 34 seconds. The exact scan reports 495 nonzero pairs among all 841
row/class pairs and no violation. This is now under fresh independent validation;
the universal scope remains open.

## 2026-08-17T19:57:51Z — base table replicated; graph extensions

Validator independently replicates the complete L4(3) scan. Begin one bounded
35-minute lane on exactly `2.L4(3).2_2` and `2.L4(3).2_3`, with structural fusion,
paper-coverage, faithful-character, outer-class, and direct-predicate gates.

## 2026-08-17T20:15:05Z — graph-extension zero-hit routed

Charge seventeen minutes nineteen seconds, cumulative `00:27:45`, and return the
remaining seventeen minutes forty-one seconds. The two exact scans report respectively `580/84/0` and `289/36/0`
tested/nonzero/violating pairs after structural gates. Route this bounded result
to fresh validation; universal scope remains open.

## 2026-08-17T20:47:45Z — graph tables replicated; switch to proof bridge

Validator independently replicates both graph-cover scans and their zero-hit
counts. Keep cumulative time at `00:27:45`. Switch to a fresh ultra proof lane on
the finite `L4(3)` 2-block defect bridge for at most 40 active minutes. The first
eight minutes must establish exact block membership and explicit defect-group
representatives; otherwise stop without reimplementing block algorithms. A failed
sufficient inequality is not a counterexample to the source statement.

## 2026-08-17T21:05:52Z — finite block bridge routed

Charge seven minutes one second, cumulative `00:34:46`, and return `00:32:59`.
The solver reports exact ordinary membership for six 2-blocks, explicit defect-
group exponents `8,4,1,1,1,1`, and all 29 exponent-versus-character-defect
inequalities passing. Route the defect-group identification—especially the use of
Theorem 3.5 for block 2—and the Proposition 3.2 implication to a fresh ultra
Validator. Universal scope remains open.

## 2026-08-17T21:45:18Z — bounded block bridge replicated

Validator's formally leased independent reconstruction passes: six blocks have
defects `7,2,0,0,0,0`, explicit defect exponents are `8,4,1,1,1,1`, and every
one of the 29 character-defect inequalities holds. Theorem 3.5 validates the
cyclic order-four defect group and Proposition 3.2 yields only the stated finite
prime-two bridge. The universal scope remains open. Route the reviewed residual
portfolio to a fresh MathExpert before the next solver increment.

## 2026-08-17T22:05:00Z — direct `3.U3(5)` residual scan

MathExpert ranks three nonduplicative routes and selects `R5-SU35-DIRECT` for at
most 25 active minutes. First verify exact table identity and that the May-2026
paper does not already cover the critical prime-three case. Then freeze one exact
ordinary-table predicate scan and request a compute lease. A hit needs row, degree,
class order, exact value, and failed integer divisibility; a miss is bounded
coverage only. No other table, prime, or catalogue expansion is authorized.

## 2026-08-17T22:18:43Z — exact `3.U3(5)` zero hit routed

The single leased invocation exited zero. Across all 1,600 ordinary character-
row/class cells, 987 exact cyclotomic values are nonzero and none violates
`o(x)chi(1) | |G|`. Charge the complete R5 increment of 7 minutes 28 seconds,
cumulative `00:43:16`, release slot 2, and route this one-table bounded result to
a fresh Validator. The universal scope remains open.
