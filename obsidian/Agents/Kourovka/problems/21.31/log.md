---
title: "Kourovka 21.31 problem-agent log"
problem_id: "21.31"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/holomorphs
  - project/kourovka
  - status/draft
---

# Problem 21.31 working log

## Active-time ledger

- 2026-08-11T15:49:23Z — work start; cumulative active minutes: 0.
- 2026-08-12T17:00:56Z — resumed work on Lead dispatch; cumulative active minutes: 7.
- 2026-08-13T16:47:56Z — resumed work on Lead's index-8 design dispatch; cumulative active minutes: 12.
- 2026-08-13T18:17:36Z — cycle continuation start; cumulative active minutes: 22; continuation budget: 60 active minutes.
- 2026-08-14T10:25:19Z — extension start; cumulative active minutes: 37; extension budget: 60 active minutes.
- 2026-08-14T12:25:34Z — corrected extension start; cumulative active minutes: 46; budget: 45 active minutes.
- 2026-08-14T12:35:32Z — diagram-restriction extension start; cumulative active minutes: 49; budget: 35 active minutes.

## Source transcription

2026-08-11T15:50:02Z — Read `_meta/agents/Kourovka/_common-kourovka.md`, the synthesis note, the (empty) problem inbox, and checked that the configured PDF resolves. Extracted PDF p. 169 with `pdftotext -f 169 -l 169 -layout "$KOUROVKA_PDF" -`, then rendered that page at 160 dpi with `pdftoppm` and visually inspected the rendered image.

Corrected transcription, checked word-for-word against the rendered page:

> **21.31. Conjecture:** If \(N\) is a finite soluble group, then any regular subgroup in the holomorph \(\operatorname{Hol}(N)\) of \(N\) is also soluble. — N. Byott

`source_transcription_checked: yes`

In my own words: for every finite soluble group \(N\), every subgroup \(G\leq \operatorname{Hol}(N)=N\rtimes\operatorname{Aut}(N)\) whose natural action on the underlying set of \(N\) is regular (free and transitive, hence \(|G|=|N|\)) must be soluble. A counterexample would therefore be a pair of finite groups \((G,N)\) of the same order with \(N\) soluble, \(G\) insoluble, and an embedding \(G\hookrightarrow\operatorname{Hol}(N)\) whose image acts regularly on \(N\).

## Staleness check

2026-08-11T15:50:28Z — The available machine-readable corpus is the 2022 issue-20 corpus and contains no record for the new issue-21 problem, so its `answered`, `has_editor_comment`, and `has_later_comment` JSON flags are unavailable. The authoritative No. 21 PDF prints 21.31 unstarred, with no editor comment and no later comment attached; operationally: `answered: false`, `has_editor_comment: false`, `has_later_comment: false` as read from the rendered source.

Searches performed on 2026-08-11:

- exact web searches for `"Kourovka 21.31"` and `"Problem 21.31" "Kourovka" Byott`;
- proposer/key-term searches for `N. Byott regular subgroup holomorph soluble group conjecture` and `site:arxiv.org regular subgroup holomorph soluble Byott`;
- follow-up searches for `"Conjecture 1.1" "finite soluble group" holomorph regular subgroup`, `"insoluble regular subgroup" "soluble group" holomorph 2024 2025 2026`, and citation-oriented variants.

Result: no complete solution or counterexample found. The current No. 21 PDF still lists the conjecture. The principal directly relevant source is N. P. Byott, *On insoluble transitive subgroups in the holomorph of a finite soluble group*, J. Algebra 638 (2024), 1–31, DOI 10.1016/j.jalgebra.2023.10.001, arXiv:2205.13464. Its abstract and introduction explicitly treat the statement as Conjecture 1.1 and give restrictions rather than a solution. It records prior computational exclusion of counterexamples for \(|N|\leq 2000\) by C. Tsang and C. Qin, *On the solvability of regular subgroups in the holomorph of a finite solvable group*, arXiv:1901.10636. Searches also found 2025–2026 talks/project material continuing to cite Byott's restriction result, not a closure of the conjecture. Negative result: no post-No. 21 paper claiming to prove or disprove this exact conjecture was located in these searches.

2026-08-11T15:51Z — Sent an early `QUESTION` to Math Expert asking for the sharpest tractable attack based on Byott's restriction theorem; continued working without waiting.

## Structural attack: sharpen the first possible order

2026-08-11T15:52Z — Read the March 22, 2026 revision of arXiv:2205.13464 through its HTML rendering. The relevant exact results are stronger than the older abstract snippet: Theorem 3.2(i) says that in a *minimal* counterexample every maximal normal subgroup of \(N\) has index 2 and \(G\) has a soluble normal subgroup \(K\) with \(G/K\cong\mathrm{GL}_3(2)\) of order 168; Corollary 3.3 says every counterexample has the simple group of order 168 as a subquotient of \(G\). Since a regular \(G\) has \(|G|=|N|\), every counterexample order is divisible by 168. Together with Tsang–Qin's exhaustive exclusion through 2000, the first arithmetically possible order is 2016 (=168·12). This is only a lower-bound observation, not a new result.

