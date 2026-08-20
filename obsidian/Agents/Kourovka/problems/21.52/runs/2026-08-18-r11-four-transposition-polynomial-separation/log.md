---
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 11
direction: proof
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/draft
---

# Cycle 11 log — four-transposition polynomial separation

## 2026-08-18T05:30:58Z — active work start, cumulative minute 164

Fresh-context run. I read the common protocol, problem-agent protocol, canonical
revision-1 scope, Lead roster, current synthesis/source note, and the sole unread
binding decision. I did not inspect historical problem logs, findings,
verification notes, archived messages, or scratch output from the preceding
four-transposition lane. Its unreviewed reduction and finite samples are not
premises here.

## Source and staleness gate

The configured PDF resolves. I rendered PDF page 172 to PNG and visually checked
the full statement (not merely `pdftotext`). Corrected transcription:

> Let `L` be a finite non-abelian simple group and `D` a conjugacy class of
> involutions in `L`. On the complete graph `Gamma` with vertex set `D`, declare
> edges `(a,b)` and `(c,d)` equivalent exactly when `|ab|=|cd|`. A coloured-graph
> automorphism is a permutation `tau` of `D` preserving this equivalence for
> every edge. Is `Aut(Gamma)` a subgroup of `Aut(L)`?

The statement is unstarred and contains no editor or later comment. The available
repository corpus ends at issue 20, so there is no issue-21 JSONL flag row; the
current PDF itself is issue 21 (2026). Because the canonical scope has
`blind_run.enabled: true`, I made no open-web or solution-bearing-history search:
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
`source_transcription_checked: yes`; `active_scope_checked: yes`.

Clause matrix:

| source clause | equivalent formulation | active? | literature status in blind run |
|---|---|---:|---|
| finite nonabelian simple `L`; one involution conjugacy class `D` | quantified admissible pair `(L,D)` | yes | deferred |
| complete graph on `D`; colour iff exact orders agree | full order-coloured complete graph, not selected colours | yes | deferred |
| `tau in S_D` preserves every edge colour | `|ab|=|a^tau b^tau|` for all distinct `a,b` | yes | deferred |
| `Aut(Gamma) <= Aut(L)` | every such `tau` is the restriction of an automorphism stabilizing `D` | yes | deferred |
| Problem 21.53 | selected-colour intersection question | no | excluded |

Constraint checklist (all seven canonical IDs):

| constraint_id | role in this family lane |
|---|---|
| `21.52-forall-L-D` | The universal quantifier is not claimed; this lane can only yield an infinite-family partial. |
| `21.52-L-finite-nonabelian-simple` | Here `L=A_n`, and the intended range `n>=14` is finite, nonabelian, and simple. |
| `21.52-D-single-involution-class` | `D` is the single `A_n` class of cycle type `2^4 1^(n-8)`; its elements have order 2. |
| `21.52-Gamma-complete-on-D` | Every unordered pair of distinct four-matchings is an edge. |
| `21.52-edge-colour-exact-product-order` | Every coordinate is computed from the exact permutation order `|xy|`, never product conjugacy class. |
| `21.52-tau-preserves-all-edge-colours` | The proposed reconstruction may use all exact-order two-point common-neighbour counts, which any such `tau` preserves. |
| `21.52-tau-induced-by-AutL` | Family target: recover a point permutation in `S_n=Aut(A_n)` (for `n>=14`) inducing `tau`; this remains only a partial toward the universal row. |

Excluded throughout: Problem 21.53, unions of involution classes, the uncoloured
complete graph, product-conjugacy-class colouring, and any bounded/family result
described as a universal solution.

## Strategy portfolio

1. **Finite local symbolic enumeration (chosen).** Classify the two-coloured union
   of two four-matchings, enumerate a third four-matching only on the finite union
   support plus `j<=8` labelled external vertices, and emit coefficients of
   `binom(n-m,j)`. Search every common-edge/no-common-edge signature pair for an
   exact coordinate whose difference has one sign in the `binom(n-14,j)` basis.
2. **Theoretical reconstruction.** If the common-edge relation is intrinsic,
   recover individual transpositions as the unique largest cliques in the
   intersection graph of four-matchings, recover disjointness of transpositions
   from star intersections, and then recover points from the line graph of `K_n`.
3. **Catalogue/small-case probe.** Directly enumerate `D` only for a small `n` as a
   checker of the symbolic coefficients, never as the proof of a uniform claim.
4. **Alternative certificate.** If coefficientwise sign fails, factor each degree
   at most eight difference over `Q` and combine exact integer-root isolation with
   a rigorous Cauchy/Fujiwara bound beyond 14.

Certificate plan: save source, compiler command/version, complete signature
inventory and representatives, every binomial coefficient array, every opposite-
status pair and its selected coordinate, transformed `binom(n-14,j)` difference,
coverage totals, and internal direct-enumeration cross-checks. The designed run is
bounded and expected below 60 seconds, so no heavy-compute lease is needed.

## 2026-08-18T05:41:31Z — local enumeration and symbolic gate, cumulative minute 175

