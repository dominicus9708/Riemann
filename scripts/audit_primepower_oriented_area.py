#!/usr/bin/env python3
"""Regression audit for the square-endpoint prime-power oriented-area identity.

Computes

    Theta_m = theta(m^2)
    P_m     = psi(m^2)-theta(m^2)
    A_m     = (Theta_{m+1}-Theta_m)(P_m+P_{m+1})/2
    W_m     = Theta_{m+1} P_m - Theta_m P_{m+1}

and verifies exactly (up to floating arithmetic)

    A_m = [Theta_{m+1}P_{m+1}-Theta_mP_m]/2 + W_m/2.

The asymptotic targets are cumulative A / M^3 -> 2/3,
cumulative W / M^3 -> 1/3, and Theta_M P_M / M^3 -> 1.
This is a numerical regression audit, not evidence for RH.
"""

from __future__ import annotations

import argparse
import math


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def integer_kth_root(n: int, k: int) -> int:
    r = int(round(n ** (1.0 / k)))
    while (r + 1) ** k <= n:
        r += 1
    while r ** k > n:
        r -= 1
    return r


def audit(nmax: int, checkpoints: list[int]) -> None:
    mmax = math.isqrt(nmax)
    primes = primes_up_to(nmax)

    log_prime = [0.0] * (nmax + 1)
    for p in primes:
        log_prime[p] = math.log(p)

    theta = [0.0] * (nmax + 1)
    run = 0.0
    for n in range(nmax + 1):
        run += log_prime[n]
        theta[n] = run

    def theta_at(x: int) -> float:
        return theta[x]

    def primepower_tail(x: int) -> float:
        total = 0.0
        k = 2
        while (1 << k) <= x:
            total += theta_at(integer_kth_root(x, k))
            k += 1
        return total

    Theta = [0.0] * (mmax + 1)
    P = [0.0] * (mmax + 1)
    for m in range(1, mmax + 1):
        x = m * m
        Theta[m] = theta_at(x)
        P[m] = primepower_tail(x)

    cumulative_A = 0.0
    cumulative_W = 0.0
    positive_W = 0
    negative_W = 0
    zero_W = 0
    max_identity_error = 0.0

    checkpoint_set = {m for m in checkpoints if 2 <= m <= mmax}
    reported: dict[int, tuple[float, float, float]] = {}

    for m in range(1, mmax):
        L = Theta[m + 1] - Theta[m]
        A = L * (P[m] + P[m + 1]) / 2.0
        W = Theta[m + 1] * P[m] - Theta[m] * P[m + 1]
        boundary_change = Theta[m + 1] * P[m + 1] - Theta[m] * P[m]

        max_identity_error = max(
            max_identity_error,
            abs(A - 0.5 * (boundary_change + W)),
        )

        cumulative_A += A
        cumulative_W += W

        if m >= 2:
            if W > 0:
                positive_W += 1
            elif W < 0:
                negative_W += 1
            else:
                zero_W += 1

        M = m + 1
        if M in checkpoint_set:
            reported[M] = (
                cumulative_A / (M**3),
                cumulative_W / (M**3),
                Theta[M] * P[M] / (M**3),
            )

    print(f"nmax={nmax}")
    print(f"mmax={mmax}")
    print(f"positive_W_shells_m_ge_2={positive_W}")
    print(f"negative_W_shells_m_ge_2={negative_W}")
    print(f"zero_W_shells_m_ge_2={zero_W}")
    print(f"max_identity_error={max_identity_error:.6g}")
    print("targets: A/M^3 -> 2/3, W/M^3 -> 1/3, boundary/M^3 -> 1")

    for M in sorted(reported):
        a, w, b = reported[M]
        print(
            f"M={M}: reserve/M^3={a:.12g}, "
            f"W/M^3={w:.12g}, boundary/M^3={b:.12g}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=5_000_000)
    parser.add_argument(
        "--checkpoints",
        type=str,
        default="500,1000,1500,2000,2236",
        help="comma-separated M values",
    )
    args = parser.parse_args()
    cps = [int(x) for x in args.checkpoints.split(",") if x.strip()]
    audit(args.nmax, cps)
