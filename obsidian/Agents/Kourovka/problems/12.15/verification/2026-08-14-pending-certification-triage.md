---
title: "Verification triage — Kourovka 12.15 — pending certification questions"
problem: 12.15
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Claims and questions

This triage covers, oldest first:

1. what evidence could certify a negative SmallGroups counterexample floor;
2. whether the proposed `d=6` order-512 exclusion proof is valid;
3. whether the central-Camina lifting lemma is valid and whether the `H^2(H,C2)` row screen is exhaustive;
4. the 15:44 isotropic-dichotomy request as expressly corrected at 15:47. Its coefficient-`C2` steps 2 and 3 are withdrawn and will not be certified.

# Target versus witnesses

- **Target:** rendered PDF page 58 asks whether every finite 2-group with the property “equal normal closures imply conjugacy” has abelian derived subgroup.
- **Bounded witness:** a finite collection of SmallGroups library objects through a stated order. This is not the universal target; a negative scan can establish only a bounded floor.
- **Structural witnesses:** hypothetical minimum counterexamples of order 512 and their quotients/extensions. These are conditional objects, not actual counterexamples.
- **Witness equals target:** false for every pending item. Each item is a bounded or conditional reduction, so the overall problem remains at most `status/conjectured`.

# Subclaims

1. The nonmetabelian filter cannot discard a counterexample, since a counterexample is defined by nonabelian `G'`.
2. Conjugacy-class representatives suffice for exact SMP testing because normal closure is constant on conjugacy classes.
3. The library loop and every order range are exhaustive and completed.
4. In the `d=6` proof, all group-theoretic reductions, the involutory isometry argument, total isotropy, and `im(alpha-1)=G'/Z` are valid.
5. The central-Camina hypothesis lifts exact SMP from `H` to a central extension `E`.
6. Commutator pairing with commuting base elements is linear in the class in `H^2(H,C2)`, and testing a basis plus generators of each centralizer is exhaustive.
7. The actual GAP implementation computes the intended cohomology space and rows without changing bases or silently omitting classes.
8. The corrected dichotomy retracts the implication from complex isotropy to splitting over `C2`; only explicitly elementary subfamilies may survive.

# Tools available

- GAP 4.12.1, Python 3.12.3, and `pdftotext` 24.02.0: available.
- SmallGrp 1.5.3 was observed earlier in this session; the cohomology routines used by the claimant are callable in the installed GAP environment but will be probed on replay.
- Sage, Magma, Lean: unavailable.
- PDF page 58 was extracted, rendered, and visually checked.

# Methods inventory

| Item | Method | What a pass proves | What a pass does not prove |
|---|---|---|---|
| Bounded floor | Independent GAP script using a separately written elementwise or class-fibre formulation; order-count and completion sentinels | `status/replicated` for the explicitly bounded library statement | The universal Kourovka assertion or coverage beyond the stated range |
| `d=6` lemma | Line-by-line hand proof plus small checks of `Aut(D8)` and `Aut(Q8)` facts | The conditional `d=6` branch is impossible | Existence/nonexistence in other branches |
| Lifting lemma | Direct normal-closure proof with every central/noncentral case split | Conditional inheritance of exact SMP | Existence of an extension satisfying central Camina |
| Cohomology obstruction | Linear-algebra proof and independent light replay on named bases, plus a positive control | Exhaustive obstruction within the computed `H^2(H,C2)` model | That every parent was selected correctly or that other coefficient modules are covered |
| Corrected dichotomy | Logical dependency audit; no global replay | Exact scope remaining after the retraction | Completeness of the original five-case claim |

# Hard limits and recommendation

No heavy enumeration is authorized. The order-256/512 catalogues and dimension-14 extension enumeration are outside this review. Give an advisory for the bounded floor; fully audit the hand lemmas; replay only light cohomology cases if they finish below 60 seconds. Treat the correction as a refutation of the withdrawn steps, not as evidence for the remaining global dichotomy.
