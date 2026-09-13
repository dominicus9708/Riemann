#!/usr/bin/env python3
"""Audit local derivative energies of the squarefree formation polynomial at the Möbius corner.

Definitions
-----------
P_X(z) = sum_{n<=X, mu(n)^2=1} prod_{p|n} z_p.
For squarefree a = prod_{p in A} p,
    partial_A P_X(-1) = sum_{r<=X/a, (r,a)=1} mu(r).

The k-th local derivative energy is
    E_mu(k;X) = sum_{a<=X, sf, omega(a)=k} |D_a(X/a)|^2.
The random-character ensemble mean is exactly
    E_avg(k;X) = sum_{n<=X} mu(n)^2 * C(omega(n), k).

This script reproduces the dyadic audit stored in
    data/formation/mobius_corner_derivative_energy_2pow14_20.csv
"""

from __future__ import annotations

import argparse
import csv
import math
from functools import lru_cache

import numpy as np


def sieve_mu_omega_spf(n: int):
    is_prime = np.ones(n + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = False
    primes = np.flatnonzero(is_prime)

    mu = np.ones(n + 1, dtype=np.int8)
    mu[0] = 0
    omega = np.zeros(n + 1, dtype=np.uint8)
    spf = np.zeros(n + 1, dtype=np.int32)

    for p0 in primes:
        p = int(p0)
        mu[p : n + 1 : p] *= -1
        omega[p : n + 1 : p] += 1
        pp = p * p
        if pp <= n:
            mu[pp : n + 1 : pp] = 0

        sl = spf[p : n + 1 : p]
        mask = sl == 0
        sl[mask] = p
        spf[p : n + 1 : p] = sl

    M = np.cumsum(mu, dtype=np.int64)
    Q = np.cumsum(mu.astype(np.int16) ** 2, dtype=np.int64)
    return primes, mu, omega, spf, M, Q


def factor_squarefree(a: int, spf: np.ndarray) -> tuple[int, ...]:
    out: list[int] = []
    while a > 1:
        p = int(spf[a])
        out.append(p)
        a //= p
    return tuple(out)


def comb_array(omega: np.ndarray, k: int) -> np.ndarray:
    w = omega.astype(np.int64)
    if k == 0:
        return np.ones_like(w)
    out = np.ones_like(w)
    for j in range(k):
        out = out * (w - j) // (j + 1)
    out[w < k] = 0
    return out


def audit(max_power: int):
    nmax = 2**max_power
    primes, mu, omega, spf, M, Q = sieve_mu_omega_spf(nmax)

    @lru_cache(maxsize=None)
    def D(A: tuple[int, ...], y: int) -> int:
        """D_A(y)=sum_{r<=y,(r,prod A)=1} mu(r), exact recursion."""
        if y < 1:
            return 0
        if not A:
            return int(M[y])

        total = int(M[y])
        k = len(A)
        for mask in range(1, 1 << k):
            prod = 1
            subset: list[int] = []
            for i, p in enumerate(A):
                if (mask >> i) & 1:
                    prod *= p
                    subset.append(p)
            yy = y // prod
            if yy:
                total += D(tuple(subset), yy)
        return total

    rows: list[dict[str, object]] = []
    for power in range(14, max_power + 1):
        X = 2**power
        max_k = 7 if power == max_power else 4

        for k in range(max_k + 1):
            if k == 0:
                e_mu = int(M[X]) ** 2
            else:
                candidates = np.flatnonzero(
                    (omega[: X + 1] == k) & (mu[: X + 1] != 0)
                )
                e_mu = 0
                for a0 in candidates:
                    a = int(a0)
                    A = factor_squarefree(a, spf)
                    v = D(A, X // a)
                    e_mu += v * v

            sf = mu[: X + 1] != 0
            e_avg = int(np.sum(sf * comb_array(omega[: X + 1], k)))
            ratio = e_mu / e_avg if e_avg else float("nan")
            rows.append(
                {
                    "X": X,
                    "k": k,
                    "E_mu": e_mu,
                    "E_avg": e_avg,
                    "ratio": ratio,
                }
            )

    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-power", type=int, default=20)
    ap.add_argument("--out", default="mobius_corner_derivative_energy.csv")
    args = ap.parse_args()

    rows = audit(args.max_power)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["X", "k", "E_mu", "E_avg", "ratio"])
        w.writeheader()
        w.writerows(rows)

    for row in rows:
        print(
            f"X={row['X']:>8} k={row['k']} "
            f"E_mu={row['E_mu']:>10} E_avg={row['E_avg']:>10} "
            f"ratio={row['ratio']:.12g}"
        )


if __name__ == "__main__":
    main()
