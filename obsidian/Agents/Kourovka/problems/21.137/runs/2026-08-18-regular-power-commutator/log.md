---
title: "Problem 21.137 proof lane — REGULAR-POWER-COMMUTATOR log"
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

# REGULAR-POWER-COMMUTATOR log

## Exact active scope

`p` is an odd prime `p>2`; `G` is a finite same-`p` group; `exp(G)=` exactly `p^2`; `P={g^p:g in G}` is the literal actual `p`th-power value set, not merely the generated subgroup; `P` itself is assumed a subgroup; ask whether `P` is abelian. The separate `p=2`/exponent-`8` clause is excluded.

Scope: `21.137/odd-prime-exponent-p2`, revision `2`.

## Source and discovery-blind gate

- Rendered source PDF page 184 was visually inspected. The active clause reads: for `p != 2`, if the `p`th powers in a finite `p`-group of exponent `p^2` form a subgroup, must that subgroup be abelian? This agrees with every canonical constraint.
- `source_transcription_checked: yes`.
- `active_scope_checked: yes`.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- No web, solution lookup, historical solution-bearing artifact, `p=2` example, or computation was used.
- The configured corpus path named in the generic protocol has no issue-21 JSONL in this vault. The current rendered source and independently audited revision-2 scope record are the controlling records; no statement was inferred from a corpus mangle.

## Clause matrix

| source clause | active? | treatment |
|---|---:|---|
| actual `p`th powers form a subgroup; must it be powerful? | no | excluded |
| `p>2`, exact exponent `p^2`, actual powers a subgroup; must it be abelian? | yes | candidate derivation for the structured Hall-regular subfamily; unrestricted clause remains open |
| `p=2`, exponent `8`, squares a subgroup; must it be abelian? | no | excluded |

## Strategy portfolio

No computation was authorized. Within the assigned route the ranked portfolio was:

1. Theoretical: expand the exact Hall-regularity identity on a normal exponent-`p` subgroup and test whether it centralizes pth powers.
2. Structural: derive from that identity, rather than cite, that the actual pth-power values of a regular group are closed.
3. Minimum-counterexample audit: combine nonabelianity of the literal power subgroup with an actual root to exhibit a two-element failure of Hall regularity.
4. Certificate: a line-by-line identity using only the Hall definition, nilpotence, exact exponent, and literal actual-valuedness.

Catalogue and computational modes were excluded by the Lead decision.

## Active-time ledger

| UTC | route minute | official cumulative minute | event |
|---|---:|---:|---|
| 2026-08-18T00:49:30Z | 0 | 742 | charged work begins after reading the Lead decision |
| 2026-08-18T00:55:49Z | 7 | 749 | gate A reached: complete normal-exponent-`p` identity and structured-family implication obtained |
| 2026-08-18T01:07:45Z | 18 | 760 | charged writing/sign audit ends; route hard-kills beyond the partial theorem; 5 minutes returned |

## Route-minute-7 gate: outcome A

I obtain a candidate complete derivation of the proposed structured-family implication. With the standard Hall identity defined below, the derivation makes every finite Hall-regular `p`-group of exponent dividing `p^2` have abelian `G^p`; in particular it covers every in-scope Hall-regular group. It does not assume class `<p`, powerfulness, central powers, or a power-commutator inclusion.

## Precise definition used

For a finite `p`-group `G`, write `H'= [H,H]`. I call `G` **Hall-regular** when for every `x,y in G` there are finitely many elements

`c_1,...,c_r in <x,y>'`

such that the exact identity

`(xy)^p = x^p y^p c_1^p ... c_r^p`                                              (R)

holds. The empty product is allowed. This formulation is inherited by subgroups because `<x,y>'` is unchanged when the same pair is viewed inside a subgroup.

## Lemma 1: actual pth powers are closed in a finite Hall-regular group

Let `Pow_p(G)={x^p:x in G}`. I derive closure from (R).

Induct on `|G|`. The abelian case is immediate. To multiply `x^p` and `y^p`, put `H=<x,y>`. If `H<G`, induction inside the regular subgroup `H` applies. Hence assume `H=G` and let

`gamma_1(H)=H`, `gamma_(i+1)(H)=[gamma_i(H),H]`.

By (R),

`(xy)^p=x^p y^p c_1^p...c_r^p`, with every `c_j in gamma_2(H)`.

