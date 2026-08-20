---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: MCO-CENTRAL-COMMUTATOR
---

# Run log — minimal central obstruction

## Active target

Let `p` be an odd prime and `G` a finite `p`-group of exponent exactly `p^2`. If the actual value set `P={g^p:g in G}` is a subgroup, show that `P` is abelian.

All seven canonical constraint rows are active. The general powerfulness clause, the exponent-8 two-group clause, every `p=2` example, and odd-prime groups of exponent other than exactly `p^2` are excluded.

## Active-time ledger

| event | UTC | cumulative active minutes | note |
|---|---|---:|---|
| start | 2026-08-16T17:36:11Z | 145 | Fresh context; began the Lead-directed MCO-CENTRAL-COMMUTATOR experiment. |

Ledger correction: the assignment fixes `STARTED_UTC` as `2026-08-16T17:33:45Z`; that timestamp, rather than the later first shell timestamp, controls this 35-minute segment. Cumulative minute 145 is therefore anchored at `2026-08-16T17:33:45Z`.

## Strategy portfolio

Ranked for the remaining 35 active minutes:

1. **Theoretical / minimal central obstruction.** Audit, in order, quotient value-set closure, preservation of exponent exactly `p^2`, and the minimality inference `P'=N<=Z(G)` for `N<=P' intersect Z(G)` of order `p`. Kill on the first failed implication and freeze by cumulative minute 165.
2. **Root-fibre cocycle observable.** Only if all three reduction gates pass, define one exact canonical observable from actual root fibres and derive a pass/fail consequence for `[P,P]` by cumulative minute 180.
3. **Catalogue and structured construction modes.** Deliberately inactive: computation is forbidden for this run, and the control message forbids reopening finite-catalogue, affine, Hall-span, compatible-root, Jennings, and wreath-shaped routes.
4. **Certificate plan.** A bounded partial result would require line-by-line quotient identities and a complete minimality argument. Any cocycle claim would have to be stated independently of a choice of roots and have an explicit identity forced by value-set closure.

## Control gates

- Quotient closure: determine whether the actual `p`th-power set of `G/N` equals `PN/N` and is a subgroup.
- Exact exponent: determine whether `exp(G/N)=p^2` follows.
- Minimality: determine whether minimality applies and forces `(PN/N)'=1`, hence `P'<=N`, and whether the chosen `N` gives equality.

## Minimal-central-obstruction audit — 2026-08-16T17:40:26Z (about 152/180)

Assume, solely for the reduction, that a counterexample exists and choose one with `|G|` minimum. Then `P` is nonabelian. Because the actual power set is a subgroup, it equals the verbal subgroup `G^p`; it is characteristic in `G`. Also every `a in P` is an actual value `a=g^p`, so `a^p=g^(p^2)=1` and `exp(P)<=p`.

The subgroup `P'` is nontrivial and normal in `G`: it is characteristic in the characteristic subgroup `P`. A nontrivial normal subgroup of a finite `p`-group meets `Z(G)` nontrivially. Hence `P' intersect Z(G)` contains a subgroup `N` of order `p`. In particular,

`N <= P' <= P`, `N <= Z(G)`, and `|N|=p`.

The three hard gates all pass:

1. **Actual-value-set closure in the quotient.** For `Q=G/N`,
   `Pow_p(Q)={(gN)^p:g in G}={g^p N:g in G}=PN/N=P/N`.
   Since `P` is a subgroup and `N<=P`, this is a subgroup of `Q`. This is equality with the actual value set, not merely with its span.
2. **Exponent remains exactly `p^2`.** Certainly `exp(Q)` divides `p^2`. If it did not equal `p^2`, then `exp(Q)<=p`, so `g^p in N` for every `g in G`. Thus `P<=N`; combined with `N<=P`, this gives `P=N`, which is cyclic of order `p`, contradicting the choice of `G` as a counterexample with nonabelian `P`.
3. **Minimality.** The group `Q` is smaller and satisfies the same odd-prime, finite-`p`-group, exact-exponent, and actual-value-set-subgroup hypotheses. Minimality therefore says its actual power subgroup `P/N` is abelian. Hence
   `(P/N)'=P'N/N=P'/N=1`,
   where `N<=P'` was used. Consequently `P'<=N`; together with `N<=P'`, this gives
   `P'=N<=Z(G)` and `|P'|=p`.

Thus any minimum-order counterexample has `P` of exponent `p`, nilpotency class exactly `2`, and central derived subgroup of order `p`. This is a reduction only; it does not establish that a counterexample exists or that the target conclusion holds.

