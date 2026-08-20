#!/usr/bin/env python3
"""Exact order-8 abelian action/orbit check for Kourovka 12.15 M1.

For A=C8, C4xC2, C2^3:
  * enumerate Aut(A) from generator images;
  * enumerate faithful V4 subgroups;
  * retain actions with |A^E|=2;
  * quotient by Aut(A)-conjugacy (E relabeling is already forgotten);
  * test whether every orbit O(a) is an affine subgroup a+Q;
  * apply the necessary q-occurrence rows A^2 <= Q and |Q:A^2| <= 2.
"""

from itertools import product


def add(x, y, moduli):
    return tuple((a + b) % n for a, b, n in zip(x, y, moduli))


def neg(x, moduli):
    return tuple((-a) % n for a, n in zip(x, moduli))


def scale(k, x, moduli):
    return tuple((k * a) % n for a, n in zip(x, moduli))


def subgroup(elements, moduli):
    S = set(elements)
    zero = tuple(0 for _ in moduli)
    return zero in S and all(neg(x, moduli) in S for x in S) and all(
        add(x, y, moduli) in S for x in S for y in S
    )


def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    ans = [0] * len(p)
    for i, j in enumerate(p):
        ans[j] = i
    return tuple(ans)


def build_automorphisms(moduli):
    elems = list(product(*(range(n) for n in moduli)))
    index = {x: i for i, x in enumerate(elems)}
    rank = len(moduli)
    basis = [tuple(1 if i == j else 0 for i in range(rank)) for j in range(rank)]
    image_choices = []
    for n in moduli:
        image_choices.append([x for x in elems if scale(n, x, moduli) == elems[0]])

    autos = {}
    for images in product(*image_choices):
        values = []
        for x in elems:
            value = elems[0]
            for coefficient, image in zip(x, images):
                value = add(value, scale(coefficient, image, moduli), moduli)
            values.append(index[value])
        perm = tuple(values)
        if len(set(perm)) == len(elems):
            autos[perm] = images
    return elems, index, basis, autos


def v4_subgroups(autos):
    perms = list(autos)
    ident = tuple(range(len(perms[0])))
    involutions = [p for p in perms if p != ident and compose(p, p) == ident]
    groups = set()
    for i, p in enumerate(involutions):
        for q in involutions[i + 1 :]:
            if compose(p, q) != compose(q, p):
                continue
            pq = compose(p, q)
            S = frozenset((ident, p, q, pq))
            if len(S) == 4:
                groups.add(S)
    return groups


def conjugacy_classes(groups, autos):
    unseen = set(groups)
    classes = []
    while unseen:
        representative = min(unseen, key=lambda S: tuple(sorted(S)))
        orbit = set()
        for p in autos:
            pinv = inverse(p)
            orbit.add(
                frozenset(compose(compose(p, h), pinv) for h in representative)
            )
        orbit &= set(groups)
        classes.append((representative, orbit))
        unseen -= orbit
    return classes


def fmt(x):
    return "(" + ",".join(str(a) for a in x) + ")"


def analyze(name, moduli):
    elems, index, basis, autos_map = build_automorphisms(moduli)
    autos = list(autos_map)
    ident = tuple(range(len(elems)))
    all_v4 = v4_subgroups(autos)
    compatible = set()
    for S in all_v4:
        fixed = [x for x in elems if all(h[index[x]] == index[x] for h in S)]
        if len(fixed) == 2:
            compatible.add(S)
    classes = conjugacy_classes(compatible, autos)
    twoA = {scale(2, x, moduli) for x in elems}

    print(f"=== {name} ===")
    print(f"moduli={moduli}")
    print(f"|Aut(A)|={len(autos)}")
    print(f"V4 subgroups={len(all_v4)}")
    print(f"compatible V4 subgroups with |A^E|=2: {len(compatible)}")
    print(f"Aut(A)-conjugacy classes of compatible actions: {len(classes)}")
    print("A^2={" + ",".join(sorted(fmt(x) for x in twoA)) + "}")

    for class_no, (S, conjugates) in enumerate(classes, 1):
        fixed = [x for x in elems if all(h[index[x]] == index[x] for h in S)]
        z = next(x for x in fixed if x != elems[0])
        generators = sorted((h for h in S if h != ident))
        print(f"-- action class {class_no}; conjugates={len(conjugates)}; z={fmt(z)}")
        for j, h in enumerate(generators, 1):
            images = [elems[h[index[e]]] for e in basis]
            print(f"  nonidentity map {j}: generators -> " + ",".join(fmt(x) for x in images))

        seen = set()
        orbit_rows = []
        for a in elems:
            if a in seen:
                continue
            O = {elems[h[index[a]]] for h in S}
            seen |= O
            Q = {add(o, neg(a, moduli), moduli) for o in O}
            affine = subgroup(Q, moduli) and {
                add(a, q, moduli) for q in Q
            } == O
            occurrence = (
                affine
                and twoA <= Q
                and len(Q) % len(twoA) == 0
                and len(Q) // len(twoA) <= 2
            )
            orbit_rows.append((a, O, Q, affine, occurrence))

        for a, O, Q, affine, occurrence in orbit_rows:
            print(
                "  a="
                + fmt(a)
                + " orbit={"
                + ",".join(sorted(fmt(x) for x in O))
                + "} Q=orbit-a={"
                + ",".join(sorted(fmt(x) for x in Q))
                + f"}} affine_subgroup={affine} q_occurrence_necessary={occurrence}"
            )
    print()


def main():
    analyze("C8", (8,))
    analyze("C4xC2", (4, 2))
    analyze("C2^3", (2, 2, 2))


if __name__ == "__main__":
    main()
