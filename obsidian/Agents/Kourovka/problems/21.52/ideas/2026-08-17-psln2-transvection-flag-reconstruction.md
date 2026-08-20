---
title: "21.52 strategy — reconstruct projective incidence from PSL_n(2) transvections"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
strategy_id: LIN2-TRANSVECTION-FLAG
direction_recommendation: proof
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - topic/projective-geometry
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-a5-equality.md
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-psl27-equality.md
---

# Recommendation

SCOPE: `21.52/involution-class-product-order-colouring`  
REVISION: `1`  
TARGET: every finite nonabelian simple `L` and every single involution class `D`.  
EXCLUDED: Problem 21.53, unions of involution classes, the uncoloured graph,
conjugacy-class colouring, and any bounded-family inference to the universal
assertion.

Switch the next increment from counterexample-first to the proof direction, using
exactly one strategy: `LIN2-TRANSVECTION-FLAG`. The objective is an infinite-family
partial result for the transvection class in
\(L=\operatorname{PSL}_n(2)=\operatorname{GL}_n(2)\), \(n\geq3\), by recovering
the point--hyperplane incidence geometry intrinsically from colour 2. The two fixed
positive cases motivate the pivot but do not support a universal inference.

All mathematical content in the proposed family argument is **general knowledge,
unverified**; no literature claim or citation is asserted.

## Obstruction

The universal difficulty is not computing another finite colour group. It is
showing that the coarse invariant \(|ab|\) still remembers a canonical geometry
from which the group action can be reconstructed. A further isolated small case
would give little information about that mechanism.

## The one strategy

Let \(V=\mathbf F_2^n\). Parametrize the rank-one transvection class by incident
point--hyperplane flags

\[
t_{u,f}=I+u\otimes f,\qquad u\ne0,\quad f\ne0,\quad f(u)=0,
\]

where scalar ambiguity disappears over \(\mathbf F_2\). For two distinct flags
\((u,f),(v,g)\), set \(a=f(v)\) and \(b=g(u)\). Rank-one multiplication should give

| `(a,b)` | proposed product order |
|---|---:|
| `(0,0)` | 2 |
| `(1,1)` | 3 |
| exactly one is `1` | 4 |

Thus colour 2 is mutual cross-incidence. For each nonzero proper subspace
\(U<V\), define

\[
K_U=\{(P,H):P\leq U\leq H\}.
\]

The key proposed reconstruction lemma is:

1. every maximal colour-2 clique is exactly one \(K_U\);
2. if \(r=\dim U\), then
   \(|K_U|=(2^r-1)(2^{n-r}-1)\);
3. the minimum-size maximal cliques are precisely `point stars`
   \(K_P\) and `hyperplane stars` \(K_H\) (for \(n=3\), these are all possible
   dimensions);
4. their nonempty-intersection graph is the point--hyperplane incidence graph of
   \(\mathrm{PG}(n-1,2)\), determined up to swapping its two parts, and each
   original flag is the unique intersection \(K_P\cap K_H\).

The mechanism behind item 1 is short: for a colour-2 clique `C`, span all its point
coordinates to obtain `U`; mutual incidence puts `U` inside every hyperplane
coordinate, so `C` lies in `K_U`, and maximality should force equality. For item 3,
compare the displayed size at `r=1,n-1` against every
`2 <= r <= n-2`.

From general mathematical knowledge (unverified), the fundamental theorem for
projective incidence geometry then makes every reconstructed incidence
automorphism either linear or a correlation. Linear maps act on `D` by conjugation;
a fixed duality is induced by the group automorphism
\(x\mapsto(x^{-1})^{T}\). Hence every full colour automorphism should be induced
by an automorphism of `L` for this entire family. This would be an infinite-family
`PARTIAL_RESULT`, never an answer to the universal scope.

## First increment — hard stop at 40 active minutes

No computation and no heavy slot.

1. `0--8 min`: write the flag parametrization, justify that it is one conjugacy
   class, and record why `PSL_n(2)=GL_n(2)` is admissible for `n>=3`.
2. `8--18 min`: derive the three product orders by algebra with
   `A=u tensor f`, `B=v tensor g`; include the nilpotence calculation in the
   asymmetric case and exclude equal vertices.
3. `18--32 min`: give a two-inclusion classification of maximal colour-2 cliques
   as `K_U`, compute their sizes, and prove the endpoint dimensions are the unique
   minima when `n>=4` (with `n=3` stated separately).
4. `32--40 min`: reconstruct the bipartite incidence graph from the minimum
   maximal cliques and write the gate outcome. Stop at 40 minutes even if a later
   realization step remains unwritten.

SUCCESS ARTIFACT:
`Agents/Kourovka/problems/21.52/psln2-transvection-flag-reconstruction.md`, containing
the exact product table, the maximal-clique classification, the size inequality,
and the reconstructed incidence graph, each with quantified hypotheses.

FAILURE ARTIFACT:
`Agents/Kourovka/problems/21.52/psln2-transvection-flag-obstruction.md`, naming the
first failed gate and giving an explicit offending pair or clique. A vague
"classification seems hard" report does not satisfy the artifact gate.

## Hard gates and kills

- `G0 — admissibility`: if the displayed transvections are not one conjugacy class
  in an admissible simple `PSL_n(2)` for every stated `n`, narrow the family before
  continuing; do not report the advertised family.
- `G1 — order table`: one explicit distinct pair whose order disagrees with the
  three-row table kills this strategy immediately.
- `G2 — intrinsic reconstruction`: one maximal colour-2 clique not of the form
  `K_U`, or an interior dimension tying or beating the endpoint clique size, kills
  the incidence-recovery mechanism. Do not replace it with an `n`-by-`n` catalogue.
- `G3 — realization`: after a successful first increment, continue only if the
  projective-incidence automorphism theorem is stated with all hypotheses and each
  type-preserving/type-swapping action is explicitly realized by conjugation or
  inverse-transpose on `D`. Failure by 90 total active minutes kills the family
  claim.
- `G4 — scope`: even if `G0--G3` pass, the universal row
  `21.52-forall-L-D` remains uncovered. The maximum outcome is `PARTIAL_RESULT`
  unless a separate argument treats all simple groups and involution classes.

## Self-critique

The likely weak point is not the rank-one order calculation but the transition
from reconstructed incidence to a fully typed group automorphism, especially the
statement of the projective-geometry theorem and low-dimensional exceptional
isomorphisms. That is why `G3` is separate and time-capped. The strategy also says
nothing about higher-rank involutions in the same groups or other simple families;
its value is a reusable reconstruction mechanism, not coverage by extrapolation.

## Planning estimate

Updated likelihood that the **universal assertion** holds: `0.66` (from `0.62`).
The increase is deliberately small: the two reviewed fixed cases are positive and
the flag model exposes an exact family-facing route, but neither controls other
involution classes or other finite-simple families. This is a scheduling estimate,
not a mathematical claim. `active_assignment_answered: no`.
