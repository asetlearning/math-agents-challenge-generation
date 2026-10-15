---
title: remote-jobs (run heavy jobs from the agent VM on remote hosts)
kind: our-repo
upstream: https://github.com/asetlearning/remote-jobs (private)
license: none yet
ownership: we-own
obtain: "git clone https://github.com/asetlearning/remote-jobs.git ~/Research/remote-jobs; VM: ln -s ~/Research/remote-jobs/client/rjob ~/.local/bin/rjob; host: run host/install.sh as the worker account (docs/mac-setup.md)"
build: "none (stdlib Python 3.11+)"
test: "python3 tests/test_runner.py   # end-to-end with a fake ssh (several fake hosts, plus the pre-multi-host runner 47b2e83); 2026-10-15: all 68 checks pass on main f6f0419"
versions_in_use:
  - "main @ 47b2e83 (2026-10-05): initial runner merged via PRs #1 and #2 (branch 1-initial-runner, now deleted)"
  - "main @ 96359a8 (2026-10-15): multi-host merged via PR #4 (issue #3; squash of 89edec9, abdb6a0 per-OS installer detection, 75776ec review fixes). VM client live from 2026-10-15; Mac host re-installed the same day"
  - "main @ f6f0419 (2026-10-15): PR #6 pins the old-runner compatibility test to 47b2e83. Open: issue #5 (hosts decide whether a job fits)"
local_patches: []
capabilities:
  - "infrastructure: ship exact commits (with submodules) from the VM to a host as git bundles over a locked SSH forced command; no GitHub credentials on the host"
  - "infrastructure: per-commit cached builds on the host (git worktree + uv venv; default recipe = b25 Dockerfile: uv sync --frozen --no-install-project --group build, then uv pip install -e . --no-build-isolation); submodule pin overridable per job"
  - "infrastructure: per-host job queue with GPU ids, CPU slots and an optional mem_gb budget (Mac: 1 GPU, 9 CPU slots), timeouts, cancel (process groups), states queued|building|running|done|failed|cancelled|timeout|dead"
  - "infrastructure: several hosts per project via <project>/rjob.toml; placement by device and free capacity; per-job GPU ids (CUDA_VISIBLE_DEVICES); optional mem_gb estimates; host recorded per job id"
  - "infrastructure: resumable, sha256-verified fetch of outputs to <runs_dir>/<job-id>/, with --include subsets and provenance.json (repo + submodule SHAs, uv.lock hash, job spec, input hashes, host, torch, device)"
heavy_processes: []
mcp: none
local_checkouts:
  asetlearning: ~/Research/remote-jobs
docs: "README.md, CLAUDE.md, docs/mac-setup.md, docs/server-setup.md, docs/execution-policy.md"
used_by: ["[[project-challenge-gen]]"]
tags: [meta, type/reference]
---

# remote-jobs

## What it is
The agents run in a sandboxed VM: 2 CPUs, about 3 GB RAM, no GPU. `remote-jobs` is the only channel from that VM to stronger compute.

- **Current host:** the owner's Mac (M1, 10 cores, 64 GB, MPS). Jobs run there under the unprivileged `gpuworker` account.
- **More hosts:** any SSH-reachable Linux server (CUDA or CPU), set up the same way (`docs/server-setup.md`). Each project lists its hosts in an `rjob.toml` in the project directory.
- **Client:** agents use the `rjob` CLI in the VM.
- **Host side:** `run_job.py`, behind an SSH key locked with `restrict,command=run-job`.

## How we use it
- **Write a `job.toml`.** It holds the `[code] path` of a clean local checkout, `[resources]` (device cpu|mps|cuda, cpus, timeout_hours), `[run] argv/files/outputs` and an optional `[data]`.
- **Run it:**
  1. `rjob submit <job.toml>` resolves SHAs, pushes missing commits and queues the job. It prints a job id.
  2. `rjob wait <id>` blocks until the job finishes; run it in the background.
  3. `rjob fetch <id>` brings results to `~/Research/challenge-gen/runs/<id>/` for this project.
