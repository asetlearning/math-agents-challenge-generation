---
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 14
outcome: PARTIAL_RESULT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Minimal-normal full-lift gate: exact partial result

## Active target and status

The active universal target is: for every finite group \(G\), every ordinary
irreducible complex character \(\chi\), and every \(x\in G\),
\(\chi(x)\ne0\) implies \(o(x)\chi(1)\mid |G|\).

This note does **not** prove or refute that target. It gives a least-counterexample
reduction, refutes two requested intermediate assertions by exact ordinary
examples, and corrects the arithmetic needed by the proposed character-triple
transfer. `active_assignment_answered: no`.

## Six canonical constraints

| constraint_id | role in this result | result |
|---|---|---|
| `20.115-forall-G-chi-x` | a hypothetical counterexample is minimized first in \(|G|\); the exact examples below refute only intermediate assertions and are not promoted to universal witnesses | pass |
| `20.115-G-finite` | every group below is finite | pass |
| `20.115-chi-complex-irreducible` | all source-side characters are ordinary irreducible complex characters; projective characters occur only inside the transfer proof | pass |
| `20.115-x-in-G` | every named \(x\) has its exact order stated | pass |
| `20.115-character-value-nonzero` | every obstruction uses an exact nonzero ordinary value | pass |
| `20.115-order-degree-divisibility` | no source violation is claimed; the obstruction examples in fact satisfy the desired source divisibility | not established universally |

## 1. Reductions in a least-order counterexample

Assume \((G,\chi,x)\) is a counterexample with \(|G|\) least, and put
\(m=o(x)\), \(d=\chi(1)\).

1. **Faithful.** If \(K=\ker\chi\ne1\), write \(q=o(xK)\) and \(r=m/q\).
   Then \(x^q\in K\) has exact order \(r\), so \(r\mid |K|\). Minimality in
   \(G/K\) gives \(qd\mid |G/K|\), hence \(md\mid |G|\), a contradiction.
2. **Primitive.** If \(\chi=\operatorname{Ind}_H^G\psi\) with \(H<G\), the
   nonzero induction sum at \(x\) has a summand with a conjugate \(y=x^g\in H\)
   and \(\psi(y)\ne0\). Minimality gives \(o(y)\psi(1)\mid |H|\), and multiplying
   by \([G:H]\) gives \(m\chi(1)\mid |G|\).
3. **Quasiprimitive.** For every \(N\lhd G\), Clifford theory says
   \(\chi_N=a(\theta_1+\cdots+\theta_t)\). If \(t>1\), the Clifford
   correspondent induces \(\chi\) from the proper inertia subgroup. Thus
   \(t=1\):
   \[
       \chi_N=a\theta,\qquad \theta\in\operatorname{Irr}(N)
       \text{ is }G\text{-invariant}.
   \]
4. If \(1<N<G\) is minimal normal, then \(\theta\ne1_N\), and
   \(\ker\theta\lhd G\) forces \(\ker\theta=1\). Hence \(\theta\) is faithful.
   If \(N\) is abelian, it is elementary abelian, while a faithful irreducible
   character of it is linear; consequently \(N=C_p\). Invariance and faithfulness
   make \(N\le Z(G)\). If \(N\) is nonabelian, then
   \(N=S^t\) for a nonabelian simple \(S\), and \(N\) is perfect.

Thus the strongest useful choice is any nonabelian proper minimal normal subgroup
when one exists. If none exists, every available choice is a central \(C_p\); a
larger central normal subgroup is not minimal and cannot silently replace it.
If \(G\) itself is simple, there is no nontrivial proper minimal normal subgroup at
all, so this gate has no input; the simple least-counterexample branch must remain
separate.

## 2. Independently derived Clifford/projective data

Put \(f=\theta(1)\), so \(d=af\), and \(Q=G/N\). On the \(N\)-isotypic space one
may identify
\[
   V_\chi\simeq V_\theta\otimes M,
\]
where \(\dim M=a\). Intertwining operators give mutually inverse factor sets on
\(Q\): an associated projective action on \(V_\theta\) and an irreducible
projective action \(D\) on \(M\). For every \(g\in G\),
\[
   \chi(g)=\operatorname{tr}P(g)\,\operatorname{tr}D(gN).
\]
In particular, \(\chi(x)\ne0\) implies \(\operatorname{tr}D(xN)\ne0\); this
factorization, rather than an unsupported no-cancellation assertion, is the exact
route from the ordinary value to the projective value.

