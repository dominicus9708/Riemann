#!/usr/bin/env python3
"""Coefficient audit for formation-word and formation-tree generating identities.

Checks through a finite bound N:

1) Ordered prime words W~(n):
       W~(1)=1,
       W~(n)=sum_{p|n} W~(n/p)
   equivalent formally to
       sum W~(n)n^-s = 1/(1-P(s)).

2) Unordered full binary prime-leaf factor trees T~(n):
       T(s)=P(s)+1/2*(T(s)^2+T(2s)).

No analytic continuation claims are made by this script; it verifies coefficients.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter
from functools import lru_cache


def sieve(N: int):
    spf = list(range(N + 1))
    if N >= 1:
        spf[0] = spf[1] = 0
    for p in range(2, math.isqrt(N) + 1):
        if spf[p] == p:
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    is_prime = [False] * (N + 1)
    for n in range(2, N + 1):
        is_prime[n] = spf[n] == n
    return spf, is_prime


def prime_factors(n: int, spf):
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        n //= p
    return out


def word_count(n: int, spf, is_prime):
    if n == 1 or is_prime[n]:
        return 1
    vals = prime_factors(n, spf)
    c = Counter(vals)
    ans = math.factorial(len(vals))
    for e in c.values():
        ans //= math.factorial(e)
    return ans


def factor_pairs(n: int):
    return [(a, n // a) for a in range(2, math.isqrt(n) + 1) if n % a == 0]


def build_trees(is_prime):
    @lru_cache(maxsize=None)
    def trees(n: int):
        if is_prime[n]:
            return (str(n),)
        out = set()
        for a, b in factor_pairs(n):
            for left in trees(a):
                for right in trees(b):
                    x, y = sorted((left, right))
                    out.add(f"({x}*{y})")
        return tuple(sorted(out))
    return trees


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=1000)
    args = ap.parse_args()

    spf, is_prime = sieve(args.N)
    primes = [p for p in range(2, args.N + 1) if is_prime[p]]

    W = [0] * (args.N + 1)
    W[1] = 1
    word_mismatches = []
    for n in range(2, args.N + 1):
        W[n] = word_count(n, spf, is_prime)
        rhs = sum(W[n // p] for p in primes if p <= n and n % p == 0)
        if W[n] != rhs:
            word_mismatches.append((n, W[n], rhs))

    trees = build_trees(is_prime)
    T = [0] * (args.N + 1)
    tree_mismatches = []
    for n in range(2, args.N + 1):
        T[n] = 1 if is_prime[n] else len(trees(n))
        if is_prime[n]:
            continue

        ordered = 0
        for a in range(2, n):
            if n % a == 0:
                b = n // a
                if b >= 2:
                    ordered += T[a] * T[b]

        r = math.isqrt(n)
        diagonal = T[r] if r * r == n else 0
        rhs = (ordered + diagonal) // 2
        if T[n] != rhs:
            tree_mismatches.append((n, T[n], rhs))

    print(f"N={args.N}")
    print(f"word_mismatches={len(word_mismatches)}")
    print(f"tree_mismatches={len(tree_mismatches)}")
    if word_mismatches:
        print("first_word_mismatch=", word_mismatches[0])
    if tree_mismatches:
        print("first_tree_mismatch=", tree_mismatches[0])


if __name__ == "__main__":
    main()
