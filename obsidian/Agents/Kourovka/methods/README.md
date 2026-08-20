---
title: "Kourovka reusable research playbooks"
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, project/kourovka, status/reference]
---

# Reusable research playbooks

This is a curated memory of problem-independent tactics and failure modes. It is
not a collection of solutions and not a reason to force every problem into the
shape of the most recent success.

Lead owns this directory. Problem agents and MathExpert propose playbooks through
the file bus. Add one only after it has produced useful information on at least one
scope or explains a repeated failure across scopes.

Each playbook records:

```markdown
---
method_id: <stable-short-id>
method_class: catalogue | structured-construction | proof-reduction | verification | supervision
topics_observed: [<topic>]
status: provisional | tested | retired
---

# <Method name>

## Trigger
What evidence suggests this method is worth trying?

## Preconditions
What mathematical and tooling assumptions are required?

## Procedure
Concrete bounded steps, including the first cheap test.

## Kill criterion
What evidence says to stop rather than enlarge parameters?

## Representation-changing pivot
What qualitatively different model should be considered next?

## Certificate
What would let Validator independently check success?

## Known failure modes
Especially ways the method can satisfy only a nearby or necessary condition.

## Evidence base
Scopes where it was tried, with outcome and limitations.
```

At portfolio review, Lead checks method diversity. A catalogue probe, a structured
construction, and a theoretical reduction are different classes; three larger
bounds in the same catalogue are one strategy. Playbooks are prompts for judgement,
not mandatory pipelines.
