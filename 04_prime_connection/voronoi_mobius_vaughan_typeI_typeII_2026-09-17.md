# Voronoi–Möbius Vaughan Type-I / Type-II reduction — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Vaughan decomposition for Möbius: STANDARD.
- Natural decomposition parameter tied to reciprocal-phase resolution: DERIVED.
- Type I branch: CLOSED at the required square-root power up to polylogarithms, with an endpoint-resonance correction.
- Type II branch: reduced to a real bilinear/three-variable monomial exponential mean-value problem.
- Baker–Weingartner real bilinear monomial literature: DIRECTLY RELEVANT functional class; available published-style bounds are not strong enough pointwise for the present critical target.
- Shparlinski 2014 multivariate monomial paper: FINITE-FIELD additive-character setting; comparison only, not a directly applicable theorem here.

## 1. Reciprocal phase on one dyadic arithmetic block

Fix a Voronoi scale `n~N` and an arithmetic variable block `r~D`. Put, at scale level,

\[
A:=2K\sqrt N,
\qquad
f(r)=e(A r^{-1/2}).
\]

The reciprocal-resolution length is

\[
\boxed{
H:=\frac{D^{3/2}}{K\sqrt N}
\asymp\frac{D^{3/2}}{A}.
}
\]

In the unresolved sector,

\[
1\lesssim H\lesssim D^{1/2}.
\]

The total oscillation parameter is

\[
\boxed{
F:=\frac{A}{\sqrt D}\asymp\frac{D}{H},
}
\]

hence `F >= sqrt(D)` in this sector.

## 2. Möbius Vaughan decomposition and the natural cutoff

Use the standard Vaughan decomposition for the Möbius function (for example the form used by Green–Tao). For parameters `U,V` with `UV<=D`,

\[
\sum_{D<r\le2D}\mu(r)f(r)
\]

splits into a Type I expression with composite divisor variable up to `UV`, plus a Type II factorization term.

Choose

\[
\boxed{U=V=H^{1/2}.}
\]

Then `UV=H<=sqrt(D)`, so the decomposition is admissible. The choice aligns the Type-I cutoff with the reciprocal derivative threshold.

## 3. Type I: ordinary region and endpoint resonance

The inner Type-I sum has the form

\[
S_d
=\sum_{w\asymp D/d}
 e\!\left(A(dw)^{-1/2}\right),
\qquad d\le H.
\]

For fixed d,

\[
\left|\frac{d}{dw}A d^{-1/2}w^{-1/2}\right|
=\frac{A}{2}d^{-1/2}w^{-3/2}.
\]

On `w~D/d`, the derivative is of scale

\[
\asymp\frac dH.
\]

For `d` bounded away from the upper endpoint `H`, the derivative remains separated from every nonzero integer and the first-derivative/Kusmin–Landau estimate gives the expected

\[
|S_d|\ll H/d
\]

(up to absolute endpoint constants).

One must **not** assert uniform nonresonance all the way to `d=H`: near the lower endpoint of the w-block and `d≈H`, the derivative may approach the integer `1`. This is a thin endpoint-resonance layer.

In that layer, the second derivative satisfies at scale

\[
|f''(w)|\asymp\frac{d^2}{HD}.
\]

Combining a second-derivative estimate in the near-resonant d-range with the first-derivative estimate away from it yields, after summing d and allowing divisor weights,

\[
\boxed{
\sum_{d\le H}|a_d||S_d|
\ll H\,\log^{O(1)}D,
}
\]

where

\[
a_d=\sum_{bc=d,\ b\le U,\ c\le V}\mu(b)\mu(c),
\qquad |a_d|\le\tau(d).
\]

Thus

\[
\boxed{
T_I\ll H\log^{O(1)}D
\ll D^{1/2}\log^{O(1)}D.
}
\]

Restoring the slowly varying Voronoi coefficient `r^{-1/4}~D^{-1/4}` gives

\[
\boxed{
T_I^{\rm weighted}
\ll D^{1/4}\log^{O(1)}D,
}
\]

which is the required power scale.

Classification:

`RECIPROCAL_VAUGHAN_TYPEI_CLOSED`.

Permanent correction:

`TYPEI_ENDPOINT_RESONANCE_GUARD` — the Type-I closure uses a first/second derivative split near `d≈H`; do not state that the first derivative is uniformly separated from every integer for all `d<=H`.

## 4. Exact Type-II phase factorization

The Type-II phase is

\[
e\!\left(A(ab)^{-1/2}\right)
=e\!\left(Aa^{-1/2}b^{-1/2}\right).
\]