2026-08-11T15:53Z — Checked the SmallGroups coverage and toolchain. Exact command/output:

```text
$ timeout 30s gap -q
GAP_VERSION=4.12.1
gap> SmallGroupsInformation(2016);
The groups of size 2016 are not available.
```

Neither `magma` nor `sage` is installed. This prevents a direct reproduction/extension of Tsang–Qin's all-groups-of-order-\(n\) algorithm at \(n=2016\), but it does not block the current structural route.

### Conditional order-2016 reduction

Suppose the least counterexample has order 2016. By Byott Theorem 3.2(i), \(G\) has a soluble normal subgroup \(K\) of order \(2016/168=12\) with \(G/K\cong T:=\mathrm{GL}_3(2)\). In fact \(K=R(G)\), the soluble radical: \(K\le R(G)\), while the image of \(R(G)\) in the simple insoluble quotient \(G/K\) is a soluble normal subgroup and hence trivial, giving \(R(G)\le K\).

Conjugation induces \(T=G/R\to\operatorname{Out}(R)\). I enumerated all five groups \(R\) of order 12 using `scratch/order12_radicals.g`. Exact command and observed output:

```text
$ timeout 30s gap -q 'Agents/Kourovka/problems/21.31/scratch/order12_radicals.g'
GAP_VERSION=4.12.1
NUMBER_SMALL_GROUPS_12=5
id=[ 12, 1 ] structure=C3 : C4 center=2 aut=12 inn=6 out=
2 out_divisible_by_168=false
id=[ 12, 2 ] structure=C12 center=12 aut=4 inn=1 out=
4 out_divisible_by_168=false
id=[ 12, 3 ] structure=A4 center=1 aut=24 inn=12 out=
2 out_divisible_by_168=false
id=[ 12, 4 ] structure=D12 center=2 aut=12 inn=6 out=
2 out_divisible_by_168=false
id=[ 12, 5 ] structure=C6 x C2 center=12 aut=12 inn=1 out=
12 out_divisible_by_168=false
```

Thus no \(\operatorname{Out}(R)\) contains an image isomorphic to \(T\). Since \(T\) is simple, its map to \(\operatorname{Out}(R)\) is trivial. Therefore \(G=R C_G(R)\), and with \(C=C_G(R)\),

\[
C\trianglelefteq G,\qquad C\cap R=Z(R),\qquad C/Z(R)\cong T,
\]

so \(G\) is the central product of its order-12 soluble radical with an insoluble normal subgroup \(C\) of order \(168|Z(R)|\). This is a conditional structural reduction only. It neither constructs nor excludes a regular embedding into the holomorph of a soluble group of order 2016.

### Exact enumeration of the forced order-252 stabiliser

2026-08-11T15:55Z — Let \(M\) be the maximal \(G\)-invariant normal subgroup used in Byott's proof. At order 2016, \(N/M\cong C_2^3\), so \(|M|=252\). For the regular action, \(H=M_*\) acts regularly on \(M\), has order 252, contains \(K=R(G)\) normally, and \(H/K\) is the point stabiliser of order 21 in \(T\)'s transitive degree-8 action, hence \(C_7:C_3\).

GAP 4.12.1 reports 46 groups of order 252. The bounded script `scratch/order252_stabilisers.g` exhaustively checked all of them for normal subgroups \(K\) of order 12 with quotient `SmallGroup(21,1) = C7 : C3`. Exact observed output:

