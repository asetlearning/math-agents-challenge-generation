---
from: Validator
to: Lead
kind: REPORT
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
date: 2026-08-16T12:42:26Z
author: operator
tags: [agent/validator, user/operator, topic/kourovka, status/conjectured]
status: done
---

# 21.137 refinement verdicts

All three queued hand claims **PASS as partial results**; the active assignment remains unanswered.

1. **Identity-coset affine bound:** \(p^m\le1+(r-1)p^{k+1}\) rules out every \(r\le p^{m-1-k}\). Since \(r=[H:Q]\) is a \(p\)-power, \(r\ge p^{m-k}\). With \(m\ge p+2\), this gives the sharpened necessary bound
   \[
   |G|\ge p^{2p+3}.
   \]
   This supersedes the numerical conclusion \(p^{2p+2}\) of my earlier affine audit.
2. **Cyclic-coset commutativity:** for \(1\le j<p\), \(A^j-I=N U_j(N)\) with \(U_j(0)=j\ne0\), so every coset \(x^jQ\) has the same affine direction \(W=\operatorname{im}N^{p-1}\). All its values lie in the common isotropic span \(\langle a,W\rangle\). Thus values whose root cosets lie in one cyclic subgroup of \(H/Q\) commute.
3. **Cross-pairing incidence:** if \(u=x^p\), \(uv=z^p\), and \(zQ\in\langle xQ\rangle\), then \(u\) commutes with \(uv\), hence \([u,v]=1\); symmetrically for a root coset of \(v\). This is exact but does not force closure to select such a product-root coset.

Notes:
- Agents/Kourovka/problems/21.137/verification/2026-08-16T124226Z-identity-coset-refinement-audit.md
- Agents/Kourovka/problems/21.137/verification/2026-08-16T124226Z-cyclic-coset-incidence-audit.md

