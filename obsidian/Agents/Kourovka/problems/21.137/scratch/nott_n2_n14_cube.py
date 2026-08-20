#!/usr/bin/env python3
"""Exhaust the frozen NOTT3-N2-N14-CUBESET carrier.

The carrier consists of f(t)=t+sum_{i=3}^{13} a_i t^i over F_3, with
composition f*g=f(g(t)) modulo t^14.  This script has no search parameters:
the CLI values are checked against the frozen manifest below.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
import time
from array import array
from pathlib import Path

P = 3
LOWEST = 3
TRUNCATE = 14
MAX_DEGREE = TRUNCATE - 1
COORDS = tuple(range(LOWEST, TRUNCATE))
CARRIER_SIZE = P ** len(COORDS)


def decode(code: int) -> list[int]:
    coeff = [0] * TRUNCATE
    coeff[1] = 1
    for degree in COORDS:
        code, coeff[degree] = divmod(code, P)
    return coeff


def encode(coeff: list[int]) -> int:
    code = 0
    place = 1
    for degree in COORDS:
        code += (coeff[degree] % P) * place
        place *= P
    return code


def tuple_string(code: int) -> str:
    coeff = decode(code)
    return ",".join(str(coeff[d]) for d in COORDS)


def compose(left_code: int, right_code: int) -> int:
    """Return f_left(f_right(t)) modulo t^14."""
    left = decode(left_code)
    right = decode(right_code)
    out = right[:]
    power = right[:]
    # Extend power successively from g^1 to g^degree.  Multiplication by g
    # uses its leading term t separately and its tail beginning in degree 3.
    for degree in range(2, TRUNCATE):
        new_power = [0] * TRUNCATE
        for n in range(degree, TRUNCATE):
            value = power[n - 1]
            upper = n - degree + 1
            for j in range(LOWEST, upper + 1):
                value += right[j] * power[n - j]
            new_power[n] = value % P
        power = new_power
        scalar = left[degree]
        if scalar:
            for n in range(degree, TRUNCATE):
                out[n] = (out[n] + scalar * power[n]) % P
    return encode(out)


def inverse(code: int) -> int:
    """Formal compositional inverse, solved coefficient-by-coefficient."""
    f = decode(code)
    g = [0] * TRUNCATE
    g[1] = 1
    powers = [[0] * TRUNCATE for _ in range(TRUNCATE)]
    powers[0][0] = 1
    powers[1][1] = 1
    for n in range(2, TRUNCATE):
        for degree in range(2, n + 1):
            value = 0
            # coefficient of t^n in g * g^(degree-1)
            for j in range(1, n + 1):
                value += g[j] * powers[degree - 1][n - j]
            powers[degree][n] = value % P
        correction = 0
        for degree in range(LOWEST, n + 1):
            correction += f[degree] * powers[degree][n]
        g[n] = (-correction) % P
        powers[1][n] = g[n]
    return encode(g)


def cube(code: int) -> int:
    square = compose(code, code)
    return compose(square, code)


def ninth_from_cube(cube_code: int) -> int:
    square = compose(cube_code, cube_code)
    return compose(square, cube_code)


def atomic_json(path: Path, payload: dict) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temp, path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def phase_record(artifact_dir: Path, name: str, started: float, payload: dict) -> None:
    payload = dict(payload)
    payload["phase"] = name
    payload["elapsed_seconds"] = round(time.monotonic() - started, 6)
    atomic_json(artifact_dir / f"{name}.json", payload)
    print(json.dumps(payload, sort_keys=True), flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--lowest-degree", type=int, required=True)
    parser.add_argument("--truncate", type=int, required=True)
    parser.add_argument("--exhaustive", action="store_true", required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    args = parser.parse_args()
    if (args.p, args.lowest_degree, args.truncate, args.exhaustive) != (P, LOWEST, TRUNCATE, True):
        parser.error("only the frozen p=3, lowest-degree=3, truncate=14 exhaustive carrier is allowed")

    artifact_dir = args.artifact_dir
    artifact_dir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    config = {
        "strategy_id": "NOTT3-N2-N14-CUBESET",
        "scope_id": "21.137/odd-prime-exponent-p2",
        "assignment_revision": 2,
        "orientation": "compose(left,right)=f_left(f_right(t)) mod t^14",
        "p": P,
        "lowest_degree": LOWEST,
        "truncate": TRUNCATE,
        "coordinates": list(COORDS),
        "carrier_size": CARRIER_SIZE,
        "python": sys.version,
        "platform": platform.platform(),
        "argv": sys.argv,
    }
    atomic_json(artifact_dir / "run-config.json", config)

    # G0: the base-3 codec is bijective and every tuple has a two-sided inverse.
    codec_misses = 0
    inverse_misses = []
    identity_misses = []
    for code in range(CARRIER_SIZE):
        if encode(decode(code)) != code:
            codec_misses += 1
        if compose(0, code) != code or compose(code, 0) != code:
            if len(identity_misses) < 4:
                identity_misses.append(code)
        inv = inverse(code)
        if compose(code, inv) != 0 or compose(inv, code) != 0:
            if len(inverse_misses) < 4:
                inverse_misses.append({"code": code, "inverse_code": inv})
    g0_pass = codec_misses == 0 and not identity_misses and not inverse_misses
    phase_record(artifact_dir, "g0-carrier-inverses", started, {
        "carrier_rows": CARRIER_SIZE,
        "distinct_tuple_codes": CARRIER_SIZE,
        "codec_misses": codec_misses,
        "identity_misses": identity_misses,
        "inverse_misses": inverse_misses,
        "carrier_closure_reason": "composition preserves leading t and zero t^2; coefficients 3..13 are reduced in F_3",
        "pass": g0_pass,
    })
    if not g0_pass:
        return 10

    # G1 and G2 share one complete pass.  The manifest is the literal map on
    # every input, not a generated subgroup.
    cube_codes = array("I")
    first_root: dict[int, int] = {}
    ninth_misses = []
    first_nonidentity_cube = None
    manifest_path = artifact_dir / "cube-manifest.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="\n") as manifest:
        manifest.write("root_code\troot_tuple\tcube_code\tcube_tuple\tninth_code\n")
        for code in range(CARRIER_SIZE):
            c = cube(code)
            n = ninth_from_cube(c)
            cube_codes.append(c)
            first_root.setdefault(c, code)
            if c != 0 and first_nonidentity_cube is None:
                first_nonidentity_cube = {"root_code": code, "root_tuple": tuple_string(code), "cube_code": c, "cube_tuple": tuple_string(c)}
            if n != 0 and len(ninth_misses) < 4:
                ninth_misses.append({"root_code": code, "root_tuple": tuple_string(code), "ninth_code": n, "ninth_tuple": tuple_string(n)})
            manifest.write(f"{code}\t{tuple_string(code)}\t{c}\t{tuple_string(c)}\t{n}\n")
    g1_pass = not ninth_misses and first_nonidentity_cube is not None
    phase_record(artifact_dir, "g1-exponent", started, {
        "tested_rows": CARRIER_SIZE,
        "ninth_power_misses": ninth_misses,
        "first_nonidentity_cube": first_nonidentity_cube,
        "exponent_exactly_9": g1_pass,
        "pass": g1_pass,
    })
    if not g1_pass:
        return 11

    p_codes = sorted(first_root)
    p_set = set(p_codes)
    cube_set_path = artifact_dir / "literal-cube-set.tsv"
    with cube_set_path.open("w", encoding="utf-8", newline="\n") as values:
        values.write("cube_code\tcube_tuple\tfirst_root_code\tfirst_root_tuple\n")
        for value in p_codes:
            root = first_root[value]
            values.write(f"{value}\t{tuple_string(value)}\t{root}\t{tuple_string(root)}\n")
    power_of_three = False
    temp_size = len(p_codes)
    while temp_size and temp_size % P == 0:
        temp_size //= P
    power_of_three = temp_size == 1
    phase_record(artifact_dir, "g2-literal-cube-set", started, {
        "input_rows": len(cube_codes),
        "literal_cube_set_size": len(p_codes),
        "size_is_power_of_3": power_of_three,
        "manifest_sha256": sha256(manifest_path),
        "literal_cube_set_sha256": sha256(cube_set_path),
        "pass": power_of_three,
    })
    if not power_of_three:
        return 12

    # G3: exact Cayley closure of the literal image; do not generate a subgroup.
    closure_defect = None
    tested_pairs = 0
    for left in p_codes:
        for right in p_codes:
            product = compose(left, right)
            tested_pairs += 1
            if product not in p_set:
                closure_defect = {
                    "left_cube_code": left,
                    "left_cube_tuple": tuple_string(left),
                    "left_root_code": first_root[left],
                    "right_cube_code": right,
                    "right_cube_tuple": tuple_string(right),
                    "right_root_code": first_root[right],
                    "product_code": product,
                    "product_tuple": tuple_string(product),
                }
                break
        if closure_defect is not None:
            break
    inverse_membership_misses = []
    if closure_defect is None:
        for value in p_codes:
            inv = inverse(value)
            if inv not in p_set and len(inverse_membership_misses) < 4:
                inverse_membership_misses.append({"value_code": value, "inverse_code": inv})
    g3_pass = 0 in p_set and closure_defect is None and not inverse_membership_misses
    phase_record(artifact_dir, "g3-subgroup-closure", started, {
        "literal_cube_set_size": len(p_codes),
        "ordered_pairs_required": len(p_codes) ** 2,
        "ordered_pairs_tested": tested_pairs,
        "identity_in_literal_set": 0 in p_set,
        "closure_defect": closure_defect,
        "inverse_membership_misses": inverse_membership_misses,
        "pass": g3_pass,
    })
    if not g3_pass:
        return 13

    # G4: a first unequal ordered product proves nonabelianity; otherwise exhaust.
    noncommuting = None
    commutativity_pairs = 0
    for left in p_codes:
        for right in p_codes:
            lr = compose(left, right)
            rl = compose(right, left)
            commutativity_pairs += 1
            if lr != rl:
                noncommuting = {
                    "left_cube_code": left,
                    "left_cube_tuple": tuple_string(left),
                    "left_root_code": first_root[left],
                    "left_root_tuple": tuple_string(first_root[left]),
                    "right_cube_code": right,
                    "right_cube_tuple": tuple_string(right),
                    "right_root_code": first_root[right],
                    "right_root_tuple": tuple_string(first_root[right]),
                    "left_then_right_code": lr,
                    "left_then_right_tuple": tuple_string(lr),
                    "right_then_left_code": rl,
                    "right_then_left_tuple": tuple_string(rl),
                }
                break
        if noncommuting is not None:
            break
    g4_pass = noncommuting is not None
    phase_record(artifact_dir, "g4-nonabelianity", started, {
        "ordered_pairs_required_if_abelian": len(p_codes) ** 2,
        "ordered_pairs_tested": commutativity_pairs,
        "noncommuting_cube_values": noncommuting,
        "literal_cube_set_is_abelian": noncommuting is None,
        "pass_for_counterexample": g4_pass,
    })

    files = [artifact_dir / name for name in (
        "run-config.json", "g0-carrier-inverses.json", "g1-exponent.json",
        "cube-manifest.tsv", "literal-cube-set.tsv", "g2-literal-cube-set.json",
        "g3-subgroup-closure.json", "g4-nonabelianity.json",
    )]
    certificate = {
        "strategy_id": "NOTT3-N2-N14-CUBESET",
        "scope_id": "21.137/odd-prime-exponent-p2",
        "assignment_revision": 2,
        "candidate_counterexample": g4_pass,
        "carrier_order": CARRIER_SIZE,
        "literal_cube_set_size": len(p_codes),
        "hashes": {path.name: sha256(path) for path in files},
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "exit_meaning": "0=candidate hit; 14=closed but abelian; 10..13=hard-gate failure",
    }
    atomic_json(artifact_dir / "g5-certificate.json", certificate)
    print(json.dumps(certificate, sort_keys=True), flush=True)
    return 0 if g4_pass else 14


if __name__ == "__main__":
    raise SystemExit(main())
