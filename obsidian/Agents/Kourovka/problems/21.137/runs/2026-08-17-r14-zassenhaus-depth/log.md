---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/zassenhaus-filtration
  - project/kourovka
  - status/draft
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: ZASSENHAUS-DEPTH-PUSH
---

# ZASSENHAUS-DEPTH-PUSH clean proof run

## Active-time ledger

- 2026-08-17T13:00:51Z — research started at scope cumulative minute 407; run cumulative 0 minutes.

## 2026-08-17T13:00:51Z — source and scope gate

The rendered source PDF, page 184, was inspected directly. Its active clause is:

> For \(p\ne2\), if the \(p\)-th powers in a \(p\)-group of exponent \(p^2\) form a subgroup, must that subgroup be abelian?

`source_transcription_checked: yes`. The displayed exponent is \(p^2\), not \(p2\). The canonical revision-2 scope agrees with the rendered statement.

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
No web, historical problem files, other construction artifacts, or excluded clauses were inspected.

### Clause matrix

| source clause | equivalent formulation | active? | handling in this run |
|---|---|---:|---|
| general powerful-subgroup question | whether the full power-value subgroup is powerful without the exponent specialization | no | excluded |
| odd-prime exponent-\(p^2\) question | for every odd prime \(p\), the actual value set \(P=\{g^p:g\in G\}\), if a subgroup, is abelian | yes | exact target |
| exponent-8 two-group question | the square-value analogue at \(p=2\) | no | excluded |

`active_scope_checked: yes`.

### Admissibility checklist

| constraint_id | required use |
|---|---|
| `21.137-odd-forall-p-G` | every identity must be uniform for arbitrary admissible \(p,G\) |
| `21.137-odd-p-not-2` | \(p\) is odd; the norm calculation uses that \(p-1\) is even |
| `21.137-odd-finite-p-group` | use the finite group's terminating Zassenhaus filtration |
| `21.137-odd-exponent-p2` | each actual \(p\)-th power has order dividing \(p\) |
| `21.137-odd-power-set-definition` | every element of \(P\), including products and commutators once closure is assumed, has an actual root |
| `21.137-odd-power-set-subgroup` | \(AB\), inverses, and commutators of actual values remain actual values |
| `21.137-odd-P-abelian` | must force every \([A,B]\), \(A,B\in P\), to be trivial |

No scope mismatch was found.

## 2026-08-17T13:01:30Z — strategy portfolio

Ranked for the exact 60-minute proof increment:

1. **Theoretical / cross-root norm linearization.** Put the equation
   \(x^p y^p=z^p\) in the Zassenhaus restricted Lie algebra. Compare it with the
   conjugated product root and determine whether the first commutator symbol survives
   quotienting by product-root, section, and lift ambiguity. This is the cheapest
   prime-uniform and hand-checkable route.
2. **Structured universal-jet model.** If the first calculation leaves a genuine
   residual, encode every homogeneous \(p\)-power jet through the live degree as a
   universal restricted-Lie polynomial and test whether the residual lies outside
   its image. Kill if the jet image contains the entire target bracket component.
3. **Bounded small-case/catalogue probe.** Not useful here: a fixed prime or group
   cannot certify a prime-uniform depth lemma, and heavy computation is excluded.

Certificate plan: state conventions; give an exact group identity; prove the one-
perturbation norm formula in the Zassenhaus graded object; list separately the
product-root, section, and lift freedoms; and identify precisely whether the target
symbol is zero or merely gauge/ambiguity.

## 2026-08-17T13:02:00Z — setup

Use the dimension/Zassenhaus filtration
\[
D_n(G)=\prod_{i p^j\ge n}\gamma_i(G)^{p^j},\qquad
L_n=D_n/D_{n+1}.
\]
Write \(L=\bigoplus L_n\), with its standard restricted Lie structure. Conventions
are
\[
[g,h]=g^{-1}h^{-1}gh,\qquad g^h=h^{-1}gh=g[g,h],
\]
and the induced graded bracket uses the same order. For \(A=x^p,B=y^p\), put
\(\alpha=A D_{p+1}=X^{[p]}\) and
\(\beta=B D_{p+1}=Y^{[p]}\) when these degree-\(p\) symbols are nonzero.

The first possible target symbol is
\[
\sigma=[B,A]D_{2p+1}=[\beta,\alpha]\in L_{2p}.
\]
(The opposite convention targets its negative and changes nothing.)