```text
GAP_VERSION=4.12.1
NUMBER_SMALL_GROUPS_252=46
TARGET_21_ID=[ 21, 1 ] TARGET_21_STRUCTURE=C7 : C3
Syntax warning: Unbound global variable in Agents/Kourovka/problems/21.31/scra\
tch/order252_stabilisers.g:11
             K -> Size(K)=12 and IdGroup(FactorGroup(H,K))=IdGroup(target));
                                                     ^
H_id=[ 252, 2 ] H_structure=C4 x (C7 : C9) matching_normal_K=1 K_ids=
[ [ 12, 2 ] ]
H_id=[ 252, 9 ] H_structure=C2 x C2 x (C7 : C9) matching_normal_K=1 K_ids=
[ [ 12, 5 ] ]
H_id=[ 252, 11 ] H_structure=(C2 x C2) : (C7 : C9) matching_normal_K=1 K_ids=
[ [ 12, 5 ] ]
H_id=[ 252, 17 ] H_structure=(C3 : C4) x (C7 : C3) matching_normal_K=1 K_ids=
[ [ 12, 1 ] ]
H_id=[ 252, 19 ] H_structure=C12 x (C7 : C3) matching_normal_K=1 K_ids=
[ [ 12, 2 ] ]
H_id=[ 252, 27 ] H_structure=A4 x (C7 : C3) matching_normal_K=1 K_ids=
[ [ 12, 3 ] ]
H_id=[ 252, 29 ] H_structure=C2 x (S3 x (C7 : C3)) matching_normal_K=1 K_ids=
[ [ 12, 4 ] ]
H_id=[ 252, 38 ] H_structure=C2 x C6 x (C7 : C3) matching_normal_K=1 K_ids=
[ [ 12, 5 ] ]
H_id=[ 252, 40 ] H_structure=C3 x ((C14 x C2) : C3) matching_normal_K=1 K_ids=
[ [ 12, 5 ] ]
MATCHING_H_GROUPS=9
MATCHING_HK_PAIRS=9
```

The warning is GAP's static warning about the enclosing loop variable in the closure, not a runtime error; the run completed. The exact conclusion is only that these nine pairs are necessary at order 2016. The computation does not test whether any \(H\) embeds regularly in \(\operatorname{Hol}(M)\), whether it lifts to a group \(N\) of order 2016, or whether the resulting full \(G\) is regular in \(\operatorname{Hol}(N)\).

2026-08-11T15:56Z — Work stop for conditional reduction claim; cumulative active minutes: 7. The research budget is not exhausted. Further mathematics is paused for Validator review because the current deliverable is a `CLAIM` under verification, not a claimed solution.

## Cycle 1 resumption: order-252 holomorph feasibility

2026-08-12T17:00:56Z — Read four inbox messages oldest-first. Validator independently reproduced both finite enumerations and retained the overall reduction at `status/conjectured`; Math Expert recommended testing the nine candidate \(H\)-types for regular embeddings in holomorphs of groups \(M\) of order 252; Lead dispatched exactly that test, with a compute lease required only after an exact capped design.

2026-08-12T17:02Z — Initial GAP capability check (exact observed output):

```text
GAP_VERSION=4.12.1
PACKAGES=[ "autpgrp", "smallgrp", "transgrp" ]
REGULAR_SUBGROUPS_BOUND=false
REGULAR_SUBGROUP_CLASSES_BOUND=false
ALL_BIJECTIVE_1COCYCLES_BOUND=false
```

Thus the installed GAP session exposes no direct regular-subgroup or bijective-1-cocycle routine. Before treating this as a missing-tool blocker, I am checking installed-but-unloaded packages and whether a standard GAP primitive supports a bounded exact formulation.

2026-08-12T17:03Z — Found that core GAP supplies `AllHomomorphismClasses`, `ComplementClassesRepresentatives`, and `OneCocycles`; the Polycyclic package is installed. Designed the exact action/complement formulation: for each \(H,M\), enumerate homomorphism classes \(f:H\to\operatorname{Aut}(M)\); in \(E=M\rtimes_f H\), enumerate complement classes to \(M\); a complement \(C\) is a regular subgroup of \(\operatorname{Hol}(M)\) precisely when it has trivial intersection with the canonical copy of \(H\), since its orbit of the basepoint has size \(|C:C\cap H|=252\). Script: `scratch/regular_pair_probe.g`.

A capped probe for \((H,M)=([252,2],[252,1])\) completed in 12.254 s. It enumerated 42 action classes and found 56 complement-class representatives passing the regularity test. Exact output included nine action classes with regular counts 4, 12, 4, 6, 6, 6, 6, 6, 6. This demonstrates feasibility for an individual pair but is not a count modulo full holomorph conjugacy and is not needed for the decisive observation below.

2026-08-12T17:05Z — **The dispatched order-252 existence test is complete but non-discriminating.** Every one of the nine candidate groups \(H\) is itself soluble of order 252. Taking \(M=H\), the canonical translation copy of \(H\) in \(\operatorname{Hol}(H)\) is regular. The already identified eligible normal subgroup \(K\trianglelefteq H\) is retained unchanged. Hence all nine pairs necessarily pass the requested existence test; no heavy computation or compute lease is warranted.

I checked all nine canonical witnesses with `scratch/nine_translation_witnesses.g`. Exact command:

```bash
timeout 30s gap -q 'Agents/Kourovka/problems/21.31/scratch/nine_translation_witnesses.g'
```

For each of the nine pairs it observed: `K_MATCHES=1`, `M_ID=H_ID`, `M_SOLUBLE=true`, `TRANSLATION_IMAGE_ORDER=252`, `DEGREE=252`, `TRANSITIVE=true`, and `STABILIZER_ORDER=1`. The full output is reproducible from the saved script; the only diagnostic was GAP's static closure-variable syntax warning, and the run completed normally.

