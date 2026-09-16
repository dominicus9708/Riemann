#!/usr/bin/env python3
"""Reproduce the exact Möbius–divisor-error bridge diagnostics.

No RH claim is made. The script checks

    psi(N)-N = -2*gamma + sum_{d<=N} mu(d) B(floor(N/d)),

where

    B(q)=log(q!)-sum_{n<=q} tau(n)+2*gamma*q
        =S(q)-Delta(q).

It also separates the Stirling-lattice and divisor-error transforms.
"""

from __future__ import annotations

import argparse
import math


def mobius_and_primes(n: int):
    lp = [0] * (n + 1)
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
            else:
                mu[i * p] = -mu[i]
    return mu, primes


def divisor_counts(n: int):
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    return tau


def von_mangoldt_prefix(n: int, primes):
    lam = [0.0] * (n + 1)
    for p in primes:
        pk = p
        lp = math.log(p)
        while pk <= n:
            lam[pk] = lp
            if pk > n // p:
                break
            pk *= p
    psi = [0.0] * (n + 1)
    s = 0.0
    for i in range(1, n + 1):
        s += lam[i]
        psi[i] = s
    return psi


def build_kernels(n: int, tau):
    gamma = 0.577215664901532860606512090082402431
    D = [0] * (n + 1)
    B = [0.0] * (n + 1)
    S = [0.0] * (n + 1)
    Delta = [0.0] * (n + 1)

    dsum = 0
    logfact = 0.0
    for y in range(1, n + 1):
        dsum += tau[y]
        logfact += math.log(y)
        D[y] = dsum
        S[y] = logfact - y * math.log(y) + y
        Delta[y] = dsum - y * math.log(y) - (2 * gamma - 1) * y
        B[y] = logfact - dsum + 2 * gamma * y

    return gamma, B, S, Delta


def bridge_at(N, mu, psi, gamma, B, S, Delta):
    total = 0.0
    cs = 0.0
    cd = 0.0
    abs_total = 0.0
    for d in range(1, N + 1):
        if mu[d] == 0:
            continue
        q = N // d
        total += mu[d] * B[q]
        cs += mu[d] * S[q]
        cd += mu[d] * Delta[q]
        abs_total += abs(B[q])

    reconstructed = -2 * gamma + total
    direct = psi[N] - N
    return {
        "N": N,
        "direct_prime_error": direct,
        "bridge_prime_error": reconstructed,
        "bridge_abs_error": abs(direct - reconstructed),
        "C_S": cs,
        "C_Delta": cd,
        "identity_difference": -2 * gamma + cs - cd,
        "absolute_mass": abs_total,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=120000)
    ap.add_argument("--step", type=int, default=1000)
    args = ap.parse_args()

    n = args.N
    mu, primes = mobius_and_primes(n)
    tau = divisor_counts(n)
    psi = von_mangoldt_prefix(n, primes)
    gamma, B, S, Delta = build_kernels(n, tau)

    max_err = 0.0
    rows = []
    for N in range(args.step, n + 1, args.step):
        row = bridge_at(N, mu, psi, gamma, B, S, Delta)
        rows.append(row)
        max_err = max(max_err, row["bridge_abs_error"])

    print(f"tested={len(rows)} max_N={n} max_identity_error={max_err:.3e}")
    print("N,direct,bridge,C_S,C_Delta,absolute_mass")
    for row in rows[-10:]:
        print(
            f'{row["N"]},'
            f'{row["direct_prime_error"]:.12g},'
            f'{row["bridge_prime_error"]:.12g},'
            f'{row["C_S"]:.12g},'
            f'{row["C_Delta"]:.12g},'
            f'{row["absolute_mass"]:.12g}'
        )


if __name__ == "__main__":
    main()