## 2026-08-17T13:03:00Z — one-perturbation norm lemma

If \(g\in D_1\), \(u\in D_k\), and \(k\ge2\), then
\[
 g^{-p}(gu)^p=u^{g^{p-1}}u^{g^{p-2}}\cdots u^g u.
\]
Modulo \(D_{k+p}\), all terms containing two occurrences of \(u\) disappear. In
the one-\(u\) terms, the coefficient of the right Engel commutator
\([\bar u,{}_j\bar g]\) is
\(\sum_{i=0}^{p-1}\binom{i}{j}=\binom p{j+1}\). It vanishes in characteristic
\(p\) for \(0\le j<p-1\), and equals one for \(j=p-1\). Since \(p-1\) is even,
\([\bar u,{}_{p-1}\bar g]=(\operatorname{ad}\bar g)^{p-1}\bar u\). The
degree-\((k+p-1)\) term is therefore
\[
 \operatorname{gr}_{k+p-1}\bigl(g^{-p}(gu)^p\bigr)
   =(\operatorname{ad}\bar g)^{p-1}\bar u. \tag{N}
\]
This lemma is only a leading-perturbation statement. It does not assume a global
Baker--Campbell--Hausdorff correspondence.

## 2026-08-17T13:04:00Z — exact conjugate-root calculation

Closure of the complete actual value set gives a product root \(z\in G\) with
\[
z^p=AB. \tag{R}
\]
Let \(\zeta=zD_2\in L_1\). The degree-\(p\) part of (R) is
\[
\zeta^{[p]}=\alpha+\beta. \tag{R_p}
\]
Conjugating (R) by \(A\) supplies another *permitted product root* without making
any choice:
\[
(z^A)^p=(AB)^A=BA. \tag{R^A}
\]
Since \(z^A=z[z,A]\) and \([z,A]\in D_{p+1}\), apply (N) with
\(g=z,u=[z,A],k=p+1\). In \(L_{2p}\),
\[
\begin{aligned}
\operatorname{gr}_{2p}\bigl(z^{-p}(z^A)^p\bigr)
 &= (\operatorname{ad}\zeta)^{p-1}[\zeta,\alpha]\\
 &= (\operatorname{ad}\zeta)^p\alpha\\
 &= [\zeta^{[p]},\alpha]\\
 &= [\alpha+\beta,\alpha]\\
 &= [\beta,\alpha]=\sigma. \tag{T}
\end{aligned}
\]
But already at group level
\[
 z^{-p}(z^A)^p=(AB)^{-1}(BA)=[B,A]. \tag{E}
\]
Thus (T) is exactly the graded shadow of (E): it reproduces the target commutator
symbol identically and gives no equation setting that symbol to zero.

## 2026-08-17T13:06:30Z — complete first-live-degree ambiguity audit

The following separates the three freedoms named in the assignment. Nothing below
identifies an unrealized restricted-Lie root with a genuine group root.

### 1. Product-root choice

For \(C=AB\), let
\[
\mathcal F_C=\{zD_2:z\in G,\ z^p=C\}\subseteq L_1.
\]
This is the **realized** leading-root fibre; it need not be the whole algebraic
fibre \(\{\zeta:\zeta^{[p]}=\alpha+\beta\}\). For every permitted
\(\zeta\in\mathcal F_C\), conjugation maps an actual root \(z\) of \(C\) to
an actual root \(z^A\) of \(C^A=BA\), with the same leading symbol \(\zeta\).
Thus this product-root operation is unavoidable and introduces no existence
assumption beyond (R).

In particular, if \(X=xD_2\) and \(Y=yD_2\), closure gives only
\[
\zeta^{[p]}=X^{[p]}+Y^{[p]}.
\]
It does **not** give \(\zeta=X+Y\): the Jacobson cross terms in
\((X+Y)^{[p]}\) are exactly what makes that substitution unjustified. Changing
the chosen roots of the fixed values \(A\) or \(B\) can also change \(X\) or
\(Y\) inside their realized fibres. At degree \(2p\), (T) depends only on the
fixed value symbols \(\alpha,\beta\) and on the displayed relation for \(\zeta\),
so all root and lift choices for \(x,y\) have already dropped out; none permits an
additive choice of \(\zeta\).

### 2. The live lift and its full linear ambiguity

