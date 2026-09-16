# Voronoi–Möbius hybrid audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Truncated Voronoi formula: classical.
- Hybrid Möbius / reciprocal-square-root phase reduction: DERIVED.
- Critical square-root-cancellation condition for the small-d half: DERIVED SUFFICIENT CONDITION.
- Full prime-error closure from this condition alone: FALSE; the large-d/Mertens half remains.
- Literature novelty: not claimed. Initial literature search found broad Möbius exponential-sum theory but no result immediately matching the required uniform reciprocal-square-root weighted bound.

## 1. Starting point

For the classical divisor error, a standard truncated Voronoi formula is

\[
\Delta(x)
=
\frac{x^{1/4}}{\pi\sqrt2}
\sum_{n\le Y}\frac{\tau(n)}{n^{3/4}}
\cos\!\left(4\pi\sqrt{nx}-\frac\pi4\right)
+
O_\varepsilon\!\left(x^\varepsilon+x^{1/2+\varepsilon}Y^{-1/2}\right),
\]

in the standard admissible parameter range.

The exact Möbius–divisor bridge contains

\[
C_\Delta(X)
=\sum_{d\le X}\mu(d)\Delta\!\left(\left\lfloor\frac Xd\right\rfloor\right).
\]

Focus first on the small-d range

\[
A_\Delta(X;K)
=\sum_{d\le K}\mu(d)\Delta\!\left(\left\lfloor\frac Xd\right\rfloor\right).
\]

Replacing `floor(X/d)` by `X/d` in the main oscillatory discussion costs only a lattice-endpoint correction of RH-scale size when `K<=sqrt(X)`; a fully rigorous use should retain the endpoint convention explicitly.

## 2. Hybrid phase sum

Substituting Voronoi formally and interchanging the finite sums gives the main term

\[
\frac{X^{1/4}}{\pi\sqrt2}
\sum_{n\le Y}\frac{\tau(n)}{n^{3/4}}
\Re\!\left[e^{-i\pi/4}V_{n,X}(K)\right],
\]

where, with `e(t)=exp(2 pi i t)`,

\[
\boxed{
V_{n,X}(K)
=\sum_{d\le K}\mu(d)d^{-1/4}
 e\!\left(2\sqrt{\frac{nX}{d}}\right).
}
\]

Thus the additive Voronoi oscillation and multiplicative Möbius sign meet in a reciprocal-square-root phase.

This is more specific than the previously closed generic floor-quotient rearrangement.

## 3. Critical parameter matching

Choose

\[
K=Y=X^{1/2}.
\]

Suppose one had the uniform hybrid estimate

\[
\boxed{
|V_{n,X}(K)|
\ll_\varepsilon K^{1/4+\varepsilon}
\qquad(1\le n\le Y).
}
\]

Since

\[
\sum_{n\le Y}\tau(n)n^{-3/4}
\ll_\varepsilon Y^{1/4+\varepsilon},
\]

the Voronoi main term is then

\[
\ll_varepsilon
X^{1/4}K^{1/4}Y^{1/4}X^\varepsilon
=X^{1/2+\varepsilon}.
\]

The truncated Voronoi remainder summed over `d<=K` contributes

\[
\ll_\varepsilon
KX^\varepsilon
+
X^{1/2+\varepsilon}Y^{-1/2}
\sum_{d\le K}d^{-1/2}
\]

\[
\ll_\varepsilon
X^{1/2+\varepsilon}
+
X^{1/2+\varepsilon}Y^{-1/2}K^{1/2}
=O_\varepsilon(X^{1/2+\varepsilon}).
\]

Hence the bound `V << K^(1/4+epsilon)` is precisely sufficient to bring the **small-d divisor-error half** to RH scale.

## 4. Why `K^(1/4)` is the natural square-root scale

The coefficient weight is `d^(-1/4)`. A random-sign / square-root heuristic predicts variance

\[
\sum_{d\le K}d^{-1/2}\asymp K^{1/2},
\]

so typical magnitude

\[
K^{1/4}.
\]

Thus the required hybrid bound asks for essentially square-root cancellation relative to the weighted coefficient energy.

This heuristic is not a proof and must not be used as RH evidence.

## 5. Standalone insufficiency

The exact hyperbola split is

\[
T(X)=A(X)+C(X),
\]

where the small-d part `A` contains the high-quotient divisor kernel, while the large-d part `C` contains

\[
\sum_{q\lesssim\sqrt X}b(q)M(\lfloor X/q\rfloor)
\]

plus the boundary correction.

Even perfect RH-scale control of the Voronoi–Möbius small-d piece does **not** control this Mertens side.

The finite audit through `X<=10^6` in fact found that the large-d/Mertens component tracks the full prime error substantially more strongly than the small-d component.

Therefore:

`VORONOI_MOBIUS_SMALL_D_SUFFICIENCY_ONLY`.

Do not promote the hybrid phase estimate to a full RH route without an independent treatment of the large-d quotient side.

## 6. Relation to known Möbius exponential sums

Classical work of Davenport and later Baker–Harman and others gives strong cancellation for various Möbius exponential sums, particularly linear/polynomial oscillatory phases. The present phase

\[
f(d)=2\sqrt{nX}\,d^{-1/2}
\]

is a reciprocal fractional-power phase whose oscillation rate varies strongly across the interval.

An initial literature search did not identify a theorem that directly yields the required **uniform** `K^(1/4+epsilon)` bound simultaneously in the critical range

\[
K=Y=X^{1/2},\qquad 1\le n\le Y.
\]

This is a literature-status note, not a novelty claim.

## 7. Current role

This hybrid sum is worth retaining as a **module**, not as the main route:

- if a known or new theorem gives the critical weighted square-root cancellation, the small-d divisor side is solved at RH scale;
- the project must still solve or bypass the large-d Mertens quotient side;
- if the needed exponential-sum bound itself implies RH-strength Mertens cancellation after specialization/limiting, classify it as re-encoding rather than an independent mechanism.

Suggested tags:

- `VORONOI_MOBIUS_RECIPROCAL_PHASE_OPEN`;
- `VORONOI_MOBIUS_SMALL_D_SUFFICIENCY_ONLY`.
