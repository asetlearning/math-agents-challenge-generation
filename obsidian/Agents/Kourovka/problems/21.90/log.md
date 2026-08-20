---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/finite-graphs
  - project/kourovka
  - status/draft
problem_id: "21.90"
cycle: 1
---

# Problem 21.90 working log

## Active-time ledger

- 2026-08-11T15:49:23Z — work started; cumulative active minutes: 0.
- 2026-08-11T15:50:27Z — initial protocol/source/tool inspection checkpoint; cumulative active minutes: 1.

## Staleness check

### 2026-08-11T15:50:27Z — source and transcription gate

- Read `_meta/agents/Kourovka/_common-kourovka.md` in full, then the assigned synthesis, checked for an existing log, and checked `Agents/Kourovka/bus/inbox/Problem-21.90/` (no messages).
- Sourced `_meta/agents/Kourovka/paths.env`; the configured `$KOUROVKA_PDF` was readable and `$KOUROVKA_AUTHOR` was `operator`.
- Inspected PDF p. 177 both with `pdftotext -f 177 -l 177 -layout "$KOUROVKA_PDF" -` and visually from a 150-dpi rendering saved as `scratch/source-page-177.png`.
- Corrected, visually checked transcription:

> **21.90.** Let $\Gamma$ be a graph of diameter $d$. For $i\in\{1,2,\ldots,d\}$, let $\Gamma_i$ be the graph on the same vertex set as $\Gamma$ with vertices $u,w$ adjacent in $\Gamma_i$ if and only if $d_\Gamma(u,w)=i$. Does there exist a $Q$-polynomial distance-regular graph $\Gamma$ of diameter $3$ such that $\Gamma_2$ and $\Gamma_3$ are strongly regular? A. A. Makhnëv.

- The statement is unstarred and has no editor or later comment on the rendered source page.
- `source_transcription_checked: yes`.
- Corpus flags: the local extracted corpus ends at issue 20 (2022), so problem 21.90 has no JSONL corpus record. Accordingly `answered`, `has_editor_comment`, and `has_later_comment` are **not present / not applicable**, rather than false corpus values. Direct source inspection supplies the relevant negative evidence above.

### 2026-08-11T15:50:27Z — literature searches

- Searched the web for exact phrases `"Kourovka 21.90"` and `"Problem 21.90" "Kourovka"`; found no independent solution notice or bibliographic match to the problem number.
- Searched for proposer/key terms `A. A. Makhnev Q-polynomial distance-regular graph diameter 3 strongly regular distance graphs` and arXiv-restricted variants involving $\Gamma_2,\Gamma_3$; found no paper claiming an example and no arXiv solution.
- Checked the configured current Notebook No. 21 (2026): it lists 21.90 unstarred with no answer/comment.
- Relevant prior literature found (not solutions of the existence question):
  - M. S. Nirova, “On distance-regular graph $\Gamma$ with strongly regular graphs $\Gamma_2$ and $\Gamma_3$,” *Siberian Electronic Mathematical Reports* 15 (2018), 175–185. Search abstract gives parameter restrictions and feasible arrays.
  - I. N. Belousov, A. A. Makhnev, M. S. Nirova, “On $Q$-polynomial distance-regular graphs $\Gamma$ with strongly regular graphs $\Gamma_2$ and $\Gamma_3$,” *Siberian Electronic Mathematical Reports* 16 (2019), 1385–1392, DOI 10.33048/semi.2019.16.096. Abstract states a parameter equation and four infinite series of feasible intersection arrays, not graph existence.
  - A. A. Makhnev, M. P. Golubyatnikov, “Nonexistence of certain $Q$-polynomial distance-regular graphs,” *Trudy Inst. Mat. i Mekh. UrO RAN* 25(4) (2019), 136–141, DOI 10.21538/0134-4889-2019-25-4-136-141. It rules out/restricts certain parameter types, not all possibilities.
  - A. A. Makhnev, I. N. Belousov, K. S. Efimov, “On distance-regular graphs of diameter 3 with eigenvalue $\theta=1$,” *Ural Mathematical Journal* 8(2) (2022), 127–132, DOI 10.15826/umj.2022.2.010. It studies a special parameter series, not the full existence problem.
