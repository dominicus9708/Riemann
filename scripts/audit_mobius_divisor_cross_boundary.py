#!/usr/bin/env python3
"""Finite false-control audit for the Möbius–divisor hyperbola split.

Checks the exact decomposition

    T(N) = psi(N)-N+2*gamma = A(N)+C(N)

at K=floor(sqrt(N)), where A is the small-d/high-quotient divisor-kernel
part and C is the large-d/low-quotient Mertens part.

This script reports finite correlations/RMS values only. It makes no RH claim.
"""

from __future__ import annotations

import argparse
import math
from statistics import fmean

GAMMA = 0.577215664901532860606512090082402431


def arithmetic_tables(n: int):
    lp = [0] * (n + 1)
    exponent = [0] * (n + 1)
    tau = [0] * (n + 1)
    mu = [0] * (n + 1)
    primes = []

    tau[1] = 1
    mu[1] = 1

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            exponent[i] = 1
            tau[i] = 2
            mu[i] = -1
            primes.append(i)

        for p in primes:
            v = i * p
            if v > n or p > lp[i]:
                break
            lp[v] = p
            if p == lp[i]:
                exponent[v] = exponent[i] + 1
                tau[v] = tau[i] // (exponent[i] + 1) * (exponent[i] + 2)
                mu[v] = 0
            else:
                exponent[v] = 1
                tau[v] = tau[i] * 2
                mu[v] = -mu[i]

    return mu, tau, primes


def build_prefixes(n: int, mu, tau, primes):
    M = [0] * (n + 1)
    b = [0.0] * (n + 1)
    B = [0.0] * (n + 1)

    for i in range(1, n + 1):
        M[i] = M[i - 1] + mu[i]
        b[i] = math.log(i) - tau[i] + 2.0 * GAMMA
        B[i] = B[i - 1] + b[i]

    lam = [0.0] * (n + 1)
    for p in primes:
        lp = math.log(p)
        pk = p
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

    return M, b, B, psi


def hyperbola_parts(N: int, mu, M, b, B, psi):
    K = math.isqrt(N)
    Q = N // (K + 1)

    A = 0.0
    for d in range(1, K + 1):
        A += mu[d] * B[N // d]

    C = 0.0
    for q in range(1, Q + 1):
        C += b[q] * M[N // q]
    C -= M[K] * B[Q]

    T = A + C
    direct = psi[N] - N + 2.0 * GAMMA
    return A, C, T, direct


def pearson(x, y):
    mx = fmean(x)
    my = fmean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = math.sqrt(sum((a - mx) ** 2 for a in x))
    dy = math.sqrt(sum((b - my) ** 2 for b in y))
    return num / (dx * dy) if dx and dy else float("nan")


def rms(x):
    return math.sqrt(fmean(v * v for v in x))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-n", type=int, default=1_000_000)
    ap.add_argument("--start", type=int, default=10_000)
    ap.add_argument("--step", type=int, default=1_000)
    args = ap.parse_args()

    mu, tau, primes = arithmetic_tables(args.max_n)
    M, b, B, psi = build_prefixes(args.max_n, mu, tau, primes)

    Ns = []
    As = []
    Cs = []
    Ts = []
    max_identity_error = 0.0

    for N in range(args.start, args.max_n + 1, args.step):
        A, C, T, direct = hyperbola_parts(N, mu, M, b, B, psi)
        Ns.append(N)
        As.append(A)
        Cs.append(C)
        Ts.append(T)
        max_identity_error = max(max_identity_error, abs(T - direct))

    As_sqrt = [a / math.sqrt(n) for a, n in zip(As, Ns)]
    Cs_sqrt = [c / math.sqrt(n) for c, n in zip(Cs, Ns)]
    Ts_sqrt = [t / math.sqrt(n) for t, n in zip(Ts, Ns)]

    print(f"samples={len(Ns)} range=[{Ns[0]},{Ns[-1]}] step={args.step}")
    print(f"max_identity_error={max_identity_error:.6e}")
    print(f"corr_A_C={pearson(As, Cs):.6f}")
    print(f"corr_A_T={pearson(As, Ts):.6f}")
    print(f"corr_C_T={pearson(Cs, Ts):.6f}")
    print(f"rms_A={rms(As):.6f}")
    print(f"rms_C={rms(Cs):.6f}")
    print(f"rms_T={rms(Ts):.6f}")
    print(f"corr_A_C_sqrt_norm={pearson(As_sqrt, Cs_sqrt):.6f}")
    print(f"corr_C_T_sqrt_norm={pearson(Cs_sqrt, Ts_sqrt):.6f}")
    print(f"rms_A_sqrt_norm={rms(As_sqrt):.6f}")
    print(f"rms_C_sqrt_norm={rms(Cs_sqrt):.6f}")
    print(f"rms_T_sqrt_norm={rms(Ts_sqrt):.6f}")


if __name__ == "__main__":
    main()
