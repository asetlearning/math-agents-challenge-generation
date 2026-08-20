#!/usr/bin/env python3
"""Strict cross-checker for the fixed-A6 order-360 Validator run.

This parser deliberately understands the submitted GAP header continuation that
made the claimant's wrapper exit 1.  It validates both artifacts from primitive
row data, then compares all 162 independently recomputed invariant rows.
"""

from __future__ import annotations

import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


EXPECTED_CLAIMANT_SHA256 = (
    "6142ece4f7daa7b08d330bce798fceade8e4de45a6b4a27637ff0364d051421e"
)
EXPECTED_HEADER = (
    "ROW_HEADER\tindex\tsize\tis_target_id\tvanishing_order_set\t"
    "equals_target_set\tcollision"
)
EXPECTED_TARGET_SET = [2, 3, 4, 5]
EXPECTED_TARGET_ID = [360, 118]
EXPECTED_COUNT = 162


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_bool(text: str) -> bool:
    require(text in {"true", "false"}, f"invalid Boolean token: {text!r}")
    return text == "true"


def parse_int(text: str) -> int:
    require(re.fullmatch(r"0|[1-9][0-9]*", text) is not None,
            f"invalid nonnegative integer: {text!r}")
    return int(text)


def parse_int_list(text: str) -> list[int]:
    require(re.fullmatch(r"\[\s*(?:[0-9]+(?:\s*,\s*[0-9]+)*)?\s*\]", text)
            is not None, f"invalid GAP integer list: {text!r}")
    body = text[1:-1].strip()
    if not body:
        return []
    return [int(piece.strip()) for piece in body.split(",")]


@dataclass
class ClaimantRow:
    index: int
    size: int
    is_target: bool
    vanishing_orders: list[int]
    equals_target: bool
    collision: bool


@dataclass
class IndependentRow:
    index: int
    size: int | None = None
    identifier: list[int] | None = None
    number_of_classes: int | None = None
    class_orders: list[int] | None = None
    zero_counts: list[int] | None = None
    vanishing_positions: list[int] | None = None
    vanishing_orders: list[int] | None = None
    equals_target: bool | None = None


