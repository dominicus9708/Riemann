# Voronoi–Möbius mean-square and resolution audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Previous uniform reciprocal-phase target: SUFFICIENT but unnecessarily strong.
- Dyadic mean-square target: DERIVED SUFFICIENT CONDITION for the small-d Voronoi module.
- Rademacher/random-sign energy scale: EXACT expectation / FALSE CONTROL.
- Finite Möbius and positive-coefficient numerics: consistent with the same K^(1/4) scale.
- Direct double-large-sieve treatment: resolves a substantial spacing region but leaves a high-d / low-n resolution corner.
- Full small-d proof: OPEN.

## 1. Reciprocal phase transform

At the critical symmetric choice

\[
X=K^2,\qquad Y=K,
\]

the Voronoi–Möbius module contains

\[
V_n(K)
:=\sum_{d\le K}\mu(d)d^{-1/4}
 e\!\left(2K\sqrt{\frac nd}\right),
\qquad 1\le n\le K.
\]

The previous audit observed that the pointwise estimate

\[
|V_n(K)|\ll_\varepsilon K^{1/4+\varepsilon}
\]

would be sufficient to put the small-d divisor-error term at RH scale. The present audit shows that a dyadic mean-square estimate is enough.

## 2. Dyadic mean-square criterion

For every dyadic `1<=N<=K`, define

\[
\mathcal M(N,K)
:=\sum_{N<n\le2N}|V_n(K)|^2.
\]

Sufficient target:

\[
\boxed{
\mathcal M(N,K)
\ll_\varepsilon N K^{1/2+\varepsilon}
\qquad(1\le N\le K).
}
\]

To see sufficiency, the Voronoi main term is, up to constants,

\[
K^{1/2}
\sum_{n\le K}\tau(n)n^{-3/4}V_n(K).
\]

On a dyadic n-block, Cauchy--Schwarz gives

\[
\sum_{n\asymp N}\tau(n)n^{-3/4}|V_n|
\le
\left(\sum_{n\asymp N}\tau(n)^2n^{-3/2}\right)^{1/2}
\mathcal M(N,K)^{1/2}.
\]

Using the standard divisor-square mean bound

\[
\sum_{n\le x}\tau(n)^2\ll x\log^3(2x),
\]

the first factor is

\[
\ll N^{-1/4}\log^{3/2}(2N),
\]

while the mean-square hypothesis makes the second

\[
\ll_\varepsilon N^{1/2}K^{1/4+\varepsilon}.
\]

Hence one dyadic block contributes

\[
\ll_\varepsilon K^{1/4+\varepsilon}N^{1/4},
\]

and summing dyadically to `N<=K` gives

\[
\ll_\varepsilon K^{1/2+\varepsilon}.
\]

After the outer Voronoi factor `K^(1/2)=X^(1/4)`, this is

\[
\boxed{O_\varepsilon(K^{1+\varepsilon})
=O_\varepsilon(X^{1/2+\varepsilon}).}
\]

Thus the mean-square criterion is enough; uniform control in n is not required.

Classification:

`VORONOI_MOBIUS_MEAN_SQUARE_SUFFICIENCY`.

## 3. Exact random-sign false control

Replace Möbius signs by independent Rademacher variables `epsilon_d in {+1,-1}` and set

\[
V_n^{\rm rand}(K)
=\sum_{d\le K}\varepsilon_d d^{-1/4}
 e\!\left(2K\sqrt{n/d}\right).
\]

Independence gives exactly

\[
\mathbb E_\varepsilon |V_n^{\rm rand}(K)|^2
=\sum_{d\le K}d^{-1/2}
=2K^{1/2}+O(1).
\]

Therefore

\[
\boxed{
\mathbb E_\varepsilon
\sum_{N<n\le2N}|V_n^{\rm rand}(K)|^2
\sim2N K^{1/2}.
}
\]

So the exponent pair `N K^(1/2)` and pointwise RMS scale `K^(1/4)` are generic coefficient-energy scales, not RH-specific phenomena.

Permanent guard:

`RECIPROCAL_PHASE_RANDOM_ENERGY_FALSE_CONTROL` — observing K^(1/4)-scale values or N K^(1/2)-scale mean square numerically is not evidence for RH unless the proposed mechanism distinguishes the arithmetic Möbius sequence from Rademacher controls.

## 4. Finite numerical audit

Direct computation used `X=K^2` and all `1<=n<=K`.

