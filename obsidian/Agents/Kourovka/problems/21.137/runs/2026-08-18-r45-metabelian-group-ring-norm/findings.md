---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
---

# PARTIAL_RESULT — metabelian norm reduction and exact operator obstruction

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: 2

Target statement: Let `p` be an odd prime and `G` a finite `p`-group of exponent
exactly `p^2`. If the literal set `P={g^p:g in G}` is a subgroup, then `P` is
abelian.

This run treats only the metabelian subfamily.

## Partial claim

For a metabelian candidate, literal power-set closure has the exact canonical
affine-norm and commutator reduction (R1)--(R7) in `log.md`. Those norm, exponent,
and fibre-support identities do not by themselves force the target commutator to
vanish: a prime-uniform truncated-polynomial module satisfies them at operator
level with a nonzero commutator symbol. The remaining content is global
associative extension-cocycle/power-map coherence, not another group-ring norm
identity.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | value / use here | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | Every admissible `p,G` | Derivation is prime-uniform but restricted to metabelian `G`. | `log.md`, R1--R7 | partial only |
| `21.137-odd-p-not-2` | admissibility | `p>2` prime | All formulas hold for odd `p`; `p=3` audited explicitly. | `log.md`; checker output | pass |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group | Reduction assumes an arbitrary finite metabelian `p`-group. Formal obstruction is not asserted to be a group. | `log.md` | pass for reduction; not a witness |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | Used to make `P` exponent `p` and to impose every length-`p^2` norm annihilator; no assumption on `exp(G')` was made. | R4 and operator audit | pass for reduction |
| `21.137-odd-power-set-definition` | admissibility | literal actual power set | Fibres are unions over every actual root quotient class, not the generated verbal subgroup. | R1--R3 | pass |
| `21.137-odd-power-set-subgroup` | admissibility | literal set is a subgroup | Used to identify each complete fibre with one `H=P intersect G'` coset and to obtain R3--R4. | R2--R4 | pass for reduction |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | Not established, even for all metabelian groups. The formal datum shows the recorded norm identities alone cannot establish it. | operator obstruction | unresolved |

## What was computed in

The hand argument is in the abelian derived `Z[G/G']`-module of an arbitrary
metabelian candidate. The finite check is only in
`F_p[S,T]/(S^p,T^p)` for `p=3,5,7`, using the exact local script
`scratch/check_norm_obstruction.py`.

## Is that object the target?

No. The truncated-polynomial datum is a formal operator/fibre-support certificate,
not an associative finite group and not a counterexample. It refutes only the
inference from the named norm identities to commutativity.

## What this does not establish

It does not prove the metabelian family theorem, does not construct a group with a
nonabelian literal power subgroup, does not address nonmetabelian groups, and does
not close the active source scope.

## Recommended handoff

Mark `METABELIAN-GROUP-RING-NORM` exhausted at the root-action/basepoint gate. A
continuation would need a fresh global factor-system strategy that couples the
power basepoints for every quotient element and then either rules out the formal
socle amplitude or realizes one complete finite group. Repeating single-root norm
collection or selecting one multiplicative root section cannot cross the gate.
