---
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 16
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

# Candidate defect-zero Clifford obstruction lemma

## Active target

Scope: `20.115/nonzero-character-order-divisibility`, revision 1.

The universal source assertion is still open. This note supplies a candidate
prime-local lemma and a candidate almost-simple consequence for independent
validation.

## Candidate lemma

Let \(S\) be a finite group, let \(S\triangleleft A\), let
\(\phi\in\operatorname{Irr}(S)\) be \(A\)-invariant, and let \(p\) be a prime
such that
\[
 v_p(\phi(1))=v_p(|S|).
\]
Let \([\alpha]\in H^2(A/S,\mathbb C^\times)\) be the Clifford obstruction to
extending \(\phi\). Then the candidate conclusion is
\[
 [\alpha]_p=1,
 \qquad\text{equivalently}\qquad
 v_p(\operatorname{ord}[\alpha])=0.
\]
In fact, if \(P\in\operatorname{Syl}_p(A/S)\) and \(H/S=P\), then \(\phi\)
extends to \(H\). Simplicity is not used in this lemma; it is used in the
almost-simple corollary through \(S=\operatorname{Inn}(S)\) and Schreier
solvability of \(A/S\).

## Reconstruction of the obstruction

Put \(Q=A/S\) and let \(\rho:S\to\operatorname{GL}(V)\) afford \(\phi\), with
\(n=\phi(1)\). Choose a section \(q\mapsto a_q\) and intertwiners \(T_q\) with
\(T_q\rho(s)T_q^{-1}=\rho(a_q(s))\). If
\(a_qa_r=\iota_{s(q,r)}a_{qr}\), Schur's lemma gives scalars
\(\alpha(q,r)\) through
\[
 T_qT_r=\alpha(q,r)\rho(s(q,r))T_{qr}.
\]
Their class is independent of choices. Its restriction to a subgroup of \(Q\)
is the extension obstruction over the inverse image of that subgroup, and the
class is trivial exactly when the intertwiners can be rescaled to an honest
extension.

For nonabelian simple \(S\), \(S\) is perfect, hence
\(\det\rho(s)=1\). Taking determinants in the displayed equation gives
\([\alpha]^n=1\). This determinant bound alone is in the wrong direction for a
defect-zero prime, because \(p^{v_p(|S|)}\mid n\); it does not kill the
\(p\)-part.

## Block proof on a Sylow inverse image

Fix \(P\in\operatorname{Syl}_p(Q)\) and let \(H\) be its inverse image.

1. **Defect-zero block theorem.** An ordinary irreducible character of
   \(p\)-defect zero is the sole ordinary irreducible character in a block
   \(b\) of defect zero. Thus \(b=\{\phi\}\), and \(b\) is \(H\)-stable because
   \(\phi\) is.
2. **Stable block over a \(p\)-group quotient.** For
   \(S\triangleleft H\), \(H/S=P\), and an \(H\)-stable block \(b\), there is a
   unique block \(B\) of \(H\) covering \(b\). A defect group \(D\) of \(B\)
   can be chosen with \(D\cap S\) a defect group of \(b\) and \(DS=H\).
   Hence here \(D\cap S=1\), \(D\cong P\), and \(B\) has defect
   \(v_p(|P|)\).
3. Choose a height-zero \(\chi\in\operatorname{Irr}(B)\). Since \(b\) has only
   \(\phi\) and \(\phi\) is invariant, Clifford theory gives
   \(\chi_S=e\phi\). Comparing character defects gives
   \[
   v_p(|H|/\chi(1))=v_p(|P|)-v_p(e).
   \]
   Height zero and \(|D|=|P|\) make the left side \(v_p(|P|)\), so
   \(v_p(e)=0\).
4. Clifford theory identifies \(e\) with the degree of an irreducible
   \(\alpha^{-1}|_P\)-projective representation of \(P\). Since
   \(H^2(P,\mathbb C^\times)\) is a \(p\)-group, the factor set can be realized
   on a finite central \(p\)-extension \(\widehat P\). Thus \(e\) is the degree
   of an irreducible character of a finite \(p\)-group and is a power of \(p\).
   Together with \(v_p(e)=0\), this forces \(e=1\). A one-dimensional
   projective representation makes the factor set a coboundary. Therefore
   \(\operatorname{res}^Q_P[\alpha]=1\).
5. Restriction followed by corestriction on \(H^2(Q,\mathbb C^\times)\)
   multiplies by \([Q:P]\). This is prime to \(p\), so restriction to \(P\) is
   injective on the \(p\)-primary subgroup. Hence \([\alpha]_p=1\).

The exact standard block-covering statement in step 2, including its defect
group conclusion, is the main item Validator should independently check. No
classification or character-table calculation enters the candidate lemma.

## Modular/projectivity cross-check and its limitation

Over a splitting \(p\)-modular system \((K,\mathcal O,k)\), the defect-zero
block algebra is a matrix algebra and its unique simple module is projective.
The strongly \(P\)-graded covering algebra is Morita equivalent to a twisted
group algebra \(\mathcal O_{\alpha}P\). A \(p\)-primary cocycle may be chosen
with values in \(p\)-power roots of unity; all reduce to 1 in characteristic
\(p\), so the reduction is Morita equivalent to the local algebra \(kP\).
This recovers uniqueness/full defect of the covering block and the height
argument above.

Modular extendibility by itself is **not** a proof: reduction sends every
\(p\)-power root of unity to 1, so it is blind to exactly the ordinary
\(p\)-primary obstruction being tested. The height-zero ordinary lift is the
essential extra step.

