---
title: "Kourovka 21.53 — PSL(2,q) two-colour rigidity proof lane"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: proof
outcome: RUNNING
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# PSL(2,q) two-colour rigidity

## 2026-08-17T21:07:55Z — work start

Start fresh proof lane at cumulative active minute 42. Lead authorizes at most 60
new active minutes on the exact simple `PSL(2,q)` family; no catalogue expansion
and no heavy computation.

## Source and current-staleness gate

The configured source PDF resolves. Page 172 was rendered at 130 dpi and visually
inspected in `/tmp/kourovka-21-53-page-172.png`. It says, in the notation of 21.52,
that `L` is finite nonabelian simple, `D` is one conjugacy class of involutions,
and edges are coloured exactly by `|ab|`; `Aut_t` preserves every edge with
`|ab|=t`; the question is whether the full colour group is the intersection for
the two minimal prime divisors `{2,p}`. This agrees with every revision-2 scope
row. `source_transcription_checked: yes`; `active_scope_checked: yes`.

This discovery-blind scope has `open_web:false`, so no new open-web search is made.
The current staleness/control gate is the Lead decision
`2026-08-17T210308Z__Lead__DECISION__psl2q-two-colour-rigidity.md`, issued only after
Validator independently replicated the fixed `PSL(2,11)` result. External
staleness remains delegated to Lead/human. Nothing in the reviewed material answers
the infinite `PSL(2,q)` family.

## Constraint checklist for the bounded family

The intended output is only a `PARTIAL_RESULT` for all prime powers `q>=4` for
which `PSL(2,q)` is simple. It must: identify the complete involution class(es),
derive `p=3` from the exact group order, use the literal every-positive-integer
`Aut_t` definition including empty relations, reconstruct every product order,
and establish the two-colour equality. It cannot discharge
`21.53-forall-L-D` outside this family and cannot answer Problem 21.52.

## Strategy portfolio

1. **Theoretical rank-one geometry (chosen).** In characteristic two identify
   involutions with nonzero vectors of `F_q^2`; in odd characteristic identify
   them with one norm class of nonsingular points in `P(sl_2(q))`. Translate
   product order into determinant/trace data and try to reconstruct the relevant
   semilinear group from the order-2 and order-3 relations.
2. **Small symbolic audits.** Use only the already reviewed `q=8,9,11` facts to
   test formula normalizations. A finite pass proves no family statement.
3. **Cross-ratio pivot.** If the orthogonal-space automorphism reconstruction has
   exceptional small fields, recover the projective line or unordered fixed-point
   pairs and invoke the fundamental theorem of projective geometry.
4. **Certificate plan.** Supply explicit coordinates, both relation equations,
   a self-contained rigidity lemma with its exceptional-field checks, and a formula
   showing that every product order is invariant under the resulting semilinear
   maps. Validator can audit every algebraic identity without trusting code.

Kill criterion: if the semilinear rigidity lemma cannot be proved uniformly, stop
at an explicit characteristic-separated reduction and name the missing lemma;
do not promote the reviewed finite cases to a family theorem.

## 2026-08-17T21:21:41Z — `PARTIAL_RESULT`, work stop

Charge 15 active minutes, cumulative 42--57, and return 45 of the newly authorized
60 minutes unused. The named strategy reached its exact kill criterion: the
characteristic-two coordinate model closes completely, while the odd case reduces
to a finite-geometry rigidity assertion that has not been proved here.

### New facts

- `p=3` for every simple `PSL(2,q)` directly from
  `q(q-1)(q+1)/gcd(2,q-1)`.
- For `q=2^f`, involutions are canonically `V\{0}` and the two relations are
  dependence and determinant one. An elementary functional equation proves
  `Aut_2 intersect Aut_3=GammaSL(2,q)=PGammaL(2,q)`, and the trace formula proves
  that this group preserves every product-order colour.
- This proves the family theorem for every even `q>=4`; `q=5` is the identical
  `A5` pair already covered at `q=4`.
- For odd `q`, the complete class is one norm orbit in `P(sl_2(q))`; the entire
  colouring is determined by `tr(XY)^2`, with order 2 equal to orthogonality and
  order 3 given by normalized squared inner product one.
- If `q=3^f` with odd `f`, the order-3 relation is empty, so the source convention
  gives `Aut_3=S_D` vacuously. Exact valency formulas are in `partial-result.md`.

### Bottleneck and alternatives

The missing assertion is
`Aut(S;R_2,R_3)=PGammaO(3,q)` on one nonsingular square-class orbit for every odd
`q>=7`; in the `q=3^(odd)` subfamily it must follow from `R_2` alone. Treating this
as obvious would be the precise unsupported step that could invalidate a claimed
whole-family proof.

Two qualitatively different next steps are:

1. an incidence-completion proof that the orthogonality graph reconstructs the
   ambient conic/polarity, followed by the fundamental theorem of projective
   geometry; or
2. the frozen single-field `q=27` audit, the first vacuous-`R_3` case, to test
   whether the conjectured rigidity is even true before investing in (1).

The Math Expert was asked for the missing theorem/proof. A frozen one-shot `q=27`
manifest and lease request were sent to Lead; no computation was run. The lane is
`awaiting_lead`, not parked. Equality outside the even-characteristic family is
not claimed.

## 2026-08-17T21:23:50Z — leased `q=27` audit completed and slot released

Lead explicitly resumed only the frozen one-shot audit. Both frozen hashes matched.
The exact manifest command exited zero in 3.186 seconds. GAP 4.12.1 / GRAPE 4.9.0
found the 351-vertex involution commuting graph to have valency 14 and full
automorphism-group order 58,968, exactly `|PGammaL(2,27)|`. Preserve this only as
a finite stress test at the first vacuous-order-3 field. The verbatim output and
limitations are in `q27-audit.md`.

Charge two further active minutes for the supervised invocation and inspection,
cumulative 57--59; return 43 of the newly authorized 60 minutes unused. Compute
slot 2 was released immediately by bus report. The odd family lemma remains
unproved, so the cycle outcome remains `PARTIAL_RESULT` and the lane returns to
`awaiting_lead` rather than self-parking.

## 2026-08-17T21:31:45Z — protocol-only CLAIM routing repair

No new mathematics, computation, or active research time. The bounded
even-characteristic family theorem is now wrapped in `findings.md` and has the
mandatory claim check
`Agents/Kourovka/problems/21.53/claim-checks/21.53-psl2-even-r2-partial-001.json`.
The JSON marks the canonical universal target unproved,
`active_assignment_answered:false`, the odd family unclaimed, and `q=27` as a
finite audit only, while setting `ready_for_validator:true` for the exact bounded
partial theorem.

`python3 _meta/scripts/kourovka-state-check.py` exited zero: six claim checks,
zero errors, and seven unrelated legacy/old-revision warnings. The active-time
ledger remains cumulative minute 59.
