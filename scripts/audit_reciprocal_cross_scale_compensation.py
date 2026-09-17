#!/usr/bin/env python3
"""Reproduce the reciprocal cross-scale lag-compensation audit.

For dyadic d in (D,2D] and n in (Q,2Q], compute

    V_n = sum_d c_d d^(-1/4) exp(2*pi*i*2*K*sqrt(n/d)),

then reconstruct sum_n |V_n|^2 from FFT autocorrelations in the d-shift h.
The script reports the full mean square and the partial lag profiles h<=H
and h<=8H, each normalized by the exact finite diagonal contribution.

Coefficient controls:
  mu       : Möbius coefficients
  positive : all coefficients +1
  random   : fixed-seed Rademacher signs

The all-positive control is important: it shows that a large or even
negative near-cell partial profile can still be followed by a very small
full mean square once farther shift scales are restored.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def mobius_sieve(n: int) -> np.ndarray:
    """Linear sieve for mu(0..n)."""
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1] = 1
    primes: list[int] = []
    is_composite = np.zeros(n + 1, dtype=np.bool_)
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def next_pow_two(n: int) -> int:
    return 1 << (n - 1).bit_length()


def coefficient_vector(mode: str, D: int, mu: np.ndarray, seed: int) -> np.ndarray:
    if mode == "mu":
        return mu[D + 1 : 2 * D + 1].astype(np.float64)
    if mode == "positive":
        return np.ones(D, dtype=np.float64)
    if mode == "random":
        rng = np.random.default_rng(seed)
        return rng.choice(np.array([-1.0, 1.0]), size=D)
    raise ValueError(f"unknown coefficient mode: {mode}")


def audit_one(D: int, Q: int, K: int, mode: str, mu: np.ndarray, seed: int) -> dict[str, float | int | str]:
    d = np.arange(D + 1, 2 * D + 1, dtype=np.float64)
    coeff = coefficient_vector(mode, D, mu, seed)
    amp = coeff * d ** (-0.25)

    nfft = next_pow_two(2 * D)
    lag_corr = np.zeros(D, dtype=np.complex128)
    direct = 0.0

    # numpy ifft(fft(z) * conj(fft(z))) at lag h equals
    # sum_j z[j+h] * conj(z[j]) for the non-wrapped range after zero padding.
    for nv in range(Q + 1, 2 * Q + 1):
        phase = 2.0 * K * math.sqrt(nv) * d ** (-0.5)
        z = amp * np.exp(2j * math.pi * phase)
        direct += float(abs(z.sum()) ** 2)
        fz = np.fft.fft(z, nfft)
        ac = np.fft.ifft(fz * np.conjugate(fz))
        lag_corr += ac[:D]

    diag = float(lag_corr[0].real)
    reconstructed = diag + 2.0 * float(lag_corr[1:].real.sum())

    H = D ** 1.5 / (K * math.sqrt(Q))
    h1 = max(0, min(D - 1, int(math.floor(H))))
    h8 = max(0, min(D - 1, int(math.floor(8.0 * H))))

    partial_h = diag + 2.0 * float(lag_corr[1 : h1 + 1].real.sum())
    partial_8h = diag + 2.0 * float(lag_corr[1 : h8 + 1].real.sum())

    rel_reconstruction_error = abs(reconstructed - direct) / max(1.0, abs(direct))
    if rel_reconstruction_error > 5e-10:
        raise RuntimeError(
            f"lag reconstruction failed: D={D} Q={Q} mode={mode} "
            f"relative error={rel_reconstruction_error:.3e}"
        )

    return {
        "D": D,
        "Q": Q,
        "K": K,
        "H": H,
        "coefficients": mode,
        "diagonal": diag,
        "full_mean_square": direct,
        "full_over_diag": direct / diag,
        "le_H_over_diag": partial_h / diag,
        "le_8H_over_diag": partial_8h / diag,
        "reconstruction_relative_error": rel_reconstruction_error,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/formation/reciprocal_cross_scale_compensation_audit.csv"),
    )
    args = parser.parse_args()

    # These choices give H=4,8,16 when K=D.
    configs = [
        (1024, 64), (1024, 16), (1024, 4),
        (2048, 128), (2048, 32), (2048, 8),
        (4096, 256), (4096, 64), (4096, 16),
    ]
    max_d = max(2 * D for D, _ in configs)
    mu = mobius_sieve(max_d)

    rows: list[dict[str, float | int | str]] = []
    for D, Q in configs:
        for mode in ("mu", "positive", "random"):
            row = audit_one(D, Q, D, mode, mu, args.seed)
            rows.append(row)
            print(
                f"D={D:4d} Q={Q:4d} H={row['H']:5.1f} {mode:8s} "
                f"full/diag={row['full_over_diag']:.6f} "
                f"<=H/diag={row['le_H_over_diag']:.6f} "
                f"<=8H/diag={row['le_8H_over_diag']:.6f}"
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
