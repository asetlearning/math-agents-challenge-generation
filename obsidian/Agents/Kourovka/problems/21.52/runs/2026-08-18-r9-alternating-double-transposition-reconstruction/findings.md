---
title: "Candidate family partial — double transpositions in alternating groups"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
cycle: 9
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - topic/coloured-graphs
  - project/kourovka
  - status/conjectured
---

# Double-transposition colour rigidity in \(A_n\), \(n\ge7\)

## Active target

Scope: `21.52/involution-class-product-order-colouring`, assignment revision 1.

The notebook target quantifies over every finite nonabelian simple group and every single involution class. This note makes only an infinite-family partial claim.

## Candidate family theorem

Let \(n\ge7\), let \(L=A_n\), and let
\[
D_n=\{(ab)(cd):a,b,c,d\text{ pairwise distinct}\}.
\]
If a permutation \(\tau\) of \(D_n\) satisfies
\[
 |xy|=|\tau(x)\tau(y)|\qquad(x\ne y),
\]
then there is a unique \(\sigma\in S_n\) such that
\[
 \tau((ab)(cd))=(\sigma(a)\sigma(b))(\sigma(c)\sigma(d)).
\]
Consequently the exact product-order coloured graph on \(D_n\) has automorphism group the natural faithful \(S_n\), and every colour automorphism is induced by an automorphism of \(A_n\).

This is a candidate `PARTIAL_RESULT` for the alternating family, not a solution claim for the universal scope.

## 1. Full two-matching product-order scheme

Identify \(x=(ab)(cd)\) with the two-edge matching \(M_x=\{ab,cd\}\) and write \(S_x\) for its four-point support. For distinct \(x,y\), put \(q=|M_x\cap M_y|\) and \(r=|S_x\cap S_y|\). The red-blue union of the matchings has maximum degree two. Alternating paths of two, three, and four edges contribute respectively a 3-, 4-, and 5-cycle to \(xy\); an alternating 4-cycle contributes two transpositions; and a common red-blue edge cancels. This gives every possibility:

| \(q\) | \(r\) | union description apart from a common doubled edge | \(|xy|\) |
|---:|---:|---|---:|
| 1 | 2 | the two remaining edges are disjoint | 2 |
| 1 | 3 | the two remaining edges meet once | 3 |
| 0 | 0 | four isolated matching edges | 2 |
| 0 | 1 | one two-edge path and two isolated edges | 6 |
| 0 | 2 | two disjoint two-edge paths | 3 |
| 0 | 2 | one three-edge path and one isolated edge | 4 |
| 0 | 3 | one four-edge path | 5 |
| 0 | 4 | one alternating 4-cycle (the other matching on the same support) | 2 |

There are no other rows: \(q=1\) forces \(r=2\) or \(3\) for distinct matchings, while \(q=0\) is classified by the path/cycle components.

For a fixed \(x\), with \(m=n-4\), the numbers of \(y\) in the eight rows are, in the same order,
\[
2\binom m2,\quad 4m,\quad 3\binom m4,\quad
12\binom m3,\quad 8\binom m2,\quad 8\binom m2,
\quad 8m,\quad 2.
\]
Their sum is \(3\binom n4-1=|D_n|-1\), so the table is exhaustive. In particular, the exact colours are \(2,3,4,5,6\) (with a row absent when its support size is unavailable).

## 2. Intrinsic recovery of the three matchings on each 4-support

For a colour-2 pair \(x,y\), define the colour-language intersection numbers
\[
 N_{ij}(x,y)=|\{z\in D_n\setminus\{x,y\}:|xz|=i,\ |yz|=j\}|.
\]
There are precisely three geometric colour-2 types:

- \(A\): \(S_x=S_y\), with the two distinct matchings on that support;
- \(B\): one common transposition and disjoint remaining transpositions;
- \(C\): disjoint supports (available only for \(n\ge8\)).

Directly partitioning the two edges of \(z\) gives:

| type | \(N_{33}\) | \(N_{24}\) |
|---|---:|---:|
| \(A\) | \(2(n-4)(n-5)\) | \((n-4)(n-5)\) |
| \(B\) | \(8n-44\) | \((n-6)(n-7)+2\) |
| \(C\) | \(32\) | \(4(n-8)(n-9)+8\) |

