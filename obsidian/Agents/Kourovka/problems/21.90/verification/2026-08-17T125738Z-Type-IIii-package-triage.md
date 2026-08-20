---
title: "Verification triage — Kourovka 21.90 — Type-II(ii) package"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 3
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
---

# Verification triage — Kourovka 21.90 — Type-II(ii) package

## Claim restated

Within the submitted primitive non-Taylor master parameterization, all local
degree-sum handshakes are claimed equivalent to `ta` even; this condition is
claimed to exclude an explicit infinite odd-`x,w` Type-II(ii) formal-parameter
subfamily, while the complementary even-`xw` residual is claimed formally
self-dual and unobstructed by the parity reduction of its zero-Krein
triple-intersection equations.

This is a candidate parameter-family partial only.  It neither constructs a graph
nor proves nonexistence for the revision-3 existential target.

## Locked scope and clause matrix

- `scope_id`: `21.90/diameter-three-distance-graphs`
- `assignment_revision`: 3
- exact active target: Does there exist a Q-polynomial distance-regular graph
  `Gamma` of diameter 3 such that `Gamma_2` and `Gamma_3` are nontrivial strongly
  regular graphs under the source-operational three-eigenvalue convention?
- excluded scopes: none in the canonical record; revision 2's disconnected cube
  candidate is superseded and out of scope under revision 3.

| source clause | active | submitted package answers it? |
|---|---:|---:|
| Definition of `Gamma_i` on the same vertex set with adjacency at distance `i` | yes | no; used only as ambient association-scheme language |
| Existence of a diameter-3 Q-polynomial distance-regular `Gamma` with both required distance graphs strongly regular | yes | no |

`active_assignment_answered: pending` during triage.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate/proof use | triage result |
|---|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | one graph satisfying all rows | no graph is supplied | unknown |
| `21.90-diameter-3` | admissibility | diameter exactly 3 | formal diameter-3 array only | unknown for any graph |
| `21.90-Q-polynomial-distance-regular` | admissibility | Q-polynomial distance-regular graph | formal feasibility data only | unknown for any graph |
| `21.90-distance-graph-definition` | admissibility | `Gamma_i` is exact distance relation | association-scheme relations are used conditionally | no candidate graph to check |
| `21.90-Gamma2-strongly-regular` | admissibility | nontrivial SRG in revision-3 sense | assumed in source-family reduction, not witnessed | unknown |
| `21.90-Gamma3-strongly-regular` | admissibility | nontrivial SRG in revision-3 sense | assumed in source-family reduction, not witnessed | unknown |
| `21.90-existence-conclusion` | target conclusion | at least one such graph exists | expressly not claimed | unproved |

No revision-3 `claim-checks/*.json` accompanies Lead's request.  The only present
claim check is the superseded revision-2 cube candidate and has
`ready_for_validator:false`.  This prevents promotion of the submitted package as
a current full-scope claim, independently of the algebraic audit below.

## Target versus witness

- source target: an actual Q-polynomial distance-regular graph satisfying every
  revision-3 row, read from the rendered Notebook page 177;
- submitted witness: symbolic parameter tuples and a formal 3-class eigenmatrix;
- witness equals target: false as stated.  A feasible formal parameter tuple is not
  an existing graph, and the package makes no such identification.

## Subclaims

1. The master array and equation imply the stated sphere sizes, induced degrees,
   and handshake equivalence.
2. Each of the four Type-I/II substitutions reproduces the master equation and has
   the claimed parity consequence.
3. The odd-`x,w` Type-II(ii) formula gives infinitely many distinct positive
   square-condition solutions and each fails a necessary graph handshake.
4. The even-`xw` residual has the stated exact 2-adic branches and infinite sample
   families.
5. Its adjacency multiplicities and eigenmatrices satisfy the claimed identities,
   including `P=Q` in the correct normalization.
6. The listed zero-Krein support is complete and gives exactly the stated
   nontrivial triple-intersection identities.
7. The claimed mod-2 reduction is valid and justifies the limited strategy claim
   that this primitive parity gate excludes no even branch.
8. The witness is the active target.  This subclaim fails by design: only a partial
   necessary-condition analysis is submitted.

## Tools and methods inventory

- source comparison: rendered PDF page 177 plus `pdftotext 24.02.0`; proves target
  fidelity, not the revision-3 convention by itself;
- hand substitution and polynomial identities: can prove exact conditional
  identities, but cannot prove existence of a graph or completeness beyond the
  stated master/source families;
- hand parity and valuation arguments: can prove necessary congruences and validate
  explicit infinite Diophantine families, but not graph realizability;
- association-scheme orthogonality and intersection-number recurrences: can check
  multiplicities, self-duality, and zero support, but formal feasibility is not
  existence;
- standard triple-intersection marginal/Krein identities: can check the equations
  and their parity consequences, but a satisfied parity consequence is only a
  necessary-condition pass;
- Python 3.12.3 is available for optional small exact-arithmetic spot checks only;
  GAP 4.12.1 is installed but every GAP call is heavy under the common protocol and
  is neither needed nor authorized here; Sage and Magma are absent.

## Hard limits and recommendation

Proceed with a hand-only, independent algebra audit.  Return an exact conditional
partial verdict for the odd family and a separate strategy verdict for the even
residual.  Keep `active_assignment_answered:no`; do not infer existence or
nonexistence of the target graph from formal feasibility, parity, or zero-Krein
necessary conditions.
