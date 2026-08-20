#!/usr/bin/env python3
"""Enumerate formal F_3 defect-support occurrence families.

Filters: nonempty supports; closure under k -> -k; one admissible identity
support ({0} or F_3); and A intersect (-B) nonempty for every ordered pair.
This is only a set-system classifier, not a group-realization search.
"""

from itertools import combinations

F3 = frozenset((0, 1, 2))
SUPPORTS = tuple(
    frozenset(c)
    for r in range(1, 4)
    for c in combinations((0, 1, 2), r)
)


def neg(a):
    return frozenset((-x) % 3 for x in a)


def label(a):
    return "{" + ",".join(str(x) for x in sorted(a)) + "}"


def powerset(items):
    for mask in range(1, 1 << len(items)):
        yield frozenset(items[i] for i in range(len(items)) if mask >> i & 1)


valid = []
for family in powerset(SUPPORTS):
    if not ({frozenset((0,))} <= family or {F3} <= family):
        continue  # Delta(1,1) must be {0} or F_3
    if {neg(a) for a in family} != set(family):
        continue
    if any(not (a & neg(b)) for a in family for b in family):
        continue
    common = set.intersection(*(set(a) for a in family))
    valid.append((family, frozenset(common)))

valid.sort(key=lambda row: (len(row[0]), sorted(map(label, row[0]))))
print(f"formal_family_count={len(valid)}")
for i, (family, common) in enumerate(valid, 1):
    names = sorted((label(a) for a in family), key=lambda s: (len(s), s))
    kind = "triangle" if not common else "common-shift"
    print(f"F{i}: supports={names} common={label(common)} kind={kind}")
