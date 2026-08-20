---
title: "Kourovka 21.90 revision 3 — asymmetric fission run log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/draft
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
direction: proof
run_dir: Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission
---

# Run log

## 2026-08-17T08:18:15Z — work start

Cumulative active time: 0 minutes. Assignment: use at most 60 active minutes to freeze the exact asymmetric-fission constraints for the live array `{39,25,10;1,5,30}`. No heavy-compute lease is held.

Canonical convention: both distance constituents must be nontrivial strongly regular graphs in the source-operational connected, noncomplete, exactly-three-adjacency-eigenvalues sense. The disconnected `H(3,2)` constituents are excluded.

Only the reviewed polar-fission result is inherited, at its exact scope: the explicit standard 300-vertex nonsquare-type perpendicularity constituent admits no fission found in the completed exhaustive search over vertex-transitive subgroups of its full automorphism group. This says nothing about asymmetric fissions or nonisomorphic `srg(300,65,10,15)` constituents.

## Source and staleness gate

- Visually inspected rendered source PDF page 177. Corrected transcription: for a diameter-`d` graph `Gamma`, `Gamma_i` has the same vertices and joins `u,w` iff `d_Gamma(u,w)=i`; the question asks whether a Q-polynomial distance-regular `Gamma` of diameter 3 exists for which `Gamma_2` and `Gamma_3` are strongly regular.
- `source_transcription_checked: yes`.
- Canonical scope audit: revision 3, Validator audit passed; every active constraint was reconciled with the rendered source. The source itself does not define “strongly regular”; revision 3's source-paper operational convention controls this run.
- The configured source is Notebook No. 21 (2026), where 21.90 is unstarred and has no editor/later comment in its displayed entry. The older corpus has no issue-21 JSONL record, so no corpus flags exist to inspect; the source page and canonical record are controlling.
- Fresh searches: exact-number searches for `"Kourovka 21.90"` and `"Problem 21.90" Kourovka`; proposer/key-term search for Makhnev plus Q-polynomial distance-regular graphs of diameter 3 with strongly regular distance graphs; and an arXiv-focused key-term search. No paper claiming to answer the 2026 existence question was found. The 2019 Belousov–Makhnev–Nirova paper classifies feasible parameter families and does not itself construct a graph for the active 300-vertex array.
- `active_scope_checked: yes`; no stale match found.

Clause matrix:

| source clause | active equivalent | in active scope? | literature status |
|---|---|---:|---|
| Definition of `Gamma_i` | adjacency matrices `A_i` are exact distance relations on the same vertex set | yes | definitional |
| Existence of diameter-3 Q-polynomial distance-regular `Gamma` with strongly regular `Gamma_2,Gamma_3` | construct one graph passing all revision-3 rows | yes | no complete answer found |

Admissibility checklist: existence of one `Gamma`; diameter exactly 3; Q-polynomial distance-regularity; exact distance-graph definition; connected noncomplete three-eigenvalue strong regularity of both `Gamma_2` and `Gamma_3`; and the existence conclusion. This run treats the selected array and fixed standard `Gamma_3` constituent as a bounded construction subproblem, not as the whole existential target.

## Strategy portfolio

1. **Delsarte-coclique fission (rank 1).** Rewrite the unknown adjacency relation as a symmetric incidence matrix of maximum cocliques of the fixed polar constituent. This should replace raw quadratic edge variables by finite row domains and exact pairwise compatibility.
2. **Direct binary matrix CSP (rank 2).** Keep one binary variable for every unordered nonedge of the constituent and impose the two Bose–Mesner identities. This is exact but has 35,100 variables before propagation.
3. **Spectral/theoretical obstruction (rank 3).** Use the `-10` eigenspace and the forced spectrum of the fission matrix to derive parity, determinant, or integral-lattice obstructions. No immediate obstruction is visible because the array is formally self-dual and Krein-feasible.
4. **Alternate constituent (deferred).** Search nonisomorphic `srg(300,65,10,15)` constituents only after the fixed-constituent formulation is frozen. A failure for the polar constituent does not cover this mode.

Certificate plan: a positive output must give the explicit 300-by-300 binary matrix, verify both exact matrix identities independently, reconstruct all four distance relations, check distances and intersection numbers, exhibit `P=Q` in the Q-polynomial ordering, and check both constituent spectra/common-neighbour parameters. A negative output must certify exhaustive coverage of the stated finite domain; timeout or one orbit family is not evidence of nonexistence.

## 2026-08-17T08:34:00Z — exact reduction obtained

