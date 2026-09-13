"""Compare direct Chebyshev psi(x) with a finite symmetric zero sum.

This is an exploratory regression script only. A finite zero sum is not a
rigorous explicit-formula bound without a certified tail estimate and a
precise summation convention.
"""

from __future__ import annotations

import argparse
import math

import mpmath as mp


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def psi_direct(x: mp.mpf) -> mp.mpf:
    n = int(mp.floor(x))
    total = mp.mpf("0")
    for p in primes_up_to(n):
        power = p
        while power <= n:
            total += mp.log(p)
            if power > n // p:
                break
            power *= p
    return total


def psi_zero_truncation(x: mp.mpf, zeros: list[mp.mpc]) -> mp.mpf:
    # symmetric sum over rho and conjugate rho for the supplied positive zeros
    zero_sum = mp.fsum(2 * mp.re(mp.power(x, rho) / rho) for rho in zeros)
    return (
        x
        - zero_sum
        - mp.log(2 * mp.pi)
        - mp.mpf("0.5") * mp.log(1 - x ** -2)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", nargs="*", default=["100.5", "1000.5"])
    parser.add_argument("--counts", nargs="*", type=int, default=[10, 50, 100, 200])
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    max_count = max(args.counts)
    zeros = [mp.zetazero(n) for n in range(1, max_count + 1)]

    for x_text in args.x:
        x = mp.mpf(x_text)
        direct = psi_direct(x)
        print(f"x={mp.nstr(x, 20)} direct={mp.nstr(direct, 30)}")
        for count in args.counts:
            approx = psi_zero_truncation(x, zeros[:count])
            error = approx - direct
            print(
                f"  pairs={count:6d} approx={mp.nstr(approx, 30)} "
                f"error={mp.nstr(error, 20)}"
            )

    print("AUDIT: finite truncation residuals are not certified tail bounds")


if __name__ == "__main__":
    main()
