# Mellin / long-Möbius Dirichlet-polynomial re-entry audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Candidate audited: use Mellin-Fourier separation of the reciprocal product phase to convert the hard Type-II block into a product of Möbius Dirichlet polynomials.
- Exact reduction: VALID.
- Generic mean-value closure: INSUFFICIENT in the critical unbalanced block.
- Structural conclusion: the needed long-polynomial mean square re-enters the same short-shift weighted Möbius correlation that appeared in the far-resonance audit.

## 1. Mellin separation of the product phase
On smooth dyadic blocks write

\[
d=Mx,\qquad w=Ly,\qquad D=ML,
\]

and let

\[
G_X(u)=W(u)e(Xu^{-1/2}),
\qquad u=xy,
\qquad X\asymp \frac{K\sqrt n}{\sqrt D}.
\]

Fourier transform in `log u` gives

\[
G_X(xy)=\frac1{2\pi}\int_{\mathbb R}\widehat G_X(t)x^{it}y^{it}\,dt.
\]

Hence a product-phase bilinear block becomes

\[
T=\frac1{2\pi}\int \widehat G_X(t)A_M(t)B_L(t)\,dt,
\]

where

\[
A_M(t)=\sum_{d\asymp M} a_d d^{it},
\qquad
B_L(t)=\sum_{w\asymp L} b_w w^{it}.
\]

At the Vaughan edge, `a_d=mu(d)` and `b_w=mu(w)`.

## 2. Stationary Mellin band
For `u` in a fixed compact dyadic interval, the `log u` phase has derivative and second derivative of size `X`. Stationary phase therefore places the main Mellin mass in a band

\[
|t|\asymp X
\]

of length `asymp X`, with pointwise transform scale

\[
|\widehat G_X(t)|\asymp X^{-1/2}
\]

inside the stationary region, up to smooth cutoffs and harmless tails. Plancherel gives total L2 mass `O(1)`.

## 3. Critical unbalanced scale
At

\[
D=K,\qquad n\asymp1,
\]

one has

\[
X\asymp K^{1/2}.
\]

For the most unbalanced natural edge block,

\[
M\asymp K^{1/4},
\qquad
L\asymp K^{3/4},
\]

so

\[
X=L^{2/3}.
\]

The short polynomial `A_M` lies below the Mellin-window length, and the ordinary Dirichlet-polynomial mean-value theorem controls it at diagonal scale.

To make Mellin Cauchy reach the desired `K^(3/4+epsilon)` Type-II scale, the long Möbius polynomial would need a diagonal-size estimate of the form

\[
\boxed{
\int_{I_X}
\left|
\sum_{w\asymp L}\mu(w)w^{it}
\right|^2dt
\ll_\varepsilon
X L^{1+\varepsilon},
\qquad |I_X|\asymp X=L^{2/3}.
}
\]

After the dyadic normalization `w~L`, this is equivalent in power scale to a critical-line Möbius Dirichlet polynomial of length `L` averaged over a `t` interval of length `L^(2/3)`.

Classification:

`LONG_MOBIUS_DIRICHLET_POLYNOMIAL_DIAGONAL_TARGET`.

## 4. Why the ordinary mean-value theorem is insufficient
For a general Dirichlet polynomial of length `L`,

\[
\int_I |B_L(t)|^2dt
\ll (|I|+L)\sum_{w\asymp L}|b_w|^2.
\]

Since `X=L^(2/3)<L` and `sum |mu(w)|^2~L`, this gives only

\[
\ll L^2,
\]

whereas the required diagonal scale is

\[
XL=L^{5/3}.
\]

Thus a generic mean-value theorem misses by `L^(1/3)` at the squared level.

## 5. Exact correlation re-entry
Insert a smooth `t` weight `W((t-T)/X)`. Expanding the square gives

\[
\begin{aligned}
I
&=\int W\!\left(\frac{t-T}{X}\right)
\left|\sum_{w\asymp L}\mu(w)w^{it}\right|^2dt\\
&=X\sum_{m,n\asymp L}
\mu(m)\mu(n)
 e^{iT\log(m/n)}
\widehat W\!\left(X\log\frac mn\right).
\end{aligned}
\]

Because `hat W` decays rapidly, only

\[
|m-n|\lesssim \frac LX
\]

contributes materially. Put

\[
Y:=\frac LX.
\]

At the critical block,

\[
\boxed{Y=L^{1/3}.}
\]

Writing `m=n+h`, the off-diagonal is therefore

\[
X\sum_{|h|\lesssim Y}
\sum_{n\asymp L}
\mu(n+h)\mu(n)
 e^{iT\log(1+h/n)}
\widehat W\!\left(X\log(1+h/n)\right).
\]

For `h<<L`, the oscillatory variable is naturally `h/Y`. This is a **smooth weighted average of binary Möbius correlations over shifts `|h|lesssim L^(1/3)`**.

## 6. Literature position
Goldston--Gonek's long Dirichlet-polynomial mean-value theory explicitly shows that when the polynomial is longer than the integration range, off-diagonal coefficient-correlation functions become the determining input.

Thus the Mellin formulation does not remove the arithmetic obstruction; it identifies it in a standard long-polynomial language.

Modern short-interval/Fourier-uniformity theorems provide strong average/logarithmic cancellation for Möbius, but the present diagonal-scale long-polynomial estimate is not obtained merely by inserting the ordinary mean-value theorem.

Classification:

`MELLIN_LONG_POLYNOMIAL_CORRELATION_REENTRY`.

## 7. Relation to the far-resonance audit
The scales match the previous reciprocal B-process frontier:

- reciprocal far shift: `h >= H` after one factor differencing;
- Mellin long-polynomial resolution: `h <= L/X` in the product variable;
- at the extreme edge `X=L^(2/3)`, the intrinsic correlation width is `L^(1/3)`.

Both descriptions show that the missing information is not generic phase spacing but a structured weighted average of Möbius two-point correlations.

## 8. Consequence
Do not treat Mellin separation itself as an independent RH mechanism.

Its useful output is a cleaner target:

\[
\boxed{
\text{diagonal-scale short-}t\text{ mean square for a long Möbius Dirichlet polynomial}
}
\]

or equivalently the associated smooth shift-correlation bound.

The next worthwhile audit is whether known averaged-Chowla / Matomäki--Radziwill--Tao results are quantitatively strong enough for this **specific smooth signed shift average**, rather than for the absolute sum of fixed-shift correlations.
