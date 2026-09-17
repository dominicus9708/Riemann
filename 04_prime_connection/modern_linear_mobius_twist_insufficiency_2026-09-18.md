# Modern linear Möbius twist insufficiency audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Purpose: test whether the current long-Möbius far-resonant block can be closed by locally linearizing the reciprocal phase and importing the strongest currently identified unconditional linear Möbius exponential-sum estimate.
- Literature update: Nicolas Robles (2026) gives a Vinogradov-quality linear-twist estimate for the Möbius endpoint.
- Conclusion: the theorem is highly relevant but still misses the present worst mesoscopic block by a polynomial factor.

## 1. Current local frequency
For a long Möbius factor `w~L` in a product block `D=ML`, the reciprocal phase is

\[
f(w)=2K\sqrt n\,d^{-1/2}w^{-1/2}.
\]

At fixed `d~M`, its local linear frequency has scale

\[
\alpha\asymp \frac{K\sqrt n}{\sqrt D}\frac1L
=\frac{X_n}{L},
\qquad
X_n:=\frac{K\sqrt n}{\sqrt D}.
\]

The corresponding natural rational denominator is therefore

\[
q\asymp \frac{L}{X_n}.
\]

At the extreme block `D=K`, `n~1`, one has `X_n~K^(1/2)`.

The most unbalanced first-generation Vaughan Type-II box has

\[
L\asymp K^{3/4},
\qquad
M\asymp K^{1/4},
\]

hence

\[
q\asymp K^{1/4}\asymp L^{1/3}.
\]

## 2. 2026 linear Möbius theorem
Robles, *Heath-Brown identities for fractional powers of zeta* (2026), proves for the Möbius endpoint an unconditional estimate of the form

\[
\sum_{m\le x}\mu(m)e(m\alpha)
\ll
\left(
 xq^{-1/2}+x^{4/5}+x^{1/2}q^{1/2}
\right)(\log x)^{C_0}
\]

whenever `|alpha-r/q|<=1/q^2` and `(r,q)=1`.

This is substantially sharper structural information than Davenport's uniform logarithmic saving and must be retained in the literature ledger.

## 3. Extreme Type-II substitution
Set

\[
x=L,
\qquad
q\asymp L^{1/3}.
\]

The three terms have powers

\[
xq^{-1/2}=L^{5/6},
\qquad
x^{4/5}=L^{4/5},
\qquad
x^{1/2}q^{1/2}=L^{2/3}.
\]

Thus the theorem yields at best

\[
\boxed{|S_L(\alpha)|\ll L^{5/6+o(1)}}
\]

in the natural small-denominator regime of the worst block.

## 4. Present required scale
For `D=K`, `Q~1`, the relaxed low-`Q` Voronoi target allows an unweighted Type-II block of size

\[
|T|\lesssim K^{3/4+\varepsilon}.
\]

With short factor `M=K^{1/4}` and long factor `L=K^{3/4}`, a triangle/Cauchy reduction that treats each long Möbius sum separately would require scale

\[
|S_L|\lesssim \frac{K^{3/4}}{M}
=K^{1/2}
=L^{2/3}.
\]

Therefore the third Robles term is exactly at the desired power, but the unavoidable first term `L^(5/6)` dominates.

The polynomial deficit is

\[
L^{5/6}/L^{2/3}=L^{1/6}=K^{1/8}.
\]

Classification:

`ROBLES_2026_LINEAR_MOBIUS_BOUND_RELEVANT_BUT_INSUFFICIENT_FOR_LONG_FACTOR`.

## 5. Interpretation
The remaining reciprocal phase should not be replaced globally by a single arbitrary linear twist.

The original phase has curvature

\[
f''(w)\asymp X_nL^{-2},
\]

so its local linear frequency changes by an order-one factor across a dyadic `w` interval. Any successful use of the modern linear theorem would have to exploit this frequency sweep together with averaging in the short factor; pointwise insertion loses too much.

## 6. Guard
Do not cite the 2026 Vinogradov-quality linear Möbius estimate as closing the reciprocal block. It improves the literature benchmark and narrows the missing exponent, but the worst current block still needs coefficient-sensitive curvature/mean-value input.

Reference retained:
- Nicolas Robles, *Heath-Brown identities for fractional powers of zeta*, arXiv:2608.07198 (2026), Theorem 1.3 for the Möbius endpoint.