What this proves: each abstract \((H,K)\) pair satisfies the isolated necessary condition “there exists a soluble order-252 \(M\) with a regular embedding \(H\hookrightarrow\operatorname{Hol}(M)\), retaining \(K\).” What it does not prove: that this \(M\) is the invariant subgroup inside any compatible order-2016 \(N\), or that the regular embedding extends through the index-8 lift. The missing compatibility/lift data are exactly where any discriminatory test must operate.

2026-08-12T17:05:53Z — work stop after Lead dispatch; cumulative active minutes: 12. No compute lease requested because the exact test completed under 30 s and, structurally, all nine cases pass canonically.

## Index-8 compatibility design and first exact filter

2026-08-13T16:47:56Z — Processed Lead's request. The full compatibility object consists of extensions \(1\to M\to N\to C_2^3\to1\) and \(1\to H\to G\to C_2^3\to1\), with \(N\) soluble; \(K=R(G)\), \(G/K\cong\mathrm{GL}_3(2)\), and \(H/K\) the order-21 point stabiliser; and a homomorphism \(\theta:G\to\operatorname{Aut}(N)\) with a bijective crossed map \(\pi:G\to N\), where \(\pi(H)=M\) and the induced coset map is the natural equivariant bijection. A positive exact certificate must give explicit groups and maps and exhaustively verify these predicates. A negative certificate must exhaust a proved-complete finite list of extension/action/cohomology classes.

2026-08-13T16:55Z — Derived a cheaper necessary condition. Since \(G=K C_G(K)\) and \(H\) is the inverse image of the point stabiliser in \(G/K\), writing \(h=kc\) shows \(c=k^{-1}h\in H\). Hence

\[
H=K C_H(K). \tag{*}
\]

This genuinely uses compatibility with the index-8 overgroup. Ran the complete bounded script `scratch/index8_group_side_filter.g`:

```bash
timeout 30s gap -q 'Agents/Kourovka/problems/21.31/scratch/index8_group_side_filter.g'
```

The seven passing pairs have \(|K C_H(K)|=252\). The two failures are:

```text
H_ID=[252,11] K_ID=[12,5] |C_H(K)|=84 |K C_H(K)|=84
H_ID=[252,40] K_ID=[12,5] |C_H(K)|=84 |K C_H(K)|=84
```

Thus `[252,11]` and `[252,40]` cannot be the forced subgroup \(H\). The saved verbatim output records all nine cases and the run completed in 1.8 seconds.

The smallest successor test is overgroup-first: for each of the seven survivors, enumerate extension classes \(1\to K\to G\to\mathrm{GL}_3(2)\to1\) whose restriction over the fixed order-21 point stabiliser is the given \(1\to K\to H\to P\to1\), and require \(R(G)=K\). Only surviving overgroups should enter the much larger \(N,\theta,\pi\) enumeration. No lease was requested because the present filter was lightweight and the successor universe is not yet proved complete or sized.

2026-08-13T16:58:24Z — work stop for Validator review; cumulative active minutes: 22.

## Continuation: verified five-pair refinement and overgroup universe

2026-08-13T18:17:36Z — Read both Validator verdicts. Validator independently reproduced the centraliser filter, then verified the stronger universal central-pullback argument: the preimage over \(P=C_7:C_3\) splits, so \(H\cong K\times P\). This additionally eliminates `[252,2]` and `[252,9]`. The verified conditional survivor list is now `[252,17]`, `[252,19]`, `[252,27]`, `[252,29]`, `[252,38]`, corresponding respectively to all five order-12 groups \(K\).

### Predeclared extension/action falsifiers

Before computation, the proposed overgroup classification is:

1. Because \(G=K C_G(K)\), with \(C_G(K)/Z(K)\cong T=\mathrm{GL}_3(2)\), the overgroup is the central product of \(K\) with a central extension of \(T\) by \(Z(K)\).
2. Since \(T\) is perfect with Schur multiplier \(C_2\), equivalence classes with fixed kernel are parametrized by homomorphisms \(C_2\to Z(K)\). Up to automorphisms of \(K\), these are the orbits on \(Z(K)[2]\).
3. Falsifiers: a center whose 2-torsion has more automorphism orbits than predicted; a resulting group not of order 2016; a resulting soluble radical not isomorphic to the prescribed \(K\); or two inequivalent extension orbits missed by the construction. Passing only produces a complete necessary \(G\)-side universe; it does not establish any action on a soluble \(N\) or any bijective crossed map.

