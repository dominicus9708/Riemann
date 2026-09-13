#!/usr/bin/env python3
"""Generate multiplicative formation descriptors for integers.

Baseline convention:
- prime factorization is the arithmetic invariant baseline.
- a formation word is an ordered sequence of prime-factor extraction.
  Example: 12 -> (2,3,2), (2,2,3), (3,2,2).
- an unordered factor tree is a full binary multiplication tree with prime
  leaves. Swapping siblings is identified, but different parenthesizations
  are retained.
- primes have zero nontrivial formation words and zero nontrivial factor trees.

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path


def factorint(n: int) -> dict[int, int]:
    if n < 2:
        raise ValueError("n must be >= 2")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime(n: int) -> bool:
    f = factorint(n)
    return len(f) == 1 and next(iter(f.values())) == 1


def divisor_count(factors: dict[int, int]) -> int:
    ans = 1
    for exponent in factors.values():
        ans *= exponent + 1
    return ans


def factor_pairs(n: int) -> list[tuple[int, int]]:
    return [(a, n // a) for a in range(2, int(n ** 0.5) + 1) if n % a == 0]


def factorization_text(factors: dict[int, int]) -> str:
    parts = []
    for p, exponent in sorted(factors.items()):
        parts.append(str(p) if exponent == 1 else f"{p}^{exponent}")
    return "*".join(parts)


def unique_multiset_permutations(values: list[int]) -> list[tuple[int, ...]]:
    counter = Counter(values)
    length = len(values)
    path: list[int] = []
    out: list[tuple[int, ...]] = []

    def visit() -> None:
        if len(path) == length:
            out.append(tuple(path))
            return
        for value in sorted(counter):
            if counter[value]:
                counter[value] -= 1
                path.append(value)
                visit()
                path.pop()
                counter[value] += 1

    visit()
    return out


@lru_cache(maxsize=None)
def factor_trees(n: int) -> tuple[str, ...]:
    if is_prime(n):
        return (str(n),)

    out: set[str] = set()
    for a, b in factor_pairs(n):
        for left in factor_trees(a):
            for right in factor_trees(b):
                x, y = sorted((left, right))
                out.add(f"({x}*{y})")
    return tuple(sorted(out))


def tree_depth(serialized: str) -> int:
    depth = 0
    maximum = 0
    for ch in serialized:
        if ch == "(":
            depth += 1
            maximum = max(maximum, depth)
        elif ch == ")":
            depth -= 1
    return maximum


def make_record(n: int) -> dict:
    factors = factorint(n)
    prime = is_prime(n)
    multiset = [p for p, e in sorted(factors.items()) for _ in range(e)]
    pairs = factor_pairs(n)

    if prime:
        words: list[tuple[int, ...]] = []
        trees: list[str] = []
        min_depth = max_depth = 0
    else:
        words = unique_multiset_permutations(multiset)
        trees = list(factor_trees(n))
        depths = [tree_depth(t) for t in trees]
        min_depth, max_depth = min(depths), max(depths)

    return {
        "n": n,
        "class": "prime" if prime else "composite",
        "factorization": factorization_text(factors),
        "prime_factor_multiset": multiset,
        "omega": len(factors),
        "Omega": sum(factors.values()),
        "tau": divisor_count(factors),
        "smallest_prime_factor": min(factors),
        "largest_prime_factor": max(factors),
        "factor_pairs": pairs,
        "formation_words": words,
        "unordered_factor_trees": trees,
        "min_tree_depth": min_depth,
        "max_tree_depth": max_depth,
    }


def write_summary(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "n", "class", "factorization", "omega", "Omega", "tau",
        "smallest_prime_factor", "largest_prime_factor",
        "nontrivial_factor_pair_count", "formation_word_count",
        "unordered_tree_count", "min_tree_depth", "max_tree_depth",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in records:
            writer.writerow({
                "n": r["n"],
                "class": r["class"],
                "factorization": r["factorization"],
                "omega": r["omega"],
                "Omega": r["Omega"],
                "tau": r["tau"],
                "smallest_prime_factor": r["smallest_prime_factor"],
                "largest_prime_factor": r["largest_prime_factor"],
                "nontrivial_factor_pair_count": len(r["factor_pairs"]),
                "formation_word_count": len(r["formation_words"]),
                "unordered_tree_count": len(r["unordered_factor_trees"]),
                "min_tree_depth": r["min_tree_depth"],
                "max_tree_depth": r["max_tree_depth"],
            })


def write_detail(records: list[dict], path: Path, lo: int, hi: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "0.1",
        "range": [lo, hi],
        "equivalence": {
            "formation_word": (
                "ordered prime-factor extraction sequence; "
                "same value sequence counted once"
            ),
            "factor_tree": (
                "full binary multiplication tree with prime leaves; "
                "left/right swaps identified; different parenthesizations retained"
            ),
            "prime": "no nontrivial formation word or factor tree",
        },
        "records": records,
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lo", type=int, default=2)
    parser.add_argument("--hi", type=int, default=100)
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("data/formation/formation_summary_2_100.csv"),
    )
    parser.add_argument(
        "--detail",
        type=Path,
        default=Path("data/formation/formation_detail_2_100.json"),
    )
    args = parser.parse_args()

    if args.lo < 2 or args.hi < args.lo:
        raise SystemExit("require 2 <= lo <= hi")

    records = [make_record(n) for n in range(args.lo, args.hi + 1)]
    write_summary(records, args.summary)
    write_detail(records, args.detail, args.lo, args.hi)


if __name__ == "__main__":
    main()
