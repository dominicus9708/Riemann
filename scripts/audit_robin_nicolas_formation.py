#!/usr/bin/env python3
"""Numerical audit for the Robin--Nicolas formation complement.

This script is a diagnostic companion to
04_prime_connection/robin_nicolas_formation_duality.md.

It constructs a colossally-abundant threshold state from prime-power marginal
slopes, then verifies the exact matched identity

    G_R + G_N = (P-A) + log(log t / log theta(x)).

This is not a proof of RH.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np

EULER_GAMMA = 0.5772156649015328606


def primes_upto(n: int) -> np.ndarray:
    a = np.ones(n + 1, dtype=np.bool_)
    a[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if a[p]:
            a[p * p : n + 1 : p] = False
    return np.flatnonzero(a)


def increment_log(p: float, k: int) -> float:
    """Exponent increment k: p^(k-1) -> p^k, k>=1."""
    pk = p ** (-k)
    return math.log1p(-pk / p) - math.log1p(-pk)


def ca_state(epsilon: float, primes: np.ndarray) -> dict[str, float | int]:
    log_n = 0.0
    log_sigma_over_n = 0.0
    support: list[tuple[int, int]] = []

    for p0 in primes:
        p = float(p0)
        # k=1: (1-p^-2)/(1-p^-1)=1+1/p.
        if math.log1p(1.0 / p) / math.log(p) <= epsilon:
            break

        exponent = 0
        k = 1
        while increment_log(p, k) / math.log(p) > epsilon:
            exponent += 1
            k += 1

        if exponent:
            support.append((int(p0), exponent))
            log_n += exponent * math.log(p)
            log_sigma_over_n += math.log(
                (1.0 - p ** (-(exponent + 1))) / (1.0 - 1.0 / p)
            )

    if not support:
        raise ValueError("epsilon too large: empty CA support")

    x = support[-1][0]
    pp = primes[primes <= x].astype(float)
    theta_x = float(np.log(pp).sum())
    mertens_log = float((-np.log1p(-1.0 / pp)).sum())

    robin_gap = EULER_GAMMA + math.log(math.log(log_n)) - log_sigma_over_n
    nicolas_log_surplus = (
        mertens_log - EULER_GAMMA - math.log(math.log(theta_x))
    )
    saturation_deficit = mertens_log - log_sigma_over_n
    scale_surplus = math.log(math.log(log_n) / math.log(theta_x))
    complement = saturation_deficit + scale_surplus

    return {
        "support_x": x,
        "log_n": log_n,
        "theta_x": theta_x,
        "log_sigma_over_n": log_sigma_over_n,
        "mertens_log": mertens_log,
        "robin_gap": robin_gap,
        "nicolas_log_surplus": nicolas_log_surplus,
        "saturation_deficit": saturation_deficit,
        "scale_surplus": scale_surplus,
        "complement": complement,
        "identity_error": robin_gap + nicolas_log_surplus - complement,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-limit", type=int, default=2_000_000)
    ap.add_argument(
        "--T",
        type=float,
        nargs="*",
        default=[1e3, 1e4, 1e5, 1e6],
        help="T0 values; epsilon=1/(T0 log T0)",
    )
    ap.add_argument(
        "--out", default="data/formation/robin_nicolas_formation_audit.csv"
    )
    args = ap.parse_args()

    primes = primes_upto(args.prime_limit)
    rows: list[dict[str, float | int]] = []

    for T0 in args.T:
        epsilon = 1.0 / (T0 * math.log(T0))
        row = {"T0": T0, "epsilon": epsilon}
        row.update(ca_state(epsilon, primes))
        x = float(row["support_x"])
        scale = math.sqrt(x) * math.log(x)
        row["sqrtx_logx"] = scale
        row["robin_scaled"] = float(row["robin_gap"]) * scale
        row["nicolas_scaled"] = float(row["nicolas_log_surplus"]) * scale
        row["complement_scaled"] = float(row["complement"]) * scale
        row["saturation_scaled"] = float(row["saturation_deficit"]) * scale
        row["scale_surplus_scaled"] = float(row["scale_surplus"]) * scale
        rows.append(row)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    for r in rows:
        print(
            f"T0={r['T0']:.0f} x={r['support_x']} "
            f"identity_error={r['identity_error']:.3e} "
            f"scaled: Robin={r['robin_scaled']:.6f}, "
            f"Nicolas={r['nicolas_scaled']:.6f}, "
            f"sum={r['complement_scaled']:.6f}"
        )
    print(f"2*sqrt(2)={2*math.sqrt(2):.12f}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
