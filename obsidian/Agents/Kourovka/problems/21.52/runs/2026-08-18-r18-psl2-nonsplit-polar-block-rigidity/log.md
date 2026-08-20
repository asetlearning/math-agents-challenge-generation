---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 18
strategy: PSL2-NONSPLIT-POLAR-BLOCK-RIGIDITY
---

# Cycle 18 log — odd nonsplit `PSL(2,q)` polar-block rigidity

## 2026-08-18T11:34:11Z — active work start

- Prior cumulative ledger supplied by Lead: `349m27s`.
- Newly charged active time starts at `0m00s`; hard lane cap `45m00s` and wall-clock safety stop `2026-08-18T12:29:52Z`.
- Exact lane: `L=PSL(2,q)`, prime powers `q congruent to 3 (mod 4)`, `q>=11`, and its unique involution class `D`.
- Context boundary: canonical scope, roster, current decision, protocol, and source only; no historical `log.md`, `findings.md`, verification notes, prior run directories, or archived messages read.
- External staleness search is deferred under canonical `blind_run.enabled: true`; no open web used.

## Source and scope gate

The source PDF, rendered page 172, was inspected directly. The statement says exactly: finite nonabelian simple `L`; one conjugacy class `D` of involutions; complete graph on `D`; edges equivalent exactly when the orders of the two involution products agree; and asks whether every labelled colour automorphism is induced by `Aut(L)`. The canonical typed conclusion adds the necessary setwise stabilizer/restriction language and has no mismatch with the displayed source. `source_transcription_checked: yes`; `active_scope_checked: yes`. Problem 21.53 is visibly separate and excluded. Canonical scope revision 1 has seven required rows:

| constraint_id | role | lane use |
|---|---|---|
| `21.52-forall-L-D` | admissibility | This family lemma is only a partial toward the universal quantifier. |
| `21.52-L-finite-nonabelian-simple` | admissibility | Need `PSL(2,q)` simple for `q>=11`. |
| `21.52-D-single-involution-class` | admissibility | Need derive uniqueness and identify `D`. |
| `21.52-Gamma-complete-on-D` | admissibility | All unordered distinct pairs in `D` are coloured. |
| `21.52-edge-colour-exact-product-order` | admissibility | Every used relation must be definable from exact `|ab|`, not an added geometric label. |
| `21.52-tau-preserves-all-edge-colours` | admissibility | Start with arbitrary labelled-colour automorphism `tau`. |
| `21.52-tau-induced-by-AutL` | target conclusion | Aim to place `tau` in the restriction of `P Gamma L_2(q)`. |

## Strategy portfolio

1. **Theoretical polar reconstruction (primary).** Derive the `SO_3(q)` model of involutions as one square class of anisotropic projective points; identify colour 2 with orthogonality; attempt to characterize traces of opposite-type polar lines intrinsically and recover the conic/projective line. Kill if a purported block predicate also selects a nongeneric clique family.
2. **Small-parameter audit (cheap sanity check).** Hand-enumerate or write only a sub-minute bespoke finite-field checker for `q=11` if a delicate clique count needs testing. Such sampling is diagnostic only and would require no family inference. No heavy computation is authorized.
3. **Alternative theoretical pivot.** If maximal-clique recovery fails, use colour-definable common-neighbour/no-common-neighbour profiles to recover the polarity or use the dihedral subgroup geometry of pairs directly.
4. **Certificate plan.** A family partial must give explicit coordinates, an exact product-order-to-trace formula, a purely colour-definable block predicate, a reconstruction theorem, and realization of every resulting semilinear orthogonal permutation by `Aut(PSL_2(q))`; Validator can audit all steps algebraically and separately brute-check `q=11`.

The canonical corpus/source audit already records the universal question as not answered. This discovery-blind lane performs no new external literature search: `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
