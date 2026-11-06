---
type: validation-triage
date: 2026-11-05
agent: Validator
---
# Triage: E0 rebuild-seed-pool rerun, breaks C3|4|15, C3|4|22 (and C1|6|1 repeats)

Request from Lead: replay certificates (all for the 2 new targets, at least one for C1|6|1), provenance (T-blind pool, no recipe), M2 route for one raw-source hit, comment on why R on w.u^-1 succeeds where R on w failed.
Claim type: L0-cert (free-group certificate of triviality in B(2,5)); route claim is scoped to what the files record (hit and R-trace are not stored).
Tool model check (step 2.5): pure-Python free reduction in F_2; the object is the free group, so the check is on the target model. No finite quotient used.
Plan: (1) replay 16 lines; (2) provenance from config, pool_measured events, code; (3) route: identify the letter automorphism and the cell split from certificate plus source cells; (4) comment.
Not planned: re-running E0 (compiled tcgraph_ext not on this VM).
