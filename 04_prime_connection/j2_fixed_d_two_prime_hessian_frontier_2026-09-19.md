# j=2 fixed-d two-prime Hessian benchmark — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: after the signed-tail route reached the product-kernel/self-dual barrier, return to the original sharp j=2 reciprocal phase.
- New sufficient target: for each fixed outer d~H^2, prove an H^(4+eps) bound for the two-prime sum in p,q~H^3.
- Unweighted benchmark: a genuine two-dimensional B-process / Poisson stationary-phase calculation reaches exactly H^4 because the (p,q) Hessian is nondegenerate.
- Sequential one-variable curvature only gives H^5 and misses by one factor H.
- Thus the useful oscillation is genuinely two-dimensional mixed curvature.
- Classification: \`J2_FIXED_D_TWO_PRIME_HESSIAN_FRONTIER\`.

## 1. Fixed-d prime-pair sum

At the sharp endpoint,
\[
d\asymp H^2,
\qquad
p,q\asymp P:=H^3,
\]
and the normalized reciprocal amplitude is
\[
F:=H^4.
\]

For fixed d write schematically
\[
S_d
=
\sum_{p,q\asymp P}
\Lambda(p)\Lambda(q)
W_1(p/P)W_2(q/P)
e\!\left(
F\,\phi(p/P,q/P)
\right),
\]
where
\[
\phi(x,y)=c_d\,x^{-1/2}y^{-1/2}
\]
and \(c_d\asymp1\) on a fixed dyadic d-block.

The full j=2 target follows from the pointwise sufficient condition
\[
\boxed{
S_d\ll_\varepsilon H^{4+\varepsilon}
}
\]
because the d-range has length H^2:
\[
\sum_{d\asymp H^2}|S_d|
\ll
H^2 H^{4+\varepsilon}
=
H^{6+\varepsilon}.
\]

This uses no cancellation in the outer Möbius d-sum.

## 2. Nondegenerate Hessian

For
\[
\phi(x,y)=x^{-1/2}y^{-1/2},
\]
we have
\[
\phi_{xx}
=
\frac34x^{-5/2}y^{-1/2},
\]
\[
\phi_{yy}
=
\frac34x^{-1/2}y^{-5/2},
\]
and
\[
\phi_{xy}
=
\frac14x^{-3/2}y^{-3/2}.
\]

Therefore
\[
\det D^2\phi
=
\left(\frac9{16}-\frac1{16}\right)x^{-3}y^{-3}
=
\boxed{\frac12x^{-3}y^{-3}}.
\]

On dyadic support this is bounded above and below by positive constants.

Thus the reciprocal product phase is genuinely nondegenerate in the two prime coordinates.

## 3. Physical Hessian scale

Returning to p,q variables, each second derivative has size
\[
\frac F{P^2}
=
\frac{H^4}{H^6}
=
\boxed{H^{-2}}.
\]

Hence
\[
\det D^2_{p,q}f
\asymp
\left(\frac F{P^2}\right)^2
=
\boxed{H^{-4}}.
\]

A two-dimensional stationary integral therefore has natural amplitude
\[
\boxed{
|\det D^2f|^{-1/2}
\asymp H^2.
}
\]

## 4. Dual frequency box

Each first derivative varies on scale
\[
\frac FP
=
\frac{H^4}{H^3}
=
\boxed H.
\]

Therefore the two-dimensional B-process / Poisson transform has a dual frequency box containing
\[
\boxed{O(H^2)}
\]
relevant lattice frequencies.

Bounding the stationary contributions absolutely gives
\[
H^2
\times
H^2
=
\boxed{H^4}.
\]

Thus for smooth **unweighted integer coefficients**,
\[
\boxed{
\sum_{m,n\asymp H^3}
W_1(m/P)W_2(n/P)
e(F\phi(m/P,n/P))
\ll_\varepsilon
H^{4+\varepsilon}.
}
\]

This is exactly the fixed-d scale needed by the full j=2 target.

Classification:
\`TWO_DIMENSIONAL_INTEGER_BPROCESS_MATCHES_J2_TARGET\`.

## 5. Sequential one-dimensional curvature is insufficient

Freeze p and sum only in q.

The q-second derivative has size
\[
H^{-2}.
\]

The one-dimensional second-derivative estimate on a length H^3 interval gives
\[
H^3\cdot H^{-1}+H
\ll
\boxed{H^2}.
\]

If the p-variable is then summed trivially over H^3 values, the fixed-d bound is only
\[
\boxed{H^5}.
\]

Thus sequential one-dimensional curvature misses the desired H^4 by
\[
\boxed H.
\]

The missing H is exactly recovered by the joint nonzero Hessian determinant.

Permanent rule:
\`J2_MIXED_HESSIAN_GAIN_NOT_SEQUENTIAL_CURVATURE\`.

## 6. Relation to previous H deficits

The same factor H has appeared repeatedly:
- raw centered variance versus target;
- Mellin fourth-moment Cauchy;
- one-cell/one-sided DLS;
- sequential one-variable curvature here.

The two-dimensional integer B-process is the first current architecture that recovers this full factor H **without** asking for the Poisson-scale E2 variance theorem.

This identifies a genuinely different sufficient route.

## 7. Prime-weight transfer problem

The desired theorem is therefore

\[
\boxed{
\sum_{p,q\asymp H^3}
\Lambda(p)\Lambda(q)
W_1(p/P)W_2(q/P)
e\!\left(
H^4\phi(p/P,q/P)
\right)
\ll_\varepsilon
H^{4+\varepsilon},
}
\]
uniformly for the dyadic d-dependent constant \(c_d\).

This is stronger than what follows from:
- applying a one-prime exponential-sum theorem separately in q;
- applying Vaughan to one prime and then one-sided Cauchy;
- generic two-product DLS.

The obstacle is the transfer of **joint two-dimensional Hessian cancellation** through two prime weights.

Classification:
\`TWO_PRIME_NONDEGENERATE_HESSIAN_TRANSFER_OPEN\`.

## 8. Why a one-prime pointwise theorem is the wrong benchmark

Even if a one-prime reciprocal sum achieved the unweighted one-dimensional curvature scale
\[
H^2,
\]
trivial summation over the second prime would still give H^5.

Hence closing this route does not require merely improving the known one-prime transition theorem.

It requires a genuinely joint estimate in the pair (p,q), or an identity/decomposition which preserves the mixed derivative before Cauchy.

Permanent guard:
\`ONE_PRIME_CURVATURE_BOUND_CANNOT_CLOSE_FIXED_D_PAIR_BY_TRIVIAL_OUTER_SUM\`.

## 9. Literature position

Current searches identified:
- multidimensional van der Corput methods for other automorphic/exponential-sum settings;
- many bilinear prime/exponential-sum theorems;
- determinant/Kloosterman-fraction methods after Poisson in arithmetic variables.

No theorem has yet been identified that can be inserted directly into the exact real phase
\[
(pq)^{-1/2}
\]
with two von-Mangoldt weights at the critical scale
\[
P=H^3,\qquad F=H^4
\]
and yields H^(4+eps).

Therefore this is recorded as an exact literature gap, not a novelty claim.

## 10. Next analytic test

Apply Vaughan/Heath--Brown to **both** prime variables, but do not take one-sided Cauchy.

For each resulting dyadic block:
1. preserve both smooth cofactors simultaneously;
2. apply a genuine 2D B-process when both are at least self-dual;
3. compute the dual factor lengths and Hessian determinant;
4. identify which mixed Type-I/Type-II blocks fail to preserve two-dimensional curvature.

The goal is to determine whether the prime-weight transfer reduces to a finite family of mixed blocks smaller than the original j=2 problem.