def parse_claimant(path: Path) -> tuple[dict[int, ClaimantRow], dict[str, str]]:
    require(sha256(path) == EXPECTED_CLAIMANT_SHA256,
            "submitted raw output hash differs from the frozen reviewed artifact")
    physical = path.read_text(encoding="utf-8").splitlines()

    logical: list[str] = []
    continuation_count = 0
    position = 0
    while position < len(physical):
        line = physical[position]
        if line.startswith("ROW_HEADER") and line.endswith("\\"):
            require(position + 1 < len(physical), "truncated continued header")
            continuation_count += 1
            logical.append(line[:-1] + physical[position + 1])
            position += 2
            continue
        logical.append(line)
        position += 1

    require(continuation_count == 1,
            "submitted artifact does not have exactly one wrapped header")
    require(logical.count(EXPECTED_HEADER) == 1,
            "continued header does not normalize to the required schema")

    metadata: dict[str, str] = {}
    summary: dict[str, str] = {}
    rows: dict[int, ClaimantRow] = {}
    for line in logical:
        if line == EXPECTED_HEADER:
            continue
        if line.startswith("META\t"):
            fields = line.split("\t", 2)
            require(len(fields) == 3, f"malformed META line: {line!r}")
            require(fields[1] not in metadata, f"duplicate META key {fields[1]}")
            metadata[fields[1]] = fields[2]
            continue
        if line.startswith("ROW\t"):
            fields = line.split("\t")
            require(len(fields) == 7, f"malformed ROW line: {line!r}")
            index = parse_int(fields[1])
            require(index not in rows, f"duplicate submitted row {index}")
            rows[index] = ClaimantRow(
                index=index,
                size=parse_int(fields[2]),
                is_target=parse_bool(fields[3]),
                vanishing_orders=parse_int_list(fields[4]),
                equals_target=parse_bool(fields[5]),
                collision=parse_bool(fields[6]),
            )
            continue
        if line.startswith("SUMMARY\t"):
            fields = line.split("\t", 2)
            require(len(fields) == 3, f"malformed SUMMARY line: {line!r}")
            require(fields[1] not in summary, f"duplicate SUMMARY key {fields[1]}")
            summary[fields[1]] = fields[2]
            continue
        raise AssertionError(f"unrecognized submitted output line: {line!r}")

    require(parse_int(metadata["order"]) == 360, "submitted META order is not 360")
    require(parse_int(metadata["number_small_groups"]) == EXPECTED_COUNT,
            "submitted catalogue count is not 162")
    require(parse_int_list(metadata["target_id"]) == EXPECTED_TARGET_ID,
            "submitted target ID is not [360,118]")
    target_set = parse_int_list(metadata["target_vanishing_order_set"])
    require(target_set == EXPECTED_TARGET_SET,
            "submitted A6 invariant is not [2,3,4,5]")
    require(sorted(rows) == list(range(1, EXPECTED_COUNT + 1)),
            "submitted rows are not exactly indices 1..162")

    target_rows: list[int] = []
    equal_rows: list[int] = []
    collision_rows: list[int] = []
    for index in range(1, EXPECTED_COUNT + 1):
        row = rows[index]
        require(row.size == 360, f"submitted row {index} has size {row.size}")
        require(row.vanishing_orders == sorted(set(row.vanishing_orders)),
                f"submitted row {index} invariant is not a strict sorted set")
        expected_target_flag = index == EXPECTED_TARGET_ID[1]
        expected_equality = row.vanishing_orders == target_set
        expected_collision = expected_equality and not expected_target_flag
        require(row.is_target == expected_target_flag,
                f"submitted row {index} target flag is inconsistent")
        require(row.equals_target == expected_equality,
                f"submitted row {index} equality flag is inconsistent")
        require(row.collision == expected_collision,
                f"submitted row {index} collision flag is inconsistent")
        if row.is_target:
            target_rows.append(index)
        if row.equals_target:
            equal_rows.append(index)
        if row.collision:
            collision_rows.append(index)

    require(parse_int(summary["row_count"]) == EXPECTED_COUNT,
            "submitted summary row count is inconsistent")
    require(parse_int_list(summary["target_rows"]) == target_rows,
            "submitted target-row summary is inconsistent")
    require(parse_int_list(summary["equal_set_rows"]) == equal_rows,
            "submitted equal-row summary is inconsistent")
    require(parse_int_list(summary["collision_rows"]) == collision_rows,
            "submitted collision-row summary is inconsistent")
    require(parse_int(summary["collision_count"]) == len(collision_rows),
            "submitted collision count is inconsistent")
    require(parse_bool(summary["complete"]), "submitted complete flag is false")
    require(target_rows == [118], "submitted target rows are not [118]")
    require(equal_rows == [118], "submitted equality rows are not [118]")
    require(collision_rows == [], "submitted output contains a collision")
    return rows, metadata


