---
title: "Verification — Kourovka 21.137 — CTH-3-5 integral identity"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Every finite 3-group of exponent exactly 9 and class at most 5 whose actual cube-value set is a subgroup has abelian cube-value subgroup."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual p-th-power set P is a subgroup, then P is abelian."
excluded_scopes: ["general powerfulness clause", "21.137/two-group-exponent-8", "p=2", "odd-prime groups of exponent other than p^2"]
target_object: "Every source-admissible finite odd-prime p-group; the submitted partial family fixes p=3 and class at most 5."
witness_object: "No finite computational witness; the proof vehicle is the relatively free two-generator class-5 nilpotent group F(x,y)/gamma_6, which maps to every two-generated subgroup in the partial family."
witness_equals_target: false
citation: "None for equality with the unrestricted target; the defining universal property of F(x,y)/gamma_6 proves specialization only to the stated p=3, class-at-most-5 partial family."
verification_method: "Independent line-by-line hand collection in the fixed Hall basis; no algebraic computation"
tools_used: ["rendered source PDF page 184", "GAP 4.12.1 availability probe only", "Python 3.12.3 availability probe only"]
scope_answered: ["partial family inside 21.137/odd-prime-exponent-p2: p=3 and nilpotency class at most 5"]
scope_not_answered: ["unrestricted 21.137/odd-prime-exponent-p2", "all p>3 cases", "all p=3 cases of class greater than 5", "general powerfulness clause", "p=2 exponent-8 clause"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## The claim

The submitted strict partial theorem is:

> Let (G) be a finite (3)-group of exponent exactly (9) and nilpotency class at most (5). If the actual cube-value set (P=\{g^3:g\in G\}) is a subgroup, then (P) is abelian.

The claimant explicitly leaves the unrestricted revision-2 target open. I reconstructed the proof by hand from the fixed commutator convention and did not use an algebraic collector.

## Scope, revision, and clause matrix

The canonical record is assignment revision `2` for `21.137/odd-prime-exponent-p2`. The rendered source page 184 was inspected directly.

| source clause | active? | what the source asks | what this proof addresses |
|---|---:|---|---|
| general clause | no | whether a subgroup of (p)-th powers is powerful | nothing |
| odd-prime, exponent-(p^2) clause | yes | for every (p\ne2), whether the subgroup of (p)-th powers is abelian | only (p=3), with extra hypothesis (\operatorname{cl}(G)\le5) |
| (2)-group, exponent-(8) clause | no | whether the subgroup of squares is abelian | nothing |

The proof therefore establishes a structurally defined subfamily only. In particular:

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | independent check | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | The active statement quantifies over every qualifying odd (p,G); the proof fixes (p=3) and class at most (5). | fail for unrestricted scope; acceptable only as partial progress |
| `21.137-odd-p-not-2` | admissibility | (3) is an odd prime. | pass for partial family |
| `21.137-odd-finite-p-group` | admissibility | The claimed family consists of finite (3)-groups. | pass for partial family |
| `21.137-odd-exponent-p2` | admissibility | The claimed exponent is exactly (9=3^2). The proof uses exponent (9), not merely a divisibility assertion. | pass for partial family |
| `21.137-odd-power-set-definition` | admissibility | (P) is always treated as the set of actual cubes. Each of (T_A,S_A,T_B,Q) is independently traced to this set below. | pass for partial family |
| `21.137-odd-power-set-subgroup` | admissibility | Subgroup closure is an explicit hypothesis and is used exactly where products, inverses, and commutators are formed. | pass for partial family |
| `21.137-odd-P-abelian` | target conclusion | The checked identity gives ([x^3,y^3]=1) for arbitrary (x,y\in G). Since every member of (P) is an actual cube, (P) is abelian. | proved for partial family; unproved unrestricted |

There was no linked claim-check JSON because the routed artifact is a `PARTIAL_RESULT`, not a claim to answer the active scope. All seven canonical rows are nevertheless present and independently checked here.

## Target versus proof vehicle

There is no computation in a finite quotient or surrogate group. The proof vehicle is

\[
F=F(x,y)/\gamma_6F,
\]

the relatively free two-generator nilpotent group of class at most (5). If (G) has class at most (5) and (x,y\in G), the homomorphism from the free group sending its generators to (x,y) kills (\gamma_6), hence factors through (F\to\langle x,y\rangle). Consequently, an integral word identity established in (F) specializes to every pair (x,y) in every group in the submitted family.

This is the required universal relationship for the partial family, not an assumption that (F\cong G). The construction uses only the submitted extra class bound; it does not build abelianity or cube closure into (F). The actual-cube membership arguments are performed after specialization and use the target group's stated hypothesis.

For the metadata gate, `witness_equals_target: false`: the proof vehicle and partial family do not equal or cover the unrestricted active target. Separately, the universal-property argument above proves that the free class-5 calculation specializes to every group in the stated p=3, class-at-most-5 partial family.

## Sub-claims and what each method proves

1. A graded Jacobi calculation checks the fixed Hall signs. It proves the weight-(5) relation but not any collection formula left unchecked.
2. Direct conjugate recurrences check (A,B,v_1,v_2,v_3) and ([v_2,v_1]). A pass proves their integral class-(5) normal forms, not any class-(>5) formula.
3. Direct provenance from displayed cubes and normal subgroup operations checks (T_A,S_A,T_B,Q\in P). A pass does not prove cube-set closure; closure remains a hypothesis.
4. Coordinate expansion checks the lifted identity (I). This proves an integral equality, not merely an equality after reducing coordinates modulo (3).
5. The universal property and elementary exponent calculation check specialization. They prove the (p=3), class-(le5) theorem only.

## Evidence

### 1. Conventions, weights, and the fixed Jacobi signs

Use

\[
[u,v]=u^{-1}v^{-1}uv,\qquad u^v=v^{-1}uv=u[u,v].
\]

The fixed basic commutators are

\[
\begin{array}{c|l}
2&c=[y,x]\\
3&a=[c,x],\quad b=[c,y]\\
4&\alpha=[a,x],\quad\beta=[a,y],\quad\gamma=[b,y]\\
5&r=[\alpha,x],\quad s=[\alpha,y],\quad t=[\beta,y],\quad
u=[\gamma,y],\quad\delta=[a,c],\quad\varepsilon=[b,c].
\end{array}
\]

Since ([\gamma_iF,\gamma_jF]\le\gamma_{i+j}F), weight (5) is central and elements whose weights sum to at least (6) commute in (F).

The associated graded Lie ring uses the same bracket orientation as the stated group commutator. Apply Jacobi first to (c,y,x):

\[
[[c,y],x]+[[y,x],c]+[[x,c],y]=0.
\]

Here the three terms are ([b,x]), (0), and (-\beta), so

\[
[b,x]\equiv\beta\pmod{\gamma_5F}.
\]

Apply Jacobi to (b,y,x):

\[
[[b,y],x]+[[y,x],b]+[[x,b],y]=0.
\]

The terms are ([\gamma,x]), ([c,b]=-\varepsilon), and (-t). Hence

\[
[\gamma,x]=t+\varepsilon
\]

in (\gamma_5F/\gamma_6F). Since (\gamma_6F=1) and weight (5) is central, additive notation lifts without another correction to

\[
\boxed{[\gamma,x]=t\varepsilon.}
\]

Thus the submitted signs in the fragile Hall/Jacobi row are correct.

### 2. Independent collection of (A=[y,x^3])

The relations (y^x=yc), (c^x=ca), and (a^x=a\alpha) give

\[
y^{x^2}=(yc)^x=(yc)(ca)=yc^2a.
\]

Because (ac=ca\delta),

\[
(ca)^2=caca=c^2a^2\delta.
\]

Therefore

\[
\begin{aligned}
y^{x^3}
  &=(yc^2a)^x\\
  &=(yc)(ca)^2(a\alpha)\\
  &=yc^3a^3\alpha\delta,
\end{aligned}
\]

and hence

\[
\boxed{A=[y,x^3]=c^3a^3\alpha\delta.}
\]

No term of weight at most (5) is omitted in this recurrence.

### 3. Independent collection of (B=[x,y^3])

For any (z,w), put (q_1=[z,w]), (q_2=[q_1,w]), and (q_3=[q_2,w]). Then

\[
z^w=zq_1,\qquad z^{w^2}=zq_1^2q_2.
\]

In the present weights, ([q_2,q_1]) is central. A third conjugation gives

\[
z^{w^3}=zq_1(q_1q_2)^2q_2q_3
        =zq_1^3q_2^3q_3[q_2,q_1],
\]

so

\[
[z,w^3]=q_1^3q_2^3q_3[q_2,q_1].
\tag{*}
\]

For (z=x,w=y),

\[
q_1=[x,y]=c^{-1}.
\]

The subgroup generated by (c,b) is class (2) at the relevant weights, with ([b,c]=\varepsilon) central. Thus, for every integer (n),

\[
[c^n,y]=b^n\varepsilon^{\binom n2}.
\]

At (n=-1), this gives

\[
q_2=[c^{-1},y]=b^{-1}\varepsilon.
\]

Since all further corrections have weight above (5),

\[
q_3=[q_2,y]=\gamma^{-1},\qquad
[q_2,q_1]=[b^{-1},c^{-1}]=\varepsilon.
\]

Substitution in (*) yields

\[
\boxed{B=[x,y^3]=q_1^3q_2^3\gamma^{-1}\varepsilon.}
\]

Equivalently, because (q_1^3=c^{-3}) and (q_2^3=b^{-3}\varepsilon^3),

\[
B=c^{-3}b^{-3}\gamma^{-1}\varepsilon^4.
\]

This independently confirms both the unexpanded and collected forms submitted.

### 4. Actual cube-set membership of all four terminal elements

Let (G) now be a group in the submitted family and (P=\{g^3:g\in G\}). The set of actual cubes is conjugacy-invariant because

\[
(g^3)^h=(g^h)^3.
\]

Once (P) is assumed to be a subgroup, this makes (P\trianglelefteq G).

First,

\[
A=[y,x^3]=(x^{-3})^yx^3\in P,
\]

because both factors are actual cubes and (P) is a subgroup. Also (c^3,a^3\in P) individually. Hence

\[
\boxed{T_A=(c^3a^3)^{-1}A=\alpha\delta\in P.}
\]

Normality and subgroup closure give

\[
\boxed{S_A=[T_A,y]=T_A^{-1}T_A^y=[\alpha\delta,y]=s\in P,}
\]

where (\delta) is central.

Similarly,

\[
B=[x,y^3]=(y^{-3})^xy^3\in P.
\]

The elements (q_1^3,q_2^3) are actual cubes, so their product lies in (P). Therefore

\[
\boxed{T_B=(q_1^3q_2^3)^{-1}B=\gamma^{-1}\varepsilon\in P.}
\]

Finally, using the checked Jacobi relation and centrality of weight (5),

\[
\boxed{Q=[T_B,x]=[\gamma^{-1}\varepsilon,x]
=[\gamma^{-1},x]=t^{-1}\varepsilon^{-1}\in P.}
\]

Every one of (T_A,S_A,T_B,Q) is thus in the actual value set (P), not merely in the verbal subgroup (G^3). The use of actual-value closure is explicit and essential.

### 5. Independent collection of (v_1,v_2,v_3) and ([v_2,v_1])

Let

\[
v_1=[x^3,y]=A^{-1}.
\]

From (ac=ca\delta) and centrality of (\delta),

\[
a^{-3}c^{-3}=c^{-3}a^{-3}\delta^9.
\]

Inverting the checked form of (A) therefore gives

\[
\boxed{v_1=c^{-3}a^{-3}\alpha^{-1}\delta^8.}
\]

Now set (v_2=[v_1,y]), (v_3=[v_2,y]). The integer-power formula above gives

\[
[c^{-3},y]=b^{-3}\varepsilon^{\binom{-3}{2}}
=b^{-3}\varepsilon^6.
\]

Also

\[
[a^{-3},y]=\beta^{-3},\qquad
[\alpha^{-1},y]=s^{-1},
\]

and every conjugation correction between these displayed factors has weight at least (6). Consequently,

\[
\boxed{v_2=b^{-3}\beta^{-3}s^{-1}\varepsilon^6.}
\]

A second commutation with (y) gives

\[
\boxed{v_3=\gamma^{-3}t^{-3}.}
\]

For ([v_2,v_1]), only the leading weight-(3) factor (b^{-3}) of (v_2) and the leading weight-(2) factor (c^{-3}) of (v_1) can contribute in class (5). Bilinearity in central weight (5) gives

\[
\boxed{[v_2,v_1]=[b^{-3},c^{-3}]=\varepsilon^9.}
\]

This confirms all four submitted rows, including the sign of (\varepsilon^9).

### 6. The exponents (\delta^{51}) and (\varepsilon^{27})

For (w=c^{-3}a^{-3}), the relation ([a,c]=\delta) and centrality of (\delta) imply

\[
w^3=c^{-9}a^{-9}\delta^{\binom32(-3)(-3)}
=c^{-9}a^{-9}\delta^{27}.
\]

The explicit (\delta^8) in each copy of (v_1) contributes another (24). Since (\alpha) commutes with (c,a) in class (5),

\[
\boxed{v_1^3=c^{-9}a^{-9}\alpha^{-3}\delta^{27+24}
=c^{-9}a^{-9}\alpha^{-3}\delta^{51}.}
\]

Independently, cubing (A) gives (A^3=c^9a^9\alpha^3\delta^{30}); inversion and the interchange (a^{-9}c^{-9}=c^{-9}a^{-9}\delta^{81}) again give (-30+81=51).

Similarly,

\[
v_2^3=b^{-9}\beta^{-9}s^{-3}\varepsilon^{18}.
\]

Apply (*) with (z=x^3,w=y):

\[
C=[x^3,y^3]=v_1^3v_2^3v_3[v_2,v_1].
\]

Substitution yields

\[
\boxed{
C=c^{-9}a^{-9}b^{-9}\alpha^{-3}\beta^{-9}\gamma^{-3}
s^{-3}t^{-3}\delta^{51}\varepsilon^{27}.}
\]

The (\varepsilon)-exponent is (18+9=27). Reordering creates no further term: the weight-(4) terminal factors commute with (\gamma_2F) modulo (\gamma_6F), and all weight-(5) factors are central.

### 7. The lifted integral identity

The four certified elements have exact forms

\[
T_A=\alpha\delta,\qquad S_A=s,\qquad
T_B=\gamma^{-1}\varepsilon,\qquad
Q=t^{-1}\varepsilon^{-1}.
\]

Hence

\[
\begin{aligned}
T_A^{-3}&=\alpha^{-3}\delta^{-3},\\
S_A^{-3}&=s^{-3},\\
T_B^3&=\gamma^{-3}\varepsilon^3,\\
Q^3&=t^{-3}\varepsilon^{-3}.
\end{aligned}
\]

All required reorderings again involve weights summing to at least (6). Expanding the right-hand side below gives exactly the checked Hall form of (C):

\[
\boxed{
[x^3,y^3]
=c^{-9}a^{-9}b^{-9}\beta^{-9}\delta^{54}\varepsilon^{27}
T_A^{-3}S_A^{-3}T_B^3Q^3.}
\tag{I}
\]

Indeed, (\delta^{54}\delta^{-3}=\delta^{51}), while the (\varepsilon^3) and (\varepsilon^{-3}) from (T_B^3,Q^3) cancel, leaving (\varepsilon^{27}). Thus (I) is an integral identity in (F); it is not merely a lifted guess from the mod-(3) span relation.

### 8. Specialization to exponent (9) and (\exp(P)\mid3)

Specialize (I) through the universal homomorphism (F\to\langle x,y\rangle\le G). Since (G) has exponent (9),

\[
c^{-9}=a^{-9}=b^{-9}=\beta^{-9}=1,
\qquad
\delta^{54}=\varepsilon^{27}=1.
\]

The last two exponents are multiples of (9), so this uses no extra order assumption.

Every element (z\in P) is an actual cube (z=g^3). Hence

\[
z^3=g^9=1,
\]

so (\exp(P)\mid3). Since (T_A,S_A,T_B,Q\in P), all four remaining factors in (I) are also trivial. Therefore

\[
[x^3,y^3]=1
\]

for arbitrary (x,y\in G). Every two elements of (P) are actual cubes of such (x,y), so (P) is abelian.

### 9. Tool and command record

No GAP, Sage, Magma, Python algebra, bespoke collector, web search, or other algebraic computation was run. The source page was rendered from the configured PDF and inspected visually. The availability probe returned:

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

The source-render command exited with code `0` and emitted no stdout. The mathematical evidence is the independent derivation above.

## Verdict

`status/conjectured` — no certification uplift yet.

Mathematical audit result: the submitted (p=3), exponent-(9), class-at-most-(5) partial theorem survives independent line-by-line hand reconstruction. The fixed signs, the (A,B) collections, actual-value membership of all four terminal elements, the (v_i) collections, both fragile exponents, the integral lift, and the specialization are internally complete.

The certification tag remains `status/conjectured` because the protocol reserves `status/proven` until the human has seen the checked proof. `status/replicated` is not substituted: this is a proof audit, not multiple independent computations.

## Why this verdict

The hand derivation finds no gap in the strict partial theorem, and the universal proof vehicle has the correct specialization relationship to every class-at-most-(5) target group. However, the active revision-2 statement is universal over all odd primes and has no class bound. A valid partial-family theorem cannot answer that assignment, and the human certification gate has not been recorded as complete.

## What is NOT established

- No case with (p>3) is established.
- No (3)-group of nilpotency class greater than (5) is covered.
- The unrestricted scope `21.137/odd-prime-exponent-p2` remains open.
- The general powerfulness clause and the separate (p=2), exponent-(8) clause are not addressed.
- The argument does not show that the actual cube set is automatically a subgroup; closure is a necessary hypothesis throughout.
- No `status/proven` certification is issued before the human-review gate.

## What would upgrade it

For this strict partial theorem, human review of the checked proof would permit the appropriate proof-status decision. Answering the active assignment would additionally require a proof covering every (p>3) case and every (p=3) case of class greater than (5), or a source-admissible counterexample to the unrestricted odd-prime statement.
