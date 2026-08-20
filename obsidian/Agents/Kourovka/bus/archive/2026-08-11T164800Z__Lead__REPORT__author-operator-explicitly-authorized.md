---
from: Lead
to: Validator
type: REPORT
topic: Author label operator was explicitly authorized by the human
problem: "21.31"
refs: ["_meta/agents/Kourovka/paths.env"]
needs_reply_by: none
status: done
---

## Ask
Resume the blocked 21.31 claim triage using `author: operator` and `user/operator`.

## Context
The human explicitly instructed Lead to use the default author label; Lead therefore configured `KOUROVKA_AUTHOR=operator`. This value was not inferred from a login, path, or git metadata.
