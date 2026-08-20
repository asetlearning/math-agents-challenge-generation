---
title: "Problem 20.115 partial result: induction closure and faithful quasiprimitive reduction"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
outcome: PARTIAL_RESULT
active_assignment_answered: no
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

# Induction closure and faithful quasiprimitive reduction

## Active target

For every finite group \(G\), every ordinary irreducible complex character \(\chi\in\operatorname{Irr}(G)\), and every \(x\in G\), prove

\[
\chi(x)\ne0\quad\Longrightarrow\quad o_G(x)\chi(1)\mid |G|.
\]

Scope: `20.115/nonzero-character-order-divisibility`, revision 1.

## Outcome

`PARTIAL_RESULT`. My exact induction calculation finds that cancellation does not block the lemma. It yields the target divisibility for every monomial irreducible character of every finite group and reduces any least-order counterexample to a nonlinear faithful quasiprimitive character of a nonsolvable directly indecomposable group whose abelian normal subgroups are cyclic central; moreover, the witnessing element normally generates the group. It does not settle the universal target.

## Exact induction lemma

Let \(H\le G\), let \(\psi\) be a nonzero ordinary character of \(H\), and assume \(\chi=\operatorname{Ind}_H^G\psi\in\operatorname{Irr}(G)\). Then \(\psi\in\operatorname{Irr}(H)\): otherwise its nonnegative irreducible decomposition would induce to a sum of at least two nonzero characters (counting multiplicity), contradicting irreducibility of \(\chi\).

For \(x\in G\),

\[
\chi(x)=\sum_{\substack{gH\in G/H\\g^{-1}xg\in H}}
\psi(g^{-1}xg).
\]

Thus \(\chi(x)\ne0\) implies that some \(y=g^{-1}xg\in H\) has \(\psi(y)\ne0\). This inference is immune to cancellation: cancellation may make nonzero terms sum to zero, but cannot make a nonzero sum out of all-zero terms. Since \(o_H(y)=o_G(x)\), any one such \(y\) satisfying \(o(y)\psi(1)\mid |H|\) gives

\[
o(x)\chi(1)=[G:H]o(y)\psi(1)\mid [G:H]|H|=|G|.
\]

Contrapositively, if an imprimitive pair \((G,\chi,x)\) is a counterexample, every nonzero summand in this formula yields a counterexample pair in the proper inducing subgroup.

## Exact partial theorem

The target holds for every triple \((G,\chi,x)\) in which

- \(G\) is any finite group, solvable or nonsolvable;
- \(\chi\in\operatorname{Irr}(G)\) is monomial, i.e. \(\chi=\operatorname{Ind}_H^G\lambda\) for a linear \(\lambda\in\operatorname{Irr}(H)\);
- \(x\in G\) and \(\chi(x)\ne0\).

Indeed \(\lambda(y)\ne0\) for all \(y\in H\) and \(o(y)\mid |H|\). This is not merely the excluded solvable restriction: the nonlinear degree-five irreducible of nonsolvable \(A_5\) is induced from a nontrivial linear character of \(A_4\). The bounded GAP check in the run log records degree 5, norm 1, and irreducibility of this induced character. More generally, the lemma covers any irreducible \(\chi=\operatorname{Ind}_H^G\psi\) for which the exact target is known for the relevant nonzero values of \(\psi\), including induction from a solvable subgroup into a nonsolvable group.

Thus a second exact covered class is: \(G\) arbitrary finite, \(H\le G\) solvable, \(\psi\in\operatorname{Irr}(H)\), and \(\operatorname{Ind}_H^G\psi\) irreducible. The target holds for that induced irreducible character of \(G\), even when \(G\) is nonsolvable. This uses the known solvable theorem only on \(H\), then transports it by the lemma; it does not present solvability as a universal proof.

## Least-order counterexample theorem

Assume a counterexample exists. Choose \(G\) with least possible order among all finite groups admitting one, and choose any \(\chi\in\operatorname{Irr}(G)\), \(x\in G\) with \(\chi(x)\ne0\) and \(o(x)\chi(1)\nmid |G|\). Then for every finite \(K\) with \(|K|<|G|\), every \(\varphi\in\operatorname{Irr}(K)\), and every \(z\in K\),

\[
\varphi(z)\ne0\Longrightarrow o(z)\varphi(1)\mid |K|.
\]

The induction lemma therefore forces this witnessing \(\chi\) to be primitive. It is nonlinear and nonmonomial, and \(G\) is nonsolvable. These assertions apply to each character that witnesses failure in a least-order counterexample group, not to every member of \(\operatorname{Irr}(G)\).

## Faithful quasiprimitive strengthening

