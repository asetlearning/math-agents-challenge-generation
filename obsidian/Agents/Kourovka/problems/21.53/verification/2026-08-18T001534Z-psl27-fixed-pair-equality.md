---
title: "Verification — Kourovka 21.53 — PSL(2,7) fixed-pair equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For L=PSL(2,7) and its unique involution class D of size 21, the product-order colours are exactly 2,3,4, so Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma)."
claimant: Problem-21.53
target_statement: "For every finite nonabelian simple group L and every conjugacy class D of involutions in L, if Gamma is the complete product-order-coloured graph on D and p is the second-smallest distinct prime divisor of |L|, then Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)."
excluded_scopes: ["Problem 21.52's induction-by-Aut(L) question", "a union of involution classes", "an arbitrary prime in place of the second-smallest distinct prime", "any inference from this fixed pair to the universal assertion"]
target_object: "For the submitted bounded claim: PSL(2,7) and its one involution conjugacy class; the active source target is the universal class of all admissible pairs."
witness_object: "The faithful eight-point projective-line permutation image of SL(2,7), with the submitted 21 matrix labels mapped into its unique involution class."
witness_equals_target: proven-with-citation
citation: "Self-contained kernel proof for the projective action in this note; no external identification theorem is assumed."
verification_method: "Rendered-source audit, hand proof, and one leased independently written exhaustive Python 3.12.3 permutation-model checker"
tools_used: ["Python 3.12.3", "GNU sha256sum 9.4", "pdftotext/pdftoppm visual source inspection"]
scope_answered: ["bounded instance L=PSL(2,7), D its unique involution class"]
scope_not_answered: ["21.53/two-minimal-prime-colours universal quantifier over every admissible (L,D)"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.53

## The claim

The submitted result is correct as a bounded statement: for
`L=PSL(2,7)` and its unique involution conjugacy class `D`, `|D|=21`, the
complete product-order scheme has precisely the three off-diagonal colours
`2,3,4`, and

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma)`.

This is one admissible equality.  It is not the universal answer requested by
Problem 21.53, so `active_assignment_answered: no`.

## Scope, revision, and clause matrix

I visually inspected the rendered source-PDF page 172.  Problem 21.53 says "in
the notation of 21.52"; that inherited notation makes `L` finite nonabelian
simple, makes `D` one conjugacy class of involutions, and colours the complete
graph on `D` by exact product order.  The source then defines `Aut_t` by a
one-way implication, states the all-label intersection for `Aut(Gamma)`, and asks
for equality using the two minimal prime divisors.  Revision 2 records all of
these features.  The source writes `G` rather than `L` in the last question; the
audited scope treats it as the group inherited through "in the notation of
21.52".

| source clause | revision-2 operational meaning | fixed-pair verification | universal status |
|---|---|---|---|
| inherited 21.52 notation | finite nonabelian simple `L`; one involution class `D`; all unordered pairs coloured by exact `|ab|` | passes for `PSL(2,7)` and its unique 21-element involution class | one pair only |
| `Aut_t` | `tau(E_t) subseteq E_t`; if `E_t` is empty, `Aut_t=S_D` vacuously | the proof uses exactly this one-way convention | does not address other pairs |
| full colour group | intersection over all positive integers, equivalently all occurring labels with absent labels vacuous | occurring labels are exactly `2,3,4` | does not determine other colour schemes |
| question | equality for every admissible pair, with `p` the second-smallest distinct prime divisor | `|L|=168`, so `p=3`, and equality holds here | not answered universally |

No prior 21.53 verification note or solution-bearing history was inspected.  The
clean inputs were the revision-2 scope, rendered source, submitted cycle-7
`partial-result.md`, its `log.md`, and the three artifacts that note explicitly
links.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independent evidence | result |
|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | every finite nonabelian simple `L` and every involution class `D` | the submission deliberately fixes only `PSL(2,7)` and its sole involution class | **not answered** |
| `21.53-L-finite-nonabelian-simple` | admissibility | `L` finite, nonabelian, simple | faithful projective image has order 168; two generators do not commute; each of the five nonidentity conjugacy classes has full normal closure | pass for this pair |
| `21.53-D-single-involution-class` | admissibility | `D` is one conjugacy class and every member has exact order 2 | exhaustive order distribution has 21 involutions; exhaustive class partition has exactly one order-2 class, of size 21 | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | complete simple graph on `D`, coloured by exact product order | all 210 unordered products independently evaluated; certificate, CSV, and displayed matrix agree entry by entry | pass |
| `21.53-Aut-t-definition` | admissibility | one-way preservation, including vacuous absent labels | finite-injection argument below begins with `tau(E_t) subseteq E_t` and treats every absent label as vacuous | pass |
| `21.53-two-minimal-primes` | admissibility | `p` is the least prime divisor above 2 | `168=2^3*3*7`; independently obtained prime list `[2,3,7]` | pass, `p=3` |
| `21.53-full-colour-group-definition` | admissibility | intersection of every colour-preserving set | only `2,3,4` occur; every other positive label contributes `S_D` | pass |
| `21.53-two-colours-determine-all` | target conclusion | full group equals `Aut_2 intersection Aut_p` | complement proof gives `Aut_2 intersection Aut_3 subseteq Aut_4`; reverse containment is definitional | holds for this pair only |

The universal quantifier row is not a failed admissibility condition for this
bounded partial result; it is precisely the active conclusion that this one-pair
calculation does not answer.  It therefore mechanically forces
`active_assignment_answered: no`.

## Target vs witness

Let `Omega=P^1(F_7)`.  A matrix
`A=(a b; c d)` in `SL(2,7)` acts by
`x -> (ax+b)/(cx+d)`, with the usual value at infinity.  If its action is
trivial, fixing infinity gives `c=0`, fixing zero gives `b=0`, and fixing one
gives `a=d`.  Since `det(A)=1`, `a^2=1`, so `A=+I` or `A=-I`.  Conversely both
central matrices act trivially.  Hence the image is faithfully

`SL(2,7)/{+I,-I} = PSL(2,7)`.

The independent checker represented this image as eight-point permutations.  It
generated it from `x -> x+1` and `x -> -1/x`, independently enumerated the full
determinant-one projective image, and checked the two sets agree and have size
168.  Thus the computational witness is the exact group in the bounded claim,
not a finite quotient, cover, or same-order substitute.

The generators do not commute: at `x=0`, applying `x -> -1/x` then translation
gives infinity, whereas applying translation then `x -> -1/x` gives `-1=6`.
So the exact finite witness is nonabelian.

For simplicity, the checker exhaustively partitioned all 168 elements into the
six conjugacy classes

`(order,size) = (1,1), (2,21), (3,56), (4,42), (7,24), (7,24)`.

For one representative of each nonidentity class, it generated the subgroup of
all conjugates and obtained order 168 in every case.  Any nontrivial normal
subgroup contains some nonidentity element, hence its whole conjugacy class and
the subgroup generated by that class.  The computed normal closure is the whole
group, so the normal subgroup is the whole group.  This proves simplicity by a
finite exhaustive certificate distinct from the claimant's normal-class-union
test.

## Sub-claims and what each method proves

| sub-claim | independent method | what the pass proves | what it does not prove |
|---|---|---|---|
| exact group identity | projective-action kernel proof plus equality of generated and full projective permutation images | witness is exactly `PSL(2,7)` | no identification for another group |
| finite, nonabelian, simple | 168-element closure, explicit noncommutation, exhaustive class partition and normal closures | all three object-class requirements for this pair | no classification or family theorem |
| single involution class | orders of every element plus every conjugacy orbit | exactly 21 involutions in one class | anything about another class or group |
| complete colour scheme | exact products for all `21 choose 2=210` pairs | occurring colours are only `2,3,4`, with counts `42,84,84` and valencies `4,8,8` | numerical automorphism-group orders or generators |
| artifact agreement | entrywise check against JSON edge list and matrix, CSV, and the displayed Markdown matrix; external and internal digests checked | the submitted finite certificate is unchanged and agrees with the independent model | truth of any unencoded universal claim |
| two-colour equality | direct finite-set complement proof | equality for this exact scheme under the source convention | equality if a fourth retained-complement colour is not unique |

## Circularity audit

The independent group was constructed from the projective action of
`SL(2,7)`, before the submitted vertex data were read into the comparison.  Its
involutions were selected by independently computed element order and conjugacy,
not by the desired colour relation.  Every product colour was then computed in
that group.  The equality was not certified by feeding a two-colour-derived graph
into an automorphism package; it follows only after the independent complete
colour inventory shows that one complementary colour remains.  The check is not
true by construction.

## Why the source's one-way convention is enough

Let `U` be the finite set of all 210 unordered edges and let `E_t` be its subset
of product-order-`t` edges.  Any `tau in S_D` induces a bijection of `U`.  Under
the source definition,

`tau in Aut_t(Gamma)` implies `tau(E_t) subseteq E_t`.

The restriction is an injection from the finite set `E_t` into itself, hence its
image has the same cardinality and `tau(E_t)=E_t`.  Thus membership in both
`Aut_2` and `Aut_3` means setwise preservation of `E_2` and `E_3`.  The exhaustive
inventory gives

`E_4 = U minus (E_2 union E_3)`.

Therefore `E_4` is also preserved.  These are all occurring colours.  If a
positive integer `t` does not occur, `E_t` is empty and the defining implication
is vacuous, so `Aut_t(Gamma)=S_D`; absent labels add no condition to the
all-label intersection.  Consequently

`Aut_2(Gamma) intersection Aut_3(Gamma) subseteq Aut(Gamma)`.

The reverse containment follows immediately from the definition of the full
colour group.  This establishes the claimed fixed-pair equality under the exact
one-way convention, without computing either automorphism group.

## Evidence

The triage note is
`Agents/Kourovka/problems/21.53/verification/2026-08-18T000152Z-psl27-fixed-pair-equality-triage.md`.
The independently written checker is
`Agents/Kourovka/problems/21.53/verification/scratch/psl27_projective_line_checker.py`.
It was frozen before the lease request:

```text
$ sha256sum Agents/Kourovka/problems/21.53/verification/scratch/psl27_projective_line_checker.py
029b3414192862a705108c1b3368c119acba00f65899edf9eb68c676209b827c  Agents/Kourovka/problems/21.53/verification/scratch/psl27_projective_line_checker.py
```

Lead independently matched that digest and granted exactly one invocation in
`Agents/Kourovka/bus/archive/2026-08-18T001323Z__Lead__DECISION__grant-independent-psl27-checker.md`.
The exact authorized command and complete observed output were:

```text
$ timeout 30s /usr/bin/time -f 'WALL=%e CPU=%P MAXRSS_KB=%M' python3 Agents/Kourovka/problems/21.53/verification/scratch/psl27_projective_line_checker.py
CHECKER_MODEL=faithful permutation action on P^1(F_7)
GROUP_ORDER=168
NONABELIAN_GENERATORS=YES
ELEMENT_ORDER_COUNTS={1: 1, 2: 21, 3: 56, 4: 42, 7: 48}
CONJUGACY_CLASS_ORDER_SIZE=[(1, 1), (2, 21), (3, 56), (4, 42), (7, 24), (7, 24)]
NORMAL_CLOSURE_SIZES=[(2, 21, 168), (3, 56, 168), (4, 42, 168), (7, 24, 168), (7, 24, 168)]
INVOLUTION_COUNT=21
INVOLUTION_CLASS_COUNT=1
PRIME_FACTORS=[2, 3, 7]
SECOND_SMALLEST_DISTINCT_PRIME=3
EDGE_COLOURS=[2, 3, 4]
EDGE_COLOUR_COUNTS={2: 42, 3: 84, 4: 84}
COLOUR_VALENCIES={2: 4, 3: 8, 4: 8}
CLAIMANT_FILE_DIGESTS=PASS
CERTIFICATE_INTERNAL_DIGESTS=PASS
VERTEX_LABELS_AND_ALL_210_PRODUCTS=PASS
CERTIFICATE_MATRIX_CSV_MARKDOWN=ENTRYWISE_EQUAL
E4_IS_COMPLEMENT_OF_E2_UNION_E3=YES
BOUNDED_FIXED_PAIR_ONLY=YES
ALL_CHECKS_PASS
WALL=0.27 CPU=50% MAXRSS_KB=17408
```

The command exited with status `0`.  It was run once only.  Slot 2 was released
immediately; no patch, rerun, alternate target, or automorphism search occurred.
The claimant's independent command, complete output, and artifact hashes remain
in the submitted cycle-7 `log.md`.

## Verdict

`status/replicated` for the precise bounded fixed-pair result.

The claimant's matrix-coset computation and the Validator's separately written
projective-permutation computation agree on the exact group, class, and every one
of the 210 unordered product orders.  The complement argument is correct under
the source's one-way definition.  This certifies equality for the one pair
`(PSL(2,7),D)`.

`active_assignment_answered: no`.

## Why this verdict

Two independent exact implementations agree, one written by the Validator.  The
second uses permutation elements, a different simplicity certificate (normal
closures rather than closed unions of classes), and an entrywise mapping of the
submitted labels.  The self-contained projective-action proof rules out a
target-versus-witness mismatch.  `status/replicated` is the conservative protocol
level: no universal proof or counterexample has been produced, and the
human-gated `status/proven` level is not invoked for this bounded report.

## What is NOT established

- The universal equality for every finite nonabelian simple group and every
  involution conjugacy class is not established.
- No counterexample is supplied; equality holds for this pair.
- No other finite simple group, other involution class, or infinite family is
  covered.
- No numerical order or generators for either automorphism group were computed.
- Problem 21.52's separate assertion about automorphisms induced from `Aut(L)` is
  not addressed.

## What would upgrade it

The active assignment requires either a line-by-line universal proof covering
every admissible `(L,D)`, including vacuous colour cases, or a source-complete
strict-inequality counterexample with an explicit separating permutation.  More
isolated equalities can be valuable partial evidence but cannot upgrade this
fixed-pair result into the universal conclusion.
