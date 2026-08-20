---
title: "Kourovka 21.31 — restriction-map lift filter before additive extensions"
problem: "21.31"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/holomorphs
  - project/kourovka
  - status/conjectured
---

# Restriction-map lift filter

## Obstruction

The present obstruction is a wrong reformulation followed by a complexity wall. The five groups (H=K\times(C_7:C_3)) are multiplicative stabilisers, whereas the additive kernel (M\trianglelefteq N) is only known to have order (252). Replacing (M) by (H) discards the regular-embedding data that carry the brace/holomorph compatibility.

Cited: Byott, *On insoluble transitive subgroups in the holomorph of a finite soluble group*, J. Algebra 638 (2024), Lemma 2.4, says that for a regular (G\leq\operatorname{Hol}(N)), the subgroup (H=M_*) acts regularly on (M). It does not identify the abstract groups (H) and (M).

## Ranked idea 1 — extend the automorphism component first

**Idea.** For each of the five verified (H)-types, each soluble order-252 group (M), and each conjugacy class of regular embeddings

\[
\beta_H=(\pi_H,\lambda_H):H\hookrightarrow\operatorname{Hol}(M),
\]

test whether (lambda_H:H\to\operatorname{Aut}(M)) lies in the image of the restriction map

\[
\operatorname{Hom}(G,\operatorname{Aut}(M))\longrightarrow
\operatorname{Hom}(H,\operatorname{Aut}(M))
\]

for either compatible verified overgroup (H<G). Quotient by simultaneous (operatorname{Aut}(M))-conjugacy and pair automorphisms preserving (H<G).

**Why it might work.** General knowledge, unverified: in any target realization, the automorphism component of (G\hookrightarrow\operatorname{Hol}(N)) restricts to automorphisms of the (G)-invariant subgroup (M); its restriction to (H=M_*) is exactly the automorphism component of the regular embedding of (H) in (operatorname{Hol}(M)). Thus failure to extend (lambda_H) is a necessary obstruction before choosing any extension (N).

**Falsifier.** A single regular pair ((H,M,\beta_H)) for which both relevant (G)-classes admit extensions of (lambda_H) shows that this filter does not eliminate that pair. If every sampled regular embedding for the first (M)-type extends, stop and move to the equivariant extension-class condition rather than expanding the search blindly.

**Finite certificate design.** Enumerate the 46 library groups (M) of order 252 only after regular embeddings are represented by a proved-complete homomorphism/complement parameterization. For each representative, solve the finite generator-relation extension problem for (lambda_G), and output either an explicit map or the exhausted finite candidate list. This is not an enumeration of order-2016 groups.

**Cost.** Design and one light pilot: 1–2 hours in GAP; no heavy slot until the number of regular-embedding representatives is measured.

**Self-critique.** The restriction map may be too permissive: (lambda_G) can extend even when no compatible (N), affine cocycle, or bijective crossed map exists. Regular embeddings themselves may already be numerous, so completeness—not the homomorphism equations—is the likely bottleneck.

## Ranked idea 2 — equivariant nonabelian extension stack

**Idea.** Only after idea 1 survives, classify (1\to M\to N\to V\to1), (V=C_2^3), by outer actions (ho:V\to\operatorname{Out}(M)), obstruction classes, and extension classes, while imposing equivariance under a chosen (lambda_G) inducing the fixed (T=GL_3(2)) action on (V). Then solve for a crossed map extending (pi_H).

**Why it might work.** General knowledge, unverified: nonabelian extension theory separates an outer action, its obstruction in degree three, and a torsor of degree-two classes; automorphisms lifting the fixed (T)-action select fixed/equivariant classes. Characteristic subgroups of (M) may give cheap quotient obstructions because every automorphism of (M) preserves them.

**Falsifier.** For one surviving ((G,H,M,\beta_H,\lambda_G)), construct an equivariant extension class and compatible bijective crossed map. That kills any proposed nonexistence shortcut for that class and supplies a target candidate for Validator.

**Finite certificate design.** Record: the exact outer action up to (operatorname{Aut}(M)\times GL(V)); the explicit obstruction cocycle; all equivariant degree-two representatives; presentations for (N); and exhaustive crossed-map equations with an injectivity/bijectivity check. Each pruning step must state its complete input universe.

**Cost.** Potentially heavy and unsuitable until idea 1 has sharply reduced the regular-pair list.

**Self-critique.** For nonabelian (M), ordinary module cohomology alone is insufficient. Treating (H^2(V,Z(M))) without first fixing the outer action and its obstruction would silently omit extensions; the equivariance also involves the actual lifted (G)-action, not merely abstract (T).

## Recommendation

Rank idea 1 first. It is the earliest exact compatibility condition that uses the nine-overgroup classification and avoids the unjustified identification (M\cong H). Idea 2 is the complete downstream framework, not yet a tractable computation.