Let \(c\in H^2(Q,\mathbb C^\times)\) be the factor-set class and let
\(n=o(c)\). It has a \(\mu_n\)-valued representative, yielding an effective
central extension
\[
   1\longrightarrow Z\cong C_n\longrightarrow \widehat Q
   \longrightarrow Q\longrightarrow1
\]
and an ordinary irreducible \(\widehat\delta\) of degree \(a\), with \(Z\) acting
faithfully by scalars. A lift of \(y=xN\) has nonzero
\(\widehat\delta\)-value.

Two determinant computations are useful and independent:

- the degree-\(a\) projective representation \(D\) gives \(n\mid a\);
- if \(N=S^t\), then \(\det\theta=1\). Hence the determinant of the
  \(f\)-dimensional intertwining representation descends to a cochain on \(Q\),
  giving \(n\mid f\).

Therefore in the nonabelian-minimal branch
\[
       n\mid\gcd(a,f),\qquad n\le f<|N|.
\]
This proves requested input (1) in that branch and makes \(|\widehat Q|<|G|\).

In the abelian-minimal branch \(N=C_p\), the class is either trivial or has
effective order \(p\). If it is trivial, \(\theta\) extends linearly to \(G\),
\(\chi\) is that extension times an inflated member of \(\operatorname{Irr}(Q)\),
and minimality in \(Q\), together with \(m/o(xN)\mid p\), proves the target.
Consequently a least counterexample in this branch would have to have nontrivial
class and then \(|Z|=p=|N|\), not \(|Z|<|N|\).

## 3. Exact transfer arithmetic and the misidentified third input

Write
\[
 q=o(xN),\qquad r=m/q,
\]
so \(x^q\in N\) has exact order \(r\), and \(r\mid |N|\). If
\(\widehat y\) is a lift of \(xN\), write
\[
 o(\widehat y)=qt,\qquad t\mid n,qquad \Delta=n/t.
\]
Minimality applied to \((\widehat Q,\widehat\delta,\widehat y)\) gives
\[
 qt\,a\mid n|Q|,\qquad\text{hence}\qquad qa\mid \Delta|Q|. \tag{*}
\]
Primewise full order means \(t=n\) (equivalently
\(v_\ell(o(\widehat y))=v_\ell(q)+v_\ell(n)\) for every \(\ell\)), so
\(\Delta=1\).

Since \(\chi(1)=af\), combining (*) with the kernel side requires
\[
       r f\Delta\mid |N|. \tag{**}
\]
Under full order this is \(rf\mid |N|\). The requested condition
\(ra\mid |N|\) is **not** (**)—it repeats the multiplicity \(a\), which already
occurs in (*), and omits the constituent degree \(f\). No Clifford theorem found
in the derivation exchanges \(a\) and \(f\).

A useful sufficient package is therefore:

1. \(n<|N|\);
2. a full-order lift of \(xN\);
3. \(r\theta(1)\mid |N|\).

The third item follows from minimality in \(N\) if
\(\theta(x^q)\ne0\). But \(\operatorname{tr}P(x)\ne0\) does not in general imply
\(\theta(x^q)=\operatorname{tr}(P(x)^q)\ne0\). This is a second precise gap.

## 4. Exact obstruction in the abelian-minimal branch: `2.A6`

Let \(G=2.A_6\cong\operatorname{SL}_2(9)\), let \(N=Z(G)=\langle z\rangle\cong
C_2\), and take either faithful spin character of degree four (`2.A6` ordinary
table row `X.8` or `X.9`). Then \(N\) is the unique proper minimal normal subgroup,
\(\chi_N=4\theta\) with \(\theta(z)=-1\), and \(\chi\) is primitive: induction
would require a proper subgroup of index at most four, while the action on its
cosets would force \(2.A_6\) or \(A_6\) into \(S_4\).

The Clifford class is nontrivial: an extension of \(\theta\) to a linear character
of the perfect group \(2.A_6\) is impossible. Its effective scalar kernel has
order two, exactly \(|N|\), so input (1) fails. With \(x=z\),
\[
 \chi(x)=-4\ne0,\quad o(x)=2,\quad o(xN)=1,\quad a=4,
\]
and \((o(x)/o(xN))a=8\nmid2=|N|\), so input (3) fails as well. The source
conclusion is not violated: \(2\cdot4=8\mid720\).

This is an exact faithful, primitive, quasiprimitive obstruction at the only
possible minimal-normal choice, not a complaint that homogeneity is weak.

## 5. Exact obstruction to input (3) with a nonabelian unique minimal normal

Let
\[
 N=A_5^8,\qquad H=A_8,qquad G=N\rtimes H,
\]
where \(H\) naturally permutes the eight factors. Let \(\alpha\) be a faithful
degree-three irreducible character of \(A_5\), put
\(\theta=\alpha^{\otimes8}\), and use the canonical tensor-permutation extension
\(\widetilde\theta\) to \(G\). Let \(\beta\) be the degree-seven standard
character of \(A_8\), and set
\[
      \chi=\widetilde\theta\otimes\operatorname{Inf}_{H}^{G}\beta.
\]
Then \(\chi\in\operatorname{Irr}(G)\), it is faithful, and
\(\chi_N=7\theta\), so the Clifford multiplicity is \(a=7\).

