#!/usr/bin/env python3
"""Audit square-shell increments of the Chebyshev event energy.

For I_m=(m^2,(m+1)^2], compute

    L_m = theta((m+1)^2)-theta(m^2)
    Q_m = sum_{p in I_m} (p-c_m) log p
    Delta H_m = L_m (E_m+E_{m+1})/2 - Q_m

where E_m=theta(m^2)-m^2 and c_m=(m^2+(m+1)^2)/2.

The script uses only prime data and math.log.  It is intended as a
finite-range regression/false-control audit, not as evidence for RH.
"""

from __future__ import annotations

import argparse
import math


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def audit(nmax: int) -> None:
    mmax = math.isqrt(nmax)
    if mmax < 3:
        raise ValueError("nmax is too small")

    # Shell m ends at (m+1)^2, so m <= mmax-1.
    block_L = [0.0] * (mmax + 1)
    block_S = [0.0] * (mmax + 1)  # sum p log p in shell

    primes = primes_up_to(nmax)
    for p in primes:
        m = math.isqrt(p - 1)
        if 2 <= m <= mmax - 1 and (m + 1) * (m + 1) <= nmax:
            lp = math.log(p)
            block_L[m] += lp
            block_S[m] += p * lp

    # theta(4)=log 2 + log 3.
    theta_a = math.log(2.0) + math.log(3.0)

    positive = 0
    tested = 0
    max_dh = -math.inf
    max_dh_m = None
    min_dh = math.inf
    min_dh_m = None
    max_norm = -math.inf
    min_norm = math.inf
    max_identity_error = 0.0

    for m in range(2, mmax):
        b = (m + 1) * (m + 1)
        if b > nmax:
            break

        L = block_L[m]
        S = block_S[m]
        theta_b = theta_a + L

        a = m * m
        Ea = theta_a - a
        Eb = theta_b - b
        midpoint = 0.5 * (a + b)
        Q = S - midpoint * L

        dh_direct = 0.5 * (theta_b * theta_b - theta_a * theta_a) - S
        dh_shell = L * 0.5 * (Ea + Eb) - Q
        identity_error = abs(dh_direct - dh_shell)
        max_identity_error = max(max_identity_error, identity_error)

        tested += 1
        if dh_direct > 0:
            positive += 1

        if dh_direct > max_dh:
            max_dh = dh_direct
            max_dh_m = m
        if dh_direct < min_dh:
            min_dh = dh_direct
            min_dh_m = m

        norm = dh_direct / (m * m)
        max_norm = max(max_norm, norm)
        min_norm = min(min_norm, norm)

        theta_a = theta_b

    print(f"nmax={nmax}")
    print(f"complete_shells={tested}")
    print(f"positive_shells={positive}")
    print(f"max_delta_H={max_dh:.12g} at m={max_dh_m}")
    print(f"min_delta_H={min_dh:.12g} at m={min_dh_m}")
    print(f"delta_H_over_m2_range=[{min_norm:.12g}, {max_norm:.12g}]")
    print(f"max_identity_error={max_identity_error:.6g}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--nmax",
        type=int,
        default=5_000_000,
        help="maximum integer to sieve (default: 5,000,000)",
    )
    args = parser.parse_args()
    audit(args.nmax)
