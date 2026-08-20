#!/usr/bin/env python3
"""Bounded exact arithmetic probe for the conditional Suzuki criterion.

This does not inspect groups or character tables.  It only factors the explicit
order formula for odd 3 <= n <= 15 and checks (P1)--(P2).
"""


def factor(integer):
    factors = {}
    divisor = 2
    remaining = integer
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def multiplicative_order(base, prime):
    order = prime - 1
    for divisor in factor(order):
        while order % divisor == 0 and pow(base, order // divisor, prime) == 1:
            order //= divisor
    return order


for exponent in range(3, 16, 2):
    q = 2**exponent
    odd_factors = factor((q * q + 1) * (q - 1))
    all_factors = {2: 2 * exponent, **odd_factors}
    primitive = []
    good = []
    for prime, valuation in factor(q * q + 1).items():
        if multiplicative_order(2, prime) != 4 * exponent:
            continue
        primitive.append((prime, valuation))
        failures = []
        for other, other_valuation in odd_factors.items():
            if other == prime:
                continue
            other_order = multiplicative_order(other % prime, prime)
            if other_order <= other_valuation:
                failures.append((other, other_valuation, other_order))
        if not failures:
            good.append((prime, valuation))
    print(
        f"n={exponent} factors={all_factors} "
        f"P1_candidates={primitive} P1_P2_candidates={good}"
    )
