# Very-small-Q weight relaxation / DLS barrier audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Previous uniform dyadic mean-square target `M(Q,K) << Q K^(1/2+eps)`: sufficient but stronger than necessary for very small `Q`.
- New weight-adapted sufficient target: `M(Q,K) << K^(1+eps) Q^(1/2)` is enough blockwise, up to logarithms.
- At the hardest reciprocal block `D~K`, this relaxes the unweighted Type-II mean-square target by the factor `H=sqrt(K/Q)`.
- Nevertheless the previously derived one-sided Cauchy + double-large-sieve estimate still misses even this relaxed target by at least `K^(1/4)` uniformly in the balanced orientation.
- Therefore the subpolynomial / bounded-`Q` edge is not closed by simply exploiting the outer `n^(-3/4)` weight inside the existing DLS architecture.

## 1. Original weighted Voronoi block
The small-`d` Voronoi contribution has, up to harmless constants and divisor/log factors,

\[
K^{1/2}
\sum_{n\le K}\tau(n)n^{-3/4}V_n(K),
\]

where

\[
V_n(K)=\sum_{d\le K}\mu(d)d^{-1/4}e\!\left(2K\sqrt{n/d}\right).
\]

For a dyadic outer block `Q<n<=2Q`, put

\[
\mathcal M(Q,K):=\sum_{Q<n\le2Q}|V_n(K)|^2.
\]

Cauchy--Schwarz gives

\[
\sum_{n\asymp Q}\tau(n)n^{-3/4}|V_n|
\le
\left(\sum_{n\asymp Q}\tau(n)^2n^{-3/2}\right)^{1/2}
\mathcal M(Q,K)^{1/2}.
\]

Using

\[
\sum_{n\asymp Q}\tau(n)^2n^{-3/2}
\ll Q^{-1/2}\log^3(2Q),
\]

the dyadic block is bounded by

\[
\ll Q^{-1/4}\log^{3/2}(2Q)\,\mathcal M(Q,K)^{1/2}.
\]

## 2. Weight-adapted sufficient target
It is enough for each dyadic block to contribute `O(K^(1/2+eps))` before the outer `K^(1/2)` factor; the `O(log K)` number of dyadic blocks is absorbed into `K^eps`.

Therefore it suffices that

\[
Q^{-1/4}\mathcal M(Q,K)^{1/2}
\ll_\varepsilon K^{1/2+\varepsilon}.
\]

Equivalently,

\[
\boxed{
\mathcal M(Q,K)
\ll_\varepsilon
K^{1+\varepsilon}Q^{1/2}.
}
\]

Classification:

`WEIGHT_ADAPTED_SMALL_Q_MEAN_SQUARE_SUFFICIENCY`.

This is weaker than the previously used random-energy/diagonal target

\[
\mathcal M(Q,K)\ll QK^{1/2+\varepsilon}
\]

by the factor

\[
\boxed{
\frac{KQ^{1/2}}{QK^{1/2}}
=\sqrt{\frac KQ}.
}
\]

At `Q=1`, for example, the relaxed criterion allows `|V_n|` as large as `K^(1/2+eps)` rather than `K^(1/4+eps)`.

Thus the very-small-`Q` blocks do **not** need random-sign square-root energy individually.

## 3. Translation to the hardest dyadic d-block
On a dyadic `d~D` block write schematically

\[
V_{n,D}=D^{-1/4}T_n,
\]

where `T_n` is the corresponding unweighted/divisor-bounded Type-II exponential sum after factor decomposition.

Then

\[
\sum_{n\asymp Q}|V_{n,D}|^2
\asymp D^{-1/2}\mathcal E(Q;M,L),
\]

where

\[
\mathcal E(Q;M,L)=\sum_{n\asymp Q}|T_n|^2,
\qquad ML\asymp D.
\]

For the hardest high-`d` block `D~K`, the relaxed condition becomes

\[
\boxed{
\mathcal E(Q;M,L)
\ll_\varepsilon
K^{3/2+\varepsilon}Q^{1/2}.
}
\]

The old unweighted target was

\[
\mathcal E\ll QK^{1+\varepsilon}.
\]

