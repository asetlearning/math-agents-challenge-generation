#!/usr/bin/env python3
"""Exact bounded checks for the explicit controls in Kourovka 20.49.

This is deliberately not a general group package.  It implements only the four
coordinate models appearing in the submitted notes: D_30, the finite abelian
Nielsen control, B=C25:C4, and W:A4 (hence G0=(W:A4)xB).
"""

from collections import Counter, deque
from functools import reduce
from itertools import product
from math import gcd, lcm


def generated(identity, multiply, generators):
    seen = {identity}
    todo = deque([identity])
    while todo:
        x = todo.popleft()
        for g in generators:
            y = multiply(x, g)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return frozenset(seen)


def element_order(identity, multiply, x, cap=5000):
    y = identity
    for n in range(1, cap + 1):
        y = multiply(y, x)
        if y == identity:
            return n
    raise AssertionError(("order cap exceeded", x))


def exponent(identity, multiply, elements):
    return reduce(lcm, (element_order(identity, multiply, x) for x in elements), 1)


def pvaluation(n, p):
    ans = 0
    while n % p == 0:
        ans += 1
        n //= p
    return ans


# ---------------------------------------------------------------------------
# D_30 = <r,s | r^15=s^2=1, srs=r^-1>.

D_ID = (0, 0)
D_ELEMENTS = tuple(product(range(15), range(2)))


def dmul(x, y):
    i, j = x
    k, ell = y
    return ((i + (-1 if j else 1) * k) % 15, (j + ell) % 2)


def dinv(x):
    for y in D_ELEMENTS:
        if dmul(x, y) == D_ID and dmul(y, x) == D_ID:
            return y
    raise AssertionError(x)


def all_d_subgroups():
    known = {frozenset({D_ID})}
    todo = deque(known)
    while todo:
        h = todo.popleft()
        for g in D_ELEMENTS:
            if g not in h:
                k = generated(D_ID, dmul, tuple(h) + (g,))
                if k not in known:
                    known.add(k)
                    todo.append(k)
    return known


D_SUBGROUPS = all_d_subgroups()
D_NORMAL = {
    h
    for h in D_SUBGROUPS
    if all(dmul(dmul(g, x), dinv(g)) in h for g in D_ELEMENTS for x in h)
}


def quotient_exponent_d(normal):
    ans = 1
    for g in D_ELEMENTS:
        power = D_ID
        for k in range(1, 31):
            power = dmul(power, g)
            if power in normal:
                ans = lcm(ans, k)
                break
        else:
            raise AssertionError((normal, g))
    return ans


d_exp = exponent(D_ID, dmul, D_ELEMENTS)
d_proper_exps = sorted({exponent(D_ID, dmul, h) for h in D_SUBGROUPS if len(h) < 30})
d_quotients = sorted(
    (len(h), quotient_exponent_d(h)) for h in D_NORMAL if 1 < len(h) < 30
)
d_minimal_normal_orders = sorted(
    len(h)
    for h in D_NORMAL
    if len(h) > 1
    and not any(1 < len(k) < len(h) and k.issubset(h) for k in D_NORMAL)
)
d_direct_factor_pairs = []
for a in D_NORMAL:
    for b in D_NORMAL:
        if 1 < len(a) < 30 and 1 < len(b) < 30:
            products = {dmul(x, y) for x in a for y in b}
            if a.intersection(b) == {D_ID} and len(products) == 30:
                d_direct_factor_pairs.append((len(a), len(b)))

assert d_exp == 30
assert d_proper_exps == [1, 2, 3, 5, 6, 10, 15]
assert d_quotients == [(3, 10), (5, 6), (15, 2)]
assert d_minimal_normal_orders == [3, 5]
assert not d_direct_factor_pairs
print("D30_PASS")
print(
    f"elements={len(D_ELEMENTS)} subgroups={len(D_SUBGROUPS)} "
    f"normal_subgroups={len(D_NORMAL)} exponent={d_exp}"
)
print(f"proper_subgroup_exponents={d_proper_exps}")
print(f"nontrivial_proper_normal_order_and_quotient_exponent={d_quotients}")
print(
    f"minimal_normal_orders={d_minimal_normal_orders} "
    f"nontrivial_direct_factor_pairs={len(d_direct_factor_pairs)}"
)


# ---------------------------------------------------------------------------
# Abelian Nielsen-move control.

A_MODS = (2, 2, 2, 3, 5, 7, 11)
A_ID = (0,) * len(A_MODS)
A_ELEMENTS = tuple(product(*(range(m) for m in A_MODS)))


