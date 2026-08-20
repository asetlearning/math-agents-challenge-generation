---
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 16
outcome: PARTIAL_RESULT
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/conjectured]
---

# Candidate bounded theorem: six-transposition classes in A12, A13, A14

## Active target

Scope: `21.52/involution-class-product-order-colouring`, revision 1.

Universal target: for every finite nonabelian simple group \(L\) and every involution class \(D\), every permutation of \(D\) preserving every exact product-order colour is induced by a setwise stabilizing automorphism of \(L\).

## The bounded claim

For each \(n\in\{12,13,14\}\), let \(L=A_n\) and let \(D_n\) be the class of involutions of cycle type \(2^6 1^{n-12}\). My candidate result is
\[
 \operatorname{Aut}_{\rm col}(D_n,\ |xy|)=S_n|_{D_n}
 =\operatorname{Aut}(A_n)|_{D_n}.
\]
This is a three-degree alternating-family `PARTIAL_RESULT`, not an answer to the universal notebook problem.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | universal over admissible \((L,D)\) | explicitly restricted to three pairs \((A_n,D_n)\); reported only as partial progress | this note, bounded-claim statement | pass-for-stated-partial only |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(L\) finite nonabelian simple | \(A_{12},A_{13},A_{14}\) | standard simplicity of \(A_n\), \(n\ge5\) | pass |
| `21.52-D-single-involution-class` | admissibility | one conjugacy class, all elements order 2 | type \(2^6 1^{n-12}\); the \(S_n\)-class does not split in \(A_n\), since splitting requires distinct odd cycle lengths | matching model below | pass |
| `21.52-Gamma-complete-on-D` | admissibility | every distinct unordered pair is coloured | every pair of six-matchings is included in the orbit and intersection-array enumeration | `scratch/matching_orbits.py`, `scratch/pair_colour_signatures.py` | pass |
| `21.52-edge-colour-exact-product-order` | admissibility | colour is exactly \(|xy|\), not conjugacy class | order computed from the actual permutation product / alternating union components | derivation and scripts below | pass |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary full-colour-preserving \(\tau\) | the sparse relation in each degree is defined by exact-colour intersection counts, hence every such \(\tau\) preserves it | exact signatures below | pass |
| `21.52-tau-induced-by-AutL` | target conclusion | every such \(\tau\) is induced by \(\operatorname{Aut}(L)\) | sparse-relation automorphism groups are the natural \(S_n\); conversely \(S_n=\operatorname{Aut}(A_n)\) acts faithfully and preserves all product orders | rigidity certificates and incidence proof below | proved for these three pairs; universal row remains unknown |

Explicit exclusions retained: no Problem 21.53; no union of involution classes; no uncoloured complete graph; no product-conjugacy-class refinement; no inference from these three degrees to all simple groups.

## 1. Matching model and exact product order

Identify an element of \(D_n\) with its six disjoint transposition edges, a six-matching of \(K_n\). For matchings \(M,N\), every nontrivial component of the two-coloured union is one of:

- a doubled common edge, contributing order 1;
- an alternating cycle of length \(2r\), on which \(MN\) is two \(r\)-cycles, contributing \(r\);
- an alternating path of \(s\) edges, on which \(MN\) is an \((s+1)\)-cycle, contributing \(s+1\).

Thus \(|MN|\) is the least common multiple of these contributions. This was independently implemented without cycle-15 constants in `scratch/matching_orbits.py` (SHA-256 `7498bab19b1f5da9e760f21f03a364bdc7b541f43f8cbea0513286d0429b01b3`). It exhausts respectively 10,395; 135,135; and 945,945 matchings and finds 10, 29, and 74 un-oriented component signatures relative to a fixed matching. For `n=14` this coarse inventory can merge the base/N orientation of unequal odd paths, so it is not asserted to be a full orbit list outside the target colours. In product colours 2 and 3, however, the only paths are respectively balanced pairs of one-edge paths or even two-edge paths; hence the candidate lists used below are complete stabilized-pair orbit lists.

