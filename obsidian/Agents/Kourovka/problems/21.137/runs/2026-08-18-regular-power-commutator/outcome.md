---
title: "Outcome — REGULAR-POWER-COMMUTATOR"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: REGULAR-POWER-COMMUTATOR
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/regular-p-groups
  - project/kourovka
  - status/conjectured
---

# Outcome — REGULAR-POWER-COMMUTATOR

## Exact active scope

`p` is an odd prime `p>2`; `G` is a finite same-`p` group; `exp(G)=` exactly `p^2`; `P={g^p:g in G}` is the literal actual `p`th-power value set, not merely the generated subgroup; `P` itself is assumed a subgroup; ask whether `P` is abelian. The separate `p=2`/exponent-`8` clause is excluded.

Scope `21.137/odd-prime-exponent-p2`, assignment revision `2`.

## Outcome

`PARTIAL_RESULT`; `status/conjectured`; `active_assignment_answered: no`.

Active ledger: `2026-08-18T00:49:30Z` to `2026-08-18T01:07:45Z`, route minutes `0--18`, official cumulative minutes `742--760`. Five of the authorized 23 minutes are returned on the strategy hard kill described below.

I obtain the following structured-family claim by a self-contained identity, pending Validator audit:

> If a finite `p`-group `G` is Hall-regular and has exponent dividing `p^2`, then the literal pth-power values form the subgroup `G^p`, and `[G^p,G^p]=1`.

Thus the derivation makes every in-scope Hall-regular group have abelian `P`. No bridge from the active hypotheses to Hall regularity was found or assumed. Instead, the same derivation makes every hypothetical counterexample contain an exact two-element Hall-irregularity certificate.

## Hall identity and proof core

Hall regularity means that for every `x,y in G`,

`(xy)^p=x^p y^p c_1^p...c_r^p`, with `c_i in <x,y>'`.                 (R)

The full lower-central induction in the linked log derives from (R), rather than cites, that `Pow_p(G)` is a subgroup and equals `G^p`.

The decisive local identity is stronger and shorter. If `N normal G` has exponent at most `p`, then `<n,g>'<=N` for every `n in N`, `g in G`. Formula (R) therefore gives

`(ng)^p=g^p`.

Both `ng` and `g` centralize `g^p`, so `n=(ng)g^(-1)` centralizes `g^p`. Hence

`[N,G^p]=1`.                                                            (PC)

When `exp(G)|p^2`, every member of the literal subgroup `G^p=Pow_p(G)` has order at most `p`. Taking `N=G^p` in (PC) gives `[G^p,G^p]=1`.

This uses no class bound, powerfulness, central-powers assumption, or unproved inclusion such as `[G^p,G^p]<=(G')^(p^2)`.

## Strongest local version actually needed

For an active-scope group, global Hall regularity is stronger than necessary. It is enough that (R) hold for every pair `(a,g)` with `a in P` and `g in G`. Indeed `P normal G`, `exp(P)<=p`, and `<a,g>'<=P`, so all correction pth powers vanish; then `(ag)^p=g^p`, which forces `[a,g^p]=1`. Literal root-surjectivity onto `P` gives `[P,P]=1`.

Equivalently, any nonabelian `P` forces failure of (R) on at least one such root pair.

## Forced irregularity certificate

Suppose, only conditionally, that an active-scope counterexample exists. Choose `a,b in P` with `[a,b]!=1`, and choose an actual root `g` with `g^p=b`. Put `H=<a,g>`. Then

`H'<=P`, so `(H')^p=1`,

but

`Delta(a,g)=b^(-1)(ag)^p != 1`.

The inequality is exact: equality would make both `ag` and `g` centralize `b`, forcing `a=(ag)g^(-1)` to centralize `b`. Therefore

`Delta(a,g) notin (H')^p=1`,

which is precisely a pairwise failure of Hall's defining identity.

Moreover `Delta(a,g)` lies in `P intersect H`, is itself a literal actual pth power (because `P` is the literal set and a subgroup), and lies outside `Z(H)`. Centrality in `H` would let `ag` centralize `b=(ag)^p Delta^(-1)` and would again force `[a,b]=1`. Thus the obstruction is a noncentral actual-power Hall defect, not just an abstract failed congruence.

In the reviewed minimum-counterexample reduction, choose `a,b` with `[a,b]` a generator of `P'=N<=Z(G)`, `|N|=p`. Then the same root pair satisfies `[a,g^p]=[a,b]` generating `N`, while its Hall correction subgroup has trivial pth powers. The reduction therefore forces, rather than cures, this concrete irregularity witness.

It also fixes the defect's commutator exactly. With `h=ag`, `n_0=[a,b]`, and `h^p=b Delta`, the identities `[h,b]=n_0` and `1=[h,b Delta]` give

`[h,Delta]=n_0^(-1)`.

Thus `<h,Delta>'=N` is central and the defect itself pairs onto the reviewed monolith. This does not close the scope: the class-two subgroup `<h,Delta>` need not contain an actual pth root of `Delta`, so its local regularity does not repair the globally irregular pair `(a,g)`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | proof use / result | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | argument covers every Hall-regular admissible `G`, not every admissible `G` | structured-family theorem and explicit missing bridge | partial only |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | fixed throughout; proof is valid in particular for every scoped odd prime | source/scope gate and identities | pass for covered family |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | finiteness and p-group nilpotence terminate the lower-central correction | Lemma 1 in log | pass for covered family |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | makes every literal pth power have order at most `p`; theorem allows the slightly stronger `exp(G)|p^2` | (PC) specialization | pass for covered family |
| `21.137-odd-power-set-definition` | admissibility | literal value set, not generated subgroup | lower-central induction proves literal closure; every use of `u^p=1` first uses `u=x^p` | Lemma 1 and theorem | pass for covered family |
| `21.137-odd-power-set-subgroup` | admissibility | literal `P` is a subgroup | assumed in the active local lemma; independently automatic in the Hall-regular family | active hypothesis / Lemma 1 | pass for covered family |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | derived only after the extra Hall-regularity hypothesis; no universal bridge | (PC) with `N=P` | unresolved universally |

## Evidence and reproducibility

- Full derivation and audit: `Agents/Kourovka/problems/21.137/runs/2026-08-18-regular-power-commutator/log.md`.
- Reviewed input reduction: `Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md`.
- Mathematical method: hand identities only.
- Computation: none.
- Web or solution lookup: none.
- Excluded sibling clause or examples: none.

## What this does not establish

- It does not show that literal pth-power closure implies Hall regularity, even locally.
- It does not rule out an irregular finite odd-`p` group of exact exponent `p^2` whose literal power set is a nonabelian subgroup.
- It does not establish the universal target, so no `CLAIM` or claim-check file is appropriate.

## Strategy stop

The regularity route is hard-killed beyond this partial theorem. Its only possible universal bridge would be to derive the `P x G` pair-local Hall identity from literal power-set closure, while the exact `Delta` certificate is precisely a failure of that identity and is compatible with the reviewed central-monolith reduction at the identities derived here. This stops only `REGULAR-POWER-COMMUTATOR`; it does not park the active scope.
