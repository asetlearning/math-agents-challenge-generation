#!/usr/bin/env python3
"""Audit and compare two independently produced 869-pair certificates."""

from __future__ import annotations

import hashlib
from pathlib import Path


GROUP_ORDER = 24_261_120
ROOT = Path("Agents/Kourovka/problems/20.115")
VALIDATOR = ROOT / "verification/scratch/l43_graph_extensions_validator.out"
CLAIMANT = (
    ROOT
    / "runs/2026-08-17-r3-l43-graph-extensions/scratch"
    / "l43_graph_extensions_exact_scan.out"
)

GRIDS = {
    "2.L4(3).2_2": (set(range(50, 70)), set(range(41, 70)), 84),
    "2.L4(3).2_3": (set(range(35, 52)), set(range(35, 52)), 36),
}


def parse_validator(path: Path) -> dict[tuple[str, int, int], tuple[str, ...]]:
    result: dict[tuple[str, int, int], tuple[str, ...]] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.startswith("PAIR|"):
            continue
        fields = raw.split("|")
        if len(fields) != 12:
            raise AssertionError(f"validator field count: {raw}")
        (
            _,
            table,
            row,
            row_name,
            degree,
            class_pos,
            class_name,
            class_order,
            value,
            nonzero,
            product,
            remainder,
        ) = fields
        key = (table, int(row), int(class_pos))
        if key in result:
            raise AssertionError(f"duplicate validator key: {key}")
        result[key] = (
            row_name,
            degree,
            class_name,
            class_order,
            value,
            nonzero,
            product,
            remainder,
        )
    return result


def parse_claimant(path: Path) -> dict[tuple[str, int, int], tuple[str, ...]]:
    result: dict[tuple[str, int, int], tuple[str, ...]] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.startswith("PAIR|"):
            continue
        record: dict[str, str] = {}
        for item in raw.split("|")[1:]:
            name, value = item.split("=", 1)
            record[name] = value
        key = (record["table"], int(record["row"]), int(record["class"]))
        if key in result:
            raise AssertionError(f"duplicate claimant key: {key}")
        if record["kernel_positions"] != "[ 1 ]":
            raise AssertionError(f"nonfaithful claimant row at {key}")
        divides = int(record["remainder"]) == 0
        nonzero = record["value"] != "0"
        if record["divides"] != str(divides).lower():
            raise AssertionError(f"claimant divides flag mismatch at {key}")
        if record["nonzero"] != str(nonzero).lower():
            raise AssertionError(f"claimant nonzero flag mismatch at {key}")
        if record["violation"] != str(nonzero and not divides).lower():
            raise AssertionError(f"claimant violation flag mismatch at {key}")
        result[key] = (
            record["row_label"],
            record["degree"],
            record["class_label"],
            record["class_order"],
            record["value"],
            record["nonzero"],
            record["product"],
            record["remainder"],
        )
    return result


def audit(records: dict[tuple[str, int, int], tuple[str, ...]], label: str) -> None:
    expected_keys: set[tuple[str, int, int]] = set()
    for table, (rows, classes, _) in GRIDS.items():
        expected_keys.update((table, row, class_pos) for row in rows for class_pos in classes)
    if set(records) != expected_keys:
        missing = sorted(expected_keys - set(records))
        extra = sorted(set(records) - expected_keys)
        raise AssertionError(f"{label} grid mismatch: missing={missing}, extra={extra}")

    for key, data in records.items():
        _, degree, _, class_order, value, nonzero, product, remainder = data
        degree_int = int(degree)
        class_order_int = int(class_order)
        product_int = int(product)
        remainder_int = int(remainder)
        if product_int != degree_int * class_order_int:
            raise AssertionError(f"{label} product mismatch at {key}")
        if remainder_int != GROUP_ORDER % product_int:
            raise AssertionError(f"{label} remainder mismatch at {key}")
        if nonzero != str(value != "0").lower():
            raise AssertionError(f"{label} exact-zero mismatch at {key}")

    print(f"AUDIT|{label}|pairs={len(records)}")
    total_nonzero = 0
    total_violations = 0
    for table, (_, _, expected_nonzero) in GRIDS.items():
        subset = [data for key, data in records.items() if key[0] == table]
        nonzero_count = sum(data[5] == "true" for data in subset)
        violations = sum(data[5] == "true" and int(data[7]) != 0 for data in subset)
        if nonzero_count != expected_nonzero:
            raise AssertionError(f"{label} nonzero count mismatch for {table}")
        if violations != 0:
            raise AssertionError(f"{label} violation found for {table}")
        total_nonzero += nonzero_count
        total_violations += violations
        print(
            f"AUDIT|{label}|table={table}|pairs={len(subset)}"
            f"|nonzero={nonzero_count}|violations={violations}"
        )
    print(
        f"AUDIT|{label}|total_nonzero={total_nonzero}"
        f"|total_violations={total_violations}"
    )


def normalized_lines(records: dict[tuple[str, int, int], tuple[str, ...]], *, nonzero_only: bool) -> list[str]:
    lines: list[str] = []
    for key in sorted(records):
        data = records[key]
        if nonzero_only and data[5] != "true":
            continue
        fields = (*key, *data)
        lines.append("|".join(str(field) for field in fields))
    return lines


def digest(lines: list[str]) -> str:
    payload = ("\n".join(lines) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


validator = parse_validator(VALIDATOR)
claimant = parse_claimant(CLAIMANT)
audit(validator, "validator")
audit(claimant, "claimant")

if validator != claimant:
    differing = sorted(key for key in set(validator) | set(claimant) if validator.get(key) != claimant.get(key))
    raise AssertionError(f"exact pair certificates differ at {differing[:10]}")

all_lines = normalized_lines(validator, nonzero_only=False)
nonzero_lines = normalized_lines(validator, nonzero_only=True)
print(f"COMPARE|exact_pair_records_equal=true|count={len(all_lines)}")
print(f"COMPARE|exact_nonzero_records_equal=true|count={len(nonzero_lines)}")
print(f"DIGEST|all_pairs_sha256={digest(all_lines)}")
print(f"DIGEST|nonzero_pairs_sha256={digest(nonzero_lines)}")
print("AUDIT_FINAL|PASS")
