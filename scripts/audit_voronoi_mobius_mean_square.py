#!/usr/bin/env python3
"""Finite diagnostic for the Voronoi–Möbius reciprocal phase.

Computes
    V_n(K) = sum_{d<=K} c_d d^{-1/4} exp(2*pi*i*2*K*sqrt(n/d))
for Möbius, all-positive, squarefree-positive, and optional random-sign controls.

This is a numerical audit only; it is not evidence for RH.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def mobius_sieve(N: int) -> np.ndarray:
    mu = np.ones(N + 1, dtype=np.int8)
    isprime = np.ones(N + 1, dtype=bool)
    isprime[:2] = False
    for p in range(2, N + 1):
        if isprime[p]:
            mu[p::p] *= -1
            pp = p * p
            if pp <= N:
                mu[pp::pp] = 0
            isprime[p * 2 :: p] = False
    mu[0] = 0
    return mu


def coefficient_matrix(K: int, random_controls: int, seed: int):
    mu = mobius_sieve(K)
    d = np.arange(1, K + 1, dtype=float)
    w = d ** (-0.25)
    cols = [
        ("mobius", mu[1:].astype(float) * w),
        ("positive", w.copy()),
        ("squarefree_positive", (mu[1:] != 0).astype(float) * w),
    ]
    if random_controls:
        rng = np.random.default_rng(seed)
        for j in range(random_controls):
            eps = rng.choice([-1.0, 1.0], size=K)
            cols.append((f"rademacher_{j+1}", eps * w))
    names = [x[0] for x in cols]
    matrix = np.column_stack([x[1] for x in cols])
    return names, matrix


def audit(K: int, chunk: int, random_controls: int, seed: int):
    names, coeff = coefficient_matrix(K, random_controls, seed)
    d = np.arange(1, K + 1, dtype=float)
    factor = 2.0 * K / np.sqrt(d)

    count_bands = int(math.floor(math.log2(K))) + 1
    band_count = np.zeros(count_bands, dtype=int)
    band_sumsq = np.zeros((count_bands, len(names)), dtype=float)
    max_abs = np.zeros(len(names), dtype=float)
    values_for_quantiles = [[] for _ in names]

    for start in range(1, K + 1, chunk):
        stop = min(start + chunk, K + 1)
        ns = np.arange(start, stop, dtype=float)
        phase = 2j * np.pi * (np.sqrt(ns)[:, None] * factor[None, :])
        Z = np.abs(np.exp(phase) @ coeff)
        max_abs = np.maximum(max_abs, Z.max(axis=0))
        for j in range(len(names)):
            values_for_quantiles[j].extend(Z[:, j].tolist())
        for row, n in enumerate(range(start, stop)):
            b = min(int(math.floor(math.log2(n))), count_bands - 1)
            band_count[b] += 1
            band_sumsq[b] += Z[row] ** 2

    scale = K ** 0.25
    print(f"K={K}, X={K*K}, scale K^(1/4)={scale:.8g}")
    for j, name in enumerate(names):
        vals = np.asarray(values_for_quantiles[j]) / scale
        print(
            f"{name:24s} max={max_abs[j]/scale:.6f} "
            f"median={np.median(vals):.6f} p95={np.quantile(vals, 0.95):.6f}"
        )

    print("\nDyadic mean-square ratios: sum |V_n|^2 / (#band * K^(1/2))")
    denom_scale = K ** 0.5
    for b in range(count_bands):
        lo = 2**b
        hi = min(2 ** (b + 1) - 1, K)
        if band_count[b] == 0:
            continue
        ratios = band_sumsq[b] / (band_count[b] * denom_scale)
        items = " ".join(f"{names[j]}={ratios[j]:.6f}" for j in range(len(names)))
        print(f"[{lo:6d},{hi:6d}] {items}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, default=10000)
    ap.add_argument("--chunk", type=int, default=100)
    ap.add_argument("--random-controls", type=int, default=8)
    ap.add_argument("--seed", type=int, default=12345)
    args = ap.parse_args()
    audit(args.K, args.chunk, args.random_controls, args.seed)
