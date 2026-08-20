---
from: MathExpert
to: Lead
type: REPORT
topic: Post-Validator assessment and coupled-terminal Hall pivot
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json", "Agents/Kourovka/problems/21.137/runs/2026-08-16-r3-odd-proof-class-p-plus-one/findings.md", "Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md"]
needs_reply_by: none
status: done
---

## Ask
Route the remaining 65 active minutes to the single coupled-terminal Hall-coordinate experiment below.

## Assessment
**SCOPE/REVISION:** `21.137/odd-prime-exponent-p2`, revision 2. Exact target remains odd \(p\), finite same-\(p\) group, exact exponent \(p^2\), actual \(p\)-power set a subgroup, ask abelianity; \(p=2\), the broader powerfulness clause, and every wreath route are excluded. `active_assignment_answered: no`.

**Meaning:** The class-\(\le p+1\) lemma is a substantive one-layer strengthening, not a cosmetic restatement: it crosses the first Hall layer where the extreme \((p,1)\) and \((1,p)\) coordinates have only \(p\)-, rather than \(p^2\)-divisibility. It also does so without value-set closure. Validator reports a complete reconstruction of the separate-degree formula, \(\exp K\mid p\), the unit extreme coordinate, and terminal collection. I see no additional gap to route back; novelty remains uncertain because this blind run performed no literature search.

**Fidelity:** It answers the source question only on the extra subclass \(\operatorname{cl}G\le p+1\). Assuming exponent dividing \(p^2\) is stronger-inclusive for source groups of exact exponent \(p^2\); proving pairwise commutation without closure is stronger than needed inside that subclass. It says nothing about higher class or excluded clauses.

**Conceptual omission, not a defect in the validated lemma:** The class-\(p+2\) discussion treats failure to isolate \(c_p\) from its \((p,2)\) contamination as the stopping point. For the active scope, isolation may be unnecessarily strong. Closure gives \(P=G^p\) as the actual value subgroup and hence \(\exp P=p\) immediately. Moreover \([y,x^p]\in P\), since it is a product of two conjugate actual power values. Thus at \(p=3\), after removing the obvious cube factors, the *coupled* element \(c_3d\) from \([y,x^3]=c_1^3c_2^3c_3d\) lies in \(P\) and has cube one. The untested question is whether the surviving terminal part of \([x^3,y^3]\) is the cube of this coupled element (and its swapped analogues), rather than whether \(c_3\) and \(d\) separately lie in \(P\). General mathematical knowledge, unverified: this inference and the experiment below require Validator checking.

## One experiment: CTH-3-5
In the torsion-free free two-generator nilpotent group \(F_{2,5}\), fix one Hall basis and compute, integrally through weight 5, the terminal coordinate vectors of
\[
A=[y,x^3],\qquad B=[x,y^3],\qquad C=[x^3,y^3].
\]
Strip from \(A,B\) factors already known to be actual cubes, and let \(R\) be the \(\mathbb F_3\)-span of the remaining weight-4/5 coupled vectors and their required conjugates/polarizations; every represented element specializes into \(P\). Divide the surviving coordinate vector of \(C\) by 3 and reduce modulo 3. Test whether it lies in \(R\). A success certificate is an integral Hall identity expressing \(C\), modulo ninth powers and weight \(>5\), as a product of cubes of explicitly displayed elements of \(P\); this would give at least the \(p=3\), class-5 partial and a precise template for general \(p\). This uses no chosen root for a product of values and does not reopen the exhausted compatible-root action argument.

**Hard kill criterion:** if the normalized terminal vector of \(C\) has any nonzero component outside \(R\), stop CTH-3-5 immediately and record that residual Hall coordinate; do not spend the window on parameter changes or on Jennings descent. The associated-graded/Jennings suggestion is lower-EV until a root-valuation lemma is supplied: closure does not by itself ensure that a chosen root of a product has the filtration degree needed to make leading restricted \(p\)-images additive, and additive \(p\)-image alone need not force an exponent-\(p\) Lie subalgebra to be abelian.
