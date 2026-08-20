---
title: "Verification — Kourovka 21.137 — regular power commutator"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "The exact Hall-regularity identity proves abelian literal pth powers for the Hall-regular exponent-p^2 subfamily, and any hypothetical counterexample has the stated noncentral defect with minimum-counterexample sign [ag,Delta]=[a,b]^{-1}."
claimant: Problem-21.137-Proof
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the set P={g^p:g in G} of actual pth-power values is a subgroup, then P is abelian."
excluded_scopes: ["general powerfulness clause", "21.137/two-group-exponent-8", "every p=2 case", "odd-prime groups whose exponent is not exactly p^2"]
target_object: "Every finite same-p group in the canonical odd-prime exact-exponent-p^2 scope whose literal actual pth-power value set is a subgroup."
witness_object: "The proper Hall-regular subfamily, together with a conditional configuration inside a hypothetical minimum-order counterexample."
witness_equals_target: false
citation: "none"
verification_method: "Independent line-by-line hand proof, with a GAP free-group word check of the two convention-sensitive commutator product identities."
tools_used: ["GAP 4.12.1", "Python 3.12.3 (probe only)", "Poppler pdftotext 24.02.0 (probe only)"]
scope_answered: []
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/regular-p-groups, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.137 — regular power commutator

## The claim

The submitted mathematics has two levels. First, every finite Hall-regular `p`-group of exponent dividing `p^2` has a subgroup of literal `p`th-power values and that subgroup is abelian; for the active Hall-regular subfamily, the assumed literal-subgroup hypothesis gives the abelian conclusion by a shorter argument that does not use power-set closure induction. Second, any hypothetical active-scope counterexample has a nontrivial, noncentral Hall defect `Delta=b^{-1}(ag)^p`, and in the named reviewed minimum-counterexample setting its exact commutator is `[ag,Delta]=[a,b]^{-1}` under the convention below.

This is a structured-family and necessary-condition `PARTIAL_RESULT`. It neither proves nor refutes the unrestricted Kourovka scope.

## Scope, revision, and clause matrix

The canonical lock is `21.137/odd-prime-exponent-p2`, assignment revision `2`.

| source clause | active? | result of this verification |
|---|---:|---|
| If actual `p`th powers form a subgroup, must it be powerful? | no | excluded |
| `p>2`, finite same-`p` group, exact exponent `p^2`, literal power set a subgroup; must it be abelian? | yes | Hall-regular subfamily only; universally unanswered |
| `p=2`, exponent `8`, square set a subgroup; must it be abelian? | no | excluded |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | independent result | status |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | the proof covers every Hall-regular admissible group, not every admissible group | partial only |
| `21.137-odd-p-not-2` | admissibility | `p>2` is retained; the identities actually need no extra odd-prime fact | pass for covered family |
| `21.137-odd-finite-p-group` | admissibility | finiteness and the `p`-group condition give nilpotence and proper lower-central terms | pass for covered family |
| `21.137-odd-exponent-p2` | admissibility | exact exponent implies every literal `p`th power has exponent at most `p` | pass for covered family |
| `21.137-odd-power-set-definition` | admissibility | the short proof and defect argument use literal actual-valuedness, not generated powers | pass for covered family/conditional defect |
| `21.137-odd-power-set-subgroup` | admissibility | used as an active hypothesis in the short proof; separately derived under Hall regularity | pass for covered family |
| `21.137-odd-P-abelian` | target conclusion | proved only after adding Hall regularity | unresolved universally |

## Target versus witness

The active target quantifies over all admissible groups. The verified theorem quantifies over the proper subfamily satisfying the additional Hall identity, while the defect calculation is conditional on a hypothetical counterexample. Thus the submitted objects are not equal to the full target class, no concrete witness is exhibited, and no structured-family result is being treated as sufficient for the active conclusion.

The `status/replicated` verdict below is restricted to the submitted partial identities and theorem. It does not elevate the canonical scope and does not change `scope_answered: false`.

## Fixed convention and exact Hall definition used

Throughout,

`x^y=y^(-1)xy`, and `[x,y]=x^(-1)y^(-1)xy=x^(-1)x^y`.

The two product identities under this convention are

