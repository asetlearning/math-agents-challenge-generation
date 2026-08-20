---
title: "Problem 20.115 proof cycle 15 - component-cycle trace transfer"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 15
strategy: COMPONENT-CYCLE-TRACE-TRANSFER
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Problem 20.115 - component-cycle trace transfer

## Active-time ledger

- Work start: `2026-08-18T06:19:56Z`; inherited detailed cumulative active time: `03:15:05`.
- Source/protocol/assignment gate completed: `2026-08-18T06:25:09Z`; elapsed and charged `00:05:13`; detailed cumulative active time `03:20:18`.

## Active target and exact six-row scope gate

Target: for every finite group G, every ordinary irreducible complex character
chi in Irr(G), and every x in G, chi(x) != 0 implies
o(x) chi(1) divides |G|.

| constraint id | role | requirement in this proof lane | state |
|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | A least-counterexample argument must eliminate every admissible triple, not just a bounded family. | active |
| `20.115-G-finite` | admissibility | G is finite; normal-subgroup and component-orbit arguments use finiteness. | active |
| `20.115-chi-complex-irreducible` | admissibility | chi is an ordinary complex irreducible character. Projective representations below are Clifford-theoretic vehicles, never replacements for the source character. | active |
| `20.115-x-in-G` | admissibility | x is in G, with exact order o(x); quotient and lift orders must be tracked exactly. | active |
| `20.115-character-value-nonzero` | admissibility | The exact ordinary value chi(x) is nonzero; no inference about arbitrary powers is allowed. | active |
| `20.115-order-degree-divisibility` | target conclusion | Establish o(x) chi(1) divides |G|. This cycle targets the nonabelian proper-minimal-normal kernel factor only. | open |

No candidate closes the universal conclusion at cycle start.

## Source and staleness gate - 2026-08-18

`source_transcription_checked: yes`

`active_scope_checked: yes`

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

Resolved the configured PDF through `_meta/agents/Kourovka/paths.env`, navigated
with `pdftotext -f 161 -l 161 -layout`, rendered displayed page 161, and visually
checked it. Correct transcription: Let chi be a complex irreducible character of a
finite group G. If chi(x) is nonzero for some x in G, must the order o(x) of x
divide |G|/chi(1)? The two following sentences are excluded context: the solvable
case is known; universally `(o(x) chi(1))^4` divides `|G|^5` is known. The
rendered statement agrees with all six canonical constraints. The corpus flags are
`answered:false`, `has_editor_comment:false`, and `has_later_comment:false`; its
page field 162 is a pagination mismatch, while the displayed/configured page is
161.

The canonical scope has `blind_run.enabled:true` and `open_web:false`, so no new
solution-bearing web search is performed in this fresh lane. The scope record
already labels the May 2026 exact-subject paper as a reviewed partial rather than a
universal answer; this is scheduling context only and supplies no premise below.

## Strategy portfolio

1. **Theoretical tensor-permutation trace (rank 1).** Construct the projective
   Clifford action of x on an irreducible N = S^t module and derive the trace cycle
   by cycle. Identify exactly what chi(x) != 0 forces. Certificate: basis-level
   formula and a primewise divisibility audit.
2. **Structured obstruction family (rank 2).** If the desired product divisibility
   fails by overlap, design wreath-product/projective examples with prescribed
   component-cycle lengths and component element orders. Certificate: symbolic
   valuations; no catalogue.
3. **Catalogue/small-case probe (rank 4).** A frozen single-family table could test
   a proposed obstruction, but a negative finite screen cannot prove the universal
   target and no catalogue expansion is authorized. No computation planned.
4. **Alternative theoretical orbit/coprimality family (rank 3).** Separate fixed
   components from nontrivial permutation cycles and prove the transfer under an
   explicit prime-disjointness condition. Certificate: lcm/product valuation
   inequalities and exact cocycle/lift-deficiency definition.

Kill criterion for the primary line: an explicit family in which the tensor trace
is nonzero but componentwise minimality controls only separate factors whose prime
valuations necessarily overlap beyond |S|^t, or an unavoidable undefined
scalar-lift factor not encoded by the cycle products. On firing, report the exact
loss and the strongest conditional family rather than widening to a catalogue.

## Early 30-minute self-check - 2026-08-18T06:44:42Z

- **Scope/revision:** still exactly revision 1 of the universal ordinary-character
  implication; work is confined to the assigned nonabelian proper-minimal-normal
  branch.
- **Current hypothesis:** G is a least-order source counterexample, N = S^t is a
  proper minimal normal subgroup, and `chi_N = a theta` is homogeneous.
- **Checkable evidence:** `findings.md` contains the basis-level cycle trace
  identity, exact component automorphism orders, and a primewise divisibility
  calculation. No computation or catalogue data are used.
- **Representation check:** tensor-permutation coordinates remain productive. They
  prove `k | |S|/phi(1)` without using values at powers. They do not control the
  global scalar factor `Delta = z/e`.
- **Constraint status:** all five admissibility rows remain explicit and pass only
  within the stated hypothetical branch; the universal conclusion row remains
  open. There is no source candidate and hence no `OUT_OF_SCOPE_EXAMPLE`.
- **First exact loss:** the corrected gate is equivalent to
  `v_p(k)+v_p(Delta) <= t v_p(|S|/phi(1))`. An exact projective family
  `(C2 x C2) x C_(2^r)` with quaternion factor set has nonzero trace but
  `Delta=2`, so trace nonvanishing cannot erase the scalar factor.
- **Alternatives:** (A) prove the p-part of a simple-character Clifford obstruction
  is bounded by component codegree; (B) seek a named invariant defect-zero simple
  character realizing nonzero p-deficiency. The recommended next experiment is
  the theorem check in (A); the kill criterion is absence of any self-contained
  obstruction/codegree theorem in this cycle.

## Cycle outcome - PARTIAL_RESULT

- Work stop: `2026-08-18T06:48:16Z`; charged this cycle `00:29:00` (elapsed
  `00:28:20`, rounded up); detailed cumulative active time `03:44:05`. Unused
  authorized increment: `00:16:00`.
- The named strategy has reached its theorem gate, so research enters
  `awaiting_lead` rather than starting a replacement method.
- New exact facts: the tensor-permutation trace is a product of ordered
  component-cycle traces; every factor is nonzero; local ordinary extensions and
  least-order minimality give `k | |S|/phi(1)`; the Clifford scalar extension gives
  the assigned `Delta=z/e`; the corrected kernel factor is equivalent to the exact
  primewise inequalities recorded in `findings.md`.
- Ruled out: inferring nonzero values at powers, placing multiplicity `a` in the
  kernel, or inferring `Delta=1` from nonzero trace. The quaternion family in the
  findings note is an exact counterexample to the last inference.
- Bottleneck: no independently available theorem bounds the p-part of the local
  outer-automorphism Clifford obstruction by the component codegree. The first
  failure family is a p-defect-zero component character together with p dividing
  Delta; existence as a simple-character triple remains open.
- Recommended continuation: MathExpert should first check the targeted
  defect-zero extension/obstruction theorem. If positive, resume only long enough
  to insert it into inequality (13). If negative, request one exact named simple
  character triple and test its nonzero cycle value. Do not widen to a catalogue.
- Uncovered structural corner: `t=1`, `C_G(S)=1`, and the local component group
  equals G, so the local minimality invocation would be circular.
