# Voronoi–Möbius random-sign false-control audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Critical hybrid sum scale `K^(1/4)`: NUMERICALLY OBSERVED for Möbius weights.
- Same scale under random-sign squarefree controls: NUMERICALLY OBSERVED.
- Interpretation as RH-specific evidence: REJECTED.
- Uniform theorem `V << K^(1/4+epsilon)`: still OPEN.

## 1. Critical hybrid sum

At the critical parameter choice `X=K^2`, define

\[
V_{n,K}:=
\sum_{d\le K}\mu(d)d^{-1/4}
 e\!\left(2K\sqrt{\frac nd}\right),
\qquad 1\le n\le K,
\]

where `e(t)=exp(2 pi i t)`.

The previous Voronoi–Möbius audit showed that a uniform estimate

\[
|V_{n,K}|\ll_\varepsilon K^{1/4+\varepsilon}
\]

would be sufficient to bring the small-`d` divisor-error half to RH scale.

## 2. Finite numerical audit

For several values of `K`, the sum was evaluated on a mixture of fixed, logarithmic-scale and random `n` values in `[1,K]`.

Typical observed behavior:

- `K=5,000`: median `|V|/K^(1/4)` about `0.95`, sampled maximum about `2.5`;
- `K=10,000`: median about `0.92`, sampled maximum about `2.2`;
- `K=20,000`: median about `0.93`, sampled maximum about `2.2`;
- `K=50,000`: median about `0.95`, sampled maximum about `2.4`.

The tested finite data are therefore consistent with the critical `K^(1/4)` scale.

This is not a proof and does not establish a uniform bound over every `1<=n<=K`.

## 3. Random-sign squarefree control

To determine whether the observed scale is special to Möbius arithmetic, keep exactly the same squarefree support

\[
\{d\le K:\mu(d)\ne0\}
\]

but replace each nonzero Möbius sign by an independent random sign `epsilon_d in {+1,-1}`.

Define

\[
V^{\rm rand}_{n,K}
=
\sum_{d\le K}\epsilon_d\mu(d)^2 d^{-1/4}
 e\!\left(2K\sqrt{\frac nd}\right).
\]

Across 20 random-sign controls for each tested `K`, the normalized medians and sampled maxima were essentially the same as for the actual Möbius sequence.

Representative control averages:

| K | Möbius median / K^(1/4) | random median | Möbius sampled max | random sampled max |
|---:|---:|---:|---:|---:|
| 5,000 | ~0.95 | ~0.92 | ~2.50 | ~2.55 |
| 10,000 | ~0.92 | ~0.94 | ~2.18 | ~2.50 |
| 20,000 | ~0.93 | ~0.91 | ~2.16 | ~2.49 |
| 50,000 | ~0.95 | ~0.91 | ~2.41 | ~2.61 |

Hence the finite `K^(1/4)` behavior is explained naturally by square-root cancellation relative to the coefficient energy

\[
\sum_{d\le K}\mu(d)^2d^{-1/2}\asymp K^{1/2}.
\]

Its square root is `K^(1/4)`.

## 4. False-control classification

Classification:

`VORONOI_MOBIUS_RANDOM_SIGN_SCALE_FALSE_CONTROL`.

Permanent rule:

A finite numerical observation of

\[
|V_{n,K}|\asymp K^{1/4}
\]

must not be interpreted as RH-specific Möbius structure unless it separates actual Möbius signs from random squarefree sign controls.

The present data do not provide such separation.

## 5. What remains genuinely open

The finite false control does **not** close the analytic estimate itself.

The live question is still the uniform deterministic theorem

\[
\boxed{
\sup_{1\le n\le K}|V_{n,K}|
\ll_\varepsilon K^{1/4+\varepsilon}.
}
\]

A proof would require controlling the Möbius-weighted reciprocal-square-root chirp uniformly in its growing parameter.

Existing classical uniform Möbius exponential-sum results mainly address linear or polynomial phases; no directly applicable theorem was identified in the current literature audit that yields this bound in the critical parameter range.

Any successful proof must also be audited for whether it imports RH-strength cancellation through a hidden Mertens or zero-free hypothesis.
