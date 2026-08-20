---
title: "Verification triage — Kourovka 19.30 — prime-power separator partial theorem"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "Under four additional prime-separator hypotheses on a finite simple group S, every finite same-order group G with the same vanishing-element-order set is isomorphic to S."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Verification triage — Kourovka 19.30

## Claim and exact scope

The submitted object is a computation-free sufficient-condition theorem, not a witness and not a scope-wide claim. It asserts recognition only for finite simple groups satisfying four extra hypotheses. The canonical active scope is `19.30/vanishing-order-simple-recognition`, revision 1, whose target is universal over all admissible pairs `(G,S)`. The canonical exclusions are the three entries in the frontmatter.

The canonical scope record points to the passed independent source-fidelity audit at `Agents/Kourovka/problems/19.30/verification/2026-08-16T114327Z-source-fidelity-audit.md`. No claim-check JSON is linked. Because the submission is expressly a `PARTIAL_RESULT`, not a scope-wide `CLAIM` or `STALE_MATCH`, this audit can assess the stated partial theorem but cannot close or control the active assignment.

## Clause matrix

| source clause | active? | submission coverage | remains open |
|---|---:|---|---|
| Definition: an element is vanishing iff some irreducible complex character vanishes on it | yes | Used in Lemmas 1–2 and Theorem 4 | No issue at triage |
| Universal recognition question for finite `G` and finite simple `S` of equal order and equal vanishing-order sets | yes | Only the subclass selected by four additional hypotheses | Every admissible simple `S` outside that subclass; hence the universal conclusion |

`active_assignment_answered: pending` at triage; it can become `yes` only if the universal row is established, which this submission explicitly does not claim.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | proof use / candidate value | triage result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | Every admissible pair `(G,S)` | Replaced by a sufficient subclass defined by four extra hypotheses | not established universally |
| `19.30-G-finite` | admissibility | `G` finite | Needed for minimal normal subgroups, Sylow theory, Clifford theory | addressed in proposed subclass |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | Assumed, with added uniqueness among simple groups of order `|S|` | addressed in proposed subclass |
| `19.30-vanishing-definition` | admissibility | Zero of at least one irreducible complex character | Lemmas 1–2 seek to exclude `p^a` from `V_o(G)` | exact definition used |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | Transfers the full `p`-part `p^a` and divisor hypotheses | addressed in proposed subclass |
| `19.30-equal-vanishing-order-sets` | admissibility | Equality of sets, without multiplicity | A single presence/absence separator `p^a` is intended to contradict equality | addressed in proposed subclass if Lemmas 1–3 hold |
| `19.30-isomorphic` | target conclusion | `G \cong S` | Intended conclusion of Theorem 4 under four extra hypotheses | not established universally |

## Target versus witness

- Source target and active assignment: the universal recognition implication in the frontmatter.
- Witness actually checked: none; this is a hand-proof audit of a restricted abstract theorem.
- Witness equals target: false as a scope-coverage statement. The proposed theorem is deliberately a proper sufficient subclass unless its four added hypotheses are separately proved for every finite simple group.
- Circularity risk: no computational witness is constructed from the desired conclusion. The proof must nevertheless avoid assuming normal Sylow structure while deriving it in Lemma 3.

## Subclaim decomposition

1. Lemma 1: for a cyclic normal Sylow `p`-subgroup `P` and a generator `x`, every irreducible character of `G` is nonzero at `x`; the orbit length and cyclotomic noncancellation steps must both be valid.
2. Lemma 2: a normal Sylow `p`-subgroup of order `p^a` forces `p^a` to be absent from the vanishing-order set, treating noncyclic and cyclic `P` separately.
3. Lemma 3: under the two minimal-normal hypotheses, every nonsimple same-order group has a normal Sylow `p`-subgroup; both the `p`-group kernel and the `p'`-kernel lifting cases must close.
4. Theorem 4: equal vanishing-order sets and the target vanishing element of order `p^a` force `G` simple, after which simple-order uniqueness forces `G \cong S`.
5. Scope fidelity: even a complete proof of 1–4 certifies only the stated sufficient subclass, not the active universal assignment.

## Tool probe and hard limits

Probe output before proof inspection: GAP is present (Debian package `gap-core` version `4.12.1-2build2`); Python 3.12.3 and `pdftotext` 24.02.0 are present; Sage and Magma were not found. No mathematics system, web access, historical solution, or computation is authorised or needed. The submitted argument will be audited by hand from the linked proof and canonical scope only. The conditional Suzuki subsection is outside the requested certification target.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| Lemma 1 | Line-by-line Clifford-theory and cyclotomic-polynomial audit | Nonvanishing at generators of a cyclic normal Sylow subgroup, if every displayed implication is justified | Nonvanishing at arbitrary elements; normality or cyclicity of Sylow subgroups |
| Lemma 2 | Element-order split plus Lemma 1 | Absence of the single integer `p^a` from `V_o(G)` when the full Sylow subgroup is normal | Absence of order `p` from groups having merely some normal subgroup of order `p` |
| Lemma 3 | Strong induction on `|G|` and independent analysis of the two minimal-normal cases | Normality of the full Sylow `p`-subgroup under the two stated divisor/automorphism hypotheses | The hypotheses for arbitrary simple groups or the conditional Suzuki inputs |
| Theorem 4 | Direct logical composition of Lemmas 2–3 with simple-order uniqueness | Recognition for precisely the stated additional-hypothesis subclass | The universal Kourovka target or any unconditional Suzuki family |
| Scope coverage | Compare theorem quantifiers against canonical revision 1 | Exact surviving subclass and `active_assignment_answered` value | Any external classification or literature claim |

## Recommendation

Proceed with a full hand audit of Lemmas 1–3 and Theorem 4. Regardless of whether those four statements survive, the maximum scope-level outcome is a reusable partial theorem with `active_assignment_answered: no`; the conditional Suzuki subsection must remain uncertified.
