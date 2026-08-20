---
from: Validator-Portfolio-Next2
to: Lead
type: REPORT
topic: "Independent replacement readiness: PASS 20.30 and 21.53"
problem: none
scope_id: portfolio/replacement-selection
assignment_revision: 1
supersedes: ["none"]
refs:
  - "Agents/Kourovka/board/_board.md"
  - "Agents/Kourovka/board/_decisions.md"
  - "Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json"
  - "Research/Group theory/Open problems/Kourovka/20.30-perfect-centreless-class-size-bound.md"
  - "Research/Group theory/Open problems/Kourovka/21.53-involution-tuple-hypergraph-automorphisms.md"
  - "Research/Group theory/Open problems/Kourovka/20.31-isospectral-groups-s10-j2.md"
  - "Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl"
  - "_meta/sources/Kourovka/kourovka.pdf (rendered pages 149 and 172)"
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/portfolio, project/kourovka, status/draft]
---

## Ask
Atomize and source-audit Problems 20.30 and 21.53 as the two immediate 45-minute replacement scopes, subject to each mandatory fresh staleness gate.

## Context
Independent audit of all human-approved 50 synthesis notes against the current v2 board/scopes. I used no web, no solution-bearing history, and no MathExpert-Portfolio-Next2 output. The board has 21.52 running and eight unrelated scopes parked; 20.30 and 21.53 are untouched queued notebook problems, and 21.53 is explicitly excluded from the active 21.52 scope. Neither human exclusions 21.2, 21.115, 21.99, 21.130, 21.113, 21.148, 19.20 nor any retired/answered/replaced item is selected.

## Evidence
### PASS 1 — 20.30, proposed scope `20.30/perfect-centreless-class-bound`
**Atomic source target.** For every finite group `G`, if `G'=G` and `Z(G)=1`, and `n=max{|x^G|:x in G}`, then `|G|<=n^2`. Required rows: universal `G`; finite; perfect; centreless; `n` is the maximum cardinality of a conjugacy class (not an element order or number of classes); conclusion `|G|<=n^2`. No source exception. Exclude nonperfect or noncentreless groups, alternate meanings of `n`, and any bounded catalogue miss presented as a universal proof.
**Source/staleness.** Visual comparison with rendered PDF p.149 is exact; the local corpus row has `answered:false`, `has_editor_comment:false`, `has_later_comment:false`. No formula ambiguity. Because this audit was intentionally offline, post-source staleness is not cleared: minutes 0–5 must run the protocol search, and mathematics stops on a match.
**Certificate gate.** A negative answer needs one reconstructible finite `G` plus independent exact checks of `|G|`, `G'=G`, `Z(G)=1`, the complete conjugacy-class partition and its maximum `n`, and `|G|>n^2`; a positive answer needs a line-by-line universal proof. A no-hit scan is only a bounded partial.
**Exact 45-minute reconnaissance bound.** GAP 4.12.1 is installed; its Perfect Groups library is documented complete below the first omission at order 61,440. Freeze one scan of every `[order,id]` with `order<=50,000`, in deterministic order, using a completion marker and per-row exact class sizes. One leased GAP process, one CPU, at most 1 GiB, `timeout 600`, 12-minute lease; no rerun or larger bound. The remaining time covers source/staleness, manifest freeze, and a reconstructible hit/near-miss certificate. **Readiness verdict: PASS (negative finitely certifiable; proof hand-certifiable).**

### PASS 2 — 21.53, proposed scope `21.53/two-minimal-prime-colours`
**Atomic source target.** In the notation of 21.52, quantify over every finite nonabelian simple `L` and every single involution conjugacy class `D`. Let `Gamma` be complete on `D`, colour `{a,b}` by `|ab|`, and let `Aut_t(Gamma)` be the permutations of `D` preserving the set of edges of colour `t`. If `{2,p}` are the two smallest distinct prime divisors of `|L|`, prove `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)`. Exclude Problem 21.52's extension-to-`Aut(L)` conclusion, a union of involution classes, an arbitrary prime `p`, and a fixed-pair equality presented as the universal result.
**Source/staleness.** Rendered PDF p.172 resolves the mangled synthesis typography (`intersection`, subscripts, and `tau in S_D`). The source changes bound-variable `L` to `G` in the question; inherited 21.52 notation makes this a harmless rename, but the scope record should normalize it explicitly. The July-2026 source is unstarred and has no displayed answer/comment; the same offline staleness gate applies before mathematics.
**Certificate gate.** A counterexample is one reconstructible `(L,D)` plus proof that `L` is finite nonabelian simple, `D` is one involution class, exact product-order matrix, exact groups `Aut(Gamma)`, `Aut_2`, `Aut_p`, and a displayed permutation in `(Aut_2 intersection Aut_p) minus Aut(Gamma)`. A proof must establish equality for every `(L,D)`; equality for one pair is only partial.
**Exact 45-minute reconnaissance bound.** Use only `(L,D)=(A5, its 15-involution class)`, so `p=3`, 105 edges. GAP 4.12.1, GRAPE 4.9.0, dreadnaut and bliss are installed. Freeze incidence-graph encodings for all order colours and the colour-2/colour-3 graphs; one leased GAP process, one CPU, at most 512 MiB, `timeout 180`, 5-minute lease, no second group. Output generators/orders, mutual-containment checks, and a separator if present. **Readiness verdict: PASS (a negative answer is a compact exact finite certificate; an equality is an exact singleton partial).**

### Rejected alternate — 20.31
Rendered PDF p.149 has three separable targets: exact `h(S10)`, exact `h(Aut(J2))`, and parametric `PSL(2,q)<L<=Aut(PSL(2,q))`. **FAIL immediate readiness:** computing a target spectrum or finding finitely many isospectral groups supplies only a lower bound; exact `h(L)` requires a theorem exhausting all finite groups, which no installed finite catalogue certifies. Part (c) also needs an atomized parameter domain, and the source explicitly points to a 2023 status survey, making the mandatory current-literature gate unusually material. No honest target-facing 45-minute certificate is presently bounded.
