---
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

# PSL(2,7) involution-colour fresh run log

This fresh-session note is separate from the historical problem log because the
Lead decision forbids reading or reusing solution-bearing history. No historical
log, findings, verification note, archived message, synthesis, or A5 computation
was inspected. The only current inbox item read was the controlling Lead decision.

## Active-time ledger

- 2026-08-17T15:51:05Z — research started; session cumulative active minutes 0;
  scope ledger reported by canonical record as 10/180 before this fresh run.
- 2026-08-17T15:54:55Z — algorithm frozen and research stopped pending compute
  lease; session cumulative active minutes 4; this run's cap is 60 active minutes.

## Staleness and source gate

- `DISCOVERY_BLIND`: yes, from the canonical scope's `blind_run.enabled`; open web
  and solution-bearing history were not used.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- The configured PDF resolved through `_meta/agents/Kourovka/paths.env`.
- Page 172 was read with `pdftotext` and independently rendered to PNG at 120 dpi
  with `pdftoppm`; the full statement and displayed notation were visually read.
- Correct transcription: Let (L) be a finite non-abelian simple group and (D)
  a conjugacy class of involutions in (L). On the complete graph \(\Gamma\) with
  vertex set (D), declare ((a,b)\sim(c,d)) iff \(|ab|=|cd|\). A coloured-graph
  automorphism is a permutation \(\tau\in S_D\) such that
  ((a,b)\sim(a^\tau,b^\tau)) for every edge. The question asks whether the
  automorphism group of \(\Gamma\) is a subgroup of \(\operatorname{Aut}(L)\).
- `source_transcription_checked: yes`.
- The configured corpus directory contains only the issue-20 corpus, so there is
  no issue-21 JSONL row from which to read `answered`, `has_editor_comment`, and
  `has_later_comment`; the current 2026 source page itself shows no editor or later
  comment on 21.52. This is recorded as a corpus-data absence, not as a literature
  conclusion.

### Clause matrix

| source clause | exact finite interpretation | active? | stale evidence used? |
|---|---|---:|---:|
| (L) finite non-abelian simple; (D) one involution class | Fix (L=\mathrm{PSL}(2,7)) and enumerate one complete conjugacy class of elements of order 2 | yes | none (blind run) |
| Complete graph on (D) | Every unordered pair of distinct class elements is an edge | yes | none |
| Edge equivalence iff \(|ab|=|cd|\) | Build the complete integer product-order matrix; equal integers are exactly equal colours | yes | none |
| \(\tau\) preserves every edge colour | Exhaustively enumerate every permutation satisfying all matrix equalities | yes | none |
| Compare with \(\operatorname{Aut}(L)\) | Compare with restrictions of every abstract automorphism stabilizing (D) setwise | yes | none |

`active_scope_checked: yes`. Every revision-1 constraint is represented: the
universal row permits a counterexample from one admissible pair; PSL(2,7) is modeled
directly as \(\mathrm{SL}(2,7)/\{\pm I\}\); the selected (D) must be one complete
class of elements of exact order 2; the graph, colours, and all-colours hypothesis
are exhaustive; the conclusion is tested by exact set difference against the
restriction image. No canonical mismatch was found.

## Strategy portfolio

1. **Catalogue/fixed-target mode (selected):** a complete exact determination for
   the single authorized pair (L=\mathrm{PSL}(2,7)), (D) its involution class.
   Equality gives only a fixed-target partial; strict containment plus a separating
   permutation gives a candidate only after every scope row is documented.
2. **Structured-construction mode (not activated):** interpret any excess colour
   symmetry through the rank/suborbit structure on the 21 involutions and design a
   family. This would be a representation-changing pivot and needs a new Lead
   decision.
3. **Theoretical mode (not activated):** reconstruct group incidence from the
   product-order relations. This fixed-target lane first determines whether such
   reconstruction is rigid.
4. **Certificate plan:** a standard-library-only exact script writes the complete
   21-by-21 colour matrix, all colour permutations, all restrictions of abstract
   automorphisms, equality/separation, deterministic counts, and SHA-256 digests.
   Validator can independently reconstruct the quotient model or rerun the bounded
   enumeration without trusting constants.

