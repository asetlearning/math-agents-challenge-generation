---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, topic/alternating-groups, project/kourovka, status/draft]
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: proof
cycle: 11
---

## 2026-08-18T05:16:38Z — active work start

Cumulative active minutes at start: **149**. Allocation: at most 31 new active
minutes. Active strategy is exactly
`ALTERNATING-DOUBLE-TRANSPOSITION-TWO-COLOUR`; no Problem 21.52 assertion and no
fixed `M11` result is a premise.

## Staleness check

- Source path was resolved only through `_meta/agents/Kourovka/paths.env`.
- The rendered source PDF, page 172, was visually inspected (PNG rendering at
  130 dpi) as well as navigated with `pdftotext`.
- Corrected transcription: in the notation of 21.52, `D` is a single conjugacy
  class of involutions in a finite nonabelian simple group `L`, the complete graph
  on `D` has two edges equivalent exactly when the two endpoint-products have the
  same order, and `Aut_t(Gamma)` is the set of permutations of `D` which send each
  exact order-`t` edge to an exact order-`t` edge. The question asks whether
  `Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)`, where `{2,p}` are the two
  smallest distinct prime divisors of the group order.
- `source_transcription_checked: yes`.
- The local corpus contains issues 1--20 but no issue-21 JSONL/markdown record,
  so the requested machine-readable `answered`, `has_editor_comment`, and
  `has_later_comment` flags are unavailable. The current rendered issue-21 page
  labels this under “New Problems (21st issue, 2026)” and displays no answer,
  editor comment, or later comment on 21.53.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`
  because the canonical scope has `blind_run.enabled=true` and forbids open-web
  or solution-bearing-history search.
- `active_scope_checked: yes`. Clause matrix:

| source clause | equivalent formulation | in active scope? | literature status in this blind run |
|---|---|---:|---|
| inherited 21.52 notation | finite nonabelian simple `L`, one involution class `D`, exact product-order colouring | yes | deferred |
| definition of `Aut_t` | preserve the exact `t`-edge set; absent relation gives all of `S_D` vacuously | yes | deferred |
| full group | intersection over all exact occurring colours | yes | deferred |
| question | do exact colours 2 and the second prime `p` determine every colour? | yes | deferred |

Constraint audit for the assigned family:

| constraint_id | assigned-family use |
|---|---|
| `21.53-forall-L-D` | This lane proves at most the explicitly delimited family `(A_n,D_{2^2})`, hence only a partial result for the universal source quantifier. |
| `21.53-L-finite-nonabelian-simple` | `A_n` is finite nonabelian simple for every `n>=5`, hence throughout the requested `n>=7`. |
| `21.53-D-single-involution-class` | `D_{2^2}` is the single `A_n`-class of cycle type `(2,2,1^{n-4})`; the `S_n` class does not split in `A_n` because its type has repeated even parts (also directly, its centralizer contains odd permutations). |
| `21.53-Gamma-product-order-colouring` | Every unordered distinct pair is classified by the exact order of the permutation product. |
| `21.53-Aut-t-definition` | All reconstruction statements use the exact binary edge sets `R_t`, including the source's one-way preservation convention. Finiteness makes one-way preservation equality on each edge set. |
| `21.53-two-minimal-primes` | `|A_n|=n!/2`; for `n>=7`, both 2 and 3 divide it and no prime lies strictly between them, so `p=3`. |
| `21.53-full-colour-group-definition` | Must reconstruct every occurring `R_t`, not merely an orbit partition or support geometry. |
| `21.53-two-colours-determine-all` | Assigned conclusion is equality for `(A_n,D_{2^2})`; this does not answer the universal row. |

No scope-record mismatch was found.

## Strategy portfolio

Ranked by information per active minute:

1. **Theoretical/coherent-count reconstruction.** Classify the two-coloured union
   of two 2-edge matchings, obtaining every exact product order. For the three
   unselected colours compute a small invariant formed solely from common-neighbour
   counts in `R_2,R_3`; distinct profiles would make each colour definable.
2. **Bounded catalogue audit.** Enumerate all 2-edge matchings for degrees 7 through
   a modest interpolation bound and tabulate mixed `R_2/R_3` common-neighbour
   counts by union type. This is a check and formula-discovery device only; it
   cannot by itself prove all degrees.
3. **Structured incidence reconstruction.** Recover 2-subsets/4-supports and then
   the Johnson scheme from extremal `R_2/R_3` cliques if coherent counts collide.
4. **Certificate plan.** Give canonical pair representatives, a hand-derived
   complete union-shape/order table, closed polynomial common-neighbour formulas,
   and a finite list of exceptional roots/degrees checked directly by the same
   hand count. Validator can reconstruct every count from the four-edge overlay,
   independently of any automorphism package.

Kill criterion: if the first-order four common-neighbour counts fail to separate
orders 4, 5, and 6 after exceptional-degree analysis, report the exact collisions
and hand off the live incidence-reconstruction pivot rather than extrapolating.

## 2026-08-18T05:23:27Z — complete hand reduction and bounded check

The four-edge overlay has exactly eight pair orbit-types.  Their exact product
orders are `2,2,2,3,3,4,5,6`; the disjoint-support order-2 type first occurs at
`n=8`, while all five colours already occur at `n=7`.

For an unordered pair `(x,y)`, define solely from `R_3`
`q(x,y)=|Gamma_3(x) intersect Gamma_3(y)|`.  Direct hand intersection of the two
order-3 overlay types gives

- order 4: `q_4=4(n-5)`;
- order 5: `q_5=(n-4)^2`;
- order 6: `q_6=4(n-3)`.

They are pairwise distinct at every integral `n>=7`.  In particular the requested
audits are `(q_4,q_5,q_6)=(8,9,16)` at `n=7` and `(12,16,20)` at `n=8`.
Although the `q_5,q_6` ordering reverses between `n=8` and `n=9`, equality would
require `(n-6)^2=8` and hence never occurs at an integer.  The excluded `n=6`
boundary has the real collision `q_4=q_5=4`.

Cheap certificate check (no compute lease needed; 1.1 seconds wall time):

```text
python3 Agents/Kourovka/problems/21.53/runs/2026-08-18-r11-alternating-double-transposition-two-colour/type_counts.py
n=7:  R4 q33=8,  R5 q33=9,   R6 q33=16
n=8:  R4 q33=12, R5 q33=16,  R6 q33=20
n=9:  R4 q33=16, R5 q33=25,  R6 q33=24
...
n=15: R4 q33=40, R5 q33=121, R6 q33=48
```

The full observed output also included all four `(R_2,R_3)` mixed counts for
each representative and is reproducible from `type_counts.py`.  The family proof
uses only the hand lists and the `q33` formulas, not interpolation or an
automorphism package.

Outcome: candidate `PARTIAL_RESULT` for all `(A_n,D_{2^2})`, `n>=7`; universal
`active_assignment_answered: no`.  Full argument and all eight constraint rows are
in `partial-result.md`.

## 2026-08-18T05:25:20Z — active work stop and handoff

Cumulative active minutes: **159** (`149--159`, 10 minutes charged; 21 minutes of
this allocation unused).  The family argument is complete enough for hostile
independent reconstruction, so charged research stops pending Lead/Validator
review.
