---
title: "Verification — Kourovka 21.90 — Type-II(ii) handshake and even residual"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 3
claim: "In the primitive non-Taylor Type-I/II parameter families, every local handshake is equivalent to ta even, excluding an explicit infinite odd-x,w Type-II(ii) formal subfamily, while the even-xw Type-II(ii) residual survives the stated spectral and zero-Krein parity gates."
claimant: Problem-21.90
target_statement: "Does there exist a Q-polynomial distance-regular graph Gamma of diameter 3 such that Gamma_2 and Gamma_3 are nontrivial strongly regular graphs under the revision-3 source-operational convention?"
excluded_scopes: ["the superseded revision-2 disconnected cube candidate and other degenerate imprimitive distance graphs"]
target_object: "An actual Q-polynomial distance-regular graph satisfying every revision-3 constraint"
witness_object: "Formal primitive non-Taylor parameter arrays, principally the Type-II(ii) specialization"
witness_equals_target: false
citation: "none; source-family labels are audited conditionally from the formulas supplied in the linked local notes"
verification_method: "independent hand derivation plus a bounded exact-integer/Fraction sanity checker"
tools_used: ["Python 3.12.3", "pdftotext 24.02.0", "rendered PDF visual inspection"]
scope_answered: ["conditional odd-x,w Type-II(ii) formal-parameter subfamily exclusion"]
scope_not_answered: ["21.90/diameter-three-distance-graphs", "even-xw Type-II(ii) realizability", "Type III", "Taylor branch"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.90 — Type-II(ii) handshake and even residual

## The claim

There are two distinct claims to judge.

1. **Candidate infinite partial.**  Conditional on the displayed primitive
   non-Taylor master parameterization and its Type-II(ii) specialization, the
   degree-sum handshakes exclude every odd-`x,w` tuple; the formula
   `w=7`, `u=8r+3`, `x=8r^2+6r+1` supplies infinitely many such formal tuples.
2. **Even-residual strategy claim.**  When `xw` is even, the displayed
   multiplicities, formal self-duality, zero-Krein support, and three
   triple-intersection equations are correct, and their primitive mod-2 gate is
   automatically satisfied.  This says only that this parity gate excludes no
   even tuple; it does not say that the full nonnegative-integral
   triple-intersection systems are feasible.

## Scope, revision, and clause matrix

The visually rendered Notebook page 177 asks for an actual Q-polynomial
distance-regular graph of diameter 3 whose second and third distance graphs are
strongly regular.  Canonical revision 3 supplies the controlling nontrivial
three-eigenvalue convention.

| source clause | active? | answered by this package? |
|---|---:|---:|
| `Gamma_i` has the same vertices and adjacency exactly at distance `i` | yes | no graph is supplied |
| existence of the required diameter-3 Q-polynomial distance-regular `Gamma` | yes | no |
| nontrivial strong regularity of both `Gamma_2` and `Gamma_3` | yes | no graph is supplied |

The revision-2 cube candidate is superseded.  None of the Type-II(ii) formal
tuples is asserted or proved to be a graph.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted object/evidence | result |
|---|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | one graph satisfies all rows | symbolic tuples only | unknown |
| `21.90-diameter-3` | admissibility | diameter exactly 3 | formal diameter-3 array | unknown for an actual graph |
| `21.90-Q-polynomial-distance-regular` | admissibility | Q-polynomial distance-regular graph | formal eigen/intersection data | unknown for an actual graph |
| `21.90-distance-graph-definition` | admissibility | exact distance relations | used conditionally in the scheme algebra | no candidate graph to test |
| `21.90-Gamma2-strongly-regular` | admissibility | nontrivial SRG | source-family reduction assumes/formalizes it | unknown for an actual graph |
| `21.90-Gamma3-strongly-regular` | admissibility | nontrivial SRG | source-family reduction assumes/formalizes it | unknown for an actual graph |
| `21.90-existence-conclusion` | target conclusion | at least one such graph exists | expressly not claimed | unproved |

There is no revision-3 `claim-checks/*.json`.  The only present claim check is the
superseded revision-2 cube record, with `ready_for_validator:false`.  Thus the
current package also fails the protocol's claim-completeness gate for promotion.

`active_assignment_answered: no`.

## Target versus witness

The source target is an actual graph.  The submitted witness is a family of formal
intersection arrays/eigenmatrices.  A formal parameter tuple is not an existence
witness, and no theorem identifying each tuple with a graph is supplied.

Therefore `witness_equals_target: false`.  The odd-family result is a conditional
parameter exclusion, not a counterexample or solution to the active existential
question.

## Independent reconstruction of the master handshake

Write

\[
 \{b_0,b_1,b_2;c_1,c_2,c_3\}
 =\{t(c+1)+a,tc,a+1;1,c,t(c+1)\},
\]

put `k=t(c+1)+a`, `d=t^2-a-1`, and assume

\[
 d(c+1)=a(a+1). \tag{1}
\]

The sphere sizes and induced `A_1`-degrees follow directly from the intersection
array:

\[
 (k_1,k_2,k_3)=(k,kt,q),\qquad
 q=\frac{k(a+1)}{c+1}=t(a+1)+d,
\]

\[
 (a_1,a_2,a_3)=(a+t-1,(t-1)(c+1),a). \tag{2}
\]

Modulo 2,

\[
 q\equiv t(a+1)+(t^2-a-1)
   \equiv a(t+1)+1,
 \qquad qa\equiv ta. \tag{3}
\]

Hence the layer-3 handshake `qa` even is equivalent to `ta` even.  Conversely,
if `ta` is even, either `t,a` are both even, when `k` is even, or exactly one is
odd, when `a+t-1` is even.  Thus the layer-1 handshake also holds.  The middle
handshake contains the factor `t(t-1)`.

The stronger nine restricted-relation degrees reconstruct as

\[
\begin{array}{c|ccc}
 &A_1&A_2&A_3\\ \hline
\Gamma_1(u)&a+t-1&tc&0\\
\Gamma_2(u)&(t-1)(c+1)&
 t(t-1)(c+1)+c+a+1-t&(t-1)(a+1)\\
\Gamma_3(u)&a&ta&t^2+t-2a-2.
\end{array} \tag{4}
\]

These entries follow from the distance-matrix recurrence and row sums.  Their
handshakes are also equivalent to `ta` even:

- row 1, column 1 is the preceding layer-1 condition;
- row 1, column 2 is automatic unless `t,c` are both odd, in which case `ta`
  even makes `a` and hence `k` even;
- row 2, columns 1 and 3 contain `t(t-1)` after multiplication by `k_2=kt`;
- for row 2, column 2, if `t` is even the sphere size is even; if `t` is odd,
  then `a` is even, the displayed degree has parity `c`, and `c` odd makes
  `k=t(c+1)+a` even;
- row 3, column 1 is (3), column 2 contains `ta`, and column 3 has the even
  degree `t(t+1)-2(a+1)`.

Conversely, row 3, column 1 again forces `ta` even.  Finally

\[
v=1+k+kt+q\equiv0\pmod2, \tag{5}
\]

so there is no additional full-distance-graph degree-sum obstruction.

## Independent reconstruction of all four substitutions

Substitution into (1), rather than acceptance of the submitted pass labels, gives:

| family | displayed substitution | resulting `d=t^2-a-1` | handshake conclusion |
|---|---|---|---|
| (Ii) | `t=su`, `c=m-1`, `a=m(s^2-1)`, `u^2=m(s^2-1)+1` | `(s^2-1)(a+1)` | `ta=msu(s^2-1)` is even |
| (Iii) | `t=u(w+1)`, `c=x(w+1)`, `a=w(c+1)`, `u^2=xw+1` | `w(a+1)` | `ta` contains `w(w+1)` |
| (IIi) | `t=su`, `c=m-1`, `a=ms^2-1`, `u^2=ms^2+m-1` | `s^2a` | `ta` is even for every integral square-condition solution |
| (IIii) | `t=uw`, `c=xw`, `a=w(c+1)-1`, `u^2=x(w+1)+1` | `wa` | `ta` is even exactly when `xw` is even |

In every row the displayed value of `d` makes `d(c+1)=a(a+1)` identically.
For (IIi), odd `ta` would force `s,u,a` odd, hence `s` odd and `m` even.  But

\[
u^2=m(s^2+1)-1\equiv3\pmod4,
\]

which is impossible.  For (IIii), if `w` is even both `ta` and `xw` are even;
if `w` is odd then the square equation makes `u` odd and
`a=w(xw+1)-1\equiv x`, so `ta\equiv x\equiv xw` modulo 2.

This validates the substitutions **as algebraic maps into the master equation**.
Because external browsing was prohibited and the cited family papers are not local
evidence in this request, it does not independently authenticate the literature
classification, the family labels, or completeness beyond these displayed maps.

## Type-II(ii): the infinite odd family

For every integer `r>=0`, set

\[
w=7,\qquad u=8r+3,\qquad x=8r^2+6r+1.
\]

All three numbers are positive, `x,w` are odd, distinct `r` give distinct `u`, and

\[
x(w+1)+1=8(8r^2+6r+1)+1=(8r+3)^2=u^2. \tag{6}
\]

Thus this is genuinely infinite at the level claimed.  Here

\[
t=7u,\quad c=7x,\quad h=c+1,\quad a=7h-1=49x+6.
\]

The parameters `t,c,a` are odd, while `h` is even.  Hence
`k=th+a` is odd and `q=k(a+1)/h=7k` is odd.  The induced layer-1 graph would
have odd order `k` and odd degree `a+t-1`; the induced layer-3 graph would have
odd order `q` and odd degree `a`.  Either violates the handshake lemma for a
finite simple graph.

**Candidate infinite-partial verdict:** the exclusion is correct as an infinite
conditional formal-parameter theorem.  It is not a family of graphs and it does
not answer the active scope.

## Type-II(ii): exact even residual

Put

\[
h=xw+1,\quad t=uw,\quad a=wh-1,\quad
k=wh(u+1)-1,
\]

so the square condition is equivalently

\[
(w+1)h=wu^2+1. \tag{7}
\]

The handshake residual `xw` even splits exactly as follows.

- If `x` is even, `u` is odd and
  `nu_2(x)+nu_2(w+1)=nu_2(u^2-1)>=3`.  In particular, if `w` is even then
  `8` divides `x`.
- If `x` is odd, `w` is even, `u` is even, and
  `x(w+1)=u^2-1=3 (mod 4)`.  Thus `x=3 (mod 4)` for `w=0 (mod 4)` and
  `x=1 (mod 4)` for `w=2 (mod 4)`.

Both branches are infinite at the Diophantine level: `w=3`, `u=2r+1`,
`x=r(r+1)` for `r>=1`, and `w=2`, `u=6r+2`,
`x=12r^2+8r+1` for `r>=0`, respectively.

## Multiplicities and formal self-duality

The four `A_1` eigenvalues reconstruct as

\[
k,\qquad R=w(h+u)-1,\qquad -1,\qquad -h,
\]

and the complete eigenmatrix is

\[
P=\begin{pmatrix}
1&k&kt&kw\\
1&R&-uw&-wh\\
1&-1&-uw&uw\\
1&-h&wu^2&-wh
\end{pmatrix}. \tag{8}
\]

Using (7), one gets `k+h=uw(h+u)=t(h+u)`.  Therefore

\[
m_{-1}=\frac{k(k+h)}{h+u}=kt,
\qquad
m_{-h}=\frac{t(kt+kw)}{wu(u+1)}=kw,
\]

and subtraction from `v=1+k+kt+kw` gives `m_R=k`.  Thus

\[
(m_0,m_R,m_{-1},m_{-h})=(1,k,kt,kw). \tag{9}
\]

Independent multiplication of (8), using only (7), gives `P^2=vI`.
Equivalently, (8) is weighted symmetric:

\[
k_iP_{ij}=k_jP_{ji},\qquad (k_0,k_1,k_2,k_3)=(1,k,kt,kw),
\]

and (9) identifies multiplicities with valencies.  Hence `Q=P` in this indexing.
The formal scheme is self-dual; this is a formal-feasibility fact, not an existence
proof.

## Zero-Krein support

Since `P=Q`, the Krein parameters equal the ordinary intersection numbers under
the displayed index identification.  Independent distance-polynomial products give

\[
\begin{aligned}
(q_{11}^{\ell})_{\ell=0}^3&=(k,a+t-1,c,0),\\
(q_{12}^{\ell})_{\ell=0}^3&=(0,tc,(t-1)h,th),\\
(q_{13}^{\ell})_{\ell=0}^3&=(0,0,a+1,a),\\
(q_{22}^{\ell})_{\ell=0}^3&=(kt,t(t-1)h,t(t-1)h+wu^2-t,t(t-1)h),\\
(q_{23}^{\ell})_{\ell=0}^3&=(0,twh,wh(t-1),ta),\\
(q_{33}^{\ell})_{\ell=0}^3&=(kw,wa,wa,w(a+u-h)).
\end{aligned} \tag{10}
\]

For positive Type-II(ii) parameters, `u>=2`.  Every entry in (10) not displayed
as zero is positive: in particular

\[
t(t-1)h+wu^2-t=t(t-1)h+wu(u-1)>0,
\]

and `a+u-h=(w-1)h+u-1>0`.  Apart from universal zeros involving index 0,
the complete zero support is therefore the single multiset

\[
\{1,1,3\}:\qquad q_{11}^3=q_{13}^1=q_{31}^1=0. \tag{11}
\]

## Triple-intersection equations and parity

For a fixed ordered base triple `(X,Y,Z)`, let
`W=d(X,Y)`, `V=d(X,Z)`, `U=d(Y,Z)` and define `[rst]` in the standard way.
The marginal equations are

\[
\sum_r[rst]=p_{st}^{U},\qquad
\sum_s[rst]=p_{rt}^{V},\qquad
\sum_t[rst]=p_{rs}^{W}. \tag{12}
\]

Column 1 of `Q=P` is

\[
L=(k,R,-1,-h),
\]

and column 3 is `wG`, where

\[
G=(k,-h,u,-h).
\]

Applying the standard zero-Krein identity to the three placements in (11), and
dividing out the common factor `w`, gives exactly

\[
\sum_{r,s,t}L_rL_sG_t[rst]=0,
\quad
\sum_{r,s,t}L_rG_sL_t[rst]=0,
\quad
\sum_{r,s,t}G_rL_sL_t[rst]=0. \tag{13}
\]

Zeros involving idempotent index 0 collapse, via (12), to the ordinary pairwise
orthogonality identities and add no triple-variable row.  Thus (13) is the complete
nontrivial zero-Krein contribution, in addition to the marginals, forced base-point
entries, triangle-support zeros, nonnegativity, and integrality.

Now `xw` even makes `c` even and `h` odd.  Every entry of `L` is odd.

- If `u` is odd, every entry of `G` is odd, so each equation (13) modulo 2 is
  `v=0 (mod 2)`.
- If `u` is even, the square equation forces `x` odd and `w` even; only `G_2=u`
  is even.  Each equation modulo 2 is then `v-k_2=v-kt=0 (mod 2)`.

Both congruences hold identically.  Indeed `k` is odd and
`v=1+k(1+t+w)` is even in both branches; in the second branch `t=uw` is even,
so `kt` is even as well.

**Even-residual strategy verdict:** the primitive mod-2 gate is correctly
exhausted and excludes no even-`xw` tuple.  This does **not** establish that any
fixed-base system (12)--(13) has a nonnegative integral solution.  Consequently,
“no even subfamily is excluded” is valid only with the qualifier “by this parity
gate”; it is not established for the full triple-intersection feasibility problem.

## Subclaims and what each method proves

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| master and nine handshakes | hand recurrence/parity derivation | exact equivalence inside the master array | that every target graph is covered by this branch |
| four substitutions | direct substitution into (1) | internal algebraic consistency and parity | literature provenance or classification completeness |
| odd infinite family | direct polynomial identity and handshake lemma | infinite formal-parameter exclusion | existence/nonexistence outside that subfamily |
| even multiplicities and `P=Q` | exact eigenmatrix identities | formal spectral self-duality | realization by an association scheme or graph |
| zero support and (13) | distance-polynomial products and zero-Krein theorem | exact necessary equations | feasibility of all integer/nonnegative systems |
| parity reduction | coefficient reduction modulo 2 | this one congruence never contradicts an even tuple | absence of stronger integral or nonnegative obstructions |
| witness is target | object audit | fails: a tuple is not a graph | any active-scope conclusion |

## Evidence

Triage note:
`Agents/Kourovka/problems/21.90/verification/2026-08-17T125738Z-Type-IIii-package-triage.md`.

Independent bounded checker:
`Agents/Kourovka/problems/21.90/verification/scratch/check_typeii_package.py`.
It solves the four eigenvalue-product equations over exact `Fraction`s rather than
copying the submitted intersection products.  The universal statements above are
the hand derivations; the checker is a transcription/sign sanity check only.

Relevant command and output, verbatim:

```text
$ source _meta/agents/Kourovka/paths.env
$ printf '%s\n' '--- tool probe ---'
$ command -v gap || true
$ command -v sage || true
$ command -v python3 || true
$ command -v magma || true
$ dpkg-query -W -f='${Package} ${Version}\n' gap-core 2>/dev/null || true
$ python3 --version
$ pdftotext -v 2>&1 | sed -n '1p'
--- tool probe ---
/usr/bin/gap
/usr/bin/python3
gap-core 4.12.1-2build2
Python 3.12.3
pdftotext version 24.02.0
```

No GAP call was made; under the common protocol every GAP call would require a
heavy-compute lease and none was needed.

```text
$ pdftotext -f 177 -l 177 -layout "$KOUROVKA_PDF" - | sed -n '/21\.90\./,/21\.91\./p' | sed '$d'
21.90. Let Γ be a graph of diameter d. For i ∈ {1, 2, . . . , d}, let Γi be the graph on
the same vertex set as Γ with vertices u, w adjacent in Γi if and only if dΓ (u, w) = i.
Does there exist a Q-polynomial distance-regular graph Γ of diameter 3 such that Γ2
and Γ3 are strongly regular?                                              A. A. Makhnëv

```

The same statement was visually checked on the rendered page image at
`Agents/Kourovka/problems/21.90/scratch/source-page-177.png`.

```text
$ find Agents/Kourovka/problems/21.90/claim-checks -maxdepth 1 -type f -name '*r3*' -printf '%f\n' | sort
```

The output is empty.

```text
$ python3 Agents/Kourovka/problems/21.90/verification/scratch/check_typeii_package.py
representative even-xw solutions: [(2, 3, 3), (8, 2, 5), (1, 2, 2), (21, 2, 8)]
  (x,w,u)=(2,3,3): P^2=vI; multiplicities=(1,83,747,249); nonzero-index zeros=[(1, 1, 3), (1, 3, 1)]
  (x,w,u)=(8,2,5): P^2=vI; multiplicities=(1,203,2030,406); nonzero-index zeros=[(1, 1, 3), (1, 3, 1)]
  (x,w,u)=(1,2,2): P^2=vI; multiplicities=(1,17,68,34); nonzero-index zeros=[(1, 1, 3), (1, 3, 1)]
  (x,w,u)=(21,2,8): P^2=vI; multiplicities=(1,773,12368,1546); nonzero-index zeros=[(1, 1, 3), (1, 3, 1)]
recovered products for (x,w,u)=(2,3,3):
  p_11^h=(83, 28, 6, 0)
  p_12^h=(0, 54, 56, 63)
  p_13^h=(0, 0, 21, 20)
  p_22^h=(747, 504, 522, 504)
  p_23^h=(0, 189, 168, 180)
  p_33^h=(249, 60, 60, 48)
odd family r=0..10: square equation and oddness pass
bounded parity/P sanity screen: 169 solutions, zero failures
```

## Verdict

**Status: `status/conjectured`, with both requested mathematical judgments made.**

- **Infinite partial:** valid as a conditional formal-parameter theorem.  Every
  displayed source-family handshake reduces as claimed, and the explicit odd
  Type-II(ii) family is infinite and impossible for a graph by two degree-sum
  contradictions.
- **Even residual:** the multiplicities, `P=Q`, zero-Krein support, three equations,
  and mod-2 reduction are correct.  The parity-only strategy is exhausted and
  excludes no even tuple.
- **Active scope:** not answered.

No higher ladder status is assigned because the revision-3 claim-check is missing,
the source-family provenance/completeness was not independently authenticated under
the no-browse instruction, and the submitted objects are not target graphs.

## Why this verdict

Every algebraic identity requested by Lead survives independent reconstruction.
The odd-family conclusion is a genuine necessary-condition exclusion.  The even
calculation is also correct but is a passed necessary-condition gate, not a
feasibility proof.  The object audit prevents either statement from being inflated
into an answer to Kourovka 21.90.

## What is NOT established

- No graph in the active scope is constructed.
- No universal nonexistence theorem for the active scope is proved.
- It is not independently established here that the four displayed substitutions
  exhaust the relevant literature families or are transcribed from those sources;
  only their internal substitution algebra is checked.
- Type III and the Taylor branch are untouched.
- No even-`xw` Type-II(ii) graph or association scheme is shown to exist.
- No fixed base-distance triple-intersection system is eliminated or solved over
  the nonnegative integers.
- Satisfying the parity consequence of (13) is not sufficient for satisfying
  (12)--(13).

## What would upgrade it

For the conditional partial, supply a clean revision-3 claim-check and a locally
auditable source transcription/theorem establishing the exact family
parameterization and its stated coverage.  For progress on the active target,
either construct and independently certify an actual graph satisfying every row,
or prove nonexistence across all branches.  For the even residual specifically,
eliminate the finitely many base-distance systems (12)--(13) symbolically or give
auditable nonnegative-integral certificates for the claimed range; parity alone
cannot decide them.
