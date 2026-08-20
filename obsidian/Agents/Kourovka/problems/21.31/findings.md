---
title: "Kourovka 21.31 — conditional reduction at order 2016"
problem_id: "21.31"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/holomorphs
  - project/kourovka
  - status/conjectured
---

# Conditional first-order reduction

## The claim

If Problem 21.31 has a counterexample of order 2016, its forced subgroup is one of the five verified direct products \(H=K\times(C_7:C_3)\), and its overgroup \((G,K)\) belongs to exactly nine distinguished central-extension orbits: a split class for each of the five order-12 radicals, and a nonsplit Schur-pushout class for each radical except \(A_4\).

## What I computed in

I computed in GAP 4.12.1:

1. all five isomorphism types `SmallGroup(12,i)`, `i=1,...,5`, including center, automorphism-group order, inner-automorphism-group order, and outer-automorphism-group order;
2. all 46 isomorphism types `SmallGroup(252,i)`, testing every normal subgroup \(K\) of order 12 and retaining exactly those for which `FactorGroup(H,K)` has ID `[21,1]`, the nonabelian group \(C_7:C_3\).

Scripts: `Agents/Kourovka/problems/21.31/scratch/order12_radicals.g` and `Agents/Kourovka/problems/21.31/scratch/order252_stabilisers.g`.

## Is that object the target?

No. These finite families are necessary subobjects of a *hypothetical counterexample of order 2016*, derived using Byott's Theorem 3.2. They are not the full target quantified over all finite soluble \(N\). It is unknown whether any of the nine pairs lifts to a counterexample; no such lift was computed.

## Argument / evidence

Tsang–Qin exclude all counterexamples of order at most 2000. Byott, Theorem 3.2(i), says a minimal counterexample has a soluble normal subgroup \(K\) with quotient \(T\cong\mathrm{GL}_3(2)\), and all maximal normal subgroups of \(N\) have index 2. Since regularity gives \(|G|=|N|\) and \(|T|=168\), 2016 is the first arithmetically possible order after 2000.

At order 2016, \(|K|=12\). Moreover \(K=R(G)\): the soluble radical contains \(K\), and its image in the simple insoluble quotient \(G/K\) is trivial. Conjugation gives a map \(T\to\operatorname{Out}(K)\). The complete order-12 computation gives outer-automorphism orders 2, 4, 2, 2, 12, respectively, so simplicity of \(T\) forces this map to be trivial. Therefore \(G=K C_G(K)\), with intersection \(K\cap C_G(K)=Z(K)\) and quotient \(C_G(K)/Z(K)\cong T\).

Byott's quotient construction then supplies \(M\trianglelefteq N\) with \(N/M\cong C_2^3\). Thus \(|M|=252\), and \(H=M_*\) acts regularly on \(M\), contains \(K\) normally, and has quotient the order-21 point stabiliser \(C_7:C_3\) in the transitive degree-8 action of \(T\). The exhaustive order-252 run found exactly these nine pairs:

```text
([252,2],[12,2]), ([252,9],[12,5]), ([252,11],[12,5]),
([252,17],[12,1]), ([252,19],[12,2]), ([252,27],[12,3]),
([252,29],[12,4]), ([252,38],[12,5]), ([252,40],[12,5]).
```

Exact commands and verbatim full outputs, including GAP's static syntax warning, are recorded in `Agents/Kourovka/problems/21.31/log.md`. The commands were:

```bash
timeout 30s gap -q 'Agents/Kourovka/problems/21.31/scratch/order12_radicals.g'
timeout 60s gap -q 'Agents/Kourovka/problems/21.31/scratch/order252_stabilisers.g'
```

Index-8 compatibility adds \(H=K C_H(K)\), because \(H\) is the inverse image of the point stabiliser in \(G/K\). The exact script `scratch/index8_group_side_filter.g` rejects `[252,11]` and `[252,40]`, where \(|K C_H(K)|=84\), and retains:

```text
([252,2],[12,2]), ([252,9],[12,5]), ([252,17],[12,1]),
([252,19],[12,2]), ([252,27],[12,3]), ([252,29],[12,4]),
([252,38],[12,5]).
```

Validator's verified central-pullback refinement further forces \(H\cong K\times(C_7:C_3)\), eliminating `[252,2]` and `[252,9]` and leaving `[252,17]`, `[252,19]`, `[252,27]`, `[252,29]`, `[252,38]`.

Since \(T\) is perfect with multiplier \(C_2\), central extensions by \(Z(K)\) are parametrized by \(Z(K)[2]\); quotienting by `Aut(K)` gives respectively 2, 2, 1, 2, 2 orbits for the five radicals, hence nine distinguished \((G,K)\) classes. The nonsplit representative is `(K x SL(2,7))/<(z,s)>` for a nontrivial central involution \(z\) and the central involution \(s\) of `SL(2,7)`.

## What this does NOT establish

It does not establish the conjecture, disprove it, exclude order 2016, construct a counterexample, classify groups \(N\) of order 2016, or prove that any of the nine overgroup classes acts compatibly on such an \(N\) or admits a bijective crossed map. GAP's library does not contain the groups of order 2016, and neither Magma nor Sage is installed.

## Marked diagram automorphisms

For an overgroup class represented by \(z\in Z(K)[2]\), the restriction group acting on \(H=K\times(C_7:C_3)\) is

\[
A_i=\operatorname{Stab}_{\operatorname{Aut}(K)}(z)\times\operatorname{Aut}(C_7:C_3).
\]

The nine orders are `504, 504, 168, 168, 1008, 504, 504, 504, 168` in the class order recorded in the log. Concrete generator maps are constructed by `scratch/diagram_restriction_groups.g`. This determines the exact simultaneous equivalence action needed for certificate-ready regular-embedding orbits, but does not enumerate those orbits.

## How I could be wrong

1. I may have misapplied the exact minimality notion in Byott Theorem 3.2 when passing to the order-8 quotient; Validator should check that the chosen \(M\) and the point-stabiliser statement apply exactly as stated.
2. The identification of the degree-8 point stabiliser with `SmallGroup(21,1)` depends on the transitive \(\mathrm{GL}_3(2)\) action in Byott's construction; an action mismatch would invalidate the nine-pair filter.
3. The deduction \(G=K C_G(K)\) uses the standard factorisation of the conjugation action through \(G/K\to\operatorname{Out}(K)\); a hidden failure of that factorisation would break the central-product conclusion.
4. The GAP enumeration is exact only for the installed SmallGroups data and GAP 4.12.1. Although `NumberSmallGroups(252)=46` and the loop completed, independent reproduction is still required.

Verified by [[Agents/Kourovka/problems/21.31/verification/2026-08-11-order-2016-nine-pair-reduction]].
