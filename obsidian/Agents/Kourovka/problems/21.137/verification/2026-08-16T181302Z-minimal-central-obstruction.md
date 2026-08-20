---
title: "Verification — Kourovka 21.137 — minimal central obstruction"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "If an in-scope counterexample exists, a minimum-order one has the stated monolithic central-extension reduction and root-fibre/stabilizer identities, without settling the unrestricted target."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual value set P={g^p:g in G} is a subgroup, then P is abelian."
excluded_scopes: ["general powerfulness clause", "21.137/two-group-exponent-8", "every p=2 case", "odd-prime groups whose exponent is not exactly p^2", "wreath-shaped material"]
target_object: "Every finite p-group in the rendered odd-prime, exact-exponent p^2 clause."
witness_object: "No exhibited witness; only a hypothetical minimum-order counterexample used for a conditional reduction."
witness_equals_target: false
citation: "none"
verification_method: "Independent hand derivation from the two request refs, canonical scope, and rendered source page only."
tools_used: ["Poppler 24.02.0 for visual source rendering", "read-only POSIX shell utilities"]
scope_answered: []
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137 — minimal central obstruction

## The claim

The submission claims only a conditional reduction: if the rendered odd-prime exact-exponent question has a counterexample, then one of minimum order has `P'=N<=Z(G)` of order `p`, every nontrivial normal subgroup contains `N`, the center is cyclic of order `p` or `p^2`, and the associated central-extension root-fibre and stabilizer maps have the displayed identities. It explicitly does not claim that such a counterexample exists or that all admissible groups have abelian `P`.

## Scope, revision, and clause matrix

The canonical lock is `21.137/odd-prime-exponent-p2`, assignment revision `2`. Rendered page 184 was inspected visually. It asks, in the active clause, whether for `p != 2` the `p`th powers in a finite `p`-group of exponent `p^2`, when they form a subgroup, must form an abelian subgroup. The canonical reading “odd prime” and “exponent exactly `p^2`” agrees with the rendering.

| source clause | active? | result of this submission |
|---|---:|---|
| Actual `p`th powers form a subgroup; must it be powerful? | no | excluded and unanswered |
| `p != 2`, exponent exactly `p^2`, actual powers a subgroup; must it be abelian? | yes | conditional reduction only; unanswered |
| `2`-group of exponent `8`, squares a subgroup; must it be abelian? | no | excluded and unanswered |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independent audit | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | the derivation starts from an arbitrary hypothetical counterexample and minimizes order; it does not prove the universal conclusion | conditional-pass |
| `21.137-odd-p-not-2` | admissibility | `p` is prime and `p>2` | the same odd prime is retained in every quotient; no `p=2` inference is imported | pass |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group | used exactly for minimum order and the normal-subgroup/center intersection | pass |
| `21.137-odd-exponent-p2` | admissibility | `exp(G)=p^2` exactly | gives exponent `p` for nonabelian `P`; quotient exactness is independently derived below | pass |
| `21.137-odd-power-set-definition` | admissibility | `P` is `{g^p}`, not merely its generated subgroup | every quotient and fibre equality below is elementwise; the sole identification with `G^p` is justified by subgroup closure | pass |
| `21.137-odd-power-set-subgroup` | admissibility | the actual value set is a subgroup | used to make `P` characteristic as a subgroup and to make its quotient images subgroups | pass as a hypothesis of the reduction |
| `21.137-odd-P-abelian` | target conclusion | `P` is abelian | no proof is supplied; the reduction assumes the contrary | unresolved |

There is no exhibited group against which the admissibility rows could be checked as witness properties. They are hypotheses in a conditional proof.

## Target versus witness

The target is a universal assertion about every group in the active source class. The submission computes in no group and exhibits no group. Its “object” is a hypothetical minimum-order counterexample. Accordingly:

- `witness_equals_target: false`;
- no witness existence is established;
- no necessary condition is being certified as sufficient;
- the quotient minimality arguments are legitimate only after all active hypotheses and nonabelianity are rechecked, which is done below.

## Conventions for the sign audit

Write

`Pow_p(H)={h^p:h in H}` and `H^p=<Pow_p(H)>`.

For commutators and conjugation use

`x^g=g^{-1}xg`, and `[x,g]=x^{-1}g^{-1}xg=x^{-1}x^g`.

With these conventions the stabilizer restriction below is exactly `beta(a,b)`, not merely “up to orientation.” If the opposite convention `x^g=gxg^{-1}` is used, it is `beta(a,b)^{-1}`. The image, radical, and fibre-filling conclusions are unchanged.

## Minimum-counterexample reconstruction

Assume an in-scope counterexample exists and choose `G` of minimum order. Put `P=Pow_p(G)`. Then `P` is nonabelian.

### 1. Characteristic actual power subgroup and exponent `p`

