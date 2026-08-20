---
title: "Problem 20.115 proof lane: irreducible induction and primitive reduction"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
strategy: IRREDUCIBLE-INDUCTION-PRIMITIVE-REDUCTION
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Irreducible induction and primitive reduction

## Active-time ledger

- Work start: `2026-08-18T04:04:12Z`; official inherited cumulative active time: `01:27:19` (87 complete minutes). Increment cap: 45 active minutes. Safety stop: `2026-08-18T05:04:12Z`.

## Scope gate

- Active target: for every finite group \(G\), every ordinary irreducible complex character \(\chi\in\operatorname{Irr}(G)\), and every \(x\in G\), prove that \(\chi(x)\ne0\) implies \(o(x)\chi(1)\mid |G|\).
- Assignment revision: 1. All six canonical constraint rows are retained.
- The source transcription and current staleness gate were already completed and recorded in `Agents/Kourovka/problems/20.115/log.md`; the exact universal scope remains open.
- This proof lane uses no unreviewed `SU_3(8)` direct-scan premise and performs no open-web search.

## Strategy portfolio

Ranked by expected information per active hour:

1. **Theoretical induction lemma (selected).** Expand an induced character value exactly, audit cancellation, and propagate the desired divisibility from the inducing subgroup. Certificate: a line-by-line induced-value formula and integer divisibility calculation.
2. **Clifford/primitive structure (selected second).** Apply minimal-counterexample induction, Clifford correspondence, and kernel quotient descent to force a faithful quasiprimitive witness; then identify consequences for normal subgroups.
3. **Structured stress-test.** Test whether cancellation or order loss under induction/quotient invalidates either reduction. Kill immediately if the divisibility factors do not multiply cleanly.
4. **Catalogue mode (not selected).** A bounded table scan cannot prove the universal statement and would duplicate previous lanes.

Current hypothesis: induction from a proper subgroup preserves the target because a nonzero induced value forces at least one nonzero summand, and the subgroup index converts both character degree and group order exactly.

## 2026-08-18T04:10:22Z — exact induction lemma and cancellation audit

Let \(H\le G\), let \(\psi\) be a nonzero ordinary character of \(H\), and suppose

\[
\chi=\operatorname{Ind}_H^G\psi\in\operatorname{Irr}(G).
\]

First, \(\psi\) is automatically irreducible. Decompose

\[
\psi=\sum_i a_i\psi_i
\]

with \(a_i\in\mathbb Z_{\ge0}\) and \(\psi_i\in\operatorname{Irr}(H)\). Then

\[
\chi=\sum_i a_i\operatorname{Ind}_H^G\psi_i.
\]

Each induced summand is a nonzero genuine character, because its degree is \([G:H]\psi_i(1)>0\). An irreducible \(\chi\) cannot be a sum of two such characters or contain one with multiplicity above one. Hence exactly one coefficient is one and \(\psi\in\operatorname{Irr}(H)\). This prevents use of an excluded reducible character.

For \(x\in G\), choose representatives for the left cosets \(G/H\). The exact formula is

\[
\chi(x)=
\sum_{\substack{gH\in G/H\\g^{-1}xg\in H}}
\psi(g^{-1}xg).
\]

If \(\chi(x)\ne0\), at least one summand is nonzero. Thus some \(g\in G\) gives \(y=g^{-1}xg\in H\) with \(\psi(y)\ne0\). Cancellation is no obstruction: it may make nonzero terms sum to zero, but a nonzero sum cannot have every term zero. Also \(o_H(y)=o_G(x)\).

If any such \(y\) satisfies \(o(y)\psi(1)\mid |H|\), then

\[
o(x)\chi(1)
=[G:H]o(y)\psi(1)
\mid [G:H]|H|
=|G|.
\]

Therefore the exact induction lemma is valid. The cancellation kill criterion does not fire. In fact the local hypothesis can be weakened from “every relevant nonzero \(\psi(y)\)” to “one relevant nonzero \(\psi(y)\) having the divisibility.”

### Exact partial theorem

For every finite group \(G\), every monomial irreducible ordinary complex character

\[
\chi=\operatorname{Ind}_H^G\lambda\in\operatorname{Irr}(G),
\qquad \lambda(1)=1,
\]

and every \(x\in G\), the implication \(\chi(x)\ne0\Rightarrow o(x)\chi(1)\mid |G|\) holds. A linear \(\lambda\) never vanishes, and Lagrange gives \(o(y)\mid |H|\), so the lemma applies.

This coverage is character-level in arbitrary finite groups, not only in solvable groups. A concrete nonsolvable example is the degree-five irreducible of \(A_5\), induced from a nontrivial linear character of an \(A_4\) point stabilizer.

