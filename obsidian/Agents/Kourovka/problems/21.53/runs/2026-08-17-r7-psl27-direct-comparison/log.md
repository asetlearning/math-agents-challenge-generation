---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: counterexample
run: 2026-08-17-r7-psl27-direct-comparison
---

# Cycle 7: direct comparison for PSL(2,7)

## 2026-08-17T23:50:04Z — active work start

Official cumulative active time starts at minute `91`; this increment is capped at
35 minutes, with research stopping by minute 30 and packaging by minute 35.  The
only permitted pair is `L=PSL(2,7)` and its single involution class `D`.

## Staleness and source-transcription gate

- Visually inspected rendered source-PDF page 172 (21st issue, 2026), not only its
  extracted text.  Problem 21.53 says, in the notation of 21.52, that
  `Aut_t(Gamma)` consists of those permutations `tau in S_D` for which
  `(a,b) ~ (a^tau,b^tau)` whenever `|ab|=t`, that
  `Aut(Gamma)=intersection_t Aut_t(Gamma)`, and asks whether
  `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)` when `{2,p}` are the two
  minimal prime divisors of the finite simple group's order.
- The inherited notation on the same rendered page defines `L` as finite
  nonabelian simple, `D` as one conjugacy class of involutions, the vertices as
  `D`, and edge colour by exact equality of product order.
- The displayed current-edition entry has no answer, editor comment, or later
  comment.  No issue-21 JSONL corpus record is present in the configured corpus
  directory; the canonical scope record supplies the audited source metadata.
- `source_transcription_checked: yes`; `active_scope_checked: yes`.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
  No open-web search or solution-bearing history was inspected.

### Clause matrix

| source clause | exact operational form | active? |
|---|---|---|
| inherited 21.52 notation | finite nonabelian simple `L`; one involution class `D`; complete graph coloured by `o(ab)` | yes |
| `Aut_t` | one-way preservation of every `t`-edge; if there is no `t`-edge the condition is vacuous and gives `S_D` | yes |
| full group | intersection over all positive integers, equivalently over all occurring colours | yes |
| question | compare full group with the intersection for the two least prime divisors `2,p` | yes |

### Admissibility checklist

All eight revision-2 rows are represented: universal `(L,D)` quantifier;
finite-nonabelian-simple `L`; one exact involution conjugacy class `D`; complete
exact product-order colouring; one-way/vacuous `Aut_t`; `p` the least prime
divisor above 2; full colour group as the all-colour intersection; and equality
as the conclusion being tested.  The assigned finite pair can refute the universal
row only if strict inequality is certified; equality is bounded partial progress.
No mismatch with the canonical record was found.

## Strategy portfolio

1. **Exact small-case model (first).** Reconstruct `PSL(2,7)` as
   `GL(3,2)` by enumerating all 168 invertible binary `3 x 3` matrices, determine
   every conjugacy class and order, isolate the involutions, and emit the complete
   21-point product-order matrix plus digests.  A negative separator result proves
   only equality for this fixed pair.
2. **Structured geometry.** Interpret involutions as the 21 flags of the Fano plane
   and seek intrinsic recovery of every remaining colour from the order-2 and
   order-3 relations.  This can certify equality without trusting an automorphism
   package.
3. **Theoretical fallback.** Use valencies and common-neighbour/intersection numbers
   to show the remaining relation matrices are polynomials or canonical predicates
   in the two retained relations.
4. **Certificate plan.** Preserve a canonical lexicographic vertex list, all 210
   unordered matrix entries, colour counts/valencies, SHA-256 digests, and group/
   class checks.  If strict, display the full 21-image permutation, exhaustively
   count preservation failures for colours 2 and 3, and show an explicit changed
   edge.  If nontrivial, freeze the automorphism-comparison input and command and
   obtain a Lead lease before execution.

## 2026-08-17T23:53:12Z — exact group, class, and matrix enumeration

Wrote and ran the deterministic integer-arithmetic enumerator
`scratch/psl27_exact_scheme.py`.  It constructs exactly
`SL(2,7)/{+I,-I}`: all determinant-one `2 x 2` matrices modulo the central sign,
using the lexicographically smaller of `A,-A` as canonical representative.  Exact
command:

```text
timeout 20s /usr/bin/time -f 'WALL=%e CPU=%P MAXRSS_KB=%M' python3 Agents/Kourovka/problems/21.53/runs/2026-08-17-r7-psl27-direct-comparison/scratch/psl27_exact_scheme.py
```

Observed output:

