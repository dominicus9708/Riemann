# Reciprocal local-Fourier / Gallagher / B-process audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Original reciprocal-phase outer mean square: primary live object.
- Local Fourier-window interpretation: DERIVED.
- Gallagher reduction: reveals a short-interval Möbius L2 target at diagonal scale.
- Existing almost-all short-interval / higher-uniformity theorems: qualitatively relevant but do not directly supply that diagonal L2 scale.
- Outer-n B-process in the hard near-diagonal cell: no independent gain.
- Naive shift-Abel route with full cumulative correlation control: RH-scale circularity guard added.

## 1. Local Taylor coordinates in the arithmetic variable
Fix a short arithmetic block centered at `D0 ~ D` and write

\[
d=D_0+m,\qquad |m|\le J.
\]

For

\[
\phi_n(d)=2K\sqrt n\,d^{-1/2},
\]

Taylor expansion gives

\[
\phi_n(D_0+m)
=
2K\sqrt n\,D_0^{-1/2}
-\theta_n m
+\kappa_n m^2
+O\!\left(\frac{J^3}{H D^2}\right),
\]

where, uniformly for `n~Q`,

\[
\theta_n=K\sqrt n\,D_0^{-3/2}\asymp \frac1H,
\]

\[
\kappa_n=\frac34K\sqrt n\,D_0^{-5/2}\asymp \frac1{HD},
\]

and

\[
H=\frac{D^{3/2}}{K\sqrt Q}.
\]

Thus the natural curvature length is

\[
\boxed{J_{\rm curv}\asymp\sqrt{DH}.}
\]

For `J=o(sqrt(DH))` the quadratic phase is asymptotically negligible; for `J~sqrt(DH)` it is only order one and the cubic remainder is

\[
O\!\left(\sqrt{H/D}\right),
\]

which tends to zero uniformly in the unresolved range `H<=D^{1/2}`.

## 2. The outer n-block scans a short Fourier window
The local linear frequency is

\[
\theta_n=K\sqrt n\,D_0^{-3/2}.
\]

Across `Q<n<=2Q`,

\[
\theta_n\asymp \frac1H,
\qquad
\theta_{n+1}-\theta_n\asymp\frac1{HQ},
\]

and the entire n-block covers a frequency interval of width

\[
\boxed{\Delta\theta\asymp\frac1H.}
\]

Consequently, after removing the harmless global phase and retaining the bounded quadratic chirp when necessary, the outer mean square locally samples the Fourier energy of the Möbius coefficients in a window of width `1/H` around a frequency of the same order.

Classification:

`RECIPROCAL_LOCAL_FOURIER_WINDOW`.

This is a local statement. A global proof still has to control interactions between the `D/J` arithmetic blocks; one must not assume block orthogonality for free.

## 3. Why the generic large sieve reproduces the H-loss
The `Q` local frequencies have spacing about

\[
\delta\asymp\frac1{HQ}.
\]

For arbitrary coefficients on a block of length `J`, the classical large sieve gives a scale

\[
(\delta^{-1}+J)\sum|a_m|^2
\asymp
(HQ+J)\sum|a_m|^2.
\]

The desired mean-square scale would have `Q`, not `HQ`, multiplying the coefficient energy. Thus generic frequency separation loses essentially a factor `H` in the regime where `HQ` dominates.

This is the same obstruction already seen in the reciprocal near-diagonal spacing and in the Type-II DLS audit, now expressed as local Fourier concentration.

Classification:

`LOCAL_FOURIER_GENERIC_LARGE_SIEVE_H_LOSS`.

## 4. Gallagher lemma and the short-interval L2 target
Gallagher's local Fourier lemma has the schematic form

\[
\int_{|\beta|\le 1/(2Y)}
\left|\sum a_m e(\beta m)\right|^2d\beta
\ll
\frac1{Y^2}\int
\left|\sum_{x<m\le x+Y}a_m\right|^2dx
+Y\max|a_m|^2.
\]

Taking `Y~H`, the natural local-Fourier energy predicted by diagonal/Parseval scaling for an unweighted length-`J` Möbius block is

\[
\asymp\frac JH.
\]

Ignoring removable endpoint issues (or using a smooth weighted variant), the arithmetic input that would produce this scale is

\[
\boxed{
\int
\left|\sum_{x<m\le x+H}\mu(m)\right|^2dx
\ll_\varepsilon JH\,D^\varepsilon.
}
\]

This is a genuine **diagonal-size L2 short-interval law**: random signs have precisely this order of magnitude.

After restoring the local weight `d^{-1/4}`, a Fourier window of width `1/H` carrying energy `~J/H` and sampled at density `~QH` contributes

\[
QH\cdot \frac JH\cdot D^{-1/2}
\asymp QJ D^{-1/2},
\]

which is exactly the local share expected from the global target `QD^{1/2}` when shares add without extra loss.

Classification:

`RECIPROCAL_GALLAGHER_DIAGONAL_L2_TARGET`.