- Negative conclusion: as of this check, no evidence that the exact question is already solved; the 2026 source itself treats it as open.

## Tool inspection

### 2026-08-11T15:50:27Z

Command and observed output:

```text
gap -q
Print("GAP ", GAPInfo.Version, "\\n");
if LoadPackage("grape", false) = fail then Print("GRAPE unavailable\\n"); else Print("GRAPE loaded\\n"); fi;

GAP 4.12.1
#I  grape package is not available. Check that the name is correct
#I  and it is present in one of the GAP root directories (see '??RootPaths')
GRAPE unavailable
```

GRAPE, named in the assignment's proposed tooling, is missing. No graph enumeration was launched.

## Cycle status

- 2026-08-11T15:51:16Z — work stopped on mandatory missing-tool condition; cumulative active minutes: 2. Sent `type: BLOCKER` to Lead. Research budget is parked pending direction/tool availability.
- 2026-08-11T15:55:20Z — work resumed after operator reported blocker cleared; cumulative active minutes: 2.

## Dependency re-check

### 2026-08-11T15:55:20Z

- Read `Agents/Kourovka/bus/inbox/Problem-21.90/` first as directed. It contained no files, so there was nothing to mark done or archive; the clearance was supplied directly by the operator.
- Exact check and observed output:

```text
GAP 4.12.1
true
LoadPackage("grape", false) = true
GRAPE version 4.9.0
/usr/bin/dreadnaut
nauty 2.8.8+ds-5
```

- `geng` and a command literally named `nauty` were not found in `PATH`; `/usr/bin/dreadnaut` is present and the Debian `nauty` package reports version `2.8.8+ds-5`. Dependency blocker is cleared.

## Mathematical work

### 2026-08-11T16:05:40Z — statement in my own words

The target is a finite connected distance-regular graph $\Gamma$ with exactly four distance relations $A_0,A_1,A_2,A_3$ (diameter exactly 3), admitting a $Q$-polynomial ordering of its primitive idempotents, for which each of the relation graphs with adjacency matrices $A_2$ and $A_3$ is a nontrivial strongly regular graph. The literal source does not add “connected” to strongly regular; however, treating disconnected $\mu=0$ graphs as strongly regular makes $H(3,2)$ an immediate degenerate witness. The fact that this is posed in 2026 after the cited literature treats the Taylor case separately strongly suggests the intended question is the primitive/nontrivial case. I asked Math Expert to check this convention.

### 2026-08-11T16:05:40Z — named-family tests

Script: `scratch/test_classical_families.g`; output: `scratch/test_classical_families.out`; GAP 4.12.1 + GRAPE 4.9.0. It constructs the exact graphs, verifies `IsDistanceRegular`, builds the exact distance-2 and distance-3 graphs, and tests the common-neighbor definition of strong regularity over all unordered vertex pairs.

Observed highlights:

```text
H(3,2) vertices=8 distance_regular=true G2=[ 8, 3, 2, 0 ] G3=[ 8, 1, 0, 0 ]
H(3,4) vertices=64 distance_regular=true G2=[ 64, 27, 10, 12 ] G3=[ "notSRG", 27, [ 8 ], [ 12, 18 ] ]
J(7,3) vertices=35 distance_regular=true G2=[ 35, 18, 9, 9 ] G3=[ "notSRG", 4, [ 0 ], [ 0, 1 ] ]
Odd graph O4=KG(7,3) vertices=35 distance_regular=true G2=[ "notSRG", 12, [ 5 ], [ 0, 4 ] ] G3=[ 35, 18, 9, 9 ]
halved 7-cube vertices=64 distance_regular=true G2=[ 64, 35, 18, 20 ] G3=[ "notSRG", 7, [ 0 ], [ 0, 2 ] ]
```

Coverage: $H(3,q)$ for $2\le q\le7$, $J(n,3)$ for $6\le n\le10$, the odd graph $O_4$, and the halved 7-cube. This is a named-family sample, not exhaustive. Only the degenerate cube passes both predicates under the permissive $\mu=0$ convention.

### 2026-08-11T16:05:40Z — parameter reduction and bounded enumeration

The 2019 Belousov–Makhnev–Nirova abstract states that the non-Taylor target must have

