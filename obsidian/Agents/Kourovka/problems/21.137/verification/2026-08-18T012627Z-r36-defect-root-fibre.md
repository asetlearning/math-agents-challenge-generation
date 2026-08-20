---
title: "Verification — Kourovka 21.137 — r36 defect root fibre"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Inside the reviewed hypothetical minimum counterexample, (C1)--(C11) force the stated defect orbit, free root-fibre V-torsors, and return law, while (C12) classifies only the formally possible V-equivariant return actions and does not realize a group."
claimant: Problem-21.137-Proof
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the literal set P={g^p:g in G} of actual pth-power values is a subgroup, then P is abelian."
excluded_scopes: ["general powerfulness clause", "21.137/two-group-exponent-8", "every p=2 case", "odd-prime groups whose exponent is not exactly p^2"]
target_object: "Every finite same-p group in the canonical odd-prime exact-exponent-p^2 scope whose literal actual pth-power value set is a subgroup."
witness_object: "No group witness; a conditional configuration in a hypothetical minimum-order counterexample and an abstract V-torsor incidence model."
witness_equals_target: false
citation: "none"
verification_method: "Independent hand derivation, GAP free-group check of the ordered cyclic norm, and arithmetic/chronology check of the corrected ledger."
tools_used: ["GAP 4.12.1", "Python 3.12.3", "Poppler pdftotext 24.02.0 (probe only)"]
scope_answered: []
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.137 — r36 defect root fibre

## The claim

The submission claims only conditional consequences in the named reviewed minimum-counterexample reduction. Starting from the noncentral Hall defect `Delta`, it derives (C1)--(C11): a full conjugacy orbit of actual values, free right-`V` actions on every associated root fibre, exact fibre transports, and a p-step return map with an automatically trivial odd-prime norm. It then classifies the freedom of the resulting **abstract** `V`-equivariant return permutation by (C12).

It does not claim that the abstract incidence data are realizable by a group, that a hypothetical counterexample exists, or that the universal target is answered.

## Scope, revision, and constraint matrix

The canonical lock is `21.137/odd-prime-exponent-p2`, assignment revision `2`.

| constraint_id | role | independent result | status |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | the derivation is conditional inside a hypothetical minimum counterexample | partial only |
| `21.137-odd-p-not-2` | admissibility | oddness is used exactly when `p` divides `p(p-1)/2` | conditional-pass |
| `21.137-odd-finite-p-group` | admissibility | finiteness supplies finite fibres and cyclic orbit arithmetic | conditional-pass |
| `21.137-odd-exponent-p2` | admissibility | root orders divide `p^2`; nontrivial pth powers force exact root order `p^2` | conditional-pass |
| `21.137-odd-power-set-definition` | admissibility | every `R_k` is a literal root fibre, and conjugates of a root remain roots of conjugate values | conditional-pass |
| `21.137-odd-power-set-subgroup` | admissibility | inherited in the reviewed setup; it places `Delta` in the literal subgroup `P` | conditional-pass |
| `21.137-odd-P-abelian` | target conclusion | assumed false conditionally; no contradiction is obtained | unresolved |

The general powerfulness clause and the `p=2`/exponent-`8` sibling are excluded. `active_assignment_answered: no`.

## Target versus witness

The source target is a universal assertion about actual finite groups. This submission exhibits no group at all. Its first object is a hypothetical minimum counterexample; its last object is a finite set with value layers, free `V`-torsors, and permutations. Such an incidence model forgets multiplication, the power map, and the requirement that all displayed actions arise by conjugation in one group. Therefore `witness_equals_target: false` and formal consistency is only a method-limit certificate.

The `status/replicated` verdict below is restricted to the conditional identities and the formal action classification, never to the active scope or to group realizability.

## Fixed convention and reviewed setup

Use

`x^y=y^(-1)xy`, `[x,y]=x^(-1)y^(-1)xy=x^(-1)x^y`.

The named reviewed reduction supplies, conditionally,

`P'=N=<n_0><=Z(G)`, `|N|=p`, `exp(P)=p`,

`[a,b]=n_0`, `g^p=b`, `h=ag`,

`Delta=b^(-1)h^p`, so `h^p=b Delta`, and `[h,Delta]=n_0^(-1)`.

Only these reviewed prerequisites are used.

## (C1)--(C3): value orbit and conjugate roots

Because `[h,Delta]` is central, reversing its arguments inverts it:

`[Delta,h]=[h,Delta]^(-1)=n_0`.

Since `x^y=x[x,y]`,

`Delta^h=Delta n_0`.

Centrality of `n_0` then gives, for every integer `k`,

`Delta^(h^k)=Delta n_0^k`.                                                (C1)

The `p` values are distinct, so the orbit is exactly `Delta N`, of size `p`. As `exp(G)=p^2` and `[h,Delta] != 1`, `|h|` is `p` or `p^2`; the kernel of the action of `<h>` on `Delta` is exactly the powers with exponent divisible by `p`, namely `<h^p>` (trivial when `|h|=p`). This verifies (C2), including the stabilizer orientation.

