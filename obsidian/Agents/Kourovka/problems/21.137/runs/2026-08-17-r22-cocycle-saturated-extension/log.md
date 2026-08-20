---
title: "Kourovka 21.137 r22 — cocycle-saturated extension"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
strategy: COCYCLE-SATURATED-EXTENSION
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Run log

## Active-time ledger

- Start: 2026-08-17T18:40:57Z; cumulative active minute 525.

## Source and scope gate

- Source PDF page 184 was extracted and rendered at 150 dpi, then visually inspected.
- Corrected active clause: for an odd prime \(p\), if the actual set
  \(P=\{g^p:g\in G\}\) in a finite \(p\)-group of exact exponent \(p^2\)
  is a subgroup, must \(P\) be abelian?
- `source_transcription_checked: yes`; the rendered exponent is \(p^2\).
- `active_scope_checked: yes`; revision 2 selects only the odd-prime clause.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- Mandatory target rows for a counterexample: \(p=3\); finite 3-group; exact
  exponent 9; literal cube-value set, not its generated subgroup; literal set
  closed as a subgroup; that subgroup nonabelian.

## Reviewed facts retained

- Any admissible counterexample has class at least 5 at \(p=3\).
- In its first lower-central quotient with nonabelian cube image, the cube image
  has order at least \(3^5\), and the ambient group has order at least \(3^6\).
- For a product root \(z^3=AB\), the convention-safe action identity is
  \(D^3(x)=[x,q]\), equivalently \(D^3=-\operatorname{ad}_q\) for the
  standard left adjoint.

## Strategy portfolio

1. **Structured construction (selected):** one complete cyclic extension
   \(1\to P\to G\to C_3\to1\) with a class-two exponent-three nonabelian
   kernel \(P\), specified by an automorphism \(\alpha\) and a lift-cube
   element \(q\). Derive the multiplication and every cube value, then impose
   surjectivity of each coset norm onto \(P\). This is the cheapest carrier in
   which literal saturation can be stated exactly.
2. **Theoretical obstruction:** prove that the norm fibres in every such cyclic
   extension lie in a commuting subgroup. This would exclude the whole frozen
   carrier, not the unrestricted target.
3. **Catalogue mode:** after a finite coefficient system is frozen and Lead
   leases it, enumerate its exact roots. A miss proves only exclusion of the
   frozen carrier.
4. **Certificate plan:** give the full pair multiplication, associativity
   conditions, closed cube formula for all three quotient cosets, exact
   exponent criterion, and either a hand all-root obstruction or a manifest
   whose rows are independently reconstructible.

## Lead correction and first-gate pivot — 2026-08-17T18:44:57Z

- Charged interval: cumulative minutes 525--529.
- Lead stopped the cyclic-quotient carrier: the reviewed cyclic-root-coset
  theorem already makes its cube values commute. The proposed requirement that
  one coset norm be surjective was also stronger than literal saturation and is
  withdrawn.
- The correct condition is the union condition
  \(P=\bigcup_{u\in G/P}\operatorname{Image}(C_u)\), equivalently (because
  every cube already lies in \(P\)) coverage by all root-coset cube maps.
- Reviewed quotient-minimal bounds force more than the merely noncyclic
  \(C_3^2\) pilot: the first equality layer \(|P|=3^5\), \(|G/P|=3^4\)
  was already screened. The frozen next carrier is therefore
  \(P=H_3(3)\times C_3^3\) and \(G/P=A=C_3^5\), so \(|G|=3^{11}\).
  This is the first adjacent elementary quotient carrier beyond that screened
  equality layer, and it has 121 independent projective root directions.
- Full equations and the union-of-images condition are frozen in
  `scratch/carrier-equations.md`. No computation has been run.

## Exact family exclusion — 2026-08-17T18:54:06Z

- For the frozen carrier \(P=H_3(3)\times C_3^3\), \(A=C_3^5\), the
  full action equations force all cube values to commute.
- If the induced action of \(A\) on \(P/Z(P)\cong\mathbb F_3^2\) is
  nontrivial, conjugacy invariance makes every coset's constant cube label lie
  in the one-dimensional common fixed space.
- If that action is trivial, the center-action identities
  \(R^3=0\), \(R^2L=J_q\), together with outer commutation, force any two
  nonzero cube labels \(q,q'\) to satisfy \(q'=bq\) for
  \(b\in\mathbb F_3^\times\).
- Hence every cube label lies on one line, and the determinant commutator law
  in \(H_3(3)\times C_3^3\) makes all actual cubes commute. This excludes
  every elementary-abelian quotient rank, not only rank five.
- Outcome: `PARTIAL_RESULT` (complete carrier-family exclusion),
  `active_assignment_answered: no`. The exact remaining frontier at this
  kernel layer is a nonabelian exponent-three quotient; other kernels remain
  open.
- No mathematical computation was run, so no compute manifest or lease was
  used.
- Stop: 2026-08-17T18:54:06Z; cumulative active minute 538. Thirteen minutes
  charged; 47 minutes of this increment returned unused. State:
  `awaiting_lead`.
