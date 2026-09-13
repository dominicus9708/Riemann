#!/usr/bin/env python3
"""Blind complex-growth audit for the Möbius formation sign.

The estimator never inserts sigma=1/2. It measures the growth exponent of
complex dyadic-shell sums of mu(n), then compares with random-sign controls on
the same squarefree support.

Dependencies: numpy.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def mobius_sieve(N: int) -> np.ndarray:
    prime = np.ones(N + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if prime[p]:
            prime[p * p : N + 1 : p] = False

    primes = np.flatnonzero(prime)
    mu = np.ones(N + 1, dtype=np.int8)
    mu[0] = 0
    for p in primes:
        mu[p::p] *= -1
        pp = int(p) * int(p)
        if pp <= N:
            mu[pp::pp] = 0
    return mu


def shell_rms(sequence, t_values, kmin, kmax):
    rows = []
    for k in range(kmin, kmax + 1):
        lo = 2**k + 1
        hi = 2 ** (k + 1)
        n = np.arange(lo, hi + 1, dtype=float)
        values = sequence[lo : hi + 1].astype(float)
        logx = np.log(n / (2**k))
        amps = []
        for t in t_values:
            z = np.sum(values * np.exp(-1j * t * logx))
            amps.append(abs(z))
        rms = math.sqrt(float(np.mean(np.square(amps))))
        rows.append((k, hi, rms))
    return rows


def slope(rows, last_n):
    subset = rows[-last_n:]
    x = np.asarray([k for k, _, _ in subset], dtype=float)
    y = np.log2([rms for _, _, rms in subset])
    return float(np.polyfit(x, y, 1)[0])


def random_on_support(mu, seed):
    rng = np.random.default_rng(seed)
    out = np.zeros_like(mu)
    idx = np.flatnonzero(mu != 0)
    out[idx] = rng.choice(np.array([-1, 1], dtype=np.int8), size=len(idx))
    if len(out) > 1:
        out[1] = 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=5_000_000)
    ap.add_argument("--kmin", type=int, default=12)
    ap.add_argument("--kmax", type=int, default=21)
    ap.add_argument("--t-min", type=float, default=5.0)
    ap.add_argument("--t-max", type=float, default=50.0)
    ap.add_argument("--t-step", type=float, default=5.0)
    ap.add_argument("--fit-shells", type=int, default=8)
    ap.add_argument("--seeds", default="1,2,3,4,5,10,20,30,40,50")
    ap.add_argument(
        "--output",
        type=Path,
        default=Path("data/formation/mobius_blind_sigma_reproduction.csv"),
    )
    args = ap.parse_args()

    if 2 ** (args.kmax + 1) > args.N:
        raise SystemExit("N must contain the largest requested dyadic shell")

    t_values = np.arange(
        args.t_min,
        args.t_max + 0.5 * args.t_step,
        args.t_step,
    )
    mu = mobius_sieve(args.N)

    rows_out = []
    mu_rows = shell_rms(mu, t_values, args.kmin, args.kmax)
    rows_out.append(("mobius", "actual", slope(mu_rows, args.fit_shells)))

    abs_rows = shell_rms(np.abs(mu), t_values, args.kmin, args.kmax)
    rows_out.append(("positive_control", "abs_mu", slope(abs_rows, args.fit_shells)))

    seeds = [int(x) for x in args.seeds.split(",") if x.strip()]
    random_values = []
    for seed in seeds:
        rand = random_on_support(mu, seed)
        rand_rows = shell_rms(rand, t_values, args.kmin, args.kmax)
        beta = slope(rand_rows, args.fit_shells)
        random_values.append(beta)
        rows_out.append(("random_control", str(seed), beta))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["kind", "id", "blind_beta"])
        for kind, ident, beta in rows_out:
            writer.writerow([kind, ident, f"{beta:.12f}"])
        writer.writerow([
            "random_control_summary",
            "mean",
            f"{float(np.mean(random_values)):.12f}",
        ])
        writer.writerow([
            "random_control_summary",
            "std",
            f"{float(np.std(random_values)):.12f}",
        ])


if __name__ == "__main__":
    main()