At `K=10000`:

### Möbius coefficients
- max |V_n| / K^(1/4): about `3.648`;
- median: about `0.922`;
- 95th percentile: about `1.925`.

For all dyadic n-bands, the ratio

\[
\frac{\sum |V_n|^2}{(\#\text{band})K^{1/2}}
\]

lay approximately between `0.76` and `1.42`.

### All-positive coefficients d^(-1/4)
- max / K^(1/4): about `4.444`;
- median: about `1.212`;
- 95th percentile: about `2.443`;
- dyadic mean-square ratios rose from small finite-band values to roughly `2.33` in the top band, still on the same power scale.

### Eight random-sign controls
- max / K^(1/4): approximately `4.07` to `5.01`;
- for moderate and large dyadic bands, normalized mean-square ratios clustered near `1.9`--`2.0`, matching the exact expectation `2`.

These are finite diagnostics only.

## 5. Double-large-sieve geometry

The phase is separable:

\[
2K\sqrt n\,d^{-1/2}=x_n y_d,
\qquad
x_n=2K\sqrt n,
\quad
y_d=d^{-1/2}.
\]

Thus Bombieri--Iwaniec's double large sieve is structurally applicable.

On dyadic blocks

\[
n\asymp N,\qquad d\asymp D,
\]

the spacings are

\[
x_{n+1}-x_n\asymp\frac K{\sqrt N},
\]

and

\[
y_d-y_{d+1}\asymp D^{-3/2}.
\]

The n-window has effective x-span of order `K sqrt(N)`. Adjacent d-frequencies are therefore resolved only when

\[
K\sqrt N\,D^{-3/2}\gtrsim1,
\]

i.e.

\[
\boxed{
D\lesssim (K\sqrt N)^{2/3}.
}
\]

This identifies a natural **resolved region** and an **unresolved high-d / low-n corner**.

## 6. What the raw double large sieve loses

Using the standard one-dimensional double-large-sieve neighbour counts on a `(N,D)` block gives schematically

\[
\|T_{N,D}\|_{2\to2}^2
\lesssim
K\sqrt N + D^{3/2}
\]

up to lower-order/logarithmic factors. The first term is compatible with the desired Voronoi contribution after dyadic Cauchy--Schwarz. The second term becomes dominant precisely beyond

\[
D\sim(K\sqrt N)^{2/3}.
\]

Hence the direct spacing inequality solves the resolved sector but not the unresolved corner.

Classification:

`RECIPROCAL_PHASE_DOUBLE_SIEVE_RESOLUTION_BARRIER`.

This is a method-resolution statement, not a proof that no sharper large-sieve or oscillatory argument can work.

## 7. Local Taylor form in the unresolved corner

For `d=D+h` with `D~K`,

\[
2K\sqrt n\,(D+h)^{-1/2}
=
2K\sqrt n\,D^{-1/2}
-K\sqrt n\,D^{-3/2}h
+\frac34K\sqrt n\,D^{-5/2}h^2
+\cdots.
\]

At `D~K`, a linearization block may have length up to roughly

\[
\boxed{
H_{\rm lin}
\asymp K^{3/4}n^{-1/4}
}
\]

before the quadratic phase changes by order one.

For `n<=K^(1/2)`, this satisfies

\[
H_{\rm lin}\gtrsim K^{5/8},
\]

which intersects the classical Zhan short-interval range for Möbius twisted by a linear phase. However those theorems provide logarithmic savings of the form `H log^{-A} H`, not square-root cancellation. Applying them blockwise by triangle inequality therefore does **not** close the required K^(1/4) / mean-square target.

Classification:

`SHORT_INTERVAL_LOG_SAVING_INSUFFICIENCY`.

## 8. Current live subproblem

The small-d route is now reduced more sharply:

1. Resolved sector `D <= (K sqrt(N))^(2/3)`: standard spacing/double-large-sieve machinery is structurally adequate at the target power scale.
2. Unresolved sector `D > (K sqrt(N))^(2/3)`: needs an additional mechanism that uses phase curvature, refined spacing, Möbius bilinear structure, or a stronger mean-value argument.
3. The observed K^(1/4) scale itself is generic and must not be treated as evidence for RH.

The next worthwhile question is therefore whether the unresolved sector admits a second transformation (B-process / exponent-pair / bilinear Möbius decomposition) that restores diagonal-scale mean square without importing an RH-level Mertens estimate.
