---
title: "Kourovka 21.137 r37 — class-p-plus-two closure bridge log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: CLASS-P-PLUS-TWO-CLOSURE-BRIDGE
active_minutes_start: 765
active_minutes_cap: 810
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/draft]
---

# Run log

## 2026-08-18T05:17:45Z — work start; cumulative active minute 765

Fresh proof context. The binding target is only the family theorem: for an odd
prime `p`, a finite `p`-group `G` of exact exponent `p^2` and class at most
`p+2`, if the literal value set `P={g^p:g in G}` is a subgroup, then `P` is
abelian. The broader powerfulness clause, the exponent-eight two-group clause,
every `p=2` example, and the unrestricted-class conclusion are excluded.

### Source and discovery-blind staleness gate

The rendered source PDF page 184 was visually inspected. Its odd-prime clause
agrees with canonical revision 2: `p != 2`, finite `p`-group, exponent exactly
`p^2`, literal actual `p`th-power values form a subgroup, conclusion that this
subgroup is abelian. `source_transcription_checked: yes` and
`active_scope_checked: yes`. The canonical source-fidelity audit also passes all
seven rows. Because this is a discovery-blind run, open-web search is forbidden:
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

### Constraint checklist

| constraint_id | use in this run |
|---|---|
| `21.137-odd-forall-p-G` | prove a uniform class-bounded statement for every admissible pair `p,G`, explicitly not the unrestricted class target |
| `21.137-odd-p-not-2` | `p` is an odd prime; binomial divisibility and the `p=3` collision are audited separately |
| `21.137-odd-finite-p-group` | `G` is a finite `p`-group for that same `p` |
| `21.137-odd-exponent-p2` | `exp(G)=p^2`; the reviewed lemma uses the inclusive hypothesis `exp(G)|p^2` |
| `21.137-odd-power-set-definition` | `P` always means the literal image `{g^p}`; generated `G^p` is not substituted |
| `21.137-odd-power-set-subgroup` | for each pair of values `x^p,y^p`, closure supplies some root `z` with `z^p=x^p y^p`; no coherent root choice is assumed |
| `21.137-odd-P-abelian` | show `[x^p,y^p]=1` for all `x,y` in the class-at-most-`p+2` family |

### Reviewed input theorem and exact hypotheses

The canonical Validator artifact
`verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md` proves by hand:
for every odd prime `p`, every group of exponent dividing `p^2` and class at
most `p+1` has pairwise commuting actual `p`th powers. It does not need literal
image closure or finiteness. It explicitly does not cover class `p+2` or the
unrestricted target. In particular, quotienting a present `G` by a central term
is legitimate once exponent and class hypotheses are checked.

### Strategy portfolio

1. Theoretical first: quotient by `gamma_{p+2}(G)`, invoke the reviewed theorem,
   then Hall-collect the one remaining central defect in the literal closure
   equation `x^p y^p=z^p`.
2. Structured obstruction: if the defect survives, identify its exact free
   weight-`p+2` Hall-coordinate module and the equations supplied by varying one
   actual root, without assuming a root section.
3. Small-case audit: do `p=3`, class five directly because multidegrees `(3,1)`
   and `(3,2)` collide with coefficient-one terms. No heavy computation is
   authorized or needed.
4. Certificate plan: a successful family theorem must give an exhaustive Hall
   factor table through weight `p+2`; a failure certificate must exhibit the
   surviving central word with its coefficient and explain why literal closure
   does or does not constrain it.

Theoretical collection is ranked first because it is the exact boundary and is
hand-checkable by Validator.

## 2026-08-18T05:24:30Z — exact Hall reduction at the new boundary

Write `C=gamma_{p+2}(G)`. It is central. In `G/C`, the exponent still divides
`p^2` and the class is at most `p+1`; its literal power set is exactly `PC/C`,
a subgroup. The reviewed theorem therefore gives `[P,P] <= C`.

The separate-degree Newton formula from the reviewed proof remains valid one
weight further. If `b` has mixed multidegree `(r,s)`, its Hall exponent in
`[X^p,Y^p]` is

`f_b(p,p)=sum_(i=1)^r sum_(j=1)^s a_(b,i,j) binom(p,i)binom(p,j)`.

For weight at most `p`, both degrees are below `p`, so `p^2` divides the
coordinate. The same holds at weight `p+1` except for the unique extreme
multidegrees `(p,1)` and `(1,p)`. Every coordinate at weights `p+1` and `p+2`
is at least `p`-divisible: a nonzero summand has `i,j<=p`, and `i=j=p` is
impossible because `r+s<=p+2<2p` for every odd `p`.

Thus, after using `exp(G)|p^2`, only `p`th powers of the two extreme
weight-`p+1` commutators and of weight-`p+2` basic commutators can remain.
The latter are already in `C`, hence contribute elements of `C^p`. For an
extreme weight-`p+1` commutator `e`, apply the reviewed extreme-coordinate
lemma in `G/C`: `eC` lies in the subgroup generated by power values there.
Because the literal set `PC/C` is a subgroup, this generated subgroup is
`PC/C`. Choose `u in P` and `c in C` with `e=uc`. Every element of the literal
set `P` is itself a `p`th power in an exponent-`p^2` group, so `u^p=1`; since
`C` is central, `e^p=c^p`. Hence every surviving factor belongs to `C^p`, and

`[P,P] <= gamma_{p+2}(G)^p`.                                          (R37.1)

In particular, the assigned class-`p+2` theorem follows under the additional
condition `exp(gamma_{p+2}(G))<=p`. Without that condition the collection has
isolated, but not killed, the last defect.

## 2026-08-18T05:24:30Z — literal closure and central root-shift audit

