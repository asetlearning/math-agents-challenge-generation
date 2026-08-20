---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
state: frozen-awaiting-lease
---

# Frozen A6 exact-computation manifest

- Exact command from vault root: `timeout 55s bash Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/run_a6_exact.sh`
- Software: Python 3.12.3 standard library; nauty/dreadnaut 2.8.8; shell `/bin/bash`.
- Resources: one CPU, estimated peak RAM below 256 MB, expected wall time below 10 s, hard outer timeout 55 s; requested lease duration 2 minutes.
- Mathematical input: `A6` as all 360 even permutations of six points; `D` as all 45 double transpositions; selected labels 2 and 3; full expected label set 2,3,4,5; zero-based deterministic lexicographic vertex indexing.
- Frozen hashes: generator `b23f6a8e09f6ff8a4957484eec3de527664ab9556a9a5e682f7603397746195a`; parameter input `e0b6ecf6752967c10a2d04009ce044ca3b0b5c89d36d04a3b4f6e5a893e966c5`; wrapper `61d85e072dc93ef60b60f63a1b508308438d030407d9c7380f12f73d1ecf2a6e`.
- Construction checks: `|A6|=360`; every listed vertex is a nonidentity involution; conjugation orbit under the enumerated `A6` equals all 45 vertices; complete symmetric 45-by-45 product-order matrix; uniform colour valencies.
- Two-colour graph: vertex-coloured incidence encoding with one cell for the 45 original vertices, one cell for 2-edge auxiliary vertices, and one cell for 3-edge auxiliary vertices. Its colour-preserving automorphisms restrict exactly to `Aut_2(Gamma) intersection Aut_3(Gamma)`.
- Full-colour graph: the same encoding with separate auxiliary cells for every occurring product order. Its restriction is exactly `Aut(Gamma)`.
- Dreadnaut settings: sparse nauty, fixed vertex partition, automorphism output enabled in permutation format.
- Output schema: `a6_build_summary.json`; `a6_vertices.json`; `a6_product_order_matrix.json`; the two generated `.dre` inputs; two nauty stdout/stderr files; pre-nauty and all-output SHA-256 manifests.
- Decision rule: if occurring colours number at most three, stop A6 as tautological and do not use the nauty comparison. Otherwise compare the two exact group orders. Strict inequality requires extracting a displayed two-colour generator that changes a 4/5 edge and then exhaustively checking that explicit permutation against the matrix. Equality is bounded evidence for this pair only.
- Independent certificate route: Validator can reconstruct the matrix directly from the cycle-notation vertex list, rerun the incidence encoding with another graph-automorphism implementation, and check any candidate permutation by a direct 990-pair loop without trusting nauty's group order.
