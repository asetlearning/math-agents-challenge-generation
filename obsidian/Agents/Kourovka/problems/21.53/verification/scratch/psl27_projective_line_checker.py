#!/usr/bin/env python3
"""Independent bounded checker for the PSL(2,7) fixed-pair certificate.

The claimant computes with canonical 2-by-2 matrices modulo sign.  This checker
uses permutations of the eight points of P^1(F_7) as its group elements, tests
simplicity by normal closures, and only then maps the submitted matrix labels into
the independently constructed permutation group for entrywise comparison.

It never executes or imports the claimant's program and performs no automorphism-
group search.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, deque
from itertools import product
from pathlib import Path


P = 7
INF = 7
OMEGA = tuple(range(8))
IDENTITY = OMEGA
HERE = Path(__file__).resolve().parent
CLAIM_SCRATCH = (
    HERE.parent.parent
    / "runs"
    / "2026-08-17-r7-psl27-direct-comparison"
    / "scratch"
)
CLAIM_NOTE = (
    HERE.parent.parent
    / "runs"
    / "2026-08-17-r7-psl27-direct-comparison"
    / "partial-result.md"
)
CERT_PATH = CLAIM_SCRATCH / "psl27_exact_scheme_certificate.json"
CSV_PATH = CLAIM_SCRATCH / "psl27_product_order_matrix.csv"
CLAIM_SCRIPT_PATH = CLAIM_SCRATCH / "psl27_exact_scheme.py"

EXPECTED_FILE_SHA256 = {
    CLAIM_SCRIPT_PATH: "54545eba3defdba8faade61d957d55dd7671d4eab540363bb7d6a3723a0a9d8a",
    CERT_PATH: "9dc3be4f7b84564e1ecd1cddc33c0f101210ec142225f3fdbfd48d50ff8536f7",
    CSV_PATH: "c184a782544ea0b3dceefc3cd495c5679044a4dc3693aabf6caf1b3f56e53ff2",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Composition left after right."""
    return tuple(left[right[x]] for x in OMEGA)


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(OMEGA)
    for x, image in enumerate(permutation):
        answer[image] = x
    return tuple(answer)


def permutation_order(permutation: tuple[int, ...]) -> int:
    power = IDENTITY
    for exponent in range(1, 169):
        power = compose(power, permutation)
        if power == IDENTITY:
            return exponent
    raise AssertionError("permutation order exceeded the group-order bound")


def subgroup_generated(
    generators: list[tuple[int, ...]] | set[tuple[int, ...]],
) -> set[tuple[int, ...]]:
    steps = set(generators)
    steps.update(inverse(g) for g in tuple(steps))
    seen = {IDENTITY}
    queue: deque[tuple[int, ...]] = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for step in steps:
            candidate = compose(current, step)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return seen


def fractional_permutation(
    matrix: tuple[int, int, int, int],
) -> tuple[int, ...]:
    a, b, c, d = matrix
    require((a * d - b * c) % P == 1, f"determinant is not 1: {matrix}")
    images: list[int] = []
    for x in OMEGA:
        if x == INF:
            if c % P == 0:
                image = INF
            else:
                image = (a * pow(c, -1, P)) % P
        else:
            numerator = (a * x + b) % P
            denominator = (c * x + d) % P
            if denominator == 0:
                image = INF
            else:
                image = (numerator * pow(denominator, -1, P)) % P
        images.append(image)
    result = tuple(images)
    require(set(result) == set(OMEGA), f"not a permutation: {matrix}")
    return result


