#!/usr/bin/env python3
"""Unbiased sigma-emergence audit for formation observables.

The script does not privilege sigma=1/2.  It compares dyadic-shell complex
profiles after subtracting the same-sigma unstructured baseline f(n)=1.

Dependencies: numpy.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def smallest_prime_factor_sieve(N: int) -> np.ndarray:
    spf = np.arange(N + 1, dtype=np.int64)
    spf[0] = 0
    if N >= 1:
        spf[1] = 1
    for p in range(2, int(math.isqrt(N)) + 1):
        if spf[p] == p:
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def arithmetic_observables(N: int):
    spf = smallest_prime_factor_sieve(N)
    omega = np.zeros(N + 1, dtype=np.int16)
    Omega = np.zeros(N + 1, dtype=np.int16)
    W = np.zeros(N + 1, dtype=np.int64)
    W[1] = 1

    for n in range(2, N + 1):
        p = int(spf[n])
        m = n // p
        Omega[n] = Omega[m] + 1
        omega[n] = omega[m] + (1 if m % p else 0)

        x = n
        total = 0
        last = 0
        while x > 1:
            q = int(spf[x])
            if q != last:
                total += int(W[n // q])
                last = q
            while x % q == 0:
                x //= q
        W[n] = total

    # composite-only nontrivial formation words
    for n in range(2, N + 1):
        if spf[n] == n:
            W[n] = 0

    return {"omega": omega, "Omega": Omega, "W": W}


def residual_profiles(values, sigmas, t_values, ks):
    shell_cache = []
    for k in ks:
        hi = 2**k
        lo = 2 ** (k - 1) + 1
        n = np.arange(lo, hi + 1, dtype=float)
        f = values[lo : hi + 1].astype(float)
        xlog = np.log(n / hi)
        phase = np.exp(-1j * np.outer(t_values, xlog))
        shell_cache.append((n, f, phase))

    result = {}
    for sigma in sigmas:
        rows = []
        for n, f, phase in shell_cache:
            base_w = n ** (-sigma)
            H0 = (phase @ base_w) / base_w.sum()
            f_w = f * base_w
            Hf = (phase @ f_w) / f_w.sum()
            rows.append(Hf - H0)
        result[float(sigma)] = np.asarray(rows)
    return result


def stability_score(profile: np.ndarray) -> float:
    diffs = np.sqrt(np.mean(np.abs(profile[1:] - profile[:-1]) ** 2, axis=1))
    scales = np.sqrt(np.mean(np.abs(profile[:-1]) ** 2, axis=1))
    rel = diffs / np.maximum(scales, 1e-15)
    return float(rel.mean())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=524288)
    ap.add_argument("--min-k", type=int, default=10)
    ap.add_argument("--max-k", type=int, default=19)
    ap.add_argument("--sigma-min", type=float, default=0.20)
    ap.add_argument("--sigma-max", type=float, default=0.90)
    ap.add_argument("--sigma-step", type=float, default=0.05)
    ap.add_argument("--t-min", type=float, default=5.0)
    ap.add_argument("--t-max", type=float, default=50.0)
    ap.add_argument("--t-step", type=float, default=2.0)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path("data/formation/sigma_emergence_shell_reproduction.csv"),
    )
    args = ap.parse_args()

    if 2 ** args.max_k > args.N:
        raise SystemExit("N must be at least 2^max_k")

    observables = arithmetic_observables(args.N)
    sigmas = np.arange(
        args.sigma_min,
        args.sigma_max + 0.5 * args.sigma_step,
        args.sigma_step,
    )
    t_values = np.arange(
        args.t_min,
        args.t_max + 0.5 * args.t_step,
        args.t_step,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["observable", "max_N", "best_sigma", "score"],
        )
        writer.writeheader()

        for name, values in observables.items():
            for max_k in range(max(args.min_k + 1, 14), args.max_k + 1):
                start_k = max(args.min_k, max_k - 5)
                ks = list(range(start_k, max_k + 1))
                profiles = residual_profiles(values, sigmas, t_values, ks)
                scores = [(sigma, stability_score(P)) for sigma, P in profiles.items()]
                best_sigma, best_score = min(scores, key=lambda row: row[1])
                writer.writerow(
                    {
                        "observable": name,
                        "max_N": 2**max_k,
                        "best_sigma": f"{best_sigma:.6f}",
                        "score": f"{best_score:.12f}",
                    }
                )


if __name__ == "__main__":
    main()
