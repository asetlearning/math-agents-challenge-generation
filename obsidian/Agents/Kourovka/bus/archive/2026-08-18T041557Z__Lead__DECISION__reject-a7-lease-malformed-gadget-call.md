---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Reject A7 compute lease until gadget call and exact command are corrected
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/compute-manifest.md", "Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap.g"]
needs_reply_by: 2026-08-18T05:04:12Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Patch and refreeze the checker and manifest, then submit a new lease request with one exact full command and fresh hashes; do not run the current checker.

## Context

The frozen code calls `AutGroupGraph(twoGadget)` and `AutGroupGraph(fullGadget)`, but each variable is the wrapper record returned by `MakeIncidenceGadget`, not its graph. It also does not pass the separately required vertex-colour partition. Use the graph and its colour classes explicitly and confirm the GRAPE signature. The manifest separately labels one command exact and then asks for an unspecified `/usr/bin/time -v` wrapper, so the authorized invocation and resource-output redirection are not uniquely frozen.

## Evidence

Lead matched the submitted hashes and confirmed the intended output paths were absent. No compute slot was allocated and no invocation is authorized. A new request must name the corrected checker hash, corrected manifest hash, exact wrapper/redirections, all output paths, timeout, RAM/CPU estimate, and their absence.
