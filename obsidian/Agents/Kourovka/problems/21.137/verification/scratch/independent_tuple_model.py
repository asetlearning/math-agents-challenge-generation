from itertools import product


def dmul(x, y):
    """Multiply r^i s^j by r^k s^l in D_8."""
    i, j = x
    k, ell = y
    return ((i + (k if j == 0 else -k)) % 4, (j + ell) % 2)


D = tuple(product(range(4), range(2)))
W = tuple(product(D, D, range(2)))
one = ((0, 0), (0, 0), 0)


def wmul(x, y):
    a, b, t = x
    c, d, u = y
    if t:
        c, d = d, c
    return (dmul(a, c), dmul(b, d), (t + u) % 2)


def wpow(x, n):
    z = one
    for _ in range(n):
        z = wmul(z, x)
    return z


squares = {wpow(x, 2) for x in W}
mul_closed = all(wmul(x, y) in squares for x in squares for y in squares)
exp_divides_8 = all(wpow(x, 8) == one for x in W)
order_8_witness = next(x for x in W if wpow(x, 4) != one)
noncommuting = next(
    (x, y) for x in squares for y in squares if wmul(x, y) != wmul(y, x)
)

print("MODEL=D8_TUPLES_SEMIDIRECT_SWAP_C2")
print(f"D_SIZE={len(D)} W_SIZE={len(W)}")
print(f"SQUARE_SET_SIZE={len(squares)} MUL_CLOSED={str(mul_closed).lower()}")
print(f"EXPONENT_DIVIDES_8={str(exp_divides_8).lower()}")
print(f"ORDER_8_WITNESS={order_8_witness}")
print(f"ORDER_8_WITNESS_FOURTH={wpow(order_8_witness, 4)}")
print(f"NONCOMMUTING_SQUARES={noncommuting}")
print("RUN_COMPLETE=true")
