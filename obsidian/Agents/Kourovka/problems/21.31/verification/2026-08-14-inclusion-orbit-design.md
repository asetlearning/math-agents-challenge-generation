---
title: "Verification — Kourovka 21.31 — marked inclusion and embedding orbit design"
problem: "21.31"
claim: "Each fixed quotient block has one marked inclusion orbit above the point stabilizers, and regular embeddings require simultaneous transporter-preserving A_i x Aut(M) orbit classification."
claimant: Problem-21.31
target_object: "Regular subgroups of Hol(N) for arbitrary finite soluble N"
witness_object: "Nine conditional quotient blocks q:G->GL(3,2), inverse images of order-21 point stabilizers, and regular embeddings H->Hol(M)"
witness_equals_target: false
citation: "Byott, arXiv:2205.13464v4, Lemma 2.4 and Proposition 2.6"
verification_method: "Hand proof, semidirect-product calculation, GAP semantics audit, and independent GAP 4.12.1 subgroup computation"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.31 — inclusion orbit and embedding orbit design

## The claim

For each of the nine fixed quotient blocks (q:G\twoheadrightarrow T=GL_3(2)), the subgroups (q^{-1}(P)), as (P) ranges over point stabilizers in the fixed transitive degree-8 affine action of (T), form one marked-inclusion orbit. The later regular-embedding enumeration must use the simultaneous action of the diagram-induced restriction group (A_i) and `Aut(M)`, not all of `Aut(H)` and not raw GAP complement classes.

## Target vs witness

The target is the universal holomorph conjecture. These witnesses are only finite conditional data for hypothetical order 2016. Witness equals target is false. No target-level or order-2016 exclusion follows.

## Unique inclusion orbit

The independent computation finds exactly one conjugacy class of order-21 subgroups (P<T); it has eight members, index 8, and (N_T(P)=P\cong C_7:C_3). These are precisely the point stabilizers in the transitive degree-8 action.