`[xy,z]=[x,z]^y [y,z]`,

`[x,yz]=[x,z] [x,y]^z`.

For this audit, **Hall-regular** is defined by the exact pair-local assertion: for every `x,y in G`, there exist `c_1,...,c_r in <x,y>'` such that

`(xy)^p=x^p y^p c_1^p ... c_r^p`.                                      (R)

The empty product is allowed. This is a definition here, so no unsubmitted literature equivalence is invoked. It is inherited by every subgroup: for a pair already in a subgroup, the generated group `<x,y>` and its derived subgroup are the same groups as when computed in `G`.

## Normal exponent-`p` lemma

Let `N normal G` with `exp(N)<=p`, and assume (R). Fix `n in N`, `g in G`, and put `K=<n,g>`. The quotient `K/(K intersect N)` is generated by the image of `g`, hence is cyclic. Therefore

`K' <= K intersect N <= N`.

Apply (R) to `(n,g)`. The leading factor `n^p` and every correction `c_i^p` are `1`, so the exact ordered identity is

`(ng)^p=g^p`.                                                            (1)

Every element commutes with its own powers, so `ng` centralizes `(ng)^p=g^p`; also `g` centralizes `g^p`. Since `C_G(g^p)` is a subgroup,

`n=(ng)g^(-1) in C_G(g^p)`.

This holds for every `n,g`, hence `N` centralizes every actual `p`th power and therefore the subgroup they generate:

`[N,G^p]=1`.                                                             (2)

No conjugation or factor-order change occurs in this argument.

## Active Hall-regular subfamily: the short proof

Now impose the active hypotheses and add Hall regularity. The literal set `P={x^p:x in G}` is assumed to be a subgroup. Automorphisms preserve the value set, so `P` is characteristic and therefore normal. Literal actual-valuedness and `exp(G)=p^2` give, for every `u=x^p in P`,

`u^p=x^(p^2)=1`.

Thus `exp(P)<=p`. Because `P` is already a subgroup containing exactly all generators of the conventional verbal subgroup, `P=G^p`. Apply (2) with `N=P`:

`[P,P]=[P,G^p]=1`.

This proves the active conclusion for every Hall-regular group in scope. Importantly, it uses the literal subgroup hypothesis directly and does **not** use the stronger closure induction audited next.

## Separate audit: actual powers are closed in every finite Hall-regular group

The stronger claim is also correct. I reconstruct it by strong induction on `|G|`.

If `G` is abelian, the `p`th-power map is a homomorphism, so its image is a subgroup. Assume the result for every proper Hall-regular subgroup of a nonabelian `G`. Given `x,y in G`, put `H=<x,y>`. If `H<G`, subgroup inheritance of (R) and induction give `x^p y^p=h^p` for some `h in H`. It remains to treat `H=G`.

Write `gamma_1(G)=G` and `gamma_(j+1)(G)=[gamma_j(G),G]`. Formula (R) gives

`(xy)^p=x^p y^p c_1^p...c_r^p`, with every `c_i in gamma_2(G)`.

The proper subgroup `gamma_2(G)` is Hall-regular. By the order induction, its actual `p`th powers form a subgroup, so the ordered correction product equals `d_2^p` for some `d_2 in gamma_2(G)`. Set `w_1=xy`; then

`w_1^p=x^p y^p d_2^p`.

For `j>=2`, suppose

`w_(j-1)^p=x^p y^p d_j^p`, with `d_j in gamma_j(G)`.

Set `w_j=w_(j-1)d_j^(-1)` and apply (R) to the ordered pair `(w_(j-1),d_j^(-1))`. It gives

`w_j^p=w_(j-1)^p d_j^(-p) e_1^p...e_s^p`

`       =x^p y^p d_j^p d_j^(-p)e_1^p...e_s^p`

`       =x^p y^p e_1^p...e_s^p`.                                      (3)

The cancellation in (3) is adjacent; no commutation is assumed. Moreover

`e_i in <w_(j-1),d_j>' <= [G,gamma_j(G)]=gamma_(j+1)(G)`.

