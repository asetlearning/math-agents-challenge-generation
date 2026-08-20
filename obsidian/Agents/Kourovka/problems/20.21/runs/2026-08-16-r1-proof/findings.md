---
title: "Kourovka 20.21 clean constructive cycle: partial reductions"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/extensions
  - project/kourovka
  - status/conjectured
problem: "20.21"
scope_id: "20.21/two-index-twelve-kernels"
assignment_revision: 1
cycle_outcome: PARTIAL_RESULT
---

# Active target

Scope: `20.21/two-index-twelve-kernels`

Assignment revision: 1

Target statement: There exist a finite group G and normal subgroups K,L normal in G such that [G:K]=[G:L]=12, K is isomorphic to L, G/K is isomorphic to C_12, and G/L is isomorphic to A_4.

# Outcome

`PARTIAL_RESULT` — no witness and no proof of the active target.

# Eligible partial results

## 0. Necessary two-branch reduction for every target witness

For any hypothetical target triple and \(N=K\cap L\), Goursat's lemma gives exactly two possibilities:

- \(G/N\cong C_{12}\times A_4\), with \(K/N\cong A_4\) and \(L/N\cong C_{12}\); or
- \(G/N\cong C_4\times A_4\), with \(K/N\cong V_4\) and \(L/N\cong C_4\).

The second group is the fibre product of \(C_{12}\) and \(A_4\) over their unique common nontrivial quotient \(C_3\). Full proof: `scratch/original-goursat-reduction.md`.

## 1. Sufficient equivariant construction template

It is sufficient to find a finite group \(P\), epimorphisms
\[
f:P\twoheadrightarrow C_4,
\qquad
h:P\twoheadrightarrow V_4,
\]
with isomorphic kernels, and \(\sigma\in\operatorname{Aut}(P)\) of order three satisfying
\[
f\sigma=f,
\qquad
h\sigma=\tau h,
\]
where \(\tau\) cycles the nonzero elements of \(V_4\). Then
\[
G=P\rtimes_\sigma C_3
\]
maps onto \(C_4\times C_3\cong C_{12}\) and \(V_4\rtimes C_3\cong A_4\), with the two original kernels.

## 2. Clean equivariant Goursat reduction

Within that template, the combined map \((f,h):P\to C_4\times V_4\) must be onto. The only proper subdirect possibility is a fibre product over \(C_2\), but its order-two Goursat kernel in \(V_4\) cannot be invariant under the 3-cycle \(\tau\). Full proof: `scratch/equivariant-goursat-reduction.md`.

## 3. Exact bounded exclusion inside the template

One Lead-leased GAP 4.12.1 / SmallGrp 1.5.3 run exhaustively covered every SmallGroups-library group \(P\) of exact order 16, 32, or 64:

| exact order | library groups completed |
|---:|---:|
| 16 | 14 |
| 32 | 51 |
| 64 | 267 |

Across all 332 groups, 1,887 ordered pairs of normal index-four subgroups passed the quotient-type and exact kernel-isomorphism filters. None had an order-three automorphism stabilizing the pair, acting identically on the \(C_4\) quotient and nontrivially on the \(V_4\) quotient.

The exact command, complete stdout/stderr, exit status, runtime (110835 ms), exhaustivity argument for the Sylow-3 step, software versions, and limitations are in `log.md` under `## Leased computation 2`. Script: `scratch/search-equivariant-p.g`; SHA-256 `f476dab18c9ffa5f139e183f5bac831f6ab7efc96f64372e74940ca97bc25c1c`.

This excludes only the stated sufficient template at those three orders. It does not exclude \(|P|\ge128\), other constructive representations, or the original target.

## 4. Split elementary-abelian family exclusion

For every \(N\cong C_2^d\) and arbitrary actions, the split extensions \(N\rtimes V_4\) and \(N\rtimes C_4\) cannot be isomorphic. Equality of derived-subgroup orders would make the two coinvariant dimensions equal, while the Frattini quotients have generator dimensions differing by one. Full proof and limitations: `scratch/split-elementary-obstruction.md`.

## 5. Exact order-128 quaternion-kernel family exclusion

Inside the equivariant template, no \(|P|=128\) extension with combined-map kernel \(N\cong Q_8\) works. The outer action has only three types. In all of them the \(V_4\)-preimage has center \(C_2^3\) or \(C_2\), while the \(C_4\)-preimage has center \(C_2\times C_4\), \(C_8\), \(C_2^2\), or \(C_4\). Thus the preimages cannot be isomorphic. Full factor-set and center argument: `scratch/q8-order128-exclusion.md`.

## 6. Exact order-128 dihedral-kernel family exclusion

The same conclusion holds for combined-map kernel \(N\cong D_8\) of order eight. Since \(Out(D_8)\cong C_2\), the outer-action list is even shorter, and the same center alternatives are pairwise incompatible. Full proof: `scratch/d8-order128-exclusion.md`.

# What was actually computed in

The computation used exactly the GAP SmallGroups-library groups of orders 16, 32, and 64. It did not enumerate groups of order 128, all finite 2-groups, all finite groups, or groups \(G\) satisfying the original index-12 statement.

# Is that object the target?

No. The computed family is a bounded subset of a sufficient auxiliary template. A negative result there is not a negative answer to Kourovka 20.21.

# Constraint status

There is no candidate triple \((G,K,L)\). Therefore no required row is asserted to pass or be proved:

| constraint_id | current result |
|---|---|
| `20.21-exists-GKL` | not established |
| `20.21-G-finite` | no candidate to test |
| `20.21-KL-normal` | no candidate to test |
| `20.21-both-index-12` | no candidate to test |
| `20.21-kernels-isomorphic` | no candidate to test |
| `20.21-quotient-K-C12` | no candidate to test |
| `20.21-quotient-L-A4` | no candidate to test |
| `20.21-existence-conclusion` | not established |

# Quarantined non-evidence

Two unrostered helpers ran unapproved computations. Lead ordered all their outputs quarantined. The run log marks the affected hand subclaims as non-evidence, and the related Validator requests were withdrawn. Nothing from those helpers supports any eligible partial result listed above.

# Uncovered scope and next strategy

Both nonabelian order-eight kernels are now exhausted. The remaining exact order-128 choices are the abelian groups \(C_8\), \(C_4\times C_2\), and \(C_2^3\). The nonsplit \(C_2^3\) family is already parametrized in `scratch/nonsplit-order-128-family.md`, with its action-layer reduction in `scratch/order-128-action-layer.md`; it is now the preferred next bounded family. No new command has been written or run; any algebra-system search requires a fresh exact Lead lease.

# Staleness status

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. The rendered source, scope, clauses, and corpus flags were checked; no web or solution-bearing local history was inspected.