For a coloured pair \((x,y)\), define the intrinsic two-point number
\[
 N_{r,s}(x,y)=|\{z\in D_n\setminus\{x,y\}: |xz|=r,\ |yz|=s\}|.
\]
The exact enumeration `scratch/pair_colour_signatures.py` (SHA-256 `f2efd61b9fa833455242331d5379ed1eb00fe1154eb1a8ab721f46498f194863`) gives:

- \(n=12\): the three order-2 pair orbits have respectively 0, 2, 4 common matching edges and \(N_{2,2}=61,37,73\). Hence
  \[
  M\sim_{12}N\iff |MN|=2\text{ and }N_{2,2}(M,N)=73
  \]
  is exactly the four-common-edge flip relation on perfect matchings.
- \(n=13\): the four order-3 pair orbits have respectively 0, 2, 3, 5 common edges and \(N_{2,3}=33,15,21,0\). Hence
  \[
  M\sim_{13}N\iff |MN|=3\text{ and }N_{2,3}(M,N)=0
  \]
  is exactly five-edge adjacency.
- \(n=14\): among all six order-2 pair orbits, the \(N_{2,4}\) values are \(258,122,176,260,290,530\), with 530 uniquely the five-common-edge/disjoint-final-edges type. Among all six order-3 pair orbits, the values are \(72,24,39,201,25,125\), with 125 uniquely the five-common-edge/intersecting-final-edges type. Thus five-edge adjacency is exactly the union of the intrinsic conditions \((|MN|,N_{2,4})=(2,530)\) and \((3,125)\).

Every full exact-colour automorphism therefore preserves the stated sparse relation in each degree.

## 2. Degree 12: exact labelled flip-graph certificate

The relation graph is the four-point flip graph \(F_{12}\) on all perfect matchings of 12 labelled points: two vertices are adjacent exactly when four of their six edges agree. The current reproducible checker is `scratch/perfect_matching_flip_aut.g` (SHA-256 `6e840f4444db78d6e5c51e96b5ed8bfa20498dea3bb8cab3228f466b03f537ae`). A successful GRAPE/nauty run observed:

```text
n=12
vertices=10395 expected=10395
degree=30 expected=30 edges=155925
natural_kernel_size=1 natural_order=479001600 expected=479001600
natural_is_subgroup_of_full=true
full_aut_order=479001600
natural_equals_full=true
ELAPSED=7.60 MAXRSS_KB=142720 EXIT=0
```

This is not an order-only comparison: the script separately constructs the labelled action homomorphism \(S_{12}\to S(D_{12})\), checks its kernel is trivial, checks its image is a subgroup of the full graph automorphism group, and then checks equality of the two permutation groups. Therefore \(\operatorname{Aut}(F_{12})=S_{12}\) in its natural matching action.

## 3. Degree 13: core-star geometry and local rigidity

Let \(X_{13}\) be the graph on six-matchings with five-edge adjacency.

The elementary Johnson-clique lemma says that a clique of at least three \(k\)-subsets with pairwise intersection \(k-1\) is either a star (one fixed \((k-1)\)-core) or a top (contained in one \((k+1)\)-set). Here a 5-core leaves three points and has exactly three six-matching extensions, so every core-star is a triangle. A top of size at least three would require seven pairwise-disjoint edges, impossible on 13 points; a nonmatching seven-edge set has at most two valid six-edge deletions. Thus the maximal cliques are exactly the core-star triangles. At a vertex \(M\), they give six disjoint edges in the induced neighborhood, one for each deleted edge of \(M\): \(X_{13}[N(M)]=6K_2\).

The labelled local certificate `scratch/n13_local_distance_certificate.py` (SHA-256 `6ec24d9aaf6323864d8ee463a4d5226df90915e5c6cefa8a1c392284505b847d`) independently generated the complete graph by the unmatched-point edge-replacement move. It obtained:

