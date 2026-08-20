#!/usr/bin/env bash

set +e

run_dir='Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817'

/usr/bin/timeout --signal=TERM --kill-after=30s 900s \
  /usr/bin/gap -q "${run_dir}/screen.g" \
  > "${run_dir}/stdout.txt" \
  2> "${run_dir}/stderr.txt"
run_exit_code=$?

printf '%s\n' "${run_exit_code}" > "${run_dir}/exit-status.txt"
exit "${run_exit_code}"
