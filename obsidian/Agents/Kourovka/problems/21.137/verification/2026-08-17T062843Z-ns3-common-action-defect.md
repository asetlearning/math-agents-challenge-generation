---
title: "Verification — Kourovka 21.137 — NS3 common action defect"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Every one of the 3^10 labelled central-correction rows in NS3-FIXED-OUTER-ACTION/F_3^10 violates the same necessary right-action equation at (h,j)=(y,x)."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the set P={g^p:g in G} is a subgroup, then P is abelian."
excluded_scopes: ["the general powerfulness clause", "21.137/two-group-exponent-8 and every p=2 case", "every extension family other than NS3-FIXED-OUTER-ACTION/F_3^10"]
target_object: "All finite odd-prime p-groups of exponent exactly p^2 whose complete actual p-th-power value set is a subgroup"
witness_object: "The frozen p=3 abstract-kernel data Q=H_3(3) x C_3^2, H=H_3(3) x C_3, action representatives A,B,C,T, and ten central factor labels"
witness_equals_target: false
citation: "Kourovka Notebook, 21st issue (2026), Problem 21.137, rendered PDF p. 184"
verification_method: "rendered-source audit; independent hand reconstruction over F_3; supplied Python checker rerun as corroboration only"
tools_used: ["GAP 4.12.1 (probe only)", "Python 3.12.3 (claimant checker corroboration only)", "GNU sha256sum"]
scope_answered: ["NS3-FIXED-OUTER-ACTION/F_3^10 only; this is not a canonical source scope"]
scope_not_answered: ["21.137/odd-prime-exponent-p2", "all repaired, enlarged, or different extension families", "all other odd primes"]
active_assignment_answered: no
operational_outcome: STRATEGY_EXHAUSTED
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/group-extensions, project/kourovka, status/conjectured]
---

# Verification — NS3 common action defect

## The claim

The bounded claim is accepted exactly as stated:

> In the frozen `NS3-FIXED-OUTER-ACTION/F_3^10` family, all `59,049`
> labelled central-correction rows fail the same necessary action identity at
> `(h,j)=(y,x)`.  Hence no row defines the proposed extension.

This is an operational `STRATEGY_EXHAUSTED` verdict for one named family.  It
is not a proof or counterexample for the active Kourovka clause.

## Scope, revision, and clause matrix

The rendered source at PDF page 184 and the canonical record agree.  The
current assignment is revision `2` and isolates the odd-prime clause.

| source clause | active? | addressed here | result |
|---|---:|---:|---|
| If the power values form a subgroup, must it be powerful? | no | no | excluded |
| For `p != 2`, exponent exactly `p^2`, must the actual power-value subgroup be abelian? | yes | no; only one frozen `p=3` family is excluded | active assignment open |
| For a `2`-group of exponent `8`, must the square-value subgroup be abelian? | no | no | excluded |
| `NS3-FIXED-OUTER-ACTION/F_3^10` | auxiliary bounded target | yes | exhausted |

`active_assignment_answered: no` is mandatory.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | bounded audit | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible odd prime and group | only a fixed `p=3` factor family | not discharged |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | `p=3` | pass for the family parameter |
| `21.137-odd-finite-p-group` | admissibility | finite group for the same prime | the action contradiction prevents every row from defining a group | no witness produced |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | action equation fails first | not reached |
| `21.137-odd-power-set-definition` | admissibility | complete actual power-value set | no group exists in the family | not reached |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | no group exists in the family | not reached |
| `21.137-odd-P-abelian` | target conclusion | the value subgroup is abelian | no group exists in the family | not reached |

No out-of-scope object is being presented as a counterexample.  A claim-check
JSON is correctly absent because the submitted outcome is `STRATEGY_EXHAUSTED`,
not `CLAIM` or `STALE_MATCH`.

## Target versus analysed object

The source target is the universal odd-prime statement.  The analysed object
is a single deliberately frozen `p=3` abstract-kernel/factor-system family.
Thus `witness_equals_target: false`; the family is useful partial-progress
evidence only.

There is no circularity in the rejection.  If a group with the displayed
lift actions and relations existed, conjugation in that group would have to
satisfy the action identity derived below.  Its failure is therefore a
necessary-condition obstruction, used only in the sound rejecting direction.

