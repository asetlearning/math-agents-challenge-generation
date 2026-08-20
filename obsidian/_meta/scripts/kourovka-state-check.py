#!/usr/bin/env python3
"""Read-only consistency checks for Kourovka protocol-v2 state."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SELECTION_STATES = {
    "longlisted",
    "shortlisted",
    "approved",
    "active",
    "reserve",
    "retired",
}
SCOPE_STATES = {
    "queued",
    "reconnaissance",
    "running",
    "awaiting_validator",
    "awaiting_mathexpert",
    "awaiting_lead",
    "awaiting_human",
    "extended",
    "parked",
    "closed",
    "stale",
}
DIRECTIONS = {"proof", "counterexample", "both", "none"}
SESSION_STATES = {"not_started", "running", "parked", "stopped", "complete"}
CONSTRAINT_ROLES = {"admissibility", "target_conclusion"}
CLAIM_KINDS = {"proof", "counterexample", "stale_match"}
CONSTRAINT_KINDS = {
    "quantifier",
    "object_class",
    "parameter",
    "exclusion",
    "order",
    "exponent",
    "hypothesis",
    "conclusion",
    "relation",
    "definition",
    "other",
}
BENCHMARK_TYPES = {
    "sealed_private_holdout",
    "secret_seed_generated",
    "adversarial_scope_fidelity",
    "private_proof_repair",
    "future_resolution_shadow",
    "public_regression",
}
FORBIDDEN_BENCHMARK_KEYS = {
    "solution",
    "solution_text",
    "solution_url",
    "shared_chat_url",
    "secret_seed",
    "generator",
    "generator_path",
    "commitment_salt",
    "hidden_rubric",
}
ISO_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?Z$")


class Report:
    def __init__(self, strict_legacy: bool = False) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.strict_legacy = strict_legacy

    def error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def warn(self, location: str, message: str, legacy: bool = False) -> None:
        rendered = f"{location}: {message}"
        if legacy and self.strict_legacy:
            self.errors.append(rendered)
        else:
            self.warnings.append(rendered)


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_string(data: dict[str, Any], key: str, location: str, report: Report) -> str:
    value = data.get(key)
    if not is_nonempty_string(value):
        report.error(location, f"{key} must be a non-empty string")
        return ""
    return value.strip()


def load_json(path: Path, report: Report) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(str(path), f"cannot read valid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        report.error(str(path), "top level must be a JSON object")
        return None
    return value


def validate_scope(path: Path, data: dict[str, Any], report: Report) -> None:
    loc = str(path)
    if data.get("schema_version") != 1:
        report.error(loc, "schema_version must be 1")
    if data.get("protocol_version") != 2:
        report.error(loc, "protocol_version must be 2")

    scope_key = require_string(data, "scope_key", loc, report)
    problem_id = require_string(data, "problem_id", loc, report)
    scope_id = require_string(data, "scope_id", loc, report)
    require_string(data, "target_statement", loc, report)

    if scope_key and path.name != f"{scope_key}.json":
        report.error(loc, f"filename must be {scope_key}.json")
    if scope_id and problem_id and not scope_id.startswith(f"{problem_id}/"):
        report.error(loc, "scope_id must begin with '<problem_id>/'")

    revision = data.get("assignment_revision")
    if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
        report.error(loc, "assignment_revision must be a positive integer")

    source = data.get("source")
    audit_required: bool | None = None
    audit_status: str | None = None
    if not isinstance(source, dict):
        report.error(loc, "source must be an object")
    else:
        page = source.get("pdf_page")
        if not isinstance(page, int) or isinstance(page, bool) or page < 1:
            report.error(loc, "source.pdf_page must be a positive integer")
        statement_checked = source.get("statement_checked")
        if not isinstance(statement_checked, bool):
            report.error(loc, "source.statement_checked must be boolean")
        if statement_checked is True:
            if not is_nonempty_string(source.get("checked_by")):
                report.error(loc, "checked source statement requires source.checked_by")
            checked_utc = source.get("checked_utc")
            if not isinstance(checked_utc, str) or not ISO_UTC.match(checked_utc):
                report.error(loc, "checked source statement requires ISO-8601 source.checked_utc")
        audit = source.get("independent_scope_audit")
        if not isinstance(audit, dict):
            report.error(loc, "source.independent_scope_audit must be an object")
        else:
            audit_required = audit.get("required")
            audit_status = audit.get("status")
            if not isinstance(audit_required, bool):
                report.error(loc, "independent_scope_audit.required must be boolean")
            if audit_status not in {"not_required", "pending", "passed", "failed"}:
                report.error(loc, "independent_scope_audit.status is invalid")
            if audit_status == "passed":
                if not is_nonempty_string(audit.get("auditor")):
                    report.error(loc, "passed independent scope audit requires auditor")
                if not is_nonempty_string(audit.get("note")):
                    report.error(loc, "passed independent scope audit requires note")
            if audit_required is False and audit_status not in {"not_required", "passed"}:
                report.error(loc, "non-required independent scope audit must be not_required or passed")

    clauses = data.get("source_clauses")
    clause_ids: set[str] = set()
    if not isinstance(clauses, list) or not clauses:
        report.error(loc, "source_clauses must be a non-empty list")
    else:
        for index, clause in enumerate(clauses):
            here = f"{loc}:source_clauses[{index}]"
            if not isinstance(clause, dict):
                report.error(here, "must be an object")
                continue
            cid = require_string(clause, "clause_id", here, report)
            require_string(clause, "text", here, report)
            if not isinstance(clause.get("in_scope"), bool):
                report.error(here, "in_scope must be boolean")
            if cid in clause_ids:
                report.error(here, f"duplicate clause_id {cid!r}")
            clause_ids.add(cid)

    constraints = data.get("constraints")
    constraint_ids: set[str] = set()
    roles_seen: set[str] = set()
    if not isinstance(constraints, list) or not constraints:
        report.error(loc, "constraints must be a non-empty list")
    else:
        for index, constraint in enumerate(constraints):
            here = f"{loc}:constraints[{index}]"
            if not isinstance(constraint, dict):
                report.error(here, "must be an object")
                continue
            cid = require_string(constraint, "constraint_id", here, report)
            require_string(constraint, "statement", here, report)
            kind = constraint.get("kind")
            role = constraint.get("role")
            if kind not in CONSTRAINT_KINDS:
                report.error(here, f"kind must be one of {sorted(CONSTRAINT_KINDS)}")
            if role not in CONSTRAINT_ROLES:
                report.error(here, f"role must be one of {sorted(CONSTRAINT_ROLES)}")
            else:
                roles_seen.add(role)
            if constraint.get("required") is not True:
                report.error(here, "required must be true; optional context belongs outside constraints")
            source_clause_id = constraint.get("source_clause_id")
            if source_clause_id not in clause_ids:
                report.error(here, f"unknown source_clause_id {source_clause_id!r}")
            if cid in constraint_ids:
                report.error(here, f"duplicate constraint_id {cid!r}")
            constraint_ids.add(cid)
    for role in CONSTRAINT_ROLES - roles_seen:
        report.error(loc, f"constraints need at least one {role!r} row")

    if not isinstance(data.get("excluded_scopes"), list):
        report.error(loc, "excluded_scopes must be a list")
    success = data.get("success_criteria")
    if not isinstance(success, dict):
        report.error(loc, "success_criteria must be an object")
    else:
        for key in ("proof", "counterexample", "certificate"):
            require_string(success, key, f"{loc}:success_criteria", report)
        if not isinstance(success.get("partial_progress"), list):
            report.error(loc, "success_criteria.partial_progress must be a list")

    selection = data.get("selection_status")
    state = data.get("state")
    direction = data.get("active_direction")
    answered = data.get("scope_answered")
    if selection not in SELECTION_STATES:
        report.error(loc, f"selection_status must be one of {sorted(SELECTION_STATES)}")
    if state not in SCOPE_STATES:
        report.error(loc, f"state must be one of {sorted(SCOPE_STATES)}")
    if direction not in DIRECTIONS:
        report.error(loc, f"active_direction must be one of {sorted(DIRECTIONS)}")
    if not isinstance(answered, bool):
        report.error(loc, "scope_answered must be boolean")
    if state in {"closed", "stale"} and answered is not True:
        report.error(loc, f"state {state!r} requires scope_answered=true")
    if answered is True and state not in {"closed", "stale"}:
        report.error(loc, "scope_answered=true requires state closed or stale")
    if selection == "retired" and state not in {"closed", "stale"}:
        report.error(loc, "selection_status retired requires state closed or stale")
    if state == "running" and direction == "none":
        report.error(loc, "state running requires an active proof or counterexample direction")
    active_states = {"running", "awaiting_validator", "awaiting_mathexpert", "awaiting_lead", "awaiting_human", "extended"}
    if state in active_states:
        if isinstance(source, dict) and source.get("statement_checked") is not True:
            report.error(loc, f"state {state!r} requires source.statement_checked=true")
        if audit_required is True and audit_status != "passed":
            report.error(loc, f"state {state!r} requires the independent scope audit to pass")

    sessions = data.get("direction_sessions")
    running_directions: list[str] = []
    if not isinstance(sessions, dict):
        report.error(loc, "direction_sessions must be an object")
    else:
        for name in ("proof", "counterexample"):
            session = sessions.get(name)
            here = f"{loc}:direction_sessions.{name}"
            if not isinstance(session, dict):
                report.error(here, "must be an object")
                continue
            session_state = session.get("state")
            if session_state not in SESSION_STATES:
                report.error(here, f"state must be one of {sorted(SESSION_STATES)}")
            if session_state == "running":
                running_directions.append(name)
                if not is_nonempty_string(session.get("session_id")):
                    report.error(here, "running session requires session_id")
        if state == "running":
            if direction == "both":
                if running_directions != ["proof", "counterexample"]:
                    report.error(
                        loc,
                        "active_direction='both' requires running proof and counterexample sessions",
                    )
            elif running_directions != [direction]:
                report.error(loc, "running direction session must match active_direction")
        elif len(running_directions) > 1 and direction != "both":
            report.error(loc, "multiple running direction sessions require active_direction='both'")

    if state == "running" and not is_nonempty_string(data.get("current_strategy")):
        report.error(loc, "running scope requires a named current_strategy")
    for key in ("strategy_history", "open_questions", "revision_history"):
        if not isinstance(data.get(key), list):
            report.error(loc, f"{key} must be a list")
    history = data.get("revision_history")
    if isinstance(history, list) and history and isinstance(revision, int):
        last = history[-1]
        if not isinstance(last, dict) or last.get("revision") != revision:
            report.error(loc, "last revision_history entry must match assignment_revision")

    updated = data.get("updated_utc")
    if updated is not None and (not isinstance(updated, str) or not ISO_UTC.match(updated)):
        report.error(loc, "updated_utc must be null or an ISO-8601 UTC timestamp ending Z")


def parse_frontmatter(path: Path) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return {}
    if not lines or lines[0].strip() != "---":
        return {}
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip("\"'")
    return values


def validate_rosters(root: Path, scopes: dict[str, dict[str, Any]], report: Report) -> int:
    roster_paths = sorted((root / "Agents/Kourovka/roster").glob("Problem-*.md"))
    for path in roster_paths:
        fm = parse_frontmatter(path)
        if not fm:
            report.warn(str(path), "no simple YAML frontmatter found", legacy=True)
            continue
        scope_id = fm.get("scope_id")
        if not scope_id or scope_id == "none":
            report.warn(str(path), "legacy roster has no scope_id; migrate on next activation", legacy=True)
            continue
        scope = scopes.get(scope_id)
        if scope is None:
            report.warn(str(path), f"scope_id {scope_id!r} has no canonical record", legacy=True)
            continue
        revision_text = fm.get("assignment_revision", "")
        try:
            roster_revision = int(revision_text)
        except ValueError:
            report.error(str(path), "assignment_revision must be an integer")
        else:
            if roster_revision != scope.get("assignment_revision"):
                report.error(str(path), "assignment_revision disagrees with canonical scope")
        direction = fm.get("direction")
        canonical_direction = scope.get("active_direction")
        if fm.get("state") == "running" and direction:
            matches_single = direction == canonical_direction
            matches_pair = canonical_direction == "both" and direction in {"proof", "counterexample"}
            if not (matches_single or matches_pair):
                report.error(str(path), "running direction disagrees with canonical scope")
    return len(roster_paths)


def validate_inbox(root: Path, scopes: dict[str, dict[str, Any]], report: Report) -> None:
    for path in sorted((root / "Agents/Kourovka/bus/inbox").glob("*/*.md")):
        fm = parse_frontmatter(path)
        scope_id = fm.get("scope_id")
        if not scope_id or scope_id == "none":
            continue
        scope = scopes.get(scope_id)
        if scope is None:
            report.warn(str(path), f"message names unknown scope_id {scope_id!r}", legacy=True)
            continue
        revision_text = fm.get("assignment_revision", "")
        try:
            message_revision = int(revision_text)
        except ValueError:
            report.warn(str(path), "scoped message lacks an integer assignment_revision", legacy=True)
            continue
        if message_revision > scope.get("assignment_revision", 0):
            report.error(str(path), "message revision is newer than canonical scope record")


def markdown_cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    content = stripped[1:-1]
    cells: list[str] = []
    current: list[str] = []
    wikilink_depth = 0
    index = 0
    while index < len(content):
        pair = content[index : index + 2]
        if pair == "[[":
            wikilink_depth += 1
            current.extend(pair)
            index += 2
            continue
        if pair == "]]" and wikilink_depth:
            wikilink_depth -= 1
            current.extend(pair)
            index += 2
            continue
        char = content[index]
        if char == "|" and wikilink_depth == 0 and (index == 0 or content[index - 1] != "\\"):
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        index += 1
    cells.append("".join(current).strip())
    return cells


def plain_cell(value: str) -> str:
    value = value.strip().strip("`")
    match = re.fullmatch(r"\[\[[^\]|]+\|([^\]]+)\]\]", value)
    return match.group(1).strip() if match else value


def validate_board(root: Path, scopes: dict[str, dict[str, Any]], report: Report) -> int:
    path = root / "Agents/Kourovka/board/_board.md"
    if not path.is_file():
        report.warn(str(path), "board is missing", legacy=True)
        return 0
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        report.error(str(path), f"cannot read board: {exc}")
        return 0
    header_index = -1
    header: list[str] = []
    legacy_table_found = False
    required = {"Scope", "Rev", "Direction", "State"}
    for index, line in enumerate(lines):
        cells = markdown_cells(line)
        if "Problem" in cells and "State" in cells:
            if required.issubset(cells):
                header_index = index
                header = cells
                break
            legacy_table_found = True
    if header_index < 0:
        message = (
            "legacy board table lacks Scope/Rev/Direction columns; migrate before next activation"
            if legacy_table_found
            else "no scheduling table found"
        )
        report.warn(str(path), message, legacy=True)
        return 0
    columns = {name: header.index(name) for name in required}
    rows_checked = 0
    represented: set[str] = set()
    for line in lines[header_index + 2 :]:
        cells = markdown_cells(line)
        if not cells:
            break
        if len(cells) < len(header):
            report.error(str(path), f"short scheduling row: {line}")
            continue
        scope_id = plain_cell(cells[columns["Scope"]])
        if scope_id in {"", "-", "—", "none"}:
            report.error(str(path), "protocol-v2 scheduling row has no atomic Scope")
            continue
        rows_checked += 1
        represented.add(scope_id)
        scope = scopes.get(scope_id)
        if scope is None:
            report.error(str(path), f"board row names unknown scope_id {scope_id!r}")
            continue
        revision_text = plain_cell(cells[columns["Rev"]])
        try:
            revision = int(revision_text)
        except ValueError:
            report.error(str(path), f"scope {scope_id}: Rev must be an integer")
        else:
            if revision != scope.get("assignment_revision"):
                report.error(str(path), f"scope {scope_id}: Rev disagrees with canonical scope")
        board_state = plain_cell(cells[columns["State"]]).replace("-", "_")
        if board_state != scope.get("state"):
            report.error(str(path), f"scope {scope_id}: State disagrees with canonical scope")
        board_direction = plain_cell(cells[columns["Direction"]])
        if board_direction != scope.get("active_direction"):
            report.error(str(path), f"scope {scope_id}: Direction disagrees with canonical scope")
    for scope_id, scope in scopes.items():
        if scope.get("selection_status") in {"approved", "active"} and scope_id not in represented:
            report.error(str(path), f"approved/active scope {scope_id!r} is absent from the board")
    return rows_checked


def find_forbidden_keys(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if str(key).lower() in FORBIDDEN_BENCHMARK_KEYS:
                found.append(path)
            found.extend(find_forbidden_keys(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(find_forbidden_keys(child, f"{prefix}[{index}]"))
    return found


def validate_benchmarks(root: Path, report: Report) -> int:
    paths = sorted((root / "Agents/Kourovka/benchmarks").glob("*.json"))
    for path in paths:
        data = load_json(path, report)
        if data is None:
            continue
        loc = str(path)
        if data.get("schema_version") != 1:
            report.error(loc, "benchmark schema_version must be 1")
        if data.get("protocol_version") != 2:
            report.error(loc, "benchmark protocol_version must be 2")
        require_string(data, "benchmark_id", loc, report)
        benchmark_type = data.get("benchmark_type")
        if benchmark_type not in BENCHMARK_TYPES:
            report.error(loc, f"benchmark_type must be one of {sorted(BENCHMARK_TYPES)}")
        if data.get("exposure_risk") not in {"low", "medium", "high", "tainted"}:
            report.error(loc, "exposure_risk must be low, medium, high, or tainted")
        forbidden = find_forbidden_keys(data)
        if forbidden:
            report.error(loc, f"private benchmark material keys are forbidden: {', '.join(forbidden)}")
        resources = data.get("allowed_resources")
        if not isinstance(resources, dict) or not isinstance(resources.get("open_web"), bool):
            report.error(loc, "allowed_resources.open_web must be boolean")
        elif resources.get("open_web") and data.get("exposure_risk") == "low":
            report.warn(loc, "open_web=true is inconsistent with a low-exposure discovery claim")
        if benchmark_type in {"sealed_private_holdout", "private_proof_repair", "secret_seed_generated"}:
            if data.get("solution_location") != "sealed_external_never_in_vault":
                report.error(loc, "private benchmark solution_location must remain sealed external")
        if data.get("reveal_status") not in {"sealed", "frozen_pending_reveal", "revealed_retired"}:
            report.error(loc, "reveal_status must be sealed, frozen_pending_reveal, or revealed_retired")
        frozen = data.get("frozen_configuration")
        if not isinstance(frozen, dict):
            report.error(loc, "frozen_configuration must be an object")
        else:
            require_string(frozen, "model", f"{loc}:frozen_configuration", report)
            require_string(frozen, "reasoning_effort", f"{loc}:frozen_configuration", report)
            budget = frozen.get("active_budget_minutes")
            if not isinstance(budget, int) or isinstance(budget, bool) or budget < 1:
                report.error(loc, "frozen_configuration.active_budget_minutes must be positive")
    return len(paths)


def validate_claim_checks(
    root: Path, scopes: dict[str, dict[str, Any]], report: Report
) -> int:
    problems_root = root / "Agents/Kourovka/problems"
    paths = sorted(problems_root.glob("**/claim-checks/*.json"))
    for path in paths:
        data = load_json(path, report)
        if data is None:
            continue
        loc = str(path)
        if data.get("schema_version") != 1:
            report.error(loc, "claim-check schema_version must be 1")
        if data.get("protocol_version") != 2:
            report.error(loc, "claim-check protocol_version must be 2")
        require_string(data, "claim_id", loc, report)
        problem_id = require_string(data, "problem_id", loc, report)
        scope_id = require_string(data, "scope_id", loc, report)
        require_string(data, "candidate_object", loc, report)
        try:
            problem_directory = path.relative_to(problems_root).parts[0]
        except (ValueError, IndexError):
            problem_directory = ""
        if problem_directory != problem_id:
            report.error(loc, "problem_id must match the parent problem directory")
        claim_kind = data.get("claim_kind")
        if claim_kind not in CLAIM_KINDS:
            report.error(loc, f"claim_kind must be one of {sorted(CLAIM_KINDS)}")
        ready = data.get("ready_for_validator")
        if not isinstance(ready, bool):
            report.error(loc, "ready_for_validator must be boolean")

        scope = scopes.get(scope_id)
        if scope is None:
            report.error(loc, f"scope_id {scope_id!r} has no canonical record")
            continue
        if scope.get("problem_id") != problem_id:
            report.error(loc, "problem_id disagrees with canonical scope")
        revision = data.get("assignment_revision")
        if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
            report.error(loc, "assignment_revision must be a positive integer")
        elif revision != scope.get("assignment_revision"):
            if ready is True:
                report.error(loc, "an old-revision claim cannot be ready for the current Validator")
            else:
                report.warn(loc, "claim check is for an old assignment revision")

        canonical_constraints = {
            item.get("constraint_id"): item
            for item in scope.get("constraints", [])
            if isinstance(item, dict) and is_nonempty_string(item.get("constraint_id"))
        }
        rows = data.get("rows")
        seen: set[str] = set()
        structurally_complete = isinstance(rows, list)
        qualifying = structurally_complete
        if not isinstance(rows, list):
            report.error(loc, "rows must be a list")
            rows = []
        for index, row in enumerate(rows):
            here = f"{loc}:rows[{index}]"
            if not isinstance(row, dict):
                report.error(here, "must be an object")
                structurally_complete = False
                qualifying = False
                continue
            constraint_id = require_string(row, "constraint_id", here, report)
            if constraint_id in seen:
                report.error(here, f"duplicate constraint_id {constraint_id!r}")
                structurally_complete = False
                qualifying = False
            seen.add(constraint_id)
            canonical = canonical_constraints.get(constraint_id)
            if canonical is None:
                report.error(here, f"constraint_id {constraint_id!r} is not in the canonical scope")
                structurally_complete = False
                qualifying = False
                continue
            role = row.get("role")
            if role != canonical.get("role"):
                report.error(here, "role disagrees with canonical scope")
                structurally_complete = False
                qualifying = False
            result = row.get("result")
            if role == "admissibility":
                if result not in {"pass", "fail", "unknown"}:
                    report.error(here, "admissibility result must be pass, fail, or unknown")
                    qualifying = False
                expected = "pass"
            else:
                allowed = {
                    "proved",
                    "violated",
                    "answered",
                    "not_proved",
                    "not_violated",
                    "not_answered",
                    "unknown",
                }
                if result not in allowed:
                    report.error(here, f"target_conclusion result must be one of {sorted(allowed)}")
                    qualifying = False
                expected = {
                    "proof": "proved",
                    "counterexample": "violated",
                    "stale_match": "answered",
                }.get(claim_kind)
            if result != expected:
                qualifying = False
            if result == expected and not is_nonempty_string(row.get("evidence_ref")):
                report.error(here, f"result {expected!r} requires a non-empty evidence_ref")
                qualifying = False

        missing = set(canonical_constraints) - seen
        extra = seen - set(canonical_constraints)
        if missing:
            report.error(loc, f"missing canonical constraint rows: {sorted(missing)}")
            structurally_complete = False
            qualifying = False
        if extra:
            structurally_complete = False
            qualifying = False
        if ready is True and not (structurally_complete and qualifying):
            report.error(loc, "ready_for_validator=true but the constraint gate does not pass")
        scope_source = scope.get("source")
        if ready is True and (
            not isinstance(scope_source, dict) or scope_source.get("statement_checked") is not True
        ):
            report.error(loc, "ready_for_validator=true requires a visually checked source statement")
        created = data.get("created_utc")
        if created is not None and (not isinstance(created, str) or not ISO_UTC.match(created)):
            report.error(loc, "created_utc must be null or an ISO-8601 UTC timestamp ending Z")
    return len(paths)


def render(scopes: list[dict[str, Any]]) -> None:
    print("| Problem | Scope | Rev | Selection | State | Direction | Strategy | Answered |")
    print("|---|---|---:|---|---|---|---|---|")
    for scope in sorted(scopes, key=lambda item: (str(item.get("problem_id")), str(item.get("scope_id")))):
        fields = [
            scope.get("problem_id", "?"),
            scope.get("scope_id", "?"),
            scope.get("assignment_revision", "?"),
            scope.get("selection_status", "?"),
            scope.get("state", "?"),
            scope.get("active_direction", "?"),
            scope.get("current_strategy") or "—",
            "yes" if scope.get("scope_answered") else "no",
        ]
        print("| " + " | ".join(str(value).replace("|", "\\|") for value in fields) + " |")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="vault root (default: cwd)")
    parser.add_argument("--render", action="store_true", help="render canonical scopes as Markdown")
    parser.add_argument(
        "--strict-legacy",
        action="store_true",
        help="treat legacy roster/message migration warnings as errors",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report(strict_legacy=args.strict_legacy)
    scope_dir = root / "Agents/Kourovka/scopes"
    scope_paths = sorted(scope_dir.glob("*.json")) if scope_dir.is_dir() else []
    scopes: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}

    if not scope_paths:
        report.warn(str(scope_dir), "no canonical scope records yet; legacy state remains to migrate")
    for path in scope_paths:
        data = load_json(path, report)
        if data is None:
            continue
        validate_scope(path, data, report)
        scope_id = data.get("scope_id")
        if is_nonempty_string(scope_id):
            if scope_id in by_id:
                report.error(str(path), f"duplicate scope_id also used by {by_id[scope_id].get('scope_key')}")
            by_id[scope_id] = data
        scopes.append(data)

    roster_count = validate_rosters(root, by_id, report)
    validate_inbox(root, by_id, report)
    board_row_count = validate_board(root, by_id, report)
    claim_check_count = validate_claim_checks(root, by_id, report)
    benchmark_count = validate_benchmarks(root, report)

    for warning in report.warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in report.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if args.render:
        render(scopes)
    print(
        f"Kourovka state check: {len(scopes)} scope(s), {roster_count} roster(s), "
        f"{board_row_count} v2 board row(s), "
        f"{claim_check_count} claim check(s), "
        f"{benchmark_count} benchmark manifest(s), "
        f"{len(report.errors)} error(s), {len(report.warnings)} warning(s).",
        file=sys.stderr,
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
