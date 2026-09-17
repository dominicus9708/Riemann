#!/usr/bin/env python3
"""Finite band-pass audit for Möbius / Liouville / squarefree controls.

Computes
    R_H(a) = integral_{1/H}^{sqrt(2)/H} |P_a(u)|^2 du
             / (((sqrt(2)-1)/H) * sum |a_m|^2)
using FFT autocorrelation and exact integration of the Fourier modes.
"""

import csv
import math
import numpy as np


def mobius_linear(n: int) -> np.ndarray:
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1] = 1
    primes = []
    comp = np.zeros(n + 1, dtype=bool)
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def liouville_linear(n: int) -> np.ndarray:
    lam = np.ones(n + 1, dtype=np.int8)
    lam[0] = 0
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    for i in range(2, n + 1):
        lam[i] = -lam[i // spf[i]]
    return lam


def autocorr(a: np.ndarray) -> np.ndarray:
    n = len(a)
    size = 1 << (2 * n - 1).bit_length()
    A = np.fft.rfft(a, size)
    return np.fft.irfft(A * np.conj(A), size)[:n]


def band_ratio(a: np.ndarray, H: int) -> float:
    c = autocorr(np.asarray(a, dtype=float))
    lo = 1.0 / H
    hi = math.sqrt(2.0) / H
    h = np.arange(1, len(a), dtype=float)
    kernel = (np.sin(2 * np.pi * hi * h) - np.sin(2 * np.pi * lo * h)) / (2 * np.pi * h)
    energy = (hi - lo) * c[0] + 2.0 * np.dot(c[1:], kernel)
    baseline = (hi - lo) * c[0]
    return float(energy / baseline)


def main() -> None:
    rng = np.random.default_rng(20260917)
    rows = []
    for D in [2**k for k in range(12, 18)]:
        mu_all = mobius_linear(2 * D)
        lam_all = liouville_linear(2 * D)
        mu = mu_all[D:2 * D].astype(float)
        lam = lam_all[D:2 * D].astype(float)
        sq = (mu != 0).astype(float)
        rand_sq = sq * rng.choice([-1.0, 1.0], size=D)
        max_h = int(D ** (1.0 / 3.0))
        Hs = [h for h in [4, 8, 16, 32, 64] if h <= max_h]
        if max_h >= 4 and max_h not in Hs:
            Hs.append(max_h)
        for H in Hs:
            for kind, seq in [("mu", mu), ("lambda", lam), ("mu2", sq), ("rand_sq", rand_sq)]:
                rows.append((D, H, kind, band_ratio(seq, H)))

    out = "data/formation/reciprocal_bandpass_parity_summary.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["D", "H", "kind", "ratio"])
        w.writerows(rows)
    print(out)


if __name__ == "__main__":
    main()