Roots \(z\) and \(z^A\) agree modulo \(D_{p+1}\). Their first difference is
\[
u=[z,A]\in D_{p+1},\qquad \bar u=[\zeta,\alpha]\in L_{p+1}.
\]
At degree \(2p\), **all** effects of changing a root by an element of
\(D_{p+1}\) are given by the linear norm map
\[
N_\zeta:L_{p+1}\longrightarrow L_{2p},\qquad
N_\zeta(v)=(\operatorname{ad}\zeta)^{p-1}v. \tag{A1}
\]
Indeed (N) applies, while two occurrences of the lift have filtration degree at
least \(3p>2p\), and its own \(p\)-th power has degree \(p(p+1)>2p\).
Consequently the whole first-live-degree lift ambiguity for fixed \(\zeta\) is
\(\operatorname{im}N_\zeta\), and the ambiguity between two lifts producing the
same prescribed product value is \(\ker N_\zeta\).

Accordingly an unavoidable pair-product ambiguity subspace at this degree is
\[
\mathfrak A_{2p}(\alpha,\beta)
 =\sum_{\zeta\in\mathcal F_{AB}}\operatorname{im}N_\zeta
 \le L_{2p}, \tag{A0}
\]
while arbitrary choices of section inside each fixed root fibre act through the
corresponding kernels. Formula (A0) is a sum only over realized product-root labels,
not over a formal algebraic fibre. Root choices with different lower labels can
only enlarge the total ambiguity; the exact relative-norm formulation (A4) below
packages those choices without pretending that their coordinate differences are
linear.

The product-order change has
\[
N_\zeta([\zeta,\alpha])=[\beta,\alpha]=\sigma. \tag{A2}
\]
Hence the target line \(\langle\sigma\rangle\) is contained in the permitted lift
ambiguity for **every** realized product-root label \(\zeta\). This is stronger
than merely failing to show that the ambient component is small: after quotienting
by the full allowed lift ambiguity, the target symbol is identically zero for gauge
reasons, not because \([A,B]\) is one filtration degree deeper.

