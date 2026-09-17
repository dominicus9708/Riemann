#!/usr/bin/env python3
"""Finite false-control audit for the Voronoi–Mobius reciprocal phase.

Computes
    V_a(n,K) = sum_{d<=K} a_d d^(-1/4) exp(2*pi*i*2*K*sqrt(n/d))
for Mobius, squarefree-random, and all-positive coefficient systems.

This is a numerical diagnostic only; it does not prove asymptotic bounds.
"""

import argparse
import math
import numpy as np


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.zeros(n + 1, dtype=np.int8)
    lp = np.zeros(n + 1, dtype=np.int32)
    primes = []
    mu[1] = 1
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
    return mu


def coefficient_vector(k: int, kind: str, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if kind == "mobius":
        return mobius_sieve(k)[1:].astype(float)
    if kind == "ones":
        return np.ones(k, dtype=float)
    if kind == "squarefree-random":
        mu = mobius_sieve(k)[1:]
        return (mu != 0).astype(float) * rng.choice([-1.0, 1.0], size=k)
    raise ValueError(kind)


def sample_n(k: int, count: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    pieces = [
        np.arange(1, min(k, 100) + 1),
        np.round(np.geomspace(1, k, min(300, k))).astype(int),
        rng.integers(1, k + 1, size=min(count, k)),
    ]
    return np.unique(np.concatenate(pieces))


def audit(k: int, kind: str, ncount: int, seed: int):
    d = np.arange(1, k + 1, dtype=float)
    coeff = coefficient_vector(k, kind, seed) * d ** (-0.25)
    ns = sample_n(k, ncount, seed)
    vals = []
    for start in range(0, len(ns), 64):
        nb = ns[start : start + 64].astype(float)
        phase = 4.0 * np.pi * k * np.sqrt(nb[:, None] / d[None, :])
        block = np.exp(1j * phase).dot(coeff)
        vals.extend(np.abs(block).tolist())
    vals = np.asarray(vals)
    scale = k ** 0.25
    return {
        "K": k,
        "kind": kind,
        "samples": len(ns),
        "max": float(vals.max()),
        "mean": float(vals.mean()),
        "rms": float(np.sqrt(np.mean(vals ** 2))),
        "max_over_K14": float(vals.max() / scale),
        "mean_over_K14": float(vals.mean() / scale),
        "rms_over_K14": float(np.sqrt(np.mean(vals ** 2)) / scale),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, nargs="+", default=[1000, 5000, 10000, 20000, 50000])
    ap.add_argument("--ncount", type=int, default=500)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    for k in args.K:
        for kind in ("mobius", "squarefree-random", "ones"):
            print(audit(k, kind, args.ncount, args.seed))


if __name__ == "__main__":
    main()
