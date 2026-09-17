# Voronoi–Möbius Vaughan Type-I / Type-II reduction — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Vaughan decomposition for Möbius: STANDARD.
- Natural decomposition parameter tied to reciprocal-phase resolution: DERIVED.
- Type I branch: CLOSED at the required square-root power (up to logarithms).
- Type II branch: reduced to a multivariate monomial exponential mean-value problem.
- Existing Baker–Weingartner / multivariate monomial literature: DIRECTLY RELEVANT functional class, but theorem-level applicability to the exact critical target not yet verified.

## 1. Reciprocal phase on one dyadic d-block

Fix a Voronoi n-scale `n~N` and an arithmetic variable block `r~D` (we use `r` here to avoid conflict with the outer Voronoi index). Put

\[
A:=2K\sqrt N
\]

at scale level and consider

\[
f(r)=e(A r^{-1/2}).
\]

The reciprocal-resolution length found earlier is

\[
\boxed{
H:=\frac{D^{3/2}}{K\sqrt N}
\asymp\frac{D^{3/2}}{A}.
}
\]

In the unresolved sector one has

\[
1\lesssim H\lesssim D^{1/2}.
\]

Equivalently the total oscillation parameter is

\[
\boxed{
F:=\frac{A}{\sqrt D}\asymp\frac{D}{H},
}
\]

so the unresolved sector still has at least `F >= sqrt(D)` oscillations across the full d-block.

## 2. Möbius Vaughan decomposition