$$
\{t(c_2+1)+a_3,\;tc_2,\;a_3+1;\;1,c_2,t(c_2+1)\}
$$

and in the $Q$-polynomial case satisfies

$$
c_2+1=\frac{a_3(a_3+1)}{t^2-a_3-1}.
$$

`scratch/enumerate_parameter_candidates.g` performs exact rational arithmetic for $1\le t\le100$, $1\le a_3\le1000$, checks layer-size integrality, linear factorization of the intersection matrix, positive integral eigenvalue multiplicities, computes the $P,Q$ matrices and all Krein parameters, and tests all six nontrivial idempotent orderings for irreducible tridiagonal $B_1^*$. Output is `scratch/enumerate_parameter_candidates.out`.

Observed summary:

```text
candidate_count=1475 bounds: 1<=t<=100, 1<=a3<=1000
qpolynomial_candidate_count=1475
```

This does **not** prove that any candidate intersection array is realized by a graph. It confirms that the quoted equation already enforces the elementary $Q$-polynomial/Krein pattern for all candidates passing the basic arithmetic filters in this box. The smallest non-Taylor candidate is

```text
t=2 a3=2 c2=5 IA={14,10,3;1,5,12} v=50
eig=[14,-6,-1,4] mult=[1,7,28,14] Qorders=[[1,4,3,2]]
```

### 2026-08-11T16:05:40Z — exact obstruction for the smallest array

For $\{14,10,3;1,5,12\}$ the distance-3 graph has spectrum/parameters $(50,7,0,1)$, hence is the unique Hoffman–Singleton graph $H$. For each vertex $x$, $C_x=\{x\}\cup\Gamma_1(x)$ would be a 15-coclique of $H$. If $x,y$ are $H$-adjacent, then $C_x\cap C_y=\varnothing$; if they are not $H$-adjacent, the intersection-number calculation gives $|C_x\cap C_y|=5$. Also $x\in C_x$.

`scratch/hoffman_singleton_local.g` reconstructs the exact Hoffman–Singleton graph from the two published GRAPE generators, computes all maximum cocliques from one GRAPE orbit representative and the full automorphism group, and records:

```text
HS vertices=50 degree=7 DR=true
15-coclique orbit_representatives=1 aut_order=252000
15-cocliques=100 incidence_count_vertex1=30
distinct pairwise intersections=[ 0, 3, 5, 8 ]
```

`scratch/search_hs_coclique_assignment.g` forms the disjointness graph on those 100 cocliques. It has two connected components, each a Hoffman–Singleton graph. Any required assignment $x\mapsto C_x$ must preserve every $H$ edge as coclique disjointness, so (because both source and a component are connected 7-regular graphs on 50 vertices) it must be an isomorphism onto one component. The script enumerates both base component isomorphisms composed with all 252,000 automorphisms of $H$ and checks $x\in C_x$ for all vertices.

Observed output:

```text
disjointness_graph degree=7 component_sizes=[ 50, 50 ]
component isomorphic_to_H=true
component isomorphic_to_H=true
isomorphisms_tested=504000 incidence_compatible_solutions=0
exit_code=0
```

Conclusion (current judgement, not yet independently validated): no distance-regular graph with intersection array $\{14,10,3;1,5,12\}$ exists. This eliminates only the smallest feasible non-Taylor parameter set, not Problem 21.90.

## Active-time ledger (continued)

- 2026-08-11T16:05:40Z — parameter/family and Hoffman–Singleton local search checkpoint; cumulative active minutes: 12.

### 2026-08-11T16:11:13Z — correction after full feasibility run

The earlier `qpolynomial_candidate_count=1475` line recorded an intermediate run. The final version of `scratch/enumerate_parameter_candidates.g` additionally reconstructs every association-scheme intersection number

$$p_{ij}^h=\frac{1}{v k_h}\sum_e m_eP_{ei}P_{ej}P_{eh}$$

and requires all of them to be nonnegative integers. Its actual final observed summary is:

```text
candidate_count=1475 bounds: 1<=t<=100, 1<=a3<=1000
qpolynomial_candidate_count=539
scheme_feasible_candidate_count=539
```