## Exact scalar valuation supplied

In the defect-zero case the available component character defect is
\(v_p(|S|/\phi(1))=0\). Therefore the transfer cannot absorb even one extra
\(p\)-factor in a scalar kernel: the exact needed bound is
\[
 v_p(\operatorname{ord}[\alpha])\le
 v_p(|S|/\phi(1))=0.
\]
The lemma supplies precisely this. Merely extending after a central cover is
insufficient if that cover has a nontrivial \(p\)-kernel. After the lemma, one
may linearize the remaining class on a central **\(p'\)-cover**, so passage to
lifts preserves all \(p\)-parts of element orders and group orders.

## Candidate `t=1` almost-simple equality corner

Assume now that \(S\) is nonabelian simple,
\(S\le A\le\operatorname{Aut}(S)\), \(Q=A/S\), and
\(\chi\in\operatorname{Irr}(A\mid\phi)\). Standard invariant Clifford theory
writes
\[
 \chi(a)=\Phi(a)\eta(\bar a),\qquad
 \chi(1)=\phi(1)\eta(1),
\]
where \(\Phi\) and \(\eta\) are projective characters with inverse factor
sets \(\alpha\) and \(\alpha^{-1}\).

Because \([\alpha]_p=1\), replace it by a cohomologous factor set of
\(p'\)-order and linearize both factors on pullback central \(p'\)-covers
\(\widehat A\) and \(\widehat Q\). If \(\chi(x)\ne0\), both lifted ordinary
factors are nonzero.

- The lifted \(\Phi\) lies in a block of \(\widehat A\) covering the
  defect-zero block of \(Z\times S\). Any defect group \(D\) of that covering
  block satisfies \(D\cap(Z\times S)=1\). Brauer's block vanishing theorem says
  nonzero value at a lift \(\widehat x\) forces its \(p\)-part into a conjugate
  of \(D\). Projection is injective on \(D\), and the central kernel is \(p'\),
  so
  \[
  o(x)_p=o(\bar x)_p.
  \]
- By Schreier's theorem, \(Q\le\operatorname{Out}(S)\) is solvable; its central
  \(p'\)-extension \(\widehat Q\) is solvable. Applying the already-known
  solvable case of the **ordinary source assertion** to the lifted irreducible
  character \(\widehat\eta\) and a lift of \(\bar x\) gives
  \[
  o(\bar x)_p\eta(1)_p\le |Q|_p.
  \]

Consequently
\[
 o(x)_p\chi(1)_p
 =o(\bar x)_p\,|S|_p\,\eta(1)_p
 \le |S|_p|Q|_p=|A|_p.
\]
This is the exact primewise equality bound for the one-component invariant
almost-simple corner. It still needs Validator to check (i) the projective
factorization on compatible \(p'\)-covers and (ii) the covering-block defect
intersection used in Brauer vanishing.

## One-group diagnostic: why full extendibility is too strong

A bounded GAP 4.12.1 check of `A6 < A6.2^2 = Aut(A6)` used
`scratch/a6_diagnostic.g`, SHA-256
`cae60c15fb05b0940fc4d70d24db663b73b8f6172867e4795ef1570dcde12356`.
It found the unique fusion
`[1,2,3,3,4,5,5]`, invariant `A6` rows of degrees `1,9,10`, four degree-9
extensions, and a single degree-20 row restricting as twice the invariant
degree-10 row. Thus the degree-10 character has the nontrivial class in
\(H^2(C_2^2,\mathbb C^\times)\cong C_2\); invariance does not imply extension.

This is consistent with the candidate lemma: degree 10 is 5-defect zero in
\(A_6\), while its obstruction has order 2. It is not 2-defect zero
(\(|A_6|_2=8\), \(10_2=2\)). The datum therefore illustrates prime-specific
sharpness and is neither a counterexample to the lemma nor to Problem 20.115.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | present result | result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | only an invariant almost-simple prime-local corner | not discharged |
| `20.115-G-finite` | admissibility | finite group | all groups in the lemmas are finite | pass for covered corner |
| `20.115-chi-complex-irreducible` | admissibility | ordinary complex irreducible | \(\phi,\chi\), and lifted quotient characters are ordinary; modular data are proof vehicles | pass for covered corner |
| `20.115-x-in-G` | admissibility | actual element and exact order | the block-vanishing step compares the actual \(p\)-part with its quotient image through an injective defect group | pass for covered corner, pending validation |
| `20.115-character-value-nonzero` | admissibility | exact ordinary value nonzero | used to make both projective factors nonzero and invoke Brauer vanishing / solvable source theorem | pass for covered corner, pending validation |
| `20.115-order-degree-divisibility` | target conclusion | \(o(x)\chi(1)\mid|G|\) | candidate primewise inequality only in the stated invariant almost-simple defect-zero corner | partial only |

## What this does not establish

- It does not prove the universal source assertion.
- It does not import or validate the preceding component-cycle calculation, and
  does not settle multi-component permutation cycles.
- It does not say that \(\phi\) extends to all of \(A\); only the \(p\)-part of
  the obstruction is killed.
- The two block-theoretic bridge statements explicitly flagged above have not
  yet received independent review.
- The `A6` calculation is a route diagnostic only, not a source witness.

## Continuation recommendation

Route the candidate obstruction lemma and the `t=1` corollary to a fresh
Validator. If both block bridges pass, the next useful experiment is for a
fresh MathExpert to splice the exact zero scalar valuation into a separately
reviewed component-cycle inequality. Do not spend another solver increment on
catalogue searches for nonextendible characters unless Validator rejects a
specific block step.