Because `Delta` is a literal actual power, choose `r^p=Delta`. Conjugation commutes with taking powers, so

`(r^(h^k))^p=(r^p)^(h^k)=Delta n_0^k`.                                  (C3)

Thus this value fibre `Delta N` is filled by conjugates of one root; no root section across unrelated fibres is used.

## (C4)--(C7): root fibres as free right-`V` sets

Put `t_k=Delta n_0^k`, `R_k={x in G:x^p=t_k}`, and `V=<Delta,N>`. The defect is outside `N` because it is noncentral whereas `N<=Z(G)`. Both `Delta` and `N` have exponent `p` and commute, so

`V is isomorphic to C_p x C_p`, and `|V|=p^2`.

For `x in R_k`, the element `x` centralizes its own power `t_k` and centralizes central `N`. Since `Delta=t_k n_0^(-k)`, it centralizes `Delta` and hence all of `V`:

`R_k subseteq C_G(V)`.                                                     (C4)

Consequently, for `v in V`, the factors `x,v` commute and `v^p=1`, giving

`(xv)^p=x^p v^p=t_k`.                                                      (C5)

Right multiplication therefore defines a free action of `V` on `R_k`; freeness is simply `xv=x => v=1`. Hence `R_k` is a disjoint union of right `V`-cosets and `p^2` divides `|R_k|`, proving (C6).

No `t_k` is `1`, since that would put `Delta` in `N`. Every root `x` has nontrivial `x^p` and order dividing `p^2`, so its order is exactly `p^2`.

Finally,

`(x^h)^p=(x^p)^h=t_k^h=t_(k+1)`,

so conjugation by `h` gives bijections `R_k -> R_(k+1)` modulo `p`. This proves (C7), equality of all fibre sizes, and divisibility by `p^3` of their disjoint union.

## (C8)--(C9): exact p-step return

Taking `k=p` in (C1) gives `Delta^(h^p)=Delta`. Since the ordered equality is `h^p=b Delta`,

`Delta^(h^p)=Delta^(b Delta)=(Delta^b)^Delta`.

Conjugation by `Delta` fixes `Delta`; the displayed equality therefore forces `Delta^b=Delta`. Thus `b` commutes with `Delta`, and with central `N`, so

`[b,V]=1`.                                                                (C8)

Every root in every `R_k` centralizes `Delta`. Because `b` also centralizes `Delta`, its conjugate `x^b` still centralizes `Delta`. Therefore the conjugation order is

`x^(h^p)=x^(b Delta)=(x^b)^Delta=x^b`.                                   (C9)

No illicit swap of `b` and `Delta` occurs.

The value orbit already has length `p`, so an `<h>`-orbit of roots has length `p` precisely when `x^b=x`, and otherwise length `p^2`. On `X_k=R_k/V`, conjugation by `h` cycles the layers and the p-step return on `X_0` is induced by `b`. Since `b in P` and `exp(P)=p`, this quotient permutation has order dividing `p`.

If `|h|=p`, then `b Delta=h^p=1`; every root centralizes `Delta`, hence also `b=Delta^(-1)`, and the return is trivial. Arbitrary nontrivial return data occur only in the `|h|=p^2` formal branch.

## (C10)--(C11): displacement and norm order

For `x in R_0`, put

`s_x=x^(-1)x^b=[x,b]`.

Because `b in P` and `P normal G`, this commutator lies in `P`. Both `x` and `b` centralize `V`, so both `x` and `x^b` lie in `C_G(V)`, hence `s_x in C_G(V)`. Therefore

`s_x in P intersect C_G(V)`, and `s_x^p=1`.                               (C10)

The exact ordered norm follows by telescoping, not by commutative collection:

`s_x s_x^b ... s_x^(b^(p-1))`

`= (x^(-1)x^b)((x^b)^(-1)x^(b^2)) ... ((x^(b^(p-1)))^(-1)x^(b^p))`

`=x^(-1)x^(b^p)=1`,                                                       (C11)

since `b^p=1`.

To audit the sign in the class-two collection, put `m=[s_x,b] in P'=N`. The fixed convention gives `s_x^b=s_x m`, not `s_x m^(-1)`. Centrality of `m` yields `s_x^(b^i)=s_x m^i`, hence

`product_(i=0)^(p-1) s_x^(b^i)=s_x^p m^(p(p-1)/2)=1`.

Here oddness is essential: `p` divides `p(p-1)/2`. Thus this particular return norm is automatic and supplies no contradiction. This does not assert that every other group-law or cross-fibre constraint is automatic.

## (C12): exact formal `V`-torsor freedom

Let `B:R_0->R_0` be conjugation by `b`, and `X=R_0/V`. Since `b` centralizes `V`, `B` is `V`-equivariant for the free right action, and `B^p=1`. Let `sigma` be its induced permutation of `X`; then `sigma^p=1`, so `X` is a finite `C_p`-set.

