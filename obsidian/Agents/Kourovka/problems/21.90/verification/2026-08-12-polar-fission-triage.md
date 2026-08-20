---
title: "Verification triage — Kourovka 21.90 — polar fission"
problem: 21.90
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
---

# Claim

No vertex-transitive distance-regular graph with intersection array `{39,25,10;1,5,30}` has the explicitly constructed 300-vertex perpendicularity graph on nonsquare-type projective points of `Q(x)=x1*x2+x3*x4+x5^2` over `GF(5)` as its distance-3 graph.

# Target vs witness

The source-PDF target (page 177) asks whether any Q-polynomial distance-regular graph of diameter 3 can have both distance-2 and distance-3 graphs strongly regular. The computational witness is one exact `srg(300,65,10,15)`, the standard polar perpendicularity graph, together with subgroups of its computed full automorphism group. The witness is not the full target: the claim intentionally addresses only the stated intersection array, this constituent, and vertex-transitive realizations. Within that bounded claim, the constructed adjacency relation is the witness being classified; identification with a named polar graph is not needed for the finite exclusion.

# Sub-claims

1. The source statement is the Kourovka problem actually under discussion.
2. The explicit quadratic-space construction gives a 300-vertex `srg(300,65,10,15)`.
3. GAP/GRAPE computes its full automorphism group `G`, with derived subgroup `D` of index two and `D` represented by the complete table of marks `S4(5)`.
4. Every transitive `H <= G` has `H cap D` transitive or with two 150-point orbits.
5. The table-of-marks and outer-extension enumeration covers every such `H`, up to harmless conjugacy/duplication.
6. Every `H`-invariant undirected valency-39 graph disjoint from `A3` is an orbital union considered by the search.
7. The necessary identity `A1*A3=10*A2+9*A3` is implemented correctly and rejects all candidates.
8. These facts imply only the bounded claim, not nonexistence of asymmetric fissions, fissions of another nonisomorphic SRG, or a solution of 21.90.

# Tools available

- GAP 4.12.1 (`/usr/bin/gap`), with GRAPE, TomLib, and AtlasRep loading successfully.
- Python 3.12.3.
- Poppler `pdftotext` 24.02.0.
- Sage and Magma are not installed.

# Methods inventory

- Source-PDF extraction checks sub-claim 1; it does not validate the bounded reduction.
- Direct finite adjacency counts check sub-claim 2; they do not establish uniqueness among SRGs with these parameters.
- GAP automorphism and table-of-marks computations check sub-claims 3 and 5, conditional on the package algorithms/data; a pass does not identify the witness with every SRG of the same parameters.
- A hand index-two argument checks sub-claim 4; it does not enumerate extensions.
- An independently written orbital-union checker addresses sub-claims 5–7; agreement can support `replicated`, but cannot promote the full Kourovka problem.
- Matrix-algebra derivation checks that the tested identity is necessary; a pass of the identity would not be sufficient for a distance-regular graph, while failure is sufficient to reject a candidate.

# Hard limits

No installed tool proves uniqueness of `srg(300,65,10,15)`, and the claim does not assert it. The computation cannot address asymmetric realizations or the convention ambiguity concerning trivial/imprimitive examples such as the cube. Package-level correctness is treated as an external computational dependency.

# Recommendation

Full verification of the bounded finite claim is feasible. The maximum permissible verdict applies only to that bounded claim; the status of Problem 21.90 remains conjectured/open.