Thus 936 arithmetically basic candidates fail the completed $Q$-polynomial/association-scheme feasibility checks. The finite bounds and the fact that feasibility is only necessary remain important limitations.

## Active-time ledger (continued)

- 2026-08-11T16:11:13Z — resumed after reconciling the completed enumeration output; cumulative active minutes: 17.

### 2026-08-11T16:16:00Z — exact-array literature reconciliation

- The maintained Q-polynomial diameter-3 parameter table marks several early arrays as nonexistent: `{19,12,5;1,4,15}` (Coolsaet–Jurišić), `{17,8,6;1,2,12}` (BCN theorem), and `{35,24,8;1,6,28}` (Jurišić–Vidali). It also marks `{69,56,10;1,14,60}` as a 2-SRG case, but its older `?` status is superseded by the explicit 2019 paper below.
- Makhnev–Isakova–Nirova, *Distance-regular graphs with intersection array `{69,56,10;1,14,60}`, `{74,54,15;1,9,60}` and `{119,100,15;1,20,105}` do not exist*, Siberian Electronic Mathematical Reports 16 (2019), 1254–1259, DOI / record: `https://www.mathnet.ru/php/archive.phtml?jrnid=semr&option_lang=eng&paperid=1127&wshow=paper`. This eliminates the first and third named arrays despite their passing elementary association-scheme feasibility.
- Exact searches for `{35,27,6;1,9,30}` did not locate a direct diameter-3 citation. Its distance-3 graph would have parameters `srg(162,21,0,3)`. Makhnev–Nosov, *On automorphisms of strongly regular graphs with λ=0 and μ=3*, Algebra i Analiz 21 (2009) / St. Petersburg Math. J. 21 (2010), states that this SRG parameter set passes all known necessary conditions and studies hypothetical automorphisms; it does not construct the graph.
- A current distance-regular-graph survey lists the related bipartite diameter-4 array `{36,35,27,6;1,9,30,36}` as nonexistent because `Γ1 ∪ Γ4` would be an `srg(324,57,0,12)`, which is known not to exist. I have not yet proved that a graph with our diameter-3 array would produce that bipartite graph, so this is a lead rather than an elimination.

All literature statements above are status evidence, not outputs of my computation. The exact source searches returned no direct construction or nonexistence proof for `{35,27,6;1,9,30}`.

### 2026-08-11T16:21:00Z — closed-neighborhood bipartite lift eliminates `{35,27,6;1,9,30}`

Suppose a distance-regular graph $\Gamma$ had this array. Put $N=A_0+A_1$, and form the bipartite incidence graph $B$ whose two colour classes are copies of $V\Gamma$, with $x^+$ adjacent to $y^-$ iff $y=x$ or $y\sim_\Gamma x$. Define candidate distance matrices

```text
R0=A0, R1=A0+A1, R2=A1+A2, R3=A2+A3, R4=A3,
```

using `R_i` on diagonal or off-diagonal blocks according to parity. Exact multiplication in the Bose–Mesner algebra gives

```text
N R0 = R1
N R1 = 36 R0 + 9 R2
N R2 = 35 R1 + 30 R3
N R3 = 27 R2 + 36 R4
N R4 = 6 R3.
```

Therefore these are indeed the distance matrices of a connected bipartite distance-regular graph with array `{36,35,27,6;1,9,30,36}`. (The positive recurrence coefficients also establish the claimed distance layers, rather than merely formal closure.)

Reproducible calculation: `scratch/closed_neighborhood_bipartite_lift.g`, GAP 4.12.1; observed output in `scratch/closed_neighborhood_bipartite_lift.out`, exit code 0. The complete output is:

```text
IA={35,27,6;1,9,30} a=[0,7,20,5]
N*R0=[ 1, 1, 0, 0 ]
N*R1=[ 36, 9, 9, 0 ]
N*R2=[ 35, 35, 30, 30 ]
N*R3=[ 0, 27, 27, 36 ]
N*R4=[ 0, 0, 6, 6 ]
recurrence: N R0=R1; N R1=36R0+9R2; N R2=35R1+30R3; N R3=27R2+36R4; N R4=6R3
bipartite_lift_IA={36,35,27,6;1,9,30,36}
```

