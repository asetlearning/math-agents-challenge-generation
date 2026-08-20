---
title: "Triage — Kourovka 21.137 — CTH-3-5 integral identity"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/draft]
---

# Triage — CTH-3-5 integral identity

## Claim restated

For every finite (3)-group (G) of exponent exactly (9) and nilpotency class at most (5), if the actual cube-value set (P=\{g^3:g\in G\}) is a subgroup, then (P) is abelian; the claimant proposes to prove this by an integral Hall identity in the relatively free two-generator class-(5) nilpotent group.

This is a strict partial result inside revision 2. It does not claim the unrestricted odd-prime theorem.

## Locked scope and source clause matrix

- Scope: `21.137/odd-prime-exponent-p2`
- Assignment revision: `2`
- Exact active target: for every odd prime (p) and every finite (p)-group (G) of exponent exactly (p^2), if the set of actual (p)-th powers is a subgroup (P\le G), then (P) is abelian.
- Excluded scopes: the general powerfulness question; the separate (p=2), exponent-(8) square-set question; every group whose exponent is not exactly (p^2).

The rendered source page 184 was inspected directly.

| source row | source content | active? | submission coverage |
|---|---|---:|---|
| `c-general` | If (p)-th powers in a finite (p)-group form a subgroup, must it be powerful? | no | not addressed |
| `c-odd` | For (p\ne2), exponent (p^2), if (p)-th powers form a subgroup, must it be abelian? | yes | only (p=3), class at most (5) |
| `c-two` | For a (2)-group of exponent (8), if squares form a subgroup, must it be abelian? | no | not addressed |

`active_assignment_answered: pending` for the triage gate; even a fully valid partial-family proof must end with `active_assignment_answered: no` because (p>3) and class (>5) remain open.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required source condition | value/use in submitted family | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd (p,G) | only (p=3), with extra class bound (\operatorname{cl}(G)\le5) | fails unrestricted target; defines a legitimate partial family |
| `21.137-odd-p-not-2` | admissibility | (p>2) prime | (p=3) | pass for partial family |
| `21.137-odd-finite-p-group` | admissibility | finite (p)-group for that same (p) | finite (3)-group | pass for partial family |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly (p^2) | exponent exactly (9) | pass for partial family, subject to specialization audit |
| `21.137-odd-power-set-definition` | admissibility | actual values (P=\{g^p:g\in G\}), not only (G^p) | all four terminal elements must be derived from actual cubes using subgroup and conjugacy closure | pending hostile membership audit |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set (P) is a subgroup | used for products, inverses, conjugates, and commutators | pass as a hypothesis for the stated family; each use pending audit |
| `21.137-odd-P-abelian` | target conclusion | (P) abelian | proposed consequence of ([x^3,y^3]=1) for arbitrary (x,y) | pending identity and specialization audit for partial family; unproved unrestricted |

## Target versus proof vehicle

- Source target object: every finite odd-prime (p)-group satisfying the exact exponent and actual-power-set subgroup hypotheses.
- Submitted partial target objects: every finite (3)-group of exponent (9), class at most (5), satisfying the actual-cube-set subgroup hypothesis.
- Proof vehicle: (F=F(x,y)/\gamma_6F), the relatively free two-generator nilpotent group of class at most (5), with the stated commutator convention and Hall coordinates.
- `proof vehicle universally specializes to partial target`: pending line-by-line audit. The intended justification is the defining universal property: each (x,y\in G) induces a homomorphism (F\to\langle x,y\rangle) when (\operatorname{cl}(G)\le5). This proves transfer of a genuine word identity, but does not remove the family restrictions.
- Circularity preflight: the proof vehicle is imposed only by the extra nilpotency-class hypothesis, not by the desired abelianity. Membership of terminal elements may nevertheless become circular if it silently replaces the actual value set by the verbal subgroup; that is a designated hostile check.

## Sub-claim decomposition

1. The fixed commutator convention yields the claimed Hall/Jacobi signs, especially ([\gamma,x]=t\varepsilon).
2. The collections of (A=[y,x^3]) and (B=[x,y^3]), including all central corrections, are exact in (F).
3. (T_A,S_A,T_B,Q) each belong to the actual cube-value set (P) after specialization, using only displayed cube values, conjugacy invariance, and the assumed subgroup closure.
4. The collections of (v_1,v_2,v_3) and ([v_2,v_1]) are exact, with no omitted weight-(le5) term.
5. The resulting coordinates of (C=[x^3,y^3]), notably (\delta^{51}\varepsilon^{27}), are exact.
6. The lifted identity (I) follows integrally from those collections; no merely mod-(3) span relation is being mistaken for an integral equality.
7. Exponent (9) kills every ninth-power factor, while (z\in P\Rightarrow z^3=1), so the four terminal cubes vanish.
8. Since every actual cube is (x^3), the identity for arbitrary (x,y) proves the partial-family (P) abelian.
9. The proof vehicle universally specializes to every group in the partial family.
10. The unrestricted revision-2 target is not answered.

## Tool probe

Verbatim probe results:

```text
gap:
/usr/bin/gap
4.12.1
exit_code=0

sage:
exit_code=1

python3:
/usr/bin/python3
Python 3.12.3
exit_code=0

magma:
exit_code=1
```

No algebraic computation is authorized without a Lead lease. The planned verification is hand reconstruction only.

## Methods inventory

| sub-claim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | derive group commutator identities from the fixed convention and graded Jacobi, tracking the group/Lie sign correspondence | the sign and terminal Hall relation in class (5) | any lower collection formula not separately checked |
| 2, 4, 5 | independent hand collection by conjugate recurrences and weight filtration | the displayed integral normal forms through weight (5) | correctness outside class (5), or any (p>3) statement |
| 3 | trace each element to explicit cube values and allowed normal-subgroup operations | actual-value membership under the stated closure hypothesis | that cube values form a subgroup without the hypothesis |
| 6 | expand both sides of (I) in the fixed Hall coordinates | equality in (F), hence after homomorphic specialization | any identity in class (>5) |
| 7, 8 | elementary exponent/order argument | vanishing and abelianity in the partial family | unrestricted active target |
| 9 | universal-property argument for (F/\gamma_6F) | transfer to every two-generated subgroup of a class-(le5) group | finiteness or exact exponent; those remain separate hypotheses |

## Hard limits and recommendation

The hand audit can completely accept or refute the submitted (p=3), class-at-most-(5) partial theorem. It cannot establish any (p>3) or class-(>5) case and cannot answer the unrestricted revision-2 assignment. No missing general-purpose tool blocks the permitted hand audit.

Recommendation: full line-by-line verification of the strict partial result only. Keep `active_assignment_answered: no` regardless of whether the partial identity survives.