Their ratio is

\[
\sqrt{\frac KQ}.
\]

At `D=K`, the reciprocal resolution is

\[
H=\frac{D^{3/2}}{K\sqrt Q}
=\sqrt{\frac KQ},
\]

so the outer Voronoi weight allows exactly an additional factor

\[
\boxed{H}
\]

relative to the old Type-II target.

## 4. Re-test of one-sided Cauchy + double large sieve
The previous sharp spacing calculation gave, relative to the old target `QML=QK`, the loss factor

\[
R_M^2
=
\left(M^2+\frac{FM}{Q}\right)
\left(1+\frac{L^2}{F}\right),
\]

where

\[
ML=K,
\qquad
F=K/H,
\qquad
Q=K/H^2.
\]

Substituting gives the exact simplified form

\[
\boxed{
R_M^2
=M(M+H)\left(1+\frac{KH}{M^2}\right).
}
\]

Because the relaxed target is larger than the old target by `H`, this proof architecture would now need only

\[
R_M\ll H K^\varepsilon.
\]

At first sight this appears capable of rescuing the very-small-`Q` range.

## 5. Uniform K^(1/4) residual deficit
Orient the one-sided Cauchy step along the smaller Type-II factor, so without loss of generality

\[
M\le L,
\qquad ML=K,
\qquad M\le K^{1/2}.
\]

From the exact expression,

\[
M+H\ge H
\]

and

\[
1+\frac{KH}{M^2}\ge\frac{KH}{M^2}.
\]

Hence

\[
R_M^2
\ge
M H\cdot\frac{KH}{M^2}
=
\frac{KH^2}{M}.
\]

Since `M<=K^(1/2)`,

\[
\boxed{
R_M^2\ge K^{1/2}H^2,
\qquad
R_M\ge K^{1/4}H.
}
\]

But the weight-adapted relaxed target only permits the factor `H`.

Therefore even after using the full outer `n^(-3/4)` slack, the one-sided Cauchy + optimal spacing + double-large-sieve route still loses at least

\[
\boxed{K^{1/4}}
\]

on the hardest `D~K` block.

Classification:

`WEIGHT_RELAXED_TYPEII_DLS_K_QUARTER_BARRIER`.

This lower bound concerns the output scale of the specified proof architecture, not the true Type-II mean square.

## 6. Consequence for bounded and subpolynomial Q
At `Q=1`,

\[
H=K^{1/2}.
\]

The relaxed outer-weight target permits an `H=K^(1/2)` loss relative to the original diagonal target. The DLS architecture, however, carries at least

\[
K^{1/4}H=K^{3/4}
\]

relative loss.

So even the maximally relaxed bounded-`Q` endpoint is missed by `K^(1/4)`.

The same argument is uniform in `Q` throughout the `D~K` reciprocal sector.

Thus:

- smooth outer-Poisson removes the artificial polynomial low-`Q` **discretization** barrier;
- the `n^(-3/4)` weight substantially relaxes the arithmetic mean-square demand at tiny `Q`;
- but standard coefficient-removing one-sided Type-II DLS still fails by a genuine polynomial factor.

## 7. Updated live problem
The remaining small-`Q` edge cannot be closed by any combination of

1. sharp outer Euler summation;
2. smooth outer Poisson alone;
3. the outer `n^(-3/4)` weight alone;
4. one-sided Cauchy followed by optimal Robert--Sargos / double-large-sieve spacing.

A surviving approach must retain information destroyed before the `K^(1/4)` loss appears. The two most concrete possibilities are:

1. a coefficient-preserving estimate for the reciprocal Möbius sum at very small `Q`, where only the relaxed `K Q^(1/2)` mean square is required;
2. a short/truncated differencing scheme that avoids the one-sided Cauchy dense-spacing floor without introducing the full rectangular fourth-moment diagonal floor.

The next literature audit should therefore target direct Möbius exponential sums with reciprocal/negative-power phase, especially estimates of the form

\[
\sum_{d\sim K}\mu(d)e(A d^{-1/2})
\]

or smooth variants, to see whether an unconditional exponent below the trivial length is already available at the relaxed endpoint scale.