Here is a hand count of the potentially fragile entries. In type \(A\), a common colour-3 neighbour uses one of the two edges of the third matching on \(S_x\), two outside points, and one of the two cross pairings, giving \(4\binom{n-4}{2}=2(n-4)(n-5)\); a \((2,4)\)-neighbour uses one of the two edges of \(x\) and an outside edge, giving \(2\binom{n-4}{2}\). In type \(B\), write \(x=e a\), \(y=e b\) on the disjoint edges \(e,a,b\). The \((3,3)\)-neighbours are the four matchings \(e\,(uv)\) with \(u\in a,v\in b\), together with the \(8(n-6)\) matchings pairing one point of each of \(e,a,b\) as described by an external fourth point. The \((2,4)\)-neighbours are the two other matchings on \(S_x\), plus \((n-6)(n-7)\) matchings supported on \(b\) and two points outside \(S_x\cup S_y\). In type \(C\), a common colour-3 neighbour chooses a cross-pair of each of the two fixed matchings and one of two bipartite pairings, giving \(4\cdot4\cdot2=32\); the \((2,4)\) count is \(8+8\binom{n-8}{2}\).

For \(n\ge8\), the type-\(A\) value of \(N_{33}\) differs from both other values:
\[
2(n-4)(n-5)-(8n-44)=2(n-6)(n-7)>0,
\]
and \(2(n-4)(n-5)\ne32\) for integral \(n\). At \(n=7\), type \(C\) is absent, while types \(A,B\) have \((N_{33},N_{24})=(12,6),(12,2)\). Hence the relation
\[
x\equiv y\iff x=y\quad\hbox{or}\quad (x,y)\text{ is a type-}A\text{ pair}
\]
is intrinsic to the exact coloured graph for every \(n\ge7\). Its classes are exactly
\[
F_S=\{\text{the three perfect matchings on }S\},
\qquad S\in\binom{[n]}4.
\]
Thus every \(\tau\) induces a permutation \(\bar\tau\) of the 4-subsets.

## 3. Recovering all support intersections

For distinct 4-subsets \(S,T\), the multiset of the nine colours between \(F_S\) and \(F_T\) is:

| \(|S\cap T|\) | colour multiset on \(F_S\times F_T\) |
|---:|---|
| 0 | \(2^9\) |
| 1 | \(6^9\) |
| 2 | \(2^1 3^4 4^4\) |
| 3 | \(3^3 5^6\) |

The four rows are distinct, so \(\bar\tau\) preserves every support-intersection cardinality.

The standard Johnson reconstruction lemma, with its exceptional case stated explicitly, says that an intersection-preserving permutation of \(\binom{[n]}4\) is point-induced when \(n\ne8\), while for \(n=8\) it is either point-induced or point-induced followed by complementation. A short reconstruction is enough here: in the adjacency graph \(|S\cap T|=3\), maximal cliques are the stars through a 3-subset (size \(n-3\)) and the tops inside a 5-subset (size 5). For \(n\ge9\) their sizes distinguish them and downward reconstruction recovers 3-subsets, then 2-subsets, then points. For \(n=7\), complement 4-subsets to 3-subsets and apply the same unequal-star/top reconstruction. For \(n=8\), stars and tops both have size 5, giving precisely the possible complementation swap.

## 4. The \(n=8\) complement cannot lift

When \(|S\cap T|=3\), the colour-3 edges between \(F_S\) and \(F_T\) form a perfect matching; call its bijection \(\phi_{S,T}:F_S\to F_T\). If \(S=I\cup\{a\}\), \(T=I\cup\{b\}\), then \(\phi_{S,T}\) pairs exactly the two double transpositions sharing their edge inside the common triple \(I\).

For a top triangle
\[
S_a=I\cup\{a\},\quad S_b=I\cup\{b\},\quad S_c=I\cup\{c\},
\]
parallel transport by the three \(\phi\)'s has identity holonomy: label all three fibres by the common internal edge in \(I\).

For a bottom triangle of 4-subsets inside a 5-set, the holonomy is a transposition. Explicitly, for
\[
B=\{1,2,3,4,5\},\quad S=B\setminus\{1\},\quad
T=B\setminus\{2\},\quad U=B\setminus\{3\},
\]
transport around \(S\to T\to U\to S\) fixes \((23)(45)\) and swaps
\((24)(35)\) with \((25)(34)\).

In degree 8, complementation sends every top triangle to a bottom triangle. Any lift would have to conjugate the source holonomy to the target holonomy, but the identity cannot be conjugate to a transposition. Therefore the complementary Johnson automorphism does not lift to the exact product-order coloured graph.

