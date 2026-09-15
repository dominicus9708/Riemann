# Source registry — integrated Chebyshev / weighted sign criteria — 2026-09-16

## Primary sources

1. Daniel R. Johnston, *On the average value of pi(t)-li(t)*, Canadian Mathematical Bulletin 66 (2023), 185-195; arXiv:2201.06184; DOI 10.4153/S0008439522000212.
   - Proves RH iff integral_2^x (theta(t)-t) dt < 0 for every x>2.
   - Under RH proves |integral_2^x (psi(t)-t) dt| <= 0.08 x^(3/2) for x>=3000.
   - Uses the reciprocal-square zero sum and explicit finite-range estimates.
   - Also studies weighted integrals and the obstruction caused by zeros to substantially stronger unconditional weights.

2. Masatoshi Suzuki, *On variants of Chebyshev's conjecture*, Ramanujan Journal 68 (2025), article 95, DOI 10.1007/s11139-025-01238-9; correction Ramanujan Journal 69 (2026), article 19, DOI 10.1007/s11139-025-01289-y.
   - Studies weighted von-Mangoldt sign criteria, Riesz-like summation, and screw-function formulations.
   - Theorem 1 gives an RH-equivalent eventual nonpositivity criterion for an integrated weighted psi_{1/2} error.
   - Used here as literature context for the smoothing/sign-criterion family, not as evidence for a new proof.

## Standard identity used

Under RH,

sum_rho 1/[rho(1-rho)] = sum_rho 1/|rho|^2
= 2 + EulerGamma - log(4*pi)
= 0.046191417932242... .

This equals twice the first Li coefficient lambda_1. It is used only to upper-bound the absolute coefficient mass of the once-integrated zero wave:

sum_rho 1/|rho(rho+1)|
< sum_rho 1/[rho(1-rho)].

## Project classification

- Johnston sign criterion: known RH equivalence.
- prime-square 2/3 buffer decomposition: structural reinterpretation.
- repeated positive smoothing: inheritance/re-encoding, not independent proof.
- finite-x robustness under extra smoothing must be audited with `SMOOTHING_DELAY_GUARD`.