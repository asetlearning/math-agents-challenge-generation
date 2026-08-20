---
title: "Frozen heavy manifest — all 27 certified central classes, exact cube gates"
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

# Frozen batch

Input is exactly the 27 gauge representatives and realizing-factor digests
certified by the leased full-family run in `../full-family-raw-output.md`.
Every digest is rederived and checked. For each and only each certified class,
the checker constructs the exact coordinate group, checks all associativity and
six relators, inspects all 59,049 elements for exponent nine, forms the literal
cube set, tests exact subgroup closure (using cardinality immediately when it
is not a power of three as an additional certificate, while still comparing
every literal image with its generated closure), and tests noncommutativity
only after closure passes.

No alternate row, action, shear, label, kernel, quotient, prime, or generated-
power substitution is admitted. No class is skipped or added.

# One command only

```text
timeout 420s python3 -u Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/check_27_classes.py
```

Frozen hashes:

```text
fa622e186f1616c504ba8b0e85c737ef854a556bff3c75a7ac706c89f7e908fc  check_27_classes.py
e9932eb57e0d219604f251bccd4f951e9851fe5e0c7226aa6cbd2b8dad218329  central_cohomology.py
f64ebe165da86d87333236b1752bbd409d1e43975db8739d969848422a01948f  check_exact_group.py
ecf9ebd11e5c74307e533e19d195348f99cfe4a68be44211cb1ad2b029eee10a  check_full_family.py
```

The three imported files are hash-pinned dependencies in the same directory;
no prior raw cube output is read. The certified representative strings and
factor digests are literal frozen inputs copied from the leased full-family
certificate, and every digest is recomputed before its class is evaluated.

Expected resources: one CPU, under 200 MiB RAM, expected under 300 seconds,
hard timeout 420 seconds, one invocation. The output must give every gate for
every class, any exponent or closure certificate, and the exact list of
target-equal class indices. Any assertion failure aborts; no patch or rerun.
