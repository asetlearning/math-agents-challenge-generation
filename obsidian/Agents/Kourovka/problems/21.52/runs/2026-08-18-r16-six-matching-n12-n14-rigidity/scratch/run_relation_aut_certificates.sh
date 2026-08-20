#!/usr/bin/env bash
set -euo pipefail

run_root='Agents/Kourovka/problems/21.52/runs/2026-08-18-r16-six-matching-n12-n14-rigidity/scratch'
n13_out="$run_root/n13_exchange_aut.stdout"
n13_err="$run_root/n13_exchange_aut.stderr"
n14_out="$run_root/n14_flip_aut.stdout"
n14_err="$run_root/n14_flip_aut.stderr"

for target in "$n13_out" "$n13_err" "$n14_out" "$n14_err"; do
  if [[ -e "$target" ]]; then
    echo "refusing to overwrite existing output: $target" >&2
    exit 90
  fi
done

/usr/bin/time -f 'ELAPSED=%e MAXRSS_KB=%M EXIT=%x' \
  -o "$n13_err" \
  timeout 180s gap -q "$run_root/n13_exchange_aut.g" \
  >"$n13_out" 2>>"$n13_err"

/usr/bin/time -f 'ELAPSED=%e MAXRSS_KB=%M EXIT=%x' \
  -o "$n14_err" \
  timeout 180s gap -q -c \
  'n:=14;; Read("Agents/Kourovka/problems/21.52/runs/2026-08-18-r16-six-matching-n12-n14-rigidity/scratch/perfect_matching_flip_aut.g");' \
  >"$n14_out" 2>>"$n14_err"
