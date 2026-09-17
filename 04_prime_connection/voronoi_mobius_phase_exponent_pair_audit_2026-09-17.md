# Voronoi–Möbius reciprocal-phase exponent-pair audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Reciprocal-square-root phase reduction: inherited from `voronoi_mobius_hybrid_audit_2026-09-16.md`.
- Current generic exponent-pair benchmark: DERIVED from the ANTEDB model-phase definition and its current convex hull.
- Required `K^(1/4+eps)` bound: NOT reached by generic exponent-pair machinery.
- Finite scaling audit: consistent with `K^(1/4)` RMS for Möbius, squarefree-random, and even all-positive coefficients; therefore finite `1/4` scaling is not Möbius-specific evidence.

## 1. Critical hybrid sum

With `X=K^2`, the small-d Voronoi–Möbius module contains

\[
V_{n,K}
=\sum_{d\le K}\mu(d)d^{-1/4}
 e\!\left(2K\sqrt{\frac nd}\right),
\qquad 1\le n\le K.
\]

The previously derived sufficient condition is

\[
|V_{n,K}|\ll_\varepsilon K^{1/4+\varepsilon}
\]

uniformly in `1<=n<=K`.

## 2. Generic phase benchmark

First ignore the Möbius coefficient and study a dyadic block `d~D` with

\[
D=K^\delta,\qquad n=K^\nu,
\qquad 0\le\delta,\nu\le1.
\]

The phase has model size

\[
T\asymp K n^{1/2}D^{-1/2}
=K^{1+\nu/2-\delta/2}.
\]

The ANTEDB definition of an exponent pair `(k,l)` gives, when `T>=D`,

\[
\sum_{d\sim D}e(TF(d/D))
\ll (T/D)^{k+o(1)}D^{l+o(1)}.
\]

After inserting the weight `d^(-1/4)`, the K-exponent is

\[
\boxed{
E_{k,l}(\delta,\nu)
=k\left(1+\frac\nu2-\frac{3\delta}{2}\right)
+\delta\left(l-\frac14\right).
}
\]

The termwise bound gives

\[
E_{\rm triv}=\frac{3\delta}{4}.
\]

For the worst high-frequency endpoint `nu=1`, one has `T>=D` for every `delta<=1`.

## 3. Current exponent-pair bottleneck

Using the current ANTEDB convex-hull vertices, including the 2025 Tao–Trudgian–Yang/Cushing updates and the reflected B-process vertices, numerical optimization of

\[
\min\left(E_{\rm triv},\min_{(k,l)}E_{k,l}(\delta,1)\right)
\]

over `0<=delta<=1` gives a maximum near

\[
\boxed{\delta\approx0.6879,\qquad E\approx0.3488821.}
\]

The active pair at the bottleneck is the B-transform of

\[
\left(\frac{18}{199},\frac{593}{796}\right),
\]

namely

\[
\left(\frac{195}{796},\frac{235}{398}\right).
\]

Thus the current generic model-phase framework only gives a benchmark of roughly

\[
\boxed{K^{0.34889+o(1)}}
\]

for the difficult dyadic region, well above the required `K^(1/4+eps)`.

This is a benchmark for generic smooth phase estimates, not a theorem that every possible method is limited to this exponent. Direct beta(alpha) estimates or structure special to this phase/Möbius weight could in principle do better.

Classification:

`RECIPROCAL_PHASE_GENERIC_EXPONENT_PAIR_GAP`.

## 4. Relation to the exponent-pair conjecture

ANTEDB records the exponent-pair conjecture as the pair `(0,1/2)`, equivalently `beta(alpha)=alpha/2` for `0<=alpha<=1`.

If the generic phase satisfied this ideal square-root law, then on each dyadic block the unweighted exponential sum would have square-root size; after multiplying by `D^(-1/4)`, the natural critical weighted scale is `D^(1/4)`.

This explains why the desired `K^(1/4)` target is genuinely a square-root-cancellation target rather than a routine consequence of present exponent-pair technology.

Do not infer equivalence with the exponent-pair conjecture: the present phase is a single special monomial family and has a Möbius coefficient.

## 5. Finite false-control audit

For finite `K`, compute

\[
V_a(n,K)=\sum_{d\le K}a_d d^{-1/4}e(2K\sqrt{n/d})
\]

for three coefficient systems:

1. `a_d=mu(d)`;
2. independent random signs on squarefree support;
3. `a_d=1`.

For sampled `1<=n<=K` through `K=50000`, the RMS divided by `K^(1/4)` stays approximately constant:

| K | Möbius RMS / K^(1/4) | squarefree-random RMS / K^(1/4) | all-positive RMS / K^(1/4) |
|---:|---:|---:|---:|
| 1,000 | ~1.07 | ~1.11 | ~1.33 |
| 5,000 | ~1.13 | ~1.11 | ~1.38 |
| 10,000 | ~1.11 | ~1.10 | ~1.38 |
| 20,000 | ~1.11 | ~1.13 | ~1.38 |
| 50,000 | ~1.12 | ~1.07 | ~1.31 |

Sample maxima are also only a few multiples of `K^(1/4)` over this range.

### Audit interpretation

The finite `1/4` scaling is therefore not specific to Möbius signs. The reciprocal-square-root phase itself already creates substantial cancellation in finite data.

Permanent guard:

`RECIPROCAL_PHASE_RANDOM_CONTROL` — observing `K^(1/4)` finite scaling in the Möbius hybrid sum is not RH evidence unless it separates from all-positive and random-sign phase controls and is proved uniformly.

## 6. Literature alignment

- Baker–Harman (1991) and later work study Möbius exponential sums, primarily linear/additive phases.
- Robles (2026), `Heath-Brown identities for fractional powers of zeta`, gives Vinogradov-quality linear-phase estimates and includes the Möbius endpoint, but does not directly supply the required reciprocal-square-root weighted uniform estimate.
- The current ANTEDB records the best-known generic model-phase exponent data used in the benchmark above.

No direct theorem was located in the present search that yields

\[
\sup_{1\le n\le K}
\left|\sum_{d\le K}\mu(d)d^{-1/4}e(2K\sqrt{n/d})\right|
\ll K^{1/4+\varepsilon}.
\]

This is a literature-status statement, not a novelty claim.

## 7. Current consequence

The small-d module remains OPEN but is now more sharply classified.

A successful proof must exploit at least one feature beyond current generic exponent-pair control:

- the Möbius coefficient;
- the exact monomial reciprocal phase and its B-process dual structure;
- cancellation after summing over the Voronoi index `n` rather than a uniform pointwise bound in `n`;
- or another bilinear/Type-I/II mechanism.

The last option is particularly important: the previous sufficient condition used a uniform bound in `n`, which may be unnecessarily strong. The next audit should test whether the outer weights `tau(n)n^(-3/4)` allow an averaged or bilinear estimate weaker than uniform `K^(1/4)` but still sufficient for an `X^(1/2+eps)` total bound.
