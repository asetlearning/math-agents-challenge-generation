#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C

run_dir='Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism'
scratch_dir="$run_dir/scratch"
checker="$scratch_dir/psu33_full_colour_checker.g"
stdout_path="$scratch_dir/psu33-full-colour-stdout.txt"
stderr_path="$scratch_dir/psu33-full-colour-stderr.txt"
resource_path="$scratch_dir/psu33-full-colour-resource.txt"
gap_log_path="$scratch_dir/psu33-full-colour-output.txt"
matrix_path="$scratch_dir/psu33-colour-matrix.g"
certificate_path="$scratch_dir/psu33-full-colour-certificate.g"
expected_checker_sha='86e2633dff9c8f5ec25c3ee7beb5ce21b8e2e3a957e26f550874b3e154843208'
sentinel='PSU33_FULL_COLOUR_CHECKER_SUCCESS'

actual_checker_sha="$(sha256sum "$checker" | cut -d ' ' -f 1)"
if [[ "$actual_checker_sha" != "$expected_checker_sha" ]]; then
  printf 'PRECHECK_FAIL checker_sha expected=%s actual=%s\n' "$expected_checker_sha" "$actual_checker_sha" >&2
  exit 64
fi

for output_path in \
  "$stdout_path" "$stderr_path" "$resource_path" "$gap_log_path" \
  "$matrix_path" "$certificate_path"
do
  if [[ -e "$output_path" ]]; then
    printf 'PRECHECK_FAIL output_already_exists=%s\n' "$output_path" >&2
    exit 65
  fi
done

set +e
/usr/bin/time -v -o "$resource_path" \
  timeout --signal=TERM --kill-after=10s 900s \
  gap --quitonbreak -q -b "$checker" >"$stdout_path" 2>"$stderr_path"
run_status=$?
set -e

if [[ $run_status -ne 0 ]]; then
  printf 'RUN_FAIL exit_status=%s stdout=%s stderr=%s\n' "$run_status" "$stdout_path" "$stderr_path" >&2
  exit 66
fi
if [[ -s "$stderr_path" ]]; then
  printf 'ACCEPTANCE_FAIL nonempty_stderr=%s\n' "$stderr_path" >&2
  exit 67
fi
for required_path in "$stdout_path" "$resource_path" "$gap_log_path" "$matrix_path" "$certificate_path"
do
  if [[ ! -s "$required_path" ]]; then
    printf 'ACCEPTANCE_FAIL missing_or_empty=%s\n' "$required_path" >&2
    exit 68
  fi
done
if grep -Fq '=FAIL' "$stdout_path" || grep -Fq '=FAIL' "$gap_log_path"; then
  printf 'ACCEPTANCE_FAIL checker_reported_failure\n' >&2
  exit 69
fi
if ! grep -Fxq "$sentinel" "$stdout_path" || ! grep -Fxq "$sentinel" "$gap_log_path"; then
  printf 'ACCEPTANCE_FAIL success_sentinel_absent\n' >&2
  exit 70
fi
if [[ "$(tail -n 1 "$stdout_path")" != "$sentinel" ]] || [[ "$(tail -n 1 "$gap_log_path")" != "$sentinel" ]]; then
  printf 'ACCEPTANCE_FAIL success_sentinel_not_terminal\n' >&2
  exit 71
fi

printf 'RUNNER_ACCEPTED_PSU33_FULL_COLOUR_CHECKER\n'
