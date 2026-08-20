---
title: "Kourovka 19.30 — post-A6 final 22-minute strategy disposition"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
outcome: PARK_RECOMMENDED
created_utc: 2026-08-17T16:51:44Z
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/problems/19.30/verification/2026-08-16T173818Z-a5-order60-fixed-target-partial.md
  - Agents/Kourovka/problems/19.30/verification/2026-08-17T152916Z-psl27-order168-zero-collision.md
  - Agents/Kourovka/problems/19.30/verification/2026-08-17T164155Z-a6-order360-zero-collision-v2.md
  - Agents/Kourovka/problems/19.30/verification/2026-08-16T164240Z-prime-power-separator-partial.md
---

# Post-A6 disposition

## Scope and obstruction

`scope_id`: `19.30/vanishing-order-simple-recognition`; revision `1`.

Exact target: for every finite group `G` and finite simple group `S`, decide whether
`|G|=|S|` and equality of the sets of orders of **actual vanishing elements under
ordinary irreducible complex characters** force `G` isomorphic to `S`.

Excluded are character-table equality without equality of the stated invariant,
equality of full element-order spectra, and pairs in which neither group is finite
simple.

The obstruction is now structural rather than computational. The reviewed A5 note
is a fixed-target hand argument; the PSL(2,7) and A6 notes are exact fixed-order
catalogue results; and the reviewed prime-power separator covers only simple targets
meeting four extra hypotheses. None supplies a parameter-uniform bridge from a
simple family's character zeros to **all** nonsimple same-order groups, nor a
complete treatment of nonisomorphic simple groups of the same order. The three
singleton misses are not a sample from which universality may be inferred.

These are internal reviewed records, not external citations. All family-level
mathematics mentioned below is **general mathematical knowledge, unverified** in
this no-web review.

## Required four-way comparison

### 1. Refine the same method — do not spend the 22 minutes

- **Idea:** instantiate the existing prime-power separator at one more simple
  target.
- **Why it might work:** a well-chosen prime could separate a target full Sylow
  order from every nonsimple group of that one order.
- **Cheap falsifier / kill:** kill immediately unless the allowed record already
  contains family-uniform Target-vanishing, CS-p, Aut-p, and a replacement for
  simple-order uniqueness. It does not.
- **Cost:** another singleton may fit 22 minutes only by reusing a catalogue;
  closing an infinite family does not.
- **Self-critique:** this would be a fourth local screen or another conditional
  instantiation, so it cannot change the universal obstruction.

### 2. Representation-changing counterexample pivot — structurally apt, not ready

- **Idea:** move from SmallGroups rows to a parametrized equal-order pair of simple
  Lie-type families, and compare symbolic formulas for their vanishing-order sets.
  A natural candidate from general knowledge (unverified) is the odd-characteristic
  type-`B_n`/type-`C_n` pair.
- **Why it might work:** an equal-order nonisomorphic simple pair automatically
  satisfies the order and simplicity rows; only the exact ordinary-character
  vanishing-order formula remains.
- **Cheap falsifier / kill:** one parameter-uniform order lying in exactly one of
  the two vanishing-order sets kills equality for that proposed subfamily.
- **Cost:** deriving both complete formulas, including exceptional parameters,
  requires Lie-type conjugacy and ordinary-character input far beyond 22 minutes;
  no such formula occurs in the allowed references.
- **Self-critique:** equal order or similar spectra do not imply equal vanishing
  orders. Without a complete formula this is only a motif, not a counterexample
  strategy permitted by the request.

### 3. Switch to a theoretical direction — promising representation, missing bridge

- **Idea:** encode `V_o(S)` by prime support of ordinary defect-zero characters,
  then compare that support with the possible minimal normal subgroups and quotient
  actions of a nonsimple same-order `G`.
- **Why it might work:** from general knowledge (unverified), an appropriate
  defect-zero character should force zeros on the corresponding prime-singular
  classes. This could replace the single-prime separator by a family-uniform menu
  of order witnesses.
- **Cheap falsifier / kill:** for a named family, fail the route if the proposed
  prime cover leaves even one element-order type untreated, or if a possible chief
  factor and its automorphism group absorb every proposed separator prime.
- **Cost:** at least a sourced defect-zero coverage theorem, its exception list,
  and a new chief-factor lemma are needed. No exact derivation of those inputs fits
  22 minutes under the present no-web/no-history restriction.
- **Self-critique:** prime divisibility is only a sufficient source of character
  zeros; it does not by itself determine the set of orders of vanishing elements.
  Confusing this support with the full invariant would repeat the metric/algebra
  mismatch the protocol warns against.

### 4. Selected action — `PARK_RECOMMENDED`

Preserve the remaining 22 problem minutes. There is no exact family formula or
family-uniform proof bridge in the allowed material, so none of the three
mathematically distinct routes has a bounded success certificate that fits the
remaining time. Lead should park revision 1 rather than start another singleton.

## Precise restart gate

Resume only when at least one of these externally groundable inputs is in hand:

1. **Counterexample gate:** a named infinite equal-order, nonisomorphic family
   `(G(t),S(t))`, with a source-grounded complete formula for both exact sets
   `V_o(G(t))` and `V_o(S(t))` under ordinary complex irreducible characters,
   including all parameter exceptions, and the formulas predict equality for a
   nonempty parameter range; or
2. **Proof gate:** a named infinite simple family `S(t)` with an explicit
   order-witness function `d(t)` and source-grounded ordinary-character input giving
   `d(t) in V_o(S(t))`, together with a uniform chief-factor argument giving
   `d(t) notin V_o(G)` for every nonsimple `G` of order `|S(t)|`, plus an explicit
   discriminator for every nonisomorphic simple order-twin.

After either gate passes, allocate a fresh family-level cycle. A finite target or a
formula for full spectra alone does not pass the gate.

## Planning probability

- Recommended `truth_likelihood`: keep `0.56`; the A5, PSL(2,7), and A6 results are
  selected finite subcases and give no calibrated universal update.
- Recommended `probability_of_substantial_progress` for the residual 22 minutes:
  `0.08` (down from `0.40`). This is a portfolio estimate driven by the absence of
  an admissible bounded family bridge, not by interpreting three zero-collision
  results as evidence for the universal assertion.

