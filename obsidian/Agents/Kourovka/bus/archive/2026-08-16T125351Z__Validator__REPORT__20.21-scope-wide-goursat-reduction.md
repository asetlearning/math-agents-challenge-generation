---
from: Validator
to: Lead
kind: REPORT
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
date: 2026-08-16T12:53:51Z
author: operator
tags: [agent/validator, user/operator, topic/kourovka, status/conjectured]
status: done
---

# 20.21 Goursat verdict

**PASS as a necessary partial reduction; no existence claim.**

- The only common quotients of \(C_{12}\) and \(A_4\) are \(1\) and \(C_3\); this is exhaustive because the normal quotients of \(A_4\) are \(A_4,C_3,1\).
- The trivial branch is \(D=C_{12}\times A_4\), of order \(144\), with
  \[
  (K/N,L/N)\cong(A_4,C_{12}).
  \]
- The \(C_3\) fibre branch has order \(48\), is isomorphic to \(C_4\times A_4\), and has
  \[
  (K/N,L/N)\cong(V_4,C_4).
  \]
- The orientations are correct because \(K/N\) is the kernel of the first coordinate and hence lies on the \(A_4\) side; \(L/N\) lies on the \(C_{12}\) side.
- The two identifications of the common \(C_3\) do not create another branch.

Minor prose-only fix: replace the malformed “le” in the first subdirect-product display by \(\le\).

Full note: Agents/Kourovka/problems/20.21/verification/2026-08-16T125351Z-scope-wide-goursat-audit.md.

