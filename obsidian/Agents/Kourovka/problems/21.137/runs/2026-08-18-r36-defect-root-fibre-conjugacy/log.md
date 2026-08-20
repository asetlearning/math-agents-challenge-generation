---
title: "Problem 21.137 proof lane r36 — DEFECT-ROOT-FIBRE-CONJUGACY log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: DEFECT-ROOT-FIBRE-CONJUGACY
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# r36 — DEFECT-ROOT-FIBRE-CONJUGACY

## Exact active scope

`p` is an odd prime `p>2`; `G` is a finite same-`p` group; `exp(G)=` exactly `p^2`; `P={g^p:g in G}` is the literal actual `p`th-power value set, not merely the generated subgroup; `P` itself is assumed a subgroup; ask whether `P` is abelian. The separate `p=2`/exponent-`8` clause is excluded.

Scope `21.137/odd-prime-exponent-p2`, revision `2`. No web, computation, solution lookup, common root section, or excluded-prime material is used.

## Corrected active ledger

The Lead conservatively fixes the earlier official cumulative total at minute `757` and rejects every future-dated portion of the earlier report.

| UTC | r36 minute | official cumulative minute | event |
|---|---:|---:|---|
| 2026-08-18T01:08:43Z | 0 | 757 | new decision has been read; newly charged r36 work begins |
| 2026-08-18T01:17:26Z | 8 complete | 765 | live mathematical audit stops after the required threshold; packaging begins uncharged |

Eight complete newly elapsed active minutes are charged. The extra seconds are conservatively unrounded; official cumulative time is `765`.

## Frozen conditional setup

Work inside the reviewed hypothetical minimum counterexample. With the reviewed convention `x^g=g^(-1)xg` and `[x,g]=x^(-1)x^g`, retain

- `P'=N=<n_0><=Z(G)`, `|N|=p`, and `exp(P)=p`;
- `a,b in P`, `[a,b]=n_0`;
- `g^p=b`, `h=ag`;
- `Delta=b^(-1)h^p in P`, so `h^p=b Delta`;
- `[h,Delta]=n_0^(-1)`.

All statements below remain conditional. They do not exhibit a group or settle the universal scope.

## Complete value conjugacy orbit

Centrality of `n_0` converts the last identity to `[Delta,h]=n_0`. Therefore

`Delta^h=Delta n_0`, and `Delta^(h^k)=Delta n_0^k` for every integer `k`.       (C1)

Since `n_0` has order `p`, the orbit is exactly

`Delta^<h> = Delta N`, of size `p`.                                           (C2)

Its stabilizer in the cyclic group `<h>` is the unique subgroup of index `p`, namely `<h^p>` (trivial when `|h|=p`, order `p` when `|h|=p^2`). Thus this particular central fibre is filled by conjugacy alone: if `Delta=r^p`, then

`(r^(h^k))^p=(r^p)^(h^k)=Delta n_0^k`.                                      (C3)

This uses one actual root and conjugacy invariance; it assumes no common section of unrelated root fibres.

## Complete root-fibre transport

Put

`t_k=Delta n_0^k`, `R_k={x in G:x^p=t_k}`, and `V=<Delta,N>`.

The element `Delta` is outside `N` because it is noncentral in `<a,g>` while `N<=Z(G)`. Hence `V` is elementary abelian of order `p^2`.

For every `x in R_k`, the element `x` centralizes its power `t_k` and centralizes `N`. Since `Delta=t_k n_0^(-k)`, it follows that

`R_k subseteq C_G(V)`.                                                       (C4)

Consequently right multiplication by `V` acts freely on `R_k` and preserves the literal pth power:

`(xv)^p=x^p=t_k` for `v in V`.                                               (C5)

Thus every root fibre is a union of full `V`-cosets and

`|R_k|` is divisible by `p^2`.                                                (C6)

Also `t_k` is never the identity, since otherwise `Delta in N`. Hence every member of every `R_k` has order exactly `p^2`, not merely order dividing `p^2`.

