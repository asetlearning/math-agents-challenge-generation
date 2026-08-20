#!/usr/bin/env python3
"""Fail-closed structural checker for the frozen GAP screen output.

This checks catalogue-row completeness and internal collision bookkeeping.  It
does not independently recompute character tables or vanishing-order sets.
"""

from __future__ import annotations

import ast
import pathlib
import sys


def parse_bool(text: str) -> bool:
    if text == "true":
        return True
    if text == "false":
        return False
    raise ValueError(f"invalid boolean: {text!r}")


def parse_int_list(text: str) -> list[int]:
    value = ast.literal_eval(text)
    if not isinstance(value, list) or not all(
        isinstance(item, int) and item > 0 for item in value
    ):
        raise ValueError(f"not a positive-integer list: {text!r}")
    if value != sorted(set(value)):
        raise ValueError(f"list is not strictly sorted and duplicate-free: {text!r}")
    return value


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_a6_order360_output.py OUTPUT")

    path = pathlib.Path(sys.argv[1])
    lines = path.read_text(encoding="utf-8").splitlines()
    meta: dict[str, str] = {}
    summary: dict[str, str] = {}
    rows: list[dict[str, object]] = []

    for line_number, line in enumerate(lines, 1):
        fields = line.split("\t")
        if fields[0] == "META" and len(fields) == 3:
            if fields[1] in meta:
                raise ValueError(f"duplicate META key at line {line_number}")
            meta[fields[1]] = fields[2]
        elif fields[0] == "SUMMARY" and len(fields) == 3:
            if fields[1] in summary:
                raise ValueError(f"duplicate SUMMARY key at line {line_number}")
            summary[fields[1]] = fields[2]
        elif fields[0] == "ROW_HEADER":
            expected = [
                "ROW_HEADER",
                "index",
                "size",
                "is_target_id",
                "vanishing_order_set",
                "equals_target_set",
                "collision",
            ]
            if fields != expected:
                raise ValueError(f"unexpected row header at line {line_number}")
        elif fields[0] == "ROW" and len(fields) == 7:
            row = {
                "index": int(fields[1]),
                "size": int(fields[2]),
                "is_target": parse_bool(fields[3]),
                "vset": parse_int_list(fields[4]),
                "equals_target": parse_bool(fields[5]),
                "collision": parse_bool(fields[6]),
            }
            rows.append(row)
        elif line:
            raise ValueError(f"unrecognized nonempty output line {line_number}: {line!r}")

    required_meta = {
        "gap_version",
        "order",
        "coverage",
        "number_small_groups",
        "target_constructor",
        "target_size",
        "target_is_simple",
        "target_id",
        "target_vanishing_order_set",
    }
    required_summary = {
        "row_count",
        "target_rows",
        "equal_set_rows",
        "collision_rows",
        "collision_count",
        "complete",
        "runtime_ms",
    }
    if set(meta) != required_meta:
        raise ValueError(f"META keys differ: {sorted(set(meta) ^ required_meta)}")
    if set(summary) != required_summary:
        raise ValueError(
            f"SUMMARY keys differ: {sorted(set(summary) ^ required_summary)}"
        )

    if meta["order"] != "360" or meta["target_size"] != "360":
        raise ValueError("order or target-size check failed")
    if meta["coverage"] != "1..NumberSmallGroups(360)":
        raise ValueError("coverage declaration changed")
    if meta["target_constructor"] != "AlternatingGroup(6)":
        raise ValueError("target constructor changed")
    if not parse_bool(meta["target_is_simple"]):
        raise ValueError("target did not pass GAP's IsSimpleGroup")

    count = int(meta["number_small_groups"])
    if count < 1:
        raise ValueError("nonpositive catalogue count")
    if [row["index"] for row in rows] != list(range(1, count + 1)):
        raise ValueError("rows do not cover every catalogue index exactly once in order")
    if any(row["size"] != 360 for row in rows):
        raise ValueError("a row has size other than 360")

    target_id = parse_int_list(meta["target_id"])
    if len(target_id) != 2 or target_id[0] != 360 or not 1 <= target_id[1] <= count:
        raise ValueError("invalid target IdGroup")
    target_set = parse_int_list(meta["target_vanishing_order_set"])

    target_rows = [int(row["index"]) for row in rows if row["is_target"]]
    equal_rows = [int(row["index"]) for row in rows if row["equals_target"]]
    collision_rows = [int(row["index"]) for row in rows if row["collision"]]
    if target_rows != [target_id[1]]:
        raise ValueError("target row does not match target IdGroup")
    if rows[target_id[1] - 1]["vset"] != target_set:
        raise ValueError("target catalogue row does not reproduce target set")
    for row in rows:
        expected_equal = row["vset"] == target_set
        expected_collision = expected_equal and not row["is_target"]
        if row["equals_target"] != expected_equal:
            raise ValueError(f"bad equals-target flag at row {row['index']}")
        if row["collision"] != expected_collision:
            raise ValueError(f"bad collision flag at row {row['index']}")

    if int(summary["row_count"]) != count:
        raise ValueError("summary row count mismatch")
    if parse_int_list(summary["target_rows"]) != target_rows:
        raise ValueError("summary target rows mismatch")
    if parse_int_list(summary["equal_set_rows"]) != equal_rows:
        raise ValueError("summary equal-set rows mismatch")
    if parse_int_list(summary["collision_rows"]) != collision_rows:
        raise ValueError("summary collision rows mismatch")
    if int(summary["collision_count"]) != len(collision_rows):
        raise ValueError("summary collision count mismatch")
    if not parse_bool(summary["complete"]):
        raise ValueError("screen did not declare complete")
    if int(summary["runtime_ms"]) < 0:
        raise ValueError("negative runtime")

    print(f"VERIFIED_COMPLETE_ROWS={count}")
    print(f"TARGET_ID={target_id}")
    print(f"TARGET_VANISHING_ORDER_SET={target_set}")
    print(f"EQUAL_SET_ROWS={equal_rows}")
    print(f"COLLISION_ROWS={collision_rows}")
    print(f"COLLISION_COUNT={len(collision_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
