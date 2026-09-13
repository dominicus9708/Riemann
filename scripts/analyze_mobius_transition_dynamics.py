#!/usr/bin/env python3
"""Audit additive transition dynamics of the Möbius function.

The multiplicative prime-activation dynamics is commutative. This script probes
a genuinely ordered direction, n -> n+h, through finite shifted correlations

    C_X(h) = sum_{n<=X-h} mu(n) mu(n+h).

For h=1 consecutive integers have disjoint prime supports. The calculations are
diagnostics only; controlling these correlations uniformly is related to Chowla-
type problems and is not claimed here.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def mobius_table(N: int):
    is_prime = np.ones(N + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, int(N**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : N + 1 : p] = False
    primes = np.flatnonzero(is_prime)

    omega = np.zeros(N + 1, dtype=np.uint8)
    squarefree = np.ones(N + 1, dtype=np.bool_)
    squarefree[0] = False
    for p0 in primes:
        p = int(p0)
        omega[p : N + 1 : p] += 1
        pp = p * p
        if pp <= N:
            squarefree[pp : N + 1 : pp] = False

    mu = np.zeros(N + 1, dtype=np.int8)
    mu[1] = 1
    idx = squarefree & (np.arange(N + 1) >= 1)
    mu[idx] = np.where((omega[idx] % 2) == 0, 1, -1)
    return mu


def shifted_correlation(mu, X: int, h: int):
    a = mu[1 : X - h + 1].astype(np.int64)
    b = mu[1 + h : X + 1].astype(np.int64)
    prod = a * b
    C = int(prod.sum())
    support = int(np.count_nonzero(prod))
    mean = C / support if support else 0.0
    z = C / math.sqrt(support) if support else 0.0
    return C, support, mean, z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-power", type=int, default=20)
    ap.add_argument("--max-shift", type=int, default=64)
    ap.add_argument(
        "--shift-output",
        type=Path,
        default=Path("data/mertens/mobius_shift_correlations_2pow20_h64.csv"),
    )
    ap.add_argument(
        "--dyadic-output",
        type=Path,
        default=Path("data/mertens/mobius_adjacent_correlation_dyadic_20.csv"),
    )
    args = ap.parse_args()

    N = 2**args.max_power
    mu = mobius_table(N)

    args.shift_output.parent.mkdir(parents=True, exist_ok=True)
    with args.shift_output.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["h", "C_X_h", "nonzero_pair_count", "conditional_mean", "C_over_sqrt_support"])
        for h in range(1, args.max_shift + 1):
            C, support, mean, z = shifted_correlation(mu, N, h)
            w.writerow([h, C, support, mean, z])

    with args.dyadic_output.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["X", "C_X_1", "nonzero_pair_count", "conditional_mean", "C_over_sqrt_support"])
        for k in range(10, args.max_power + 1):
            X = 2**k
            C, support, mean, z = shifted_correlation(mu, X, 1)
            w.writerow([X, C, support, mean, z])


if __name__ == "__main__":
    main()
