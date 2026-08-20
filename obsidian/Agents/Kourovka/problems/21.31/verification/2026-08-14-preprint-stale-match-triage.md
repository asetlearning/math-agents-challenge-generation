---
title: "Verification triage — Kourovka 21.31 — counterexample preprint"
problem: 21.31
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Claim

Di Matteo–Ferrara–Trombetti, arXiv:2607.22795v1, constructs a finite soluble group \(N\) and an insoluble group \(G\) embedded regularly in \(\operatorname{Hol}(N)\), so it is an exact counterexample to Kourovka 21.31 rather than to the converse convention.

# Target versus witness

- **Target:** PDF page 169 asks whether every regular subgroup of \(\operatorname{Hol}(N)\) is soluble whenever the finite group \(N\) is soluble.
- **Paper witness:** the additive group \((N,+)=N_0^{\mathrm{op}}\), with \(N_0=P\rtimes Q\), and the multiplicative/source group \(G=H\rtimes L\), where \(G/H\cong L\cong\operatorname{PSL}_2(7)\). The paper defines a bijective cocycle \(b:G\to N\) and a homomorphism \(\lambda:G\to\operatorname{Aut}(N)\).
- **Witness equals target:** to be established from the paper's explicit final map \(x\mapsto(b(x),\lambda_x)\), including the paper's opposite-group convention and the order of the holomorph multiplication.

# Subclaims

1. The source statement on rendered PDF page 169 is exact.
2. The paper's additive group \(N) is finite and soluble.
3. Its group \(G\) is insoluble.
4. \(|G|=|N|\) and the map \(b:G\to N\) is bijective.
5. The identity \(b(xy)=b(x)+\lambda_x(b(y))\) uses the standard left-holomorph convention and yields a homomorphism \(G\to\operatorname{Hol}(N)\).
6. The image is regular, not merely transitive or normalized by a regular subgroup.
7. The use of \(N_0^{\mathrm{op}}\) repairs orientation and does not swap additive and multiplicative roles.
8. The preprint was submitted before this review and therefore makes the assignment stale if the construction is accepted.

# Tools available

- GAP 4.12.1, Python 3.12.3, `pdftotext` 24.02.0 and `pdftoppm`: available.
- Sage and Magma: unavailable.
- arXiv abstract and 15-page PDF: accessible through the web reader.

# Methods inventory

| Subclaim | Method | What a pass proves | What it does not prove |
|---|---|---|---|
| 1 | PDF extraction plus rendered-page inspection | Exact Notebook target | Paper correctness |
| 2–4 | Line-by-line audit of definitions, series, orders, quotient, coset decomposition and Proposition 2.7 | Internal proof of finiteness, solubility, insolubility and bijectivity | Independent machine reproduction of all coordinate tables |
| 5–7 | Convention translation and direct holomorph calculation | That the constructed brace gives the target-direction regular embedding | Validity of every earlier coordinate lemma unless audited separately |
| 8 | arXiv metadata | Existence and submission date of the cited artifact | Peer review or later-version stability |

# Hard limits and recommendation

The construction has order \(7^8 3^7 2^3\), so brute-force element enumeration is inappropriate. The paper says its proof is direct in coordinates; verification therefore requires a line-by-line proof audit, with only light checks of bounded matrix/function identities. Recommendation: full stale-match review; keep the mathematical verdict at `conjectured` if any coordinate lemma or convention link remains unchecked.
