---
title: "Fixed rank-four nonsplit H3 central-cohomology family exhausted"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
outcome: PARTIAL_RESULT
strategy_outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

# Exact active source scope

Odd `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual set
`{g^p:g in G}`, never generated subgroup; literal set itself a subgroup; ask
whether it is abelian; `p=2`/exponent-eight sibling excluded.

# Bounded outcome

`RANK4-NONSPLIT-H3-CENTRAL-CORRECTION-COHOMOLOGY` is exhausted for exactly the
fixed `p=3` data: kernel `K=3_+^(1+4) x C3^2`, quotient `H_3(3)`, frozen
`A,B,C`, `TX,TY,TZ`, `LX,LY,LZ`, `qX=f2`, `qY=e2`, and the six frozen
noncentral relator representatives. Only the 18 central relator coordinates
were varied.

The independently leased full-family certificate proves that the complete
consistent central-relator image has dimension eight (6,561 rows), the
normalized section-gauge image has rank five (243 rows), and the quotient has
exactly 27 classes. Equality of the 69-dimensional exact-row cochain kernel
and the 69-dimensional zero-relator section-gauge kernel proves that these 27
classes are complete, not merely sampled presentation rows.

The subsequent single leased batch reconstructed a realizing normalized factor
for every one of the 27 representatives and checked an exact group and every
literal cube. Every class has the same target-gate profile:

| classes | order | kernel | quotient | exponent | literal cube image | generated closure | literal image closed? | noncommutativity gate | target hit |
|---|---:|---:|---:|---|---:|---:|---|---|---|
| `0--26` | `59049=3^10` | `2187=3^7` | `27`, frozen `H_3(3)` | exactly `9` | `135` | `729` | no | not run after closure failure | no |

For all 27 classes the exact printed closure outsider is
`(2,1,0,2,2,0,1,0,0,0)`, and the generated-order progression is
`[1,3,9,27,81,243,729]`. The batch's target-equal index list is empty.
The complete per-class stdout and aggregate are in `all27-raw-output.md`.

Because section gauge gives group isomorphisms carrying actual cubes to actual
cubes, failure for one representative excludes its complete 243-row orbit.
The 27 orbits partition all 6,561 feasible rows. Hence **every central
correction in this fixed family fails the literal-power-set subgroup
hypothesis**. This is a bounded family exclusion, not a solution of Problem
21.137.

# Seven-row constraint matrix

| constraint_id | role | fixed-family evidence | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility/quantifier | a counterexample would need one admissible object; a proof would need all objects, while this is one structural family | active universal assertion not answered |
| `21.137-odd-p-not-2` | admissibility | `p=3` | pass for all 27 representatives |
| `21.137-odd-finite-p-group` | admissibility | exact coordinate order `3^10`; kernel `3^7`, quotient `3^3` | pass for all 27 |
| `21.137-odd-exponent-p2` | admissibility | all 59,049 elements checked; ninth powers are one and an order-nine witness exists | pass for all 27 |
| `21.137-odd-power-set-definition` | admissibility | the literal set of all 59,049 cubes was formed; image size 135 | pass for all 27; no generated-power substitution |
| `21.137-odd-power-set-subgroup` | hypothesis | literal image size 135 versus generated closure 729, with explicit outsider | **fail for all 27** |
| `21.137-odd-P-abelian` | target conclusion | leased guardrail tests this only after closure; no class reaches it | not reached; no target-equal object |

# Exact boundary

Established: all 6,561 consistent central-relator rows for the frozen action,
lift, shears, labels, kernel, quotient, and noncentral representatives are
excluded by exact literal-cube nonclosure.

Not established: any other compatible automorphism lift or shear, different
outer action, changed labels/noncentral representatives, different kernel or
nonabelian quotient, odd prime other than three, or the unrestricted theorem.

# Ranked genuinely new next-strategy portfolio

1. **Change the automorphism-lift orbit before cohomology.** Classify compatible
   lift/shear solutions for the same `K` and `H_3(3)` that are not conjugate to
   the frozen `A,B,C/T/L` row. The first hard gate should be a section-invariant
   quotient cube-label/support calculation; open a factor system only for a
   lift whose support can be a `3`-power-sized subgroup and contains two
   nonorthogonal labels. This changes the datum proved exhausted here.
2. **Change the nonabelian exponent-three quotient.** Keep the reviewed rank-four
   kernel bounds but replace `H_3(3)` by one explicitly frozen nonabelian
   order-81 quotient/action orbit. Before any cocycle enumeration, compute the
   complete projected norm-label set and kill the row unless it is subgroup
   shaped and large enough for noncommuting fibres. This crosses a quotient
   boundary rather than reopening central rows.
3. **Proof-direction fibre obstruction.** Abstract the uniform batch phenomenon
   `|P|=135` and `|<P>|=729` into a theorem: for nonsplit extensions of this
   kernel by exponent-three nonabelian quotients, determine whether two
   nonorthogonal cube labels force a fibre count divisible by a non-`3` factor
   or an explicit closure outsider. The hard gate is a hand-derived fibre
   identity independent of the frozen lift; without that identity, stop rather
   than generalize the computation.

Recommendation: route item 1 to a fresh MathExpert/Lead choice. It most directly
changes the exact datum exhausted here while retaining the strongest reviewed
order and label constraints. No next strategy is executed in this lane.