The next action compatibility condition common to every lift is also predeclared: for a regular embedding represented by \((\pi,\theta)\), \(\ker\theta\) is soluble because \(\pi\) restricts to a group embedding of \(\ker\theta\) into soluble \(N\). Hence \(\ker\theta\le R(G)=K\), so the automorphism image \(\theta(G)\le\operatorname{Aut}(N)\) must retain the unique nonabelian composition factor \(T\). Any candidate \(N\) whose automorphism group lacks a \(T\) section is therefore impossible. This is exact but cannot yet be enumerated because the installed SmallGroups library lacks order 2016.

2026-08-13T18:25Z — GAP 4.12.1 confirmed `SchurCover(T)` has order 336 and structure `SL(2,7)`. For the five radicals, the exact center-2-torsion orbit data are:

```text
K=[12,1] C3:C4   Z=C2     |Z[2]|=2  Aut(K)-orbits=2
K=[12,2] C12     Z=C12    |Z[2]|=2  Aut(K)-orbits=2
K=[12,3] A4      Z=1      |Z[2]|=1  Aut(K)-orbits=1
K=[12,4] D12     Z=C2     |Z[2]|=2  Aut(K)-orbits=2
K=[12,5] C6xC2   Z=C6xC2  |Z[2]|=4  Aut(K)-orbits=2 (sizes 1,3)
```

Therefore there are exactly **nine distinguished overgroup-extension orbits** \((G,K)\): one split class \(K\times T\) for every \(K\), and one nonsplit Schur-pushout class for every \(K\ne A_4\). For `C6 x C2`, its three nonidentity involutions form one automorphism orbit, so they give only one distinguished isomorphism class.

Construction formula for the nonsplit class, giving an exact certificate without an order-2016 library, is

\[
G_z=(K\times \mathrm{SL}_2(7))/\langle(z,s)\rangle,
\]

where \(s\) is the central involution of \(\mathrm{SL}_2(7)\) and \(z\) represents the unique nontrivial `Aut(K)`-orbit in \(Z(K)[2]\). Its order is \(12\cdot336/2=2016\), its quotient by the embedded \(K\) is \(T\), and its soluble radical is exactly \(K\) by the same simple-quotient argument already verified. The split and first nonsplit constructions for `[12,1]`, and the split construction for `[12,2]`, were explicitly built before a 30-second cap expired; each reported order 2016. The attempted all-nine construction was too slow because GAP's pc factor-group conversion dominated, so no unobserved construction outputs are claimed. The complete classification rests on the cohomological parameterization plus the fully observed orbit calculation, not on those partial constructions.

### Sharpened action compatibility

The induced quotient action supplies more than “\(T\) is a section of \(\operatorname{Aut}(N)\).” Let

\[
\Theta:G\longrightarrow\operatorname{Aut}(N)\longrightarrow\operatorname{Aut}(N/M)=\mathrm{GL}_3(2).
\]

In Byott's quotient, the induced affine image \(G/K=T\) is faithful and transitive on \(V=N/M\), with stabiliser \(H/K=P\). Thus **\(\ker\Theta=K\)** and the descended linear part, together with the descended crossed map, must be the exceptional transitive affine realization of \(T\) on eight points. Consequently any proposed extension \(N\) must admit a lift of this fixed outer action of \(T\) on \(V\), and the obstruction/restriction test must be performed before enumerating crossed maps.

Smallest next finite certificate for each of the nine \((G,K)\) classes and five \(M=K\times P\) types:

1. enumerate extension classes \(1\to M\to N\to V\to1\) together with lifts of the fixed affine \(T\)-action on \(V\);
2. reject unless the pullback automorphism action \(G\to\operatorname{Aut}(N)\) has quotient kernel exactly \(K\) and restricts on \(H\) compatibly with some regular crossed map \(H\to M\);
3. only then enumerate the remaining crossed-map classes and test bijectivity.

Predeclared falsifier for this next stage: any extension/action class satisfying the lift and restriction conditions survives; failure of a search without a completeness proof is not a negative certificate. No heavy job was started and no lease was requested.

2026-08-13T18:32Z — work stop; continuation cumulative active minutes: 15/60 (overall recorded active minutes: 37).

## Extension: completeness gate for the N-side parameterization

2026-08-14T10:25:19Z — Incorporated Validator's verdict: exactly nine conditional pair-isomorphism classes \((G,K)\), and the quotient linear action has kernel exactly \(K\).

### BLOCKER — five H-types are not five M-types

The dispatch calls the five verified order-252 groups “\(M=K\times(C_7:C_3)\).” The verified result actually proves \(H=M_*\cong K\times(C_7:C_3)\), where \(H\) is the multiplicative index-8 subgroup. It does not prove that the additive normal subgroup \(M\trianglelefteq N\) is isomorphic to \(H\). The established relation is only a regular embedding \(H\hookrightarrow\operatorname{Hol}(M)\); regular subgroups of a holomorph need not be isomorphic to the underlying group.