Cumulative active time: 16 minutes. Derived the exact fission and maximum-coclique formulations recorded in `constraints.md`. The key representation change is `M=I+A_1`: every row support must be a Hoffman-bound 40-coclique in `B=A_3`, and the global problem becomes a 300-partite pairwise-compatibility CSP on those cocliques. This is an exact equivalence for the fixed constituent, not merely a necessary condition.

## 2026-08-17T08:38:00Z — cheap exact gate completed

Cumulative active time: 20 minutes. After freezing the formulation and script, ran the exact GAP/GRAPE gate three times under a 55-second process cap; every run exited normally in under five seconds, so no heavy-compute lease was required. The final transcript is saved at `scratch/enumerate_coclique_orbits.out`.

The reconstructed graph has 300 vertices, degree 65, common-neighbour values 10 and 15, automorphism-group order 9,360,000, and one vertex orbit. Exact search found no 40-coclique; `MaximumClique` returned size 30 with an explicit witness; a separate size-40 search after replacing the graph group by the trivial group also returned empty.

Consequence: every proposed fission would force a closed `A_1`-neighbourhood of size 40 that is a coclique in `A_3`, whereas this fixed standard polar `A_3` has coclique number 30 computationally. Thus the standard constituent admits no fission at all, subject to independent validation. This strictly strengthens the inherited vertex-transitive-only exclusion but still has exactly one-constituent scope.

## 2026-08-17T08:40:32Z — strategy exhausted; work stop

Cumulative active time: 22 minutes. Outcome: `PARTIAL_RESULT` for the fixed standard polar constituent. No active-scope solution claim is made; `active_assignment_answered: no`. The asymmetric-fission method over this constituent has met its kill criterion because its necessary row domain is empty. Representation-changing pivot occurred (edge fission to maximum-coclique incidence).

Two qualitatively different alternatives remain for Lead to choose:

1. Search for or construct a nonisomorphic `srg(300,65,10,15)` constituent and rerun the 40-coclique gate.
2. Leave this array and derive the same local-coclique obstruction for another feasible formally self-dual array/constituent.

Recommended next experiment if Lead continues this direction: identify whether any nonisomorphic `srg(300,65,10,15)` with a 40-coclique is known or constructible; kill that route if no explicit constituent source can be named within one bounded hour. State: `awaiting_lead`; no charged research continues.

## 2026-08-17T08:45:51Z — CONTINUE, integral/design gate

Cumulative active time: 22 minutes. Lead directed the remaining allocation to constituent-independent integral, `p`-rank, Smith-form, and design obstructions for the symmetric incidence system. Resumed without a heavy lease and assumed only an arbitrary `srg(300,65,10,15)` constituent satisfying the frozen equations.

## 2026-08-17T08:48:04Z — constituent-independent contradiction; work stop

Cumulative active time: 24 minutes. The first integral gate already contradicts the array. Since `a_1=39-25-1=13`, the local graph at any vertex would be 13-regular on 39 vertices, with odd degree sum 507. Equivalently, the frozen `M^2` equation makes the off-diagonal `M`-relation on each 39-point open row support 13-regular. The proof is in `integral-obstruction.md`.

Outcome: candidate `PARTIAL_RESULT` eliminating the array, not the full active existential scope. The method has met its kill criterion before `p`-rank or Smith-form analysis; those downstream gates are moot for an inconsistent integral system. State: `awaiting_lead`; no charged research continues.

## 2026-08-17T08:53:47Z — CONTINUE, source-family feasibility rescreen

Cumulative active time: 24 minutes. Lead directed a corrected bounded rescreen of the non-Taylor source parameterization, with every layer-handshake parity condition added to the earlier sphere, spectral, scheme, Krein, Q-order, and absolute-bound gates.

## 2026-08-17T09:15:00Z — rescreen completed; work stop

Cumulative active time: 45 minutes. Reconstructed the master `(t,a_3,c_2)` equation and wrote the explicit substitutions from all four Type-I/II source families. The exact corrected run in the inherited finite box produced 482 final arithmetic survivors, with smallest-by-order array `{19,12,5;1,4,15}` on 96 vertices. Froze the exact `srg(96,19,2,4)` Hoffman-20-coclique fission observable in `source-family-rescreen.md`. This is not a catalogue completeness claim and does not answer the active existential target. State: `awaiting_lead`.

## 2026-08-17T09:41:50Z — CONTINUE, known-exclusion reconciliation

Cumulative active time: 45 minutes. Lead directed the final 15 minutes to sort the 482 rows by order, reconcile every maintained exclusion by provenance, and freeze the first genuinely unexcluded row without beginning its construction test.

