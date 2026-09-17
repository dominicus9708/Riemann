# Type-II product-collapse and inverse-scale barrier audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Vaughan decomposition for Möbius: STANDARD.
- Type I reciprocal-phase branch: CLOSED at the required power up to polylogarithms, subject to the recorded endpoint-resonance correction.
- Standard Type-II Cauchy / inverse machinery: useful for qualitative or logarithmic orthogonality, but not automatically adapted to RH square-root scale.
- Apparent three-variable phase freedom: CORRECTED — the arithmetic factor variables collapse exactly through their product.

## 1. Exact Möbius Vaughan identity
Green–Tao Lemma 4.1 gives, for a sequence `f` and `UV<=N`,

\[
\mathbb E_{N<r\le2N}\mu(r)\overline{f(r)}=-T_I+T_{II},
\]

with

\[
T_I=\frac1N\sum_{d\le UV}a_d
\sum_{N/d<w\le2N/d}\overline{f(dw)},
\]

\[
a_d=\sum_{bc=d,\ b\le U,\ c\le V}\mu(b)\mu(c),
\]

and

\[
T_{II}=\frac1N
\sum_{V<d\le2N/U}
\sum_{\max(U,N/d)<w\le2N/d}
\mu(w)b_d\overline{f(dw)},
\]

\[
b_d=\sum_{c\mid d,\ c>V}\mu(c).
\]

The product variable always satisfies `r=dw`.

## 2. Product-collapse of the reciprocal phase
For the present phase

\[
f_n(r)=e\!\left(2K\sqrt n\,r^{-1/2}\right),
\]

one has identically

\[
f_n(dw)
=e\!\left(2K\sqrt n\,d^{-1/2}w^{-1/2}\right)
=e\!\left(2K\sqrt n\,(dw)^{-1/2}\right).
\]

Thus the factor coordinates `(d,w)` do **not** create an independent two-dimensional phase. They are a lifted factorization coordinate system for the single arithmetic variable

\[
r=dw.
\]

Grouping the Type-II expression by `r` gives

\[
T_{II,n}
=\frac1N\sum_{N<r\le2N} C_{U,V}(r)
 e\!\left(2K\sqrt n\,r^{-1/2}\right),
\]

where `C_{U,V}(r)` is a restricted divisor convolution formed from `mu(w)b_d`.

Coefficientwise Vaughan gives

\[
\mu(r)=-A_{U,V}(r)+C_{U,V}(r),
\]

where

\[
A_{U,V}(r)=
\sum_{\substack{bc\mid r\\b\le U,\ c\le V}}
\mu(b)\mu(c).
\]

Hence

\[
C_{U,V}(r)=\mu(r)+A_{U,V}(r).
\]

So the Type-II phase is not a new spectral object: it is the original reciprocal phase carrying a different coefficient decomposition.

Classification:

`TYPEII_PRODUCT_PHASE_COLLAPSE`.

## 3. Meaning of the three-variable monomial form
Keeping the outer Voronoi variable makes the displayed phase

\[
n^{1/2}d^{-1/2}w^{-1/2}.
\]

Real three-dimensional monomial estimates are therefore relevant as **analytic inequalities in the lifted coordinates**, but the phase has the exact multiplicative collapse

\[
d^{-1/2}w^{-1/2}=(dw)^{-1/2}.
\]

Accordingly:

- the literature match to Robert–Sargos remains valid;
- but its existence is not evidence that the present problem has gained a genuinely new independent phase dimension;
- any gain from the lifted variables must come from the factorized coefficient structure or from a bilinear inequality, not from new information in the phase itself.

Permanent guard:

`LIFTED_MONOMIAL_DIMENSION_GUARD` — a factorization coordinate is not counted as a new independent phase degree of freedom when the phase factors exactly through the product map.

## 4. Green–Tao Type-II inverse correlation
Green–Tao Proposition 4.2 shows schematically that a normalized Möbius correlation of size `delta` forces either a Type-I obstruction or a multiplicative four-point correlation of `f` of size at least

\[
\delta^4\log^{-O(1)}N.
\]

The Type-II four-point phase for the reciprocal function is

