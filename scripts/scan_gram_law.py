"""Scan Gram points for failures of the empirical sign rule.

Gram's law is intentionally treated as an empirical pattern, not as a
completeness theorem. This script exists partly as a negative-control fixture:
a long successful run of a pattern must not be generalized without proof.
"""

from __future__ import annotations

import argparse

import mpmath as mp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=300)
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    print("n,gram_point,Z_at_gram_point")
    failures = 0

    for n in range(args.start, args.stop):
        g = mp.grampoint(n)
        z = mp.siegelz(g)
        expected_sign_ok = ((-1) ** n) * z > 0
        if not expected_sign_ok:
            failures += 1
            print(f"{n},{mp.nstr(g, 40)},{mp.nstr(z, 40)}")

    print(f"# failures={failures}")
    print("# AUDIT: Gram's law is not a proof of zero completeness")


if __name__ == "__main__":
    main()