## 2026-08-17T09:56:00Z — reconciliation completed; work stop

Cumulative active time: 59 minutes. The old order-300 target was not the smallest unresolved row: loop order had hidden `{19,6,8;1,1,12}` on 210 vertices, while the new handshake gate removes the order-300 row. After accounting separately for validated in-house arguments and literature-only citations, the order-210 row is first not already excluded. Its two constituent parameter sets and its exact Hoffman-20-coclique fission observable are frozen in `known-exclusion-reconciliation.md`; the observable computation was not started. The finite box is not claimed complete. State: `awaiting_lead`.

## 2026-08-17T09:51:32Z — CONTINUE, SRG210 constituent gate

Lead authorized a new bounded gate: spend at most 15 active minutes identifying and exactly checking one explicit `srg(210,76,26,28)` before any Hoffman-20-coclique work.

## 2026-08-17T10:03:00Z — constituent source gap; work stop

Charged active time in this continuation: about 11 minutes. Brouwer's current SRG table marks `(210,76,26,28)` unknown, and the closest primary source treats the equivalent `2-(210,77,28)` design as putative and supplies only conditional orbit structures. No local adjacency data or constructor exists. The exact equivalence `D=I+B`, `D^2=49I+28J` is recorded in `srg210-constituent-gate.md`, along with the still-frozen coclique/matrix gate. No coclique computation was begun and no lease was requested. Outcome: `BLOCKER` for this implementation route, not a nonexistence result; state `awaiting_lead`.

## 2026-08-17T10:05:00Z — CONTINUE, constituent-independent integral gate

Lead charged 15 minutes to the stopped constituent gate and directed the remaining allocation to the abstract `D,M` identities, beginning with the two rational spectral-multiplicity branches and then integral/design obstructions.

## 2026-08-17T10:40:00Z — local clique-partition contradiction; work stop

The trace equations give exactly two preliminary `M`-spectrum branches; the mixed identity eliminates the branch containing eigenvalue 13 and forces `20^1,14^19,0^114,(-1)^76`. More decisively, each 19-vertex local `A_1` graph is 12-regular and any two nonadjacent local vertices have no common local neighbour. It must therefore be a disjoint union of `K_13`, impossible on 19 vertices. Full matrix proof: `srg210-integral-obstruction.md`. This covers every hypothetical distance-3 constituent and eliminates the array, pending Validator review. No modular/SAT/catalogue computation was needed. Outcome: candidate `PARTIAL_RESULT`; state `awaiting_lead`.

## 2026-08-17T10:50:00Z — CONTINUE, order-540 local-integral gate

Lead accepted the independently validated order-210 exclusion at exactly its
single-array scope, set the centralized cumulative ledger to 179 active
minutes, granted the first one-hour extension, and directed the next bounded
gate to `{77,60,13;1,12,65}`. Resumed without a heavy-compute lease and with
literature/catalogue search forbidden.

## 2026-08-17T11:11:00Z — cheap gates pass; work stop

Charged active time in this continuation: about 21 minutes; centralized
cumulative time about 200 minutes. Derived spheres `(1,77,385,77)`, all
induced relation degrees and handshakes, the two constituent SRG parameter
sets, the exact `M=I+A_1` identities, and the forced 78-coclique incidence
system. All parity, rational-spectrum, elementary modular, and local-component
gates pass. In particular, a nonedge of the 16-regular 77-vertex local graph
has eleven common-neighbour slots after removing the base vertex, so the
zero-codegree clique-partition proof used at order 210 does not transfer.

The exact frozen next observable is maximum-78-coclique enumeration followed
by the symmetric 540-partite intersection-compatibility CSP for one explicit
`srg(540,77,4,12)`. It was not run because no explicit constituent was
supplied and no heavy lease exists. Full details and a cheap reproducibility
script are in `order540-local-integral-gate.md` and
`scratch/order540_local_integral_gate.g`. Outcome: `CHECKPOINT`, not an
existence or nonexistence claim; `active_assignment_answered: no`; state
`awaiting_lead`.

## 2026-08-17T11:17:52Z — CONTINUE, installed rank-3 orbital gate

Centralized cumulative active time: 200 minutes, with exactly 40 minutes left
in extension 1. Lead authorized only the installed degree-540 primitive-group
layer, with a 12-active-minute availability/subdegree kill. No web or broad
catalogue search was permitted; any heavy follow-up required a frozen command,
hash, and lease.

## 2026-08-17T11:27:18Z — no length-77 suborbit; strategy stop

