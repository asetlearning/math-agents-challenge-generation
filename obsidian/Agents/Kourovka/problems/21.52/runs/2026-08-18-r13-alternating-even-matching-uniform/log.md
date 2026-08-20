---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/draft
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
cycle: 13
run: 2026-08-18-r13-alternating-even-matching-uniform
---

# Cycle 13 log: alternating even matchings

## 2026-08-18T06:15:18Z — active work start

Active ledger starts at cumulative minute `206`; this fresh lane has at most 45
new active minutes.  The binding target is the single class

\[
D_{n,k}=\{\text{permutations of cycle type }2^k1^{n-2k}\}\subseteq A_n,
\qquad k\ge2\text{ even},\quad n\ge2k,
\]

in the simple alternating groups among those parameters.  No previous `k=2` or
`k=4` family result, table, or array is a premise.

## Source and staleness gate

- Resolved the source through `_meta/agents/Kourovka/paths.env` and inspected PDF
  page 172 both as layout text and as a 144-dpi rendering.
- Corrected transcription: Let `L` be a finite non-abelian simple group and `D`
  one conjugacy class of involutions.  On the complete graph with vertex set `D`,
  edges `{a,b}` and `{c,d}` have the same colour exactly when `|ab|=|cd|`.  A
  colour automorphism is a permutation `tau` of `D` preserving this equivalence
  for every edge.  The question is whether every such permutation is induced by
  an automorphism of `L` (typed as the restriction of a setwise stabilizer of
  `D`).
- `source_transcription_checked: yes`; the rendered formula uses exact element
  order, not conjugacy class of the product.
- The configured PDF is issue 21 (2026), and the displayed item has no editor or
  later-answer comment.  This is a discovery-blind run, so
  `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- Clause matrix: source object clause, complete-graph clause, exact-colour clause,
  and colour-automorphism question all belong to scope
  `21.52/involution-class-product-order-colouring`.  Problem 21.53, a union of
  involution classes, an uncoloured graph, and colouring by product conjugacy
  class are excluded.
- `active_scope_checked: yes`.  The seven canonical rows are: universal
  quantifier; finite nonabelian simple `L`; one involution class `D`; complete
  simple graph on `D`; exact product-order colours; preservation of every edge
  colour; extension to a setwise-stabilizing automorphism of `L`.  The present
  family can only be a partial result for the universal row.

## Strategy portfolio

1. **Theoretical / cheapest certifiable route.** Derive the union-component rule
   for products of two matchings.  Search for a colour whose edges have a unique
   common transposition, then recover the transposition stars by an intrinsic
   triangle or common-neighbour relation and invoke the line graph of `K_n`.
2. **Structured route.** For `k=6`, colour 11 is promising: primality should force
   the two matchings to share one edge and make their other five edges a single
   alternating 10-edge path.  Try to reconstruct the shared-edge labels of these
   colour-11 pairs uniformly in `n`.
3. **Uniform route.** For general even `k`, use an odd prime contribution larger
   than `k` (Bertrand) to force one long alternating path plus a common core; audit
   the exceptional case `p=k+1` where two long paths can occur.  Determine whether
   these core-labelled colour graphs reconstruct individual transpositions.
4. **Bounded catalogue probe.** A small local enumerator may test triangle-label
   conjectures around one matching.  Any output is only a conjecture filter, never
   a proof or a universal conclusion, and no run over 60 seconds is authorized.
5. **Certificate plan.** A family partial must give the component formula, an
   intrinsic colour-only definition of edge stars, all extremal/connectivity
   inequalities, the `S_n` reconstruction, the single-class check in `A_n`, and
   the `A_6` exception audit.  Validator should be able to check it entirely by
   hand.

## 2026-08-18T06:20:00Z — colour-11 gate and representation pivot

For `k=6`, the component rule shows that exact colour 11 means: one common
transposition and a single alternating 10-edge path on the other five edges from
each matching.  I tested the tempting claim that every colour-11 triangle has a
single common-edge label.  The bounded conjecture-filter script is
`scratch/sample_colour11_triangles.py` (SHA-256
`92f6787605ed55b4b938a4109fccecc9e8e96983f8448031c52f5105c9c00d75`).
The exact command was

```text
timeout 50s python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r13-alternating-even-matching-uniform/scratch/sample_colour11_triangles.py
```

It exited zero.  On the local neighbourhood of one 6-matching at `n=13`, it
generated all 23,040 colour-11 neighbours and sampled 2,000,000 neighbour pairs.
Among 338,966 sampled colour-11 triangles, 222,258 used different labels; the
script prints an explicit first example.  Thus triangle equivalence is decisively
the wrong label-recovery predicate.  This finite run proves no family statement.

Representation pivot: use the exact number of common colour-2 neighbours.  Since
colour 2 is commutation, a common centralizer matching preserves both supports
setwise and splits over their union and its complement.  The resulting falling-
factorial expansion has first coefficients `1` and an explicit one-edge invariant.

## 2026-08-18T06:24:52Z — candidate uniform stable-range partial

Wrote `findings.md`, giving a candidate hand proof for every even `k>=2` and

```text
n >= N(k) = 4 k B_k + 6 k,
B_k = sum_{j=1}^k binom(binom(4k,2),j).
```

For a pair `M,N`, the colour-definable common-centralizer count is

```text
K(M,N) = sum_{j=0}^k a_j(M,N) mu_{k-j}(n-u),
u = |supp(M) union supp(N)|,  a_0=1.
```

The explicit range makes the `mu_k`, `mu_{k-1}`, and lower scales numerically
disjoint at this single fixed `n`.  Hence `K` recovers `u` and `a_1`.  These two
numbers define “share exactly `k-1` transpositions”.  Maximum core cliques in the
resulting matching-Johnson graph, a strict `>4` cross-edge test, and the recovered
`KG(n,2)` then reconstruct transposition stars and point stars, forcing the natural
`S_n` action.  The range is above 6, so the exceptional `A_6` automorphisms do not
occur.  The `A_n` class is single because its centralizer contains a constituent
odd transposition.

All seven canonical rows are audited in `findings.md`.  The universal quantifier
remains open: this is an infinite alternating-family `PARTIAL_RESULT`, not a scope
claim.  Recommended next state is independent Validator reconstruction of the
falling-factorial separation and downward core-star induction; if upheld,
MathExpert should assess whether the huge bound can be reduced by sharper
coefficient estimates.

## 2026-08-18T06:24:52Z — active work stop

Charge 10 new active minutes, cumulative `206--216`.  Outcome:
`PARTIAL_RESULT`.  Research state is `awaiting_lead`; 35 authorized minutes remain
unused rather than being spent after a substantial reviewable result.
