#!/usr/bin/env bash
set -u

validation_dir="Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-v2-20260817"
gap_script="$validation_dir/independent-a6-order360-v2.g"
python_checker="Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/verify-independent.py"
hash_manifest="$validation_dir/frozen-v2.sha256"
claimant_output="Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/a6_order360_vanishing_collision.out"
gap_stdout="$validation_dir/gap-stdout-v2.txt"
gap_stderr="$validation_dir/gap-stderr-v2.txt"
gap_status="$validation_dir/gap-exit-status-v2.txt"
checker_stdout="$validation_dir/checker-stdout-v2.txt"
checker_stderr="$validation_dir/checker-stderr-v2.txt"
checker_status="$validation_dir/checker-exit-status-v2.txt"
hash_output="$validation_dir/hash-check-v2.txt"

for output_path in \
  "$gap_stdout" "$gap_stderr" "$gap_status" \
  "$checker_stdout" "$checker_stderr" "$checker_status" "$hash_output"
do
  if [ -e "$output_path" ]; then
    printf 'refusing to overwrite existing artifact: %s\n' "$output_path" >&2
    exit 97
  fi
done

/usr/bin/sha256sum --check "$hash_manifest" >"$hash_output" 2>&1
hash_rc=$?
if [ "$hash_rc" -ne 0 ]; then
  exit "$hash_rc"
fi

(
  ulimit -t 870
  ulimit -v 2097152
  exec /usr/bin/gap -q --quitonbreak "$gap_script"
) >"$gap_stdout" 2>"$gap_stderr"
gap_rc=$?
printf '%s\n' "$gap_rc" >"$gap_status"
if [ "$gap_rc" -ne 0 ]; then
  exit "$gap_rc"
fi

/usr/bin/python3 "$python_checker" "$claimant_output" "$gap_stdout" \
  >"$checker_stdout" 2>"$checker_stderr"
checker_rc=$?
printf '%s\n' "$checker_rc" >"$checker_status"
exit "$checker_rc"
