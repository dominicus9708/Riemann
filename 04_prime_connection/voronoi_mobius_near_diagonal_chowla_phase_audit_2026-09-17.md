# Voronoi–Möbius near-diagonal correlation / phase audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Exact mean-square expansion: EXACT.
- Near-diagonal resolution width: DERIVED.
- Binary-Chowla reduction: SUFFICIENT but not necessary.
- Ordered reciprocal-phase cancellation: remains OPEN and may bypass raw short-interval Möbius variance.
- Existing averaged Chowla inserted absolutely: INSUFFICIENT at the critical polynomial shift range.

## 1. Mean-square expansion

For

\[
V_n(K)=\sum_{d\le K}\mu(d)d^{-1/4}e\!\left(2K\sqrt{n/d}\right),
\]

the dyadic mean square is exactly

\[
\mathcal M(N,K)
=\sum_{N<n\le2N}|V_n(K)|^2
\]

\[
=\sum_{d,e\le K}
\frac{\mu(d)\mu(e)}{(de)^{1/4}}
\sum_{N<n\le2N}
 e\!\left(2K\sqrt n\,(d^{-1/2}-e^{-1/2})\right).
\]

Thus the off-diagonal problem is a Möbius two-point correlation weighted by an oscillatory Gram kernel.

## 2. Near-diagonal width

On a dyadic d-block `d,e~D`, write `e=d+h`, `|h|<<D`. Then

\[
d^{-1/2}-(d+h)^{-1/2}
=\frac{h}{2D^{3/2}}+O\!\left(\frac{h^2}{D^{5/2}}\right)
\]

at the level of scale.

Across the n-window `n~N`, the total phase variation is controlled by

\[
\frac{K\sqrt N\,|h|}{D^{3/2}}.
\]

Hence the inner n-sum can remain of size comparable to `N` only for

\[
\boxed{
|h|\lesssim H(D,N):=\frac{D^{3/2}}{K\sqrt N}.
}
\]

This is the same threshold that appeared in the double-large-sieve resolution audit.

## 3. Coarse Chowla-strength sufficient condition

If one discards the ordered phase information inside the near-diagonal zone, the dangerous contribution is schematically

\[
N D^{-1/2}
\sum_{|h|\lesssim H}
\sum_{d\asymp D}\mu(d)\mu(d+h)W_{d,h},
\]

with `W` a bounded slowly varying weight.

The target diagonal scale on the `(N,D)` block is

\[
N D^{1/2}.
\]

Thus a coarse sufficient condition is

\[
\boxed{
\left|
\sum_{|h|\lesssim H}
\sum_{d\asymp D}\mu(d)\mu(d+h)W_{d,h}
\right|
\ll_\varepsilon D^{1+\varepsilon}.
}
\]

Without signed cancellation the trivial size is `HD`; the sufficient estimate saves essentially the whole shift length H.

## 4. Existing averaged Chowla does not close this coarse route

Matomäki--Radziwiłł--Tao prove averaged Chowla estimates of the qualitative form

\[
\sum_{h\le H}
\left|
\sum_{d\le D}\mu(d)\mu(d+h)
\right|
=o(HD)
\]

as `H->infinity` (with quantitative logarithmic-type decay in related formulations).

If this is inserted by absolute value, it only gives `o(HD)`, not the `O(D)` scale required above when H is a growing power.

Therefore:

`AVERAGED_CHOWLA_ABSOLUTE_SAVING_GAP`.

This does not say averaged Chowla is irrelevant; it says the known qualitative/absolute formulation is not by itself the critical estimate required by the coarse near-diagonal reduction.

## 5. Cluster-energy sufficient condition and its limitation

Partition a d-block of length ~D into disjoint intervals `I` of length ~H. A stronger sufficient condition is

\[
\boxed{
\sum_I\left|\sum_{d\in I}\mu(d)\right|^2
\ll_\varepsilon D^{1+\varepsilon}.
}
\]

For independent random signs this has natural size ~D. Finite Möbius data also displays this diagonal scale very cleanly.