The target array is consequently impossible: van Dam–Koolen–Tanaka, *Distance-regular graphs*, Electronic Journal of Combinatorics Dynamic Survey DS22, §17.3.2, lists the lifted array as nonexistent. Their footnote reduces its existence to an `srg(324,57,0,12)`. Independent primary citations for the latter nonexistence include Kaski–Östergård, *There are exactly five biplanes with k=11*, J. Combin. Designs 16 (2008), 117–127, DOI `10.1002/jcd.20145`, whose abstract explicitly states this implication; and Gavrilyuk–Makhnev, *On Krein graphs without triangles* (2005).

This is a rigorous reduction to published nonexistence, but it eliminates only one intersection array and does not solve Problem 21.90.

### 2026-08-11T16:25:00Z — absolute-bound correction supersedes the Hoffman–Singleton search

I added the standard absolute bound to `scratch/enumerate_parameter_candidates.g`: for every pair $E_i,E_j$, the sum of multiplicities in the nonzero Krein support is at most $m_i m_j$ if $i\ne j$, and at most $m_i(m_i+1)/2$ if $i=j$. Final observed counts are now:

```text
candidate_count=1475 bounds: 1<=t<=100, 1<=a3<=1000
scheme_feasible_candidate_count=539
absolute_bound_feasible_candidate_count=538
qpolynomial_candidate_count=538
```

The unique newly rejected array is the smallest one, `{14,10,3;1,5,12}`:

```text
ABSOLUTE_BOUND_FAIL t=2 a3=2 c2=5 IA={14,10,3;1,5,12} v=50
  pair=[ 2, 2 ] lhs=43 rhs=28 support=[ 1, 3, 4 ]
```

Here GAP indices are one-based. The relevant primitive idempotent has multiplicity 7, while its Schur square has Krein support of total multiplicity $1+28+14=43>7\cdot8/2=28$. Thus the array is already infeasible by a standard theorem. The Hoffman–Singleton coclique computation remains an independent conditional obstruction but is no longer the primary or cheapest argument.

The earlier log line reporting 539 Q-polynomial candidates is therefore also intermediate: 539 pass intersection/Krein nonnegativity, but only 538 pass the added absolute bound in the stated finite box.

### 2026-08-11T16:30:00Z — smallest remaining live parameter line

After removing `{14,10,3;1,5,12}` by the absolute bound; `{19,12,5;1,4,15}`, `{17,8,6;1,2,12}`, and `{35,24,8;1,6,28}` by table citations; `{35,27,6;1,9,30}` by the bipartite lift; and `{69,56,10;1,14,60}` by Makhnev–Isakova–Nirova, the smallest survivor in my enumeration is apparently

```text
{39,25,10;1,5,30}, v=300.
```

`scratch/early_candidate_distance_srg_parameters.g` computes association-scheme intersection numbers exactly for early survivors. Observed output for this array:

```text
G2=[300,195,130,120] G3=[300,65,10,15]
```

The SRG database at DistanceRegular.org identifies an existing `srg(300,65,10,15)` as the $NO_5^{-\perp}(5)$ graph. Therefore nonexistence of the constituent SRG cannot eliminate the array; the live issue is whether that SRG admits the required 3-class fission with a 39-regular distance-1 relation. I asked Math Expert for a standard construction and literature status. Exact-array web searches found no direct result.

Other early outputs recorded by the same script (necessary constituents only, not graph constructions):

```text
{77,60,13;1,12,65}: G2=(540,385,280,260), G3=(540,77,4,12)
{19,6,8;1,1,12}: G2=(210,114,63,60), G3=(210,76,26,28)
{87,66,16;1,11,72}: G2=(726,522,381,360), G3=(726,116,10,20)
{119,96,18;1,16,102}: G2=(960,714,538,510), G3=(960,126,6,18)
```

These computations prove only the parameters forced if the association scheme exists.

### 2026-08-11T16:42:14Z — exact 300-vertex constituent and symmetry screen

The database download was inaccessible from the sandbox (`curl: (6) Could not resolve host`), so I constructed the exact polar graph directly rather than fabricating or approximating data. `scratch/construct_perpno_5_5.g` enumerates the 1-spaces of $\mathbb F_5^5$ in normalized coordinates for

$$Q(x)=x_1x_2+x_3x_4+x_5^2,$$