- **Inspect:** `rjob status|logs|list|info|cancel`.
- **Large inputs:** `rjob put-data <file>` uploads them once per host; they are content-addressed. `rjob submit` uploads a job's `[data]` to the host it was placed on.
- **Which host:** `rjob submit` places a job on the first project host that can run its `device` and has room for its `gpus`, `cpus` and `mem_gb`; otherwise on the capable host with the shortest queue. Priority: `--host`, then `$RJOB_HOST` (outranks the project file), then `host = "..."` in job.toml, then placement. Later commands on the job id use the host recorded at submit; a job missing from the record goes to `$RJOB_HOST`, else the project host that knows the id, else `mac`. `rjob hosts` shows every host's load.
- **Which tasks go remote** is set in the project's execution policy (see [[project-challenge-gen]]):
  - GPU work, and anything expected to exceed about 30 minutes or 2 GB, runs remotely;
  - editing, compiling, unit tests, smoke runs and analysis stay local.

## Protected surfaces
- **Job spec / `job.json`** (`name`, `code{repo,sha,submodules,build_steps}`, `resources{device,cpus,timeout_hours,gpus?,mem_gb?}`, `run{argv,files,outputs}`, `data`, `runs_dir`). A future container or Slurm backend must honour the same contract; changes are additive only.
- **`provenance.json` and `manifest.json`.** Experiment notes cite job ids and rely on these fields.
- **The SSH verb set and the forced-command boundary.** Over SSH, no verb may execute client-supplied strings.

## Known pitfalls
- **Mac host is live (2026-10-05).** It is `Alex-MacBook-M1` at 10.211.55.2: macOS 15.3, 10 cores, 64 GB, torch MPS. Slots are 1 GPU and 9 CPU, with a 54 GB `mem_gb` budget since 2026-10-15. The challenge-gen host list is `~/Research/challenge-gen/rjob.toml` (Mac active; the Linux server is to be added). The locked key was verified: shell, arbitrary commands, scp and forwarding are all refused.
- **b25 builds on the Mac (2026-10-05):**
  - **The committed submodule pin `c09327705a` fails**, as documented: Hybrid, Dehn, LengthRange, HighPowerCount, WordProductLength and Abelianized scorers are undeclared.
  - **Building against tcgraph `main` (26f4f5a9) works** in about 30 s once uv's cache is warm (`[code.submodules."cpp/tcgraph"] sha = "main"`, as in `examples/b25-build-tcgraph-main`). `tcgraph_ext` imports with torch 2.12.0 and MPS.
  - **`examples/pb-smoke` ran the full PatternBoost loop** with the model on `mps`.
  - **Seed gotcha:** if the sampler and PatternBoost use the same seed, the target lands in the initial pool and training never runs.
- **Isolation of the worker account (fixed 2026-10-05).**
  - The first `install.sh` picked up the owner's uv from PATH. Since the fix merged into main (47b2e83), it always uses `~/.local/bin/uv`, and the host config now points to gpuworker's own uv.
  - The owner's home was listable by other accounts (the macOS default). The owner set `chmod 700 /Users/alex`, so gpuworker is now blocked from everything there.
  - Keep both properties when changing hosts or installers.
- **Docker is not used on the Mac.** Docker on macOS runs a Linux VM without Metal/MPS, so containers would be CPU-only. Mac jobs therefore run natively, as builds pinned to a commit SHA. Linux servers also run natively for now (owner, 2026-10-14); a container backend (`docker run --gpus all`) or Slurm scheduling is optional later, behind the same job contract. b25's `Dockerfile` is stale: it runs `git submodule update` without `.git`, and compose forces amd64.
- **Hosts update separately.** A host runs the `run_job.py` copied by its last `install.sh`; the Mac was re-installed on 2026-10-15 (multi-host runner, `mem_gb = 54` added to its config by hand, since `install.sh` keeps an existing config). The new client works with older runners (placement falls back to "idle host"), but GPU ids, `mem_gb` scheduling and the extended `info` need `install.sh` re-run on that host.
- **Estimates are not limits.** `mem_gb` and `cpus` only steer scheduling; a job that exceeds them can starve its neighbours or hit the OOM killer.
- **Job code is unrestricted** as the worker account, so the account must hold nothing of value. A `sandbox-exec` wrapper is a TODO.

## Related material
- [[project-challenge-gen]]: first consumer; its execution policy says what runs remotely
- [[dep-b25-pyproject-agentic]] · [[dep-tcgraph-agentic]]: the code shipped and built by these jobs
- [[projects-and-dependencies-convention]]
