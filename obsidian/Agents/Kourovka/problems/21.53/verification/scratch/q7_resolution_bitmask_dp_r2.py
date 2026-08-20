#!/usr/bin/env python3
"""Independent q=7 certificate checker using projective charts and bitmask DP.

This deliberately does not reuse the claimant's projective canonicalization or
list-valued exact-cover search.  A resolution is counted by a memoized recurrence
on the covered-point bitmask, pivoting at the least uncovered point.
"""

from functools import cache

F = 7
NS = {3, 5, 6}


def projective_chart():
    """The unique representatives whose first nonzero coordinate is 1."""
    return (
        [(1, y, z) for y in range(F) for z in range(F)]
        + [(0, 1, z) for z in range(F)]
        + [(0, 0, 1)]
    )


def normalize(v):
    v = tuple(a % F for a in v)
    j = next(i for i, a in enumerate(v) if a)
    inv = pow(v[j], -1, F)
    return tuple((a * inv) % F for a in v)


def q(v):
    x, y, z = v
    return (y * y - x * z) % F


def dot(v, w):
    return sum(a * b for a, b in zip(v, w)) % F


def det3(rows):
    (a, b, c), (d, e, f), (g, h, i) = rows
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)) % F


POINTS = tuple(projective_chart())
LINES = POINTS
assert len(POINTS) == F * F + F + 1 == 57

CONIC = frozenset(v for v in POINTS if q(v) == 0)
INTERNAL = tuple(sorted(v for v in POINTS if q(v) in NS))
INDEX = {v: i for i, v in enumerate(INTERNAL)}
FULL = (1 << len(INTERNAL)) - 1
assert len(CONIC) == 8 and len(INTERNAL) == 21


def mask(points):
    answer = 0
    for v in points:
        answer |= 1 << INDEX[normalize(v)]
    return answer


def line_support(line):
    return frozenset(v for v in INTERNAL if dot(v, line) == 0)


def conic_section(line):
    return frozenset(v for v in CONIC if dot(v, line) == 0)


SECANT_LINES = tuple(line for line in LINES if len(conic_section(line)) == 2)
GEOMETRIC = frozenset(mask(line_support(line)) for line in SECANT_LINES)
assert len(SECANT_LINES) == len(GEOMETRIC) == 28
assert all(block.bit_count() == 3 for block in GEOMETRIC)

# Submitted points: check exact values before normalization, then square class.
RAW_SIX = ((1, 0, 1), (3, 1, 1), (5, 2, 1), (2, 0, 1), (4, 0, 1), (6, 4, 1))
assert tuple(q(v) for v in RAW_SIX) == (6, 5, 6, 5, 3, 3)
P, A, B, C, D, R = tuple(normalize(v) for v in RAW_SIX)
SIX = (P, A, B, C, D, R)
assert all(q(v) in NS for v in SIX)

OLD = frozenset(
    mask(block)
    for block in ((P, A, B), (P, C, D), (A, C, R), (B, D, R))
)
NEW = frozenset(
    mask(block)
    for block in ((P, A, C), (P, B, D), (A, B, R), (C, D, R))
)
assert OLD <= GEOMETRIC
assert not (NEW & GEOMETRIC)
assert all(
    det3(block) != 0
    for block in ((P, A, C), (P, B, D), (A, B, R), (C, D, R))
)

TRADED = (GEOMETRIC - OLD) | NEW
assert len(TRADED) == 28


def gram_signature(blocks):
    """Diagonal and upper-triangular entries of X X^T, as an integer tuple."""
    result = []
    for i in range(len(INTERNAL)):
        bi = 1 << i
        result.append(sum(bool(block & bi) for block in blocks))
        for j in range(i + 1, len(INTERNAL)):
            bj = 1 << j
            result.append(sum((block & bi) and (block & bj) for block in blocks))
    return tuple(result)


assert gram_signature(GEOMETRIC) == gram_signature(TRADED)


def count_resolutions(blocks):
    """Count partitions of all 21 points by seven distinct weight-three blocks."""
    blocks = tuple(sorted(blocks))
    through = tuple(
        tuple(block for block in blocks if block & (1 << point))
        for point in range(len(INTERNAL))
    )

    @cache
    def ways(covered):
        if covered == FULL:
            return 1
        remaining = FULL ^ covered
        pivot_bit = remaining & -remaining
        pivot = pivot_bit.bit_length() - 1
        return sum(
            ways(covered | block)
            for block in through[pivot]
            if not (covered & block)
        )

    return ways(0)


print(f"projective_points={len(POINTS)}")
print(f"conic_points={len(CONIC)}")
print(f"internal_points={len(INTERNAL)}")
print(f"geometric_blocks={len(GEOMETRIC)}")
print(f"traded_blocks={len(TRADED)}")
print(f"new_determinants={[det3(b) for b in ((P,A,C),(P,B,D),(A,B,R),(C,D,R))]}")
print(f"gram_equal={gram_signature(GEOMETRIC) == gram_signature(TRADED)}")
print(f"geometric_resolutions={count_resolutions(GEOMETRIC)}")
print(f"traded_resolutions={count_resolutions(TRADED)}")