def aadd(x, y):
    return tuple((u + v) % m for u, v, m in zip(x, y, A_MODS))


def aorder(x):
    return reduce(lcm, (m // gcd(v, m) for v, m in zip(x, A_MODS)), 1)


x_a = (1, 0, 0, 1, 1, 0, 0)
y_a = (0, 1, 0, -1 % 3, 0, 1, 0)
z_a = (0, 0, 1, 0, 0, 0, 1)
xp_a = aadd(x_a, y_a)
ambient_a_exp = reduce(lcm, A_MODS, 1)


def abelian_pair_exponent(u, v):
    return lcm(aorder(u), aorder(v))


def defects(e):
    return tuple(p for p in (2, 3, 5, 7, 11) if pvaluation(e, p) < pvaluation(ambient_a_exp, p))


t_size = len(generated(A_ID, aadd, (x_a, y_a, z_a)))
tp_size = len(generated(A_ID, aadd, (xp_a, y_a, z_a)))
t_defects = {
    "xy": defects(abelian_pair_exponent(x_a, y_a)),
    "xz": defects(abelian_pair_exponent(x_a, z_a)),
    "yz": defects(abelian_pair_exponent(y_a, z_a)),
}
tp_defects = {
    "x+y,y": defects(abelian_pair_exponent(xp_a, y_a)),
    "x+y,z": defects(abelian_pair_exponent(xp_a, z_a)),
    "yz": defects(abelian_pair_exponent(y_a, z_a)),
}
assert len(A_ELEMENTS) == 9240 and ambient_a_exp == 2310
assert t_size == tp_size == len(A_ELEMENTS)
assert t_defects == {"xy": (11,), "xz": (7,), "yz": (5,)}
assert tp_defects == {"x+y,y": (11,), "x+y,z": (3,), "yz": (5,)}
print("NIELSEN_CONTROL_PASS")
print(
    f"group_order={len(A_ELEMENTS)} exponent={ambient_a_exp} "
    f"T_generated={t_size} Tprime_generated={tp_size}"
)
print(f"T_defects={t_defects}")
print(f"Tprime_defects={tp_defects}")


# ---------------------------------------------------------------------------
# B = C25 : C4, with c a c^-1 = a^7.

B_ID = (0, 0)
B_ELEMENTS = tuple(product(range(25), range(4)))


def bmul(x, y):
    i, j = x
    k, ell = y
    return ((i + pow(7, j, 25) * k) % 25, (j + ell) % 4)


B_ORDERS = {b: element_order(B_ID, bmul, b) for b in B_ELEMENTS}
b_exp = reduce(lcm, B_ORDERS.values(), 1)
assert pow(7, 2, 25) == 24 and pow(7, 4, 25) == 1
assert b_exp == 100
assert all(25 % o == 0 or 4 % o == 0 for o in B_ORDERS.values())
assert all(o % 100 != 0 for o in B_ORDERS.values())
print("B_CONTROL_PASS")
print(
    f"order={len(B_ELEMENTS)} exponent={b_exp} "
    f"element_order_distribution={dict(sorted(Counter(B_ORDERS.values()).items()))}"
)
print("elements_with_order_divisible_by_4_and_25=0")


# ---------------------------------------------------------------------------
# W : A4 and G0 = (W : A4) x B.

P_ID = (0, 1, 2, 3)


def pcompose(p, q):
    return tuple(p[q[i]] for i in range(4))


def pact(p, vector):
    out = [0, 0, 0, 0]
    for i, value in enumerate(vector):
        out[p[i]] = value
    return tuple(out)


u = (1, 2, 0, 3)
v = (1, 0, 3, 2)
A4 = generated(P_ID, pcompose, (u, v))
assert len(A4) == 12

W_ZERO = (0, 0, 0, 0)
W = tuple(w for w in product(range(3), repeat=4) if sum(w) % 3 == 0)


def wadd(x, y):
    return tuple((a + b) % 3 for a, b in zip(x, y))


def wneg(x):
    return tuple((-a) % 3 for a in x)


def wspan(vectors):
    return generated(W_ZERO, wadd, vectors)


subspaces = {wspan(())}
for a in W:
    subspaces.add(wspan((a,)))
    for b in W:
        subspaces.add(wspan((a, b)))
subspaces.add(frozenset(W))
invariant_subspaces = [
    space
    for space in subspaces
    if all(pact(g, w) in space for g in A4 for w in space)
]
proper_nonzero_invariant = [space for space in invariant_subspaces if 1 < len(space) < len(W)]
assert len(W) == 27 and len(subspaces) == 28
assert not proper_nonzero_invariant

n_w = (1, 0, 0, 2)
u2 = pcompose(u, u)
norm_n = wadd(wadd(n_w, pact(u, n_w)), pact(u2, n_w))
assert norm_n == (1, 1, 1, 0)
norm_orbit_span = wspan(tuple(pact(g, norm_n) for g in A4))
assert len(norm_orbit_span) == len(W)


def xop(w):
    return wadd(pact(u, w), wneg(w))


x_image = {xop(w) for w in W}
x2_image = {xop(xop(w)) for w in W}
x3_image = {xop(xop(xop(w))) for w in W}
assert (len(x_image), len(x2_image), len(x3_image)) == (9, 3, 1)

K_ID = (W_ZERO, P_ID)
K_ELEMENTS = tuple(product(W, A4))


def kmul(x, y):
    wx, px = x
    wy, py = y
    return (wadd(wx, pact(px, wy)), pcompose(px, py))


K_ORDERS = {k: element_order(K_ID, kmul, k) for k in K_ELEMENTS}
k_exp = reduce(lcm, K_ORDERS.values(), 1)
assert k_exp == 18

G_ID = (K_ID, B_ID)


def gmul(x, y):
    return (kmul(x[0], y[0]), bmul(x[1], y[1]))


x_g = ((n_w, u), B_ID)
y_g = ((W_ZERO, v), (0, 1))
z_g = (K_ID, (1, 0))
g_generators = (x_g, y_g, z_g)
g_orders = tuple(element_order(G_ID, gmul, g) for g in g_generators)
g0_exp = lcm(k_exp, b_exp)
g0_generated = generated(G_ID, gmul, g_generators)
assert g_orders == (9, 4, 25)
assert g0_exp == 900
assert len(g0_generated) == len(K_ELEMENTS) * len(B_ELEMENTS) == 32400


def g_order(g):
    return lcm(K_ORDERS[g[0]], B_ORDERS[g[1]])


def subgroup_exponent_g(gens):
    h = generated(G_ID, gmul, gens)
    return len(h), reduce(lcm, (g_order(t) for t in h), 1)


xy_size, xy_exp = subgroup_exponent_g((x_g, y_g))
xz_size, xz_exp = subgroup_exponent_g((x_g, z_g))
yz_size, yz_exp = subgroup_exponent_g((y_g, z_g))


def g0_defects(e):
    return tuple(p for p in (2, 3, 5) if pvaluation(e, p) < pvaluation(g0_exp, p))


pair_data = {
    "xy": (xy_size, xy_exp, g0_defects(xy_exp)),
    "xz": (xz_size, xz_exp, g0_defects(xz_exp)),
    "yz": (yz_size, yz_exp, g0_defects(yz_exp)),
}
assert pair_data["xy"][2] == (5,)
assert pair_data["xz"][2] == (2,)
assert pair_data["yz"][2] == (3,)

# Since B acts trivially on W and commutes with A4, G0 is the direct product
# K x B.  The B-projection of <x,w> is cyclic, K has no 5-part and only one
# factor of 2 in its exponent, so a full-exponent partner would require a B
# element whose order is divisible by both 4 and 25.  The exhaustive B table
# above proves that there is none; the count of possible w is recorded here.
partner_capable_b = [b for b, order in B_ORDERS.items() if order % 4 == 0 and order % 25 == 0]
assert not partner_capable_b
assert all(pvaluation(order, 2) <= 1 and pvaluation(order, 5) == 0 for order in K_ORDERS.values())
print("G0_CONTROL_PASS")
print(
    f"W_order={len(W)} W_subspaces={len(subspaces)} "
    f"proper_nonzero_A4_invariant_subspaces={len(proper_nonzero_invariant)}"
)
print(
    f"u_minus_1_image_sizes={[len(x_image), len(x2_image), len(x3_image)]} "
    f"norm_n={norm_n} norm_orbit_span={len(norm_orbit_span)}"
)
print(
    f"K_order={len(K_ELEMENTS)} K_exponent={k_exp} B_order={len(B_ELEMENTS)} "
    f"G0_order={len(g0_generated)} G0_exponent={g0_exp} generator_orders={g_orders}"
)
print(f"pair_size_exponent_defects={pair_data}")
print(
    f"partner_capable_B_coordinates={len(partner_capable_b)} "
    f"G0_elements_covered_by_direct_product_argument={len(K_ELEMENTS) * len(B_ELEMENTS)}"
)
