---
title: "Triage — Kourovka 21.137 — frozen CTH-3-6 defect"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "In F(x,y)/gamma_7, for the exact frozen word R_5, the h_3-coordinate of [x^3,y^3]R_5^{-1} is -1, so the frozen CTH-3-6 correction-lattice test fails."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual p-th-power set is a subgroup, then it is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "the general powerfulness clause", "any odd-prime group of exponent other than p^2"]
target_object: "For this strategy report only: the exact word D=[x^3,y^3]R_5^{-1} in F(x,y)/gamma_7; the active Kourovka target remains all admissible finite p-groups."
witness_object: "The same exact free-nilpotent word, with no finite or computational quotient asserted."
witness_equals_target: "pending exact-word reconstruction for the strategy object; false as an identification with the unrestricted Kourovka object class"
verification_method: "independent truncated Magnus-series collection plus hand free-Lie/Hall audit"
tools_available: ["GAP 4.12.1", "Python 3.12.3"]
tools_unavailable: ["Sage", "Magma"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/hall-collection, project/kourovka, status/draft]
---

# Triage — frozen CTH-3-6 defect

## Claim restated

With commutators interpreted as exact group words and with the claimant's frozen
definition of (R_5), the central image of

\[
D=[x^3,y^3]R_5^{-1}\in \gamma_6(F/\gamma_7F)
\]

has coefficient (-1) at (h_3=[[[[y,x],x],x],y],y]).  This would certify only
that the named frozen correction lattice (9L+3\langle U\rangle) cannot contain
(D); it cannot certify the class-6 theorem or the active assignment.

## Scope, revision, and clause matrix

Canonical scope: `21.137/odd-prime-exponent-p2`, revision 2.  The assigned
resource boundary permits the current canonical record and the report's two
references only.  The scope record already carries a passed source-fidelity
audit; this verification does not reopen source or solution-bearing history.

| source clause | in scope | addressed by this report | status |
|---|---:|---:|---|
| General question: power values form a subgroup implies powerful | no | no | excluded |
| Odd (p), exponent exactly (p^2): power-value subgroup abelian | yes | no | active assignment unanswered |
| (p=2), exponent 8 square-value subgroup | no | no | excluded |

`active_assignment_answered: pending` until the exact strategy certificate is
checked; even a pass must end with `active_assignment_answered: no`.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | effect of strategy claim | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all admissible odd (p,G) | fixes (p=3) and one proof mechanism | not addressed |
| `21.137-odd-p-not-2` | admissibility | (p>2) prime | uses (p=3) | pass only for experiment |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime (p)-group | computes in a free nilpotent group, not an admissible finite witness | not addressed |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly (p^2) | correction lattice is motivated by exponent 9, but no universal implication is certified here | not addressed |
| `21.137-odd-power-set-definition` | admissibility | actual values, not verbal subgroup | inherited only as motivation for frozen corrections | not independently addressed |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | inherited only as motivation for frozen corrections | not independently addressed |
| `21.137-odd-P-abelian` | target conclusion | (P) abelian | proposed lift stops before an identity | not established |

No row can support `active_assignment_answered: yes`.

## Target versus witness

There are two deliberately separated targets.  The *strategy target* is an exact
coordinate of a specified word in (F/\gamma_7F); the witness is intended to be
that same word, so no model-equality theorem is needed once every factor and
commutator convention is reconstructed.  The *Kourovka target* quantifies over
finite groups and is not equal to this strategy object.  Thus a successful check
is evidence only for `STRATEGY_EXHAUSTED`.

## Subclaims

1. The nine displayed weight-six words really are an integral Hall basis of
   (L=\gamma_6(F/\gamma_7F)), not merely nine spanning-looking commutators.
2. The asserted three-conjugate formula for ([x^3,y^3]) is exact under the stated
   commutator convention.
3. Collection of the left side gives (h_3)-coordinate (-1), with no omitted
   (h_3) term from (v_1^3,v_2^3,[v_2,v_1]).
4. Collection of every exact factor of (R_5), especially (Q=[T_B,x]), gives
   total (h_3)-coordinate zero.
5. Reversal and interchange in (R_5^{-1}) add no hidden degree-six correction.
6. A coordinate (-1) excludes membership in (9L+3\langle U\rangle), independently
   of the ten vectors (U).
7. The conclusion is restricted to exhaustion of the frozen lift.

## Methods inventory

| subclaim | independent method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | Witt rank plus degree-six Magnus images compared with a standard Lyndon/Hall lattice | the named words form the required integral basis and the coordinate is meaningful | any theorem about finite (3)-groups |
| 2 | literal free-word reduction and independent truncated Magnus expansion | exactness of the three-conjugate formula through all degrees / as a free word | correctness of later collection |
| 3–5 | separately written exact integer Magnus-series checker truncated at degree 6; solve against the audited basis | the requested coordinate of the exact words in (F/\gamma_7F) | equality in an unrestricted finite group or existence of another identity |
| 6 | elementary divisibility in the free abelian layer | the frozen lattice-membership test fails | that an enlarged or different correction mechanism fails |
| 7 | scope comparison | correct operational verdict | the active theorem |

The checker will not reuse claimant code (none was supplied) or claimant-derived
intermediate formulas.  Exact input words will be transcribed directly from the
request references, and all coefficient output will be retained verbatim.

## Hard limits and recommendation

Installed GAP lacks any assumed nilpotent-quotient package until probed; Sage and
Magma are absent.  A bounded degree-six noncommutative-series checker is simpler
than the claim and auditable, so no general-purpose reimplementation is needed.
The recommendation is full verification of the exact coordinate and a verdict no
higher or broader than the frozen-strategy disposition.