The example was checked with:

```text
gap -q -b -c 'g:=AlternatingGroup(5);; h:=Stabilizer(g,5);; irrh:=Irr(h);; lam:=Filtered(irrh,c->Degree(c)=1 and c<>TrivialCharacter(h))[1];; chi:=InducedClassFunction(lam,g);; Print("degree=",Degree(chi)," norm=",ScalarProduct(chi,chi)," irreducible=",IsIrreducibleCharacter(chi),"\n");; QUIT;'
```

Observed output:

```text
degree=5 norm=1 irreducible=true
```

Version command `gap -q -b -c 'Print(GAPInfo.Version,"\\n");; QUIT;'` returned `4.12.1`.

Subgroup identity command `gap -q -b -c 'g:=AlternatingGroup(5);; h:=Stabilizer(g,5);; Print("G_size=",Size(g)," H_size=",Size(h)," H_structure=",StructureDescription(h),"\\n");; QUIT;'` returned `G_size=60 H_size=12 H_structure=A4`.

More generally, the lemma covers any irreducible \(\chi=\operatorname{Ind}_H^G\psi\) for which the exact target is known for one relevant nonzero value of \(\psi\); in particular, \(H\) may be solvable while \(G\) is not.

Accordingly, a second exact partial class consists of all irreducible characters of arbitrary finite groups that are irreducibly induced from an irreducible character of a solvable subgroup. The known solvable theorem supplies the hypothesis only inside \(H\); the induction lemma transports it to \(G\).

## Minimal-counterexample reduction, all quantifiers explicit

For a finite group \(K\), define

\[
P(K):\quad
\forall\varphi\in\operatorname{Irr}(K)\ \forall z\in K,\quad
\varphi(z)\ne0\Longrightarrow o_K(z)\varphi(1)\mid |K|.
\]

If the universal target is false, choose a finite group \(G\) of least order with \(\neg P(G)\), then choose

\[
\chi\in\operatorname{Irr}(G),\qquad x\in G,\qquad
\chi(x)\ne0,\qquad o_G(x)\chi(1)\nmid |G|.
\]

Minimality says exactly:

\[
\forall K\text{ finite with }|K|<|G|\quad
\forall\varphi\in\operatorname{Irr}(K)\quad
\forall z\in K,\quad
\varphi(z)\ne0\Longrightarrow o_K(z)\varphi(1)\mid |K|.
\]

If \(\chi=\operatorname{Ind}_H^G\psi\) with \(H<G\), then \(\psi\in\operatorname{Irr}(H)\), minimality gives \(P(H)\), and the lemma contradicts the chosen failure. Therefore every character that occurs in a counterexample pair for a least-order counterexample group is primitive. This does not say that every irreducible character of \(G\) is primitive.

The witness is nonlinear, since degree-one characters never vanish and Lagrange settles them. Hence it is nonmonomial. The known solvable case makes \(G\) nonsolvable, but that fact is used only as a base-case exclusion.

## Stronger quotient and Clifford reductions

### Faithful quotient descent

Let \(K=\ker\chi\), let \(\overline G=G/K\), and let \(\overline\chi\in\operatorname{Irr}(\overline G)\) be the deflation. Put \(n=o_G(x)\) and \(m=o_{\overline G}(xK)\). Then

\[
\overline\chi(xK)=\chi(x)\ne0,\qquad
m\mid n,\qquad x^m\in K,\qquad
o_K(x^m)=n/m.
\]

Thus \(n/m\mid |K|\). If \(m\overline\chi(1)\mid |G/K|\), multiplying the two divisibilities gives \(n\chi(1)\mid |G|\). Contrapositively, every counterexample descends to a counterexample \((G/K,\overline\chi,xK)\) with faithful character. A least-order witness therefore has \(\ker\chi=1\).

### Primitive implies faithful quasiprimitive

Let \(N\trianglelefteq G\) be arbitrary and let \(\theta\in\operatorname{Irr}(N)\) be a constituent of \(\chi_N\). Put \(I=I_G(\theta)\). Clifford correspondence supplies \(\phi\in\operatorname{Irr}(I)\) with

\[
\operatorname{Ind}_I^G\phi=\chi.
\]

Primitivity forces \(I=G\). Hence \(\theta\) is \(G\)-invariant and Clifford's restriction formula becomes

\[
\chi_N=e_N\theta,\qquad e_N\in\mathbb Z_{>0}.
\]

Thus \(\chi\) is quasiprimitive. Because \(\chi\) is faithful,

\[
\ker\theta=\ker(\chi_N)=N\cap\ker\chi=1.
\]

