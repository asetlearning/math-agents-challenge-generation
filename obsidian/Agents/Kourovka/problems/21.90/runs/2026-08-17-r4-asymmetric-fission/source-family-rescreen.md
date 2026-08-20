---
title: "Bounded source-family feasibility rescreen after the handshake gate"
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: CHECKPOINT
active_assignment_answered: no
---

# Source-family feasibility rescreen

## Exact master parameterization

For the primitive non-Taylor branch in the Belousov--Makhnev--Nirova parameterization, put `a=a_3`.  The intersection array is

\[
 \{t(c+1)+a,\;tc,\;a+1;\;1,c,t(c+1)\}. \tag{1}
\]

Thus `k=t(c+1)+a`, `a_1=a+t-1`, `a_2=(t-1)(c+1)`, `k_2=kt`, and
`k_3=k(a+1)/(c+1)`.  The Q-polynomial equation quoted by the source is

\[
 (t^2-a-1)c=a^2-t^2+2a+1,
\]

equivalently

\[
 (t^2-a-1)(c+1)=a(a+1). \tag{2}
\]

This is exactly why the old enumerator loops over `(t,a)`, requires positive
`d=t^2-a-1` dividing `a(a+1)`, and sets `c=a(a+1)/d-1`.

The bridge to the four explicit Type-I/II families in Makhnev--Belousov's 2022
conference abstract is obtained by comparison with (1):

| source family | substitution into `(t,c,a)` | square condition consistent with the master equation |
|---|---|---|
| (Ii) | `t=su`, `c=m-1`, `a=ms^2-m` | `u^2=ms^2-m+1` |
| (Iii) | `t=u(w+1)`, `c=x(w+1)`, `a=w(c+1)=w(xw+x+1)` | `u^2=xw+1` |
| (IIi) | `t=su`, `c=m-1`, `a=ms^2-1` | `u^2=ms^2+m-1` |
| (IIii) | `t=uw`, `c=xw`, `a=w(c+1)-1=xw^2+w-1` | `u^2=x(w+1)+1` |

There are two typographical inconsistencies in the short 2022 conference
abstract as printed: its (IIi) line prints `u^2=ms^2-m-1`, whereas substitution
of its own array into (2), or the detailed 2019 Type-II factorization, gives
`u^2=ms^2+m-1`; its (IIii) line prints `b_2=xw+w`, whereas comparison with its
first entry and (1) gives `b_2=xw^2+w`.  The corrected expressions in the table
are forced algebraically, not silent OCR guesses.  With these corrections each
substitution reproduces all six entries of (1) and satisfies (2).  The detailed
Type-II formulas are independently displayed in Makhnev--Golubyatnikov,
*Nonexistence of some Q-polynomial distance-regular graphs* (2019),
<https://journal.imm.uran.ru/sites/default/files/content/25_4/TrIMMUrORAN_2019_4_p136_L.pdf>:
case (i) has `w=s^2`, `t=su`, and
`c=(u^2-s^2)/(s^2+1)`; case (ii) has `c=xw`, `t=uw`, and
`u^2=x(w+1)+1`.  These simplify to the two corrected Type-II rows above.

The same 2022 abstract leaves Type III as the fifth case, without one of these
four factor parameterizations.  Hence the bounded `(t,a)` loop covers every integral
tuple satisfying the *master* non-Taylor equations in its box, including Type
III, but this is not a completeness theorem for graphs, does not cover the
Taylor branch, and is not an unbounded catalogue.  Source checked: Makhnev and
Belousov, XIV Group Theory School-Conference abstracts (2022), p. 83,
<https://group.imm.uran.ru/conf-group/group/%D0%A1%D0%B1%D0%BE%D1%80%D0%BD%D0%B8%D0%BA%20%D1%82%D0%B5%D0%B7%D0%B8%D1%81%D0%BE%D0%B2%20XIV%20%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9%20%D1%88%D0%BA%D0%BE%D0%BB%D1%8B-%D0%BA%D0%BE%D0%BD%D1%84%D0%B5%D1%80%D0%B5%D0%BD%D1%86%D0%B8%D0%B8%20%D0%BF%D0%BE%20%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D0%B8%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF.pdf>.

