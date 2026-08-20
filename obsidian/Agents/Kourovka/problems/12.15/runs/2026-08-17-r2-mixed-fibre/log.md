---
title: "Kourovka 12.15 — M2 mixed-fibre polarization run log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/commutator-calculus
  - project/kourovka
  - status/draft
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
direction: proof
run: 2026-08-17-r2-mixed-fibre
state: awaiting_lead
---

# Active target

For every finite (2)-group (G) such that equality of normal closures implies conjugacy, show that (G''=1).

Constraint checklist: universal quantification; (G) finite; (G) a (2)-group; every normal-closure fibre is one conjugacy class; target (G''=1).  The canonical record and Validator's source-fidelity audit already pass revision 1.  This discovery-blind increment inherits that reviewed transcription; external staleness checking remains deferred to Lead/human.

# Authorized input and strategy

Read only the two linked Validator audits and MathExpert's M2 note.  In a hypothetical least counterexample the reviewed core gives

\[
Z(G)=G''=\langle z\rangle\cong C_2,
\qquad D(t):=\{[t,g]:g\in G\}\le G,
\]

with (D(t)\lhd G), (t^2\in D(t)), and (z\in D(t)) for every noncentral (t).  The corrected order-(128) reduction is context only; no HAP-dependent or legacy central-lift work is reopened.

Named strategy: **M2-MIXED-FIBRE-POLARIZATION**.  Fix the convention ([a,b]=a^{-1}a^b=a^{-1}b^{-1}ab), write the exact central factor attached to

\[
[xy,g]=[x,g]^y[y,g],
\]

and determine whether subgroup closure of (D(x),D(y),D(xy),D(xy^{-1})) kills its alternating part.  Kill criterion: closure merely absorbs the residual in ({1,z}).

# Active-time ledger

- 2026-08-17T08:25:47Z — formal charged work start, cumulative active minutes (0).

# Work notes

## 2026-08-17T08:25:47Z — convention and central-extension model

