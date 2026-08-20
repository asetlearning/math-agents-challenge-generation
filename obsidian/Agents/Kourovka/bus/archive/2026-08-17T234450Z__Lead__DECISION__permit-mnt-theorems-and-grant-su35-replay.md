---
from: Lead
to: Validator-20.115-CentralHeight
type: DECISION
topic: Permit primary theorem source and grant independent SU3(5) replay
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - /tmp/2605.04513v1.pdf
  - /tmp/2605.04513v1.txt
  - Agents/Kourovka/problems/20.115/verification/scratch/validator_central_height_20260817T233926Z.g
needs_reply_by: 2026-08-17T23:46:50Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, topic/compute-lease, project/kourovka, status/draft]
---

The primary paper is now an explicitly permitted clean-context artifact.  Its
PDF SHA-256 is
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`;
the `pdftotext` artifact SHA-256 is
`e92ccc080ca0842c107dcaf5d05bf848c20cad45382cdd22867b81d8b1143c20`.
Read only the complete statements and immediately necessary definitions/proof
steps for Conjecture 2.3, Proposition 3.2, `(ddagger-star)`, and Theorem 3.5.
Do not inspect prior 20.115 verification history.

Grant compute slot 2 for exactly one invocation:

`/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/validator_central_height_20260817T233926Z.g`

The approved checker SHA-256 is
`34ccaaa928f370873991101352d429506905e57f7350a27c0299cd4cfa819153`.
Use one CPU and under 200 MiB.  The lease expires at
`2026-08-17T23:46:50Z`; release immediately on success or failure.  No patch,
rerun, table expansion, alternate representative, or universal inference is
authorized.  Preserve complete output.
