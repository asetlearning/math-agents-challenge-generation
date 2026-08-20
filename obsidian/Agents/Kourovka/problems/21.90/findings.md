---
tags: [status/conjectured, project/kourovka, problem/21.90]
---

## The claim

No vertex-transitive distance-regular graph with intersection array `{39,25,10;1,5,30}` has the known `NO_5^{-\perp}(5)` graph as its distance-3 graph.

## What I computed in

The exact 300-point graph on nonsquare-type projective points of the quadratic space

$$Q(x)=x_1x_2+x_3x_4+x_5^2\quad\text{over }\mathbb F_5,$$

with perpendicularity adjacency. GRAPE 4.9.0 and nauty identify its full automorphism group as a transitive permutation group of order 9,360,000, with derived subgroup `PSp(4,5)` of order 4,680,000. I used GAP's complete table of marks `S4(5)` (307 subgroup conjugacy classes) and the exact 300-point permutation action.

## Is that object the target?

For this intersection array, the distance-3 graph is forced to have parameters `srg(300,65,10,15)`. DistanceRegular.org identifies the constructed graph as the unique rank-4 graph with those parameters, not as the unique SRG with those parameters. Therefore the computation excludes vertex-transitive target realizations whose distance-3 constituent is this standard polar graph. It does not exclude a realization using a nonisomorphic SRG with the same parameters, if one exists.

## Argument / evidence

Script: `Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5.g`.

Final output: `Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5_slot3.out`.

Exact command:

```bash
timeout 35m gap -q Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5.g > Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5_slot3.out 2> Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5_slot3.stderr
```

Observed summary:

```text
projective_points=781 Q_counts=[156,163,150,150,162]
type_size=300 degrees=[65] common_counts=[10,15]
minus_perp aut_order=9360000 vertex_orbit=300 stabilizer_orbit_sizes=[1,65,104,130]
derived_order=4680000 stabilizer_orbit_sizes=[1,65,104,130]
tom_classes=307 iso_fail=false
derived_transitive_classes=5 derived_target_hits=0 two_150_classes=3 runtime_ms=668
outer_extensions_tested=3 outer_transitive=3 outer_target_hits=0 total_vertex_transitive_hits=0 total_runtime_ms=749
exit_code=0
```

Completeness for vertex-transitive subgroups of the full polar-graph automorphism group is as follows. If `G=Aut(A3)` and `D=G'` has index two, then for a transitive subgroup `H<=G`, `H∩D` is either transitive or has exactly two orbits of size 150. All transitive subgroup classes inside `D` were obtained from the complete table of marks. All three `150+150` classes were extended through every outer involution in `N_G(H∩D)/(H∩D)`. For every resulting transitive group, every self-paired orbital union of valency 39 disjoint from `A3` was tested against

$$A_1A_3=10A_2+9A_3.$$

No union passed this necessary identity; consequently none needed the subsequent exact quadratic check

$$A_1^2=34I+8A_1+5J-5A_3.$$

An earlier unpruned attempt was stopped after it exposed 47 eligible orbitals; it produced no result and is not part of the certificate. The final pruned run exited normally.

## What this does NOT establish

- It does not exclude asymmetric realizations of `{39,25,10;1,5,30}`.
- It does not exclude a realization whose distance-3 graph is a different `srg(300,65,10,15)`.
- It does not settle Problem 21.90 or eliminate any other feasible intersection array.
- It does not resolve whether the literal problem intentionally permits the degenerate cube witness `H(3,2)`.

## How I could be wrong

1. The database statement “unique rank-4” could be misread as uniqueness among all SRGs; I have deliberately not made that inference.
2. The table-of-marks group-to-permutation-group isomorphism could map into the wrong index-two subgroup, although the computed image has the verified order 4,680,000 and is the derived subgroup of the full graph automorphism group.
3. The outer-extension completeness argument could omit a subgroup if `H∩D` were neither transitive nor `150+150`; index two and transitivity force precisely those two possibilities, so Validator should check this step.
4. A coding error in orbital pairing or the linear matrix identity could cause false rejection; the script uses GRAPE's undirected edge-orbit graphs and Validator should independently inspect the implementation.
