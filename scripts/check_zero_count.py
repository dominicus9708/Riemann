"""Regression checks for N(T), theta(T), and S(T).

This script is NOT a rigorous zero-certification tool. It compares mpmath's
implementations of the zeta zero-counting identities and the smooth
Riemann-von Mangoldt main term. Later certification code must use interval
arithmetic and an independent completeness argument.
"""

from __future__ import annotations

import argparse

import mpmath as mp


def smooth_count(T: mp.mpf) -> mp.mpf:
    return (
        T / (2 * mp.pi) * mp.log(T / (2 * mp.pi))
        - T / (2 * mp.pi)
        + mp.mpf(7) / 8
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("T", nargs="*", type=str, default=["50", "100", "143.12", "1000", "10000"])
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    mp.mp.dps = args.dps

    print("T,nzeros,smooth_plus_7_8,S,theta_pi_plus_1_plus_S")
    for text in args.T:
        T = mp.mpf(text)
        n = mp.nzeros(T)
        S = mp.backlunds(T)
        theta = mp.siegeltheta(T)
        identity = theta / mp.pi + 1 + S
        print(
            ",".join(
                [
                    mp.nstr(T, 20),
                    str(n),
                    mp.nstr(smooth_count(T), 20),
                    mp.nstr(S, 20),
                    mp.nstr(identity, 20),
                ]
            )
        )

    print("AUDIT: this is a regression check, not a certified completeness proof")


if __name__ == "__main__":
    main()
