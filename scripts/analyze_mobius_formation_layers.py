#!/usr/bin/env python3
"""Analyze squarefree formation layers A_k(x) and Möbius cancellation.

For
    A_k(x) = #{n <= x : mu(n)^2 = 1 and omega(n) = k},
we have
    M(x) = sum_k (-1)^k A_k(x).

The script computes dyadic layer counts, parity balance, simple null models,
the finite layer polynomial G_x(z)=sum_k A_k(x) z^k, and selected checks of
the exact inter-layer recurrence

    (k+1) A_{k+1}(x)
      = sum_p sum_{j=0}^k (-1)^j
          A_{k-j}( floor(x / p^(j+1)) ).

NumPy is used for the sieve because the default range reaches 2^24.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def build_tables(N: int):
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
    idx = squarefree
    mu[idx] = np.where((omega[idx] % 2) == 0, 1, -1)
    mu[0] = 0
    M = np.cumsum(mu, dtype=np.int64)
    return primes, omega, squarefree, mu, M


def layer_counts(omega, squarefree, X: int, width: int):
    vals = omega[1 : X + 1][squarefree[1 : X + 1]]
    return np.bincount(vals, minlength=width).astype(np.int64)


def count_A(omega, squarefree, X: int, k: int) -> int:
    if X < 1:
        return 0
    return int(np.count_nonzero(squarefree[1 : X + 1] & (omega[1 : X + 1] == k)))


def recurrence_rhs(primes, omega, squarefree, X: int, k: int) -> int:
    total = 0
    for p0 in primes:
        p = int(p0)
        if p > X:
            break
        q = p
        for j in range(k + 1):
            if q > X:
                break
            total += ((-1) ** j) * count_A(omega, squarefree, X // q, k - j)
            if q > X // p:
                break
            q *= p
    return total


def write_outputs(args, primes, omega, squarefree, M):
    max_k = int(omega.max())
    args.layers.parent.mkdir(parents=True, exist_ok=True)

    layer_rows = []
    summary_rows = []
    pair_rows = []

    for K in range(args.min_power, args.max_power + 1):
        X = 2**K
        A = layer_counts(omega, squarefree, X, max_k + 1)
        Q = int(A.sum())
        even = int(A[::2].sum())
        odd = int(A[1::2].sum())
        m = int(M[X])

        ks = np.arange(len(A), dtype=np.float64)
        mean_k = float(np.dot(ks, A) / Q)
        var_k = float(np.dot((ks - mean_k) ** 2, A) / Q)
        poisson_null = Q * math.exp(-2.0 * mean_k)

        psel = primes[primes <= X].astype(np.float64)
        log_ind = float(np.log((psel - 1.0) / (psel + 1.0)).sum())
        independent_null = Q * math.exp(log_ind)

        coeff = A.astype(np.float64)
        nonzero = np.flatnonzero(coeff)
        poly = coeff[: nonzero[-1] + 1]
        roots = np.roots(poly[::-1]) if len(poly) > 1 else np.array([], dtype=np.complex128)
        if len(roots):
            root = min(roots, key=lambda z: abs(z + 1.0))
            root_re = float(root.real)
            root_dist = float(abs(root + 1.0))
        else:
            root_re = float("nan")
            root_dist = float("nan")

        gp = sum(k * int(A[k]) * ((-1) ** (k - 1)) for k in range(1, len(A)))

        layer_rows.append((X, m, Q, even, odd, A.copy()))
        summary_rows.append(
            (
                X,
                m,
                Q,
                m / math.sqrt(Q),
                mean_k,
                var_k,
                poisson_null,
                independent_null,
                gp,
                root_re,
                root_dist,
            )
        )

        D = []
        for j in range((max_k + 2) // 2):
            a = int(A[2 * j]) if 2 * j < len(A) else 0
            b = int(A[2 * j + 1]) if 2 * j + 1 < len(A) else 0
            D.append(a - b)
        pair_rows.append((X, m, D))

    with args.layers.open("w", newline="", encoding="utf-8") as f:
        fields = ["X", "M", "Q_squarefree", "even_layers", "odd_layers"] + [
            f"A{k}" for k in range(max_k + 1)
        ]
        w = csv.writer(f)
        w.writerow(fields)
        for X, m, Q, even, odd, A in layer_rows:
            w.writerow([X, m, Q, even, odd] + [int(v) for v in A])

    with args.summary.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "X",
                "M",
                "Q_squarefree",
                "M_over_sqrtQ",
                "mean_k",
                "var_k",
                "poisson_parity_null",
                "independent_channel_parity_null",
                "Gprime_minus1",
                "root_near_minus1_real",
                "root_distance",
            ]
        )
        for row in summary_rows:
            w.writerow(row)

    with args.pairs.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        pair_names = [f"D{j}_A{2*j}_minus_A{2*j+1}" for j in range((max_k + 2) // 2)]
        w.writerow(["X", "M"] + pair_names)
        for X, m, D in pair_rows:
            w.writerow([X, m] + D)


def verify_recurrence(args, primes, omega, squarefree):
    args.recurrence.parent.mkdir(parents=True, exist_ok=True)
    with args.recurrence.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["X", "k", "lhs_kplus1_Akplus1", "rhs_prime_channel_recurrence", "difference"])
        for X in args.check_x:
            max_k = int(omega[: X + 1].max())
            for k in range(max_k):
                lhs = (k + 1) * count_A(omega, squarefree, X, k + 1)
                rhs = recurrence_rhs(primes, omega, squarefree, X, k)
                w.writerow([X, k, lhs, rhs, lhs - rhs])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-power", type=int, default=10)
    ap.add_argument("--max-power", type=int, default=24)
    ap.add_argument("--check-x", type=int, nargs="*", default=[100, 500, 1000, 5000, 10000])
    ap.add_argument("--layers", type=Path, default=Path("data/formation/mobius_layer_counts_dyadic_24.csv"))
    ap.add_argument("--summary", type=Path, default=Path("data/formation/mobius_layer_summary_dyadic_24.csv"))
    ap.add_argument("--pairs", type=Path, default=Path("data/formation/mobius_layer_pair_balance_dyadic_24.csv"))
    ap.add_argument("--recurrence", type=Path, default=Path("data/formation/mobius_layer_recurrence_audit.csv"))
    args = ap.parse_args()

    N = 2 ** args.max_power
    primes, omega, squarefree, mu, M = build_tables(N)
    write_outputs(args, primes, omega, squarefree, M)
    verify_recurrence(args, primes, omega, squarefree)


if __name__ == "__main__":
    main()