def parse_independent(path: Path) -> tuple[dict[int, IndependentRow], dict[str, str]]:
    rows: dict[int, IndependentRow] = {}
    metadata: dict[str, str] = {}
    target: dict[str, object] = {}
    summary_fields: list[str] | None = None
    validation_complete = False

    def row_for(index: int) -> IndependentRow:
        require(1 <= index <= EXPECTED_COUNT, f"independent row index out of range: {index}")
        if index not in rows:
            rows[index] = IndependentRow(index=index)
        return rows[index]

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(("RUN\t", "GAP_VERSION\t", "SMALLGRP_VERSION\t",
                            "CTBLLIB_VERSION\t", "DEFINITION\t", "CATALOGUE_COUNT\t")):
            key, value = line.split("\t", 1)
            require(key not in metadata, f"duplicate independent metadata key {key}")
            metadata[key] = value
            continue
        if line.startswith("TARGET\t"):
            fields = line.split("\t")
            require(fields[:2] == ["TARGET", "SIZE"] and len(fields) == 7,
                    f"malformed TARGET line: {line!r}")
            require(fields[3] == "IS_SIMPLE" and fields[5] == "ID_GROUP",
                    f"malformed TARGET labels: {line!r}")
            target["size"] = parse_int(fields[2])
            target["simple"] = parse_bool(fields[4])
            target["id"] = parse_int_list(fields[6])
            continue
        target_prefixes = {
            "TARGET_CLASS_ORDERS": "class_orders",
            "TARGET_ZERO_COUNTS": "zero_counts",
            "TARGET_VANISHING_CLASS_POSITIONS": "positions",
            "TARGET_VANISHING_ORDER_SET": "orders",
        }
        matched_target = False
        for prefix, key in target_prefixes.items():
            if line.startswith(prefix + "\t"):
                require(key not in target, f"duplicate target field {key}")
                target[key] = parse_int_list(line.split("\t", 1)[1])
                matched_target = True
                break
        if matched_target:
            continue
        if line.startswith("GROUP\t"):
            fields = line.split("\t")
            require(len(fields) == 8 and fields[2] == "SIZE"
                    and fields[4] == "ID_GROUP"
                    and fields[6] == "NUMBER_OF_CLASSES",
                    f"malformed GROUP line: {line!r}")
            index = parse_int(fields[1])
            row = row_for(index)
            require(row.size is None, f"duplicate GROUP base row {index}")
            row.size = parse_int(fields[3])
            row.identifier = parse_int_list(fields[5])
            row.number_of_classes = parse_int(fields[7])
            continue
        simple_row_prefixes = {
            "GROUP_CLASS_ORDERS": "class_orders",
            "GROUP_ZERO_COUNTS": "zero_counts",
            "GROUP_VANISHING_CLASS_POSITIONS": "vanishing_positions",
        }
        matched_row = False
        for prefix, attribute in simple_row_prefixes.items():
            if line.startswith(prefix + "\t"):
                fields = line.split("\t", 2)
                require(len(fields) == 3, f"malformed {prefix} line")
                row = row_for(parse_int(fields[1]))
                require(getattr(row, attribute) is None,
                        f"duplicate {attribute} for row {row.index}")
                setattr(row, attribute, parse_int_list(fields[2]))
                matched_row = True
                break
        if matched_row:
            continue
        if line.startswith("GROUP_VANISHING_ORDER_SET\t"):
            fields = line.split("\t")
            require(len(fields) == 5 and fields[3] == "EQUALS_TARGET_SET",
                    f"malformed GROUP_VANISHING_ORDER_SET line: {line!r}")
            row = row_for(parse_int(fields[1]))
            require(row.vanishing_orders is None and row.equals_target is None,
                    f"duplicate invariant line for row {row.index}")
            row.vanishing_orders = parse_int_list(fields[2])
            row.equals_target = parse_bool(fields[4])
            continue
        if line.startswith("SUMMARY\t"):
            require(summary_fields is None, "duplicate independent SUMMARY")
            summary_fields = line.split("\t")
            continue
        if line == "VALIDATION_COMPLETE\ttrue":
            require(not validation_complete, "duplicate VALIDATION_COMPLETE")
            validation_complete = True
            continue
        raise AssertionError(f"unrecognized independent output line: {line!r}")

    require(metadata.get("RUN") == "VALIDATOR-INDEPENDENT-A6-ORDER360",
            "independent run identifier is wrong")
    require(metadata.get("CATALOGUE_COUNT") == str(EXPECTED_COUNT),
            "independent catalogue count is not 162")
    require(validation_complete, "independent VALIDATION_COMPLETE is absent")

    require(target.get("size") == 360, "independent target size is not 360")
    require(target.get("simple") is True, "independent target is not simple")
    require(target.get("id") == EXPECTED_TARGET_ID,
            "independent target ID is not [360,118]")
    target_class_orders = target.get("class_orders")
    target_zero_counts = target.get("zero_counts")
    target_positions = target.get("positions")
    target_orders = target.get("orders")
    require(isinstance(target_class_orders, list)
            and isinstance(target_zero_counts, list)
            and isinstance(target_positions, list)
            and isinstance(target_orders, list),
            "independent target class data are incomplete")
    require(len(target_class_orders) == len(target_zero_counts),
            "target class-order and zero-count lengths differ")
    expected_target_positions = [
        position for position, count in enumerate(target_zero_counts, start=1)
        if count > 0
    ]
    require(target_positions == expected_target_positions,
            "target vanishing positions do not match zero counts")
    derived_target_orders = sorted({
        target_class_orders[position - 1] for position in target_positions
    })
    require(target_orders == derived_target_orders == EXPECTED_TARGET_SET,
            "target invariant does not derive exactly as [2,3,4,5]")

    require(sorted(rows) == list(range(1, EXPECTED_COUNT + 1)),
            "independent rows are not exactly indices 1..162")
    equal_indices: list[int] = []
    for index in range(1, EXPECTED_COUNT + 1):
        row = rows[index]
        require(row.size == 360, f"independent row {index} has wrong size")
        require(row.identifier == [360, index],
                f"independent row {index} has wrong IdGroup")
        require(row.number_of_classes is not None
                and row.class_orders is not None
                and row.zero_counts is not None
                and row.vanishing_positions is not None
                and row.vanishing_orders is not None
                and row.equals_target is not None,
                f"independent row {index} is incomplete")
        require(len(row.class_orders) == row.number_of_classes,
                f"row {index} class-order length mismatch")
        require(len(row.zero_counts) == row.number_of_classes,
                f"row {index} zero-count length mismatch")
        expected_positions = [
            position for position, count in enumerate(row.zero_counts, start=1)
            if count > 0
        ]
        require(row.vanishing_positions == expected_positions,
                f"row {index} vanishing positions disagree with zero counts")
        derived_orders = sorted({
            row.class_orders[position - 1]
            for position in row.vanishing_positions
        })
        require(row.vanishing_orders == derived_orders,
                f"row {index} invariant does not derive from actual class orders")
        expected_equality = row.vanishing_orders == EXPECTED_TARGET_SET
        require(row.equals_target == expected_equality,
                f"row {index} equality flag is inconsistent")
        if expected_equality:
            equal_indices.append(index)

    require(equal_indices == [118],
            "independent equal-set indices are not [118]")
    require(summary_fields is not None and len(summary_fields) == 9,
            "independent SUMMARY schema is wrong")
    require(summary_fields[0] == "SUMMARY"
            and summary_fields[1] == "CATALOGUE_COUNT"
            and parse_int(summary_fields[2]) == EXPECTED_COUNT
            and summary_fields[3] == "TARGET_INDEX"
            and parse_int(summary_fields[4]) == 118
            and summary_fields[5] == "EQUAL_SET_INDICES"
            and parse_int_list(summary_fields[6]) == [118]
            and summary_fields[7] == "COLLISION_INDICES"
            and parse_int_list(summary_fields[8]) == [],
            "independent SUMMARY values are inconsistent")
    return rows, metadata


