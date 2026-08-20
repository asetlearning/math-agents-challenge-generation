---
title: "Verification triage — Kourovka 21.31 — marked inclusion and embedding orbit design"
problem: "21.31"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 21.31 — marked inclusion and embedding orbit design

## Claim

For each of the nine verified quotient blocks (q:G\to T), the inverse images of point stabilizers in the fixed degree-8 action form one marked-inclusion orbit, while regular embeddings must be classified under the simultaneous action of the restriction image of diagram automorphisms and `Aut(M)`, retaining complement transporters and stabilizers.

## Target vs witness

The target is the universal holomorph conjecture. The witnesses are nine conditional order-2016 quotient blocks, their order-252 subgroups, 46 possible additive groups, and regular embeddings. Witness equals target: false; the audit can validate only the finite conditional design and remains `status/conjectured`.

## Sub-claims

1. The point stabilizers (P<T=GL_3(2)) in the degree-8 affine action form one conjugacy class.
2. Conjugacy (P'=tPt^{-1}) lifts through a surjection (q:G\to T) to inner conjugacy of inverse images, preserving the marked extension diagram.
3. The allowed automorphisms of (H) are the restriction image (A_i) of automorphisms of the quotient/inclusion diagram, not all `Aut(H)`.
4. Crossed maps for a fixed action correspond bijectively to complement graphs, and regularity is characterized correctly.
5. GAP homomorphism and complement class routines use equivalences different from the required simultaneous (A_i\times Aut(M)) action.
6. A complete implementation must retain enough transporter/stabilizer data to undo forbidden identifications and join action representatives exactly.

## Methods inventory

- Hand proof of lifted inner conjugacy: proves uniqueness of the inclusion orbit within each fixed quotient block, not equality of the nine blocks.
- GAP 4.12.1: independently count conjugacy classes of order-21 subgroups in `GL(3,2)` and record the point-stabilizer type. This does not compute the nine groups (A_i).
- Direct semidirect-product calculation: proves the crossed-map/complement correspondence and identifies conjugation actions.
- GAP documentation semantics plus explicit group-action analysis: determines which routine outputs are too coarse for the final orbit set.

## Hard limits and recommendation

No full regular-embedding enumeration or (A_i) computation is authorized. Validate the design only; require explicit generators/actions for all nine (A_i), transporter-aware orbit construction, and completion certificates before any eliminations.
