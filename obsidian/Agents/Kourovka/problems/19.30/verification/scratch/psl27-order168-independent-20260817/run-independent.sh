#!/usr/bin/env bash
set -u

validation_dir="Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817"
validation_script="$validation_dir/independent-order168.g"
validation_stdout="$validation_dir/stdout.txt"
validation_stderr="$validation_dir/stderr.txt"
validation_status="$validation_dir/exit-status.txt"

/usr/bin/timeout --signal=TERM --kill-after=30s 900s \
  /usr/bin/gap -q "$validation_script" \
  >"$validation_stdout" 2>"$validation_stderr"
validation_rc=$?
printf '%s\n' "$validation_rc" >"$validation_status"
exit "$validation_rc"