takes the 300 nonsquare-type points, and joins perpendicular points using the polar form. Exact all-pair checks and GRAPE/nauty output:

```text
projective_points=781 Q_counts=[156,163,150,150,162]
type_size=325 degrees=[60] common_counts=[10,15]
type_size=300 degrees=[65] common_counts=[10,15]
minus_perp aut_order=9360000 vertex_orbit=300 stabilizer_orbit_sizes=[1,65,104,130]
derived_order=4680000 stabilizer_orbit_sizes=[1,65,104,130]
```

Thus the 300-point graph is exactly an `srg(300,65,10,15)` with the database's stated full automorphism-group order. A 39-regular relation cannot be invariant under the full group or its index-two derived subgroup, since neither point stabilizer has suborbits summing to 39. This rules out only fissions preserving either of those large groups; an asymmetric or lower-symmetry fission remains possible.

I attempted `MaximalSubgroupClassReps(aut)` under the exact bounded command `timeout 50s gap -q scratch/construct_perpno_5_5.g`. It reached the verified outputs above but timed out before returning maximal-subgroup classes; observed exit code `124`. No result from the unfinished subgroup enumeration is asserted. The process was stopped at the preset bound and no heavy-compute lease threshold was crossed.

### 2026-08-11T16:42:14Z — Validator replies processed

- Validator accepts the absolute-bound violation as the primary elimination of `{14,10,3;1,5,12}` and directs that the 504,000-isomorphism search remain corroborative only.
- Validator independently confirms the closed-neighborhood bipartite lift and the Kaski–Östergård citation, hence validates the rigorous elimination of `{35,27,6;1,9,30}`.
- Validator states that any eventual existence witness needs canonical adjacency data and a separate checker for simplicity, connectedness, diameter 3, distance-regularity, the Q-polynomial ordering, and both SRG predicates.
- All three messages were marked `done` and moved to the bus archive.

## Active-time ledger (continued)

- 2026-08-11T16:42:14Z — constituent construction, symmetry screen, and Validator processing complete; cumulative active minutes: 49.

## One-hour checkpoint

### 2026-08-11T22:26:36Z

- Current approach: **300-vertex polar-graph fission via subgroup orbitals** for the smallest apparently unresolved array `{39,25,10;1,5,30}`.
- Evidence produced: exact local construction of the forced `srg(300,65,10,15)` constituent; verified full automorphism group of order 9,360,000; full group and derived subgroup ruled out because their point-suborbit sizes `[1,65,104,130]` cannot yield a 39-regular invariant relation. Separately, Validator confirmed two rigorous low-array eliminations.
- Next test: with a one-hour extension and an approved compute lease, enumerate conjugacy classes of transitive subgroups of `Aut(NO_5^{-\perp}(5))`, reject every subgroup whose non-diagonal suborbit sizes cannot sum to 39, and test any surviving orbital unions against the complete target intersection table.
- Kill criterion: abandon the symmetry line if no transitive subgroup admits a 39-valent orbital union, or if every such union fails one required intersection number. This would rule out all vertex-transitive realizations over this constituent, not asymmetric realizations.

The first bounded maximal-subgroup computation timed out at 50 seconds (exit 124) and produced no subgroup-class result. It therefore requires a leased slot rather than repeated unleased attempts.

## Cycle-1 report

### 2026-08-11T22:26:36Z — `REPORT: PROMISING`

The assignment's wall-clock `SAFETY_STOP_UTC=2026-08-11T18:49:23Z` has elapsed, so I stop now despite unused active-minute budget.

1. **Named approach:** 300-vertex polar-graph fission via transitive-subgroup orbitals.
2. **Specific one-hour next step:** obtain a compute lease; finish transitive maximal-subgroup/subgroup enumeration for the exact GRAPE graph in `scratch/construct_perpno_5_5.g`; enumerate all 39-valent orbital unions and check the full association-scheme intersection numbers for `{39,25,10;1,5,30}`.
3. **Reason it may produce something:** the forced distance-3 graph is an explicit, unique rank-4 `srg(300,65,10,15)`, and the two largest natural symmetry groups are already excluded. The finite subgroup/orbital test can either find an explicit candidate relation or certify nonexistence of every vertex-transitive realization supported by this constituent.
4. **Abandon criterion:** no transitive subgroup has suborbits summing to 39, or every 39-valent union violates a target intersection number. In that event the method is exhausted; asymmetric fissions would require a SAT/ILP formulation and an installed solver.