There is also a useful minimality corollary. If `1 != M normal G` and `M<=P` but `N` is not contained in `M`, then the actual power subgroup of `G/M` is `P/M`, the quotient still has exponent exactly `p^2`, and `(P/M)'=NM/M` is nontrivial. This would be a smaller counterexample. Hence every nontrivial `G`-normal subgroup contained in `P` contains `N`. In particular `Z(G) intersect P=N`: an order-`p` subgroup of `Z(G) intersect P` different from `N` would violate this conclusion.

The reduction is now frozen; no Hall/collection reformulation is being reopened.

## Canonical central-extension/root-fibre observable — 2026-08-16T17:44:18Z

Put `Q=G/N`, `A=P/N`, and let `pi:G->Q` be the quotient map. Then `A` is the actual `p`th-power subgroup of `Q`, it is abelian by minimality, and

`P=pi^{-1}(A)`.

Because `N` is central of order `p`, the following root-value map is canonical:

`kappa:Q->P`, `kappa(gN)=g^p`.

It is well-defined: replacing `g` by `gn`, with `n in N`, does not change the power because `(gn)^p=g^p n^p=g^p`. It is onto because every member of `P` is an actual `p`th power. For `a in A`, let

`R_a={u in Q:u^p=a}` and `P_a=pi^{-1}(a) subset P`.

Then `kappa_a:R_a->P_a` is onto for every `a`. This fibrewise surjectivity is exactly the part of actual-value-set closure that survives the central quotient: every one of the `p` central lifts of every quotient power value is itself a power value.

Choose only for coordinates a normalized section `s:Q->G` and write its central factor set

`f(u,v)=s(u)s(v)s(uv)^{-1} in N`.

It obeys the exact cocycle identity

`f(u,v) f(uv,w) = f(v,w) f(u,vw)`.

For `u in R_a`, define the central coordinate

`lambda_a(u)=s(u)^p s(a)^{-1} in N`.

Repeatedly applying the definition of `f` gives the exact cyclic-norm formula

`lambda_a(u) = product_{i=1}^{p-1} f(u^i,u)`.

The original closure hypothesis is equivalent here to

`lambda_a(R_a)=N` for every `a in A`.

Indeed, the lifts of `u` differ by elements of the central exponent-`p` kernel and hence all have the same `p`th power; conversely every `n s(a) in P_a` has a root in `G`. Changing the section translates every value of a fixed `lambda_a` by the same element of `N`, so surjectivity is section-independent even though its scalar coordinates are not.

The commutator obstruction is the skew of the same cocycle on `A`:

`beta(a,b)=f(a,b) f(b,a)^{-1}=s(a)s(b)s(a)^{-1}s(b)^{-1} in N`.

It is independent of the section. Since `P'=N`, a hypothetical minimum counterexample has `beta` nontrivial (indeed its image is `N`), whereas `P` is abelian exactly when `beta(a,b)=1` for all `a,b in A`. This is the requested exact pass/fail test for `[P,P]`.

### Precise obstruction met by the test

The onto conditions on the `lambda_a` do not themselves force `beta=1`. Each `lambda_a` sees only the restriction of `f` along cyclic strings `(u^i,u)`. The desired obstruction is the alternating, rank-two part `f(a,b)f(b,a)^{-1}`. For odd `p`, diagonal/cyclic power data on the exponent-`p`, class-two group `P` are intrinsically blind to that alternating part: `P` can have all element powers equal to `1` while its alternating commutator pairing is nonzero.

Closure supplies a nonempty relation between root fibres—given values over `a` and `b`, their product has some root over `ab`—but it supplies no canonical choice of that root. Also the product of two chosen roots need not be a root of the product of their values. Thus there is no canonical multiplication `R_a x R_b -> R_{ab}` with which to polarize the cyclic norms. Any chosen root section creates an additional choice-dependent cochain; only its skew collapses back to `beta`, the obstruction one was trying to kill. A further argument would have to produce a choice-free cross-fibre identity, not another cyclic power formula.

## Source and staleness gate — 2026-08-16T17:46Z

The configured source PDF was inspected at rendered page 184, including a visual rendering rather than `pdftotext` alone. Correct active-clause transcription:

> For `p != 2`, if the `p`-th powers in a `p`-group of exponent `p^2` form a subgroup, must that subgroup be abelian?

The page separately asks the general powerfulness question and the exponent-8 question for `2`-groups; neither is in the active scope. Problem 21.137 has no star, editor answer, or later comment printed with it on the source page. The vault contains the older issue-20 corpus, not an issue-21 JSONL record from which `answered`, `has_editor_comment`, or `has_later_comment` fields could be read. The source page and the canonical scope record agree, including all seven constraint rows.

| source clause | equivalent formulation | active? | treatment in this run |
|---|---|---|---|
| actual `p`th powers form a subgroup; must it be powerful? | general powerfulness question | no | excluded |
| `p != 2`, exponent `p^2`, actual powers a subgroup; must it be abelian? | odd-prime exact-exponent target | yes | exact target |
| `2`-group, exponent `8`, square set a subgroup; must it be abelian? | separate two-group clause | no | excluded |