Take actual values `A=x^p`, `B=y^p`, and let `D=[A,B]`. By (R37.1), choose
`c in C` with `c^p=D`. Literal subgroup closure—not generated-subgroup
membership—supplies an element `z` with `z^p=AB`. With the convention
`[u,v]=u^-1 v^-1 u v`, one has `AB=BA D`, hence `BA=AB D^-1`. Both

`(z^A)^p=(z^p)^A=BA`

and

`(z c^-1)^p=z^p c^-p=AB D^-1=BA`.

Therefore the two orderings lead to two permitted roots in the same value
fibre. No hypothesis identifies them. More generally, central multiplication
gives `(g c^k)^p=g^p D^k`, so the actual power image is automatically saturated
along every cyclic subgroup of `C^p`. The literal closure equation is therefore
blind to precisely the residual group `C^p`: killing `D` would require a new
root-fibre rigidity statement, not another choice of roots or a multiplicative
section.

### Separate `p=3` audit

Here `C=gamma_5(G)`. Weights at most three have coordinates divisible by `9`.
At weight four, `(2,2)` is `9`-divisible while the unique `(3,1)` and `(1,3)`
coordinates are `3`-divisible. At weight five, the multidegrees are `(4,1)`,
`(3,2)`, `(2,3)`, `(1,4)`; every Hall coordinate is `3`-divisible, including
both independent `(3,2)` and `(2,3)` directions. The reviewed class-five
formula's weight-five contamination merely changes the chosen central factor
`c` when lifting an extreme weight-four commutator from `G/C`; its cube still
lies in `C^3`. Hence (R37.1) and the root-shift obstruction remain valid at
`p=3` with no hidden coefficient-one survivor.

### Self-check

The scope, odd-prime restriction, exact exponent, finite `p`-group object,
literal value-set definition, subgroup hypothesis, and desired abelianity row
are all still explicit. The result is a class-bounded partial, not the universal
answer, and it does not prove the full class-at-most-`p+2` family because
`gamma_{p+2}(G)` may have exponent `p^2`. The representation is still productive
only up to the exact quotient `C^p`; further Hall collection or arbitrary root
choice cannot remove it.

## 2026-08-18T05:30:00Z — separate `p=3` quotient bridge

There is a stronger branch at the exceptional prime. Put `H=G/P`. Literal
subgroup closure makes `H` an exponent-three group. The exponent-three identity
already makes every two-generator subgroup class at most two: for `a,b in H`,
set `u=b`, `v=b^a`, `w=b^(a^2)`. From `(ab)^3=1` and `(a b^-1)^3=1`,
respectively,

`w v u=1` and `u v w=1`.

Hence `w=u^-1 v^-1=v^-1 u^-1`, so `[u,v]=1`. Since
`[b,a]=b^-1 b^a=u^-1v`, this commutator centralizes `b`; swapping variables
gives the full two-generator class-two assertion. Equivalently, `H` is a
2-Engel group.

The standard elementary 2-Engel lemma gives `gamma_4(H)=1` (its usual
Hall--Witt proof gives nilpotency class at most three). Therefore
`gamma_4(G)<=P`. In class five, every potentially surviving Hall factor in
`[x^3,y^3]` is a cube of a weight-four or weight-five commutator. Its base lies
in `P`, and `P` has exponent three, so every factor dies. This yields the
candidate exceptional-prime family theorem:

`p=3`, `exp(G)|9`, `cl(G)<=5`, literal cubes a subgroup  =>  that subgroup is abelian.  (R37.2)

More generally, the same collection proves for any odd `p` that
`cl(G/P)<=p`, together with `cl(G)<=p+2`, implies `P` abelian: then
`gamma_{p+1}(G)<=P` contains the base of every surviving Hall factor.
The only unexpanded dependency in (R37.2) is the standard 2-Engel class-three
lemma; it is routed for independent reconstruction rather than treated as a
classification black box.

### Light diagnostic command (not proof)

The following sub-ten-second GAP presentation check used only the four displayed
two-generator exponent-three relators and agreed with the hand reduction:

`timeout 10s gap -q -c 'F:=FreeGroup("a","b");; a:=F.1;; b:=F.2;; Q:=F/[a^3,b^3,(a*b)^3,(a*b^-1)^3];; Print(Size(Q)," ",NilpotencyClassOfGroup(Q),"\\n"); QUIT;'`

Observed output: `27 2`. This does not certify the all-generator 2-Engel lemma.

## 2026-08-18T05:33:52Z — work stop; cumulative active minute 781

Charged sixteen complete active minutes from `05:17:45Z` through `05:33:52Z`.
Outcome: `PARTIAL_RESULT`. The prime-uniform result is the exact inclusion
`[P,P]<=gamma_{p+2}(G)^p` plus the central root-shift obstruction; the stronger
`p=3`, class-five theorem and the conditional `cl(G/P)<=p` theorem are submitted
at `status/conjectured`. Twenty-nine authorized minutes remain unused pending
Validator reconstruction and Lead/MathExpert direction. State: `awaiting_lead`.

### Command record

- `pdftotext -f 184 -l 184 -layout "$KOUROVKA_PDF" -` displayed the full
  source page; `pdftoppm` plus visual inspection confirmed the rendered formula
  `p^2`, the restriction `p != 2`, and the separate exponent-eight clause.
- The light GAP presentation command and its exact `27 2` output are recorded
  above. No heavy computation ran and no compute lease was used.
- The configured issue-21 corpus JSONL path was absent; the canonical scope,
  rendered 2026 source page, and passed source-fidelity audit supplied the source
  and flag gate. Open-web staleness remained deferred by discovery-blind mode.