Validated partial results from this cycle:

- `{14,10,3;1,5,12}` fails the absolute bound (`43>28`); the Hoffman–Singleton search is corroborative only.
- `{35,27,6;1,9,30}` would lift to a bipartite distance-regular graph with array `{36,35,27,6;1,9,30,36}`, hence would imply the nonexistent `srg(324,57,0,12)`. Validator independently accepted the calculation and citation.
- The bounded necessary-condition enumeration has 538 absolute-bound-feasible Q-polynomial arrays for `1<=t<=100`, `1<=a3<=1000`; this is neither exhaustive without bounds nor existence evidence.

Honest status: Problem 21.90 is not solved. No explicit target graph was found. Cumulative active research time is approximately 59 minutes; wall-clock waiting and stopped-process time were excluded.

## Cycle 1 resumed — slot 3

### 2026-08-11T22:34:31Z — inbox and dependency/lease check

- Read own inbox first. Lead authorized continuation of cycle 1 using the unused active budget and heavy-compute slot 3 through `2026-08-11T23:30:40Z`; no extension was granted.
- Marked the Lead message `done` and moved it to the archive.
- Roster evidence (read-only): `active_minutes_used: 59`, `compute_slot: 3`, `compute_expires_utc: 2026-08-11T23:30:40Z`, new safety stop equal to the lease expiry.
- GAP 4.12.1, GRAPE 4.9.0, and nauty remained available through the exact construction script.

### 2026-08-11T22:44:24Z — exact bounded subgroup-orbital result

The first resumed implementation attempted to enumerate all subsets of 47 eligible edge orbitals and was stopped after live output exposed the exponential materialization. It produced no terminal result and is not evidence. A second recursive version also terminated without an exit record while on the same class, so it too is excluded from the certificate.

The final implementation uses the necessary linear identity

$$A_1A_3=10A_2+9A_3$$

during exact subset backtracking, checked only on point-stabilizer-orbit representatives (sufficient by transitivity). It retains the quadratic target identity

$$A_1^2=34I+8A_1+5J-5A_3$$

for any linear survivor. Exact final command and observed exit:

```text
timeout 35m gap -q Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5.g \
  > Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5_slot3.out \
  2> Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5_slot3.stderr
exit_code=0
```

Observed final summary:

```text
tom_classes=307 iso_fail=false
derived_transitive_classes=5 derived_target_hits=0 two_150_classes=3 runtime_ms=668
outer_extensions_tested=3 outer_transitive=3 outer_target_hits=0
total_vertex_transitive_hits=0 total_runtime_ms=749
```

Completeness scope: if a transitive `H <= Aut(A3)` and `D=Aut(A3)'` has index two, then `H∩D` is transitive or has two 150-point orbits. The complete `S4(5)` table of marks supplies all classes in the first case and the three possible `150+150` classes in the second. For the second case, the script enumerates every outer involution in `N_G(H∩D)/(H∩D)` and tests the resulting transitive extension. No valency-39 orbital union passes the linear identity.

Conclusion submitted for validation: no vertex-transitive realization of `{39,25,10;1,5,30}` exists with the standard polar `NO_5^{-\perp}(5)` graph as `Γ3`. Asymmetric fissions remain completely unresolved, as do realizations based on a nonisomorphic `srg(300,65,10,15)`.

### 2026-08-11T22:44:24Z — Math Expert replies

- Math Expert confirms the standard polar model is the appropriate exact object and independently emphasizes that orbital failure excludes vertex-transitive cases only.
- Math Expert reports a genuine convention ambiguity: the printed problem does not say “nontrivial” or “primitive” strongly regular, so literal definitions allowing disconnected SRGs make `H(3,2)` a witness. The intended Makhnev–Nirova variant likely excludes it, but context cannot silently change the quantifiers.
- Both messages were marked `done` and archived.

## Active-time ledger (continued)

- 2026-08-11T22:44:24Z — slot-3 exact test complete and replies processed; cumulative active minutes: 69.
