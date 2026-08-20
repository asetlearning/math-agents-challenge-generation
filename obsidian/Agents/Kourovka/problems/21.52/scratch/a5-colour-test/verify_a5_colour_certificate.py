#!/usr/bin/env python3
"""Independent exact verifier for the Kourovka 21.52 A5 certificate.

The verifier reconstructs the permutation model and colour matrix, reruns a
separately written complete colour-automorphism backtrack, and enumerates all A5
automorphisms by evaluating canonical words for every possible generator-image
pair and then testing the full multiplication table.
"""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import itertools
import json
from pathlib import Path


Perm = tuple[int, ...]
N = 5
ONE: Perm = tuple(range(N))


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def sign(p: Perm) -> int:
    crossings = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            crossings += int(p[i] > p[j])
    return crossings % 2


def order(p: Perm) -> int:
    x = ONE
    for k in range(1, 61):
        x = mul(x, p)
        if x == ONE:
            return k
    raise RuntimeError("order bound failed")


def zero_based(images: list[int]) -> Perm:
    return tuple(x - 1 for x in images)


def digest(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def independent_colour_automorphisms(matrix: list[list[int]]) -> set[Perm]:
    """Complete DFS using a fixed reverse source order and forward checking."""
    size = len(matrix)
    assignment = [-1] * size
    occupied = [False] * size
    answers: set[Perm] = set()

    def compatible(source: int, target: int) -> bool:
        for old_source in range(size):
            old_target = assignment[old_source]
            if old_target >= 0 and matrix[source][old_source] != matrix[target][old_target]:
                return False
        return True

    def dfs(depth: int) -> None:
        if depth == size:
            answers.add(tuple(assignment))
            return
        # Fixed source ordering deliberately differs from the generator script.
        source = size - 1 - depth
        for target in range(size):
            if not occupied[target] and compatible(source, target):
                assignment[source] = target
                occupied[target] = True
                # Every remaining source must still have at least one target.
                viable = True
                for future_source in range(source):
                    if not any(
                        not occupied[future_target]
                        and compatible(future_source, future_target)
                        for future_target in range(size)
                    ):
                        viable = False
                        break
                if viable:
                    dfs(depth + 1)
                occupied[target] = False
                assignment[source] = -1

    dfs(0)
    return answers


def canonical_words(group: list[Perm], steps: tuple[Perm, ...]) -> dict[Perm, tuple[int, ...]]:
    words: dict[Perm, tuple[int, ...]] = {ONE: ()}
    queue = deque([ONE])
    while queue:
        current = queue.popleft()
        for label, step in enumerate(steps):
            nxt = mul(current, step)
            if nxt not in words:
                words[nxt] = words[current] + (label,)
                queue.append(nxt)
    if len(words) != len(group):
        raise RuntimeError("fixed generators did not span reconstructed A5")
    return words


def evaluate_word(word: tuple[int, ...], image_steps: tuple[Perm, ...]) -> Perm:
    value = ONE
    for label in word:
        value = mul(value, image_steps[label])
    return value


def independent_a5_automorphisms(group: list[Perm]) -> set[tuple[int, ...]]:
    a: Perm = (1, 2, 0, 3, 4)
    b: Perm = (1, 2, 3, 4, 0)
    steps = (a, b, inv(a), inv(b))
    words = canonical_words(group, steps)
    index = {g: i for i, g in enumerate(group)}
    answers: set[tuple[int, ...]] = set()
    for image_a in group:
        for image_b in group:
            image_steps = (image_a, image_b, inv(image_a), inv(image_b))
            mapping = {
                g: evaluate_word(words[g], image_steps)
                for g in group
            }
            if len(set(mapping.values())) != len(group):
                continue
            if all(
                mapping[mul(x, y)] == mul(mapping[x], mapping[y])
                for x in group for y in group
            ):
                answers.add(tuple(index[mapping[g]] for g in group))
    return answers


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", required=True, type=Path)
    parser.add_argument("--enumerator-script", required=True, type=Path)
    parser.add_argument("--verification", required=True, type=Path)
    args = parser.parse_args()

    cert = json.loads(args.certificate.read_text(encoding="utf-8"))
    claimed_digest = cert["certificate_sha256"]
    cert_without_digest = dict(cert)
    del cert_without_digest["certificate_sha256"]

    s5 = sorted(tuple(p) for p in itertools.permutations(range(N)))
    a5 = [p for p in s5 if sign(p) == 0]
    a5_index = {g: i for i, g in enumerate(a5)}
    involutions = [g for g in a5 if order(g) == 2]
    involution_index = {g: i for i, g in enumerate(involutions)}

    matrix = [[1 if i == j else order(mul(involutions[i], involutions[j]))
               for j in range(len(involutions))]
              for i in range(len(involutions))]

    listed_colour = {
        zero_based(p)
        for p in cert["full_colour_automorphism_group"]["elements_on_vertices"]
    }
    recomputed_colour = independent_colour_automorphisms(matrix)

    recomputed_group_auts = independent_a5_automorphisms(a5)
    listed_group_auts = {
        zero_based(p)
        for p in cert["full_A5_automorphism_enumeration"][
            "automorphisms_on_A5_elements"
        ]
    }

    recomputed_restrictions: set[Perm] = set()
    for automorphism in recomputed_group_auts:
        recomputed_restrictions.add(tuple(
            involution_index[a5[automorphism[a5_index[d]]]]
            for d in involutions
        ))
    listed_restrictions = {
        zero_based(p)
        for p in cert["full_A5_automorphism_enumeration"][
            "restriction_image_on_vertices"
        ]
    }

    conjugation_restrictions: set[Perm] = set()
    for s in s5:
        sinv = inv(s)
        conjugation_restrictions.add(tuple(
            involution_index[mul(mul(s, d), sinv)]
            for d in involutions
        ))

    reconstructed_vertices = [
        zero_based(row["images"])
        for row in cert["involution_class"]["vertices"]
    ]
    reconstructed_a5 = [
        zero_based(row["images"])
        for row in cert["group"]["elements"]
    ]

    checks = {
        "certificate_digest_matches": digest(cert_without_digest) == claimed_digest,
        "enumerator_script_hash_matches": (
            hashlib.sha256(args.enumerator_script.read_bytes()).hexdigest()
            == cert["script_sha256"]
        ),
        "reconstructed_S5_order_120": len(s5) == 120,
        "reconstructed_A5_order_60": len(a5) == 60,
        "certificate_A5_model_exact": reconstructed_a5 == a5,
        "reconstructed_involution_class_size_15": len(involutions) == 15,
        "certificate_involution_class_exact": reconstructed_vertices == involutions,
        "certificate_complete_colour_matrix_exact": (
            cert["complete_product_order_colouring"]["matrix"] == matrix
        ),
        "listed_colour_group_has_only_valid_permutations": all(
            len(set(p)) == len(involutions)
            and all(matrix[i][j] == matrix[p[i]][p[j]]
                    for i in range(len(involutions))
                    for j in range(len(involutions)))
            for p in listed_colour
        ),
        "independent_colour_enumeration_equals_certificate": (
            recomputed_colour == listed_colour
        ),
        "independent_A5_automorphism_enumeration_equals_certificate": (
            recomputed_group_auts == listed_group_auts
        ),
        "independent_restriction_image_equals_certificate": (
            recomputed_restrictions == listed_restrictions
        ),
        "S5_conjugation_image_equals_full_restriction_image": (
            conjugation_restrictions == recomputed_restrictions
        ),
        "restriction_image_is_contained_in_colour_group": (
            recomputed_restrictions <= recomputed_colour
        ),
        "certificate_comparison_relation_exact": (
            cert["comparison"]["relation"]
            == (
                "strict_containment_counterexample"
                if recomputed_colour - recomputed_restrictions
                else "equality_for_A5"
            )
        ),
    }

    verification = {
        "schema": "kourovka-21.52-a5-colour-independent-verification-v1",
        "certificate_sha256": claimed_digest,
        "verifier_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": checks,
        "recomputed_orders": {
            "full_colour_automorphism_group": len(recomputed_colour),
            "full_A5_automorphism_group": len(recomputed_group_auts),
            "restriction_image": len(recomputed_restrictions),
            "S5_conjugation_image": len(conjugation_restrictions),
        },
        "colour_only_elements": [
            [x + 1 for x in p]
            for p in sorted(recomputed_colour - recomputed_restrictions)
        ],
        "all_checks_pass": all(checks.values()),
    }
    verification["verification_sha256"] = digest(verification)

    args.verification.parent.mkdir(parents=True, exist_ok=True)
    args.verification.write_text(
        json.dumps(verification, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for name, passed in checks.items():
        print(f"CHECK {name} {passed}")
    print(f"ALL_CHECKS_PASS {verification['all_checks_pass']}")
    print(f"VERIFICATION_SHA256 {verification['verification_sha256']}")
    if not verification["all_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
