---
title: "Reconciliation of the 482 bounded survivors with recorded exclusions"
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: CHECKPOINT
active_assignment_answered: no
---

# Sorted-survivor reconciliation

The corrected non-Taylor arithmetic screen has 482 final rows in the inherited
box `1<=t<=100`, `1<=a_3<=1000`.  Sorting by vertex number, rather than by the
enumerator's loop order `(t,a_3)`, gives the following initial segment.  Status
uses only exclusions already written in the maintained log or reviewed notes.

| order `v` | intersection array | recorded status |
|---:|---|---|
| 96 | `{19,12,5;1,4,15}` | literature/table citation only (Coolsaet--Jurišić) |
| 120 | `{17,8,6;1,2,12}` | literature/table citation only (BCN theorem) |
| **210** | **`{19,6,8;1,1,12}`** | **no recorded exclusion; first live row** |
| 216 | `{35,24,8;1,6,28}` | literature/table citation only (Jurišić--Vidali) |
| 392 | `{69,56,10;1,14,60}` | literature-only 2019 nonexistence citation |
| 540 | `{77,60,13;1,12,65}` | no recorded exclusion |
| 630 | `{74,54,15;1,9,60}` | literature-only 2019 nonexistence citation |
| 672 | `{55,32,16;1,4,40}` | no recorded exclusion |
| 726 | `{87,66,16;1,11,72}` | no recorded exclusion |
| 800 | `{119,100,15;1,20,105}` | literature-only 2019 nonexistence citation |

This accounts for every already-recorded exclusion that remains among the 482
rows.  In particular, the maintained 2019 paper title names all three rows of
orders 392, 630, and 800; the older prose's phrase “first and third” did not
justify leaving the order-630 row live.  None of these literature-only entries
is promoted here to an in-house proof.

Three other recorded exclusions do not occur among the 482:

| order `v` | intersection array | why absent / proof provenance |
|---:|---|---|
| 50 | `{14,10,3;1,5,12}` | fails the absolute bound `43>28`; in-house exact proof accepted by Validator |
| 162 | `{35,27,6;1,9,30}` | now already fails the local handshake (`35*7` odd); independently, the in-house closed-neighborhood lift plus published `srg(324,57,0,12)` nonexistence was accepted by Validator |
| 300 | `{39,25,10;1,5,30}` | fails two handshakes (`39*13` and `65*9` odd); in-house proof, with the current validation request still pending |

The older polar-fission records for the order-300 row have narrower scope and
are not used as an array exclusion: Validator left the vertex-transitive
subgroup-orbital claim conjectured, and the newer exact 40-coclique computation
for one standard constituent is also awaiting review.  The elementary
array-level handshake proof, if upheld, makes both constituent-level routes
redundant without strengthening their historical certificates.

The older claim that the order-300 row was the smallest unresolved row arose
from reading output ordered by `(t,a_3)` and from the missing handshake gate.
After actual sorting and reconciliation, the first row not already excluded is
the order-210 row above.  This statement is relative only to the finite screen
and maintained exclusions; it is not a literature-completeness claim.

**Superseding update (2026-08-17):** the order-210 row is now eliminated by the
constituent-independent local clique-partition contradiction in
`srg210-integral-obstruction.md`, pending Validator review. The table above is
retained as the exact state at the time of the reconciliation decision; it must
not be used to call that row live after this update.

## Frozen first live row

For

\[
  \{19,6,8;1,1,12\},
\]

the layer sizes are `(1,19,114,76)`, so `v=210`, and
`(a_1,a_2,a_3)=(12,10,7)`.  The adjacency spectrum is

\[
  19^1,\quad (-2)^{76},\quad (-1)^{114},\quad 13^{19}.
\]

The two required distance constituents have exact parameters and spectra

\[
 \Gamma_2:\ \operatorname{srg}(210,114,63,60),\qquad
 \operatorname{Spec}(A_2)=\{114^1,9^{76},(-6)^{133}\},
\]

\[
 \Gamma_3:\ \operatorname{srg}(210,76,26,28),\qquad
 \operatorname{Spec}(A_3)=\{76^1,6^{114},(-8)^{95}\}.
\]

Both are connected, noncomplete, three-eigenvalue graphs, so their parameter
sets pass the revision-3 source-operational strong-regularity convention.

## Finite observable, frozen but not run

Put `X=A_1`, `B=A_3`, and `M=I+X`.  The intersection array forces

\[
 X^2=18I+11X+J-B,\qquad XB=8J-8I-8X-B,
\]

and hence

\[
 M(B+8I)=8J,\qquad M^2=6I+13M+J-B. \tag{*}
\]

Thus every row support of `M` is a 20-coclique in
`B=srg(210,76,26,28)`.  This attains Hoffman's bound
`210*8/(76+8)=20`.  Moreover, two row supports meet in 14, 1, or 0 points
according as their vertices are related by `X`, `A_2`, or `B`.

The frozen finite construction/nonexistence observable is therefore: for one
explicit `srg(210,76,26,28)` constituent, enumerate its Hoffman-bound
20-cocliques.  An empty domain excludes that constituent; otherwise test whether
210 of them form a symmetric diagonal-one matrix satisfying `(*)`.  No such
enumeration was started in this increment.  Failure for one constituent would
not cover nonisomorphic constituents, and success would still require the full
admissibility certificate.

## Scope limits

This note neither promotes the two source-family typo corrections before
independent review nor relies on them.  It does not claim the finite box covers
the full source problem, and it does not answer Problem 21.90.
`active_assignment_answered: no`.
