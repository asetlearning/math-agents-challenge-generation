---
title: "Validator advice — Kourovka 21.137 structural-family certificate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
result: certifiable-in-principle
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# Certificate threshold

**Yes.** A gap-free proof for every qualifying group of class (<p), with the case of class at least (p) explicitly uncovered, is certifiable as a structural-family `PARTIAL_RESULT`. For odd (p), “class at most 2 or class (<p)” is just class (<p): the first family is contained in the second, including (p=3).

The proof package must include:

1. the exact theorem quantifiers: every odd prime, every finite (p)-group of exponent exactly (p^2), the actual value set (P=\{g^p:g\in G\}), and the hypothesis that this set is a subgroup;
2. the explicit step (P=G^p) from value-set closure, rather than silently replacing the value set by the verbal subgroup;
3. a fixed commutator convention and the exact Hall–Petrescu/collection identities used, with every error term displayed and killed by a named class, weight, exponent, or (p)-adic divisibility argument;
4. a separate audit of (p=3), where generic “odd-prime” divisibility shortcuts most often fail;
5. the final identity ([x^p,y^p]=1) for arbitrary (x,y\in G), not merely centrality modulo a lower-central term or checks on generators;
6. if a Lie/Lazard formulation is used, a proved correspondence in precisely the class-(<p), exponent-(p^2) range and a translation of group powers and brackets back to the asserted group identity;
7. a scope statement that class (ge p) remains open and that the full active assignment is not answered.

For class at most 2, the short calculation may be certified separately: state and prove the class-2 commutator power law and derive ([x^p,y^p]=[x,y]^{p^2}=1). A computation or a formula “modulo higher commutators” is insufficient unless completeness of the killed terms is proved.