## 5. Literature boundary
Matomäki–Radziwiłł prove cancellation of Möbius in almost all short intervals as soon as the interval length tends to infinity. Later Matomäki–Radziwiłł–Tao–Teräväinen–Ziegler prove much stronger average Fourier/Gowers uniformity, including polynomial phases, over short intervals in broad ranges.

These results establish that short Möbius sums are typically **o(H)**, and that they are highly orthogonal to low-complexity phases on average. They do not, from their stated forms alone, give the sharper random-sign/diagonal mean-square scale

\[
\int |\sum_{x<n\le x+H}\mu(n)|^2dx\ll XH\,X^\varepsilon
\]

uniformly in the polynomial ranges needed here.

This distinction matters: `o(H)` per interval corresponds only to `o(H^2)` at the squared level, whereas the desired diagonal scale is `H`.

Recent work on short exponential sums also continues to identify improved Möbius `ell^2` estimates as a source of further progress, consistent with the present reduction.

Permanent guard:

`SHORT_INTERVAL_L1_UNIFORMITY_NOT_L2_DIAGONAL`.

Do not promote an almost-all `o(H)` theorem or an L1-averaged phase-uniformity theorem to the diagonal L2 law without a separate second-moment argument.

## 6. Outer-n B-process does not solve the hard cell
For a fixed pair `(d,d+h)`, the outer kernel phase is

\[
\psi(n)=2K\sqrt n\,[d^{-1/2}-(d+h)^{-1/2}].
\]

For `d~D`,

\[
\psi'(n)
\asymp
\frac{K h}{D^{3/2}\sqrt Q}
=
\frac{h}{HQ}.
\]

Hence over the entire n-block the total phase variation is

\[
Q|\psi'(n)|\asymp\frac hH.
\]

In the genuinely dangerous region

\[
1\le h\lesssim H,
\]

one has

\[
|\psi'(n)|\lesssim \frac1Q,
\]

so there is no nonzero dual integer/stationary branch for a van-der-Corput B-transform to expose. The standard first-derivative estimate is only

\[
|\mathcal K_{Q,K}(d,h)|\lesssim Q
\]

there, i.e. no power gain over the trivial bound.

For `h>>H`, one obtains the familiar decay scale

\[
|\mathcal K_{Q,K}(d,h)|
\lesssim
\frac{HQ}{h}
\]

away from derivative resonances; that is the already-easier far-shift region.

Classification:

`OUTER_BPROCESS_NEAR_CELL_NO_GAIN`.

Thus the outer B-process is useful only after the core near-diagonal obstruction has already been left behind; it does not resolve that obstruction by itself.

## 7. Naive Abel transform and Mertens circularity
Let `I` be an arithmetic block and define the cumulative unweighted pair correlation

\[
C_I(T)
:=
\sum_{1\le h\le T}
\sum_{\substack{d,d+h\in I}}
\mu(d)\mu(d+h).
\]

If `T` reaches the full diameter of `I`, every unordered distinct pair occurs once, and therefore exactly

\[
\boxed{
C_I(\operatorname{diam}I)
=
\frac12
\left[
\left(\sum_{d\in I}\mu(d)\right)^2
-
\sum_{d\in I}\mu(d)^2
\right].
}
\]

Consequently a uniform full-range estimate

\[
|C_I(T)|\ll_\varepsilon |I|^{1+\varepsilon}
\]

strong enough to drive a naive Abel/summation-by-parts argument all the way across the shift range would imply

\[
\left|\sum_{d\in I}\mu(d)\right|
\ll_\varepsilon |I|^{1/2+\varepsilon/2},
\]

a square-root Mertens bound on every such block. Dyadic summation then has RH-level strength.

Classification:

`SHIFT_ABEL_CUMULATIVE_MERTENS_CIRCULARITY_GUARD`.

Abel transformation itself remains legal and potentially useful; the guard only forbids inserting a full-range cumulative-correlation estimate whose strength already contains the desired square-root cancellation.

## 8. Current reduction
The previous Type-II detour and the present local Fourier audit now identify the same core from two directions:

> The unresolved reciprocal-phase block is a local spectral-flatness problem for Möbius at frequency resolution `1/H`, and generic harmonic-analysis inequalities lose exactly the resolution multiplicity `H`.

A viable proof must therefore use arithmetic information while preserving the signed phase kernel. It cannot come solely from:

- generic large-sieve spacing;
- a standard Type-II Cauchy/inverse reduction;
- near-cell B-process oscillation;
- almost-all `o(H)` short-interval cancellation;
- a full-range cumulative correlation bound of Mertens strength.

## 9. Next direct audit
There are now two sharply defined possibilities worth testing:

1. **Weighted short-interval L2 below the generic Gallagher barrier:** exploit the slowly varying reciprocal chirp and Möbius multiplicativity together, rather than first replacing the phase by an arbitrary Fourier frequency;
2. **cross-scale compensation:** derive an exact or signed identity coupling `h<=H` and `h>H`, so that the near-cell need not satisfy the diagonal target separately.

The second direction is especially important because positive/smooth-coefficient false controls already show that full reciprocal-phase cancellation can be much stronger than any estimate obtained by bounding each shift band independently.