Charged active time: about 10 minutes; centralized cumulative time 210 minutes,
leaving 30 minutes in extension 1. GAP 4.12.1 / PrimGrp 3.4.4 contains ten
primitive groups of degree 540. Indices 1--8 all have subdegrees
`[1,224,252,63]`; indices 9 and 10 are the natural `A_540` and `S_540`, hence
have subdegrees `[1,539]`. Thus the installed layer contains no length-77
suborbit, self-paired or otherwise. No orbital graph or coclique computation
was reached.

The exact bounded frontier, commands, hashes, outputs, and limitations are in
`order540-rank3-orbital-gate.md` and
`scratch/order540_primitive_orbital_gate.out`. Outcome:
`STRATEGY_EXHAUSTED` only for the installed primitive-orbital route;
`active_assignment_answered: no`; state `awaiting_lead`.

## 2026-08-17T11:29:04Z — compute-protocol correction; evidence quarantined

Lead corrected the compute interpretation: every GAP call is heavy regardless
of duration. All preceding degree-540 GAP output and the apparent primitive-
orbital negative frontier are quarantined as non-evidence. Froze, but did not
execute, one deterministic all-ten-group replay script. Active research stopped
at the five-minute correction cap; centralized cumulative ledger at most 215,
with at least 25 minutes left in extension 1, pending a compute lease.

## 2026-08-17T11:39:43Z — slot 2 leased replay

Verified the frozen script hash and ran the exact authorized command once.
It exited 0 and covered all ten installed degree-540 primitive groups. Indices
1--8 have subdegrees `[1,63,224,252]`; indices 9--10 are natural `A_540,S_540`
with `[1,539]`. Thus the leased replay finds no length-77 suborbit. No orbital
graph, coclique, or CSP follow-on was run. Slot 2 released immediately on exit.
Evidence: `order540-primitive-allten-leased-replay.md`. State
`awaiting_lead`; `active_assignment_answered: no`.

## 2026-08-17T11:44:30Z — CONTINUE, source-family handshake congruences

Resumed without compute and with catalogue/web work forbidden. The assigned
representation is the exact primitive non-Taylor master array and the four
algebraically consistent Type-I/II substitutions from the prior rescreen.

## 2026-08-17T11:53:34Z — infinite Type-(IIii) parity exclusion; checkpoint

The original three layer handshakes, and in fact all nine handshakes obtained
by restricting every distance relation to every nonzero sphere, are equivalent
to the single master congruence `t*a` even. Families (Ii), (Iii), and every
integral square-condition solution of (IIi) satisfy it automatically. In
(IIii) it is exactly `x*w` even, so all tuples with `x,w` odd are excluded.
This excluded part is genuinely infinite: for every `r>=0`,
`w=7`, `u=8r+3`, `x=8r^2+6r+1` satisfies the family square condition and
fails both the layer-1 and layer-3 handshakes.

Full derivation: `source-family-handshake-congruences.md`. No GAP, web,
catalogue, constituent, or construction work was used. Conservatively charging
the five-minute correction cap, leased replay/report, and this symbolic block
puts the cumulative ledger at about 227 minutes, leaving about 13 minutes in
extension 1. Outcome: candidate `PARTIAL_RESULT`, sent for Validator review;
current strategy has reached its exact residual congruence frontier and is at a
pivot checkpoint. `active_assignment_answered: no`; state `awaiting_lead`.

## 2026-08-17T11:55:40Z — CONTINUE, even-IIii 2-adic/spectral gate

Resumed at centralized minute 227 with a 13-minute cap. Separated the even-`x`
and odd-`x`, even-`w` square-condition branches and substituted the Type-(IIii)
formulas into the exact constituent multiplicities and eigenmatrix.

## 2026-08-17T11:59:03Z — formal self-duality; exact residual frozen

Charged about four minutes, reaching cumulative minute 231 with about nine
extension minutes unused. The even residual is not removed: the multiplicities
are exactly `(1,k,kt,kw)`, equal to the valencies, and the eigenmatrix satisfies
`P=Q`, so Krein integrality adds no independent 2-adic obstruction. The exact
remaining congruences are (i) `x` even with
`nu_2(x)+nu_2(w+1)>=3`, or (ii) `x` odd, `w` even, with
`x(w+1)=3 mod 4`, always subject to the square equation. Both branches have
explicit infinite positive solutions.

Full hand derivation: `ii-even-2adic-spectral.md`. No computation or external
search occurred. Outcome: `STRATEGY_EXHAUSTED` for this symbolic gate only;
the odd-`x,w` partial remains pending fresh validation and the full problem is
not parked. `active_assignment_answered: no`; state `awaiting_lead`.
