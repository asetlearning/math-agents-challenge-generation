---
title: "SRG(210,76,26,28) constituent gate"
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: BLOCKER
active_assignment_answered: no
---

# Exact outcome

No explicit `srg(210,76,26,28)` constituent could be named from the maintained
workspace, installed graph tools, or current authoritative catalogue.  The
implementation route therefore stops before any coclique computation.

Brouwer's current strongly-regular-graph parameter table marks
`(210,76,26,28)` with `?`, whose table legend means that no graph is known; it
records the expected spectrum `76^1,6^114,(-8)^95` but gives no construction or
data file:
<https://aeb.win.tue.nl/graphs/srg/srgtab201-250.html>.

The closest primary-source object found is M. Gashi, “On the Symmetric Block
Design with Parameters (210,77,28) Admitting a Frobenius Group of Order 57,”
*European Journal of Pure and Applied Mathematics* 13 (2020), 608--619,
DOI `10.29020/nybg.ejpam.v13i3.3769`.  Its abstract explicitly calls the design
*putative*.  The paper derives six possible orbit structures under an assumed
Frobenius group of order 57; it does not give a completed block list or incidence
matrix.  Its final Remark 1 explicitly says that indexing those six orbit
structures to produce an example remains open.  Thus those orbit structures are
not graph constructions.

## Exact conditional vertex/adjacency model

The catalogue/design gap is not merely a naming issue.  If `B` were the
adjacency matrix of the required graph, then

\[
 B^2=76I+26B+28(J-I-B)=48I-2B+28J.
\]

Consequently `D=I+B` would be a symmetric zero-one matrix with row sum 77 and

\[
 DD^{\mathsf T}=D^2=49I+28J. \tag{1}
\]

It is therefore the incidence matrix of a symmetric `2-(210,77,28)` design,
under an identification of its 210 blocks with its 210 points for which `D` is
symmetric and every diagonal entry is one.  In geometric language, this is a
polarity model with every point incident with its identified polar block.

Conversely, any such matrix `D` gives `B=D-I`, and (1) gives

\[
 B^2=48I-2B+28J.

\]

Hence the conditional graph model is:

- vertices are the 210 points of that self-dual symmetric design;
- for distinct points `x,y`, put `x~y` iff point `x` is incident with the block
  identified with `y`.

The matrix identity then verifies exactly 210 vertices, valency `77-1=76`, 26
common neighbours for adjacent pairs (the design intersection 28 with the two
diagonal incidences removed), and 28 for nonadjacent pairs.  This is an exact
equivalence, but no incidence matrix satisfying it is known or locally present,
so it is not an existence verification.

## Frozen downstream gate, not run

If an explicit `B` is later supplied, the complete finite row domain is the set
of all 20-cocliques of `B`; Hoffman's bound is exactly
`210*8/(76+8)=20`.  A fission must choose a symmetric diagonal-one matrix
`M=I+A_1` whose rows lie in that domain and satisfy

\[
 M(B+8I)=8J,\qquad M^2=6I+13M+J-B. \tag{2}

\]

Equivalently, distinct row supports meet in 14, 1, or 0 points according as the
vertex pair lies in `A_1`, `A_2`, or `B`.  No 20-coclique enumeration, orbit
indexing, or matrix search was started, and no compute lease was requested.

## Precise blocker and scope

The missing prerequisite is canonical adjacency data (or a proved construction)
for even one `srg(210,76,26,28)`.  The known `srg(210,114,63,60)` distance-2
parameter set has constructions, but it cannot substitute for the missing
distance-3 constituent in (2).  Possible orbit structures for a putative design
also cannot substitute for an incidence matrix.

This catalogue gap does not prove that the SRG, the intersection array, or a
target graph is nonexistent.  Even a future negative result for one explicit
constituent would not cover nonisomorphic constituents.  The bounded row does
not answer the revision-3 existential problem.  `active_assignment_answered: no`.