def canonical_matrix(
    matrix: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    negative = tuple((-entry) % P for entry in matrix)
    return min(matrix, negative)  # type: ignore[return-value]


def conjugacy_classes(
    group: set[tuple[int, ...]],
) -> list[set[tuple[int, ...]]]:
    unseen = set(group)
    classes: list[set[tuple[int, ...]]] = []
    while unseen:
        representative = min(unseen)
        orbit = {
            compose(compose(inverse(g), representative), g)
            for g in group
        }
        require(orbit <= unseen, "conjugacy classes failed to partition")
        classes.append(orbit)
        unseen -= orbit
    return classes


def canonical_json_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_from_markdown(path: Path) -> list[list[int]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = lines.index("## Complete product-order matrix")
    fence_start = next(
        i for i in range(heading + 1, len(lines)) if lines[i].strip() == "```text"
    )
    fence_end = next(
        i for i in range(fence_start + 1, len(lines)) if lines[i].strip() == "```"
    )
    rows: list[list[int]] = []
    for line in lines[fence_start + 1 : fence_end]:
        fields = line.split()
        if len(fields) == 22 and fields[0].isdigit():
            row_number = int(fields[0])
            require(row_number == len(rows) + 1, "markdown row labels are not consecutive")
            rows.append([int(value) for value in fields[1:]])
    require(len(rows) == 21, "markdown does not contain exactly 21 matrix rows")
    return rows


def distinct_prime_factors(number: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    remainder = number
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            factors.append(divisor)
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors.append(remainder)
    return factors


# Independent projective-line group.  These are x -> x+1 and x -> -1/x.
translation = tuple((x + 1) % P if x != INF else INF for x in OMEGA)
inversion = tuple(
    INF if x == 0 else 0 if x == INF else (-pow(x, -1, P)) % P
    for x in OMEGA
)
group = subgroup_generated([translation, inversion])
require(len(group) == 168, "projective generator closure does not have order 168")
require(
    compose(translation, inversion) != compose(inversion, translation),
    "projective generators unexpectedly commute",
)

# Cross-check that the generator closure is the full determinant-one projective
# image, while retaining permutations—not matrix cosets—as the group model.
sl2_matrices = [
    matrix
    for matrix in product(range(P), repeat=4)
    if (matrix[0] * matrix[3] - matrix[1] * matrix[2]) % P == 1
]
canonical_projective_matrices = sorted({canonical_matrix(m) for m in sl2_matrices})
full_projective_image = {fractional_permutation(m) for m in sl2_matrices}
require(len(sl2_matrices) == 336, "SL(2,7) matrix count is not 336")
require(len(canonical_projective_matrices) == 168, "quotient-by-sign count is not 168")
require(full_projective_image == group, "generator closure is not the full projective image")

orders = {g: permutation_order(g) for g in group}
order_counts = Counter(orders.values())
require(
    dict(sorted(order_counts.items())) == {1: 1, 2: 21, 3: 56, 4: 42, 7: 48},
    "independent element-order distribution differs",
)

classes = conjugacy_classes(group)
classes.sort(key=lambda orbit: (orders[next(iter(orbit))], len(orbit), min(orbit)))
class_summary = [(orders[next(iter(orbit))], len(orbit)) for orbit in classes]
require(
    class_summary == [(1, 1), (2, 21), (3, 56), (4, 42), (7, 24), (7, 24)],
    "independent conjugacy-class summary differs",
)

# A finite group is simple iff every nonidentity element has full normal closure.
# It suffices to test one representative of every nonidentity conjugacy class.
normal_closure_sizes: list[tuple[int, int, int]] = []
for orbit in classes:
    representative = min(orbit)
    if representative == IDENTITY:
        continue
    conjugates = {
        compose(compose(inverse(g), representative), g)
        for g in group
    }
    normal_closure = subgroup_generated(conjugates)
    normal_closure_sizes.append(
        (orders[representative], len(orbit), len(normal_closure))
    )
require(
    all(size == 168 for _, _, size in normal_closure_sizes),
    "a nonidentity class representative has a proper normal closure",
)

involutions = {g for g in group if orders[g] == 2}
involution_classes = [orbit for orbit in classes if orders[next(iter(orbit))] == 2]
require(len(involutions) == 21, "independent involution count differs")
require(len(involution_classes) == 1, "independent involution-class count differs")
require(involution_classes[0] == involutions, "the order-2 class is not all involutions")

# Freeze and validate the claimant's three explicitly linked artifacts without
# executing the claimant's script.
for artifact, expected_digest in EXPECTED_FILE_SHA256.items():
    require(file_sha256(artifact) == expected_digest, f"file digest changed: {artifact.name}")

certificate = json.loads(CERT_PATH.read_text(encoding="utf-8"))
require(certificate["projective_group_order"] == len(group), "certificate group order differs")
require(certificate["sl2_matrix_count"] == len(sl2_matrices), "certificate SL2 count differs")
require(certificate["prime_factorization"] == {"2": 3, "3": 1, "7": 1}, "bad factorization")
prime_factors = distinct_prime_factors(len(group))
require(prime_factors == [2, 3, 7], "independent prime factors differ")
require(certificate["second_smallest_distinct_prime"] == prime_factors[1] == 3, "bad p")
require(
    certificate["element_order_counts"]
    == {str(order): count for order, count in sorted(order_counts.items())},
    "certificate order counts differ",
)
require(
    [(row["order"], row["size"]) for row in certificate["conjugacy_classes"]]
    == class_summary,
    "certificate conjugacy classes differ",
)
require(certificate["normal_subgroup_sizes"] == [1, 168], "certificate normal sizes differ")
require(certificate["involution_count"] == 21, "certificate involution count differs")
require(certificate["involution_class_count"] == 1, "certificate involution class count differs")

# Check the displayed noncommuting matrix witness in the permutation action.
nonabelian = certificate["nonabelian_witness"]
witness_a = fractional_permutation(tuple(nonabelian["a"]))
witness_b = fractional_permutation(tuple(nonabelian["b"]))
require(compose(witness_a, witness_b) != compose(witness_b, witness_a), "witness commutes")
require(
    fractional_permutation(tuple(nonabelian["ab"])) == compose(witness_a, witness_b),
    "displayed AB is incorrect",
)
require(
    fractional_permutation(tuple(nonabelian["ba"])) == compose(witness_b, witness_a),
    "displayed BA is incorrect",
)

vertex_records = certificate["involution_vertices"]
require([record["vertex"] for record in vertex_records] == list(range(1, 22)), "bad labels")
labelled_involutions = [
    fractional_permutation(tuple(record["matrix_mod_7_up_to_sign"]))
    for record in vertex_records
]
require(len(set(labelled_involutions)) == 21, "submitted vertex labels are not distinct")
require(set(labelled_involutions) == involutions, "submitted labels are not the involution class")

independent_matrix = [
    [permutation_order(compose(left, right)) for right in labelled_involutions]
    for left in labelled_involutions
]
require(certificate["product_order_matrix"] == independent_matrix, "certificate matrix differs")
require(matrix_from_markdown(CLAIM_NOTE) == independent_matrix, "displayed matrix differs")

with CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
    csv_rows = list(csv.reader(handle))
require(csv_rows[0] == ["vertex"] + [str(i) for i in range(1, 22)], "CSV header differs")
csv_matrix = []
for expected_label, row in enumerate(csv_rows[1:], start=1):
    require(int(row[0]) == expected_label, "CSV row label differs")
    csv_matrix.append([int(value) for value in row[1:]])
require(csv_matrix == independent_matrix, "CSV matrix differs")

independent_edges = [
    {"i": i + 1, "j": j + 1, "order": independent_matrix[i][j]}
    for i in range(21)
    for j in range(i + 1, 21)
]
require(certificate["unordered_edges"] == independent_edges, "certificate edge list differs")
edge_counts = Counter(edge["order"] for edge in independent_edges)
require(dict(sorted(edge_counts.items())) == {2: 42, 3: 84, 4: 84}, "edge counts differ")
require(set(edge_counts) == {2, 3, 4}, "occurring colour set differs")
valencies = {
    colour: [
        sum(independent_matrix[i][j] == colour for j in range(21) if j != i)
        for i in range(21)
    ]
    for colour in sorted(edge_counts)
}
require({colour: sorted(set(values)) for colour, values in valencies.items()} == {2: [4], 3: [8], 4: [8]}, "valencies differ")
require(certificate["occurring_edge_colours"] == [2, 3, 4], "certificate colours differ")
require(certificate["edge_colour_counts"] == {"2": 42, "3": 84, "4": 84}, "certificate edge counts differ")
require(
    certificate["colour_valencies_by_vertex"]
    == {str(colour): values for colour, values in valencies.items()},
    "certificate valencies differ",
)

# Check every internal digest, including the claimant's canonical matrix-coset list.
expected_internal_digests = {
    "projective_elements_sha256": canonical_json_digest(
        [list(matrix) for matrix in canonical_projective_matrices]
    ),
    "involution_vertices_sha256": canonical_json_digest(vertex_records),
    "product_order_matrix_sha256": canonical_json_digest(independent_matrix),
    "unordered_edges_sha256": canonical_json_digest(independent_edges),
}
require(certificate["digests"] == expected_internal_digests, "internal digests differ")

all_edges = {(i, j) for i in range(21) for j in range(i + 1, 21)}
edge_sets = {
    colour: {
        (i, j)
        for i in range(21)
        for j in range(i + 1, 21)
        if independent_matrix[i][j] == colour
    }
    for colour in (2, 3, 4)
}
require(edge_sets[4] == all_edges - edge_sets[2] - edge_sets[3], "colour 4 not complement")

print("CHECKER_MODEL=faithful permutation action on P^1(F_7)")
print(f"GROUP_ORDER={len(group)}")
print("NONABELIAN_GENERATORS=YES")
print(f"ELEMENT_ORDER_COUNTS={dict(sorted(order_counts.items()))}")
print(f"CONJUGACY_CLASS_ORDER_SIZE={class_summary}")
print(f"NORMAL_CLOSURE_SIZES={normal_closure_sizes}")
print(f"INVOLUTION_COUNT={len(involutions)}")
print(f"INVOLUTION_CLASS_COUNT={len(involution_classes)}")
print(f"PRIME_FACTORS={prime_factors}")
print(f"SECOND_SMALLEST_DISTINCT_PRIME={prime_factors[1]}")
print(f"EDGE_COLOURS={sorted(edge_counts)}")
print(f"EDGE_COLOUR_COUNTS={dict(sorted(edge_counts.items()))}")
print(f"COLOUR_VALENCIES={{2: 4, 3: 8, 4: 8}}")
print("CLAIMANT_FILE_DIGESTS=PASS")
print("CERTIFICATE_INTERNAL_DIGESTS=PASS")
print("VERTEX_LABELS_AND_ALL_210_PRODUCTS=PASS")
print("CERTIFICATE_MATRIX_CSV_MARKDOWN=ENTRYWISE_EQUAL")
print("E4_IS_COMPLEMENT_OF_E2_UNION_E3=YES")
print("BOUNDED_FIXED_PAIR_ONLY=YES")
print("ALL_CHECKS_PASS")