```text
vertices=135135 degree=12 local_vertices=12
local_edges=6 local_degree_set=[1]
distance_sources=13 initial_distance_colours=7701
equitable_refinement_colour_counts=[7701, 107463, 135135, 135135]
pointwise_closed_neighborhood_stabilizer_bound=1
vertex_stabilizer_bound=46080
full_aut_order_bound=6227020800 factorial_13=6227020800
natural_S13_containment_plus_bound_gives_equality=true
ELAPSED=13.00 MAXRSS_KB=91612 EXIT=0
```

Why this certifies the bound: an automorphism fixing \(M\) acts on \(6K_2\), so its induced local action has order at most \(2^6 6!=46{,}080\). An automorphism fixing the closed neighborhood pointwise preserves every distance vector from those 13 fixed sources and every subsequent equitable-refinement colour. The final discrete partition therefore makes that pointwise kernel trivial. Since the natural faithful \(S_{13}\) is vertex-transitive and has stabilizer \(2^6\!\rtimes S_6\),
\[
 |\operatorname{Aut}(X_{13})|\le 135135\cdot 2^6 6!=13!,
\]
while the natural \(S_{13}\) is already contained. Hence \(\operatorname{Aut}(X_{13})=S_{13}\).

## 4. The perfect-matching flip graph F14

This auxiliary graph has 135,135 perfect matchings of 14 points and degree \(2\binom72=42\). Fix a base matching \(M\). Its neighborhood is \(21K_2\): the 21 blocks correspond to unordered pairs \(\{i,j\}\) of the seven edges of \(M\), and the two block vertices are the two alternate pairings of their four endpoints.

The exact local tables in `scratch/n14_flip_kernel_refinement.py` (SHA-256 `b2650f5df63f68d6599af681950eb8f363187516939aedcf8cde16cc06088632`) show:

- the two vertices in one direction block have exactly 1 common neighbor;
- vertices from distinct direction blocks have exactly 2 common neighbors when the two 2-subsets are disjoint and exactly 3 when they intersect;
- for the three blocks \(ij,ik,jk\), after binary labelling of the two alternatives, three chosen local vertices have 1 common neighbor for even bit parity and 3 common neighbors for odd parity.

Consequently a stabilizer of \(M\) first induces an automorphism of the line graph \(L(K_7)\), hence an element of \(S_7\). After removing that natural block permutation, let \(s_{ij}\in\mathbf F_2\) say whether the two vertices of direction \(ij\) are swapped. The triple-common-neighbor table forces
\[
 s_{ij}+s_{ik}+s_{jk}=0
\]
for every triple. These solutions are exactly \(s_{ij}=t_i+t_j\), so there are at most \(2^6\) local actions after the block permutation.

For the remaining pointwise closed-neighborhood kernel, exact equitable refinement gives:

```text
vertices=135135 degree=42 adjacency_entries=5675670
same_direction_pair_common_neighbor_counts=[1]
distinct_direction_pair_common_neighbor_table=[(('disjoint', 2), 420), (('intersect', 3), 420)]
direction_triangle_parity_common_neighbor_table=[((0, 1), 140), ((1, 3), 140)]
first_refinement_counts=[44, 604, 3964, 15836, 40700, 64859, 68219, 68219]
stable_cell_size_distribution=[(1, 1303), (2, 66916)] max_cell=2
second_refinement_counts=[68220, 68259, 68867, 73679, 92463, 123615, 135135, 135135]
individualized_second_partition_is_discrete=true
pointwise_closed_neighborhood_stabilizer_order_bound=2
ELAPSED=12.29 MAXRSS_KB=151488 EXIT=0
```

Indeed, the pointwise kernel has every orbit inside a first stable cell, hence an orbit of size at most 2. After fixing one point of a two-cell the second partition is discrete, so that point stabilizer is trivial and the kernel has order at most 2. Therefore
\[
 |\operatorname{Aut}(F_{14})_M|\le 2\cdot2^6\cdot7!=2^7 7!,
\qquad
 |\operatorname{Aut}(F_{14})|\le135135\cdot2^7 7!=14!.
\]
The natural faithful \(S_{14}\) is contained, so equality follows with the labelled natural action.