\[
\begin{aligned}
&f(dw)\overline{f(d'w)}\overline{f(dw')}f(d'w')\\
&=e\!\left(
2K\sqrt n\,[d^{-1/2}-d'^{-1/2}]
[w^{-1/2}-w'^{-1/2}]
\right).
\end{aligned}
\]

Thus the rectangular product difference found in the previous audits is exactly the standard multiplicative parallelogram revealed by the Type-II inverse argument.

This is an important correction: the rectangular identity is not by itself a new structure; it is the natural `U^2`/multiplicative-energy structure already exposed by the standard Type-II Cauchy reduction.

Classification:

`TYPEII_RECTANGLE_STANDARD_INVERSE_STRUCTURE`.

## 5. Square-root-scale quantitative barrier
The Green–Tao inverse theorem is designed to detect correlations `delta` large on logarithmic/qualitative scales. The present RH target is much smaller.

For a sum of length `D`, square-root scale corresponds after normalization to

\[
\delta\asymp D^{-1/2+\varepsilon}.
\]

The inverse lower bound then has scale

\[
\delta^4
\asymp D^{-2+4\varepsilon}
\]

(up to logarithms).

But the normalized four-point multiplicative energy has an exact diagonal baseline. In the representation

\[
\mathcal U=
\mathbb E_{d,d'}
\left|
\mathbb E_w
f(dw)\overline{f(d'w)}
\right|^2,
\]

all `d=d'` terms equal `1`, so

\[
\boxed{\mathcal U\ge \frac1M}
\]

for a factor block `d~M`. Symmetrically,

\[
\mathcal U\ge\frac1L
\]

when written with the other factor outside. With `ML\asymp D`,

\[
\max(M^{-1},L^{-1})\ge D^{-1/2}.
\]

Therefore for every fixed small `epsilon<3/8`,

\[
D^{-2+4\varepsilon}\ll D^{-1/2}.
\]

At RH scale, the inverse-theorem conclusion is thus already below the unavoidable diagonal energy floor. It cannot distinguish a genuine super-square-root obstruction from the baseline multiplicative diagonal.

Classification:

`TYPEII_INVERSE_DELTA4_DIAGONAL_SATURATION`.

This does **not** invalidate Green–Tao's theorem. It only shows that its quantitative architecture is far coarser than the microscopic `D^{-1/2+epsilon}` correlation scale relevant here.

## 6. Relation to the previous Cauchy barriers
This explains the preceding calculations from a more structural viewpoint.

- one-sided Cauchy loses at least one full factor variable;
- full rectangular fourth-moment Cauchy introduces a large diagonal floor;
- the standard Type-II inverse theorem converts a large correlation into a fourth-order multiplicative energy, but at RH scale the required `delta^4` signal lies well below the same diagonal baseline;
- grouping by the product shows that no new phase information was created by the factorization.

Thus these are not four unrelated failures. They are manifestations of one phenomenon:

> **square-root scale is already the natural diagonal-energy scale, while standard Cauchy/inverse reductions deliberately discard the coefficient information needed to distinguish that diagonal scale from a genuine excess.**

## 7. Consequence for the live research front
The standard Vaughan decomposition remains useful as a diagnostic decomposition and for closing Type I, but the following route is now closed as an independent RH strategy:

`Vaughan Type II -> discard arithmetic coefficients by Cauchy -> generic bilinear/trilinear monomial estimate -> RH scale`.

Classification:

`STANDARD_VAUGHAN_COEFFICIENT_REMOVAL_ROUTE_CLOSED_AT_RH_SCALE`.

A surviving Type-II route would have to retain information that the standard inverse theorem removes. There are two logically distinct possibilities:

1. **coefficient-preserving bilinear route:** exploit the actual pair `mu(w), b_d` before Cauchy removes it;
2. **return to the original one-variable mean square:** work directly with the near-diagonal Möbius correlation kernel and preserve the ordered reciprocal-phase weight across shifts.

Because the phase itself collapses through `r=dw`, option 1 is only genuinely new if the factorized coefficient structure produces a provable cancellation unavailable after regrouping by `r`.

## 8. Next audit
Before attempting any further Type-II estimate, test the coefficient-preserving question:

> Does the restricted convolution `mu(w)b_d`, together with the factor ranges imposed by Vaughan, give a cancellation statement stronger than what is already equivalent to controlling the original Möbius reciprocal-phase sum?

If regrouping, Möbius inversion, or a norm identity shows that any required gain is exactly the original near-diagonal Möbius cancellation in another form, close the Type-II route entirely and return to the original kernel.