Every automorphism sends `g^p` to another actual `p`th power. Thus the set `P` is invariant, and because it is assumed to be a subgroup it is characteristic. It also equals the verbal subgroup `G^p`, but only now: a subgroup containing every actual value contains their generated subgroup, while `G^p` is generated by elements already in `P`.

For each `x in P`, actual-valuedness gives `x=g^p` for some `g`, hence

`x^p=g^(p^2)=1`.

Thus `exp(P)<=p`. Since `P` is nonabelian, it is nontrivial, so `exp(P)=p` exactly. This step would not follow merely from `x in G^p` without the equality of `P` with the actual value set.

### 2. Existence of `N<=P' intersect Z(G)`

`P'` is nontrivial because `P` is nonabelian. It is characteristic in characteristic `P`, hence normal in `G`. Under conjugation of the finite `p`-group `G` on nontrivial normal `P'`, every nonfixed orbit has size divisible by `p`, while `|P'|` is divisible by `p`. Therefore the fixed set `P' intersect Z(G)` has order divisible by `p` and is nontrivial. It contains a subgroup `N` of order `p`. Hence

`N<=P'<=P`, `N<=Z(G)`, and `|N|=p`.

### 3. Exact quotient value set

For `Q=G/N`, elementwise—not merely after taking generated subgroups—

`Pow_p(Q)={(gN)^p:g in G}={g^p N:g in G}=PN/N=P/N`,

where the last equality uses `N<=P`. Since `P` is a subgroup, `P/N` is a subgroup. No occurrence of `G^p` is substituted for the actual value set in this calculation.

### 4. Preservation of exact exponent `p^2`

`exp(Q)` divides `p^2`. If it were not exactly `p^2`, then it would divide `p`; hence `(gN)^p=N` for every `g`, so every actual value `g^p` lies in `N`. Therefore `P<=N`. Together with `N<=P`, this gives `P=N`, cyclic of order `p`, contrary to nonabelianity. Thus `exp(Q)=p^2` exactly.

### 5. Minimality forces `P'=N`

`Q` is smaller and retains the same odd prime, finite `p`-group class, exact exponent, and actual-value-subgroup hypothesis. Minimality therefore makes its actual power subgroup `P/N` abelian. Since `N<=P'`,

`(P/N)'=P'N/N=P'/N=1`.

Thus `P'<=N`, and the reverse inclusion was built into `N`; hence `P'=N<=Z(G)` and `|P'|=p`. Consequently `P` has nilpotency class exactly `2`.

### 6. Every nontrivial normal subgroup contains `N`

Let `1 != M normal G` and suppose `N` is not contained in `M`. The quotient has exact actual value set

`Pow_p(G/M)=PM/M`,

which is a subgroup. If `exp(G/M)` were below `p^2`, every `g^p` would lie in `M`, so `P<=M` and then `N<=M`, a contradiction. Thus its exponent is exactly `p^2`.

The power subgroup in the quotient is the image of `P`, so its derived subgroup is exactly

`(PM/M)'=P'M/M=NM/M`.

This is nontrivial because `N` has order `p` and is not contained in `M`. Hence `G/M` would be a smaller counterexample, contrary to minimality. Therefore every nontrivial normal subgroup of `G` contains `N`.

### 7. Unique minimal normal subgroup and cyclic center

`N` is itself minimal normal because it has order `p`; the preceding result makes it the unique minimal normal subgroup. Every order-`p` subgroup of `Z(G)` is normal and must contain `N`, hence must equal `N`. A finite abelian `p`-group with a unique subgroup of order `p` is cyclic (equivalently its order-`p` torsion has rank one). Since `N<=Z(G)` and `exp(Z(G))<=p^2`, it follows that

`Z(G)` is cyclic of order `p` or `p^2`.

In the second case, if `Z(G)=<z>`, then `z^p` generates the unique order-`p` subgroup `N`.

## Central factor set and cyclic norm

Put `A=P/N` and let `pi:G->Q=G/N`. The preceding steps give: `A=Pow_p(Q)` is an abelian subgroup, `N=P'<=Z(G)` has order `p`, and `P=pi^{-1}(A)`.

Choose a normalized section `s:Q->G` and define

`f(u,v)=s(u)s(v)s(uv)^{-1} in N`.

Associating `s(u)s(v)s(w)` in the two possible ways and using centrality of `N` gives, with no inverse or order change,

`f(u,v)f(uv,w)=f(v,w)f(u,vw)`.

For `a in A`, set `R_a={u in Q:u^p=a}` and

`lambda_a(u)=s(u)^p s(a)^{-1}`.

Induction from `s(u^i)s(u)=f(u^i,u)s(u^(i+1))` yields

`s(u)^p=(product from i=1 to p-1 of f(u^i,u))s(u^p)`.

Thus for `u in R_a`, the exact sign and index range are

