---
title: "Kourovka 21.90 revision 2 — literal-definition cube candidate"
author: operator
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 2
outcome_candidate: OUT_OF_SCOPE_EXAMPLE
claim_kind: proof
review_status: withdrawn-after-source-context-check
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/finite-graphs, status/conjectured]
---

# Candidate witness

> Superseded by canonical revision 3 after the human supplied the MathNet source
> paper. The argument below is correct only for the literal permissive definition;
> `2K4` and `4K2` have fewer than three distinct eigenvalues and fail the
> source-operational nontrivial convention. This artifact is preserved as an audit
> trail and is not ready for validation as an answer to the current scope.

Use the displayed definition supplied by the human at
<https://en.wikipedia.org/wiki/Strongly_regular_graph>: a graph is strongly regular
when it is regular and adjacent and nonadjacent vertex pairs have constant numbers
of common neighbours. Revision 2 permits the disconnected/imprimitive cases that
the same page calls trivial and says are conventionally omitted from detailed
lists.

Let \(\Gamma=H(3,2)\), the graph on \(\mathbf F_2^3\) in which two binary triples
are adjacent exactly when they differ in one coordinate.

## Distance regularity and the Q-polynomial property

The distance is Hamming distance, so the diameter is exactly three. Relative to
vertices at distance \(i\), exactly \(i\) one-coordinate moves decrease the
distance and exactly \(3-i\) increase it. Hence \(\Gamma\) is distance regular
with intersection array

\[
  \{3,2,1;1,2,3\}.
\]

For a self-contained Q-polynomial certificate, index the characters of
\(\mathbf F_2^3\) by \(y\in\mathbf F_2^3\),
\(\chi_y(x)=(-1)^{x\cdot y}\), and group the primitive idempotents by the Hamming
weight \(j=\operatorname{wt}(y)\). Entrywise multiplication by the weight-one
idempotent sends the weight-\(j\) character space only to weights \(j-1\) and
\(j+1\): multiplying \(\chi_y\) by a weight-one character replaces \(y\) by a
vector at weight \(j-1\) or \(j+1\). Both transition coefficients are positive
when the corresponding level exists. Thus the Krein matrix for the ordering
\(E_0,E_1,E_2,E_3\) is irreducible tridiagonal, which is the Q-polynomial
condition.

## The two distance graphs

Parity is preserved by distance two. Each parity class has four vertices, and any
two distinct triples of the same parity differ in exactly two coordinates.
Therefore

\[
  \Gamma_2=2K_4=\operatorname{srg}(8,3,2,0).
\]

Every triple has exactly one vertex at distance three, its bitwise complement.
Therefore

\[
  \Gamma_3=4K_2=\operatorname{srg}(8,1,0,0).
\]

For \(2K_4\), adjacent pairs have two common neighbours and nonadjacent pairs have
none. For \(4K_2\), every pair has zero common neighbours, with degree one. Thus
both satisfy the adopted literal definition.

# Constraint-and-conclusion matrix

| constraint_id | candidate value | result | evidence |
|---|---|---|---|
| `21.90-exists-Gamma` | \(H(3,2)\) | pass | explicit vertex and adjacency definition above |
| `21.90-diameter-3` | maximum Hamming distance is 3 | pass | \(000\) and \(111\) are distance 3 |
| `21.90-Q-polynomial-distance-regular` | Hamming scheme ordering \(E_0,E_1,E_2,E_3\) | pass candidate | intersection numbers and character-idempotent argument above |
| `21.90-distance-graph-definition` | adjacency at Hamming distance 2 or 3 | pass | direct construction above |
| `21.90-Gamma2-strongly-regular` | \(2K_4=\operatorname{srg}(8,3,2,0)\) | pass | common-neighbour count above |
| `21.90-Gamma3-strongly-regular` | \(4K_2=\operatorname{srg}(8,1,0,0)\) | pass | common-neighbour count above |
| `21.90-existence-conclusion` | one explicit graph exists | pass candidate | all preceding rows |

# Exact limitation

This answers revision 2 only if the human-supplied displayed definition is used
literally. It does not answer the stricter variant requiring a nontrivial,
connected, or primitive strongly regular graph. The cited page itself notes that
the disconnected examples are conventionally excluded from detailed studies, so
the review circle must audit the interpretation as well as the graph proof before
Lead asks the human to close the scope.