## Subclaims and what each method proves

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| commutator and section order | direct group manipulation | the exact factor `u(y,x)` and matrix order | any other factor equation |
| matrices `A,B,C` | hand action on five basis coordinates | the exact common automorphism defect | existence of a group |
| inner representative | class-two commutator formula | the defect is nontrivial and requires `a-b` modulo the centre | consistency after allowing that repair |
| all-parameter quantifier | inspect all ten frozen coordinates | the same contradiction covers every labelled row | any family with noncentral corrections |
| claimant checker | rerun after the hand derivation | computational agreement with the hand calculation | independent replication or any target-facing conclusion |

## Independent hand reconstruction

### Kernel and inner actions

Work over `F_3` in ordered column coordinates `(a,b,u,v,z)` for
`Q=H_3(3) x C_3^2`, with only `[a,b]=z` nontrivial.  For
`r=(r_a,r_b,r_u,r_v,r_z)` and
`q=(q_a,q_b,q_u,q_v,q_z)`, right conjugation gives

```text
r^q = r + (r_a q_b-r_b q_a)z.
```

Thus `Inn(q)` is the identity except for last-row coefficients
`(q_b,-q_a,0,0,1)`.  In particular every central `z`-power has trivial inner
action.

The displayed definitions give

```text
A(r)=(r_a,r_b,r_u-r_b,r_v+r_u,r_z+r_v),
B(r)=(r_a,r_b,r_u+r_a,r_v+r_u,r_z+r_v).
```

Both preserve the only bracket.  Writing `A=I+N_A`, the chain from `b` is
`b -> -u -> -v -> -z`; hence in characteristic three
`A^3=I+N_A^3=Inn(a)`.  Likewise the `B` chain
`a -> u -> v -> z` gives `B^3=Inn(b)`.

With the fixed standard commutator convention in `Aut(Q)`,

```text
C=[A,B]=A^(-1)B^(-1)AB,
C(r)=(r_a,r_b,r_u,r_v+r_a+r_b,r_z+r_a+r_b).
```

Consequently `C^3=I`.  Direct substitution also gives

```text
[C,A]=[C,B]=Inn(a-b).
```

For the zero-central-coordinate convention, this representative is unique:
the last row `(2,2,0,0,1)` forces `q_b=2` and `-q_a=2`, hence
`q=(1,2,0,0,0)=a-b`.

### Quotient, section, and the right-action order

The quotient presentation is

```text
<x,y,c,t | x^3=y^3=c^3=t^3=1, [y,x]=c, c,t central>.
```

Since `[r,s]=r^(-1)s^(-1)rs`, the relation `[y,x]=c` is exactly
`yx=xyc`.  It collects every word to `x^i y^j c^k t^l` with all exponents in
`{0,1,2}`.  Conversely the multiplication

```text
(i,j,k,l)(i',j',k',l')
  =(i+i',j+j',k+k'+j i',l+l')  mod 3
```

realises all `81` such tuples and satisfies the presentation.  Hence the
normal forms are unique and `|H|=3^4=81`.

Let `alpha_h(q)=q^{s(h)}` and define the right factor by

```text
s(h)s(j)=s(hj)u(h,j).
```

Because `q^{gh}=(q^g)^h`, column matrices satisfy

```text
alpha_j alpha_h = Inn(u(h,j)) alpha_(hj).       (1)
```

The normal-form section is `s(x^i y^j c^k t^l)=X^iY^jK^kT0^l`.
For `(h,j)=(y,x)`, the quotient relation gives

```text
yx=xyc,             s(yx)=XYK,
alpha_(yx)=CBA.
```

The order `CBA` is forced: right conjugation by `XYK` applies `A`, then `B`,
then `C`.  This is also why the outer action is an anti-homomorphism.  The
action of the quotient word `[y,x]` is represented by
`ABA^(-1)B^(-1)`, not by the standard automorphism commutator `C`; the two
differ by the inner map found below, so their outer classes agree.

### The decisive frozen relation

The lift relation is

```text
[Y,X]=K z^e_YX.
```

The same commutator manipulation gives

```text
YX=XY[Y,X]=XYK z^e_YX=s(yx)z^e_YX,
```

so `u(y,x)=z^e_YX`.  Equation (1) therefore requires

```text
AB=Inn(z^e_YX)CBA=CBA.                            (2)
```

Hand multiplication from the displayed actions gives

```text
AB =
1 0 0 0 0
0 1 0 0 0
1 2 1 0 0
1 0 2 1 0
0 0 1 2 1

CBA =
1 0 0 0 0
0 1 0 0 0
1 2 1 0 0
1 0 2 1 0
1 1 1 2 1
```

Equivalently, `CBA` adds `r_a+r_b` to the final coordinate relative to
`AB`.  Therefore

```text
AB(CBA)^(-1)=Inn(a-b)
            = identity except for last row (2,2,0,0,1).
```