Choose one basepoint `e_x` in each torsor. Equivariance gives unique `q_x in V` with

`e_x^b=e_(sigma x) q_x`.                                                   (C12)

Iteration and `b^p=1` give `sigma^p x=x` and the product of the `q` values around the p-step `sigma` walk equal to `1`. Because `V` is abelian, its order is irrelevant. Thus:

- at a fixed point of `sigma`, the condition is `q_x^p=1`, automatic for every `q_x in V`;
- on a free p-cycle, each `q` occurs once and their product must be `1`.

Changing basepoints to `e'_x=e_x r_x` changes the coordinate to

`q'_x=r_(sigma x)^(-1) q_x r_x`.

On a fixed point this leaves `q_x` unchanged. On a free p-cycle the product-one condition is exactly what permits a recursive choice of the `r_x` making every `q'_x=1`.

Accordingly, **as an abstract V-equivariant permutation**, the return data consist of an arbitrary nonempty finite `C_p`-set, an arbitrary translation in `V` on each fixed quotient torsor, and no essential translation parameter on a free quotient p-cycle. A root has an `h`-orbit of length `p` exactly for a fixed quotient torsor with zero translation; a fixed torsor with nonzero translation or a free quotient p-cycle gives length `p^2`.

This classification is exact at the action-set level.

## Formal-incidence boundary

The preceding word “arbitrary” must not be promoted beyond its stated category. A bare `V`-set with permutations has no multiplication, no map `x -> x^p`, no subgroup `P`, and no elements `s_x=x^(-1)x^b`. It can model the projected orbit, torsor, and return rows, but it cannot literally instantiate all group equations or prove simultaneous realization in a finite `p`-group.

In particular, (C10)--(C11) show that an actual group's return displacement has an automatically satisfied norm; they do not prove that every formal `sigma,q` pair lifts to compatible displacements in one group. The submission explicitly labels its construction a formal incidence model, so no correction is required. Its correct logical use is solely: the orbit/torsor data derived so far do not themselves force a contradiction.

## Ledger audit and implication

The corrected start precedes the corrected stop, both precede this verification, and their elapsed difference is `523` seconds, i.e. eight complete minutes plus 43 seconds. Charging eight complete minutes sends the stated cumulative total from `757` to `765`. The earlier future-dating defect is absent from this r36 ledger.

This verifies chronology and arithmetic only. Active-time provenance and scheduling authority remain Lead's responsibility, and reaching cumulative minute `765` neither proves a mathematical row nor closes the scope.

## Evidence

The clean boundary comprised the canonical scope, the r36 request and its two named refs, and the explicitly named reviewed minimum-counterexample verification. No web, unrelated solution-bearing history, excluded-prime material, common root section, or external citation was used.

The ordered norm was independently checked in the free group for `p=3` and `p=5`:

```text
$ gap -q -c 'F:=FreeGroup("x","b");; x:=F.1;; b:=F.2;; s:=x^-1*x^b;; n3:=Product([0..2],i->s^(b^i));; n5:=Product([0..4],i->s^(b^i));; Print(n3=x^-1*x^(b^3),"\n"); Print(n5=x^-1*x^(b^5),"\n"); QUIT;'
true
true
```

The ledger arithmetic check returned:

```text
523
8.0
765
```

The full mathematical evidence is the hand derivation above.

## Verdict

`PARTIAL_RESULT`; `status/replicated`; `active_assignment_answered: no`.

(C1)--(C11) have the submitted orientation, order, divisibility, and odd-prime norm. (C12) correctly classifies the abstract `V`-equivariant return action, subject to the explicit formal-incidence boundary. No mathematical correction is required.

## Why this verdict

The conjugation convention sends `[h,Delta]=n_0^(-1)` to `Delta^h=Delta n_0`; the right-`V` action is justified because each root centralizes all of `V`; the ordered equality `h^p=b Delta` gives `x^(h^p)=x^b` only after (correctly) showing that both `b` and the roots centralize `Delta`; and the norm telescopes in the submitted order. The classification of equivariant permutations is a complete elementary torsor calculation, while the submission does not mistake it for a group construction.

## What is NOT established

- The universal active conclusion is not proved or refuted.
- No finite group is shown to realize the formal incidence model, and no admissible counterexample is exhibited.
- Not every formal `C_p`-set or translation datum is shown liftable to group multiplication, a power map, and compatible displacements `s_x`.
- No common root section or cross-fibre compatibility is obtained.
- The `|h|=p` branch has trivial return; arbitrary nontrivial return data concern only the formal `|h|=p^2` branch.
- The general powerfulness clause and every `p=2`/exponent-`8` question remain excluded.
- Ledger completion has no mathematical scope implication.

## What would upgrade it

The formal action data would need to be lifted to a reconstructible finite group and then checked against every active admissibility row, or a new group-law/cross-fibre identity would have to rule out every conditional minimum-counterexample configuration. Neither is present.
