#!/usr/bin/env python3
"""Audit the large-prime late-stage compensation in the Mertens sum.

For X and y=sqrt(X), define

    F_y(X) = sum_{n<=X, squarefree, P+(n)<=y} mu(n).

Because p>sqrt(X) implies X/p<p, the remaining prime tail is exactly

    T(X) = sum_{sqrt(X)<p<=X} M(floor(X/p)),
    M(X) = F_y(X) - T(X).

Grouping q=floor(X/p) gives a natural prime-counting kernel.  The script also
replaces exact prime interval counts with Li interval masses to isolate the
smooth PNT-level common mode.  These approximations are diagnostics, not an RH
argument.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import mpmath as mp
import numpy as np

EULER_GAMMA = 0.5772156649015328606


def tables(N: int):
    is_prime = np.ones(N + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, int(N**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : N + 1 : p] = False
    primes = np.flatnonzero(is_prime).astype(np.int64)

    omega = np.zeros(N + 1, dtype=np.uint8)
    squarefree = np.ones(N + 1, dtype=np.bool_)
    squarefree[0] = False
    pmax = np.zeros(N + 1, dtype=np.int64)
    for p0 in primes:
        p = int(p0)
        omega[p : N + 1 : p] += 1
        pmax[p : N + 1 : p] = p
        if p * p <= N:
            squarefree[p * p : N + 1 : p * p] = False

    mu = np.zeros(N + 1, dtype=np.int8)
    mu[1] = 1
    idx = squarefree & (np.arange(N + 1) >= 1)
    mu[idx] = np.where((omega[idx] % 2) == 0, 1, -1)
    M = np.cumsum(mu, dtype=np.int64)
    return primes, squarefree, pmax, mu, M


def f_sqrt(X, squarefree, pmax, mu):
    y = int(math.isqrt(X))
    mask = squarefree[1 : X + 1] & (pmax[1 : X + 1] <= y)
    return int(mu[1 : X + 1][mask].sum())


def exact_tail(X, primes, M):
    y = int(math.isqrt(X))
    return sum(int(M[X // int(p)]) for p in primes if y < p <= X)


def li_kernel(X, M):
    """PNT/Li replacement for the exact prime interval weights."""
    qmax = int(math.isqrt(X)) - 1
    total = mp.mpf("0")
    for q in range(1, qmax + 1):
        a = mp.mpf(X) / (q + 1)
        b = mp.mpf(X) / q
        total += int(M[q]) * (mp.li(b) - mp.li(a))
    return float(total)


def first_moment_models(X):
    L = math.log(X)
    first = -X / (L * L)
    second = first - 2.0 * (1.0 + EULER_GAMMA) * X / (L**3)
    return first, second


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-power", type=int, default=10)
    ap.add_argument("--max-power", type=int, default=20)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path("data/mertens/late_stage_compensation_dyadic_20.csv"),
    )
    args = ap.parse_args()

    N = 2**args.max_power
    primes, squarefree, pmax, mu, M = tables(N)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "X",
        "M",
        "F_sqrt",
        "prime_tail",
        "identity_error",
        "Li_kernel",
        "F_sqrt_minus_Li_kernel",
        "tail_minus_Li_kernel",
        "minus_X_over_log2X",
        "through_second_moment",
        "tail_minus_second_moment",
    ]

    with args.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for k in range(args.min_power, args.max_power + 1):
            X = 2**k
            Fs = f_sqrt(X, squarefree, pmax, mu)
            tail = exact_tail(X, primes, M)
            li = li_kernel(X, M)
            first, second = first_moment_models(X)
            row = {
                "X": X,
                "M": int(M[X]),
                "F_sqrt": Fs,
                "prime_tail": tail,
                "identity_error": int(M[X]) - (Fs - tail),
                "Li_kernel": li,
                "F_sqrt_minus_Li_kernel": Fs - li,
                "tail_minus_Li_kernel": tail - li,
                "minus_X_over_log2X": first,
                "through_second_moment": second,
                "tail_minus_second_moment": tail - second,
            }
            w.writerow(row)


if __name__ == "__main__":
    main()
