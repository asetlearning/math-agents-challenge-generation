---
from: Validator
to: Lead
kind: REPORT
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
date: 2026-08-16T12:52:29Z
author: operator
tags: [agent/validator, user/operator, topic/kourovka, status/conjectured]
status: done
---

# 21.137 cyclic-cover verdict

**PASS as a structural partial; active scope unanswered.**

For \(2d=\dim Q/Z(Q)\), every cyclic root-coset subgroup supplies one totally isotropic linear piece of size at most \(p^d\), and these pieces cover the symplectic quotient. Counting nonzero points gives \(t\ge p^d+1\). Since \(H/Q\) has exponent \(p\),

\[
t=\frac{[H:Q]-1}{p-1},
\]

so \([H:Q]>p^d\), and the \(p\)-power order gives

\[
[H:Q]\ge p^{d+1}.
\]

The spread example verifies that the underlying isotropic-cover count is sharp; this cannot by itself prove \(Q\) abelian.

Full note: Agents/Kourovka/problems/21.137/verification/2026-08-16T125229Z-cyclic-isotropic-cover-audit.md.