If \(A\trianglelefteq G\) is abelian, then this \(\theta\) is a faithful \(G\)-invariant linear character. It embeds \(A\) in a finite subgroup of \(\mathbb C^\times\), so \(A\) is cyclic. Moreover,

\[
\theta(a^g)=\theta(a)\quad\Longrightarrow\quad a^g=a
\]

by faithfulness, so \(A\le Z(G)\). Therefore every abelian normal subgroup is cyclic central. An abelian minimal normal subgroup is central of prime order; a nonabelian minimal normal subgroup has the standard form \(S^t\) for a nonabelian finite simple group \(S\).

This Clifford reduction does not assume the target theorem.

### Linear-twist consequence for the center

Every linear twist \(\chi\lambda\), with \(\lambda\in\operatorname{Irr}(G/G')\), has the same degree and the same zero set as \(\chi\). Thus it is another counterexample character in the least-order group and must also be faithful.

Let \(z\in Z(G)\) have prime order \(p\). The faithful central character of \(\chi\) has \(\chi(z)=\chi(1)\mu(z)\), where \(\mu(z)\) is a primitive \(p\)-th root. If \(z\notin G'\), prescribe the value \(\mu(z)^{-1}\) on the order-\(p\) subgroup \(\langle zG'\rangle\le G/G'\); a complex linear character of a subgroup of a finite abelian group extends to the whole group. Thus a linear character \(\lambda\) of \(G/G'\) can be chosen with \(\lambda(z)=\mu(z)^{-1}\). Then \(z\in\ker(\chi\lambda)\), contradicting faithfulness. Hence every prime-order element of \(Z(G)\) lies in \(G'\).

Taking determinants, \(\det\chi\) is trivial on \(G'\), while

\[
(\det\chi)(z)=\mu(z)^{\chi(1)}.
\]

Therefore \(p\mid\chi(1)\) for every prime \(p\mid |Z(G)|\), or equivalently

\[
\operatorname{rad}(|Z(G)|)\mid\chi(1).
\]

This is an additional structural constraint, not a proof of the target.

### Relative-degree divisibility and normal generation by the witness

The homogeneous Clifford multiplicity has an additional standard divisibility:

\[
e_N\mid [G:N].
\]

Here is the independent route. On the multiplicity space of \(\theta\) in the representation affording \(\chi\), the quotient \(G/N\) has an irreducible projective representation of degree \(e_N\). Realize its finite-order factor set on a finite central extension

\[
1\longrightarrow C\longrightarrow \widetilde Q
\longrightarrow G/N\longrightarrow1
\]

with \(C\) finite cyclic, so that the projective representation lifts to an ordinary irreducible character of \(\widetilde Q\) of degree \(e_N\). Itô's character-degree theorem for an abelian normal subgroup says that every irreducible degree of \(\widetilde Q\) divides \([\widetilde Q:C]\). Hence

\[
e_N\mid[\widetilde Q:C]=|G/N|.
\]

This is a standard projective-degree lemma and is independent of the target conjecture.

Now let \(N\triangleleft G\) be proper. If \(x\in N\), then

\[
0\ne\chi(x)=e_N\theta(x),
\]

so \(\theta(x)\ne0\). Minimality applied to the smaller group \(N\) gives

\[
o(x)\theta(1)\mid |N|.
\]

Multiplying by \(e_N\mid[G:N]\) gives

\[
o(x)\chi(1)=e_No(x)\theta(1)\mid |G|,
\]

contrary to the chosen witness. Therefore

\[
x\notin N\qquad\text{for every proper normal subgroup }N\triangleleft G.
\]

Equivalently, the normal closure of the witnessing element is all of \(G\):

\[
\langle x^G\rangle=G.
\]

Passing to the abelianization, every conjugate of \(x\) has the same image. Hence

\[
G/G'=\langle xG'\rangle
\]

is cyclic, and \(|G:G'|=o_{G/G'}(xG')\mid o_G(x)\).

This is the stronger Clifford/primitive reduction sought by the assignment.

The argument also has a counterexample-descent form that does not presuppose least-order choice. If \(\chi\) is primitive, \(N\triangleleft G\), \(x\in N\), and \(\chi(x)\ne0\), then \(\chi_N=e_N\theta\) makes \(\theta(x)\ne0\). If \(o(x)\theta(1)\mid|N|\), the factor \(e_N\mid[G:N]\) yields the target divisibility upstairs. Consequently, if the pair upstairs is bad, \((N,\theta,x)\) is bad. Together with the induction and kernel descents, any hypothetical counterexample can be reduced strictly until:

- its character is primitive;
- its character is faithful;
- its nonvanishing element normally generates the group.

No solvability hypothesis enters this three-step descent.

## Sharpenings and closure checks

1. **Counterexample descent under induction.** If an imprimitive pair is a counterexample, every nonzero summand \(\psi(g^{-1}xg)\) in the induced-value formula is a counterexample pair in \(H\). If any one were good, the index calculation would make the original pair good.
2. **Counterexample descent through kernels.** The order-lift factor \(o(x)/o(xK)\) divides \(|K|\), so badness survives in the faithful quotient.
3. **Direct-product closure.** If \(P(A)\) and \(P(B)\), then \(P(A\times B)\). For \(\alpha\otimes\beta\in\operatorname{Irr}(A\times B)\), nonvanishing at \((a,b)\) implies nonvanishing of both factors. With \(n_A=o(a)\), \(n_B=o(b)\),

   \[
   \operatorname{lcm}(n_A,n_B)\alpha(1)\beta(1)
   \mid n_An_B\alpha(1)\beta(1)
   \mid |A||B|.
   \]

   Consequently a least-order counterexample group is directly indecomposable.

## Bottleneck

The surviving case is a nonlinear faithful quasiprimitive character of a nonsolvable directly indecomposable group with cyclic central abelian normal subgroups, together with an element \(x\) that normally generates \(G\). The standard projective-degree lemma settles the case \(x\in N\) for a proper normal subgroup \(N\), but it does not control a value at \(x\notin N\). Extending the homogeneous restriction argument to such elements would require new information about character values on cosets, not merely Clifford multiplicities.

## Formatting repair note

The first draft of this new run log was immediately regenerated because JavaScript string escaping had stripped backslashes from inline LaTeX and inserted tab/control escapes in \(\theta\) and \(\varphi\). The mathematical entries, command, and observed output were preserved; the repaired file was checked for nonprinting control characters before further work.

## Early 30-minute self-check — 2026-08-18T04:27:37Z

- Active increment: 23 minutes 25 seconds; official cumulative active time: `01:50:44`.
- Target/revision: exact universal ordinary-character scope, revision 1; all six constraints retained.
- Current hypothesis/evidence: the induced-value formula gives the exact induction closure; cancellation cannot block the existence of a nonzero summand. Kernel quotient descent, Clifford correspondence, projective-degree divisibility via Itô's theorem, and direct-product closure give a faithful primitive/quasiprimitive normally-generated reduction.
- Checkable partial theorem: all monomial irreducibles of arbitrary finite groups, and all irreducibles induced irreducibly from a character of a solvable subgroup, satisfy the target.
- Ruled out: the cancellation objection, the reducible-inducer loophole, and any least-order witness with imprimitive or nonfaithful character, with its element in a proper normal subgroup, or in a direct product of smaller target-good groups.
- Representation check: induction and homogeneous normal restriction were productive through the normally-generated case. They stop giving a value relation when \(x\) lies outside every proper normal subgroup.
- Two qualitatively different next routes: (1) use the generalized Fitting subgroup structure of faithful quasiprimitive linear groups; (2) derive a coset-value/projective-character trace relation for a normally generating element outside all proper normal subgroups.
- Recommended next experiment: first route the named projective-degree/Itô step and the normal-descent conclusion to Validator; if retained, ask MathExpert to choose between those two routes.
- Kill criterion: do not infer further divisibility from \(\chi_N=e_N\theta\) alone once \(x\notin N\); a next step must add genuine coset-value information or change representation.
- Constraint status: finite \(G\), ordinary irreducible \(\chi\), exact \(x\), and exact nonvanishing are used throughout. The conclusion is established only for the two stated character classes; `20.115-forall-G-chi-x` and the universal conclusion remain partial. There is no universal candidate and `active_assignment_answered: no`.

This checkpoint is slightly early because the named strategy already reached a checkable `PARTIAL_RESULT` and its precise structural bottleneck; continuing it without a representation-changing decision would be padding.

## Outcome and work stop — 2026-08-18T04:28:30Z

- Outcome: `PARTIAL_RESULT`.
- Increment charged: `00:24:18`.
- Official cumulative active time: `01:51:37`.
- Universal target: unanswered; `active_assignment_answered: no`.
- Compute: only two bounded GAP identity/irreducibility commands, each under three seconds; no heavy-compute lease required.
- Independence: no unreviewed `SU_3(8)` direct-scan result was read or used.
- State: `awaiting_lead` after filing the required Report.

### Ledger correction — 2026-08-18T04:30:29Z

The wording/control-character audit and bus-file check occurred after the preliminary stop entry. Final charged work stop: `2026-08-18T04:30:29Z`; increment: `00:26:17`; official cumulative active time: `01:53:36`. This supersedes only the preliminary `04:28:30Z` time totals; the `PARTIAL_RESULT` and `active_assignment_answered: no` outcome are unchanged.