```text
MODEL=PSL(2,7)=SL(2,7)/{+I,-I}
SL2_MATRIX_COUNT=336
GROUP_ORDER=168
ELEMENT_ORDER_COUNTS={1: 1, 2: 21, 3: 56, 4: 42, 7: 48}
CONJUGACY_CLASS_ORDER_SIZE=[(1, 1), (2, 21), (3, 56), (4, 42), (7, 24), (7, 24)]
NORMAL_CLASS_UNIONS_TESTED=32
NORMAL_SUBGROUP_SIZES=[1, 168]
NONABELIAN_WITNESS={'a': [0, 1, 6, 0], 'b': [0, 1, 6, 1], 'ab': [1, 6, 0, 1], 'ba': [1, 0, 1, 1]}
INVOLUTION_COUNT=21
INVOLUTION_CLASS_COUNT=1
EDGE_COLOURS=[2, 3, 4]
EDGE_COLOUR_COUNTS={2: 42, 3: 84, 4: 84}
COLOUR_VALENCIES={2: 4, 3: 8, 4: 8}
DIGESTS={'projective_elements_sha256': '9ee0b7498470f817c28d48202918e8df8fa8ad498a15ea9dd49e32a7d0596996', 'involution_vertices_sha256': 'a1e99b777d98da03e9742c257194addb343aa9da699392ec64f9ee6ad6ddb19c', 'product_order_matrix_sha256': '66f19056e9bea032b266798406fe28842a8bc7b7ca3364dde2a6bac814d7cda8', 'unordered_edges_sha256': 'be05645469287e5409b437a4ed7df585a1746fd3fcd2741bf7e09aab0948fc47'}
CERTIFICATE=psl27_exact_scheme_certificate.json
MATRIX_CSV=psl27_product_order_matrix.csv
WALL=0.44 CPU=38% MAXRSS_KB=16768
```

The program exhaustively checks closure/inverses of the 168 projective elements,
partitions them into all six conjugacy classes, and tests all `2^5=32` unions of
conjugacy classes containing the identity for subgroup closure and inverses.  Only
sizes 1 and 168 occur, an exact simplicity check.  The displayed unequal products
give nonabelianity.  There is exactly one order-2 class and it has size 21.

The full 21-vertex list, all 210 unordered edges, and the 21-by-21 matrix are in
`scratch/psl27_exact_scheme_certificate.json`; the same matrix is separately in
`scratch/psl27_product_order_matrix.csv`.  File SHA-256 values observed after the
run are:

```text
54545eba3defdba8faade61d957d55dd7671d4eab540363bb7d6a3723a0a9d8a  scratch/psl27_exact_scheme.py
9dc3be4f7b84564e1ecd1cddc33c0f101210ec142225f3fdbfd48d50ff8536f7  scratch/psl27_exact_scheme_certificate.json
c184a782544ea0b3dceefc3cd495c5679044a4dc3693aabf6caf1b3f56e53ff2  scratch/psl27_product_order_matrix.csv
```

An optional `jq` display command failed because `jq` is not installed; it was not
needed and no mathematical computation depended on it.  Plain-text inspection of
the CSV displayed all 21 rows.

Since `168=2^3*3*7`, the required second-smallest distinct prime is `p=3`.

## Exact equality argument for the fixed pair

Let `E_t` denote the set of unordered edges with product order `t`.  The complete
inventory is exactly `E_2,E_3,E_4`; their sizes are `42,84,84`, and their constant
vertex valencies are `4,8,8` respectively.

Take any `tau in Aut_2(Gamma) intersection Aut_3(Gamma)` under the source's
one-way convention.  The induced map on the finite 210-edge set is a bijection.
The defining implications give `tau(E_2) subseteq E_2` and
`tau(E_3) subseteq E_3`; injectivity and finiteness upgrade both inclusions to
equalities.  Therefore `tau` preserves the complement
`E_4 = Edges(Gamma) minus (E_2 union E_3)`.  Hence it preserves every occurring
colour and lies in `Aut(Gamma)`.  The reverse containment follows directly from
the definition.  Nonoccurring labels have `Aut_t(Gamma)=S_D` vacuously and do not
alter the full intersection.

Thus the assigned fixed pair has equality for a tautological three-colour reason.
No automorphism comparison was run and no compute lease was needed.  This is a
bounded finite partial result, not a statement about the universal scope.

## 2026-08-17T23:56:13Z — active work stop and cycle outcome

An `awk` row-by-row comparison returned
`DISPLAY_MATRIX_MATCHES_CSV=YES`, so the 21 displayed rows in `partial-result.md`
match the generated CSV exactly.  Outcome: `PARTIAL_RESULT`.  Charge 7 active
minutes (rounded conservatively from the recorded interval), cumulative `91--98`;
28 authorized minutes are returned unused.  `active_assignment_answered: no`.