The inclusion follows because the two-generator derived subgroup is the normal closure of its basic commutator, and `gamma_(j+1)(G)` is normal. If the next lower-central term is nontrivial, it is a proper Hall-regular subgroup, so the order induction combines the ordered product in (3) into `d_(j+1)^p` for some `d_(j+1) in gamma_(j+1)(G)`. If it is trivial, (3) already reads `w_j^p=x^p y^p`.

Finite `p`-groups are nilpotent, so this recursion terminates. Hence the product of any two actual `p`th powers is an actual `p`th power. Inverses are actual powers because `(x^p)^(-1)=(x^(-1))^p`. Therefore `Pow_p(G)` is a subgroup, and since `G^p` is by definition the subgroup generated by `Pow_p(G)`,

`Pow_p(G)=G^p`.

The induction has no hidden class bound and no circular use of closure in `G`: closure is invoked only in proper lower-central subgroups.

## Forced Hall defect in a hypothetical counterexample

Assume only the active hypotheses and, conditionally, that `P` is nonabelian. Choose `a,b in P` with `[a,b] != 1`, and choose `g in G` with `g^p=b`; the latter uses literal actual-valuedness. Put `H=<a,g>` and `h=ag`.

Because `P` is characteristic, `H/(H intersect P)` is cyclic, generated by the image of `g`. Hence `H'<=P`. Also `exp(P)<=p`, so `(H')^p=1`.

If (R) held for the single pair `(a,g)`, then `a^p=1` and all allowed correction powers would be trivial, forcing

`h^p=(ag)^p=g^p=b`.

But `h` centralizes `h^p=b` and `g` centralizes `b=g^p`; their product `a=hg^(-1)` would then centralize `b`, contradicting `[a,b]!=1`. Thus

`Delta=b^(-1)h^p != 1`.                                                  (4)

Both `b` and `h^p` lie in the literal subgroup `P`, so `Delta in P intersect H`. Because membership in `P` means being an actual value, `Delta` is itself a literal `p`th power (its root need not lie in `H`). It has order exactly `p`: it is nontrivial and `exp(P)<=p`.

It is also noncentral in `H`. If `Delta in Z(H)`, then `h` would centralize both `h^p=b Delta` and `Delta`, hence would centralize `b=(b Delta)Delta^(-1)`. Together with `g in C_G(b)`, this would again put `a=hg^(-1)` in `C_G(b)`, a contradiction.

Finally, (4) is an exact failure of (R), not just of an auxiliary sufficient condition: `(H')^p=1`, whereas rearranging (R) for `(a,g)` would put `Delta` in the subgroup generated by the correction `p`th powers.

## Minimum-counterexample sign

Use only the named reviewed reduction's hypotheses `P'=N<=Z(G)`, `|N|=p`. Choose `a,b in P` with

`n_0=[a,b] != 1`,

so `n_0` generates `N`, and choose `g^p=b`. Retain `h=ag` and `Delta=b^(-1)h^p`, so the ordered equality is

`h^p=b Delta`.                                                           (5)

First, using `[xy,z]=[x,z]^y[y,z]`,

`[h,b]=[ag,b]=[a,b]^g[g,b]=n_0`,                                       (6)

because `g` commutes with `b=g^p` and `n_0` is central. Next, `h` commutes with `h^p`; from (5) and `[x,yz]=[x,z][x,y]^z`,

`1=[h,b Delta]=[h,Delta][h,b]^Delta=[h,Delta]n_0`.

Therefore the exact sign is

`[ag,Delta]=[h,Delta]=n_0^(-1)=[a,b]^(-1)`.                              (7)

No commutation of `b` with `Delta` was assumed: only the ordered identity `b Delta=h^p` was used. Since the commutator in (7) generates central `N`, it also follows that `<h,Delta>'=N`. This is consistent rather than contradictory: although `Delta` is a global actual power, its root need not lie in `<h,Delta>`.

## Order, conjugation, and sign audit

| risk | independent finding |
|---|---|
| correction-product order in (R) | preserved throughout |
| cancellation in the closure induction | `d_j^p d_j^(-p)` is adjacent; valid without commutation |
| depth of new corrections | exactly contained in `gamma_(j+1)` by normality of the lower-central term |
| replacement of actual values by generated powers | made only after the literal set is known to be a subgroup |
| order in the defect definition | `Delta=b^(-1)h^p`, hence `b Delta=h^p`; no swap to `h^p b^(-1)` |
| conjugation convention in `[ag,b]` | gives `[a,b]^g[g,b]`, then centrality removes the conjugate |
| second-variable product convention | gives `[h,b Delta]=[h,Delta][h,b]^Delta` |
| final sign | `[h,Delta]=[a,b]^(-1)`, as submitted |