## Frozen exact algorithm at +4 active minutes

Script:
`Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27_exact.py`

SHA-256:
`934b86ed083311263b7fbdfb4c59fdf84dd0c512fc56f78412ad4bc84a3daeaa`

The script deterministically:

1. constructs all 168 sign-pairs of determinant-one 2-by-2 matrices over
   \(\mathbf F_7\), with exact quotient multiplication;
2. computes element orders and all conjugacy classes of involutions, requiring one
   complete class of size 21;
3. computes all 210 off-diagonal product orders and their full matrix;
4. exhaustively backtracks through every partial permutation compatible with every
   already exposed edge colour, with forward checking and a hard 50,000,000-node
   failure cap, collecting every full colour-preserving permutation;
5. finds a deterministic generating pair for (L), tests all \(168^2=28,224\)
   possible image pairs by exact Cayley-graph propagation, and retains precisely
   the conflict-free bijections, which are all abstract automorphisms because the
   source pair generates;
6. filters the setwise stabilizer of (D), computes every restriction, compares the
   two exact permutation sets, and records the lexicographically first separator if
   one exists.

Frozen command (not yet run):

`timeout 180s python3 Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27_exact.py --output Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27-certificate.json --max-nodes 50000000`

Resource bound: one CPU core, less than 512 MiB RAM expected, 180-second hard
timeout, five-minute compute lease requested. Python version observed: 3.12.3.

## Authorized exact run

- 2026-08-17T16:03:22Z — research resumed after Lead granted compute slot 3;
  frozen script SHA-256 rechecked and matched the lease.
- 2026-08-17T16:03:41Z — run and immediate certificate inspection finished;
  compute slot 3 released by REPORT; session cumulative active minutes 5 (one
  charged minute since lease; canonical scope ledger was 10/180 before this run).

The authorized command was run exactly once, without patch or rerun, and returned
exit status 0 after 1.888816803 wall seconds. Verbatim stdout:

```json
{
  "group_order": 168,
  "involution_class_size": 21,
  "edge_colour_counts": {
    "2": 42,
    "3": 84,
    "4": 84
  },
  "colour_automorphism_count": 336,
  "colour_search_nodes": 5902,
  "autL_count": 336,
  "setwise_stabilizer_count": 336,
  "restriction_image_count": 336,
  "groups_equal": true,
  "separator": null,
  "certificate_content_sha256": "e95c416a195bf1cda3d6dc8c23385ffecdeeb32b6150ca23ab264436348556ea"
}
```

Certificate file:
`Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27-certificate.json`
(156872 bytes; SHA-256
`4042b2a1ed73c8f4e3e7b798059d39772ddc0c3b2c367c3428c02af0c60f3bcc`).

### Constraint-and-conclusion interpretation

| constraint_id | fixed-target value / use | result |
|---|---|---|
| `21.52-forall-L-D` | A counterexample could refute the universal assertion at one admissible pair; equality at one pair cannot establish it | not answered universally |
| `21.52-L-finite-nonabelian-simple` | Direct quotient model `SL(2,7)/{±I}` of `PSL(2,7)`, order 168 | pass for fixed target |
| `21.52-D-single-involution-class` | Exact order computation and conjugation partition give one complete class of 21 involutions | pass |
| `21.52-Gamma-complete-on-D` | All 210 unordered distinct pairs appear in the 21-by-21 matrix | pass |
| `21.52-edge-colour-exact-product-order` | Exact quotient multiplication and element order give counts 42, 84, 84 for orders 2, 3, 4 | pass |
| `21.52-tau-preserves-all-edge-colours` | Exhaustive backtracking returns all 336 permutations satisfying every matrix equality | pass for enumerated group |
| `21.52-tau-induced-by-AutL` | Exact restriction image also has 336 permutations and is equal as a permutation set | holds at this fixed target, not violated |

Outcome: **fixed-target `PARTIAL_RESULT`**. There is no separating permutation and
therefore no counterexample candidate. The result does not establish the universal
target, does not cover another simple group, and has not yet received independent
Validator certification.

Verified by [[Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-psl27-equality]].
