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
  - "infrastructure: optional per-host cost_per_hour (default 0) and max_hours in rjob.toml; placement passes over hosts whose max_hours < timeout_hours while another capable host is reachable, else uses them; submit prints the cost bound; rjob cost sums hours and cost per job and host (issue #8, PR #9 merged 2026-10-21 as main @ 3ea57cb; the VM client runs main)"
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

- **Current hosts:** the owner's Mac (M1, 10 cores, 64 GB, MPS), with jobs under the unprivileged `gpuworker` account; and `cpuserver`, a CPU-only Linux server (16 cores, 62 GB), with jobs under the unprivileged `cpuworker` account (since 2026-10-21).
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
- **Job length and cost:** the Mac takes jobs with `timeout_hours <= 2` (`max_hours = 2` in challenge-gen's `rjob.toml`, owner 2026-10-21); longer jobs go to the servers, and to the Mac only when no other host can run them (MPS/GPU with no GPU server, or no server reachable). `cpuserver` costs $0.55/h. Paid hosts carry `cost_per_hour`; `rjob cost` charges each job the full host rate for the hours it held the host, so concurrent jobs overstate the bill.
- **Paid hosts stop themselves when idle; `rjob power` starts them (remote-jobs #10: part 1 PR #11 and setup scripts PR #13 merged 2026-10-22; part 2 PR #15 merged 2026-10-22; VM power key set up for cpuserver).** `cpuserver` stops itself through the Nebius API after 30 idle minutes (no running or queued jobs, no runner activity except `info`/`status`/`list`, no login, no hold); a shutdown from inside the VM would keep billing. From the VM: `rjob power status` (cloud state, autostop decision, hold, stop time), `rjob power start cpuserver` (waits until the runner accepts jobs), `rjob power hold cpuserver <hours>` (≤ 12 h, `0` clears it), `rjob power stop cpuserver` (stops once idle; never kills jobs). Until part 3 (start on submit): a stopped server is not started automatically, so a long job would fall back to the Mac. Agents use `rjob power`, never the `nebius` CLI. Design and owner setup: remote-jobs `docs/power.md`.
- **Large inputs:** `rjob put-data <file>` uploads them once per host; they are content-addressed. `rjob submit` uploads a job's `[data]` to the host it was placed on.
- **Which host:** `rjob submit` places a job on the first project host that can run its `device` and has room for its `gpus`, `cpus` and `mem_gb`; otherwise on the capable host with the shortest queue. Priority: `--host`, then `$RJOB_HOST` (outranks the project file), then `host = "..."` in job.toml, then placement. Later commands on the job id use the host recorded at submit; a job missing from the record goes to `$RJOB_HOST`, else the project host that knows the id, else `mac`. `rjob hosts` shows every host's load.
- **Which tasks go remote** is set in the project's execution policy (see [[project-challenge-gen]]):
  - GPU work, and anything expected to exceed about 30 minutes or 2 GB, runs remotely;
  - editing, compiling, unit tests, smoke runs and analysis stay local.
- **Local runs go through `capjob`** (2026-10-16; `client/capjob`, merged in remote-jobs PR #7, main @ 7eb813c). It caps memory and CPU, by default at 2 GB, 1 GB swap and 2 CPUs, with oom_score_adj 1000. When the cap kills a job it falls back to `rjob submit`, either automatically or by leaving a draft job.toml (exit 75). It was added after OOM kills of `maestri-app` on 2026-10-15/16. Rule: [[_common]] § Memory cap and rjob fallback.

## Protected surfaces
- **Job spec / `job.json`** (`name`, `code{repo,sha,submodules,build_steps}`, `resources{device,cpus,timeout_hours,gpus?,mem_gb?}`, `run{argv,files,outputs}`, `data`, `runs_dir`). A future container or Slurm backend must honour the same contract; changes are additive only.
- **`provenance.json` and `manifest.json`.** Experiment notes cite job ids and rely on these fields.
- **The SSH verb set and the forced-command boundary.** Over SSH, no verb may execute client-supplied strings.

## Known pitfalls
- **Mac host is live (2026-10-05).** It is `Alex-MacBook-M1` at 10.211.55.2: macOS 15.3, 10 cores, 64 GB, torch MPS. Slots are 1 GPU and 9 CPU, with a 54 GB `mem_gb` budget since 2026-10-15. The challenge-gen host list is `~/Research/challenge-gen/rjob.toml` (Mac first, then `cpuserver`). The locked key was verified: shell, arbitrary commands, scp and forwarding are all refused.
- **`cpuserver` is live (2026-10-21).** It is `math-agent-compute-16p-64g-1`: Ubuntu 24.04 x86_64, 16 cores, 62 GB, 184 GB free disk, no GPU, reached over the owner's Tailscale (headscale) network, with no public address. Slots are 15 CPU and a 53 GB `mem_gb` budget; the host Python is 3.12.15 with torch 2.14.1+cu130 (`cuda: false`). It is listed second in `~/Research/challenge-gen/rjob.toml`, with `cost_per_hour = 0.55`. Verified the same day: shell, arbitrary commands, scp and port forwarding are refused; a CPU smoke job and a `[code]` job (push, per-SHA build, uv venv, fetch, provenance) both ran.
- **Tailscale SSH bypasses the lock.** With Tailscale SSH on (`RunSSH: true`), `tailscaled` answers port 22 on the tailnet address and logs users in by tailnet identity, so `authorized_keys` and its `restrict,command=run-job` line are ignored: the worker key gets a full shell, and rjob verbs run as shell commands (`rjob info` printed the GNU `info` manual). The remote-jobs `docs/server-setup.md` step 4 now carries this warning. On a tailnet host, run `sudo tailscale set --ssh=false` so OpenSSH handles port 22, and make sure every admin account has its own key in `authorized_keys` first, or the admin is locked out. Then `from=` must be the address sshd sees the VM connect from (the Mac's tailnet address, since the VM has no Tailscale of its own).
- **b25 builds on the Mac (2026-10-05):**
  - **The committed submodule pin `c09327705a` fails**, as documented: Hybrid, Dehn, LengthRange, HighPowerCount, WordProductLength and Abelianized scorers are undeclared.
  - **Building against tcgraph `main` (26f4f5a9) works** in about 30 s once uv's cache is warm (`[code.submodules."cpp/tcgraph"] sha = "main"`, as in `examples/b25-build-tcgraph-main`). `tcgraph_ext` imports with torch 2.12.0 and MPS.
  - **`examples/pb-smoke` ran the full PatternBoost loop** with the model on `mps`.
  - **Seed gotcha:** if the sampler and PatternBoost use the same seed, the target lands in the initial pool and training never runs.
- **Isolation of the worker account (fixed 2026-10-05).**
  - The first `install.sh` picked up the owner's uv from PATH. Since the fix merged into main (47b2e83), it always uses `~/.local/bin/uv`, and the host config now points to gpuworker's own uv.
  - The owner's home was listable by other accounts (the macOS default). The owner set `chmod 700` on its home directory, so gpuworker is now blocked from everything there.
  - Keep both properties when changing hosts or installers.
- **Docker is not used on the Mac.** Docker on macOS runs a Linux VM without Metal/MPS, so containers would be CPU-only. Mac jobs therefore run natively, as builds pinned to a commit SHA. Linux servers also run natively for now (owner, 2026-10-14); a container backend (`docker run --gpus all`) or Slurm scheduling is optional later, behind the same job contract. b25's `Dockerfile` is stale: it runs `git submodule update` without `.git`, and compose forces amd64.
- **Hosts update separately.** A host runs the `run_job.py` copied by its last `install.sh`; the Mac was re-installed on 2026-10-15 (multi-host runner, `mem_gb = 54` added to its config by hand, since `install.sh` keeps an existing config). The new client works with older runners (placement falls back to "idle host"), but GPU ids, `mem_gb` scheduling and the extended `info` need `install.sh` re-run on that host.
- **Estimates are not limits.** `mem_gb` and `cpus` only steer scheduling; a job that exceeds them can starve its neighbours or hit the OOM killer.
- **Job code is unrestricted** as the worker account, so the account must hold nothing of value. A `sandbox-exec` wrapper is a TODO.

## Related material
- [[project-challenge-gen]]: first consumer; its execution policy says what runs remotely
- [[dep-b25-pyproject-agentic]] · [[dep-tcgraph-agentic]]: the code shipped and built by these jobs
- [[projects-and-dependencies-convention]]
