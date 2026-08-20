---
title: "Kourovka program benchmarking"
protocol_version: 2
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, project/kourovka, status/draft]
---

# Benchmarking without pretending contamination is absent

No retrospective public theorem can prove clean model discovery: the statement,
solution, or discussion may have appeared in training. Treat public solved problems
as workflow diagnostics, not as uncontaminated evidence of research ability.

Benchmark separate capabilities instead of compressing everything into “solved”:

1. target and constraint fidelity;
2. problem selection and tractability calibration;
3. mathematical discovery and substantial progress;
4. Lead supervision, pivots, and budget allocation;
5. independent verification and false-claim rejection;
6. reproducibility and state hygiene.

## Benchmark tiers

### A. Sealed private post-deployment holdouts — primary

Use a problem with a human-held solution that has never been placed in the vault,
file bus, prompt history, searchable service, or any model-connected tool. The
human's withheld Kourovka solution is exactly this kind of asset if it remains
sealed.

- Keep the solution, shared-chat link, identifying hints, commitment salt, and
  evaluator rubric outside this vault.
- Before the run, freeze the protocol version, model, reasoning effort, budget,
  allowed resources, statement, scope constraints, and scoring rubric.
- Give the crew only the statement and public run manifest. For the cleanest
  discovery score, disable open-web search and let the human separately perform the
  staleness check, or supply a frozen literature packet that omits the solution.
- Run once. Do not tune prompts between glimpses of the hidden answer.
- Reveal only after all agent artifacts and the final Lead report are frozen.
- Retire the task permanently from the clean set after reveal. It may then become a
  public regression test, clearly labelled contaminated.

A salted, timestamped solution commitment may be held by the evaluator or a trusted
third party. Do not store an unsalted solution hash here; mathematical text can have
low enough variation to invite guessing.

### B. Secret-seed generated finite research tasks — primary

Generate fresh instances after the models and protocol are fixed. The evaluator
keeps the generator, seed, and answer outside the vault and releases only a
mathematical statement. Prefer tasks whose answers admit small exact certificates:
finite groups or presentations, word-map witnesses, module actions, extension data,
graph/group constructions, rewriting certificates, or exhaustive bounded
nonexistence proofs.

These test genuine search and certificate production with much lower exposure risk.
They do not by themselves show readiness for open-ended theory, so mix construction,
proof, and counterexample shapes and vary the mathematical representation.

### C. Adversarial target-fidelity tasks — primary process tests

Create fresh multi-clause statements containing an easy but irrelevant nearby case
and a harder active scope. Vary primes, exponent/order conditions, quantifier order,
object classes, and exclusions. The evaluator plants plausible near misses.

Score zero for a claimed answer when any required admissibility row fails. This tier
directly tests the system's defenses against solving the wrong clause and should span
many group-theoretic topics rather than imitate any one notebook problem.

### D. Private proof-repair and false-claim tasks — primary Validator tests

After protocol freeze, a human or formal tool introduces one hidden error into a
valid proof, construction, transcription, or computation. Ask the crew to review the
artifact. Vary the fault: quantifier drift, invalid converse, circular construction,
wrong ambient object, incomplete enumeration, bad citation, or a failed hypothesis.
Measure whether Validator finds and localizes it and whether Lead prevents it from
reaching the human as a result.

### E. Future-resolution shadow portfolio — high validity, slow feedback

Timestamp and freeze current work on genuinely open scopes. When the community later
publishes a solution, compare the crew's prior reductions, predicted obstruction,
and proposed strategy with the new result. This avoids retrospective solution
exposure, although it produces sparse and delayed labels.

### F. Public solved problems — secondary diagnostics only

Older Kourovka solutions and standard theorems remain useful for regression,
orchestration, and verification tests. Label them `exposure_risk: high`; never cite
success on them as clean evidence of independent discovery. Obfuscation, renaming,
translation, or changing notation does not remove semantic contamination.

Cross-model-generated problems are also secondary: they can inherit generator bias
and accidental triviality. Use exact post-generation validation and secret seeds.

## Fair comparison protocol

When comparing a shared ChatGPT session with the agentic system, freeze:

- the same underlying model class and reasoning effort where the products permit;
- the same active-time and computation budget;
- the same statement, scope constraints, tools, and literature packet;
- the same disclosure rule for prior recognition;
- the same evaluator and outcome rubric.

Run multiple public process tasks, but preserve sealed private holdouts as one-shot
tests. Report medians and failure modes, not only the best run. A new protocol may be
tuned on development tasks and synthetic tasks; it must not be tuned on the sealed
holdout.

## Scoring

Target fidelity and admissibility are hard gates. If either fails, discovery score
is zero even when the nearby mathematics is interesting. Otherwise score separately:

| Dimension | Example measure |
|---|---|
| Mathematical outcome | exact solution, counterexample, checkable lemma, reduction, bound, or none |
| Substantial progress | evaluator-defined milestone fixed before the run |
| Verification | independent reconstruction, complete certificate, false-positive rate |
| Supervision | useful pivots, repetition avoided, checkpoint decisions supported by evidence |
| Efficiency | active hours and heavy-compute cost to each checkable result |
| State fidelity | correct scope/revision, no stale control action, no over-retirement |
| Human load | number and quality of interventions; routine guidance handled by Lead |
| Exposure | none suspected, possible prior exposure, demonstrated exposure |

Also record process measures on live open problems: number of genuinely different
strategies, time to first falsifiable experiment, useful negative results, successful
representation changes, reproducible partials, false claims caught, and unresolved
questions escalated to the human. These are operational metrics, not substitutes for
mathematical success.

## Contamination incident rule

Any agent that recognizes a benchmark, recalls a likely solution, discovers the
hidden answer, or sees an identifying shared-chat link immediately writes
`possible_prior_exposure` and stops clean-score work. Preserve the transcript. The
run can still diagnose scope handling or verification, but its discovery score is
tainted. Never penalize disclosure; penalizing it teaches agents to conceal exposure.
