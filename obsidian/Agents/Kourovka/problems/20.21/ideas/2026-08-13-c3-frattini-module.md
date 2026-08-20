---
title: "20.21 idea — C3 action on the Frattini module"
problem: 20.21
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/finite-groups
  - project/kourovka
  - status/conjectured
---

# Ranked idea: reduce to a constrained 2-group with a `C3`-action

## Obstruction

The catalogue search measures ambient order, while the real obstruction is extension-theoretic: an abstract isomorphism `K ≅ L` need not carry `K ∩ L` to itself. Consequently the visibly different quotients `K/(K∩L) ≅ V4` and `L/(K∩L) ≅ C4` do not themselves separate `K` and `L`.

## The idea

By Conder–Maslova's minimal-counterexample proposition, pass to a least-order example and put `M=KL`, `N=K∩L`. Then `M` is a `2`-group, `[G:M]=3`, and `G/N ≅ C4 × A4`; hence `M/K ≅ C4` and `M/L ≅ V4`. A Sylow `3`-subgroup acts on `M`: it acts trivially on `M/K`, while its induced action on `M/L ≅ V4` is the nontrivial order-three action.

Study the Frattini module `V=M/Φ(M)` as an `F2[C3]`-module. The two quotient maps force, respectively, a trivial one-dimensional quotient and the irreducible two-dimensional quotient. Thus a candidate `V` must contain both module types. The proposed next step is to derive the induced Frattini quotients of `K` and `L` from the two kernels and test whether their dimensions or `C3`-fixed-point dimensions must differ. If they do, `K ≅ L` is impossible. If the first layer does not separate them, repeat on the Jennings/Frattini layers `Φ_i(M)/Φ_{i+1}(M)`; coprime `C3`-action makes every layer semisimple.

## Why it might work

- **Cited:** M. Conder and N. V. Maslova's proposition, recorded in N. V. Maslova, “2023 Ural workshop on group theory and combinatorics,” *Trudy Instituta Matematiki i Mekhaniki UrO RAN* 30(1) (2024), 284–293, gives the minimal-case reduction above.
- **General knowledge, unverified:** Schur–Zassenhaus supplies a complement of order `3` to the normal `2`-group `M`.
- **General knowledge, unverified:** Since `char(F2)` does not divide `3`, Maschke's theorem decomposes each `F2[C3]` layer into trivial one-dimensional and irreducible two-dimensional summands.
- This targets a structural asymmetry already visible in every computed near miss (different kernel abelianizations), but asks whether that asymmetry is forced rather than extrapolating from the catalogue.

## Cheap falsification criterion

Enumerate `2`-groups `M` only through order `256` (or the largest cheap SmallGroups range), their order-three automorphisms, and invariant normal index-four pairs `(K,L)` with quotient actions `C4`-trivial and `V4`-irreducible. If any pair has `K ≅ L`, or even matching Frattini-layer module data, the proposed first-layer obstruction is dead and the output becomes a focused construction target. This search is narrower and structurally parameterized; it is not another bound on arbitrary ambient `G`.

## Cost

About 1–2 hours: 30–45 minutes for the module lemmas and 30–75 minutes for a bounded GAP falsification screen. A run over all groups of order `256` may require a leased heavy slot; the proof-side layer calculation does not.

## Self-critique

The likely failure is that abstract group isomorphism forgets the ambient `C3`-action: `K` and `L` may be isomorphic even when their embeddings, fixed-point spaces, or induced module structures differ. Even the ordinary Frattini dimensions may coincide while only the equivariant data separates them, which would not contradict `K ≅ L`. The idea is therefore ranked as a falsifiable structural route, not as an obstruction already obtained.