Thus a complete universe must start with all pairs \((M,b)\), where \(|M|=252\) and \(b=(r_H,c_H)\) is regular crossed data from one of the five \(H\)-types to \(M\), modulo `Aut(H) x Aut(M)`. Restricting \(M\) to the five H-types requires a missing theorem.

Light falsifier probe: tested surviving `H=[252,17]` against nonisomorphic `M=[252,1]`. The exact homomorphism/complement method exhausted 42 action classes in 15.531 seconds and observed `REGULAR_CLASSES_TOTAL=0`. This one negative pair cannot establish the missing theorem. The predeclared falsifier for the five-M restriction is any surviving \(H\) regularly embedded in a nonisomorphic \(M\).

### Correct complete marked parameterization, if all eligible M are authorized

For each verified \((G,K)\), put \(H=q_G^{-1}(P)\), and fix the verified affine data \((\lambda,\beta)\) for \(T\) on \(V=C_2^3\). A complete marked tuple has four layers:

1. an order-252 group \(M\) and regular crossed datum \((r_H,c_H)\), with \(r_H:H\to\operatorname{Aut}(M)\), bijective \(c_H:H\to M\), and the crossed identity;
2. an abstract kernel \(\alpha:V\to\operatorname{Out}(M)\). Its Teichmüller obstruction in \(H^3(V,Z(M)_\alpha)\) must vanish; if so, marked extensions \(1\to M\to N\to V\to1\) form a torsor under \(H^2(V,Z(M)_\alpha)\);
3. an action lift \(r:G\to\operatorname{Aut}(N)\) inducing \(\lambda q_G\) on \(V\), restricting to \(r_H\) on \(H\), and having quotient-action kernel \(K\);
4. a crossed-map lift \(c:G\to N\) with \(q_Nc=\beta q_G\), \(c|_H=c_H\), the crossed identity for \(r\), and bijectivity.

Marked tuples are equivalent under isomorphisms of \(G\) and \(N\) preserving \(K,H,M\), inducing the fixed \(T,P,V\) data up to simultaneous conjugacy, and transporting \(r,c\). Unmarked enumeration quotients further by the corresponding automorphism groups. This separates outer actions, `H^3/H^2` extension classes, action lifts, and crossed maps.

Completeness falsifier: a compatible target embedding whose induced tuple is absent, or two equivalent tuples counted separately. Failure of a search without exhausting all eligible \((H,M)\) regular data is not a negative certificate.

2026-08-14T10:34Z — work stopped on the scope/completeness blocker; extension active minutes: 9/60; overall cumulative active minutes: 46.

## Corrected extension: marked inclusions and regular-pair benchmark

2026-08-14T12:25:34Z — Read Validator's restriction-filter verdict and Lead's corrected assignment. All 46 additive groups remain in scope. The atomic data are simultaneous marked tuples; regular embeddings may not be quotiented by all of `Aut(H)` independently of the inclusion.

### Marked-inclusion orbit gate

Fix one of the nine verified marked quotient maps \(q:G\twoheadrightarrow T\), with kernel \(K\), and the conjugacy class of point stabilisers \(P<T\) in the fixed degree-8 affine realization. There is exactly one inclusion orbit \(H=q^{-1}(P)<G\) under automorphisms of the marked quotient diagram allowing simultaneous inner conjugacy on \(T\): if \(P'=tPt^{-1}\), choose any \(g\in q^{-1}(t)\). Then the inner automorphism \(c_g\) preserves \(K\), satisfies \(q c_g=c_t q\), and maps \(q^{-1}(P)\) onto \(q^{-1}(P')\). Thus the single conjugacy class of \(P\) does lift without changing the marked extension class.

This does **not** authorize quotienting embeddings by all of `Aut(H)`. For a fixed representative define the exact allowed group

\[
A_i=\operatorname{im}\bigl(\operatorname{Aut}(G,K,q,P)\to\operatorname{Aut}(H)\bigr),
\]

where an automorphism of the diagram may induce an allowed automorphism of \(T\) stabilizing \(P\). Regular embeddings must be orbited simultaneously by \(A_i\times\operatorname{Aut}(M)\). Computing generators for these nine \(A_i\) is required by the eventual certificate; replacing \(A_i\) by `Aut(H)` is unsound.

### Exact complement correspondence and equivalence

For a homomorphism \(\lambda:H\to\operatorname{Aut}(M)\), put \(E_\lambda=M\rtimes_\lambda H\). Crossed maps \(c:H\to M\) correspond bijectively to complements \(C_c=\{(c(h),h):h\in H\}\) of \(M\) in \(E_\lambda\). The induced holomorph embedding is regular exactly when \(C_c\cap H_0=1\), where \(H_0\) is the canonical complement: this is simultaneously trivial point stabilizer and faithfulness, and orders then give transitivity.

