# Two-variable monomial bilinear benchmark audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Purpose: compare the current fixed-`n` reciprocal Type-II block against theorem-level arbitrary-coefficient bilinear monomial estimates.
- Conclusion: strong classical bilinear estimates are directly relevant, but even the sharper benchmark remains above the required `K^(3/4+epsilon)` endpoint scale.

## 1. Fixed-`n` Type-II model
At the extreme low outer block `n~1`, `D~K`, write

\[
T=\sum_{m\asymp M}\alpha_m
\sum_{n\asymp N}\beta_n
 e\!\left(X(m/M)^{-1/2}(n/N)^{-1/2}\right),
\]

with

\[
MN=K,
\qquad
X\asymp K^{1/2},
\qquad
|\alpha_m|,|\beta_n|\lesssim K^{o(1)}.
\]

The relaxed bounded-outer-index target is

\[
\boxed{|T|\ll K^{3/4+\varepsilon}.}
\]

## 2. Fouvry–Iwaniec / Robert–Sargos style benchmark
A standard strong bilinear monomial bound recorded in Kowalski–Robert–Wu has the shape

\[
S(M,N)
\ll
\left(
(XM^6N^6)^{1/8}
+M^{1/2}N
+MN^{3/4}
+X^{-1/2}MN
\right)(MN)^\varepsilon
\]

for nondegenerate real monomial exponents.

With `MN=K`, `X=K^(1/2)`, the first and last terms become

\[
K^{13/16},
\qquad
K^{3/4}.
\]

Optimizing the middle terms over a split `M=K^a`, `N=K^(1-a)` still leaves an exponent at least about `5/6` in the relevant orientation. Thus this benchmark does not reach `3/4`.

## 3. Sharper recorded double-sum benchmark
A sharper double-exponential-sum estimate recorded in later literature has terms

\[
(XM^3N^4)^{1/5}
+(X^4M^{10}N^{11})^{1/16}
+(XM^7N^{10})^{1/11}
+MN^{1/2}
+X^{-1/2}MN.
\]

At the balanced point

\[
M=N=K^{1/2},
\qquad X=K^{1/2},
\]

the corresponding powers are

\[
K^{4/5},
\quad K^{25/32},
\quad K^{9/11},
\quad K^{3/4},
\quad K^{3/4}.
\]

The dominant exponent is therefore

\[
\boxed{9/11=0.81818\ldots}
\]

rather than the required

\[
3/4=0.75.
\]

The remaining polynomial deficit is

\[
K^{9/11-3/4}=K^{3/44}.
\]

Classification:

`ARBITRARY_COEFFICIENT_REAL_MONOMIAL_BILINEAR_BOUND_INSUFFICIENT_AT_3_4_SCALE`.

## 4. Meaning
This is a useful narrowing.

The phase class itself is well covered by established bilinear exponential-sum technology. The missing saving is not plausibly obtained by merely citing a generic monomial estimate with bounded coefficients.

The present arithmetic coefficients contain information absent from those theorems:

1. one factor is an actual Möbius sequence;
2. the other Vaughan coefficient is a restricted Möbius-divisor convolution;
3. the coefficient pair is linked to the same product variable that generated the reciprocal phase;
4. in the full problem there is also an outer `n` mean value.

A viable improvement must preserve at least one of these structures rather than replacing both coefficient sequences by arbitrary bounded weights.

## 5. Current frontier after this audit
For bounded `Q`, the near-shift cell is already at the relaxed target scale by first-derivative cancellation.

The remaining hard contribution is the far-resonant / long-Möbius sector. Existing arbitrary-coefficient bilinear monomial estimates reduce the deficit but do not remove it.

Therefore the next theorem-search / derivation should target a **coefficient-sensitive bilinear estimate**, not another generic spacing theorem.

References retained in the literature ledger:
- Kowalski–Robert–Wu, bilinear/type-II monomial estimates (Proposition 5 in the retained source).
- Related sharper double-exponential-sum estimates recorded in the monomial literature and used in later analytic-number-theory applications.