The proper subgroup `gamma_2(H)` is regular, so induction says its actual pth powers are closed. Thus `c_1^p...c_r^p=d_2^p` for some `d_2 in gamma_2(H)`. Set `h_2=xy d_2^(-1)`. Applying (R) to `xy,d_2^(-1)` gives

`h_2^p=x^p y^p d_3^p`

for some `d_3 in gamma_3(H)`: indeed the main factors `d_2^p d_2^(-p)` cancel adjacently, all new correction elements lie in `<xy,d_2>' <= gamma_3(H)`, and induction combines their pth powers into one.

Repeat. If `h_i^p=x^p y^p d_(i+1)^p` with `d_(i+1) in gamma_(i+1)(H)`, put `h_(i+1)=h_i d_(i+1)^(-1)`. Formula (R) pushes the remaining correction into `gamma_(i+2)(H)`, because `d_(i+1)` is central modulo that term. Nilpotence terminates the process, giving an `h` with

`h^p=x^p y^p`.

Inverses satisfy `(x^p)^(-1)=(x^(-1))^p`. Hence `Pow_p(G)` is a subgroup and therefore equals the generated power subgroup `G^p`.

## Lemma 2: a normal exponent-p subgroup centralizes all pth powers

Let `N normal G`, `exp(N)<=p`, and assume (R). For `n in N`, `g in G`, the quotient `<n,g>/(N intersect <n,g>)` is cyclic. Therefore

`<n,g>' <= N`.

Apply (R) to `n,g`. Since `n^p=1` and every correction element lies in `N`,

`(ng)^p=g^p`.                                                               (1)

Now `ng` commutes with its own power `(ng)^p=g^p`, while `g` commutes with `g^p`. Since a centralizer is a subgroup,

`n=(ng)g^(-1) in C_G(g^p)`.

Thus

`[N,G^p]=1`.                                                                (2)

This is the required power-commutator identity; it has been derived directly from (R).

## Structured-family theorem

Suppose `G` is finite Hall-regular and `exp(G)` divides `p^2`. Lemma 1 gives

`P=Pow_p(G)=G^p` as a characteristic subgroup.

Every `u in P` is literally `u=x^p`, so `u^p=x^(p^2)=1`; hence `exp(P)<=p`. Apply Lemma 2 with `N=P`. It yields

`[G^p,G^p]=[P,P]=1`.

For the active scope the exponent is exactly `p^2` and `p>2`, so this yields `P` abelian for the complete Hall-regular subfamily, pending independent audit. (The derivation happens to need only exponent dividing `p^2`; no inference about the excluded sibling clause is made.)

## Exact irregularity certificate in every hypothetical counterexample

Now use only the active hypotheses and suppose `P` is nonabelian. Choose `a,b in P` with `[a,b] != 1`. Literal actual-valuedness gives a root `g in G` with `g^p=b`. Since `P` is characteristic and every member is an actual pth power, `P normal G` and `exp(P)<=p`.

Let `H=<a,g>`. The quotient `H/(H intersect P)` is cyclic, so

`H' <= P`, hence `(H')^p=1`.                                                  (3)

If the Hall identity (R) held for this single pair `a,g`, its correction elements would lie in `H'`, and (3), together with `a^p=1`, would force

`(ag)^p=g^p=b`.                                                              (4)

But (4) is impossible: `ag` would commute with its own power `b`, and `g` commutes with `b=g^p`; hence `a=(ag)g^(-1)` would commute with `b`, contrary to the choice of `a,b`.

Consequently the pair `(a,g)` is an explicit Hall-irregularity witness. More algebraically,

`Delta(a,g)=(a^p g^p)^(-1)(ag)^p=b^(-1)(ag)^p != 1`,

while `(<a,g>')^p=1`; therefore

`Delta(a,g) notin (<a,g>')^p`.

Here the superscript `p` on the subgroup denotes the subgroup generated by pth powers. This is exactly the negation of (R), not merely a failure of a sufficient auxiliary condition.

There is a little more exact information. Both `(ag)^p` and `b=g^p` belong to the literal subgroup `P`, so `Delta(a,g) in P`; because every member of `P` is an actual value, `Delta(a,g)` is itself an actual pth power. It is also noncentral already in `H=<a,g>`. If `Delta` centralized `H`, then `ag`, which centralizes `(ag)^p=b Delta`, would centralize `b`; since `g` centralizes `b`, so would `a=(ag)g^(-1)`, again contradicting `[a,b]!=1`. Thus the forced certificate has