`lambda_a(u)=product from i=1 to p-1 of f(u^i,u)`.

Centrality makes the displayed product order immaterial, but it is already in the correct inductive order.

## Actual-value closure versus fibrewise `lambda` surjectivity

This equivalence is correct only with the reduced data fixed. Specifically, one must retain `A=Pow_p(Q)` as a subgroup, the candidate subgroup `P=pi^{-1}(A)`, and central kernel `N` of exponent `p`. It is not an unconditional statement about an arbitrary central extension.

For `u in R_a`, every lift has the form `s(u)n`, `n in N`, and

`(s(u)n)^p=s(u)^p=lambda_a(u)s(a)`.

Therefore the actual values lying over `a` are exactly

`Pow_p(G) intersect pi^{-1}(a)={lambda_a(u)s(a):u in R_a}`,

whereas the full candidate fibre is

`P_a=pi^{-1}(a)=N s(a)`.

The actual values fill `P_a` if and only if `lambda_a(R_a)=N`. Since `A` is precisely the quotient's actual value set, every actual value of `G` lies over some `a in A`, and every `R_a` is nonempty. Hence all fibres are filled if and only if `Pow_p(G)=pi^{-1}(A)=P`; because `A` is a subgroup, this equality is exactly actual-value-set closure in the reduced setup.

In the forward direction used by the submission, `P` already is the actual-value subgroup and contains `N`, so `P=pi^{-1}(A)` and every fibre is filled. In the converse direction, fibre filling proves equality with the actual value set, not merely equality after generation.

## Section-change behavior

Let another normalized section be `s'(q)=c(q)s(q)`, where `c(q) in N` and `c(1)=1`. Then the exact formulas are

`f'(u,v)=c(u)c(v)c(uv)^{-1}f(u,v)`

and, because `c(u)^p=1`,

`lambda'_a(u)=lambda_a(u)c(a)^{-1}`.

Thus a section change translates the entire image of a fixed `lambda_a` by the single element `c(a)^{-1}`. The inverse sign is essential; surjectivity is nevertheless invariant.

## `beta` as the commutator pairing

For `a,b in A`, `ab=ba`, and direct cancellation gives

`f(a,b)f(b,a)^{-1}=s(a)s(b)s(a)^{-1}s(b)^{-1}`.

The right side lies in central `N`. In this central-commutator situation it equals `[s(a),s(b)]` under the convention fixed above. Changing either lift by an element of `N` does not change it. Equivalently, the section-change factors in `f'(a,b)f'(b,a)^{-1}` cancel because `ab=ba`. Hence

`beta(a,b)=f(a,b)f(b,a)^{-1}`

is exactly the section-independent commutator pairing `A x A -> N`. Since `P` has class two and exponent `p`, it is alternating and biadditive. `P` is abelian exactly when `beta` is identically `1`. Here `P'=N` of order `p`, so in a hypothetical counterexample `beta` is nontrivial and its value set generates—and, by biadditivity, equals—`N`.

## Central-root automatic-fibre branch

Suppose `Z(G)=<z>` has order `p^2` and put `n=z^p`, so `N=<n>`. For any actual value `t=g^p` and `0<=k<p`, centrality gives the exact identity

`(gz^k)^p=g^p z^(kp)=t n^k`.

For every `a in A`, a quotient root exists because `A=Pow_p(Q)`. Starting from one lift of such a root, multiplication by `z^k` therefore realizes all `p` elements of the central fibre. Equivalently, multiplication by `(zN)^k` stays inside `R_a` and makes the corresponding `lambda_a` values run through `N`. Thus fibrewise surjectivity is automatic in the `|Z(G)|=p^2` branch and imposes no condition on `beta` there. This does not establish that a nonzero `beta` is globally realizable; it only proves that this fibre test cannot exclude it in that branch.

## Stabilizer homomorphism and off-radical filling

For `a in A`, choose `t in P` with `tN=a`, and let

`S_a={g in G:t^{-1}t^g in N}`.

This is the inverse image of the stabilizer of `a` for the conjugation action of `Q` on `A`. Define

`chi_a(g)=t^{-1}t^g`.

Replacing `t` by `tn`, `n in N`, leaves `chi_a` unchanged because `N` is central. For `g,h in S_a`, write `t^g=t chi_a(g)`. Then

`chi_a(gh)=t^{-1}(t^g)^h=chi_a(h)chi_a(g)=chi_a(g)chi_a(h)`.

The last equality uses that `N` is abelian. Hence `chi_a:S_a->N` is a homomorphism. Its image records exactly the central coordinates in the `S_a`-orbit of `t`.

Since `A=P/N` is abelian, `P<=S_a`. For `h in P`, with `b=hN`, central changes of lifts do not affect commutators, so under the fixed convention

`chi_a(h)=t^{-1}t^h=[t,h]=beta(a,b)`.

