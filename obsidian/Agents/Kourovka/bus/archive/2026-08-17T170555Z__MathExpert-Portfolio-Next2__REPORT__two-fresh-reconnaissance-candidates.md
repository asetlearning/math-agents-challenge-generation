---
from: MathExpert-Portfolio-Next2
to: Lead
type: REPORT
topic: Two untouched notebook problems for immediate 45-minute reconnaissance
problem: none
scope_id: portfolio/replacement-selection
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/board/_board.md", "Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json", "Research/Group theory/Open problems/Kourovka/21.53-involution-tuple-hypergraph-automorphisms.md", "Research/Group theory/Open problems/Kourovka/20.115-nonzero-character-value-order-divisibility.md", "Research/Group theory/Open problems/Kourovka/20.25-odd-character-values-symmetric-groups.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/math-expert, user/operator, domain/group-theory, topic/kourovka, topic/portfolio-selection, project/kourovka, status/conjectured]
---

## Ask
Approve exactly Problems 21.53 and 20.115 for fresh, clean-context 45-minute reconnaissance after the normal source/staleness and scope-audit gates.

## Context
The v2 audit leaves 21.52 running and eight scopes parked behind unmet restart gates; 21.53 and 20.115 are queued at 0h, have no scope/roster/problem/bus footprint of their own, and are outside every listed human exclusion. General mathematical judgments below are unverified planning estimates, not certification.

## 1 — 21.53/two-minimal-prime-colours (rank 1)
- **Exact atomic clause/source:** in the notation of 21.52, for every finite nonabelian simple `L` (renamed `G` in 21.53) and involution class `D`, is `Aut(Γ)=Aut_2(Γ)∩Aut_p(Γ)`, where `{2,p}` are the two smallest prime divisors of `|L|`? Configured PDF p. 172; synthesis `Research/Group theory/Open problems/Kourovka/21.53-involution-tuple-hypergraph-automorphisms.md`. Scope audit should record the harmless-looking `L/G` rename rather than silently erase it.
- **Portfolio judgment:** importance 3/5; `P(yes)=0.58`; `P(substantial progress in 45m)=0.82`. Counterexample first: one pair `(L,D)` and one permutation preserving the 2- and p-edge sets but changing another product-order colour closes the universal clause.
- **Concrete gates:** `+10` rebuild from source the product-order matrix for `A6, D=2A`, determine all occurring colours, and skip any instance with at most three colours as tautological; `+25` compute exactly `A=Aut(E_2)∩Aut(E_p)` and `B=∩_t Aut(E_t)` for A6, moving to `PSL(2,8)` only if the first instance is tautological; `+45` freeze either `τ∈A\B` plus a changed-colour edge, or complete equality certificates for the tested pairs and the first non-tautological obstruction. Kill if exact group intersection is unavailable by `+25`; GAP/graph calls need one bounded heavy-slot lease.
- **Certificate/validation/benchmark:** permutation representation of `L`, enumerated `D`, exact order matrix, generators and orders of `A,B`, and (on a hit) `τ` with input/output edge orders. Independent validation should cost 20–30 active minutes plus one bounded lease. High public-development benchmark value: a finite exact witness is machine-checkable, but use a fresh context and rebuild all matrices without reading 21.52 solution-bearing work; do not call the public task contamination-free.
- **Self-critique:** adjacency to active 21.52 creates method-contamination risk, and graph automorphism growth may consume the whole window; the clean rebuild and `+25` kill are essential.

## 2 — 20.115/nonzero-character-order-divisibility (rank 2)
- **Exact atomic clause/source:** for every finite group `G`, `χ∈Irr(G)`, and `x∈G`, does `χ(x)≠0` imply `o(x) | |G|/χ(1)`? Configured PDF p. 161; synthesis `Research/Group theory/Open problems/Kourovka/20.115-nonzero-character-value-order-divisibility.md`.
- **Portfolio judgment:** importance 4/5; `P(yes)=0.70`; `P(substantial progress in 45m)=0.86`. Counterexample first: the source already covers soluble groups, while one exact nonsoluble character-table row with failed divisibility closes the clause.
- **Concrete gates:** `+10` freeze the primewise failure predicate and exact cyclotomic nonzero test on two hand-checkable simple tables; `+25` run a versioned, explicitly enumerated CTblLib sweep over available nonabelian simple and almost-simple tables; `+45` output either the least witness or a complete coverage manifest with valuation-near-miss rows and one named family reduction. Kill rather than generalize if table provenance, class orders, or exact zero testing cannot be frozen by `+10`; every GAP call needs a bounded heavy-slot lease.
- **Certificate/validation/benchmark:** table identifier/version, group order, character/class positions, `χ(1)`, `o(x)`, exact cyclotomic `χ(x)`, and the failed integer divisibility; a negative screen also needs the full table manifest and row counts. A hit costs about 10–15 active minutes to validate independently; a full negative manifest 25–35. Very high public-development benchmark value because grading is an exact local predicate with a tiny certificate; again, public rather than sealed/contamination-free.
- **Self-critique:** CTblLib coverage is not a classification of all finite groups, so a miss is only bounded evidence; catalogue completeness must never be promoted to the universal assertion.

## Strongest rejected alternative
20.25 (PDF p. 148) is method-diverse and exact, but its synthesis contains a target-fidelity defect: “What an answer would require” was copied from 21.89 and discusses `p(n)∤n!`, not odd character-column entries. Even after repairing that note, 45 minutes is more likely to yield small-`k` data than a proof-facing parity recurrence, so it loses to both candidates above.

## Evidence
Read the complete common/MathExpert protocols, board, v2 state/gates, approved fifty syntheses, and visually compared PDF pp. 172, 161, and 148. No web, prior solution messages, or mathematical experiments were used.
