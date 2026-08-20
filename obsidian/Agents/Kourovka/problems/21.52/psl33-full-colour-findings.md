---
title: "Kourovka 21.52 — fixed PSL(3,3) full-colour determination"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
outcome: PARTIAL_RESULT
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/conjectured]
---

# Fixed `PSL(3,3)` full-colour determination

## Active target

Scope: `21.52/involution-class-product-order-colouring`, revision 1.

Universal target: for every finite nonabelian simple `L` and every single involution conjugacy class `D`, every permutation of `D` preserving every exact product-order edge colour is induced by an automorphism of `L` stabilizing `D`.

## Bounded result

For the exact fixed group `L=PSL(3,3)` and its unique involution class `D` of size 117, the frozen computation reports

`Aut_col(D, |ab|) = res_D(Aut(L))`,

with both permutation groups of order 11,232. Thus `PSL(3,3)` supplies no counterexample. This is a singleton `PARTIAL_RESULT`; it does not answer the universal scope.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed candidate / use | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible `(L,D)` | only the fixed pair `(PSL(3,3),D)` | direct quantifier comparison | **not covered universally** |
| `21.52-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `SL(3,3)` has order 5,616 and trivial centre, hence is `PSL(3,3)`; standard PSL simplicity theorem and exact GAP predicate | log hand derivation; certificate lines 4--10 | pass for fixed pair |
| `21.52-D-single-involution-class` | admissibility | one conjugacy class, all members order 2 | the unique class, size 117 | anti-flag derivation; exact enumeration lines 11--13 | pass for fixed pair |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered pairs of distinct vertices | all `117 choose 2 = 6,786` pairs | complete matrix and incidence encoding | pass for fixed pair |
| `21.52-edge-colour-exact-product-order` | admissibility | colour exactly `Order(ab)` | orders `2,3,4,6`, counts `702,1872,1404,2808` | complete 117-by-117 matrix in `run.stdout` | pass for fixed pair |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary full-colour-preserving permutation | full automorphism group of the exactly coloured incidence encoding | certificate group generators/order and exhaustive direct generator checks | pass for fixed pair |
| `21.52-tau-induced-by-AutL` | target conclusion | every such permutation extends | exact mutual subgroup containment with the full `Aut(L)` restriction image | certificate lines 603--678 | pass for fixed pair; **unproved universally** |

No target-conclusion row is violated, so there is no counterexample claim.

## Exact object and group/class reconstruction

The mathematical object computed in is a faithful permutation image of the matrix group `SL(3,3)`. The checker obtains order 5,616, trivial centre, an explicit isomorphism with GAP's `PSL(3,3)`, nonabelianity, and simplicity. It enumerates every conjugacy class and finds exactly one whose representative has order two; that class has 117 members and every selected member is checked to have order two.

Independently, an involution on `F_3^3` is semisimple with eigenvalue multiplicities `(+1)^1,(-1)^2`. It is therefore an anti-flag `(P,H)` in `PG(2,3)`, with `P` not on `H`. There are `13*9=117` such anti-flags. The centralizer has order 48 in `SL(3,3)`, giving the same class size, and determinant surjectivity in the `GL(1,3) x GL(2,3)` centralizer prevents class splitting from `GL` to `SL`.

## Complete exact colouring

The checker computes `Order(D[i]*D[j])` for every ordered matrix entry and uses all 6,786 off-diagonal unordered pairs. Its full 117-by-117 order matrix is printed in `run.stdout`; the observed off-diagonal histogram is:

| exact order | valency | unordered edges |
|---:|---:|---:|
| 2 | 12 | 702 |
| 3 | 32 | 1,872 |
| 4 | 24 | 1,404 |
| 6 | 48 | 2,808 |

This agrees with the independent anti-flag calculation. If `t(u,f)=2(u tensor f)-I` and `t(v,g)=2(v tensor g)-I`, normalized by `f(u)=g(v)=1`, put `alpha=f(v)` and `beta=g(u)`. For distinct vertices, the product order is 2 when both cross-values vanish, 6 when exactly one vanishes, 3 when `alpha*beta=1`, and 4 when `alpha*beta=-1`.

## Full colour group and automorphism restriction image

For every coloured edge `{i,j}`, the checker creates one subdivision vertex adjacent exactly to `i,j`; original vertices form one vertex-colour class and subdivision vertices are partitioned by exact product order. This graph has 6,903 vertices. Restriction gives an isomorphism from its vertex-colour-preserving automorphism group to the full colour-preserving group on `D`: every colour permutation extends uniquely to edge-vertices, and every incidence automorphism restricts faithfully because endpoints determine each edge-vertex.

GRAPE/nauty returns incidence and restricted colour groups of order 11,232. GAP independently computes the full `AutomorphismGroup(L)`, also of order 11,232. The involution class is unique, so its setwise stabilizer is the whole automorphism group. Restricting all automorphism generators gives a faithful permutation group on `D` of order 11,232. Exact permutation-group tests return both `Aut(L)|_D <= Aut_col` and `Aut_col <= Aut(L)|_D` as true. The transcript prints generators of both groups and checks every generator against all 6,786 edge colours.

## Reproducibility

- Frozen checker: `Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/psl33_full_colour.g`
- Checker SHA-256: `4fd4e8ef68143e31421986f8fa2b02adfce1fa136f2075d181928e9668da1c79`
- Manifest: `Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/frozen-run-manifest.md`
- Exact command: `timeout --signal=TERM --kill-after=5s 60s gap -q Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/psl33_full_colour.g > Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/run.stdout 2> Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/run.stderr`
- Sole invocation: exit 0 in 26.68 seconds; GAP 4.12.1; GRAPE 4.9.0.
- `run.stdout`: SHA-256 `f238e45b0a22eeb835f2e6650314410f1b03983b972fa513a6609ff29ac75eea`, 50,495 bytes.
- `run.stderr`: empty; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## What this does not establish

It does not prove Problem 21.52 for any group other than the fixed `PSL(3,3)` pair, does not address a second involution class (there is none in this group), and does not justify extrapolation from the three reviewed/fixed positive cases. It does not address Problem 21.53, unions of involution classes, an uncoloured graph, or conjugacy-class edge colours.

## How this could be wrong

1. A defect in GAP's group or graph-automorphism routines could affect the computational equality; Validator should rebuild the anti-flag structure or use an independent exact encoding.
2. The vertex-coloured incidence construction could be mistranslated, although the endpoint-uniqueness argument and exhaustive direct generator checks are explicit safeguards.
3. Equality of orders alone would be insufficient; the certificate therefore tests both exact subgroup containments.
4. The fixed pair is not the universal family; presenting this bounded equality as a proof would fail `21.52-forall-L-D`.

