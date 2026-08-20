#!/usr/bin/env python3
"""Exact F_7 audit of the hand-derived Pasch trade; no external packages."""

from itertools import product

P = 7
SQUARES = {1, 2, 4}


def canon(v):
    v = tuple(x % P for x in v)
    for x in v:
        if x:
            inv = pow(x, -1, P)
            return tuple((inv * y) % P for y in v)
    raise ValueError("zero projective vector")


POINTS = sorted({canon(v) for v in product(range(P), repeat=3) if any(v)})
LINES = POINTS


def qform(v):
    x, y, z = v
    return (y * y - x * z) % P


def incident(point, line):
    return sum(x * a for x, a in zip(point, line)) % P == 0


CONIC = {x for x in POINTS if qform(x) == 0}
INTERNAL = {x for x in POINTS if qform(x) in {3, 5, 6}}
SECANTS = []
for line in LINES:
    on_conic = {x for x in CONIC if incident(x, line)}
    if len(on_conic) == 2:
        support = frozenset(x for x in INTERNAL if incident(x, line))
        assert len(support) == 3
        SECANTS.append((line, support, frozenset(on_conic)))

assert len(POINTS) == 57 and len(CONIC) == 8 and len(INTERNAL) == 21
assert len(SECANTS) == 28

P0 = canon((1, 0, 1))
A = canon((3, 1, 1))
B = canon((5, 2, 1))
C = canon((2, 0, 1))
D = canon((4, 0, 1))
R = canon((6, 4, 1))

old = {
    frozenset((P0, A, B)),
    frozenset((P0, C, D)),
    frozenset((A, C, R)),
    frozenset((B, D, R)),
}
new = {
    frozenset((P0, A, C)),
    frozenset((P0, B, D)),
    frozenset((A, B, R)),
    frozenset((C, D, R)),
}
geometric = {support for _, support, _ in SECANTS}
assert old <= geometric and not (new & geometric)


def gram(blocks):
    return {
        (x, y): sum(x in block and y in block for block in blocks)
        for x in INTERNAL
        for y in INTERNAL
    }


traded = (geometric - old) | new
assert len(traded) == 28
assert gram(geometric) == gram(traded)


def exact_covers(blocks):
    blocks = sorted(blocks, key=lambda b: tuple(sorted(b)))
    by_point = {x: [b for b in blocks if x in b] for x in INTERNAL}
    answers = []

    def visit(uncovered, chosen):
        if not uncovered:
            answers.append(tuple(chosen))
            return
        x = min(uncovered, key=lambda p: len([b for b in by_point[p] if b <= uncovered]))
        for block in by_point[x]:
            if block <= uncovered:
                visit(uncovered - block, chosen + [block])

    visit(frozenset(INTERNAL), [])
    return answers


original_resolutions = exact_covers(geometric)
traded_resolutions = exact_covers(traded)

print(f"points={len(POINTS)} conic={len(CONIC)} internal={len(INTERNAL)}")
print(f"geometric_columns={len(geometric)} traded_columns={len(traded)}")
print(f"gram_equal={gram(geometric) == gram(traded)}")
print(f"original_resolutions={len(original_resolutions)}")
print(f"traded_resolutions={len(traded_resolutions)}")
for i, resolution in enumerate(traded_resolutions, 1):
    encoded = [sorted(block) for block in resolution]
    print(f"traded_resolution_{i}={encoded}")
