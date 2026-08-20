#!/usr/bin/env python3
"""Audit and compare every submitted and independently reconstructed cell."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path("Agents/Kourovka/problems/20.115")
RUN = ROOT / "runs/2026-08-17-r5-su35-direct/scratch"
VERIFY = ROOT / "verification/scratch"
CLAIMANT_SCRIPT = RUN / "su35_exact_scan.g"
CLAIMANT_OUTPUT = RUN / "su35_exact_scan.out"
VALIDATOR_OUTPUT = VERIFY / "validator_su35_scan.out"
REPORT = VERIFY / "validator_su35_compare.json"

EXPECTED_HASHES = {
    CLAIMANT_SCRIPT: "47b67f1ee3a23f7e954c5dbbe7a35d2d10671e5743ba1e80a2ddf9c8effffeaa",
    CLAIMANT_OUTPUT: "313d8c9fcabc541ccf1ca88cf724241a4f1f1404a940e7b4caa70ce1b84bcfce",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_value(value: str) -> str:
    return re.sub(r"\s+", "", value)


def logical_blocks(text: str, prefix: str, next_prefix: str) -> list[str]:
    pattern = rf"(?m)^{re.escape(prefix)}\t(.*?)(?=^{re.escape(prefix)}\t|^{re.escape(next_prefix)}\t|\Z)"
    return [block.replace("\r", "").replace("\n", "") for block in re.findall(pattern, text, re.S)]


def parse_claimant(text: str) -> dict:
    classes = {}
    for match in re.finditer(
        r"(?m)^CLASS\t(\d+)\tlabel=([^\t]+)\torder=(\d+)\tsize=(\d+)\tcentral=(true|false)$",
        text,
    ):
        index, label, order, size, central = match.groups()
        classes[int(index)] = {
            "label": label,
            "order": int(order),
            "size": int(size),
            "central": central == "true",
        }

    rows = {
        int(index): int(degree)
        for index, degree in re.findall(r"(?m)^ROW\t(\d+)\tdegree=(\d+)$", text)
    }

    cells = {}
    cell_pattern = re.compile(
        r"^row=(\d+)\tclass=(\d+)\tlabel=([^\t]+)\tdegree=(\d+)"
        r"\tclass_order=(\d+)\tvalue=(.*?)\tnonzero=(true|false)"
        r"\tproduct=(\d+)\tremainder=(\d+)\tviolation=(true|false)$"
    )
    for block in logical_blocks(text, "CELL", "SUMMARY"):
        match = cell_pattern.match(block)
        if not match:
            raise ValueError(f"unparsed claimant cell: {block[:180]}")
        row, cls, label, degree, order, value, nonzero, product, remainder, violation = match.groups()
        coordinate = (int(row), int(cls))
        if coordinate in cells:
            raise ValueError(f"duplicate claimant coordinate {coordinate}")
        cells[coordinate] = {
            "label": label,
            "degree": int(degree),
            "order": int(order),
            "value": normalize_value(value),
            "nonzero": nonzero == "true",
            "product": int(product),
            "remainder": int(remainder),
            "violation": violation == "true",
        }

    summaries = {
        name: int(value)
        for name, value in re.findall(r"(?m)^SUMMARY\t([^\t]+)\t\s*(\d+)$", text)
    }
    return {"classes": classes, "rows": rows, "cells": cells, "summary": summaries}


def parse_validator(text: str) -> dict:
    classes = {}
    for match in re.finditer(
        r"(?m)^VCLASS\tindex=(\d+)\tlabel=([^\t]+)\torder=(\d+)\tsize=(\d+)\tcentral=(true|false)$",
        text,
    ):
        index, label, order, size, central = match.groups()
        classes[int(index)] = {
            "label": label,
            "order": int(order),
            "size": int(size),
            "central": central == "true",
        }

    rows = {
        int(index): int(degree)
        for index, degree in re.findall(r"(?m)^VROW\tindex=(\d+)\tdegree=(\d+)$", text)
    }

    cells = {}
    cell_pattern = re.compile(
        r"^row=(\d+)\tclass=(\d+)\tlabel=([^\t]+)\tdegree=(\d+)"
        r"\tclass_order=(\d+)\tvalue=(.*?)\tnonzero=(true|false)"
        r"\tproduct=(\d+)\tdivides=(true|false)$"
    )
    for block in logical_blocks(text, "VCELL", "VSUMMARY"):
        match = cell_pattern.match(block)
        if not match:
            raise ValueError(f"unparsed validator cell: {block[:180]}")
        row, cls, label, degree, order, value, nonzero, product, divides = match.groups()
        coordinate = (int(row), int(cls))
        if coordinate in cells:
            raise ValueError(f"duplicate validator coordinate {coordinate}")
        cells[coordinate] = {
            "label": label,
            "degree": int(degree),
            "order": int(order),
            "value": normalize_value(value),
            "nonzero": nonzero == "true",
            "product": int(product),
            "divides": divides == "true",
        }

    summaries = {
        name: int(value)
        for name, value in re.findall(r"(?m)^VSUMMARY\t([^\t]+)\t\s*(\d+)$", text)
    }
    metadata = dict(re.findall(r"(?m)^VMETA\t([^\t]+)\t(.*)$", text))
    return {
        "classes": classes,
        "rows": rows,
        "cells": cells,
        "summary": summaries,
        "metadata": metadata,
    }


def audit() -> tuple[dict, list[str]]:
    errors: list[str] = []
    observed_hashes = {str(path): sha256(path) for path in EXPECTED_HASHES}
    for path, expected in EXPECTED_HASHES.items():
        if observed_hashes[str(path)] != expected:
            errors.append(f"hash mismatch: {path}")

    claimant = parse_claimant(CLAIMANT_OUTPUT.read_text(encoding="utf-8"))
    validator = parse_validator(VALIDATOR_OUTPUT.read_text(encoding="utf-8"))
    expected_coordinates = {(row, cls) for row in range(1, 41) for cls in range(1, 41)}

    if set(claimant["classes"]) != set(range(1, 41)):
        errors.append("claimant class index set is not 1..40")
    if set(validator["classes"]) != set(range(1, 41)):
        errors.append("validator class index set is not 1..40")
    if set(claimant["rows"]) != set(range(1, 41)):
        errors.append("claimant row index set is not 1..40")
    if set(validator["rows"]) != set(range(1, 41)):
        errors.append("validator row index set is not 1..40")
    if set(claimant["cells"]) != expected_coordinates:
        errors.append("claimant coordinate grid is not exactly 40x40")
    if set(validator["cells"]) != expected_coordinates:
        errors.append("validator coordinate grid is not exactly 40x40")

    if claimant["classes"] != validator["classes"]:
        errors.append("class records differ")
    if claimant["rows"] != validator["rows"]:
        errors.append("row degree records differ")

    claimant_nonzero = 0
    claimant_violations = 0
    validator_nonzero = 0
    validator_failures = 0
    cell_mismatches = []
    internal_errors = []

    for coordinate in sorted(expected_coordinates):
        if coordinate not in claimant["cells"] or coordinate not in validator["cells"]:
            continue
        original = claimant["cells"][coordinate]
        fresh = validator["cells"][coordinate]
        claimant_nonzero += int(original["nonzero"])
        claimant_violations += int(original["violation"])
        validator_nonzero += int(fresh["nonzero"])
        validator_failures += int(fresh["nonzero"] and not fresh["divides"])

        expected_product = original["degree"] * original["order"]
        expected_remainder = 378000 % expected_product
        expected_violation = original["nonzero"] and expected_remainder != 0
        canonical_nonzero = original["value"] != "0"
        if (
            original["product"] != expected_product
            or original["remainder"] != expected_remainder
            or original["violation"] != expected_violation
            or original["nonzero"] != canonical_nonzero
        ):
            internal_errors.append(coordinate)

        compared_fields = ("label", "degree", "order", "value", "nonzero", "product")
        if any(original[field] != fresh[field] for field in compared_fields):
            cell_mismatches.append(coordinate)
        if fresh["divides"] != (fresh["product"] != 0 and 378000 % fresh["product"] == 0):
            internal_errors.append(coordinate)

    if internal_errors:
        errors.append(f"internal arithmetic/value errors at {len(set(internal_errors))} cells")
    if cell_mismatches:
        errors.append(f"claimant/validator mismatches at {len(cell_mismatches)} cells")
    if claimant_nonzero != 987 or validator_nonzero != 987:
        errors.append("nonzero count is not 987 in both reconstructions")
    if claimant_violations != 0 or validator_failures != 0:
        errors.append("a failed divisibility was found")

    expected_claimant_summary = {
        "TOTAL_PAIRS": 1600,
        "NONZERO_PAIRS": 987,
        "VIOLATIONS": 0,
    }
    expected_validator_summary = {
        "CELLS": 1600,
        "NONZERO": 987,
        "FAILED_DIVISIBILITIES": 0,
    }
    if claimant["summary"] != expected_claimant_summary:
        errors.append("claimant summary mismatch")
    if validator["summary"] != expected_validator_summary:
        errors.append("validator summary mismatch")

    required_metadata = {
        "IDENTIFIER": "3.U3(5)",
        "ORDINARY": "true",
        "PERFECT": "true",
        "QUASISIMPLE": "true",
        "GROUP_ORDER": "378000",
        "SU3_ORDER_FORMULA": "378000",
        "CENTRE_FORMULA": "3",
        "CENTRE_ORDER": "3",
        "QUOTIENT_ORDER": "126000",
        "NUMBER_ROWS": "40",
        "NUMBER_CLASSES": "40",
        "CLASS_SIZE_SUM": "378000",
        "DEGREE_SQUARE_SUM": "378000",
        "ALL_VALUES_CYCLOTOMIC": "true",
        "ORTHOGONALITY_FAILURES": "0",
    }
    for key, expected in required_metadata.items():
        if validator["metadata"].get(key) != expected:
            errors.append(f"validator metadata mismatch: {key}")
    if "SU(3,5)" not in validator["metadata"].get("INFO_TEXT", ""):
        errors.append("validator info text omits SU(3,5)")

    ordered = sorted(expected_coordinates)
    nonzero_stream = "".join("1" if claimant["cells"].get(c, {}).get("nonzero") else "0" for c in ordered)
    value_stream = "\n".join(
        f"{r},{c}:{claimant['cells'].get((r, c), {}).get('value', '<missing>')}"
        for r, c in ordered
    )
    arithmetic_stream = "\n".join(
        f"{r},{c}:{claimant['cells'].get((r, c), {}).get('product', '<missing>')}:{claimant['cells'].get((r, c), {}).get('remainder', '<missing>')}"
        for r, c in ordered
    )

    report = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "observed_hashes": observed_hashes,
        "claimant": {
            "classes": len(claimant["classes"]),
            "rows": len(claimant["rows"]),
            "cells": len(claimant["cells"]),
            "nonzero": claimant_nonzero,
            "failed_divisibilities": claimant_violations,
        },
        "validator": {
            "classes": len(validator["classes"]),
            "rows": len(validator["rows"]),
            "cells": len(validator["cells"]),
            "nonzero": validator_nonzero,
            "failed_divisibilities": validator_failures,
            "gap_version": validator["metadata"].get("GAP_VERSION"),
            "ctbllib_version": validator["metadata"].get("CTBLLIB_VERSION"),
        },
        "all_1600_coordinates_compared": not cell_mismatches
        and set(claimant["cells"]) == expected_coordinates
        and set(validator["cells"]) == expected_coordinates,
        "cell_mismatch_count": len(cell_mismatches),
        "internal_error_count": len(set(internal_errors)),
        "fingerprints": {
            "row_major_nonzero_bits_sha256": hashlib.sha256(nonzero_stream.encode()).hexdigest(),
            "row_major_exact_values_sha256": hashlib.sha256(value_stream.encode()).hexdigest(),
            "row_major_product_remainder_sha256": hashlib.sha256(arithmetic_stream.encode()).hexdigest(),
        },
    }
    return report, errors


def main() -> int:
    report, errors = audit()
    with REPORT.open("x", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

