#!/usr/bin/env python3
"""Exact bounded check for Kourovka 21.89 using Euler's recurrence."""

import argparse
import json
import platform
import sympy
from sympy import factorint


def partitions_up_to(limit: int) -> list[int]:
    values = [0] * (limit + 1)
    values[0] = 1
    for n in range(1, limit + 1):
        total = 0
        k = 1
        while True:
            g1 = k * (3 * k - 1) // 2
            if g1 > n:
                break
            sign = 1 if k % 2 else -1
            total += sign * values[n - g1]
            g2 = k * (3 * k + 1) // 2
            if g2 <= n:
                total += sign * values[n - g2]
            k += 1
        values[n] = total
    return values


def factorial_valuation(n: int, prime: int) -> int:
    result = 0
    while n:
        n //= prime
        result += n
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int)
    args = parser.parse_args()
    ps = partitions_up_to(args.limit)
    divisors = []
    obstruction_counts = {"prime_gt_n": 0, "valuation_only": 0}
    examples = {"prime_gt_n": [], "valuation_only": []}
    for n in range(1, args.limit + 1):
        factors = factorint(ps[n])
        failures = [(q, e, factorial_valuation(n, q)) for q, e in factors.items()
                    if e > factorial_valuation(n, q)]
        if not failures:
            divisors.append(n)
        elif n >= 40:
            kind = "prime_gt_n" if any(q > n for q, _, _ in failures) else "valuation_only"
            obstruction_counts[kind] += 1
            if len(examples[kind]) < 10:
                examples[kind].append({"n": n, "p_n": ps[n], "factors": factors,
                                       "failures": failures})
    print(json.dumps({
        "python": platform.python_version(),
        "sympy": sympy.__version__,
        "limit": args.limit,
        "divisors": divisors,
        "obstruction_counts_for_n_ge_40": obstruction_counts,
        "first_examples": examples,
    }, indent=2))


if __name__ == "__main__":
    main()
