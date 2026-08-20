---
title: "All-27 leased exact cube gates — complete raw output"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

# Exact active source scope

Odd `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual set
`{g^p:g in G}`, never generated subgroup; literal set itself a subgroup; ask
whether it is abelian; `p=2`/exponent-eight sibling excluded.

# Lease integrity

All five leased hashes matched before execution. Exactly one invocation ran,
with no patch, rerun, class change, or action/lift/kernel/quotient/prime change:

```text
timeout 420s python3 -u Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/check_27_classes.py
```

It completed normally with exit code 0 at `2026-08-17T21:51:17Z`. Standard
error was empty. The following is the complete stdout, including the redundant
aggregate line; no content is omitted.

# Raw stdout

```text
certified input classes: 27
V checks/base equations/rank: 729 19683 78732 59049 1951
CLASS 0 000000000000002002 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 1 000000000000002102 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 2 000000000000002202 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 3 000000000000102002 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 4 000000000000102102 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 5 000000000000102202 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 6 000000000000202002 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 7 000000000000202102 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 8 000000000000202202 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
CLASS 9 000000100000012022 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 10 000000100000012122 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 11 000000100000012222 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 12 000000100000112022 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 13 000000100000112122 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 14 000000100000112222 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 15 000000100000212022 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 16 000000100000212122 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 17 000000100000212222 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 18 000000200000022012 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 19 000000200000022112 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 20 000000200000022212 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 21 000000200000122012 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 22 000000200000122112 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 23 000000200000122212 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 24 000000200000222012 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 25 000000200000222112 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 26 000000200000222212 exp9 True cube_size 135 closed False closure_size 729 order/kernel/quotient 59049 2187 27 noncomm None hit False
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
ALL CLASS RESULTS: [(0, '000000000000002002', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (1, '000000000000002102', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (2, '000000000000002202', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (3, '000000000000102002', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (4, '000000000000102102', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (5, '000000000000102202', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (6, '000000000000202002', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (7, '000000000000202102', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (8, '000000000000202202', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0)), (9, '000000100000012022', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (10, '000000100000012122', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (11, '000000100000012222', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (12, '000000100000112022', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (13, '000000100000112122', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (14, '000000100000112222', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (15, '000000100000212022', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (16, '000000100000212122', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (17, '000000100000212222', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (18, '000000200000022012', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (19, '000000200000022112', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (20, '000000200000022212', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (21, '000000200000122012', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (22, '000000200000122112', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (23, '000000200000122212', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (24, '000000200000222012', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (25, '000000200000222112', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), (26, '000000200000222212', True, None, 135, False, 729, [1, 3, 9, 27, 81, 243, 729], (2, 1, 0, 2, 2, 0, 1, 0, 0, 0), None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1))]
TARGET-EQUAL CLASS INDICES: []
```