No mathematical correction is required.

## Subclaims and what each method proves

| subclaim | method | what the pass proves | what it does not prove |
|---|---|---|---|
| exact Hall identity | definition and pair-local inheritance check | fixes the structured class used | equivalence to unsubmitted formulations in the literature |
| normal exponent-`p` identity | hand proof | `(ng)^p=g^p` and `[N,G^p]=1` in Hall-regular groups | that an arbitrary active-scope group is Hall-regular |
| active structured theorem | hand proof using literal `P` | every in-scope Hall-regular group has abelian `P` | the universal active conclusion |
| stronger closure theorem | strong order induction plus lower-central push | `Pow_p(G)=G^p` in every finite Hall-regular group | closure outside that class |
| defect | direct centralizer argument | every hypothetical counterexample violates (R) on a root pair and has noncentral actual-power `Delta` | existence or elimination of a counterexample |
| minimum sign | convention-fixed commutator calculation | exact inverse sign in the reviewed conditional setting | a global contradiction or a root inside `<h,Delta>` |

## Evidence

The evidence boundary was limited to the canonical scope, the submitted request, its two named run refs, and the explicitly named reviewed minimum-counterexample note. No web search, unrelated `21.137` history, excluded sibling material, remembered theorem, or external citation was used.

Tool probe output:

```text
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftotext
Python 3.12.3
pdftotext version 24.02.0
```

Sage and Magma returned no path. GAP reported version `4.12.1`.

The convention-sensitive free-group check was:

```text
$ gap -q -c 'F:=FreeGroup("x","y","z");; x:=F.1;; y:=F.2;; z:=F.3;; Print((Comm(x*y,z)=Comm(x,z)^y*Comm(y,z)),"\n"); Print((Comm(x,y*z)=Comm(x,z)*Comm(x,y)^z),"\n"); QUIT;'
true
true
```

The mathematical verification itself is the complete hand derivation above. The claimant's rejected active-time ledger was excluded from the audit; this note neither validates nor reproduces that accounting.

## Verdict

`PARTIAL_RESULT`; `status/replicated`; `active_assignment_answered: no`.

The structured Hall-regular theorem, the stronger finite Hall-regular power-closure induction, the forced defect properties, and the exact minimum-counterexample commutator sign all survive independent reconstruction. The replicated status applies only to those submitted mathematical partials.

## Why this verdict

Every correction term remains in the claimed subgroup; every cancellation respects factor order; literal actual-valuedness is used exactly where a root or exponent bound is needed; and the commutator identities under the fixed convention force the inverse sign. The short proof of the active Hall-regular subfamily is independent of the more delicate closure theorem, so even a concern about the latter would not contaminate the former. In fact, the closure theorem also passes after making its recursion explicit.

The extra Hall-regularity hypothesis is not a consequence of the active assumptions here. Indeed, the defect argument shows that any hypothetical counterexample must violate precisely the needed pair-local identity. Treating the partial as a universal answer would therefore be a necessary-as-sufficient error.

## What is NOT established

- The universal active assertion is not proved or refuted.
- Literal power-set closure is not shown to imply Hall regularity, globally or on every pair in `P x G`.
- No admissible counterexample is constructed, and the conditional defect configuration is not shown realizable.
- The reviewed minimum-counterexample configuration is not eliminated; a global root of `Delta` need not lie in `<h,Delta>`.
- No conclusion is made about the general powerfulness clause, `p=2`, or the exponent-`8` sibling.
- No active-time accounting in the submitted artifacts is certified.

## What would upgrade it

A universal proof must bridge the active literal-subgroup hypothesis to enough pair-local control to force `[P,P]=1` without assuming Hall regularity. Alternatively, a counterexample must be explicitly reconstructed and pass every canonical admissibility row, including exact exponent `p^2` and equality with the literal actual-power set. Neither is supplied here.
