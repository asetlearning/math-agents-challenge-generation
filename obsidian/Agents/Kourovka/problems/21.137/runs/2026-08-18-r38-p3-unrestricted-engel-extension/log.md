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
---

# Cycle 26 log — P3-UNRESTRICTED-ENGEL-EXTENSION

## Active-time ledger

- 2026-08-18T05:39:35Z — work started at official cumulative minute 781; at most 45 new active minutes authorized.
- 2026-08-18T06:04:35Z — named Engel-extension gate met its exact survivor; research and packaging stopped after 25 new active minutes, official cumulative minute 806. Outcome: `PARTIAL_RESULT`; 20 authorized minutes returned unused pending Lead direction.

## Staleness and source gate

### 2026-08-18T05:41:41Z

`source_transcription_checked: yes`

I rendered and visually inspected page 184 of the configured issue-21 PDF. The exact source statement is:

> **21.137.** If the \(p\)-th powers in a finite \(p\)-group form a subgroup, must that subgroup be powerful? That is, for \(p\ne2\), if the \(p\)-th powers in a \(p\)-group of exponent \(p^2\) form a subgroup, must that subgroup be abelian? For a \(2\)-group of exponent \(8\), if the squares form a subgroup, must that subgroup be abelian? — L. Wilson

The item is unstarred and has no editor or later comment on the rendered page. The configured local corpus stops at issue 20, so JSON flags for 21.137 are unavailable. This discovery-blind scope has `open_web:false`; accordingly `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. The canonical synthesis records that issue 21 still lists the item open and that an external result concerns only the excluded exponent-eight clause.

`active_scope_checked: yes`

| source clause | equivalent formulation | active? | external match recorded in permitted context? |
|---|---|---:|---|
| General powerfulness question | actual \(p\)-power set subgroup \(\Rightarrow\) powerful | no | none used |
| Odd-prime exponent-\(p^2\) question | for odd \(p\), actual \(p\)-power set subgroup \(\Rightarrow\) abelian | yes; this run treats only the complete \(p=3\) subfamily | no exact match |
| Exponent-eight 2-group question | square set subgroup \(\Rightarrow\) abelian | no | an external claimed counterexample is recorded, but is irrelevant to this run |

### Constraint-and-conclusion checklist

| constraint_id | role | required condition | use in this run |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all admissible odd \(p,G\) | a \(p=3\) theorem is only a family partial, never the universal answer |
| `21.137-odd-p-not-2` | admissibility | \(p>2\) prime | freeze \(p=3\); exclude \(p=2\) |
| `21.137-odd-finite-p-group` | admissibility | finite same-\(p\) group | \(G\) finite 3-group |
| `21.137-odd-exponent-p2` | admissibility | exact exponent \(p^2\) | exponent exactly \(9\) |
| `21.137-odd-power-set-definition` | admissibility | literal set \(P=\{g^p:g\in G\}\) | literal cube image, never merely \(G^3\) unless closure proves equality |
| `21.137-odd-power-set-subgroup` | admissibility | literal power set is a subgroup | assumed; hence cube map is onto the subgroup \(P\) |
| `21.137-odd-P-abelian` | target | \(P\) abelian | must establish \([x^3,y^3]=1\) for all \(x,y\) |

The broader powerfulness question and the \(p=2\), exponent-eight sibling are excluded.

## Strategy portfolio

1. **Theoretical / minimal-quotient Engel reduction (first).** Derive from scratch that \(P\) and \(G/P\) have exponent at most three, prove the exponent-three 2-Engel/class-three facts actually used, then pass to a minimal hypothetical counterexample and analyze the induced action on \(P\) without assuming \(P\) abelian. Certificate: explicit lemmas with quotient-power-set equality and no classification citation.
2. **Structured extension / automorphism cube-root gate.** In the minimal reduction, encode a root \(x^3=a\in P\) as an automorphism \(\alpha_x\) of \(P\) satisfying \(\alpha_x^3=\operatorname{Inn}(a)\) and \(\alpha_x(a)=a\). Determine whether simultaneous realizability for every \(a\) forces \(P'=1\); if not, isolate the exact symplectic/Jordan obstruction that survives. Certificate: a reconstructible finite presentation or an exact automorphism-module datum, explicitly not a source counterexample unless all group axioms and literal cube closure are checked.
3. **Catalogue/small-case probe (low priority).** No catalogue computation is authorized or needed for the identity gate. A bounded GAP check would only test selected exponent-nine groups and could not prove the unrestricted family; heavy computation would require a frozen manifest and Lead lease.
4. **Direct commutator collection fallback.** Expand \([x^3,y^3]\) under only exponent-nine plus the independently proved extension identities and name the first surviving mixed commutator. Certificate: a checked collection identity in a precisely stated nilpotent quotient, not a formal Lie counterexample.

Kill criterion: if the Engel/minimal-extension identities reduce the target to an unconstrained automorphism norm or a surviving mixed commutator, record that exact term/model and recommend the smallest separate consistency test; do not claim that a formal object refutes the source problem.

## First deductions

- Because every element of the subgroup \(P\) is literally some cube \(g^3\), every element of \(P\) has cube \(g^9=1\). Thus \(P\) has exponent at most three. Because every \((gP)^3=P\), \(G/P\) also has exponent at most three.
- The literal closure makes \(P=G^3\) only in the sense that the literal cube image itself is already the subgroup generated by all cubes; no replacement of the value set by a generated subgroup was made.
- For every \(a\in P\), a chosen root \(x^3=a\) centralizes \(a\). On \(P\), conjugation \(\alpha_x\) satisfies \(\alpha_x^3=\operatorname{Inn}(a)\). This is the first mixed extension constraint and does not assume \(P\) abelian.

### 2026-08-18T05:48:45Z — protocol incident; output quarantined

I mistakenly treated a `timeout 55s` GAP SmallGroups probe as light because it was below 60 seconds. Common protocol §4 classifies GAP/enumeration runs themselves as heavy, independently of duration, so the command required a Lead lease. The unleased command was:

`timeout 55s gap -q Agents/Kourovka/problems/21.137/runs/2026-08-18-r38-p3-unrestricted-engel-extension/scratch/find-noncommuting-cubes.g`

It exited in 2.97 seconds after screening orders 81, 243, and 729, but **the output is quarantined and is not evidence for any claim or outcome**. I notified Lead immediately and will run no further GAP/enumeration computation without a lease.

## Independent Engel and minimal-counterexample reduction

### 2026-08-18T05:52:28Z

Let \(E\) be a group of exponent three. Linearizing the identity \(u^3=1\) (equivalently applying it to \(xy\), \(xz\), and \(xyz\)) gives the standard alternating triple-commutator law: repeated entries vanish, so \([x,y,y]=1\), and all fourfold commutators vanish. Thus an exponent-three group is 2-Engel and nilpotent of class at most three. In this run I use only those two consequences. Applied to the first deductions, both \(P\) and \(G/P\) are 2-Engel of class at most three; this does **not** bound the class of their mixed extension.

For a sharper extension analysis, suppose that a counterexample \(G\) of least order exists within the complete \(p=3\) subfamily. For every nontrivial \(N\triangleleft G\), the literal cube set of \(G/N\) is exactly
\[
 \{(gN)^3:g\in G\}=PN/N,
\]
which is a subgroup. If \(G/N\) still has exponent nine, minimality makes \(PN/N\) abelian; if its exponent is at most three, that cube set is trivial. In either case \(P'\leq N\). Therefore the nontrivial group \(W=P'\) lies in every nontrivial normal subgroup of \(G\). A minimal normal subgroup of a finite 3-group has order three and is central, so
\[
 P'=W\cong C_3\leq Z(G).
\]
In particular, a least counterexample has \(P\) of exponent three and class exactly two. No class-five result or previous run is used here.

Use the class-two Baer correspondence on \(P\): its underlying \(\mathbb F_3\)-Lie algebra \(L\) has \([L,L]=W=\mathbb F_3z\), and \(V=L/Z(L)\) has the nondegenerate alternating form \(\beta(\bar u,\bar v)z=[u,v]\). For a root \(x^3=a\in P\), let \(A_x\) be right conjugation by \(x\) on \(L\), put \(M_x=A_x-I\), and define \(D_a(u)=[u,a]\). Since \(x^3=a\), class two gives the exact mixed identity
\[
 A_x^3=I+D_a,
 \qquad M_x^3=D_a
 \tag{E1}
\]
(the second equality is the characteristic-three identity \((I+M)^3=I+M^3\)). Also \(M_xa=0\), because every element commutes with its own cube. Thus for two cube values \(a=x^3\), \(b=y^3\),
\[
 [b,a]=M_x^3b,\qquad [a,b]=M_y^3a. \tag{E2}
\]
The exponent-three quotient only says that the operator induced by \(M_x\) on \(V\) has cube zero. It does not kill the central value on the right of (E1)--(E2).

Choose a vector-space splitting \(L=U\oplus Z(L)\). Write
\[
 A_x=\begin{pmatrix}T&0\\ f&S\end{pmatrix},\quad n=T-I,\quad s=S-I.
\]
Because \(W\leq Z(G)\), \(T\) preserves \(\beta\) and \(S\) fixes \(z\). Cubing the block matrix and using characteristic three gives the exact lower-left equation
\[
 D_a=s^2f+sfn+fn^2. \tag{E3}
\]
If the whole center were fixed, only \(fn^2\) would remain and the usual symplectic Jordan-image restriction would follow. In the unrestricted extension, the term \(s^2f\) survives: a two-step unipotent action on the extra center can carry the nonzero inner functional even when \(T=I\). This is the precise obstruction to deriving cube centrality from the exponent-three/2-Engel layers alone.

### A genuine finite model for the surviving `s^2 f` term

This is a reconstructible group model for (E1)--(E3), **not** a source counterexample. Let
\[
P_0=\langle e,f,z_0,z_1,z_2\mid e^3=f^3=z_i^3=1,\ z_i\in Z(P_0),\ [e,f]=z_0\rangle,
\]
an order-\(3^5\), class-two, exponent-three group. Define an automorphism \(\alpha\) by
\[
e\mapsto e,\quad f\mapsto fz_2^2,\quad z_2\mapsto z_2z_1,
\quad z_1\mapsto z_1z_0,\quad z_0\mapsto z_0.
\]
Direct substitution gives \(\alpha^3(f)=fz_0^2=f^e\) and fixes the other generators as conjugation by \(e\) does; hence \(\alpha^3=\operatorname{Inn}(e)\) and \(\alpha(e)=e\). The consistent cyclic extension
\[
G_0=\langle P_0,x\mid x^{-1}px=\alpha(p)\ (p\in P_0),\ x^3=e\rangle
\]
has order \(3^6\) and exact exponent nine: it has three normal forms over \(P_0\), every cube lies in the exponent-three kernel, and \(x\) has order nine. Its cube \(e=x^3\) is noncentral because \([e,f]=z_0\ne1\). Thus (E1)--(E3) genuinely permit a noncentral cube; global literal cube-image closure, not the separate Engel layers, must supply any remaining proof.

### Exact noncommuting-cube survivor when literal closure is removed

There is an even sharper concrete boundary model requiring no computation. Let \(U=UT_7(\mathbb F_3)\), and put
\[
x=I+E_{12}+E_{23}+E_{34},\qquad
y=I+E_{45}+E_{56}+E_{67}.
\]
For every strictly upper triangular \(N\), \((I+N)^3=I+N^3\) in characteristic three. Hence
\[
x^3=I+E_{14},\qquad y^3=I+E_{47},\qquad
[x^3,y^3]=I+E_{17}\ne I. \tag{E4}
\]
The finite 3-group \(U\) has exact exponent nine. Its subgroup generated by all cubes lies in \(1+J^3\), has exponent three and class at most two, while the quotient by it has exponent three; so even stronger Engel/class bounds than the basic reduction coexist with (E4).

The missing canonical hypothesis is visible exactly: the literal cube set is not closed. Indeed
\[
x^3y^3=I+E_{14}+E_{47}+E_{17}.
\]
If this were \(I+N^3\), its \((1,4)\) entry would force
\(n_{12}n_{23}n_{34}=1\), and its \((4,7)\) entry would force
\(n_{45}n_{56}n_{67}=1\). Then the unique length-three path from 2 to 5 forces
\((N^3)_{25}=n_{23}n_{34}n_{45}\ne0\), contrary to the displayed product's zero \((2,5)\) entry. Thus this is an explicit `OUT_OF_SCOPE_EXAMPLE`, failing only the literal cube-set subgroup row among the p=3 structural hypotheses relevant here. It isolates \(E_{17}\) as an exact surviving mixed commutator and shows why closure must be used globally.

## What literal closure still says after the reduction

For a fixed coset \(xP\), write \(a=x^3\) and let \(T\) be the action of \(x\) on \(V=P/Z(P)\). If \(p\in P\) has image \(v\in V\), then the exact identity
\[
(xp)^3=x^3p^{x^2}p^xp
\]
gives, after projection to the abelian group \(V\),
\[
\overline{(xp)^3}=\bar a+(I+T+T^2)v
=\bar a+(T-I)^2v. \tag{E5}
\]
Thus the projected cube fibre over \(xP\) is the affine space
\(\bar a+\operatorname{im}(T-I)^2\). Literal surjectivity onto \(P\) forces the union of these affine fibres, over all cosets of \(P\), to cover all of \(V\).

Equation (E3) explains why this cover alone does not finish the proof. If \(S=I\) on \(Z(P)\), it forces the basepoint \(\bar a\) into the same double-Jordan image and a nilpotent-module argument becomes available. Without a center-action hypothesis, \(s^2f\) can place \(\bar a\) outside that image; the concrete cyclic extension above realizes exactly this case with \(T=I\). Consequently the surviving target term for two roots is
\[
 [x^3,y^3]=[a,b]=D_b(a)=M_y^3a\in W, \tag{E6}
\]
and neither the 2-Engel law in \(P\) and \(G/P\), nor the separate affine-fibre equations, forces (E6) to vanish. A proof must use a genuinely cross-fibre compatibility identity (or show that global literal coverage is incompatible with the `s^2f` central chain). The UT7 matrices show that deleting literal closure leaves (E6) nonzero in an actual finite exponent-nine 3-group.

## A global consequence: the center-action square must survive

Let \(H=G/P\), acting on \(V=P/Z(P)\) and on \(Z=Z(P)\); the actions factor through \(H\) because \(P\) acts trivially on both sections. Let \(I\) be the augmentation ideal of \(\mathbb F_3H\). Suppose, within the least-counterexample reduction above, that
\[
[Z(P),G,G]=1,
\quad\text{equivalently }ZI^2=0. \tag{E7}
\]
For a root action in (E3), this makes \(s^2=0\), so
\[
D_a=(sf+fn)n.
\]
Because the left side has values in the one-dimensional \(W\), its scalar coefficient factors through \(n\). Extending that coefficient functional from \(\operatorname{im}n\) to \(V\), and using the nondegenerate \(H\)-invariant symplectic form \(\beta\), gives
\[
\bar a\in\operatorname{im}(n^\dagger)\subseteq VI.
\]
Equation (E5) then puts the whole projected cube fibre over \(xP\) inside \(VI\), since \(\operatorname{im}n^2\subseteq VI\). Literal surjectivity of the cube map onto \(P\) forces \(V=VI\). But \(H\) is a finite 3-group, so its group-algebra augmentation ideal is nilpotent; iterating \(V=VI\) gives \(V=0\), contradicting nonabelian \(P\).

Therefore every least counterexample must satisfy the exact mixed-depth obstruction
\[
[Z(P),G,G]\ne1. \tag{E8}
\]
In particular, centralizing \(Z(P)\), or even a square-zero action on \(Z(P)\), would finish the least-counterexample argument. The pure \(s^2f\) term in (E3) is not cosmetic: it is the only term that evades this Nakayama argument, and the cyclic model realizes it by the chain \(z_2\mapsto z_1\mapsto z_0\mapsto0\).

## Cycle outcome and self-check

`PARTIAL_RESULT`, not a p=3 theorem. The exact target remains the finite, exact-exponent-nine, literal-cube-subgroup p=3 family; all seven canonical rows remain explicit in `findings.md`. Evidence is hand-derived. The accidental GAP output is quarantined. The named strategy has reached its kill criterion at (E3)/(E6): separate exponent-three and 2-Engel identities leave the pure central-action square \(s^2f\) and the genuine UT7 survivor. A materially different continuation must derive a cross-fibre central-cocycle identity from roots of products, with arbitrary-section covariance checked before reuse.