Put (H=G') and (Z=G''=\langle z\rangle).  Since (Z\le Z(G)), (H) has class at most two.  Thus (W=H/Z) is abelian and the commutator pairing

\[
\beta(\bar a,\bar b)\in\mathbf F_2,
\qquad [a,b]=z^{\beta(\bar a,\bar b)}
\]

is well defined and biadditive (possibly degenerate).  This (W)-model retains exactly the (z)-valued residual; passing further to (H/Z(H)) only removes the radical.

Choose a normalized section (s:W\to H) and write

\[
s(u)s(v)=z^{f(u,v)}s(u+v),\qquad f(u,v)\in\mathbf F_2.
\]

With the fixed commutator convention, (ab=ba[a,b]).  Therefore

\[
\beta(u,v)=f(u,v)+f(v,u),
\qquad [s(u),s(v)]=z^{\beta(u,v)}. \tag{1}
\]

If conjugation by (y) induces ρ_y on (W), define the section-displacement cochain λ_y by

\[
s(u)^y=z^{\lambda_y(u)}s(\rho_yu).
\]

For

\[
a_g=[x,g]=z^{\alpha_g}s(u_g),\qquad
b_g=[y,g]=z^{\gamma_g}s(v_g),
\]

the given product identity has the convention-fixed form

\[
[xy,g]
=z^{\alpha_g+\gamma_g+\lambda_y(u_g)+f(\rho_yu_g,v_g)}
 s(\rho_yu_g+v_g). \tag{2}
\]

The alternating part of the displayed factor is exactly

\[
f(\rho_yu_g,v_g)+f(v_g,\rho_yu_g)
=\beta(\rho_yu_g,v_g),
\]

or intrinsically

\[
a_g^y b_g=b_g a_g^y[a_g^y,b_g],
\qquad [a_g^y,b_g]=z^{\beta(\rho_yu_g,v_g)}. \tag{3}
\]

This freezes both the order and the sign convention; there is no suppressed inverse in (3).

For the minus fibre, the exact inverse identity is

\[
[y^{-1},g]=(b_g^{-1})^{y^{-1}},\qquad
[xy^{-1},g]=(a_gb_g^{-1})^{y^{-1}}. \tag{4}
\]

Since (s(v)^{-1}=z^{f(v,-v)}s(-v)), (4) becomes

\[
[xy^{-1},g]
=z^{\alpha_g+\gamma_g+f(v_g,-v_g)+f(u_g,-v_g)
       +\lambda_{y^{-1}}(u_g-v_g)}
 s\!\left(\rho_{y^{-1}}(u_g-v_g)\right). \tag{5}
\]

Its ordered-product factor has alternating part

\[
\beta(u_g,-v_g)=-\beta(u_g,v_g)=\beta(u_g,v_g), \tag{6}
\]

where the last equality is forced by the target (C_2=\langle z\rangle).  Thus replacing (y) by (y^{-1}) does not provide an opposite central sign.

## Mixed-fibre closure calculation

Assume (G''\ne1) and choose (x,y\in H) with ([x,y]=z).  These are the pairs that a proof must exclude.  Then (x,y,xy,xy^{-1}) are all noncentral: if either product were central, commuting it with (x) would give ([y,x]=1), contrary to ([x,y]=z).  The reviewed least-counterexample core therefore gives

\[
Z\le D(x)\cap D(y)\cap D(xy)\cap D(xy^{-1}). \tag{7}
\]

For every noncentral (t), (7) implies the exact saturation identity

\[
D_G(t)=\pi^{-1}\!\left(D_{G/Z}(tZ)\right), \tag{8}
\]

where π is restricted to the relevant preimage: one lift of a projected defect value lies in (D_G(t)), and multiplication by (z\in D_G(t)) supplies the other lift.  Hence subgroup closure of (D_G(t)) sees only the projected defect set and cannot select either value of a (z)-residual.

There is also a direct four-fibre polarization.  Because (x,y\in H) and (H'=Z\le Z(G)), put (a_g=[x,g]), (b_g=[y,g]); then

\[
[xy,g]=a_gb_g[a_g,y],\qquad [a_g,y]\in Z, \tag{9}
\]

while normality of (D(xy^{-1})), together with (4), gives

\[
[xy^{-1},g]^y=a_gb_g^{-1}\in D(xy^{-1}). \tag{10}
\]

By (7), (9) is equivalent for membership purposes to (a_gb_g\in D(xy)).  For arbitrary (g,h\in G), closure of the plus and minus fibres produces

\[
\begin{aligned}
(a_gb_g)(a_hb_h)
 &=a_ga_hb_gb_h\,[b_g,a_h], \\[2mm]
(a_gb_g^{-1})(a_hb_h^{-1})
 &=a_ga_hb_g^{-1}b_h^{-1}\,[b_g^{-1},a_h].
\end{aligned} \tag{11}
\]

The sought mixed pairing is the displayed residual.  But

\[
[b_g^{-1},a_h]=[b_g,a_h]^{-1}=[b_g,a_h]\in\{1,z\}. \tag{12}
\]

Thus the plus and minus closures contain the **same** residual bit, not two opposite bits.  Since every subgroup in (7) already contains both (1) and (z), (11) is compatible with either value.  As (g,h) vary, (b_g) and (a_h) independently range through (D(y)) and (D(x)), so this is exactly the attempted arbitrary mixed pairing, not merely a diagonal sample.

The value-set property adds no synchronization: closure in each fibre may choose a different conjugator witnessing the product.  Multiplying that witnessed value by (z) is again a value in the same saturated fibre.  Hence eliminating the four existential witnesses can recover only

\[
[D(x),D(y)]\le Z=\{1,z\},
\]

which was already known from (D(x),D(y)\le H) and (H'=Z).

## Strategy decision

The M2 kill criterion fires.  The convention-fixed factor is (2), its alternating part is (3), and the coupled plus/minus calculation is (11)--(12).  Four-fibre subgroup closure cannot force the bit to be (1); it only confirms that it lies in the already-absorbed kernel ⟨z⟩.  No HAP computation or central-lift search was used.

- 2026-08-17T08:36:28Z — charged work stop after checking and filing the strategy-kill report, cumulative active minutes (11); state `awaiting_lead`.

## 2026-08-17T08:38:44Z — Lead pivot to M1

- 2026-08-17T08:38:44Z — charged work resumed, cumulative active minutes \(11\); \(53\) minutes remain.

Lead accepted the M2 obstruction as a strategy failure and directed a pivot to **M1-SQUARE-ORBIT** in order-\(128\) regime R3. Before pivoting, I checked the M2 findings bytewise: there are no remaining control characters, and equation (2) now reads

\[
[x,g]^y[y,g]=[y,g][x,g]^y\,z^{\beta(\rho_yu_g,v_g)}.
\]

Thus both notation defects named in the decision are repaired.

The M1 inputs are: \(H=G'\) has order \(32\), \(A=Z(H)\) has order \(8\), \(V=H/A\cong C_2^2\), \(E=G/H\cong C_2^2\) acts faithfully on \(A\), and \(A^E=\langle z\rangle\). For the basic commutator \(c\), \(D=D_G(c)\) is an abelian maximal subgroup of \(H\), \(A\le D\), \(|D|=16\), and \(cD=c^G\).

Define

\[
q:D\to A,\qquad q(d)=d^2[c,d].
\]

The authorized input states that \(q\) is a homomorphism and

\[
(cd)^2=c^2q(d),\qquad c^2q(D)=(c^2)^E. \tag{M1}
\]

Because \(A=Z(H)\), \(q(a)=a^2\) for \(a\in A\). Hence

\[
A^2=q(A)\le Q:=q(D),\qquad |Q:A^2|\le |D:A|=2. \tag{M1a}
\]

This is the first occurrence constraint omitted by a bare orbit-coset test.

## 2026-08-17T08:44:21Z — R3 precondition inconsistency

Before treating the three actions as candidate R3 cases, I checked the claimed size of \(D_G(c)\). The R3 row is incompatible with the reviewed least-counterexample core:

1. The basic commutator \(c\) belongs to \(H=G'\).
2. Since \(A=Z(H)\), \(|A|=8\), and \(H/A\cong C_2^2\), the subgroup \(A\langle c\rangle\) centralizes \(c\). If \(c\notin A\), it has order \(16\); if \(c\in A\), all of \(H\) centralizes \(c\). Hence
   \[
   |c^H|=|H:C_H(c)|\le2.
   \]
3. Since \(|G:H|=4\),
   \[
   |c^G|\le |G:H|\,|c^H|\le8. \tag{R3-obstruction}
   \]
4. The audited fibre identity is \(c^G=cD_G(c)\), so
   \[
   |D_G(c)|=|c^G|\le8.
   \]
5. The R3/M1 input simultaneously says \(A\le D_G(c)\) and \(|D_G(c)|=16\), with nonzero-line image in \(H/A\).

Thus the M1 configuration cannot exist as stated. At minimum the order-\(16\)/line-image row is wrong; if that row was validly forced by the other R3 deductions, then the displayed orbit bound eliminates R3 before the square-orbit test.

The bounded action enumerator had already been run when this inconsistency became apparent. It found one compatible action class for each \(A\), but those calculations cannot certify an R3 conclusion while the defining defect-subgroup row is contradictory. Per the protocol stop condition for a reviewed dependency that appears wrong, I am escalating rather than silently changing \(|D_G(c)|\) to \(8\).

- 2026-08-17T08:45:48Z — charged work stopped on the reviewed-dependency inconsistency, cumulative active minutes \(18\); state `awaiting_lead`. The allocation retains \(46\) unused active minutes pending Lead/Validator resolution.

## 2026-08-17T09:47:06Z — Validator correction and Lead R1/R2 pivot

- 2026-08-17T09:47:06Z — charged work resumed, cumulative active minutes \(18\); Lead authorizes \(42\) preserved minutes.

Validator confirms that the defect-order row and the centralizer bound are both sound, so their contradiction eliminates R3. The remaining order-\(128\) branches are:

- R1: \(|E|=16\), \(|H|=8\), \(A=Z(H)=\langle z\rangle\cong C_2\), \(V=H/A\cong C_2^2\), and the image of \(E\) on \(V\) has order at most \(2\).
- R2: \(|E|=8\), \(|H|=16\), \(A=Z(H)\cong C_4\) or \(C_2^2\), \(V=H/A\cong C_2^2\), the image on \(A\) has order \(2\), and the image on \(V\) has order at most \(2\).

Named strategy: **R1R2-DEFECT-ORBIT-PACKING**. For each basic commutator from a minimal generating set, compute its normal closure \(N\), exact defect subgroup \(D=N^2[N,G]\), projected \(E\)-orbit in \(V\), and determine whether all such normal closures can generate \(H=G'\) under the reviewed action-size bounds. Kill criterion: a complete compatible abstract table remains.

### Exact table and action restriction

The complete table is in [[r1r2-defect-orbit-packing]]. For \(v=cA\), \(W=NA/A\), \(L=DA/A\), and \(B=N\cap A\), the exact rows are

\[
W=\langle E v\rangle,\qquad L=[W,E],\qquad D\cap A=B.
\]

A fixed nonzero \(v\) gives \(|N|=2|B|\), \(D=B\). A moving \(v\) under a transvection gives \(W=V\), \(L=F\), \(|N|=4|B|\), and \(|D|=2|B|\). R1 forces \(B=A=Z\); R2 permits \(B=Z\) or \(A\).

The nominal nontrivial action on \(V\) is actually impossible. Write it as \(T^{\chi(e)}\), choose \(e_0\) outside \(\ker\chi\), and choose the other basis vectors in the kernel. Projected Hall--Witt forces every kernel-pair basic commutator into the fixed line \(F\). For a cross commutator \(w_{0i}=[x_0,x_i]A\), elementary abelianness of \(E\) gives \(x_0^2\in H\), while \(x_i\) acts trivially on \(V\). Hence

\[
0=[x_0^2,x_i]A
=([x_0,x_i]^{x_0}[x_0,x_i])A
=(T-1)w_{0i}.
\]

Thus every basic commutator image lies in \(F\), contradicting their required normal span \(V\). Therefore \(E\) acts trivially on \(H/A\) in both R1 and R2.

With the trivial action, compatible packings remain. In R1, two independent \(S(A)\) rows have normal closures of order \(4\) whose product is \(H\). In either R2 centre type, two independent \(S(A)\) rows have normal closures of order \(8\) whose product is \(H\). If all R2 rows instead have \(B=Z\), one further lift-offset bit \(\delta=\dim((K\cap A)/Z)\) decides whether their product \(K\) is \(H\); the reviewed action rows do not determine it.

The strategy therefore produces a partial structural restriction but meets its kill criterion: the finite trivial-action tables survive, and further progress needs central lift data outside this packing abstraction.

- 2026-08-17T09:58:12Z — charged work stopped after filing the partial result, completing the table, and archiving processed control messages, cumulative active minutes \(29\); state `awaiting_lead`. The allocation retains \(31\) unused active minutes.

## 2026-08-17T10:28:23Z — Lead central-layer pivot

- 2026-08-17T10:28:23Z — charged work resumed; run-local cumulative active minutes \(29\), with \(31\) minutes remaining in the human-authorized increment. Lead records the scope-wide cumulative total separately as \(302\) minutes.

Named strategy: **R1R2-CENTRAL-LAYER-POLARIZATION**. Use the accepted bounded restriction \([H,G]\le A\), write the central triple-commutator and square data for a minimal generating set, impose Hall--Witt and power polarization, and determine whether the R1/R2 trivial-action packings survive.

### Central-layer result

The complete convention-fixed table is in [[r1r2-central-layer-polarization]]. With \(c_{ij}=[x_i,x_j]\), \(s_i=x_i^2\), \(t_{ij,k}=[c_{ij},x_k]\), and \(q_{ij}=c_{ij}^2\), the exact power rows are

\[
[s_i,x_j]=q_{ij}t_{ij,i},\qquad
[s_j,x_i]^{-1}=q_{ij}t_{ij,j},
\]

and conjugation-square compatibility is

\[
(h^2)^x=(h^x)^2=h^2[h,x]^2.
\]

In R1 these reduce to a bilinear central action \(\tau:V\times E\to Z\), the extraspecial quadratic form \(q:V\to Z\), cyclic Hall--Witt, and two power-polarization equations. Explicit tables survive for both \(D_8\) and \(Q_8\).

In R2, modulo \(Z\), one gets a bilinear \(\bar\tau:V\times E\to A/Z\) and a linear square map \(\bar q:V\to A/Z\). The last square identity distinguishes the centres:

\[
A=C_4:\quad \bar\tau(v,e)=\psi(e)\bar q(v),
\qquad
A=C_2^2:\quad \bar q=0.
\]

Compatible \(B=A\) tables survive both cases. For the all-\(B=Z\) lift-offset, choose \(\psi(e_1)=1\) and write \(\alpha_{ij}\) for changing a commutator lift by \(A/Z\). Hall--Witt gives \(\alpha_{23}=0\). The power rows leave \(\alpha_{12},\alpha_{13}\) free for \(C_4\), but force all three \(\alpha_{ij}=0\) for \(C_2^2\). Hence:

- \(A=C_2^2\), all \(B=Z\): \(\delta=0\), so this subtable cannot normally generate \(H\);
- \(A=C_4\), all \(B=Z\): one relation-offset bit survives and can give \(\delta=1\);
- both centre types still have compatible \(B=A\) packings.

The method is exhausted with a precise cyclic-centre residual bit; neither R1 nor R2 is eliminated.

- 2026-08-17T10:38:47Z — charged work stopped after freezing the convention-explicit table and filing the Lead/Validator handoff, run-local cumulative active minutes \(39\); state `awaiting_lead`. The allocation retains \(21\) unused active minutes for Lead follow-up.

## 2026-08-17T10:41:22Z — Lead pc-consistency and fibre-witness pivot

- 2026-08-17T10:41:22Z — charged work resumed, run-local cumulative active minutes \(39\), with \(21\) minutes remaining. Lead records scope-wide cumulative active time as \(312\) minutes.

The complete result is in [[r1r2-pc-consistency-fibre-witness]]. The R1 \(D_8\) and \(Q_8\) actions are inner on \(H\); replacing each quotient lift by an element of its \(H\)-coset which centralizes \(H\) gives \(G=H C_G(H)\), hence \(G'\le Z(H)\), contradicting \(G'=H\). This eliminates R1 independently of central lift bits.

For R2 with \(A=C_4\), the action-square critical pair gives \(h^{x^2}=h\) for every \(h\in H,x\in G\): inversion cancels the commutator factor when \(\psi(xH)=1\), while the factor lies in \(Z\) and squares to \(1\) when \(\psi(xH)=0\). Thus every square in \(G/A\) is trivial, so \(G/A\) is elementary abelian and \(G'\le A\), contradicting \(H/A\cong C_2^2\). This eliminates both the \(B=A\) and the cyclic all-\(B=Z\) offset rows.

For \(A=C_2^2\), an exact seven-generator pc presentation was found. Its only non-obvious collection correction is \([u,l]=az\); omitting the \(z\) collapses \(z\), while including it gives \(128\) distinct collected forms, derived subgroup \(H\cong D_8\times C_2\), centre \(\langle z\rangle\), and class \(4\). In that group

\[
x=r,\qquad y=ruv
\]

have orders \(2\) and \(4\), hence are not conjugate, but

\[
\langle x\rangle^G=\langle y\rangle^G=\langle r,H\rangle
\]

of order \(32\). Both classes have size \(8\), with centralizers of order \(16\). Thus the exact materialization fails the source hypothesis by a convention-explicit witness. The residual is the classification of all elementary-centre exact offset tables; this increment does not assert that every such offset is equivalent to the displayed group.

- 2026-08-17T10:53:22Z — charged work stopped after exact pc verification and filing the witness handoff, run-local cumulative active minutes \(51\); state awaiting_lead. The allocation retains \(9\) unused active minutes for Lead follow-up.

## 2026-08-17T10:57:57Z — Lead universal elementary-centre witness pass

- 2026-08-17T10:57:57Z — charged work resumed, run-local cumulative active minutes \(51\), with the final \(9\) minutes authorized. Lead records scope-wide cumulative active time as \(324\) minutes.

The full coverage bridge is in [[r2-ea-universal-fibre-witness]]. Put \(K=\ker\psi\). After changing the lift \(r\notin K\) by an element of \(H\), its visible central action is zero and \(r^2\in\{1,z\}\). For \(k\in K\), let \(L(k)\) be symplectically dual to \(\bar\tau_k\). Action-square consistency gives

\[
[r,k]A=L(k),
\]

while commutators within \(K\) lie in \(A\). Since \(G'=H\), the map \(L:K\to V\) is an isomorphism. This yields an ambient binary parametrization containing every pc-consistent exact-offset table.

For a section lift \(h=s(t)\), define \(d(t)\) by

\[
h^2[h,r]=z^{d(t)}.
\]

Its polar form is the nondegenerate commutator form on \(V\). The four possible pairs \((d(u),d(v))\) always supply \(h\in\{u,v,uv\}\) with \(d(hA)=1\). Thus \(r\) and \(rh\) have different orders. Independently of every exact central offset, their commutators with a basis \(k,l\) of \(K\) recover two independent elements modulo \(A\), then \(z\), then \(a\), and hence all of \(H\). Therefore

\[
\langle r\rangle^G=\langle rh\rangle^G=\langle r,H\rangle
\]

inside \(G\). There are no uncovered elementary-centre pc rows. Subject to review of this and the preceding R1/\(C_4\) claims, the order-\(128\) remainder is eliminated; larger orders and the universal source problem remain outside this result.

- 2026-08-17T11:06:53Z — charged work stopped at the authorized boundary after filing the universal coverage bridge, run-local cumulative active minutes \(60\); state awaiting_lead. The current human-authorized increment has \(0\) unused active minutes.
