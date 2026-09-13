#!/usr/bin/env python3
"""Audit the finite squarefree Boolean-group / Hilbert-space bridge.

For the first m primes p_1,...,p_m let P_m be their primorial and
G_m = D(P_m) ~= (Z/2Z)^m.  For a cutoff X define

    f_{X,m}(d) = 1[d <= X],  d | P_m.

The raw Fourier coefficient against the Mobius/parity character is

    F_m(X) = sum_{d|P_m, d<=X} mu(d).

This is exactly the prime-activation state used elsewhere in the repository.
The script verifies the exact-zero primorial regime, records the Haar density,
and compares F with the generic Parseval bound sqrt(2^m N).

Optionally it computes the full Walsh spectrum at one m and aggregates Fourier
energy by degree.  This is a finite diagnostic only; no RH claim is made.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def primes_up_to_count(count: int) -> list[int]:
    if count <= 0:
        return []
    # More than enough for the default 20; grow if required.
    bound = max(100, int(count * (math.log(max(count, 2)) + math.log(math.log(max(count, 3))) + 3)))
    while True:
        sieve = bytearray(b"\x01") * (bound + 1)
        sieve[:2] = b"\x00\x00"
        for p in range(2, int(bound**0.5) + 1):
            if sieve[p]:
                sieve[p * p : bound + 1 : p] = b"\x00" * (((bound - p * p) // p) + 1)
        ps = [i for i in range(2, bound + 1) if sieve[i]]
        if len(ps) >= count:
            return ps[:count]
        bound *= 2


def finite_group_rows(X: int, max_m: int):
    primes = primes_up_to_count(max_m)
    # Store only states satisfying d<=X.  Python integers avoid primorial overflow.
    states: list[tuple[int, int]] = [(1, 1)]  # (product, Mobius parity sign)
    primorial = 1
    rows = []
    for m, p in enumerate(primes, start=1):
        additions = [(d * p, -sgn) for d, sgn in states if d * p <= X]
        states.extend(additions)
        primorial *= p
        N = len(states)
        F = sum(sgn for _, sgn in states)
        group_size = 1 << m
        density = N / group_size
        parseval_bound = math.sqrt(group_size * N)
        rows.append(
            {
                "m": m,
                "p_m": p,
                "primorial_le_X": primorial <= X,
                "primorial": primorial,
                "N_allowed": N,
                "group_size": group_size,
                "density": density,
                "F": F,
                "F_over_group": F / group_size,
                "F_over_parseval_bound": abs(F) / parseval_bound if parseval_bound else 0.0,
            }
        )
    return rows, primes


def full_indicator(X: int, primes: list[int]) -> np.ndarray:
    """Boolean halfspace indicator indexed by bit masks, using log sums."""
    vals = np.array([0.0], dtype=np.float64)
    for p in primes:
        lp = math.log(p)
        vals = np.concatenate((vals, vals + lp))
    return (vals <= math.log(X) + 1e-12).astype(np.float64)


def fwht(a: np.ndarray) -> np.ndarray:
    a = a.copy()
    h = 1
    n = len(a)
    while h < n:
        x = a.reshape(-1, 2 * h)
        left = x[:, :h].copy()
        right = x[:, h:].copy()
        x[:, :h] = left + right
        x[:, h:] = left - right
        h *= 2
    return a


def degree_spectrum(X: int, primes: list[int]):
    m = len(primes)
    f = full_indicator(X, primes)
    hat = fwht(f)
    idx = np.arange(1 << m, dtype=np.uint32)
    raw = idx.view(np.uint8).reshape(-1, 4)
    degree = np.unpackbits(raw, axis=1).sum(axis=1)
    total_energy = float(np.sum(hat * hat))
    rows = []
    for k in range(m + 1):
        vals = hat[degree == k]
        rows.append(
            {
                "degree": k,
                "count": len(vals),
                "energy_fraction": float(np.sum(vals * vals) / total_energy),
                "rms_raw": float(np.sqrt(np.mean(vals * vals))),
                "max_abs_raw": float(np.max(np.abs(vals))),
            }
        )
    # all-bits mask = Mobius parity character
    return rows, int(round(hat[-1]))


def write_csv(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--X", type=int, default=2**20)
    ap.add_argument("--max-m", type=int, default=20)
    ap.add_argument("--spectrum-m", type=int, default=20)
    ap.add_argument(
        "--summary-out",
        type=Path,
        default=Path("data/formation/boolean_hilbert_bridge_2pow20.csv"),
    )
    ap.add_argument(
        "--spectrum-out",
        type=Path,
        default=Path("data/formation/boolean_halfspace_fourier_degree_2pow20_m20.csv"),
    )
    args = ap.parse_args()

    rows, primes = finite_group_rows(args.X, args.max_m)
    write_csv(args.summary_out, rows)

    if args.spectrum_m > args.max_m:
        raise SystemExit("spectrum-m must be <= max-m")
    spectrum, parity = degree_spectrum(args.X, primes[: args.spectrum_m])
    write_csv(args.spectrum_out, spectrum)

    expected = next(r["F"] for r in rows if r["m"] == args.spectrum_m)
    if parity != expected:
        raise AssertionError((parity, expected))

    # Exact orthogonality invariant before the primorial crosses X.
    for r in rows:
        if r["primorial_le_X"] and r["F"] != 0:
            raise AssertionError(f"orthogonality failure at m={r['m']}: F={r['F']}")

    print(f"X={args.X}, max_m={args.max_m}")
    print(f"spectrum m={args.spectrum_m}, parity coefficient={parity}")
    print(f"wrote {args.summary_out}")
    print(f"wrote {args.spectrum_out}")


if __name__ == "__main__":
    main()