GAP's `AllHomomorphismClasses(H,Aut(M))` returns representatives up to `Aut(M)`-conjugacy. `ComplementClassesRepresentatives(E,M)` returns representatives up to full `E`-conjugacy. Neither list alone is the desired orbit list: the latter may identify crossed maps by translations and inner automorphisms, while the final equivalence is the simultaneous action

\[
(a,u)\cdot(c,\lambda)=
\bigl(u\,c\,a^{-1},\;u\lambda(a^{-1}(-))u^{-1}\bigr),
\qquad (a,u)\in A_i\times\operatorname{Aut}(M).
\]

A complete implementation must either expand complement conjugacy classes back to all graphs before taking these orbits, or use the complement stabilizer/transporter data to compute the same double-orbit set without expansion. It must retain transporters between `Aut(M)`-conjugate action representatives for exact restriction matching.

### Cheap filters and benchmarks

Necessary prefilters recorded before complement enumeration:

- \(|\lambda(H)|\mid\gcd(252,|\operatorname{Aut}(M)|)\), and the image order must be an actual quotient order of \(H\);
- \(\ker\lambda\) must embed in \(M\), since the crossed map restricts to an injective homomorphism on the kernel;
- element orders required by each candidate image and kernel must occur in `Aut(M)` and `M`, respectively;
- for trivial \(\lambda\), bijectivity forces \(H\cong M\), giving an immediate zero otherwise.

The cheapest order-divisibility filter was weak: for `[252,17]`, `[252,19]`, and `[252,27]`, every one of the 46 M-types retained at least one nontrivial possible quotient order before the 20-second capped script reached its timeout. No eliminations are claimed.

Observed stratified probes using `scratch/regular_pair_probe.g`:

```text
H=[252,17], M=[252,6], |Aut(M)|=72:
  72 homomorphism classes; hom stage 0.026 s; full complement stage 6.794 s;
  regular classes reported by the coarse E-conjugacy probe: 0.

H=[252,17], M=[252,1], |Aut(M)|=252:
  42 homomorphism classes; hom stage 12.601 s; total 15.531 s;
  regular classes reported: 0.

H=[252,27], M=[252,11], |Aut(M)|=1512:
  did not finish the homomorphism stage within 20 s; capped, no count.
```

These are feasibility timings only: the current probe uses GAP's coarse complement conjugacy and does not compute final simultaneous marked orbits. A sample timeout is not a negative result.

### Resumable complete design and cost bound

There are 230 base `(H,M)` pairs, then embeddings attach to the one or two marked overgroups having that H-type. A resumable driver should checkpoint independently by `(H_ID,M_ID,kernel_ID,image_subgroup_class,action_class)`, saving explicit maps, transporters, complement stabilizers, final orbit representatives, version, deterministic seed, completion sentinel, and hashes. Restart skips only sentinel-complete strata.

With a 60-second per-base-pair cap, the mechanical outer bound is 13,800 CPU seconds (3.83 CPU-hours) merely to classify action/complement strata, before the nine `A_i` transporter/orbit calculations. Observed runtimes range from 6.8 s to >20 s. Therefore a complete run does not fit the present 45-minute extension, and no honest global cost below the heavy threshold is supportable.

Kill criteria for a future leased pilot: stop if any completed stratum exceeds 60 s, RSS exceeds 1 GB, an action class produces more than 100,000 complements before orbit compression, or the first 20 stratified base pairs project above four CPU-hours. A lease request is premature until the nine `A_i` groups and a transporter-preserving driver exist; running the present coarse probe at scale could not produce a complete certificate.

2026-08-14T12:28:09Z — work stop for marked-inclusion claim review; corrected-extension active minutes: 3/45; overall cumulative active minutes: 49.

## Explicit diagram-restriction groups A_i

2026-08-14T12:35:32Z — Incorporated Validator's verdict: one inclusion orbit per quotient block is verified; raw ambient complement conjugacy remains too coarse. Lead requested explicit \(A_i\) for all nine blocks.

### Predeclared falsifiers

For the extension class represented by \(z\in Z(K)[2]\), I predicted

\[
A_i\cong \operatorname{Stab}_{\operatorname{Aut}(K)}(z)
       \times \operatorname{Aut}(P),\qquad P=C_7:C_3.
\]

Falsifiers were: an additional derivation/twist factor; an automorphism of \(T\) stabilizing \(P\) that does not lift; an allowed \(K\)-automorphism not stabilizing \(z\); a computed size different from the product; or a constructed generator that is not bijective on concrete \(H=K\times P\).

### Exhaustion proof