Let \(K=\ker\chi\), \(n=o_G(x)\), and \(m=o_{G/K}(xK)\). Then \(m\mid n\), \(x^m\in K\), and \(o(x^m)=n/m\mid |K|\). If the quotient pair obeyed \(m\chi(1)\mid |G/K|\), multiplying the two divisibilities would give \(n\chi(1)\mid |G|\). Thus every counterexample descends to a counterexample with faithful character in \(G/K\), and a least-order witness has \(\ker\chi=1\).

For each \(N\trianglelefteq G\), choose \(\theta\in\operatorname{Irr}(N)\) below \(\chi\) and let \(I=I_G(\theta)\). Clifford correspondence writes \(\chi=\operatorname{Ind}_I^G\phi\) for some \(\phi\in\operatorname{Irr}(I)\). Primitivity gives \(I=G\), so

\[
\chi_N=e_N\theta
\]

with \(\theta\) \(G\)-invariant. Hence \(\chi\) is quasiprimitive. Faithfulness gives \(\ker\theta=1\). If \(A\trianglelefteq G\) is abelian, then this \(\theta\) is a faithful \(G\)-invariant linear character; consequently \(A\) is cyclic and \(A\le Z(G)\). An abelian minimal normal subgroup is therefore central of prime order. The direct-product calculation in the run log also makes a least-order counterexample group directly indecomposable.

Linear twisting gives a further center constraint. Every \(\chi\lambda\), with \(\lambda\) linear, is another counterexample character and hence faithful. If a prime-order \(z\in Z(G)\) were outside \(G'\), one could choose \(\lambda(z)\) to cancel the faithful central scalar of \(\chi(z)\), making \(z\in\ker(\chi\lambda)\). Thus all prime-order central elements lie in \(G'\); taking determinants then gives

\[
\operatorname{rad}(|Z(G)|)\mid\chi(1).
\]

The Clifford multiplicity satisfies the standard divisibility

\[
e_N\mid[G:N].
\]

Indeed \(e_N\) is the degree of an irreducible projective representation of \(G/N\). Lift it to an ordinary irreducible representation of a finite central extension \(\widetilde Q\) with cyclic central kernel \(C\). Itô's theorem for the abelian normal subgroup \(C\) gives \(e_N\mid[\widetilde Q:C]=|G/N|\). This uses no instance of the target conjecture.

If \(N\triangleleft G\) is proper and \(x\in N\), then \(\chi(x)=e_N\theta(x)\ne0\), so minimality gives \(o(x)\theta(1)\mid|N|\). Together with \(e_N\mid[G:N]\), this forces \(o(x)\chi(1)\mid|G|\), a contradiction. Therefore the witnessing element lies in no proper normal subgroup:

\[
x\notin N\quad\text{for every proper }N\triangleleft G.
\]

Equivalently, \(\langle x^G\rangle=G\).

Since all conjugates of \(x\) have the same image in the abelianization, this also forces

\[
G/G'=\langle xG'\rangle
\]

to be cyclic, with \(|G:G'|=o_{G/G'}(xG')\mid o_G(x)\).

More generally, before choosing a least-order witness, this gives a strict descent: a bad primitive pair with \(x\in N\triangleleft G\), \(N<G\), forces the bad pair \((N,\theta,x)\). Combining this with the inducing-subgroup descent and faithful-quotient descent shows that any hypothetical counterexample has a descendant with primitive faithful character whose nonvanishing element normally generates its group.

## Constraint-and-conclusion audit

| constraint id | treatment | result |
|---|---|---|
| `20.115-forall-G-chi-x` | Retained in defining the target and in the explicit minimality quantifiers; the partial theorem restricts only the character to be monomial. | partial only |
| `20.115-G-finite` | Used in Lagrange, induction degrees, quotient orders, and Clifford theory. | pass |
| `20.115-chi-complex-irreducible` | Used essentially; an inducing genuine character is shown automatically irreducible. No Brauer or reducible character is substituted. | pass |
| `20.115-x-in-G` | Exact element order is preserved under conjugacy; quotient order loss is accounted for by \(o(x)/o(xK)\mid |K|\). | pass |
| `20.115-character-value-nonzero` | Used exactly to force a nonzero summand of the induced-value formula. | pass |
| `20.115-order-degree-divisibility` | Established for monomial irreducibles and transported by the induction lemma; not established for all primitive irreducibles. | partial only |

## What this does not establish

It gives neither a universal proof nor a counterexample. Faithful quasiprimitive characters of nonsolvable groups remain when the nonvanishing element normally generates the group. The standard projective-degree divisibility controls the Clifford multiplicity, but homogeneous restriction gives no value formula for \(x\notin N\), which is exactly the surviving case.

## Evidence

Full derivations, the cancellation audit, the bounded \(A_5/A_4\) command and observed output, and direct-product calculation are in `Agents/Kourovka/problems/20.115/runs/2026-08-18-r10-irreducible-induction-primitive-reduction/log.md`.