However this condition is **not necessary** for the original reciprocal-phase mean square. The all-positive coefficient false control has enormous unphased cluster energy but still shows the same K^(1/4) reciprocal-phase power scale numerically.

Permanent guard:

`SHORT_INTERVAL_VARIANCE_OVERREDUCTION_GUARD` — do not replace the reciprocal-phase problem by a stronger unphased short-interval Möbius variance problem unless the loss is explicitly accepted as a sufficient-only route.

## 6. Why all-positive coefficients can still cancel

At `d~D`, the derivative of the reciprocal phase is

\[
\frac{d}{dd}\left(2K\sqrt n\,d^{-1/2}\right)
\asymp-rac{K\sqrt n}{D^{3/2}}.
\]

Define

\[
\alpha_{N,D}:=\frac{K\sqrt N}{D^{3/2}}
=\frac1{H(D,N)}.
\]

Although a frequency-resolution cell has length H, the entire d-block has approximately

\[
D\alpha_{N,D}=\frac{D}{H}
\]

oscillations. Therefore positive/smooth coefficients can exhibit strong first-derivative cancellation across the full ordered block.

For the extreme unresolved corner `D=K,N=1`,

\[
\alpha\asymp K^{-1/2},
\qquad D\alpha\asymp K^{1/2},
\]

so ordinary phase cancellation already predicts an unweighted sum of size roughly `K^(1/2)`; after the coefficient `d^(-1/4)` this is the target `K^(1/4)` scale.

This explains why the positive-coefficient false control does not contradict the double-large-sieve resolution loss: the latter is an arbitrary-coefficient operator estimate and discards the ordering/smoothness of the coefficient-phase interaction.

## 7. Operator-norm false control

For the finite matrix

\[
A_{n,d}=d^{-1/4}e\!\left(2K\sqrt{n/d}\right),
\qquad 1\le n,d\le K,
\]

direct SVD diagnostics give approximately

- K=100: largest singular value 10.9;
- K=200: 15.4;
- K=400: 21.2;
- K=800: 29.5.

The largest singular value grows roughly like `K^(1/2)`, so the worst arbitrary coefficient vector is much larger than the random-energy / Möbius target.

Classification:

`RECIPROCAL_PHASE_ARBITRARY_COEFFICIENT_OPERATOR_BARRIER`.

Thus neither of the following extremes is adequate:
- arbitrary-coefficient large-sieve operator norm: too weak;
- unphased Möbius cluster variance: stronger than necessary.

The useful theorem must retain both the **specific coefficient structure** and the **ordered reciprocal phase**.

## 8. Literature boundary

Classical Davenport/Baker--Harman and later work establish deep estimates for linear twists

\[
\sum_{n\le x}\mu(n)e(\alpha n),
\]

and modern short-interval work handles polynomial/nilsequence twists in substantial ranges. These results confirm strong Möbius orthogonality but do not directly provide the critical dyadic mean-square for the reciprocal fractional phase `A d^(-1/2)` derived here.

No novelty claim is made: this is only the present project's literature boundary after the initial search.

## 9. Current live target

The unresolved sector should now be treated as an ordered oscillatory bilinear problem, not immediately as Chowla:

\[
\boxed{
\sum_{N<n\le2N}
\left|
\sum_{d\asymp D}\mu(d)d^{-1/4}
 e\!\left(2K\sqrt{n/d}\right)
\right|^2
\stackrel{?}{\ll}_\varepsilon
N D^{1/2+\varepsilon}
}
\]

uniformly in the high-d / low-n sector left by the raw double large sieve.

Promising proof mechanisms to audit next:
1. B-process / reciprocal-phase transformation in d;
2. Vaughan/Heath--Brown-style decomposition of Möbius followed by bilinear phase estimates;
3. a refined large-sieve inequality exploiting monotone curvature rather than only pair spacing;
4. a weighted Chowla/short-interval input only if it beats the `HD -> D` saving gap at the required scales.