Here \(N\) is the unique minimal normal subgroup: it is minimal by transitivity
on the simple factors, while a normal subgroup disjoint from \(N\) centralizes
\(N\), whose centralizer in \(G\) is trivial. The character is primitive. Indeed,
if \(\chi=\operatorname{Ind}_K^G\varphi\), then \([G:K]\mid7\cdot3^8\). Every
proper subgroup of \(A_5^8\) has index divisible by 2 or 5 (induct on the number
of factors using a coordinate projection), so \(N\cap K=N\). Thus \(N\le K\),
and \([G:K]\) is the index of a subgroup of \(A_8\). No proper subgroup of
\(A_8\) has index at most seven: simplicity would embed \(A_8\) in \(S_7\), but
\(|A_8|>7!\). Hence \(K=G\). The normal-subgroup description also makes
\(\chi\) quasiprimitive.

Take \(x\) to be a complement element acting as \((12)(34)\) on the eight
factors. It has order two and six cycles. The tensor-permutation trace is \(3^6\),
while \(\beta(x)=4-1=3\), so
\[
       \chi(x)=3^7\ne0,
       \qquad o(x)=o(xN)=2,
       \qquad (o(x)/o(xN))a=7\nmid60^8=|N|.
\]
The Clifford class is trivial here (\(Z=1<|N|\), and full lift is automatic), so
this example isolates the failure of input (3) after the strongest—indeed unique—
nonabelian minimal-normal choice. Again the source conclusion holds; the factor
7 is supplied by \(|A_8|\).

## 6. Full-order lift: exact remaining theorem

For a fixed effective \(C_n\)-extension, full order at \(y\) is precisely the
statement that \(\langle\widehat y\rangle\cap Z=Z\). It is automatic when
\((n,o(y))=1\), after multiplying a split-order lift by a generator of \(Z\), but
at common primes it is a restriction-of-cocycle condition.

Nonzero projective trace does not itself force it. For example, in
\(E=2.A_6\times A_5\), with scalar kernel the central \(C_2\) of the first factor,
take the outer tensor product of a faithful degree-four spin character with a
degree-three character of \(A_5\). At \(y=(1,h)Z\), where \(h\) is an involution
of \(A_5\), the value is \(-4\ne0\), but both lifts \((1,h)\) and \((z,h)\) have
order two rather than four. The quotient \(A_6\times A_5\) is perfect, so a
linear-character/Bockstein twist cannot alter this restriction while keeping the
same effective \(C_2\)-class.

This last example has another, larger minimal normal subgroup, so it is not by
itself a refutation after the mandated strongest choice. It identifies the first
genuinely missing theorem: one would have to prove that the strongest
minimal-normal choice in a least **ordinary** counterexample forces the Clifford
class to restrict fully at \(\langle xN\rangle\). No such implication follows
from homogeneity, determinant divisibility, or nonzero projective trace.

## Strongest surviving package and recommendation

- A least counterexample is faithful, primitive, and quasiprimitive.
- A simple least counterexample is not touched by a proper-minimal-normal transfer.
- A central minimal normal subgroup either has trivial obstruction and is
  eliminated, or has effective kernel equal to that subgroup and cannot shrink the
  induction group.
- A nonabelian minimal normal subgroup always gives an effective scalar kernel of
  order \(n\mid\gcd(a,\theta(1))<|N|\), hence a genuinely smaller ordinary group.
- For a lift with \(o(\widehat y)=o(xN)t\), the exact residual loss is
  \(\Delta=n/t\), and the sufficient kernel condition is
  \((o(x)/o(xN))\theta(1)\Delta\mid|N|\).

The next proof increment should target the two exact nonvanishing/order statements
in the nonabelian branch: full restriction of the Clifford class at
\(\langle xN\rangle\), and nonvanishing of \(\theta(x^{o(xN)})\). It should not
continue with the false multiplicity condition \((o(x)/o(xN))a\mid|N|\).

## Reproducible exact-table checks used

GAP/CTblLib command (completed in under three seconds):

```text
gap -q -c 't:=CharacterTable("2.A6");; Display(t);;
Print(OrdersClassRepresentatives(t),"\n");; QUIT;'
```

The displayed table has faithful degree-four rows `X.8`, `X.9`, central class
`2a`, and value `-4` there. No catalogue search or job over 60 seconds was run.