Conjugation by `h` gives bijections

`R_k -> R_(k+1)`, `x -> x^h`,                                                (C7)

with indices modulo `p`. Hence all fibre cardinalities are equal, and the union of roots over `Delta N` has cardinality divisible by `p^3`.

## Return monodromy after one value cycle

Equation (C1) gives `Delta^(h^p)=Delta`. Since `h^p=b Delta`, this forces

`[b,Delta]=1`; hence `b` centralizes all of `V`.                              (C8)

Every root in every `R_k` centralizes `Delta`, so on the root union conjugation by `h^p=b Delta` is exactly conjugation by `b`:

`x^(h^p)=x^b` for `x in union R_k`.                                          (C9)

Therefore an `<h>`-orbit of roots has length `p` when its root centralizes `b`, and length `p^2` otherwise. On the quotient sets `X_k=R_k/V`, conjugation by `h` cycles the `p` layers, and the return permutation on `X_0` is the order-dividing-`p` permutation induced by `b`.

Equivalently, when `|h|=p^2`, the root stabilizer inside `<h>` is `<h^p>` exactly for `b`-fixed roots and is trivial otherwise. When `|h|=p`, equation `h^p=b Delta=1` makes the return action trivial and every root orbit has length `p`. These are all possibilities because the value orbit already has length `p`.

For a base root `x in R_0`, put `s_x=x^(-1)x^b=[x,b]`. Normality of `P` and (C4),(C8) give

`s_x in P intersect C_G(V)`, `s_x^p=1`.                                     (C10)

The only forced return equation is

`s_x s_x^b ... s_x^(b^(p-1))=1`.                                            (C11)

But this is automatic: `P` has class two and exponent `p`, so if `[s_x,b]=m in N`, then `s_x^(b^i)=s_x m^i`, and the product in (C11) is

`s_x^p m^(p(p-1)/2)=1`

because `p` is odd and `m^p=1`. Thus the monodromy supplies no contradiction.

## Exact formal freedom that survives

Let `X=R_0/V`. The derived data allow an arbitrary nonempty finite `C_p`-set `X` for the return action `sigma` induced by `b`. There is additional torsor freedom which cannot be discarded. Choose a base root `e_x` in each free `V`-torsor over `x in X`. Since `b` centralizes `V`, its return action has the form

`e_x^b=e_(sigma x) q_x`, with `q_x in V`.                                   (C12)

The condition `b^p=1` says exactly that the product (equivalently, additive sum) of the `q` values around each `sigma`-orbit is `1` (respectively `0`). On a fixed point of `sigma`, this imposes no restriction because `V` has exponent `p`: every translation `q_x in V` is allowed. On a free p-cycle the zero-sum condition can be removed by changing basepoints, but the p-cycle itself remains.

Thus root orbits of length `p` occur only for a fixed quotient torsor with zero translation. A fixed torsor with nonzero translation and every free quotient p-cycle produce root orbits of length `p^2`. The complete formal incidence consists of `p` value layers of free `V`-torsors, the transvection `Delta -> Delta n_0` on `V`, an arbitrary `C_p`-set `X`, and the V-valued return translations (C12).

All these choices respect (C1)--(C11), fibre sizes divisible by `p^2`, and finiteness.

This is a formal incidence model, not a group or counterexample. It pinpoints the missing information: nothing derived controls the `C_p`-set `R_0/V`, its V-torsor translations, or interaction with another noncommuting value fibre. A common root section or an affine multiplicity assumption would erase precisely this permitted monodromy and is not admissible.

## Strategy stop

`DEFECT-ROOT-FIBRE-CONJUGACY` reaches a hard algebraic limit after (C12): conjugacy determines the value fibre, free `V`-torsor structure, and cyclic return law, but the return `C_p`-set and its V-translations remain formally arbitrary. A further step would need a genuinely new cross-fibre identity; assuming a common root section would simply delete the surviving freedom. Outcome: `PARTIAL_RESULT`, `active_assignment_answered: no`. This stops only the named strategy, not the scope.
