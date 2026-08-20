---
title: "Verification — Kourovka 21.31 — automorphism-component restriction filter"
problem: "21.31"
claim: "In any compatible order-2016 realization, the automorphism component of the induced regular embedding H->Hol(M) extends along the actual inclusion H<G to G->Aut(M)."
claimant: MathExpert / Problem-21.31
target_object: "Regular subgroups of Hol(N) for arbitrary finite soluble N"
witness_object: "Marked inclusions H<G from nine conditional overgroups, all 46 order-252 additive groups M, and regular embeddings H->Hol(M)"
witness_equals_target: false
citation: "Byott, arXiv:2205.13464v4, Lemma 2.4 and Proposition 2.6"
verification_method: "Line-by-line holomorph proof, equivalence audit, and GAP 4.12.1 scope check"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "pdftotext 24.02.0"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.31 — restriction-map lift filter

## The claim

Suppose a compatible hypothetical order-2016 realization gives a regular embedding

\[
\beta_G=(c_G,r_G):G\hookrightarrow Hol(N),
\]

a G-invariant normal subgroup M in N, and H=M_*<G. The induced regular embedding `beta_H=(c_H,lambda_H):H->Hol(M)` has an automorphism component that extends along the actual inclusion `i:H->G` to a homomorphism `lambda_G:G->Aut(M)`.

## Target vs witness

The Kourovka target ranges over all finite soluble (N) and all regular subgroups of `Hol(N)`. This filter concerns only marked finite data forced by a hypothetical counterexample of order 2016. Witness equals target is false. It is a necessary filter, not an order-2016 exclusion and not a solution.

## Proof of the necessary condition

Because (M) is (G)-invariant, every automorphism (r_G(g)\in Aut(N)) preserves (M). Restriction therefore defines

\[
\lambda_G:G\longrightarrow Aut(M),\qquad
g\longmapsto r_G(g)|_M.
\]

Restriction of automorphisms respects composition, so this is a homomorphism. By Byott's Lemma 2.4, (H=M_*) acts on (M), and its induced holomorph embedding is obtained by restricting the original affine action. Consequently

\[
\lambda_G\circ i=\lambda_H.
\]

Thus failure of `lambda_H` to extend along the actual marked inclusion is a valid necessary obstruction.

The condition is not sufficient: it discards (c_H), the extension (1\to M\to N\to C_2^3\to1), the lift to automorphisms of (N), the fixed quotient affine action, and the global bijective crossed map.

## Correct finite classification problem

The atomic object is not an abstract homomorphism alone. It is marked data

\[
(G,K,q_G,P,H,i; M; \beta_H=(c_H,\lambda_H)),
\]

where:

1. `(G,K)` is one of the nine verified conditional pair classes and (q_G:G\to T=GL_3(2)) is a quotient identification;
2. (P<T) is the point stabilizer in the fixed degree-8 affine realization;
3. (H=q_G^{-1}(P)), with its actual inclusion (i:H\hookrightarrow G); all inequivalent marked inclusion orbits must be represented;
4. (M) is one of all 46 groups `SmallGroup(252,j)`—the light check confirms all 46 are soluble;
5. `beta_H` is a regular embedding, meaning `c_H:H->M` is bijective and obeys
   \[
   c_H(xy)=c_H(x)\lambda_H(x)(c_H(y)).
   \]

The nine overgroups already determine which of the five (H)-types occurs. The raw universe is therefore nine overgroup blocks times 46 additive types, refined by every marked-inclusion orbit and every regular-embedding orbit—not an unrestricted Cartesian product of five (H)'s with all nine (G)'s.

## Correct equivalence relation

Two marked tuples are equivalent only when there are isomorphisms

\[
\phi:G\to G',\qquad \psi:M\to M'
\]

such that:

- `phi` preserves K, transports the chosen quotient/point-stabilizer data as allowed, and maps the marked subgroup H and inclusion to H'<G';
- conjugation by `psi` on holomorphs transports the entire regular embedding, including both `c_H` and `lambda_H`, to the embedding precomposed by `phi|H`;
- when extension maps `lambda_G` are recorded, the same `phi,psi` transport them.

Equivalently, orbit the inclusion and regular embedding simultaneously under the automorphisms of the whole marked diagram. Quotienting regular embeddings independently by all of `Aut(H)`, and then attaching a single chosen inclusion (H<G), is not sound: an automorphism of (H) need not extend to the marked overgroup.

## Complete enumeration of regular embeddings

For each `(H,M)`:

1. enumerate a proved-complete set of homomorphisms `lambda:H->Aut(M)`, initially with explicit maps rather than only unlabeled images;
2. for each action, enumerate all crossed maps (c:H\to M) satisfying the cocycle identity and bijectivity;
3. equivalently, enumerate complements (graphs) in (M\rtimes_\lambda H), and retain those acting regularly on (M), but state exactly which conjugacy relation the GAP complement routine uses;
4. quotient by the stabilizer of `lambda` in `Aut(H) x Aut(M)` and then by the simultaneous marked-diagram equivalence above.

