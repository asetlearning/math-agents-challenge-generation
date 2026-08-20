---
title: "Exact A5 colour-automorphism compute report — Kourovka 21.52"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
outcome: PARTIAL_RESULT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/conjectured
---

# Exact A5 colour-automorphism compute report

## Outcome

For \(L=A_5\) and its unique 15-element involution class \(D\), the frozen exact enumerations return

\[
\operatorname{Aut}_{\rm col}(D,|ab|)
=\operatorname{res}_D(\operatorname{Aut}(A_5)),
\qquad |\operatorname{Aut}_{\rm col}|=120.
\]

Thus \(A_5\) supplies no counterexample. This is only a fixed-\(A_5\) partial result and does not establish the universal assertion in Problem 21.52.

## Coverage and exact comparison

- Group: all 60 even permutations of five points.
- Class: all 15 order-two elements, the unique involution class of \(A_5\).
- Graph: all 105 unordered pairs of distinct class elements.
- Colours: exactly product orders, with colour set \(\{2,3,5\}\).
- Full colour group: exhaustive backtracking, 1516 search nodes, 120 permutations.
- Full \(\operatorname{Aut}(A_5)\): all 3600 images of a fixed generating pair tested; 120 automorphisms, each checked on all 3600 products.
- Restriction image: 120 permutations.
- Independent image: conjugation by every element of \(S_5\), again the same 120 permutations.
- Exact set difference in both directions: empty.
- Independent verifier: all 15 checks pass.

## Reproducible evidence

The exact frozen commands, resources, output paths, and pre-run hashes are in `frozen-run-manifest.json` (SHA-256 `9d91be237370aef9bf40013325b08e4927e228e5f8d4ecc93b062cffe91f357a`).

The complete certificate is `a5-colour-certificate.json` (file SHA-256 `4dc45ea15635231524e0b04fba73bf775e2be89da8f364648137d8d9622375e2`; embedded canonical digest `58eee67fc303b15947a21fe9eb997f92f32b348a2e00018446a11b1eedbe3674`). The independent verification is `a5-colour-independent-verification.json` (file SHA-256 `c74bf55643f3cf112f43e718dbf50fd5c6a58f97747501add4a3e5dd7becd299`; embedded digest `5edcf0aedf02ea4464309bb21c191e788bc0a48e0f54bbb60dc265b0c12407b1`). Full stdout/stderr hashes and observed wall times are in `Agents/Kourovka/problems/21.52/log.md`.

## What this does not establish

It does not cover any finite simple group other than \(A_5\), does not prove the universal claim, and supplies no separating colour permutation. Certification remains for Validator; this note remains `status/conjectured`.