## 5. Killing the fibrewise kernel

After composing \(\tau\) with the inverse of its recovered point permutation, assume \(\tau\) fixes every support fibre. Write its restriction as \(f_S\in\operatorname{Sym}(F_S)\). Preservation of the colour-3 perfect matchings gives
\[
f_T\phi_{S,T}=\phi_{S,T}f_S.
\]
Fix \(S\), choose an external point \(e\), and put \(B=S\cup\{e\}\). For each pair \(a,b\in S\), the bottom triangle
\[
S,\quad B\setminus\{a\},\quad B\setminus\{b\}
\]
has holonomy the transposition of \(F_S\) fixing the matching that contains the edge \(ab\). As \(ab\) ranges over the six pairs of \(S\), these give the three transpositions of \(F_S\). The intertwining equation makes \(f_S\) commute with all three, so \(f_S=1\). This holds for every \(S\); hence the fibrewise kernel is trivial.

## 6. Group-theoretic conclusion and exceptional degrees

The set \(D_n\) is one \(A_n\)-class: the \(S_n\)-class of cycle type \(2^2 1^{n-4}\) does not split in \(A_n\), by the usual splitting criterion (splitting requires distinct odd cycle lengths). Every point permutation \(\sigma\in S_n\) normalizes \(A_n\), and conjugation has exactly the recovered action on \(D_n\). It is faithful: \(D_n\) generates \(A_n\) because it is a nontrivial conjugacy class in the simple group \(A_n\), and \(C_{S_n}(A_n)=1\) for \(n\ge5\).

For context, the classical alternating-group automorphism theorem has the exact relevant hypothesis
\[
n\ge7\implies \operatorname{Aut}(A_n)\cong S_n
\]
via this conjugation action. Degree 6 is exceptional: \(\operatorname{Aut}(A_6)\) is strictly larger than the natural \(S_6\) (indeed \(|\operatorname{Out}(A_6)|=4\)), so the identity must not be quoted there. Degree 5 satisfies \(\operatorname{Aut}(A_5)\cong S_5\) but lies outside this uniform lane and was already a separate bounded target; degrees at most 4 are not finite nonabelian simple alternating groups. The family argument above uses only the explicit conjugation automorphism once \(\sigma\) is reconstructed, so it does not depend circularly on the full automorphism theorem.

## Constraint-and-conclusion matrix

| constraint_id | role | family handling | result |
|---|---|---|---|
| `21.52-forall-L-D` | admissibility | Only \((L,D)=(A_n,D_n)\), uniformly for \(n\ge7\); no claim for other simple groups/classes. | **not discharged universally** |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(A_n\) is finite nonabelian simple for every \(n\ge7\). | pass for family |
| `21.52-D-single-involution-class` | admissibility | \(D_n\) is the nonsplit single class of cycle type \(2^2 1^{n-4}\). | pass for family |
| `21.52-Gamma-complete-on-D` | admissibility | The eight-row table partitions every distinct pair in \(D_n\). | pass for family |
| `21.52-edge-colour-exact-product-order` | admissibility | Only the exact orders \(2,3,4,5,6\) are used; no product conjugacy classes occur. | pass for family |
| `21.52-tau-preserves-all-edge-colours` | admissibility | \(\tau\) is arbitrary subject to all exact pair-order equalities. | pass for family |
| `21.52-tau-induced-by-AutL` | target conclusion | Support reconstruction, exclusion of degree-8 complementation, and trivial fibre kernel yield conjugation by \(\sigma\in S_n\). | candidate established for family |

## What this does not establish

It does not answer Problem 21.52 for every finite nonabelian simple group or for other involution classes. It says nothing about Problem 21.53, unions of involution classes, or the finer colouring by the conjugacy class of a product. Degree 6 is not covered, and no conclusion about its exceptional outer automorphisms is inferred.

## How this could fail under review

- The two-point count table could contain an omitted configuration; the displayed hand partitions and the exhaustive row-count identity are intended to make that check local.
- The Johnson reconstruction lemma could be applied with stars and tops interchanged; degrees 7 and 8 are therefore handled separately rather than folded into the generic argument.
- The bottom-triangle holonomy orientation could be wrong; the explicit three-matching calculation is supplied for direct reconstruction.
- The proof recovers a point action, but a restriction-image statement still requires checking that conjugation by every recovered \(S_n\) element is an automorphism of \(A_n\); normality of \(A_n\) supplies exactly that step.
