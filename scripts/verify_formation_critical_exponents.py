#!/usr/bin/env python3
"""Verify emergent critical exponents for formation words and trees.

- W(n): number of ordered prime-factor words, zeroed on primes for the
  composite-only nontrivial convention.
- T(n): number of unordered full binary prime-leaf factor trees.

The script uses coefficient data only for the empirical dyadic growth exponents.
No value 1/2 is used anywhere.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def spf_sieve(N: int):
    spf = list(range(N + 1))
    if N >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(N) + 1):
        if spf[p] == p:
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def distinct_prime_divisors(n: int, spf):
    out = []
    x = n
    while x > 1:
        p = spf[x]
        out.append(p)
        while x % p == 0:
            x //= p
    return out


def all_divisors(n: int, spf):
    factors = []
    x = n
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        factors.append((p, e))
    divs = [1]
    for p, e in factors:
        base = list(divs)
        mul = 1
        for _ in range(e):
            mul *= p
            divs.extend(d * mul for d in base)
    return divs


def formation_counts(N: int, spf):
    W = [0] * (N + 1)
    T = [0] * (N + 1)
    W[1] = 1

    for n in range(2, N + 1):
        prime = spf[n] == n

        # Ordered prime words with trivial one-letter prime word first.
        W[n] = sum(W[n // p] for p in distinct_prime_divisors(n, spf))

        # Unordered binary factor trees.
        if prime:
            T[n] = 1
        else:
            total = 0
            for a in all_divisors(n, spf):
                if a < 2:
                    continue
                b = n // a
                if a > b:
                    continue
                if a < b:
                    total += T[a] * T[b]
                else:
                    total += T[a] * (T[a] + 1) // 2
            T[n] = total

    # Repository convention: prime itself is not a nontrivial formation word.
    for n in range(2, N + 1):
        if spf[n] == n:
            W[n] = 0

    return W, T


def dyadic_rows(values, min_k: int, max_k: int):
    pref = [0] * len(values)
    total = 0
    for i, value in enumerate(values):
        total += value
        pref[i] = total

    rows = []
    prev_x = prev_A = None
    for k in range(min_k, max_k + 1):
        x = 2**k
        A = pref[x]
        if prev_x is not None and prev_A > 0:
            alpha = math.log(A / prev_A, 2)
            rows.append((x, alpha))
        prev_x, prev_A = x, A
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=524288)
    ap.add_argument("--min-k", type=int, default=10)
    ap.add_argument("--output", type=Path,
                    default=Path("data/formation/formation_critical_exponents_reproduction.csv"))
    args = ap.parse_args()

    max_k = int(math.log2(args.N))
    if 2**max_k > args.N:
        max_k -= 1

    spf = spf_sieve(args.N)
    W, T = formation_counts(args.N, spf)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["observable", "x", "dyadic_local_exponent"])
        for name, values in (("W", W), ("T", T)):
            for x, alpha in dyadic_rows(values, args.min_k, max_k):
                writer.writerow([name, x, f"{alpha:.12f}"])


if __name__ == "__main__":
    main()