`Delta in (P intersect H) minus Z(H)`, `Delta` an actual pth power, and `(H')^p=1`.

## Interaction with the reviewed minimum-counterexample reduction

In the reviewed minimum counterexample, `P'=N<=Z(G)` and `|N|=p`. Choose `a,b in P` so that `[a,b]` is a nonidentity element (hence a generator) of `N`, then choose `g^p=b`. The same pair `(a,g)` gives

- `(<a,g>')^p=1`;
- `[a,g^p]=[a,b]` generates the reviewed monolith `N`;
- `b^(-1)(ag)^p != 1`, so the Hall identity fails already on this two-element subgroup.

Thus the reviewed reductions do not force Hall regularity; they force a concrete contradiction to it if the hypothetical minimum counterexample exists. This certificate does not eliminate irregular groups and therefore supplies no bridge to the unrestricted target.

The central monolith sharpens the certificate. Put `h=ag`, `n_0=[a,b]`, and retain `Delta=b^(-1)h^p`, so `h^p=b Delta`. With the reviewed commutator convention,

`[h,b]=[ag,b]=[a,b]^g[g,b]=n_0`,

because `g` commutes with `b=g^p` and `n_0 in N<=Z(G)`. Since `h` commutes with `h^p=b Delta`,

`1=[h,b Delta]=[h,Delta][h,b]^Delta=[h,Delta]n_0`.

Therefore

`[h,Delta]=n_0^(-1)`, a generator of `N`.                                (5)

So every reviewed minimum counterexample would contain the exact configuration

- `Delta` is a literal actual pth power of order `p`;
- `<h,Delta>'=N<=Z(G)` and `[h,Delta]` is specified by (5);
- nevertheless the Hall-defining pair that fails is `(a,g)`, for which the allowed correction subgroup has trivial pth powers.

There is no contradiction here: the class-two subgroup `<h,Delta>` need not contain a pth root of `Delta`. Thus (5) strengthens the irregularity certificate but does not smuggle in the missing global root constraint.

## Internal gap audit

I separated two logical levels so that a possible objection to the stronger notation `G^p` cannot contaminate the active-family result.

1. **Active Hall-regular subfamily.** Here literal `P` is already assumed a subgroup. Characteristicity makes it normal, literal actual-valuedness plus `exp(G)=p^2` makes `exp(P)<=p`, and Lemma 2 alone gives `[P,P]=1`. This part does not use Lemma 1 at all.
2. **Stronger proposed implication.** To read `G^p` conventionally as the generated subgroup without separately assuming literal closure, Lemma 1 is needed. Its induction was checked for the following possible leaks:
   - every subgroup invoked is regular because (R) is pair-local;
   - `gamma_i(H)<H` for `i>=2` in the nonabelian finite p-group, so the order induction is legitimate;
   - at correction depth `i`, `<h,d_i>'<=gamma_(i+1)(H)` because `d_i` is central modulo `gamma_(i+1)(H)`;
   - the factors `d_i^p d_i^(-p)` are adjacent in the ordered Hall identity, so no commutation is smuggled into the cancellation.

The only bridge still absent is from literal power-set closure to the pair-local Hall identity. The exact defect `Delta(a,g)` shows why that missing bridge contains the whole difficulty: a counterexample must have a coset `Pg` on which the pth-power map is not constant even though its image remains inside the subgroup `P`.

## Strategy hard kill and returned time

The regularity route has reached its exact target-facing limit. It derives the Hall-regular theorem and the weaker `P x G` pair-local theorem, but a hypothetical counterexample necessarily violates that very pair-local identity by the explicit noncentral actual-power defect `Delta`. The reviewed minimum-counterexample structure makes the defect pair onto the central monolith via (5), yet leaves a consistent class-two subgroup whose missing root lies outside it. Continuing with regular-group identities would therefore assume away the exact configuration that remains to be excluded.

`REGULAR-POWER-COMMUTATOR` is hard-killed beyond this `PARTIAL_RESULT`; this is not a scope park. Charged use is `18` active minutes, official cumulative `742--760`; `5` authorized minutes are returned to Lead.

## What this does not establish

- It does not prove that every group in the active scope is Hall-regular.
- The actual-power-set subgroup hypothesis by itself does not imply (R) by anything derived here.
- It does not eliminate the exact irregularity certificate above.
- It does not prove the universal active conclusion and constructs no counterexample.