`source_transcription_checked: yes`

`active_scope_checked: yes`

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

## Hostile audit strengthening — 2026-08-16T17:50Z

The earlier normal-subgroup corollary does not require `M<=P`. Let `1 != M normal G` and suppose `N` is not contained in `M`. In `G/M` the actual power set is exactly `PM/M`, hence a subgroup. If the quotient exponent dropped below `p^2`, then `P<=M`, contrary to `N<=P` and `N` not contained in `M`. Moreover the image of `P` inside `PM/M` has derived subgroup `NM/M`, which is nontrivial. Therefore `PM/M` is nonabelian and `G/M` would be a smaller counterexample.

Consequently **every nontrivial normal subgroup of a minimum counterexample contains `N`**. Thus `N` is the unique minimal normal subgroup of `G`. Every order-`p` subgroup of `Z(G)` is normal, so it must equal `N`; a finite abelian `p`-group with a unique order-`p` subgroup is cyclic. Hence

`Z(G)` is cyclic, and because `exp(G)=p^2`, `|Z(G)|` is either `p` or `p^2`.

If `|Z(G)|=p^2`, its central generator has `p`th power generating `N`; if `|Z(G)|=p`, the central obstruction `N` has no central `p`th root. This is a genuine structural dichotomy, but neither side was closed in this experiment.

In the `|Z(G)|=p^2` branch, write `Z(G)=<z>` and `z^p=n`, where `N=<n>`. If `g^p=t`, then centrality gives `(gz^k)^p=t n^k`. Thus one root over a quotient value automatically supplies all `p` central lifts of that value. Equivalently, in `Q` the central element `zN` translates each `R_a` while `lambda_a` advances through all of `N`. Therefore the root-fibre surjectivity condition is automatic in this branch once the quotient has actual power set `A`; it cannot force the alternating cocycle `beta` to vanish. Any future use of the root-fibre observable should first either exclude `|Z(G)|=p^2` by a different argument or focus on the `Z(G)=N` branch.

## Stabilizer-commutator test — 2026-08-16T17:52:43Z (about 164/180)

There is a section-free explanation of why root-fibre closure is blind to the nonzero part of `beta`. For `a in A`, choose any `t in P` with `tN=a`, and let

`S_a={g in G : [t,g] in N}`,

the full inverse image in `G` of the stabilizer of `a` under the conjugation action on `A`. Define

`chi_a:S_a->N`, `chi_a(g)=t^{-1}t^g`.

This is independent of replacing `t` by `tn` with `n in N`, and it is a homomorphism because `N<=Z(G)`. Its image is exactly the set of central coordinates swept out by the `S_a`-conjugacy orbit of `t`. If `t=x^p` is one actual value, then every conjugate `t^g=(x^g)^p` is again an actual value. Consequently, whenever `chi_a` is nontrivial, `im(chi_a)=N` and one root value automatically fills the entire central fibre `P_a`.

Because `A=P/N` is abelian, `P<=S_a`. The restriction of `chi_a` to `P` is precisely the row `beta(a,-)` of the commutator pairing (up to the fixed harmless commutator orientation). Hence

`a notin rad(beta)  ==>  chi_a(P)=N  ==>  P_a is automatically filled by conjugates of one power value`.

Thus actual-value-set closure puts no additional root-fibre constraint on any direction where `beta` is already nonzero. Only radical directions can carry new fibre information, and elements outside `P` may still make `chi_a` nonzero there. This is the precise pass/fail diagnosis: the canonical stabilizer observable detects `beta`, but a nonzero result makes closure easier rather than contradictory. It therefore cannot by itself force `[P,P]=1`.

## Stop and outcome — 2026-08-16T17:53:29Z

Target/revision self-check: exact scope `21.137/odd-prime-exponent-p2`, assignment revision `2`; all seven canonical rows remain accounted for. No candidate was treated as an example. The reduction used only the stipulated odd-prime, finite-`p`-group, exponent-exactly-`p^2`, actual-value-set-subgroup hypotheses.

Outcome: `PARTIAL_RESULT`. The three minimum-counterexample gates pass, yielding the monolithic central-extension reduction. The root-fibre experiment met its stop criterion with exact cocycle and stabilizer identities plus a precise obstruction: fibre closure is automatic off `rad(beta)` and, when `|Z(G)|=p^2`, automatic on every fibre. The target conclusion remains unresolved.

No web/history, solution-bearing file, unlisted prior run, computation, delegate, wreath-shaped material, or git operation was used.

| event | UTC | cumulative active minutes | note |
|---|---|---:|---|
| stop | 2026-08-16T17:53:29Z | 165 | Stopped early when the mandated exact canonicity obstruction was obtained; 15 minutes of the cap remain unspent. |
