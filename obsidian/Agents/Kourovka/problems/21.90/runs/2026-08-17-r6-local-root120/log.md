---
title: "Problem 21.90 run 6 log — local-root gate"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/draft
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
strategy: IIii-LOCAL-ROOT-120
cycle_outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Run log

## Scope control and inputs

- Canonical scope: `21.90/diameter-three-distance-graphs`, revision 3.
- Exact bounded target: the Type-II(ii) tuple `(x,w,u)=(1,2,2)`, hence only the
  formal array `{17,8,6;1,2,12}`.
- Allowed reviewed inputs: the revision-3 scope record, the current roster and
  Lead decision, the MathExpert local-root assessment, and Validator's reviewed
  Type-II(ii) package.
- External staleness search: not repeated in this resumed, no-web increment; the
  canonical source and revision-3 source audit remain controlling.
- No web, catalogue, computation, or delegated agent was used.

## Active-time ledger

- `2026-08-17T13:26:04Z` — run activated and charged work started with
  protocol/scope reconciliation; cumulative scope time `239` minutes, run active
  minute `0`.
- `2026-08-17T13:33:00Z` — 15-minute kill gate satisfied early: the local spectral
  inequality was derived directly from the primitive-idempotent Gram matrix and
  the cosine recurrence; continue.
- `2026-08-17T13:35:00Z` — 30-minute kill gate satisfied early: both `A_17` and `D_17`
  support-graph translations were explicit, including the parallel-support case
  in type `D`; continue to package.
- `2026-08-17T13:36:59Z` — charged work stopped at run active minute `11`;
  cumulative scope time `250` minutes. Outcome: `PARTIAL_RESULT` pending Validator.

## Strategy portfolio

1. **Theoretical local-spectrum/root-lattice gate (selected).** Derive the local
   eigenvalue interval from distance-regular identities, form the integral Gram
   matrix `2I+A`, invoke the irreducible simply-laced classification, and analyze
   the resulting support graphs.
2. **Structured construction.** An explicit 120-vertex fission would be
   target-faithful, but no constituent is available in the reviewed inputs and it
   is outside this no-compute assignment.
3. **Catalogue mode.** Forbidden by the Lead decision and unnecessary for the
   exact local obstruction.
4. **Certificate plan.** A self-contained four-lemma hand derivation that
   Validator can reconstruct without trusting code, a graph catalogue, or a
   numerical spectrum.

## Result

The candidate argument in `findings.md` excludes an actual distance-regular graph
with intersection array `{17,8,6;1,2,12}`. It does not establish existence or
nonexistence for the revision-3 Kourovka scope, and it does not authenticate or
complete the source-family classification.

The local graph would be 8-regular on 17 vertices, and every nonprincipal local
eigenvalue would lie in `[-9/5,3]`. Hence `2I+A` is positive definite. Its 17
norm-two generators span an irreducible rank-17 simply-laced crystallographic root
system, so only `A_17` and `D_17` can occur. In type `A`, the generators are the
edges of a 17-edge tree whose line graph is 8-regular; the leaf degree equation
forces the tree to be `K_{1,9}`, a contradiction. In type `D`, the support
multigraph is unicyclic. A possible parallel pair is incompatible with
8-regularity; in the remaining simple case independence forces an odd cycle and
the line-graph degree equation forces every support-graph degree to be 5,
contradicting its 17 vertices and 17 edges.

## Limitations

- This is one array-level nonexistence claim at `status/conjectured` pending
  independent validation.
- It removes only `(x,w,u)=(1,2,2)` from the reviewed even Type-II(ii) formal
  residual.
- Formal source-family tuples are not graphs, and the active existential question
  remains unanswered.