This is not limited to the single product \(AB\). Since \(P\) has exponent
dividing \(p\), for every \(i,j\in\mathbb F_p\) closure supplies a root
\(z_{ij}^p=A^iB^j\), with a realized label satisfying
\(\zeta_{ij}^{[p]}=i\alpha+j\beta\). Conjugation by \(A^i\) supplies the
permitted root \(z_{ij}^{A^i}\) of \(B^jA^i\), and
\[
N_{\zeta_{ij}}([\zeta_{ij},i\alpha])
 =[i\alpha+j\beta,i\alpha]
 =ij[\beta,\alpha]. \tag{A2'}
\]
Thus the complete scalar grid of two-value product roots absorbs every polarization
multiple of the target symbol. There is no missing \(i,j\) coefficient whose
comparison forces \(\sigma=0\).

The exact exponent condition supplies no overlooked relation in \(L_{2p}\).
Every element of \(P\) has order dividing \(p\), so
\((A^iB^j)^p=1\); but with \(A,B\in D_p\), the first homogeneous terms of that
\(p\)-th-power identity have degree at least \(p^2\). For odd \(p\),
\(p^2>2p\). Hence these exponent identities cannot cancel or constrain the
degree-\(2p\) bracket symbol.

### 3. Section ambiguity

Choose any set-theoretic section \(s:P\to G\) of the actual power map,
\(s(C)^p=C\). No multiplicativity or conjugation equivariance is available. For
\(C=AB\), both \(s(C)^A\) and \(s(C^A)\) are roots of \(C^A\). If they agree
through degree \(p\), their degree-\((p+1)\) discrepancy \(k\) satisfies
\[
N_\zeta(k)=0,
\]
because the two exact \(p\)-th powers are equal. Thus changing the section replaces
the conjugation lift \([\zeta,\alpha]\) by
\([\zeta,\alpha]+k\) with \(k\in\ker N_\zeta\), and (A2) is unchanged. If the
two section roots already have different lower jets, those differences satisfy the
corresponding lower relative-norm equations; their total contribution through the
first degree where their exact powers could differ is still zero. Such lower-jet
choices therefore redistribute the decomposition but supply no section-independent
equation on \(\sigma\).

Changing the representative of \(zD_2\) or any of the filtration lifts of \(z\)
below \(D_{p+1}\) also does not create an omitted term in (A2): in
\([z,A]D_{p+2}\) only \(zD_2\) and \(AD_{p+1}\) occur. Lifts deeper than
\(D_{p+1}\) first affect degrees greater than \(2p\). Thus product-root labels,
the complete live \(D_{p+1}\)-lift image/kernel, arbitrary sections, and all
shallower/deeper representative changes have been accounted for at degree \(2p\).

### Intrinsic description of the larger root-jet space

Because the complete actual value set \(P\) is a subgroup,
\[
V_n=((P\cap D_n)D_{n+1})/D_{n+1}\le L_n
\]
is an \(\mathbb F_p\)-subspace. Exactness of the value set says that \(V_n\) is
precisely the set of degree-\(n\) jets realized by roots whose \(p\)-th powers lie
in \(D_n\). In particular
\[
[V_p,V_p]\subseteq V_{2p}. \tag{A3}
\]
Equation (A3) is closure rewritten in the graded object, not a depth push. It says
that the entire degree-\(2p\) target bracket component is itself inside the
actual-root jet space. Formula (A2) identifies the still sharper local reason:
each target symbol is already the norm of the mandatory conjugation lift.

### The commutator root and the actual first nonzero degree

Closure also supplies an actual root \(q\) of \([B,A]\), because inverses of
actual powers are actual powers and the complete value set is a subgroup. If
\([B,A]\in D_r\), the equation
\[
q^p=[B,A]
\]
only says that its degree-\(r\) symbol lies in \(V_r\). One must not assume
\(q\in D_{\lceil r/p\rceil}\): \(qD_2\) may be a nonzero \(p\)-null root label,
with section and lift jets cancelling in every degree below \(r\). Thus replacing
the existential commutator root by a homogeneous restricted \(p\)-th root would
silently discard a live ambiguity.

For completeness, the exact relative norm packages **all** such jets without a
linearity assumption. For a root \(z\) and arbitrary relative lift \(u\), set
\[
\mathcal N_z(u)=z^{-p}(zu)^p
  =u^{z^{p-1}}u^{z^{p-2}}\cdots u^z u.
\]
If \(r\) is the first nonzero degree of \([B,A]\), define
\[
\mathcal U_r(z)=\{u:\mathcal N_z(u)\in D_r\},\qquad
\mathcal A_r(z)=\operatorname{span}_{\mathbb F_p}
 \{\mathcal N_z(u)D_{r+1}:u\in\mathcal U_r(z)\}\le L_r. \tag{A4}
\]
This contains every lower root-label, section, and lift choice whose relative
power output vanishes through degree \(r-1\); no Hall/Jacobson term is omitted,
because \(\mathcal N_z\) is the exact group word. For the permitted product-root
change \(u=[z,A]\),
\[
\mathcal N_z([z,A])=[B,A],
\]
so the actual minimal symbol \([B,A]D_{r+1}\) lies in \(\mathcal A_r(z)\).
Changing the chosen section root of \(BA\) merely replaces \([z,A]\) by another
element with the same relative norm; changing between two roots of the same exact
value has relative norm \(1\) and belongs to the full kernel. At \(r=2p\), (A4)
specializes to the explicit linear image/kernel calculation (A1)--(A2).

## 2026-08-17T13:06:49Z — strategy kill

The named kill criterion has fired before the 30-minute cap. The cross-root
residual is not a section-independent obstruction: at the first live degree its
entire target line lies in the explicit permitted lift image, and the exact group
identity shows the same conjugate-root ambiguity persists at any later first
nonzero degree. Namely, for any filtration degree \(r\) at which \([B,A]\) first
appears,
\[
z^{-p}(z^A)^p=[B,A]
\]
projects to that very symbol in \(L_r\). Thus merely iterating to the next degree
cannot turn this pair-root covariance into a vanishing identity.

This exhausts `ZASSENHAUS-DEPTH-PUSH` as a **pair-equation / section-independent
root-jet strategy**. It does not show the active assertion false, does not produce
a group, and does not rule out an argument using genuinely additional coherence
among three or more product roots. No such replacement strategy is started pending
Lead direction.

## Active-time stop

- 2026-08-17T13:11:16Z — research stopped on the early strategy kill; run
  cumulative 11 active minutes, scope cumulative 418 active minutes.
- State: `awaiting_lead`. No further strategy has been started.