def main() -> int:
    require(len(sys.argv) == 3,
            "usage: verify-independent.py CLAIMANT_OUT INDEPENDENT_OUT")
    claimant_path = Path(sys.argv[1])
    independent_path = Path(sys.argv[2])
    submitted_rows, _ = parse_claimant(claimant_path)
    independent_rows, metadata = parse_independent(independent_path)

    require(metadata["CATALOGUE_COUNT"] == str(EXPECTED_COUNT),
            "independent catalogue count is not 162")
    require(sorted(independent_rows) == list(range(1, EXPECTED_COUNT + 1)),
            "independent rows are not exactly 1..162")
    for index in range(1, EXPECTED_COUNT + 1):
        require(independent_rows[index].vanishing_orders ==
                submitted_rows[index].vanishing_orders,
                f"row {index} invariant differs between implementations")

    print(f"CLAIMANT_SHA256\t{sha256(claimant_path)}")
    print(f"INDEPENDENT_SHA256\t{sha256(independent_path)}")
    print("PARSED_CLAIMANT_ROWS\t162")
    print("PARSED_INDEPENDENT_ROWS\t162")
    print("TARGET_ID\t[360,118]")
    print("TARGET_VANISHING_ORDER_SET\t[2,3,4,5]")
    print("EQUAL_SET_INDICES\t[118]")
    print("COLLISION_INDICES\t[]")
    print("ALL_162_INVARIANT_ROWS_AGREE\ttrue")
    print("VERIFIER_COMPLETE\ttrue")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:  # fail closed with the exact reason on stderr
        print(f"VERIFIER_FAILURE: {error}", file=sys.stderr)
        raise
