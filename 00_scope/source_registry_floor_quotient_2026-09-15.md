# Audited Source Registry — Floor-Quotient Supplement 2026-09-15

## S046 — Jeffery C. Lagarias & David Harry Richman (2024), The floor quotient partial order

- Type: `PRIMARY_RESEARCH`.
- Journal: Advances in Applied Mathematics 153 (2024), Paper 102615.
- DOI: `10.1016/j.aam.2023.102615`.
- arXiv: `2212.11689`.
- Role: defines the floor quotient order `d <=_1 n` iff `d=floor(n/k)` for some positive integer `k`; develops its incidence Möbius function `mu_1(d,n)`.
- Exact results used in this audit:
  - the initial interval has lower/upper halves exchanged by `d -> floor(n/d)`;
  - the upper half is anti-isomorphic to the divisor order on `1..floor(sqrt(n))`;
  - `mu_1(floor(n/k),n)=mu(k)` for `k<=sqrt(n)`;
  - general bound `|mu_1(d,n)| <= (n/d)^alpha0`, where `zeta(alpha0)=2` and `alpha0≈1.729`;
  - `mu_1(1,n)` has infinitely many sign changes;
  - a separate recursion exists for the differenced one-variable floor-poset Möbius function at `n=s^2` and `n=s(s+1)`.
- Critical audit use: classical Möbius cancellation is exactly embedded in the top half, so floor-poset representations must be checked for whether they simplify or merely move the cancellation to the lower half.
- Audit verdict: `ACCEPT_AS_PRIMARY_FLOOR_QUOTIENT_REFERENCE`.

## S047 — Jean-Paul Cardinal & Marius Overholt (2020), A Variant of Möbius Inversion

- Type: `PRIMARY_RESEARCH`.
- Journal: Experimental Mathematics 29(3), 247–252.
- DOI: `10.1080/10586458.2018.1459960`.
- Role: develops Möbius inversion through symmetric positive-definite matrices related to divisibility and gives a new formula for the Mertens function.
- Critical audit use: matrix/floor-quotient inversion is an existing analytic-number-theory route; a new matrix representation alone is not independent RH progress.
- Audit verdict: `ACCEPT_FOR_MATRIX_MOBIUS_INVERSION_CONTEXT`.

## S048 — Lagarias & Richman (2025), The family of a-floor quotient partial orders

- Type: `PRIMARY_RESEARCH / PROCEEDINGS_CHAPTER`.
- In: Combinatorial and Additive Number Theory VI, pp. 283–318.
- DOI: `10.1007/978-3-031-65064-2_15`.
- arXiv: `2403.04342`.
- Role: generalizes the floor quotient order to a family interpolating between the floor quotient order and divisor order.
- Critical audit use: prevents treating the `a=1` order as an isolated newly discovered structure; there is already a broader structural family.
- Audit verdict: `ACCEPT_FOR_GENERALIZED_FLOOR_ORDER_CONTEXT`.

## Current consequence

The repository's exact corollary

`M(s) = - sum_{d<=s} mu_1(d,s(s+1))`

is retained as an information-preservation identity, not as a novelty claim. Numerical audit shows that the lower-half absolute mass is far larger than `|M(s)|`, so the representation currently moves rather than removes cancellation.