Fix a surjection (q:G\to T) with kernel (K). If (P'=tPt^{-1}), choose any (g\in G) with (q(g)=t). Then inner conjugation satisfies

\[
q\circ c_g=c_t\circ q,
\qquad c_g(K)=K,
\qquad c_g(q^{-1}(P))=q^{-1}(P').
\]

Thus all inverse-image inclusions lie in one orbit under automorphisms of the marked quotient diagram that permit the simultaneous inner automorphism (c_t) of (T). This proof applies uniformly to every one of the nine quotient blocks and does not require constructing the blocks anew.

The wording matters: if “automorphism of `(G,K,q)`” were required to satisfy (q\phi=q) strictly, the displayed inner conjugacies would generally not qualify. The correct diagram group consists of compatible pairs

\[
D_i=\{(\phi,\tau):\phi\in Aut(G),\ \phi(K)=K,\ \tau\in Aut(T),\ q\phi=\tau q,\ \tau(P)=P\}.
\]

For the fixed representative (H=q^{-1}(P)), the allowed group is

\[
A_i=\operatorname{im}(D_i\to Aut(H)),\qquad(\phi,\tau)\mapsto\phi|_H.
\]

The unique inclusion orbit does not imply (A_i=Aut(H)). Generators and the faithful permutation/action representation of each of the nine (A_i) remain required certificate data.

## Crossed maps and complement graphs

For a fixed homomorphism (\lambda:H\to Aut(M)), let (E_\lambda=M\rtimes_\lambda H), with canonical complement (H_0=\{(1,h)}). The crossed identity

\[
c(xy)=c(x)\lambda(x)(c(y))
\]

is exactly the condition that

\[
C_c=\{(c(h),h):h\in H\}
\]

is a subgroup. Projection (C_c\to H) is an isomorphism, so (C_c) is a complement to (M). Conversely every complement projects isomorphically to (H) and is the graph of one crossed map.

The induced affine action has stabilizer of (1_M) equal to the elements with (c(h)=1), equivalently (C_c\cap H_0). Thus it is regular exactly when this intersection is trivial: then (c) is injective, and equal orders make it bijective.

## Required simultaneous equivalence

For (a\in A_i) and (u\in Aut(M)), the correct action is

\[
\lambda'(h)=u\lambda(a^{-1}h)u^{-1},
\qquad c'(h)=u(c(a^{-1}h)).
\]

This transports the entire holomorph embedding and the marked inclusion simultaneously. Replacing (A_i) by all of `Aut(H)` is unsound because an automorphism of (H) need not extend to the quotient diagram.

## GAP routine semantics and the missing transporter data

`AllHomomorphismClasses(H,Aut(M))` supplies action representatives modulo conjugacy in the target. When (a\in A_i) sends one action to a target-conjugate representative, a complete implementation must retain an explicit target transporter (u), not merely note equality of conjugacy classes. It must also retain the target-conjugacy stabilizer/centralizer of each action, because that stabilizer acts on its crossed maps.

`ComplementClassesRepresentatives(E,M)` returns complement representatives under conjugacy in the ambient semidirect product. Ambient conjugacy includes conjugation by (M), which changes crossed maps by coboundaries/translations. Translation is not an automorphism of the additive group fixing its identity and is not part of the required `Aut(M)` equivalence. Ambient conjugacy also includes canonical-(H) conjugacy; the corresponding inner automorphisms of (H) are allowed because they extend to (G), but this does not repair the forbidden (M)-conjugacy collapse.

Therefore raw complement-class representatives are too coarse. A certificate-ready implementation must do one of the following:

1. enumerate all crossed-map graphs explicitly and orbit them under (A_i\times Aut(M)); or
2. retain full complement transporters and stabilizers, decompose/expand ambient conjugacy classes enough to recover the exact required double-orbit set, and prove the reconstruction.

For every action stratum it must save:

- the explicit homomorphism and its chosen target-conjugacy representative;
- transporters induced by each relevant generator of (A_i);
- the stabilizer of the action inside (A_i\times Aut(M));
- complement/crossed-map representatives before any forbidden collapse;
- complement stabilizers and transporters;
- final orbit representatives, sizes, and a sum-of-orbit-sizes completeness check;
- commands, versions, checkpoints, sentinels, hashes, and verbatim output.

The restriction-map stage must then use these same transporters so that equality of (\lambda_H) with a restricted (G\to Aut(M)) is tested under the exact simultaneous equivalence, rather than under unrelated conjugacy choices.

## Circularity check

The point-stabilizer class is computed independently in (T). Regular embeddings must be enumerated before testing extendability and may not be constructed from extendable actions. Otherwise the restriction filter would pass by construction.

## Evidence

Command:

```text
timeout 20s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_point_stabilizer_orbit.g > Agents/Kourovka/problems/21.31/verification/scratch/independent_point_stabilizer_orbit.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
T_ID=[ 168, 42 ] T_SIZE=168
ORDER21_CONJUGACY_CLASSES=1
P_ID=[ 21, 1 ] P_DESC=C7 : C3 CLASS_SIZE=8 NORMALIZER_SIZE=21 INDEX=8
RUN_COMPLETE=true
```

```text
RUN_EXIT=0
SENTINEL_EXIT=0
c4b721e1b1b308d05cc7971a6f02e4e2802bbccc6ba8038cb13f1a8fdf2a0169  Agents/Kourovka/problems/21.31/verification/scratch/independent_point_stabilizer_orbit.g
fe7a40c97268a5a556bdb98ed9c144f53ed2216d68b099a04c21ed097025d04f  Agents/Kourovka/problems/21.31/verification/scratch/independent_point_stabilizer_orbit.out
```

The three reported timing probes are not verification evidence: two coarse zero counts and one timeout do not use the final simultaneous orbit relation and imply no eliminations.

## Verdict

`status/conjectured` overall. The unique marked-inclusion orbit claim is verified for each fixed quotient block, and the transporter-preserving regular-embedding orbit design is correct with the clarified diagram group above. No embedding classification or restriction-map elimination is yet certified.

## Why this verdict

The conjugacy lift and crossed-map/complement calculations are complete. The independent finite check confirms the single point-stabilizer class. But the nine groups (A_i), the regular-embedding orbits, and their transporter/stabilizer certificates have not been computed.

## What is NOT established

- The size or generators of any (A_i) are not established.
- No complete regular-embedding orbit count is established for any `(H,M)` pair by this audit.
- No timing-probe zero is certified as an elimination.
- No automorphism-component restriction test has been exhaustively completed.
- Order 2016 and Kourovka 21.31 remain open.

## What would upgrade it

Construct all nine diagram restriction groups (A_i), implement the transporter/stabilizer-preserving orbit algorithm above, and produce completion certificates for all 230 base `(H,M)` pairs before attaching the nine overgroups and running the restriction-map filter.
