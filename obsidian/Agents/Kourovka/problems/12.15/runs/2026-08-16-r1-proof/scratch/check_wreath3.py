#!/usr/bin/env python3
"""Exact diagnostic for the standard Sylow-2 subgroup C2 wr C2 wr C2 <= S8.

This is a bounded, problem-specific enumerator.  Permutations act on the right;
mul(p, q) means first p, then q.
"""

from collections import deque


def mul(p, q):
    return tuple(q[p[i]] for i in range(len(p)))


def inv(p):
    ans = [0] * len(p)
    for i, j in enumerate(p):
        ans[j] = i
    return tuple(ans)


def conj(x, g):
    return mul(mul(inv(g), x), g)


def comm(x, g):
    return mul(inv(x), conj(x, g))


def generated(gens, identity):
    gens = tuple(dict.fromkeys((*gens, *(inv(g) for g in gens))))
    seen = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for g in gens:
            b = mul(a, g)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return frozenset(seen)


def cycles(p):
    seen = set()
    out = []
    for i in range(len(p)):
        if i in seen or p[i] == i:
            continue
        cyc = []
        j = i
        while j not in seen:
            seen.add(j)
            cyc.append(j + 1)
            j = p[j]
        out.append("(" + " ".join(map(str, cyc)) + ")")
    return "".join(out) or "()"


def main():
    identity = tuple(range(8))

    # (1 2), (1 3)(2 4), (1 5)(2 6)(3 7)(4 8)
    generators = (
        (1, 0, 2, 3, 4, 5, 6, 7),
        (2, 3, 0, 1, 4, 5, 6, 7),
        (4, 5, 6, 7, 0, 1, 2, 3),
    )
    group = generated(generators, identity)
    ordered = tuple(sorted(group))

    defect = {}
    conjugacy_class = {}
    normal_closure = {}
    first_intrinsic_failure = None
    for x in ordered:
        values = frozenset(comm(x, g) for g in ordered)
        defect[x] = values
        is_subgroup = generated(values, identity) == values
        square_in = mul(x, x) in values
        if first_intrinsic_failure is None and not (is_subgroup and square_in):
            first_intrinsic_failure = (x, len(values), is_subgroup, square_in)

        cls = frozenset(conj(x, g) for g in ordered)
        conjugacy_class[x] = cls
        normal_closure[x] = generated(cls, identity)

    first_fibre_failure = None
    for i, x in enumerate(ordered):
        for y in ordered[i + 1 :]:
            if normal_closure[x] == normal_closure[y] and y not in conjugacy_class[x]:
                first_fibre_failure = (x, y, len(normal_closure[x]))
                break
        if first_fibre_failure:
            break

    commutators = frozenset(comm(x, y) for x in ordered for y in ordered)
    derived = generated(commutators, identity)
    derived_ordered = tuple(sorted(derived))
    second_commutators = frozenset(
        comm(x, y) for x in derived_ordered for y in derived_ordered
    )
    second_derived = generated(second_commutators, identity)

    print("group: standard <(1 2),(1 3)(2 4),(1 5)(2 6)(3 7)(4 8)> <= S8")
    print(f"group_order: {len(group)}")
    print(f"derived_order: {len(derived)}")
    print(f"second_derived_order: {len(second_derived)}")
    print(f"normal_closure_fibre_property: {first_fibre_failure is None}")
    if first_fibre_failure:
        x, y, n_order = first_fibre_failure
        print(
            "first_fibre_failure: "
            f"x={cycles(x)} y={cycles(y)} shared_normal_closure_order={n_order}"
        )
        print(f"x_conjugacy_class_order: {len(conjugacy_class[x])}")
        print(f"y_conjugacy_class_order: {len(conjugacy_class[y])}")
    print(f"intrinsic_conditions_hold: {first_intrinsic_failure is None}")
    if first_intrinsic_failure:
        x, value_count, is_subgroup, square_in = first_intrinsic_failure
        print(
            "first_intrinsic_failure: "
            f"x={cycles(x)} commutator_value_count={value_count} "
            f"value_set_is_subgroup={is_subgroup} square_in_value_set={square_in}"
        )


if __name__ == "__main__":
    main()