## 5. Degree 14: star/top reconstruction

Let \(X_{14}\) be the five-common-edge graph on six-matchings.

By the same clique lemma, its maximal cliques are of two intrinsically distinguishable kinds:

- a **core-star** \(S_C\), all extensions of one 5-matching \(C\); four points remain and there are \(\binom42=6\) extensions, so \(|S_C|=6\);
- a **top** \(T_P=\{P\setminus\{e\}:e\in P\}\) from one perfect 7-matching \(P\); hence \(|T_P|=7\).

There are no other maximal cliques of size at least three. In the top case, if the underlying seven-edge union contained an intersecting pair, deleting one edge could repair it for at most the two endpoints of that incompatibility, so at most two valid six-matchings would occur; thus a genuine top has seven disjoint edges.

Each 5-core leaves four points. Their three perfect matchings give exactly three tops, each meeting \(S_C\) in two vertices. Hence the graph whose vertices are the intrinsic size-7 tops, with two tops adjacent when they occur in a common size-6 star, is precisely \(F_{14}\); every star records one flip triangle.

An automorphism of \(X_{14}\) therefore induces an automorphism of \(F_{14}\). This action is faithful: if all tops are fixed, then every star is fixed because its incident triple of tops determines its 5-core uniquely. For fixed \(P\), every pair of vertices \(P\setminus\{e\},P\setminus\{f\}\) is the intersection of \(T_P\) with the star of \(P\setminus\{e,f\}\). A permutation of \(T_P\) fixing every such 2-subset is the identity. Thus
\[
 \operatorname{Aut}(X_{14})\hookrightarrow\operatorname{Aut}(F_{14})=S_{14}.
\]
The natural \(S_{14}\) is already contained, proving equality.

## 6. Return to the exact-order colouring

For every \(n=12,13,14\), exact-colour automorphisms preserve the colour-defined sparse relation, so
\[
 \operatorname{Aut}_{\rm col}(D_n)\le\operatorname{Aut}(X_n)=S_n.
\]
Conversely every point permutation in \(S_n=\operatorname{Aut}(A_n)\) conjugates the class setwise and preserves the exact order of every product. Its action on six-matchings is faithful. Therefore both inclusions are labelled natural inclusions and equality holds.

## Failed run explicitly excluded

A frozen heavy runner was leased once. Its first redundant full `n=13` GRAPE job timed out with exit 124 after `ELAPSED=172.58`, `MAXRSS_KB=302592`; stdout was empty. Fail-fast prevented the `n=14` job from launching. This failed invocation is not used anywhere above. The successful local certificates are separate sub-60-second computations.

## What this does not establish

- It does not prove Problem 21.52 for arbitrary finite simple groups or arbitrary involution classes.
- It does not use or validate the preceding unreviewed \(n\ge15\) theorem; that result is not a premise here.
- It does not address Problem 21.53, unions of classes, or product-conjugacy-class colouring.
- The finite colour-definability and local-rigidity enumerations require independent Validator reproduction before certification.

## How this could be wrong

1. The coarse component-key generator deliberately forgets odd-path orientation; the argument needs the stated completeness check only in product colours 2 and 3. Validator should independently reconstruct those candidate lists and the compact signature coordinates.
2. The equitable-refinement argument is valid only because initial source vertices are individualized pointwise and refinement is automorphism-invariant; an implementation/indexing error could invalidate the numerical discreteness claims.
3. The star/top reduction relies on the full maximal-clique classification, especially excluding three valid deletions from a nonmatching seven-edge union.
4. The observed successful `n=12` run preceded a later print-only removal of a verbose orbit listing; the current checker retains the same graph/action/equality computation, but Validator should rerun it from the current hash rather than trust that provenance detail.
