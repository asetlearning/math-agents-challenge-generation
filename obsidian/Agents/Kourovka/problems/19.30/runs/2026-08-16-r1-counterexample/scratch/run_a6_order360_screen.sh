#!/usr/bin/env bash
set -euo pipefail

base='Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch'
gap_script="$base/a6_order360_vanishing_collision.g"
verifier="$base/verify_a6_order360_output.py"
manifest="$base/a6_order360_frozen.sha256"
output="$base/a6_order360_vanishing_collision.out"
verification="$base/a6_order360_vanishing_collision.verify"

if [[ ! -f 'Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json' ]]; then
    printf '%s\n' 'ERROR: run from the vault root' >&2
    exit 2
fi

/usr/bin/sha256sum --check "$manifest"

if [[ -e "$output" || -e "$verification" || -e "$output.sha256" ]]; then
    printf '%s\n' 'ERROR: frozen output path already exists; refusing to overwrite' >&2
    exit 2
fi

# GAP is single-process here.  Hard caps: 2 GiB virtual address space and 870
# CPU seconds.  The lease command applies a separate 960-second wall cap to this
# entire wrapper.
/usr/bin/prlimit --as=2147483648 --cpu=870 /usr/bin/gap -q "$gap_script" \
    >"$output" 2>&1

/usr/bin/python3 "$verifier" "$output" >"$verification"
/usr/bin/sha256sum "$output" "$verification" >"$output.sha256"