## Corrected bounded screen

The exact GAP script `scratch/rescreen_parameter_candidates.g` keeps the old
bounds `1<=t<=100`, `1<=a<=1000` and applies, in order:

1. integral nonnegative intersection data and integral sphere sizes
   `k_i=(1,k,kb_1/c,kb_1b_2/(cc_3))`;
2. all four handshake conditions `k_i a_i` even (`i=0,1,2,3`);
3. four rational integral eigenvalues and positive integral multiplicities;
4. nonnegative integral intersection numbers of the putative 3-class scheme;
5. all Krein parameters nonnegative and an irreducible tridiagonal
   `B_1^*` in one of the six nonprincipal eigenspace orders;
6. the same absolute product/support bounds as the old screen.

The completed run took about ten seconds and gave:

```text
raw_parameter_count=1475
sphere_integral_count=1475
all_layer_handshakes_count=1284
integral_spectral_multiplicity_count=1284
scheme_feasible_count=483
scheme_and_all_Krein_nonnegative_count=483
absolute_bound_feasible_count=482
qpolynomial_and_absolute_count=482
```

The smallest final survivor by vertex number is

\[
 \boxed{\{19,12,5;1,4,15\}},\qquad v=96,
\]

coming from `(t,a,c)=(3,4,4)`.  Its sphere sizes are `(1,19,57,19)`,
`(a_1,a_2,a_3)=(6,10,4)`, adjacency eigenvalues `(19,-5,-1,7)` with
multiplicities `(1,19,57,19)`, and Q-order `[1,4,3,2]`.  “Survivor” here means
only survivor of the stated bounded arithmetic gates; earlier literature cited
in the problem log reports this array nonexistent, and this run neither
reproves nor assumes that result in counting the 482 rows.

## Why the 300-vertex array passed the old screen

For `{39,25,10;1,5,30}`, equation (1) gives `(t,a,c)=(5,9,5)`.  Its sphere
sizes `(1,39,195,65)` are integral, its eigenvalues and multiplicities are
integral, and it passed the old scheme, Krein/Q-order, and absolute-bound tests.
The old script simply never tested `k_i a_i` parity.  Here

\[
 k_1a_1=39(9+5-1)=39\cdot13=507
\]

is odd (and also `k_3a_3=65*9=585` is odd), so the corrected screen rejects it
before spectral work.  No constituent of this array is reopened.

## Frozen next observable for the 96-vertex survivor

Let `X=A_1` and `B=A_3`.  The array forces `B` to have parameters
`srg(96,19,2,4)` and forces

\[
 X^2=15I+2X+4J-4B,\qquad XB=5J-5I-5X-B. \tag{3}
\]

Equivalently, for `M=I+X`,

\[
 M(B+5I)=5J,\qquad M^2=12I+4M+4J-4B. \tag{4}
\]

Thus every row support of `M` is a 20-coclique in `B`, attaining the Hoffman
bound `96*5/(19+5)=20`.  A concrete bounded construction/nonexistence observable
is therefore: for an explicit `srg(96,19,2,4)`, enumerate its 20-cocliques; the
row domain being empty certifies nonexistence over that constituent, while any
construction must select 96 of them into a symmetric diagonal-one matrix
satisfying (4).  This freezes an exact next experiment without claiming that a
catalogue of all such constituents is available or complete.

## Scope

This rescreen is a bounded necessary-condition calculation for the non-Taylor
master family.  It does not establish uniqueness of the smallest row, does not
turn a literature citation into a new nonexistence proof, and does not answer
the full existential Problem 21.90.  `active_assignment_answered: no`.
