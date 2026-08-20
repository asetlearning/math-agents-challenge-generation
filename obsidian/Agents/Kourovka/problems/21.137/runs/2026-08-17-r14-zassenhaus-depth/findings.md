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
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
outcome: STRATEGY_EXHAUSTED
strategy: ZASSENHAUS-DEPTH-PUSH
active_assignment_answered: no
---

# ZASSENHAUS-DEPTH-PUSH — outcome

## Exact target

For every odd prime \(p\) and finite same-\(p\) group \(G\) of exponent exactly
\(p^2\), prove that the complete actual value set
\(P=\{g^p:g\in G\}\), if a subgroup, is abelian.

## Outcome

`STRATEGY_EXHAUSTED` for the pair-equation, section-independent Zassenhaus
depth-push only. The unrestricted target remains unanswered.

## Checkable method-failure lemma

Let \(D_n\) be the Zassenhaus filtration and
\(L=\bigoplus D_n/D_{n+1}\). Put \(A=x^p\), \(B=y^p\), with degree-\(p\)
symbols \(\alpha,\beta\). Closure gives an actual root \(z^p=AB\), whose
leading symbol \(\zeta\) satisfies \(\zeta^{[p]}=\alpha+\beta\).

Conjugation gives the permitted product root
\((z^A)^p=BA\), and \(z^A=z[z,A]\) with
\([z,A]D_{p+2}=[\zeta,\alpha]\). The first-live-degree relative norm is
\[
N_\zeta(v)=(\operatorname{ad}\zeta)^{p-1}v:
L_{p+1}\to L_{2p}.
\]
Therefore
\[
N_\zeta([\zeta,\alpha])
 = [\zeta^{[p]},\alpha]
 = [\alpha+\beta,\alpha]
 = [\beta,\alpha].
\]
Exactly at group level,
\[
z^{-p}(z^A)^p=(AB)^{-1}(BA)=[B,A].
\]
Thus the target commutator symbol lies in the permitted root-lift ambiguity for
every realized product-root label. Arbitrary section changes add the kernel of
\(N_\zeta\); different lower root labels and all higher jets are covered by the
exact relative norm
\[
\mathcal N_z(u)=z^{-p}(zu)^p
=u^{z^{p-1}}\cdots u^z u.
\]
For every \(i,j\in\mathbb F_p\), the same calculation for
\(z_{ij}^p=A^iB^j\) absorbs \(ij[\beta,\alpha]\). Hence the complete two-value
product-root polarization has no surviving coefficient that forces the bracket
one degree deeper.

If the actual first nonzero commutator symbol occurs after degree \(2p\), the
exact identity still puts that symbol in the full relative-root ambiguity at its
first live degree. Iterating this same pair-root comparison cannot produce a
section-independent depth push.

## Ambiguities explicitly retained

- **Product root:** only realized labels
  \(\zeta\in\{zD_2:z^p=AB\}\) are used; no assumption
  \(\zeta=X+Y\) is made.
- **Live lift:** its full linear image is
  \(\operatorname{im}(\operatorname{ad}\zeta)^{p-1}\), and fixed-value lift
  changes form the corresponding kernel.
- **Section:** a section of the actual power map need not be multiplicative or
  conjugation-equivariant; same-value section changes have exact relative norm
  one, while lower-label changes are retained in \(\mathcal N_z\).
- **Commutator root:** closure gives \(q^p=[B,A]\), but \(q\) may have a shallow
  nonzero \(p\)-null leading label. It is not legitimate to replace \(q\) by a
  homogeneous root in \(D_{\lceil r/p\rceil}\).

## What this rules out

It rules out a prime-uniform one-degree push obtained solely by antisymmetrizing
the existential pair equations \(A^iB^j=z_{ij}^p\) and then quotienting by all
root/section/lift choices. The desired symbol is itself one of those allowed
relative-norm images.

## What this does not establish

It does not prove or disprove that \(P\) is abelian. It does not rule out a
different invariant using genuine coherence among three or more product roots, a
minimal-counterexample restriction on root fibres, or another representation.
No example or computation was used.

## Evidence

The full conventions, norm-collection proof, scalar polarization, arbitrary-degree
relative-norm formulation, and source/constraint gates are in
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r14-zassenhaus-depth/log.md`.