A complement-class list up to conjugation by (M) is not by itself the final `Aut(H) x Aut(M)` orbit list. Conversely, starting only from homomorphism-class representatives can miss an exact restriction match unless conjugacy and stabilizers are carried explicitly.

## Restriction-image test

For every surviving marked tuple, solve

\[
\Lambda:G\to Aut(M),\qquad \Lambda\circ i=\lambda_H.
\]

It is permissible to solve equality up to `Aut(M)` conjugacy only when the same conjugacy is applied to the full regular embedding and accounted for in the simultaneous equivalence relation. The result must record either:

- an explicit extending homomorphism `Lambda` on generators, with all relations and the restriction checked; or
- a proved-exhaustive finite candidate list and a transcript showing every candidate fails.

An extending `Lambda` is only a survivor of this filter. It need not lift to `Aut(N)` and need not be compatible with `c_H`.

## Exhaustive negative certificate requirements

To claim that this filter eliminates every hypothetical order-2016 realization, a certificate must contain:

1. all nine explicit `(G,K)` representatives, quotient maps to (T), and a complete orbit list of compatible marked inclusions (H<G);
2. all 46 order-252 (M) identifiers and proof that the list is complete;
3. for every resulting `(G,H,M)` block, counts and canonical representatives for all regular-embedding orbits, with the action/cocycle or complement-to-embedding bijection proved;
4. exact stabilizers and orbit sizes showing no embedding was lost or counted twice under simultaneous equivalence;
5. for every representative, the complete restriction-map computation, including explicit maps or exhaustive failures;
6. zero survivors across the full marked universe;
7. scripts, versions, commands, exit codes, completion sentinels, hashes, and verbatim outputs.

If even one automorphism component extends, the filter is inconclusive for that tuple and the downstream additive-extension/action/crossed-map layers remain necessary. A timeout, sample, first representative, or search with an unproved orbit universe is not a negative certificate.

## Circularity check

The nine group-side classes and 46 SmallGroups objects are external inputs. Regular embeddings must be generated independently through complete action/cocycle data, not manufactured from extendable homomorphisms. Otherwise the restriction test would pass by construction and prove nothing.

## Evidence

Light scope command:

```text
timeout 20s gap -q Agents/Kourovka/problems/21.31/verification/scratch/restriction_filter_scope.g > Agents/Kourovka/problems/21.31/verification/scratch/restriction_filter_scope.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
SMALLGRP_VERSION=1.5.3
NUMBER_SMALL_GROUPS_252=46
SOLUBLE_GROUPS_252=46 IDS=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
  34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46 ]
H_TYPES=[ [ [ 252, 17 ], "(C3 : C4) x (C7 : C3)" ], 
  [ [ 252, 19 ], "C12 x (C7 : C3)" ], [ [ 252, 27 ], "A4 x (C7 : C3)" ], 
  [ [ 252, 29 ], "C2 x (S3 x (C7 : C3))" ], 
  [ [ 252, 38 ], "C2 x C6 x (C7 : C3)" ] ]
ABSTRACT_OVERGROUP_PAIR_CLASSES=9
MARKED_INCLUSION_CLASSES=NOT_COMPUTED
RUN_COMPLETE=true
```

```text
RUN_EXIT=0
SENTINEL_EXIT=0
7e089fffeefe5b6e436feb6b479a036b38310fd5b2fe38eef36d8dc65f5e5e44  Agents/Kourovka/problems/21.31/verification/scratch/restriction_filter_scope.g
b6ac2bea34fecb8ee7de9cb47c61c13ff89b88e32cc2119919323413d00b762f  Agents/Kourovka/problems/21.31/verification/scratch/restriction_filter_scope.out
```

## Verdict

`status/conjectured` overall. The automorphism-component extension condition is mathematically sound as a necessary filter on correctly marked tuples. No exhaustive restriction computation has yet been performed, so no pair, overgroup, or order-2016 realization is eliminated by this audit.

## Why this verdict

The proof of necessity is direct, and the corrected scope includes all 46 possible additive groups. However, completeness additionally requires simultaneous classification of marked inclusions and regular embeddings. Those inclusion orbits and embedding orbits are not presently certified.

## What is NOT established

- No restriction-map failure or survivor count is established.
- No overgroup or additive group is eliminated.
- Order 2016 is not excluded and no target realization is constructed.
- Extending an automorphism component does not establish a compatible (N), action on (N), translation component, or bijective crossed map.
- Kourovka 21.31 remains open.

## What would upgrade it

Produce the complete marked-universe certificate specified above. Any survivors must proceed to equivariant nonabelian extension classification and full crossed-map lifting; zero survivors would give a finite conditional exclusion of order 2016, still not a universal solution.
