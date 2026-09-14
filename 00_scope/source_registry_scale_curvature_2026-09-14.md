# Mertens Scale-Curvature Source Audit — 2026-09-14

This note records literature relevant to the multiplicative-scale curvature branch. It inherits the repository's evidence/status rules.

## S040 — Nathan Ng (2004), The Distribution of the Summatory Function of the Möbius Function

- Type: `PRIMARY_RESEARCH`.
- Journal: Proceedings of the London Mathematical Society 89(2), 361–389.
- DOI: `10.1112/S0024611504014741`.
- Role: studies the normalized signal `e^(-y/2) M(e^y)`, weak-Mertens-type mean square, and a limiting distribution under RH plus conjectural negative-moment control of `zeta'(rho)`.
- Critical audit use: long-log-scale curvature/autocorrelation is not a new spectral viewpoint; normalized Mertens statistics and their zero-residue energy already have a substantial literature.
- Audit verdict: `ACCEPT_FOR_NORMALIZED_MERTENS_DISTRIBUTION_AND_ZERO_ENERGY_CONTEXT`.

## S041 — H. M. Bui (2024), Negative discrete moments of the derivative of the Riemann zeta-function

- Type: `PRIMARY_RESEARCH`.
- Journal: Bulletin of the London Mathematical Society.
- DOI: `10.1112/blms.13092`.
- Role: modern discussion of negative moments of `zeta'(rho)` and their relation to the Weak Mertens Conjecture.
- Critical audit use: records the classical implication that WMC forces RH, simplicity of nontrivial zeros, and convergence of reciprocal-derivative square sums; therefore an L2 curvature-energy bound can be stronger than bare RH.
- Audit verdict: `ACCEPT_FOR_WEAK_MERTENS_AND_NEGATIVE_MOMENT_CONTEXT`.

## S042 — Sergey Liflandsky (2026), Explicit formula for the discrete Laplace transform of the Möbius function, related special functions, and a criterion for the Riemann hypothesis

- Type: `PRIMARY_RESEARCH_PREPRINT`.
- arXiv: `2607.09797`.
- Role: gives a zero-based explicit formula for a discrete Laplace transform of the Möbius function under a simple-zero assumption and formulates an RH criterion from transform growth.
- Critical audit use: smoothing the Möbius sum by a Laplace kernel and reading zero exponents is itself not novel; if the scale-curvature branch adopts a smoothed transform, novelty must lie in an additional nonlinear pair-filter or arithmetic inequality.
- Limitation: recent preprint; do not use as authority for a settled theorem beyond its stated assumptions.
- Audit verdict: `ACCEPT_AS_RECENT_PREPRINT_FOR_SMOOTHED_MOBIUS_OVERLAP`.

## S043 — Nicholas G. Polson (2026), Thorin, Levy and Mobius: Sign Structure in the Reciprocals of xi and zeta

- Type: `RECENT_PREPRINT / SSRN`.
- DOI: `10.2139/ssrn.7243438`.
- Role: proposes RH-equivalent positivity conditions involving Hankel determinant families built from a different moment construction attached to `xi`/`zeta`.
- Critical audit use: the phrase 'Hankel determinant criterion for RH' is already occupied by unrelated recent work; no novelty claim should be made merely from using a `2x2` determinant.
- Limitation: not the same observable as `M(X/a)^2-M(X)M(X/a^2)`; current targeted search did not identify a direct published match to the repository's multiplicative-scale determinant.
- Audit verdict: `CONTEXT_ONLY / DO_NOT_CONFLATE_WITH_SCALE_CURVATURE`.

## Current audit consequence

The scale-curvature identity is algebraically useful because it kills one exponential mode and exposes pair interference, but its long-average is a second-order spectral-energy/autocorrelation object. The first-100 known-zero reconstruction already explains the empirical dyadic curvature mean to within a few percent. Therefore the branch is classified as `SPECTRAL_REENCODING` unless an arithmetic-only cross-scale bound survives after the known zero-energy contribution is removed.
