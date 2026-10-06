---
title: remote-jobs (run heavy jobs from the agent VM on remote hosts)
kind: our-repo
upstream: https://github.com/asetlearning/remote-jobs (private)
license: none yet
ownership: we-own
obtain: "git clone https://github.com/asetlearning/remote-jobs.git ~/Research/remote-jobs; VM: ln -s ~/Research/remote-jobs/client/rjob ~/.local/bin/rjob; host: run host/install.sh as the worker account (docs/mac-setup.md)"
build: "none (stdlib Python 3.11+)"
test: "python3 tests/test_runner.py   # end-to-end with a fake ssh; 2026-10-05: all 28 checks pass, hostile-command and streaming-fetch fixes included"
versions_in_use:
  - "main @ 47b2e83 (2026-10-05): initial runner merged via PRs #1 and #2 (branch 1-initial-runner, now deleted)"
local_patches: []
capabilities:
  - "infrastructure: ship exact commits (with submodules) from the VM to a host as git bundles over a locked SSH forced command; no GitHub credentials on the host"
  - "infrastructure: per-commit cached builds on the host (git worktree + uv venv; default recipe = b25 Dockerfile: uv sync --frozen --no-install-project --group build, then uv pip install -e . --no-build-isolation); submodule pin overridable per job"
  - "infrastructure: job queue with GPU (1) and CPU (7 on the Mac) slots, timeouts, cancel (process groups), states queued|building|running|done|failed|cancelled|timeout|dead"
  - "infrastructure: resumable, sha256-verified fetch of outputs to <runs_dir>/<job-id>/, with --include subsets and provenance.json (repo + submodule SHAs, uv.lock hash, job spec, input hashes, host, torch, device)"
heavy_processes: []
mcp: none
local_checkouts:
  asetlearning: ~/Research/remote-jobs
docs: "README.md, CLAUDE.md, docs/mac-setup.md, docs/execution-policy.md"
used_by: ["[[project-challenge-gen]]"]
tags: [meta, type/reference]
---

# remote-jobs

## What it is
The agents run in a sandboxed VM: 2 CPUs, about 3 GB RAM, no GPU. `remote-jobs` is the only channel from that VM to stronger compute.

- **Current host:** the owner's Mac (M1, 8 cores, 64 GB, MPS). Jobs run there under the unprivileged `gpuworker` account.
- **Future hosts:** Linux/CUDA servers, reached the same way.
- **Client:** agents use the `rjob` CLI in the VM.
- **Host side:** `run_job.py`, behind an SSH key locked with `restrict,command=run-job`.

## How we use it
- **Write a `job.toml`.** It holds the `[code] path` of a clean local checkout, `[resources]` (device cpu|mps|cuda, cpus, timeout_hours), `[run] argv/files/outputs` and an optional `[data]`.
- **Run it:**
  1. `rjob submit <job.toml>` resolves SHAs, pushes missing commits and queues the job. It prints a job id.
  2. `rjob wait <id>` blocks until the job finishes; run it in the background.
  3. `rjob fetch <id>` brings results to `~/Research/challenge-gen/runs/<id>/` for this project.
- **Inspect:** `rjob status|logs|list|info|cancel`.
- **Large inputs:** `rjob put-data <file>` uploads them once; they are content-addressed.
- **Which tasks go remote** is set in the project's execution policy (see [[project-challenge-gen]]):
  - GPU work, and anything expected to exceed about 30 minutes or 2 GB, runs remotely;
  - editing, compiling, unit tests, smoke runs and analysis stay local.

## Protected surfaces
- **Job spec / `job.json`** (`name`, `code{repo,sha,submodules,build_steps}`, `resources`, `run{argv,files,outputs}`, `data`, `runs_dir`). A future container backend must honour the same contract.
- **`provenance.json` and `manifest.json`.** Experiment notes cite job ids and rely on these fields.
- **The SSH verb set and the forced-command boundary.** Over SSH, no verb may execute client-supplied strings.

## Known pitfalls
- **Mac host is live (2026-10-05).** It is `Alex-MacBook-M1` at 10.211.55.2: macOS 15.3, 10 cores, 64 GB, torch MPS. Slots are 1 GPU and 9 CPU. The locked key was verified: shell, arbitrary commands, scp and forwarding are all refused.
- **b25 builds on the Mac (2026-10-05):**
  - **The committed submodule pin `c09327705a` fails**, as documented: Hybrid, Dehn, LengthRange, HighPowerCount, WordProductLength and Abelianized scorers are undeclared.
  - **Building against tcgraph `main` (26f4f5a9) works** in about 30 s once uv's cache is warm (`[code.submodules."cpp/tcgraph"] sha = "main"`, as in `examples/b25-build-tcgraph-main`). `tcgraph_ext` imports with torch 2.12.0 and MPS.
  - **`examples/pb-smoke` ran the full PatternBoost loop** with the model on `mps`.
  - **Seed gotcha:** if the sampler and PatternBoost use the same seed, the target lands in the initial pool and training never runs.
- **Isolation of the worker account (fixed 2026-10-05).**
  - The first `install.sh` picked up the owner's uv from PATH. Since the fix merged into main (47b2e83), it always uses `~/.local/bin/uv`, and the host config now points to gpuworker's own uv.
  - The owner's home was listable by other accounts (the macOS default). The owner set `chmod 700 /Users/alex`, so gpuworker is now blocked from everything there.
  - Keep both properties when changing hosts or installers.
- **Docker is not used on the Mac.** Docker on macOS runs a Linux VM without Metal/MPS, so containers would be CPU-only. Mac jobs therefore run natively, as builds pinned to a commit SHA. A container backend (`docker run --gpus all`) is planned for Linux/CUDA servers. b25's `Dockerfile` is stale: it runs `git submodule update` without `.git`, and compose forces amd64.
- **Job code is unrestricted** as the worker account, so the account must hold nothing of value. A `sandbox-exec` wrapper is a TODO.

## Related material
- [[project-challenge-gen]]: first consumer; its execution policy says what runs remotely
- [[dep-b25-pyproject-agentic]] · [[dep-tcgraph-agentic]]: the code shipped and built by these jobs
- [[projects-and-dependencies-convention]]