I derived pair signatures independently as follows. Regard a class element as a
four-edge matching. In the union of ordered matchings `X,Y`, each component is:

- `E`, an edge common to both;
- an alternating path `P_l` of `l` edges; or
- an alternating cycle `C_(2r)` of `2r` edges.

For an odd path the label records which matching supplies the extra edge (`X` or
`Y`); labels are canonicalized under the one global swap `X<->Y`, because the
endpoint pair is unordered. An `E` contributes order 1, `P_l` contributes order
`l+1`, and `C_(2r)` contributes order `r`, so `|XY|` is their least common
multiple. This follows by tracing `XY`: it is one `(l+1)`-cycle on a path and two
`r`-cycles on an alternating cycle.

The first bounded C++ run used source hash
`035a28a08f40c37dd50fa978cae1e73f5b419bd6b593aa73e82dd2769ed26e43`.
It stopped after 2.98 seconds at signature 6 with `coordinate symmetry failure`.
This exposed a modelling error in an internal assertion: an unordered signature
need not admit a point permutation swapping its two chosen representatives (for
example `C4+P1X+P3Y`), so oriented counts need not themselves be symmetric. I
discarded that partial 3,123-line output. The correct invariant is the explicitly
symmetrized coordinate
`M_{r,s}=N_{r,s}+N_{s,r}` for `r<s`, and `M_{r,r}=N_{r,r}`.

After removing only that false assertion and documenting downstream
symmetrization, the frozen source hash is
`08088dbf076e89d4502d1c0775bc8f738ede81c478cc1b2b87845ef9d3222814`.
Command (GCC 13.3.0):

```text
g++ -O3 -std=c++17 -Wall -Wextra -pedantic scratch/enumerate.cpp -o /tmp/p2152-enumerate
timeout 60s /tmp/p2152-enumerate > scratch/local-coefficients.tsv
```

The sole corrected invocation exited 0 in 9.39 seconds with maximum RSS 3,584
KiB. Output hash:
`3b11b3ecb6fbe71521be41e5fc64980238cc303360e84c5854c37911bd70b367`.
It found 54 unordered signatures: 22 containing `E`, 32 containing none. For
every signature `S` of support size `m` and every `j=0,...,8`, its internal total
equals exactly `105*binom(m,8-j)`; all 486 total rows pass. The 29,081 `C` rows
are the full nonzero oriented local coefficient data. Exact product orders seen
against a third matching are
`1,2,3,4,5,6,7,8,9,10,12,14,15,20,21,30`; order 1 rows are excluded from the
common-neighbour coordinates because they are precisely endpoint contributions.

An independent component-multiset enumerator, hash
`506ac72685ade629649f4150cf0129a0e43472002633b09787c72894bc656af9`,
reconstructed the signature list without enumerating point matchings and returned:

```text
signature_audit=PASS
signatures 54
common 22
no_common 32
```

For each symmetrized coordinate, `certify.py` (hash
`1c37c7097dfec51c78806f884265d90a5f7538b326ad3141a36006a93fad6ac6`)
converted

`M^S_{r,s}(n)=sum_(j=0)^8 a^S_{r,s,j} binom(n-m,j)`

to the common Newton basis

`M^S_{r,s}(n)=sum_(k=0)^8 b^S_{r,s,k} binom(n-14,k)`.

The output `scratch/separation-certificate.tsv`, hash
`9d4ea05e3c08affb6d686aefcf74a128eafaf1580ec92bbb4de8086bdcb108a4`,
contains the complete 54-row inventory, 5,568 nonzero coefficient-array rows,
and one `CERT` row for each of `22*32=704` opposite-status pairs. All 704 selected
differences are actually constant or affine in `n-14`: 674 have one nonzero
Newton coefficient and 30 have two. In every row `d_0` is strict and all `d_k`
have the same weak sign. Hence the named coordinate difference cannot vanish at
any integer `n>=14`, not merely at sampled degrees.

The standalone structural verifier (hash
`b90ecfdeb29dd154a1334abed450ba1db2161616acbdf63552f0df4dbcb1b85d`)
returned:

```text
certificate_verification=PASS
opposite_pairs 704
certificates 704
all_nonzero_for_every_integer_n_ge_14=yes
```

No run exceeded ten seconds or 4 MiB; no heavy-compute lease was needed.

## 2026-08-18T05:44:03Z — cycle outcome, cumulative minute 182

Timing correction: the assignment/spawn at `05:26:08Z`, rather than the later
first-log timestamp, was the true active-work start. I charge 18 active minutes,
bringing the scope ledger from 164 to 182. Active research now stops.

Outcome: `PARTIAL_RESULT`. The uniform symbolic gate succeeds: all 704
opposite-status signature pairs have a strict coefficientwise-sign separator for
every integer `n>=14`. Combining this with the maximum-clique reconstruction gives
a candidate theorem for the single `A_n` class `2^4 1^(n-8)`, every `n>=14`.
The proof and exact files are in `findings.md`; this remains an unvalidated
infinite-family partial and `active_assignment_answered: no` for the universal
Kourovka scope.