Thus it is a real bilinear monomial phase with

\[
\boxed{\alpha=\beta=-1/2.}
\]

The rectangular four-point difference factorizes exactly:

\[
\begin{aligned}
&(ab)^{-1/2}-(a'b)^{-1/2}-(ab')^{-1/2}+(a'b')^{-1/2}\\
&\qquad=
(a^{-1/2}-a'^{-1/2})
(b^{-1/2}-b'^{-1/2}).
\end{aligned}
\]

Hence this branch is naturally a bilinear-monomial / double-large-sieve problem rather than a generic Chowla problem.

## 5. Correct normalized oscillation parameter

On

\[
a\asymp M,
\qquad b\asymp L,
\qquad ML\asymp D,
\]

write

\[
A a^{-1/2}b^{-1/2}
=
F\frac{a^{-1/2}b^{-1/2}}{M^{-1/2}L^{-1/2}},
\]

where

\[
\boxed{F=A D^{-1/2}\asymp D/H.}
\]

Thus `sqrt(D) <= F <= D` throughout the unresolved sector.

## 6. Two-variable published bounds are not enough pointwise

Baker–Weingartner (2013), *Some applications of the double large sieve*, studies real bilinear monomial sums

\[
\sum_{m\sim M}\sum_{n\sim L}a_m b_n
 e\!\left(
F\frac{m^\alpha n^\beta}{M^\alpha L^\beta}
\right),
\qquad |a_m|,|b_n|\le1.
\]

A later paper quoting their Theorem 1 records bounds containing terms of the shape

\[
M^{7/8}L^{13/16}F^{1/16},
\quad
M^{93/104}L^{23/26}F^{1/26},
\]

\[
M^{467/512}L^{65/64}F^{-1/128},
\quad
M^{65/72}L,
\]

in its applicable parameter regime.

Even under the optimistic balanced test `M~L~D^{1/2}` and the smallest present oscillation `F~D^{1/2}`, the first displayed term is already of order about

\[
D^{7/8},
\]

far above the pointwise square-root target `D^{1/2+epsilon}`. Hence importing the classical two-variable theorem pointwise cannot close the present branch.

This is a **scale comparison**, not a claim that every refinement of Baker–Weingartner fails.

Classification:

`TYPEII_TWO_VARIABLE_POINTWISE_DEFICIT`.

## 7. Why the outer Voronoi mean square must be retained

The actual problem does not require a pointwise `D^{1/2}` bound for every outer n. The target is

\[
\boxed{
\sum_{N<n\le2N}
\left|
\sum_{\substack{ab\asymp D\\a,b\gtrsim H^{1/2}}}
\alpha_a\beta_b
 e\!\left(2K\sqrt n\,a^{-1/2}b^{-1/2}\right)
\right|^2
\ll_\varepsilon
ND^{1+\varepsilon}.
}
\]

After restoring the squared Voronoi weight `D^{-1/2}`, this becomes the desired `ND^{1/2+epsilon}` contribution.

The phase is the real three-variable monomial

\[
\boxed{n^{1/2}a^{-1/2}b^{-1/2}.}
\]

Therefore the live analytic object is a **three-variable real monomial mean square**, not the already-audited two-variable pointwise sum.

## 8. Literature boundary correction

Shparlinski (2014), *Multiple exponential and character sums with monomials*, studies additive characters over finite fields `F_p`; negative exponents there are interpreted via modular inversion. It is useful as a methodological comparison for multivariable monomial sums, but it is **not** a theorem directly applicable to the real phase above.

Accordingly the direct literature match retained here is Baker–Weingartner's real bilinear-monomial framework. A theorem-level source for the exact real three-variable mean-square target has not yet been identified in the present search.

No novelty claim is made.

Classification:

`REAL_THREE_VARIABLE_MONOMIAL_LITERATURE_OPEN`.

## 9. Current consequence

The reciprocal-phase branch is now split as follows:

- **Type I:** closed at the required power, with endpoint resonance handled separately;
- **Type II two-variable pointwise:** known-style double-large-sieve estimates miss the critical power;
- **Type II with outer n-average retained:** still OPEN and now the unique analytic core of this branch.

Next priority:
1. search specifically for real three-variable monomial mean-value estimates with exponents `(1/2,-1/2,-1/2)`;
2. derive a direct Cauchy/double-large-sieve bound for the full n,a,b mean square and quantify its exact deficit;
3. test whether the exact rectangular factorization removes that deficit before introducing any new conjectural input.