This map is nonidentity; for example, it sends `a` to `a-z`.  Thus (2) is
false for every value of `e_YX`.  The exact noncentral correction required at
this pair is `a-b`, up to an arbitrary central factor.

### Quantification over all ten parameters

The frozen labels are

```text
(e_X,e_Y,e_K,e_T,e_YX,e_KX,e_KY,e_TX,e_TY,e_TK) in F_3^10.
```

Only `e_YX` occurs in the decisive relation, and it occurs as the central
element `z^e_YX`, whose inner action is the identity for all three values.
The other nine coordinates do not occur at this quotient pair.  Hence the
same contradiction applies to every one of the `3^10=59,049` labelled rows.
No row enumeration or group-element enumeration is needed.

## Corroborating artifact evidence

The checker was not used to derive the proof above.  It was rerun only after
the convention, section order, matrices, defect, and quantifier had been
reconstructed by hand.

Artifact hashes:

```text
$ sha256sum scratch/ns3_fixed_outer_action.py scratch/sign-gate-output.json
dc44143d0649259d5e8065aadeeff5c06e43ad49e24b2b96be3840a68c8b4046  scratch/ns3_fixed_outer_action.py
925e6abf912fca6e53111dba3f5c66d55286ba6c546b10dda45e6e34db4b7254  scratch/sign-gate-output.json
```

Here `scratch/` abbreviates the claimant run directory
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r10-ns3-fixed-outer-action/scratch/`.

The exact rerun command was

```text
python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r10-ns3-fixed-outer-action/scratch/ns3_fixed_outer_action.py --sign-gate-only
```

It returned the same JSON data as the linked
`scratch/sign-gate-output.json`: all ten advertised assertions are `true`,
`left_equals_right` is `false`, the missing inner representative is
`[1,2,0,0,0]`, and both enumeration counters are zero.  A semantic JSON
comparison recorded verbatim:

```text
JSON semantic equality: True
```

The saved JSON is not byte-for-byte raw current stdout: its nested arrays were
whitespace-compacted.  The script stdout hash was
`c61fed4d4bfdb1b7df68c9d858a48e4ac8b3b0af1a76fd3ea480964122a71d10`,
whereas the saved compact JSON has the reported hash above.  This is a minor
artifact-description defect only; the parsed JSON objects are equal and the
checker has no independent evidentiary role in this verdict.

Tool probe:

```text
$ which gap
/usr/bin/gap
$ which sage
[no output]
$ which python3
/usr/bin/python3
$ which magma
[no output]
$ python3 --version
Python 3.12.3
$ gap -q -c 'Print(VERSION,"\n"); QUIT;'
Error, Variable: 'VERSION' must have a value
not in any function at stream:1
$ gap -q -c 'Print(GAPInfo.Version,"\n"); QUIT;'
4.12.1
```

GAP was probed only and played no role in the audit.

## Verdict

`STRATEGY_EXHAUSTED` is justified for exactly
`NS3-FIXED-OUTER-ACTION/F_3^10`.  The contradiction is a hand-checkable
necessary action equation and covers all labelled rows without enumeration.

The canonical tag remains `status/conjectured`, because the unrestricted
revision-2 target is larger than this family and remains unanswered.

## Why this verdict

The right-action order, quotient product, section factor, and automorphism
matrices all lead to the same exact identity.  The required discrepancy is the
nontrivial inner automorphism represented by `a-b`; every allowed correction
at this pair is central and therefore has trivial inner action.  The all-row
quantifier is immediate because nine coordinates are absent and the tenth is
annihilated by `Inn`.

## What is NOT established

- The active odd-prime universal assertion is neither proved nor refuted.
- No admissible finite group, exponent computation, actual cube set, subgroup
  closure test, or abelianity test is produced by this run.
- Nothing is excluded after allowing the required noncentral `a-b` correction,
  changing the representative `C`, adding `<u,v>` corrections, changing the
  outer action, or choosing any other extension family.
- The audit does not assert that inserting `a-b` makes the remaining factor or
  cocycle equations consistent.
- The remaining action, cocycle, `(C5)`, exponent, and cube-set tests were not
  performed because every frozen row already fails the necessary first gate.
- The supplied checker is claimant code and is corroboration, not an
  independent computation.

## What would upgrade it

Only a line-by-line proof of the universal odd-prime clause or a reconstructible
finite odd-prime group passing every canonical admissibility row and violating
the abelian conclusion can answer the active assignment.  Any repaired or
enlarged extension family is a new Lead-authorised experiment, not part of this
verdict.