Thus if `a` lies outside `rad(beta)`, the restriction `chi_a(P)` is nontrivial. Because `|N|=p`, it equals all of `N`. Choose an actual power value `t` over `a`—one exists because `a in Pow_p(Q)`, and under the original closure every lift in `P` is actual. Every conjugate satisfies `t^g=(x^g)^p` when `t=x^p`. Consequently its `P`-orbit fills `tN=P_a` with actual values. Therefore fibres outside `rad(beta)` are filled automatically by conjugation.

The same conclusion survives the opposite conjugation convention because it only replaces `beta(a,b)` by its inverse. Radical membership and the image subgroup are unchanged.

## Actual values versus `G^p` audit

| use | exact status |
|---|---|
| `P=G^p` | valid only because the actual value set is assumed to be a subgroup; the proof states this before using equality |
| quotient by `N` | `Pow_p(G/N)=P/N` is an elementwise image equality |
| quotient by arbitrary `M` | `Pow_p(G/M)=PM/M` is an elementwise image equality |
| `kappa(gN)=g^p` is onto | uses that every member of `P` is an actual value, not merely in the verbal subgroup |
| fibrewise `lambda` condition | reconstructs every actual value in each central fibre; it is stronger than a statement about generated subgroups |
| stabilizer filling | starts from an actual value and uses conjugacy invariance of actual powers |

No illicit replacement of the actual value set by `G^p` occurs after the initial, justified equality.

## Subclaims and what each method proves

| subclaim family | method | what the pass proves | what it does not prove |
|---|---|---|---|
| scope and exclusions | visual source/canonical comparison | the audit concerns exactly revision 2, `p>2`, and exact exponent `p^2` | any excluded clause |
| minimum-counterexample gates | hand quotient derivation | every hypothetical minimum counterexample has `P'=N<=Z(G)`, `|N|=p` | existence or nonexistence of a counterexample |
| monolithic/cyclic-center strengthening | hand normal-quotient derivation | every nontrivial normal subgroup contains `N`; center dichotomy follows | elimination of either center branch |
| factor set, `lambda`, section change, `beta` | hand central-extension identities | exact formulas, signs, and conditional fibre equivalence | an identity forcing `beta=1` |
| central-root and stabilizer tests | hand orbit derivation | automatic filling in the central-root branch and off `rad(beta)` | automatic filling in every radical fibre when `Z(G)=N` |

## Evidence

Only these mathematical sources were used:

1. the specified request;
2. its two refs, `findings.md` and `log.md` in run `2026-08-16-r6-minimal-central-obstruction`;
3. `Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json`;
4. the visual rendering of configured PDF page 184.

The read-only tool probe returned, verbatim:

```text
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftoppm
/usr/bin/pdftotext
```

`sage` and `magma` returned no path. Version probes used for the nonmathematical source workflow returned:

```text
Python 3.12.3
pdftoppm version 24.02.0
pdftotext version 24.02.0
```

GAP's `--version` probe returned no line. GAP was not invoked for mathematics. No computation, web/history search, other run, delegate, `p=2` or exponent-8 material, wreath-shaped material, or git operation was used. The mathematical evidence is the complete hand reconstruction printed above.

## Verdict

`PARTIAL_RESULT`; `status/conjectured`.

The requested conditional structural claims and exact identities pass the hand audit, subject to the explicitly stated prerequisites for the closure–`lambda` equivalence and the fixed commutator convention. This does not raise the status of the unrestricted target.

## Why this verdict

The quotient gates are noncircular: before minimality is used, the quotient is shown to retain the exact actual value set, subgroup closure, exact exponent `p^2`, the same odd prime, and nonabelianity. The arbitrary-normal-subgroup quotient gives the unique-minimal-normal and cyclic-center claims. The cocycle, section-change, central-root, and stabilizer identities have the signs shown above.

The submission nevertheless has no witness and no proof that `beta=1`. Its statement that the cyclic norms “cannot presently be polarized” is correctly read as a description of the present method's limitation, not as a theorem that no cross-fibre argument can exist. Certification above `status/conjectured` would overstate a bounded reduction.

## What is NOT established

- The active assertion that `P` is abelian for every admissible `G` is not established.
- No admissible counterexample is constructed and no witness is proved equal to the target.
- Nonzero `beta` is not shown compatible with all remaining global extension constraints.
- The radical fibres in the `Z(G)=N` branch are not resolved.
- No impossibility theorem rules out a different, choice-free polarization or cross-fibre identity.
- The general powerfulness clause, all `p=2` material, and the exponent-8 clause remain outside this audit.

## What would upgrade it

A separate gap-free argument would have to force `beta=1` in both center branches for every admissible group, or an explicitly reconstructed finite group would have to pass every canonical admissibility row while having nonabelian actual power subgroup. Neither is present here.