Use the standard Vaughan decomposition for Möbius (as in Green--Tao's quadratic-uniformity treatment). For parameters `U,V` with `UV<=D`, a sum

\[
\sum_{D<r\le2D}\mu(r)f(r)
\]

splits into a Type I expression with composite divisor variable up to `UV` and a Type II expression in a factorization `r=ab` whose factors lie beyond the chosen truncation scales.

Choose

\[
\boxed{U=V=H^{1/2}.}
\]

Then

\[
UV=H\le D^{1/2}<D,
\]

so the decomposition is admissible.

This choice is not arbitrary:
- Type I composite divisor `d` satisfies `d<=H`, exactly the low-derivative region;
- Type II has both factor variables beyond roughly `sqrt(H)`, exposing the multiplicatively separable reciprocal phase.

## 3. Type I is at the required power

The Type I inner sum has the shape

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

On `w~D/d`, this is

\[
\asymp\frac{A d}{D^{3/2}}
\asymp\frac dH.
\]

More precisely, on a standard dyadic w-interval and for `d<=H`, its magnitude stays below a fixed constant <1 and is bounded below by a constant multiple of `d/H`. Thus there is no nonzero-integer derivative resonance, and the Kusmin--Landau / first-derivative estimate gives

\[
\boxed{|S_d|\ll H/d.}
\]

The Vaughan Type-I coefficient

\[
a_d=\sum_{bc=d,\ b\le U,\ c\le V}\mu(b)\mu(c)
\]

satisfies the crude but sufficient bound

\[
|a_d|\le\tau(d).
\]

Hence the unweighted Type-I contribution obeys

\[
|T_I|
\ll H\sum_{d\le H}\frac{\tau(d)}d
\ll H\log^2(2H).
\]

Since `H<=sqrt(D)`,

\[
\boxed{
T_I\ll D^{1/2}\log^2 D.
}
\]

Restoring the slowly varying Voronoi coefficient `r^(-1/4)~D^(-1/4)` gives

\[
\boxed{
T_I^{\rm weighted}\ll D^{1/4}\log^2D,
}
\]

which is the desired square-root-energy pointwise power for this dyadic block.

Classification:

`RECIPROCAL_VAUGHAN_TYPEI_CLOSED`.

## 4. Exact Type-II phase factorization

The Type-II phase is

\[
e\!\left(A(ab)^{-1/2}\right)
=e\!\left(Aa^{-1/2}b^{-1/2}\right).
\]

Thus it is a bilinear monomial phase with exponents

\[
\boxed{\alpha=\beta=-1/2.}
\]

After a rectangular Cauchy differencing, the four-point phase difference factorizes **exactly**:

\[
\begin{aligned}
&(ab)^{-1/2}-(a'b)^{-1/2}-(ab')^{-1/2}+(a'b')^{-1/2}\\
&\qquad=
(a^{-1/2}-a'^{-1/2})
(b^{-1/2}-b'^{-1/2}).
\end{aligned}
\]

This exact product structure is the reason the Type-II branch belongs naturally to double-large-sieve / bilinear-monomial theory rather than to a generic Chowla-correlation treatment.

## 5. Correct oscillation parameter

On factor blocks

\[
a\asymp M,\qquad b\asymp L,\qquad ML\asymp D,
\]

the phase may be normalized as

\[
A a^{-1/2}b^{-1/2}
=
F
\frac{a^{-1/2}b^{-1/2}}{M^{-1/2}L^{-1/2}},
\]

with

\[
\boxed{
F=A D^{-1/2}\asymp D/H.
}
\]

Since `H<=sqrt(D)`,

\[
F\gtrsim D^{1/2}.
\]

Therefore the Type-II boxes are not low-frequency perturbations. They sit in a genuinely oscillatory monomial regime.

## 6. Why the outer Voronoi mean square must be retained

A pointwise arbitrary-coefficient Type-II estimate is stronger than needed and incurs diagonal/Cauchy losses. The actual target is the dyadic outer mean square.

Ignoring divisor-bounded logarithmic factors and restoring factor coefficients schematically, the required unweighted Type-II target is

\[
\boxed{
\sum_{N<n\le2N}
\left|
\sum_{\substack{ab\asymp D\\ a,b\gtrsim H^{1/2}}}
\alpha_a\beta_b
 e\!\left(2K\sqrt n\,a^{-1/2}b^{-1/2}\right)
\right|^2
\ll_\varepsilon
N D^{1+\varepsilon}.
}
\]

Multiplying by the squared Voronoi weight `D^(-1/2)` then gives the desired

\[
N D^{1/2+\varepsilon}
\]

contribution.

The phase is now the three-variable monomial

\[
\boxed{n^{1/2}a^{-1/2}b^{-1/2}.}
\]

## 7. Literature alignment

Baker--Weingartner (2013), *Some applications of the double large sieve*, explicitly studies arbitrary-coefficient bilinear sums of the form

\[
\sum_{m\sim M}\sum_{n\sim N}a_m b_n
 e\!\left(
F\frac{m^\alpha n^\beta}{M^\alpha N^\beta}
\right),
\]

which is exactly the functional class of the present Type-II phase with `alpha=beta=-1/2` at the formal level.

There is also literature on multivariate exponential sums with monomials (for example Shparlinski) that is structurally relevant once the outer Voronoi n-average is retained.

However, the present audit has not yet verified from the full theorem statements that:
1. negative exponents `-1/2,-1/2` satisfy every nondegeneracy/range hypothesis used in the sharpest published estimates; and
2. those estimates reach the exact critical target `ND^(1+epsilon)` uniformly in the parameter range `F=D/H`, `sqrt(D)<=F<=D`.

Therefore no theorem is imported yet and no novelty is claimed.

Classification:

`TYPEII_MONOMIAL_LITERATURE_MATCH_PENDING`.

## 8. Consequence

The small-d reciprocal-phase module has now advanced from one undifferentiated exponential-sum problem to:

- **Type I:** closed at the required power by a direct first-derivative estimate;
- **Type II:** the only live analytic core, with exact monomial factorization and a clearly specified three-variable mean-square target.

This is materially narrower than the previous `unresolved high-d/low-n corner` formulation.

Next audit priority:
1. obtain the precise Baker--Weingartner theorem statement and test `alpha=beta=-1/2`, `F=D/H`;
2. if its range or exponent misses the target, quantify the exact deficit;
3. test whether the outer n-average upgrades the two-variable bound through multivariate monomial estimates;
4. only if those standard tools fail should a new Type-II estimate be proposed.
