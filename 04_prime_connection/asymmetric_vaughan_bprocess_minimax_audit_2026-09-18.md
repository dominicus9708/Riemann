# Asymmetric Vaughan / B-process minimax audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Previous recursive Vaughan audit left asymmetric parameters `U=H^theta`, `V=H^(1-theta)` as a possible escape.
- New result: for the smooth cofactor exposed from a balanced Type-II parent, the primal and B-dual lengths have fixed product `X`, and their maximum is uniquely minimized at `theta=1/2`.
- Therefore asymmetric Vaughan parameters do **not** improve the worst smooth-variable length inside the pure `Vaughan decomposition -> expose smooth cofactor -> B-process` architecture.
- This closes asymmetry as an automatic scale-saving mechanism. It does not close coefficient-sensitive multilinear uses of the asymmetric decomposition.

## 1. Abstract reciprocal module
Use the notation of the recursive fixed-point audit. Let

\[
\mathcal S(Y,X)
=\sum_{m\asymp Y}\mu(m)c_m
 e\!\left(X(m/Y)^{-1/2}\right),
\]

and define the natural reciprocal resolution

\[
\boxed{H:=Y/X.}
\]

Choose asymmetric Vaughan parameters

\[
\boxed{
U=H^\theta,
\qquad
V=H^{1-\theta},
\qquad
UV=H,
}
\]

with `0<=theta<=1`.

## 2. Smooth cofactor length in a balanced Type-II parent
In the balanced Type-II parent box the non-Möbius factor has length

\[
d\asymp Y^{1/2}.
\]

Expanding its coefficient with

\[
d=cr,
\qquad c>V,
\]

shows that the longest possible exposed smooth cofactor is

\[
R_{\max}
\asymp \frac{Y^{1/2}}{V}.
\]

Since `Y=HX`,

\[
Y^{1/2}=X^{1/2}H^{1/2},
\]

and therefore

\[
\boxed{
R_{\max}
\asymp
X^{1/2}H^{\theta-1/2}.
}
\]

At `theta=1/2` this is the previously found self-dual length `sqrt(X)`.

## 3. B-process dual length
For a reciprocal-square-root phase with normalized amplitude `X` on a variable of length `R`, the B-process dual length is

\[
R^*\asymp X/R.
\]

Applying this to `R=R_max` gives

\[
\boxed{
R^*_{\max}
\asymp
X^{1/2}H^{1/2-\theta}.
}
\]

Consequently

\[
\boxed{
R_{\max}R^*_{\max}\asymp X.
}
\]

The asymmetry does not change the phase-space product; it only transfers length from the primal side to the dual side.

## 4. Exact minimax statement
The worse of the two lengths is

\[
\max(R_{\max},R^*_{\max})
\asymp
X^{1/2}H^{|\theta-1/2|}.
\]

Hence

\[
\boxed{
\min_{0\le\theta\le1}
\max(R_{\max},R^*_{\max})
\asymp \sqrt X,
}
\]

and equality occurs uniquely at

\[
\boxed{\theta=1/2.}
\]

Classification:

`ASYMMETRIC_VAUGHAN_BPROCESS_MINIMAX_SELFDUAL`.

Thus the symmetric choice is not merely aesthetically natural; it is the minimax optimizer for the exposed smooth variable and its B-dual.

## 5. Extreme Voronoi corner check
At

\[
D=K,
\qquad N=1,
\]

one has

\[
H=X=K^{1/2}.
\]

Therefore

\[
R_{\max}
=K^{1/4}K^{(\theta-1/2)/2},
\]

and

\[
R^*_{\max}
=K^{1/4}K^{(1/2-\theta)/2}.
\]

For example, `theta=3/4` gives the pair

\[
K^{3/8},\qquad K^{1/8},
\]

whose larger member `K^(3/8)` is worse than the symmetric `K^(1/4)` self-dual length.

The B-process indeed shortens the long side in this asymmetric example, but only by sending it to the correspondingly shorter dual side; the worst scale has increased before the transform.

## 6. Interaction with the weight-relaxed small-Q target
The 2026-09-18 weight audit showed that very small outer `Q` allows a factor

\[
\sqrt{K/Q}
\]

more than the old random-energy target. This relaxation changes the amount of cancellation required, but it does **not** alter the invariant

\[
R R^*=X
\]

or the minimax conclusion above.

Therefore an asymmetric threshold cannot remove the residual `K^(1/4)` loss of the generic Type-II spacing architecture merely by producing a longer smooth variable and B-transforming it.

Any gain from asymmetry would have to come from arithmetic coefficients **before** the smooth variable is reduced to an unsigned B-process problem.

## 7. Consequence for the recursive search
The following pure scale strategy is now closed:

> choose an asymmetric Vaughan split, expose a longer unweighted cofactor, and rely on a B-process length reduction to beat the symmetric fixed point.

The scale map has a minimax fixed point at `theta=1/2`.

Remaining logically distinct exits are:

1. retain the two Möbius signs `mu(c)mu(w)` in a multilinear mean value instead of taking absolute spacing counts;
2. exploit the weighted-small-`Q` slack together with a coefficient-sensitive operator estimate on the long Möbius orientation;
3. use a transformation that changes the reciprocal exponent or phase geometry, rather than only redistributing factor lengths.

The next direct calculation should therefore focus on the **long Möbius / short cofactor orientation** and ask whether its signed Gram operator has a smaller norm for actual Möbius coefficients than for arbitrary bounded coefficients.