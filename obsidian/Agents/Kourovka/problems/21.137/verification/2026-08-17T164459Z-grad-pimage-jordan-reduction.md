---
title: "Verification — Kourovka 21.137 — first power-image quotient and Jordan obstruction"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "A hypothetical counterexample has a first lower-central quotient whose literal p-power image forces a length-(p+1) Jordan chain plus an independent fixed vector, the bounds |Pbar|>=p^(p+2) and |G|>=p^(p+3), and an abelian power image in the action quotient; a dimension-(p+2) cyclic extension is sharp only for the local product-root equation."
claimant: Problem-21.137-Proof
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the set P={g^p:g in G} of actual p-th powers is a subgroup, then P is abelian."
excluded_scopes: ["the general powerfulness clause", "21.137/two-group-exponent-8", "generated-power-subgroup substitutes", "odd-prime groups of exponent other than exactly p^2"]
target_object: "Every finite odd-prime p-group of exact exponent p^2 whose literal p-th-power value set is a subgroup."
witness_object: "A quotient of an assumed counterexample for the necessary-condition lemma; separately, a constructed local Baer group and cyclic extension realizing one product-root equation."
witness_equals_target: false
citation: "Internal reviewed dependency: Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md; no external citation."
verification_method: "Independent hostile hand reconstruction in class-two Baer/BCH coordinates and elementary quotient calculations."
tools_used: ["GAP 4.12.1 (availability probe only)", "Python 3.12.3 (availability probe and protocol state check only)", "pdftotext", "pdftoppm"]
scope_answered: ["necessary first-lower-central-quotient obstruction for any hypothetical counterexample", "sharpness of the single product-root equation"]
scope_not_answered: ["21.137/odd-prime-exponent-p2", "the general powerfulness clause", "21.137/two-group-exponent-8"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/lie-methods, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## The claim

The submitted necessary-condition lemma survives hostile hand reconstruction,
with one notation correction: under the declared group convention

\[
[u,v]=u^{-1}v^{-1}uv,\qquad u^v=v^{-1}uv,
\]

the convention-free operator identity is

\[
D^p(x)=[x,q]. \tag{1}
\]

Thus (1) is \(D^p=\operatorname{ad}^{R}_{q}\) for the **right** adjoint
\(\operatorname{ad}^{R}_{q}(x)=[x,q]\).  With the standard left-adjoint
notation \(\operatorname{ad}_{q}(x)=[q,x]\), the submitted display must read

\[
D^p=-\operatorname{ad}_{q}. \tag{2}
\]

The claimant's immediately following equation
\(D^p(a)=[a,q]=[a,b]\) has the correct sign, so this is a notation/sign repair,
not a failure of the Jordan or order argument.

The sharp local extension also has exponent exactly \(p^2\).  A further
independent calculation below shows that **all of its actual \(p\)-th powers
commute**.  It therefore cannot accidentally be an in-scope nonabelian
power-image witness, whether or not its value set is closed.

## Scope, revision, and clause matrix

The canonical record is revision 2 of
`21.137/odd-prime-exponent-p2`.  The statement was independently read from
source PDF page 184 and visually checked on the rendered page.

| source clause | active? | result of this verification |
|---|---:|---|
| If the power values in a finite \(p\)-group form a subgroup, must it be powerful? | no | not addressed |
| If \(p\ne2\), \(\exp G=p^2\), and the actual \(p\)-power values form a subgroup, must it be abelian? | **yes** | a necessary condition is checked; the universal conclusion is not proved |
| If a 2-group has exponent 8 and its squares form a subgroup, must it be abelian? | no | not addressed |

`active_assignment_answered: no`.

The linked claim-check JSON contains every canonical constraint exactly once.
Its `21.137-odd-forall-p-G` row is `unknown`, its conclusion row is
`not_proved`, and `ready_for_validator` is correctly `false`.  The protocol
state checker reports zero errors.  This is consistent with a routed
`PARTIAL_RESULT`; it forbids treating the artifact as a whole-scope claim.

## Constraint-and-conclusion matrix

| constraint_id | role | source requirement | independent result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying \(p,G\) | **unknown for the target**; the argument is conditional on a hypothetical counterexample |
| `21.137-odd-p-not-2` | admissibility | \(p>2\) prime | pass for the partial lemma; class 2 is then less than \(p\), and \(1/2\in\mathbb F_p\) |
| `21.137-odd-finite-p-group` | admissibility | finite same-\(p\) group | pass for the conditional quotient and for the finite sharp model |
| `21.137-odd-exponent-p2` | admissibility | exact exponent \(p^2\) | pass for the first quotient and sharp extension by explicit elements of order \(p^2\) |
| `21.137-odd-power-set-definition` | admissibility | literal set \(\{g^p\}\) | pass for the first quotient; its literal value set is exactly the image of \(P\) |
| `21.137-odd-power-set-subgroup` | admissibility | the literal value set is a subgroup | pass for the first quotient; the sharp model is not submitted under this row |
| `21.137-odd-P-abelian` | target conclusion | \(P\) abelian | **not proved** |

## Target versus witness

The source target is a universal class of finite groups.  The main proof object
is produced only after assuming a counterexample; it yields a necessary
condition and is not itself an independently exhibited witness.  The sharpness
object is deliberately built from the local operator equation and does not
have the designated nonabelian Baer subgroup as its literal power image.

Accordingly, `witness_equals_target: false`.  There is no circular inference:
the quotient calculation is used only conditionally, while the model built to
satisfy the local equation is used only to prove that this one local equation
cannot yield a stronger dimension estimate.

## Subclaims and what each method proves

| subclaim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| literal power image survives the first quotient | direct image calculation | the quotient is itself a source-admissible counterexample if one started with a counterexample | existence or nonexistence of a counterexample |
| Baer linearization and (1) | functorial class-two BCH calculation | exact root transgression and its sign | any relation among operators from different root choices |
| chain plus extra vector | cyclic-module argument | \(\dim\bar P\ge p+2\) | that the extra vector is a separate \(J_1\) summand |
| ambient order bound | explicit nontrivial coset represented by the product root | \(|G|\ge p^{p+3}\) | optimality for genuine counterexamples |
| action-quotient power image | two inclusions on literal value sets | \(U^{\{p\}}=\operatorname{Inn}(\bar P)\) | recovery of \(\bar P'\), which the action kills |
| sharp model | direct bracket, automorphism, central quotient, exponent, and power-image audit | local dimension sharpness and no accidental witness | closure of its literal value set or the active conclusion |

## Evidence

### 1. The first lower-central quotient retains the literal power image

Assume that \(G\) is a counterexample and write

\[
P=\{g^p:g\in G\}.
\]

Because this literal set is a subgroup, it equals the verbal subgroup \(G^p\),
but more is true: every element of \(P\), not merely every chosen generator,
is an actual \(p\)-th power.  Hence \(x^p=1\) for every \(x\in P\), so
\(\exp P\mid p\).

Let

\[
c=\min\{i:P'\not\leq\gamma_{i+1}(G)\},\qquad
N=\gamma_{c+1}(G),\qquad Q=G/N.
\]

Since \(P'\leq\gamma_2(G)\), one has \(c\ge2\); minimality gives
\(P'\leq\gamma_c(G)\).  Put \(\bar P=PN/N\).  Directly,

\[
\{(gN)^p:g\in G\}=\{g^pN:g\in G\}=PN/N=\bar P. \tag{3}
\]

The second equality in (3) uses the literal-value property: each element of
\(P\) is one \(g^p\).  Thus the quotient has the literal power image, not just
the subgroup generated by that image, and it remains a subgroup.

Moreover,

\[
\bar P'=P'N/N\ne1,
\qquad
\bar P'\leq\gamma_c(Q)\leq Z(Q).
\]

Therefore \(\bar P\) is nonabelian of class two and exponent dividing \(p\).
Choose noncommuting \(A,B\in\bar P\).  Then \(AB\ne1\), and (3) supplies
\(z\in Q\) with \(z^p=AB\).  Since \(\exp Q\mid p^2\), this \(z\) has order
exactly \(p^2\).  Consequently \(Q\) has exponent exactly \(p^2\), so it is
itself in the active source class and remains a counterexample.

The previously checked class-at-most-\(p+1\) theorem therefore applies to
\(Q\): its noncommuting powers force

\[
\operatorname{cl}(Q)\ge p+2.
\]

This dependency is exactly the internal verification named in the
frontmatter; no stronger class assertion is imported.

### 2. Baer correspondence and the exact sign

Because \(p\) is odd and \(\bar P\) has class two and exponent \(p\), the
class-two Baer correspondence applies (equivalently, BCH truncates after the
bracket and only \(2^{-1}\) is required).  Write \(L=\log(\bar P)\), and put

\[
a=\log A,\quad b=\log B,\quad q=\log(AB),\quad
\alpha=c_z|_{\bar P},\quad D=\alpha-I.
\]

The subgroup \(\bar P\) is characteristic as a literal power-value subgroup,
so conjugation by \(z\) really restricts to an automorphism.  Functoriality of
the Baer correspondence makes \(\alpha\) linear.

For right conjugation \(x^g=g^{-1}xg\), the class-two BCH calculation is

\[
\log((\exp x)^{\exp q})=x+[x,q]. \tag{4}
\]

Hence

\[
\alpha^p=c_{z^p}=c_{AB}=I+\operatorname{ad}^{R}_{q}.
\]

Since \(I\) and \(D\) commute and the endomorphism algebra has
characteristic \(p\),

\[
(I+D)^p=I+D^p.
\]

This proves (1), and also proves the standard-adjoint version (2).  It audits
both the conjugation sign and the characteristic-\(p\) binomial step.

In BCH coordinates,

\[
q=a+b+\tfrac12[a,b],
\quad [a,q]=[a,b]=:c_0\ne0. \tag{5}
\]

Because \(z\) centralizes its own power \(z^p=AB\), one has \(Dq=0\).  Because
\(c_0=\log[A,B]\) lies in \(\log(\bar P')\subseteq\log Z(Q)\), conjugation by
\(z\) fixes it, so \(Dc_0=0\).  Equations (1) and (5) now give

\[
D^pa=c_0\ne0,
\qquad D^{p+1}a=0. \tag{6}
\]

### 3. Chain independence, the extra vector, and both order bounds

Equation (6) says that the minimal polynomial of \(D\) on the cyclic vector
\(a\) has degree \(p+1\).  Therefore

\[
a,Da,\ldots,D^pa
\]

are linearly independent and span a \(J_{p+1}\) cyclic block.  The kernel of
\(D\) on this span is exactly \(\langle c_0\rangle\).

The vector \(q\) is fixed by \(D\), but it is not central because
\([a,q]=c_0\ne0\).  If \(q\) lay in the displayed cyclic span, it would lie in
its kernel and hence be a scalar multiple of the central vector \(c_0\), a
contradiction.  Thus

\[
\dim_{\mathbb F_p}L\ge p+2,
\qquad |\bar P|=p^{\dim L}\ge p^{p+2}. \tag{7}
\]

This proves an independent fixed vector, not necessarily a direct \(J_1\)
summand in an arbitrary Jordan decomposition.

Finally \(z\notin\bar P\): otherwise \(z^p=1\) because
\(\exp\bar P\mid p\), contrary to \(z^p=AB\ne1\).  Hence

\[
|Q:\bar P|\ge p,
\qquad |G|\ge|Q|\ge p|\bar P|\ge p^{p+3}. \tag{8}
\]

Both submitted order bounds follow without assuming that \(Q=G\).

### 4. Exact literal power image in the action quotient

Let

\[
C=C_Q(\bar P),\qquad U=Q/C.
\]

The centralizer is normal because \(\bar P\unlhd Q\).  For every \(g\in Q\),

\[
(gC)^p=g^pC\in\bar PC/C,
\]

so the literal power image of \(U\) is contained in the image of \(\bar P\).
Conversely, (3) says that every \(h\in\bar P\) is \(g^p\) for some \(g\in Q\),
and hence \(hC=(gC)^p\).  Therefore, as literal sets,

\[
\{u^p:u\in U\}=\bar PC/C
 \cong\bar P/(\bar P\cap C)
 =\bar P/Z(\bar P)
 \cong\operatorname{Inn}(\bar P). \tag{9}
\]

Since \(\bar P\) has class two, the subgroup in (9) is abelian.  It is
nontrivial because \(\bar P\) is nonabelian, so \(U\) itself still has
exponent exactly \(p^2\).  Also \(C\) contains the nontrivial central subgroup
\(\bar P'\), so \(U\) is strictly smaller than \(Q\).  Thus the closure
hypothesis really descends, but the action quotient kills, in particular, the
derived subgroup that the target seeks to control.

### 5. The sharp local model and its exponent

Let \(L_0\) have basis

\[
e_0,e_1,\ldots,e_p,q
\]

and sole nonzero basis bracket \([e_0,q]=e_p\).  Define

\[
De_i=e_{i+1}\ (i<p),\qquad De_p=Dq=0,
\qquad T=I+D.
\]

The bracket depends only on the \(e_0\)- and \(q\)-coordinates, which are
unchanged by \(T\), while \(T(e_p)=e_p\).  Thus \(T\) is a Lie automorphism.
Also

\[
D^p=\operatorname{ad}^{R}_{q},
\qquad T^p=I+D^p=c_q.
\]

Let \(P_0\) be the corresponding class-two exponent-\(p\) Baer group.  Form
\(S=P_0\rtimes\langle t\rangle\), where \(|t|=p^2\) and right conjugation by
\(t\) is \(T\).  This is legitimate because \(T^p=c_q\ne I\) and
\(T^{p^2}=I\), so \(T\) has order \(p^2\).

The element

\[
s=t^pq^{-1}
\]

centralizes \(P_0\), and it commutes with \(t\) because \(Tq=q\).  It is a
nontrivial central element of order \(p\), and
\(\langle s\rangle\cap P_0=1\).  Hence \(P_0\) embeds in

\[
E=S/\langle s\rangle.
\]

If \(z\) is the image of \(t\), then \(z^p=q\ne1\), while
\(E/P_0\cong C_p\).  Every \(g\in E\) therefore has \(g^p\in P_0\), whence
\(g^{p^2}=1\); the element \(z\) has order \(p^2\).  Thus

\[
\exp E=p^2. \tag{10}
\]

Finally set

\[
a=e_0,
\qquad b=q-e_0-\tfrac12e_p.
\]

The class-two BCH law gives

\[
a*b=a+b+\tfrac12[a,b]=q,
\qquad [a,b]=e_p\ne0.
\]

So \(z^p=a*b\) realizes the submitted nonzero local transgression in the
minimal dimension \(p+2\).

### 6. The sharp model is definitely not an accidental target witness

The claimant only warned that saturation was not shown.  One can say more.
Every element of \(E\) has the form \(z^kx\), with
\(0\le k<p\) and \(x=\exp(v)\in P_0\).  If \(k=0\), its \(p\)-th power is
trivial.  If \(k\ne0\), collection gives

\[
(z^kx)^p=q^k\prod_{j=0}^{p-1}T^{jk}(x), \tag{11}
\]

up to reversing the displayed orbit order; the orbit factors commute.  Indeed,
every \(T^{jk}v\) has the same \(e_0\)- and \(q\)-coordinates as \(v\), and
those are the only coordinates seen by the bracket.  Their pairwise brackets
are therefore zero.  Their total \(e_0\)-coordinate is \(pv_0=0\), so the
orbit product also commutes with \(q^k\).

Put

\[
N_k=\sum_{j=0}^{p-1}T^{jk}.
\]

Since \(D^{p+1}=0\), the coefficient of \(D^r\) in \(N_k\) is
\(\sum_j\binom{jk}{r}\).  For \(0\le r\le p-2\), this is the sum over
\(\mathbb F_p\) of a polynomial in \(j\) of degree at most \(p-2\), hence is
zero.  Consequently

\[
N_kL_0\subseteq D^{p-1}L_0+D^pL_0
 =\langle e_{p-1},e_p\rangle. \tag{12}
\]

Equations (11)--(12) show that the logarithm of every actual \(p\)-th power
in \(E\) lies in

\[
W=\langle q,e_{p-1},e_p\rangle.
\]

This is an abelian Lie subalgebra.  Hence all actual \(p\)-th-power values in
\(E\) commute pairwise.  In particular, the noncommuting displayed factors
\(a=e_0\) and \(b=q-e_0-\tfrac12e_p\) are not actual power values.  The model
is therefore not a nonabelian target witness even if its literal value set
were to be a subgroup.

## Tool and command record

No mathematical computation, script, web search, or external literature query
was used.  No compute lease was needed.

Availability probe, verbatim:

```text
$ for tool in gap sage python3 magma pdftotext pdftoppm; do command -v "$tool" || true; done
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftotext
/usr/bin/pdftoppm
$ python3 --version
Python 3.12.3
$ gap -q -c 'Print(GAPInfo.Version,"\n"); QUIT;'
4.12.1
```

Source extraction, relevant verbatim paragraph from the command output:

```text
$ source _meta/agents/Kourovka/paths.env
$ pdftotext -f 184 -l 184 -layout "$KOUROVKA_PDF" -
21.137. If the p-th powers in a finite p-group form a subgroup, must that subgroup
be powerful? That is, for p ̸= 2, if the p-th powers in a p-group of exponent p2 form a
subgroup, must that subgroup be abelian? For a 2-group of exponent 8, if the squares
form a subgroup, must that subgroup be abelian?                               L. Wilson
```

The same page was rendered with `pdftoppm` and visually inspected; it shows the
exponent as \(p^2\).

State-check result, verbatim:

```text
$ python3 _meta/scripts/kourovka-state-check.py 2>&1 | sed "s|$PWD/||g"
WARNING: Agents/Kourovka/roster/Problem-16.4.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-17.76.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-19.25.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-20.55.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-21.31.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/roster/Problem-21.89.md: legacy roster has no scope_id; migrate on next activation
WARNING: Agents/Kourovka/problems/21.90/claim-checks/21.90-diameter-three-distance-graphs-r2-candidate-001.json: claim check is for an old assignment revision
Kourovka state check: 9 scope(s), 14 roster(s), 9 v2 board row(s), 4 claim check(s), 0 benchmark manifest(s), 0 error(s), 7 warning(s).
```

## Verdict

**Status: `status/conjectured` partial result.**

The quotient-power-image equality, Baer applicability, right-adjoint identity,
Jordan-chain independence, extra fixed vector, both order bounds, action-quotient
literal power-image equality, and sharp extension all survive independent hand
reconstruction.  The sharp extension has exponent exactly \(p^2\), and its
actual power values are pairwise commuting, so it is not an in-scope witness.

The sole correction is notation-sign exactness: with the standard left
adjoint, write \(D^p=-\operatorname{ad}_q\); equivalently and most safely,
write \(D^p(x)=[x,q]\).  The mathematical chain in the submitted note already
uses this correct right-adjoint equation.

The certification tag remains `status/conjectured` because this is a strict
necessary-condition/local-sharpness partial, the active universal conclusion is
not proved, and the human certification gate for the partial theorem has not
been recorded.

## Why this verdict

Every fragile passage has an explicit hand proof above.  In particular, (3)
prevents replacing the literal image by a generated subgroup; (4) fixes the
conjugation sign; (6) proves rather than assumes the full chain; (8) proves the
ambient index; (9) proves both inclusions for the quotient's literal value set;
and (10)--(12) prove both exact exponent and non-witness status for the model.
No necessary condition is promoted to a sufficient one, and no constructed
local model is confused with the source target.

## What is NOT established

- The unrestricted revision-2 assertion that every qualifying \(P\) is
  abelian remains open.
- No admissible counterexample is produced.
- Closure supplies no coherent section relating roots of \(A\), \(B\), and
  \(AB\); the checked equation concerns one chosen product root.
- In an arbitrary counterexample, the independent fixed vector \(q\) need not
  span a separate \(J_1\) Jordan summand; only the dimension bound is proved.
- The calculation does not decide whether the sharp extension's literal
  power-value set is closed.  It proves the stronger fact relevant to witness
  exclusion: all those values commute.
- The general powerfulness clause and the exponent-eight two-group clause are
  untouched.

## What would upgrade it

After the human has seen this checked hand proof, the **partial lemma only** may
be eligible for a higher certification tag.  Closing the active assignment
still requires either a universal proof using genuinely global compatibility
among all root fibres, or a reconstructible finite odd-prime exponent-
\(p^2\) group whose complete actual power-value set is a nonabelian subgroup.