Let \(e_z\in H^2(T,Z(K))\cong Z(K)[2]\) be the marked extension class. A compatible diagram automorphism inducing \((a,\tau)\in\operatorname{Aut}(K)\times\operatorname{Aut}(T)\) exists exactly when \(a_*(e_z)=\tau^*(e_z)\). `Aut(T)` acts trivially on the multiplier \(C_2\), so this condition is exactly \(a(z)=z\). The kernel of the map from diagram automorphisms to such pairs is \(H^1(T,Z(K))=\operatorname{Hom}(T,Z(K))=0\), since \(T\) is perfect. Hence compatible lifts are unique and all arise this way.

The stabilizer of an order-21 point subgroup \(P\) in `Aut(T)` has order \(336/8=42\). Its restriction to \(P\) is faithful: an automorphism centralizing \(P\) centralizes its normal \(C_7\) and its complement \(C_3\), giving the identity. Since \(|\operatorname{Aut}(P)|=42\), restriction identifies this stabilizer with all of \(\operatorname{Aut}(P)\cong C_7:C_6\).

In the nonsplit Schur-pushout model, the preimage of \(P\) in `SL(2,7)` is \(C_2\times P\), and its complement to the central \(C_2\) is unique because `Hom(P,C2)=0`. Thus restriction introduces no central twist. The induced action on the concrete product \(H=K\times P\) is exactly \((k,p)\mapsto(a(k),b(p))\). This proves both the product formula and exhaustion.

### Exact nine groups and concrete actions

`scratch/diagram_restriction_groups.g` constructs generator maps on each concrete `SmallGroup(252,hid)` product representative by extending generators of the allowed subgroup of `Aut(K)` trivially across \(P\), and generators of `Aut(P)` trivially across \(K\). Every generated mapping passed `IsBijective`. Script SHA-256:

```text
ff67ac795feeb0519df5c76d96096deccfe8b1f2b8965e77fdb4aa9d92765793
```

Complete table:

| K | G class | H | allowed K factor | A_i order | generators |
|---|---|---|---|---:|---:|
| `[12,1]` | split | `[252,17]` | `D12` (12) | 504 | 6 |
| `[12,1]` | nonsplit | `[252,17]` | `D12` (12) | 504 | 6 |
| `[12,2]` | split | `[252,19]` | `C2 x C2` (4) | 168 | 5 |
| `[12,2]` | nonsplit | `[252,19]` | `C2 x C2` (4) | 168 | 5 |
| `[12,3]` | split | `[252,27]` | `S4` (24) | 1008 | 7 |
| `[12,4]` | split | `[252,29]` | `D12` (12) | 504 | 6 |
| `[12,4]` | nonsplit | `[252,29]` | `D12` (12) | 504 | 6 |
| `[12,5]` | split | `[252,38]` | `D12` (12) | 504 | 8 |
| `[12,5]` | nonsplit | `[252,38]` | `C2 x C2` (4) | 168 | 5 |

The only split/nonsplit difference in \(A_i\) occurs for `K=[12,5]=C6 x C2`: its three nonzero central involutions form one `Aut(K)` orbit, so a chosen nonsplit class has stabilizer of order 4 rather than 12. Static GAP warnings concerned loop-variable lexical analysis; both optimized evidentiary runs reached `RUN_COMPLETE=true` and exit code 0.

What this establishes: the exact groups and concrete generator actions required by the later simultaneous orbit driver. What it does not establish: any regular-embedding orbit, restriction-map survivor/failure, compatible additive extension \(N\), or target solution.

2026-08-14T12:38:31Z — work stop for Validator review; extension active minutes: 3/35; overall cumulative active minutes: 52.

## Corrected regular-pair dispatch — safety stop

2026-08-14T12:10:46Z — Read Lead's corrected dispatch and Math Expert's restriction-map design. Lead withdrew the invalid five-\(M\) premise and authorized the complete universe: five verified multiplicative \(H\)-types, all 46 additive groups \(M\) of order 252, complete regular-embedding representatives, and nine compatible overgroups.

The assigned safety stop was `2026-08-14T12:06:11Z`. The authoritative `kv_now` value on receipt was `2026-08-14T12:10:46Z`, already 4 minutes 35 seconds past the process cap. Per protocol, no mathematical probe, script modification, enumeration, or lease request was started. Active extension time charged for this expired dispatch: 0 minutes; overall cumulative active minutes remain 46.

The next authorized task, if respawned with a fresh cap, is precisely the restriction-map design in `ideas/2026-08-14-restriction-map-lift-filter.md`: prove completeness of regular-pair representatives modulo `Aut(H) x Aut(M)`, then test whether each automorphism component lies in the restriction image from each compatible overgroup, modulo `Aut(M)` conjugacy and automorphisms of the marked pair \(H<G\).
