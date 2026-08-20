---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
---

# P3-UNRESTRICTED-ENGEL-EXTENSION — partial reduction

## Outcome

`PARTIAL_RESULT` for the complete \(p=3\) subfamily; the source scope and the p=3 family remain unanswered.

Independently of the preceding class-five lane, a least p=3 counterexample must have
\[
P'=C_3\le Z(G),\qquad [Z(P),G,G]\ne1.
\]
The exact surviving mixed term is the square of the action on \(Z(P)\). It can carry
\([x^3,y^3]\) even though both \(P\) and \(G/P\) are exponent-three 2-Engel groups.

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: `2`

Run subfamily: finite 3-groups of exact exponent nine whose literal actual cube set is a subgroup; prove that subgroup abelian. A p=3 theorem would be a family partial only.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use/evidence | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible odd prime and group | this run freezes \(p=3\), so it cannot answer the universal odd-prime quantifier | partial only |
| `21.137-odd-p-not-2` | admissibility | odd prime \(p\ne2\) | \(p=3\) throughout | pass for run family |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime p-group | all reductions assume a finite 3-group; the boundary model is finite \(UT_7(3)\) | pass |
| `21.137-odd-exponent-p2` | admissibility | exact exponent \(p^2\) | exact exponent nine throughout; explicit order-nine unitriangular elements in the boundary model | pass |
| `21.137-odd-power-set-definition` | admissibility | literal actual power-value set | the cube map is treated as a value set; quotient equality and affine fibres are exact | pass |
| `21.137-odd-power-set-subgroup` | admissibility | literal cube set is a subgroup | assumed in the reduction; the UT7 boundary model explicitly fails this row | pass for reduction / fail for boundary model |
| `21.137-odd-P-abelian` | target | \(P\) abelian | reduced to a central term but not established | open |

The \(p=2\), exponent-eight sibling and the broader powerfulness question are excluded.

## Independent structural derivation

Since every element of the literal cube subgroup \(P\) is some \(g^3\), \(P\) has exponent at most three; \(G/P\) also has exponent at most three. The standard polarization of the exponent-three law gives the 2-Engel identity and nilpotency class at most three for each of these two groups. This supplies no class bound for the mixed extension.

Assume a p=3 counterexample of least order. For every nontrivial normal \(N\), the literal cube set in \(G/N\) is exactly \(PN/N\). Minimality when the quotient has exponent nine, and triviality of cubes when its exponent is at most three, both give \(P'\le N\). Hence \(P'=W\) is the unique minimal normal subgroup, so \(|W|=3\) and \(W\le Z(G)\). Thus \(P\) has class two.

Apply the class-two Baer correspondence. Write \(L=\log P\), \(V=L/Z(L)\), and \([L,L]=W=\mathbb F_3z\), with nondegenerate alternating form \(\beta\) on \(V\). If \(x^3=a\), right conjugation \(A_x\) on \(L\), with \(M_x=A_x-I\), satisfies
\[
M_x^3=D_a,\qquad D_a(u)=[u,a].
\]
For a splitting \(L=V\oplus Z(L)\), write
\[
A_x=\begin{pmatrix}T&0\\f&S\end{pmatrix},\qquad n=T-I,\quad s=S-I.
\]
Direct block cubing in characteristic three gives the exact mixed equation
\[
D_a=s^2f+sfn+fn^2. \tag{1}
\]
For \(p\in P\), the projected cube fibre of the coset \(xP\) is exactly
\[
\bar a+\operatorname{im}(T-I)^2. \tag{2}
\]
Literal cube surjectivity says that these affine fibres cover all of \(V\).

If \([Z(P),G,G]=1\), then \(s^2=0\), and (1) factors through \(n\). Symplectic duality puts every basepoint \(\bar a\) in the augmentation submodule \(VI\), where \(I\) is the augmentation ideal of \(\mathbb F_3[G/P]\). Equation (2) then puts every projected cube in \(VI\). Surjectivity gives \(V=VI\), impossible because \(I\) is nilpotent. Therefore a least counterexample necessarily has
\[
[Z(P),G,G]\ne1.
\]

## Exact surviving commutator and genuine boundary models

For roots \(x^3=a\), \(y^3=b\), the target term is exactly
\[
[x^3,y^3]=[a,b]=M_y^3a\in W.
\]
The term \(s^2f\) in (1) can be nonzero even when \(T=I\). The run log gives an explicit order-\(3^6\), exponent-nine cyclic extension of
\[
\langle e,f,z_0,z_1,z_2\mid e^3=f^3=z_i^3=1, z_i\in Z, [e,f]=z_0\rangle
\]
with a noncentral cube \(x^3=e\), realizing precisely that central Jordan chain. This model is not a counterexample because it does not supply two noncommuting values in a closed literal cube set.

The finite matrix group \(UT_7(3)\) gives an exact two-value boundary:
\[
x=I+E_{12}+E_{23}+E_{34},\quad y=I+E_{45}+E_{56}+E_{67},
\]
so \(x^3=I+E_{14}\), \(y^3=I+E_{47}\), and \([x^3,y^3]=I+E_{17}\ne I\). But \(x^3y^3\) cannot be a cube: any \(N^3\) with nonzero \((1,4)\) and \((4,7)\) entries must have nonzero \((2,5)\) entry. Thus this is an `OUT_OF_SCOPE_EXAMPLE` with an explicit failure of literal cube-set closure, not a source counterexample.

## What this does not establish

- It does not prove the p=3 subfamily, still less the universal odd-prime statement.
- It does not construct a group satisfying literal cube-set closure with nonabelian cube values.
- It does not bound the nilpotency class of \(G\); exponent-three kernel and quotient do not provide such a mixed bound.
- It does not show that the affine cover (2) alone controls the basepoints. The unrestricted \(s^2f\) term is exactly why it does not.
- The accidental unleased GAP probe recorded in the log is quarantined and supports none of these claims; every displayed result above is a hand derivation or explicit matrix calculation.

## Recommended continuation

Do not continue with separate 2-Engel identities: they stop exactly at (1). The next bounded proof experiment should pass to the central extension \(G/W\) and derive the **cross-fibre cocycle identity** imposed by a root of each product \(ab\). Its first gate is whether that identity kills the \(s^2f\) component in the last nonzero augmentation layer of \(Z(P)\). Kill the route immediately if arbitrary section/factor-set changes can realize that component while preserving all literal cube fibres.

Full derivations and the protocol incident are in `log.md` in this run directory.
