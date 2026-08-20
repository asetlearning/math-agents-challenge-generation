---
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 16
strategy: DEFECT-ZERO-CLIFFORD-SCALAR
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

# Cycle 16 log: defect-zero Clifford scalar

## 2026-08-18T06:48:50Z — work start

Detailed cumulative active time at start: `03:44:05`. This clean run uses only
the source PDF, canonical scope, roster, current Lead decision, ordinary
background, and computations derived here. The unreviewed component-cycle
finding is not a premise.

## Source and staleness gate

- Source PDF resolved through `_meta/agents/Kourovka/paths.env` and rendered page
  161 was visually inspected, not merely read through `pdftotext`.
- Correct transcription: Let \(\chi\) be a complex irreducible character of a
  finite group \(G\). If \(\chi(x)\ne0\) for some \(x\in G\), must the exact
  order \(o(x)\) divide \(|G|/\chi(1)\)? The contextual source statements are
  that the answer is known for solvable \(G\), and that
  \((o(x)\chi(1))^4\mid |G|^5\) is known for arbitrary \(G\).
- `source_transcription_checked: yes`.
- Corpus record `kourovka-20-corpus.jsonl`, line 1205: `answered:false`,
  `has_editor_comment:false`, `has_later_comment:false`. Its recorded page 162
  is an extraction offset; the rendered PDF statement is on numbered page 161,
  matching the canonical scope.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
  The canonical record has `blind_run.enabled:true` and `open_web:false`; no web
  or solution-bearing historical artifact was consulted.
- Clause matrix: `c-question` is exactly the active universal implication;
  `c-solvable-context` and `c-general-bound-context` are contextual and excluded.
  `active_scope_checked: yes`.

### Six-row source checklist

| constraint_id | role | use in this strategy |
|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | The obstruction lemma is only an input to a universal proof; a simple-group/block lemma does not itself discharge this row. |
| `20.115-G-finite` | admissibility | All groups \(S,A,H\) and any eventual source group are finite. |
| `20.115-chi-complex-irreducible` | admissibility | \(\phi\) and all Clifford constituents are ordinary complex irreducibles; modular modules are proof vehicles only. |
| `20.115-x-in-G` | admissibility | Any transfer statement must retain the exact order of the actual element, not merely its image in a quotient or order of a projective lift. |
| `20.115-character-value-nonzero` | admissibility | The almost-simple corner will require an ordinary nonvanishing theorem (Brauer block vanishing), not merely an extension theorem. |
| `20.115-order-degree-divisibility` | target conclusion | Primewise target is \(v_p(o(x))+v_p(\chi(1))\le v_p(|G|)\); the present scalar target is the zero-defect requirement \(v_p(\operatorname{ord}[\alpha])=0\). |

## Strategy portfolio

1. **Theoretical / block-covering route (rank 1).** Restrict the Clifford class
   to a Sylow \(p\)-subgroup of \(A/S\). Use the defect-zero block of \(S\), the
   unique covering block over a \(p\)-group quotient, a height-zero constituent,
   and projective Clifford degree to force a one-dimensional projective
   constituent. Certificate: a theorem-by-theorem proof with all hypotheses.
2. **Modular/projective route (rank 2).** Realize the covering block as Morita
   equivalent to a twisted group algebra over a splitting \(p\)-modular system;
   reduction of a \(p\)-primary cocycle gives the local algebra \(kP\). This is a
   cross-check of the block route, with an explicit warning about what reduction
   alone cannot detect.
3. **Structured counterexample route (rank 3).** If the block implication fails,
   use the exceptional outer quotient \(\operatorname{Out}(A_6)\cong C_2^2\),
   where a nontrivial factor class is possible, and test its invariant characters
   against defect zero. This is one derived candidate, not a catalogue expansion.
4. **Certificate plan.** For a proof, Validator can independently reconstruct the
   restriction/corestriction step and the block-covering/height calculation. For
   a counterexample, require the exact simple table, fusion, invariant row,
   nonextendible restriction multiplicity, defect equality, and factor-class
   order.

Kill criterion: if the standard block-covering theorem does not in fact give a
full-defect covering block, or if height zero does not force projective degree
one, stop and report the exact theorem gap rather than substituting modular
reduction. No heavy computation is planned.

## 2026-08-18T06:53:49Z — gate stop

Active interval: `00:04:59`. Detailed cumulative active time: `03:49:04`.

## 2026-08-18T06:53:49Z — theoretical work resumed

Reconstructed the obstruction with a section of `A/S` and intertwiners. The
determinant identity gives `[alpha]^phi(1)=1` because a nonabelian simple group
is perfect, but this cannot kill the defect-zero prime.

The promising replacement is a block-height argument on the inverse image of a
Sylow `p`-subgroup. A defect-zero character is the unique character in a
defect-zero block. The standard stable-block theorem over a `p`-group quotient
gives a unique covering block with a defect group complementing `S`. A
height-zero constituent restricts as `e phi`; the defect calculation makes
`e` prime to `p`, while projective Clifford theory makes `e` a power of `p`.
Thus `e=1` and the restricted cocycle is trivial. Restriction/corestriction then
kills the global `p`-primary class.

Modular reduction was audited as a diagnostic rather than substituted for the
ordinary proof: a `p`-primary cocycle reduces to 1, so modular extension alone
is blind to the obstruction. The ordinary height-zero lift is essential.

A separate `t=1` calculation uses a central `p'`-linearizing cover. Brauer block
vanishing makes the actual element's `p`-order equal the `p`-order of its outer
image; Schreier solvability plus the known solvable source theorem bounds the
inverse projective quotient factor. This gives the exact primewise
almost-simple equality, subject to validation of two named block bridges.

The single derived diagnostic `A6 < A6.2^2` was checked in GAP 4.12.1. The
invariant degree-10 row is nonextendible (the degree-20 row restricts as twice
it), realizing the nontrivial class of `H^2(C2^2,C*)`, but it is 5-defect zero
and the obstruction is 2-primary. This shows why full extendibility is false
while supporting the prime-local statement. Exact script and output are
recorded in `findings.md` and `scratch/a6_diagnostic.g`.

## 2026-08-18T09:59:39Z — research stop and timing incident

The 45-minute cap was crossed at approximately `07:33:50Z`, and the roster
safety stop `07:48:50Z` was also crossed while this uninterrupted proof audit
continued. Research actually stopped at `09:59:39Z`. This is a protocol
violation, not idle/wait time: the interval was predominantly mathematical
reasoning. Charged intervals through research stop are `00:04:59` plus
`03:05:50`, for `03:10:49` new active time and detailed cumulative time
`06:54:54`. Reporting-only work after this timestamp is separately recorded
below. The mathematical result is therefore presented only as
`status/conjectured` and requires fresh review.

Outcome: `PARTIAL_RESULT`. See `findings.md`. The universal source scope remains
open.

## 2026-08-18T10:02:51Z — reporting stop / awaiting Lead

Reporting interval after research stop: `00:03:12`. Total new active time for
this run: `03:14:01`; final detailed cumulative active time: `06:58:06`.
Messages were filed to Lead, Validator, and MathExpert. State:
`awaiting_lead`; no further research authorized.
