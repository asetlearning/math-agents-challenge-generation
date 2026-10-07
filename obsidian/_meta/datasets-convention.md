---
title: Datasets convention
status: draft
author: asetlearning
tags: [meta, convention]
---

# Datasets convention

A **dataset** is a file (or a small set of files) of problem instances, words, presentations, labels or other records that more than one experiment, agent or person will use: challenge sets, benchmark corpora, relator banks, labelled training data. Datasets are registered in the vault so that every experiment cites the same, checksummed, vetted object instead of a bare path that may have changed.

Rule of thumb: **the files live in git (or another storage with a checksum); the vault note says what they are, how they were made and what was checked.**

## Dataset notes vs experiment `data/` notes

| | Dataset note (`#dataset`) | Experiment data note (`#data`) |
|---|---|---|
| Where | `Datasets/<Domain>/<Instance>/ds-<...>.md` | `Experiments/<...>/<Experiment type>/data/<...>.md` |
| Scope | cross-experiment, reusable, immutable | one experiment type: its inputs, constants, logs, run dirs |
| Lifecycle | `draft` → `validated` (vetted) → `superseded` | follows the experiment |

An experiment's `data/` note **links** the dataset notes it consumes or produces and does not re-describe them.

## When to register a dataset

Register when any of these holds:
- a second experiment, agent or person will use the files;
- the files are a deliverable (e.g. a challenge set);
- the files are input to a published or validated result.

One-off intermediate files stay in the run directory and are described in the experiment's `data/` note.

## Location and naming

- **Note:** `Datasets/<Domain>/<Instance>/ds-<instance>-<slug>-<YYYYMMDD>.md`, e.g. `Datasets/Group Theory/B25/ds-b25-trivial-2-5reduced-aut8-20261007.md`. The filename (without `.md`) is the `dataset_id`; it is never reused.
- **Data file:** a matching unique name, e.g. `data/b25_trivial_2_5reduced_unique_aut8_20261007.txt`. Companion files share the stem (`.sources.csv`, `.certificates.json`, `.labels.csv`).
- Template: [[dataset-note]]. Content-type tag: `#dataset` (see [[tags]]).

## Storage

- **Registered dataset files (≤ 10 MB each, text or JSON) are committed to the vault repo's `data/` folder** at the repo root. For challenge-gen that repo is the fork `asetlearning/math-agents-challenge-generation`; **nothing is ever committed to the original `math-agents` repo.** `data/` is the one data exception to "the repo root holds onboarding files only". Vault notes stay data-free.
- **Only registered dataset files are committed.** Parent or intermediate files (e.g. the raw sets a dataset was derived from) stay local and untracked unless the owner says otherwise; the dataset note records their sha256.
- **Larger files** stay in the producing code repo, on a remote host via `rjob put-data` (content-addressed by sha256, see [[dep-remote-jobs]]), or in external storage. The note's `obtain:` says how to fetch them.
- **Reference files as `<repo>:<path>`** (e.g. `math-agents-challenge-generation:data/<file>`), never by a machine path. Local checkout paths are per-user config ([[projects-and-dependencies-convention]] § Local checkouts).
- **Committing a data file is a human gate**, like any vault commit. Add files to git by name, never with a broad `git add data/`.

## Immutability and versions

- The **sha256 in the note is the dataset's identity.** A changed file is a new dataset: new file name, new note, with `supersedes:` / `superseded_by:` linking the two. The old note gets `#status/superseded` and stays.
- Fixing a typo in the note's prose is fine; changing `files:`, `records:` or `property_claimed:` is not.

## Provenance and vetting

- `derived_from:` lists every parent: a registered dataset note, or, for an unregistered parent, its `<repo>:<path>`, sha256 and what is known about its origin (`unknown` is an honest value).
- `produced_by:` gives the script as `<repo>@<sha>:<path>`, plus the run dir or rjob job id. Scripts live in code repos, never in the vault.
- `vetting:` records every check: what was checked, the tool and version, **the object it was checked in**, the result and who ran it. A check in a finite quotient (e.g. B₀(2,5) via GAP) is evidence of consistency, never a proof in the free group; the table must say which is which (see [[validator]] and [[_common]] § Validator's verdict layers).
- **Status.** The producer writes the note as `#status/draft`. It becomes `#status/validated` when the property claims have been checked by a path independent of the producing one, normally by Validator (who updates only the status tag and links its verification note) or by the owning human. `validated` means "the vetting table is complete and correct", not "every claim is proved"; unproved claims stay labelled as such.

## Using a dataset

- Cite it by wikilink to its note in pre-registrations, results and data notes, e.g. "Problem set: `[[ds-<...>]]`".
- **Verify the sha256 before use** and record it in the run's provenance. A mismatch is a stop condition: report it, don't proceed.
- Code loads datasets from a path passed in config (taken from the note), never from a hardcoded path.
- Add the consuming note to the dataset's `used_by:`.

## Related material
- [[dataset-note]] — template
- [[experiment-folder-convention]] — experiment `data/` notes link datasets
- [[projects-and-dependencies-convention]] — provenance record, local checkouts
- [[naming-conventions]]
- [[tags]]
