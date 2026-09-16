# Voronoi–Möbius hybrid audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Truncated Voronoi formula: classical.
- Hybrid Möbius / reciprocal-square-root phase reduction: DERIVED.
- Critical square-root-cancellation condition for the small-d half: DERIVED SUFFICIENT CONDITION.
- Full prime-error closure from this condition alone: FALSE; the large-d/Mertens half remains.
- Literature novelty: not claimed. Initial literature search found broad Möbius exponential-sum theory but no result immediately matching the required uniform reciprocal-square-root weighted bound.

## 1. Starting point

For the classical divisor error, use the standard truncated Voronoi form

\[
\Delta(x)=\frac{x^{1/4}}{\pi\sqrt2}\sum_{n\le Y}\frac{\tau(n)}{n^{3/4}}\cos\!\left(4\pi\sqrt{nx}-\frac\pi4\right)+O_\varepsilon\!\left(x^\varepsilon+x^{1/2+\varepsilon}Y^{-1/2}\right).
\]

The exact Möbius–divisor bridge contains

\[
C_\Delta(X)=\sum_{d\le X}\mu(d)\Delta\!\left(\left\lfloor\frac Xd\right\rfloor\right).
\]

Focus first on

\[
A_\Delta(X;K)=\sum_{d\le K}\mu(d)\Delta\!\left(\left\lfloor\frac Xd\right\rfloor\right).
\]

The floor/end-point convention must be retained in a final proof; replacing it by `X/d` in the oscillatory model costs at most RH-scale lattice corrections when `K<=sqrt(X)`.

## 2. Hybrid phase sum

Substitution gives the main oscillatory term

\[
\frac{X^{1/4}}{\pi\sqrt2}\sum_{n\le Y}\frac{\tau(n)}{n^{3/4}}\Re\!\left[e^{-i\pi/4}V_{n,X}(K)\right],
\]

where, with `e(t)=exp(2 pi i t)`,

\[
\boxed{V_{n,X}(K)=\sum_{d\le K}\mu(d)d^{-1/4}e\!\left(2\sqrt{\frac{nX}{d}}\right).}
\]

Thus additive Voronoi oscillation and multiplicative Möbius sign meet in a reciprocal-square-root phase. This is more specific than the closed generic floor-quotient rearrangement.

## 3. Critical parameter matching

Set

\[
K=Y=X^{1/2}.
\]

Assume the uniform estimate

\[
\boxed{|V_{n,X}(K)|\ll_\varepsilon K^{1/4+\varepsilon}\qquad(1\le n\le Y).}
\]

Since

\[
\sum_{n\le Y}\tau(n)n^{-3/4}\ll_\varepsilon Y^{1/4+\varepsilon},
\]

the Voronoi main term is

\[
\ll_\varepsilon X^{1/4}K^{1/4}Y^{1/4}X^\varepsilon=X^{1/2+\varepsilon}.
\]

The summed truncation error is

\[
\ll_\varepsilon KX^\varepsilon+X^{1/2+\varepsilon}Y^{-1/2}\sum_{d\le K}d^{-1/2}
\]

\[
\ll_\varepsilon X^{1/2+\varepsilon}+X^{1/2+\varepsilon}Y^{-1/2}K^{1/2}=O_\varepsilon(X^{1/2+\varepsilon}).
\]

Hence `V << K^(1/4+epsilon)` is sufficient to bring the small-d divisor-error half to RH scale.

## 4. Natural square-root scale

Because the coefficient energy satisfies

\[
\sum_{d\le K}d^{-1/2}\asymp K^{1/2},
\]

a random-sign heuristic predicts magnitude `K^(1/4)`. This is only a scale heuristic, not evidence for RH.

## 5. Standalone insufficiency

The exact hyperbola split remains

\[
T(X)=A(X)+C(X),
\]

and the large-d side contains

\[
\sum_{q\lesssim\sqrt X}b(q)M(\lfloor X/q\rfloor)
\]

plus a boundary correction. Even perfect RH-scale control of the Voronoi–Möbius small-d piece therefore does not control the Mertens side.

The finite audit through `X<=10^6` found that this large-d/Mertens component tracks the full prime error substantially more strongly than the small-d component.

Classification:

`VORONOI_MOBIUS_SMALL_D_SUFFICIENCY_ONLY`.

## 6. Literature position

Classical work of Davenport and later Baker–Harman and others treats strong cancellation in various Möbius exponential sums. The present phase

\[
f(d)=2\sqrt{nX}\,d^{-1/2}
\]

is a reciprocal fractional-power phase with strongly varying oscillation rate. The initial literature search did not identify a theorem directly giving the required uniform `K^(1/4+epsilon)` estimate in the simultaneous critical range

\[
K=Y=X^{1/2},\qquad 1\le n\le Y.
\]

This is a literature-status note, not a novelty claim.

## 7. Current role

Retain this as a module, not the main route:

- a critical weighted square-root estimate would solve the small-d divisor side at RH scale;
- the large-d Mertens quotient side still needs an independent mechanism;
- if the exponential-sum estimate itself imports RH-strength Mertens information, classify it as re-encoding.

Suggested tags:

- `VORONOI_MOBIUS_RECIPROCAL_PHASE_OPEN`;
- `VORONOI_MOBIUS_SMALL_D_SUFFICIENCY_ONLY`.
