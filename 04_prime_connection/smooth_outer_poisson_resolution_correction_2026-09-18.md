# Smooth outer-Poisson resolution correction — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Previous sharp-cutoff split `Q>=D^(1/3)` versus `Q<D^(1/3)`: **CORRECTED as non-intrinsic**.
- Composite midpoint summation already improves the sharp-cutoff discrete-to-continuum threshold to `Q>=D^(1/5)` at `K~D`.
- For the nonnegative dyadic mean square, a smooth outer `n`-majorant is legal; Poisson summation then makes the near-cell discrete-to-continuum error smaller than any fixed power of `Q`.
- Consequently every polynomial low-`Q` range `Q>=D^delta` can be transferred to a smooth continuous reciprocal kernel by choosing sufficiently many integrations by parts / Poisson decay.
- The arithmetic obstruction remains the mesoscopic Möbius reciprocal-band energy; smoothing removes a bookkeeping barrier, not the Möbius cancellation problem.

## 1. Original mean-square block
The Voronoi–Möbius module has

\[
V_n(K)=\sum_{d\le K}\mu(d)d^{-1/4}e\!\left(2K\sqrt{n/d}\right)
\]

and the sufficient dyadic target

\[
\mathcal M(Q,K)
=\sum_{Q<n\le2Q}|V_n(K)|^2
\ll_\varepsilon QK^{1/2+\varepsilon}.
\]

On a dyadic `d~D` block, after expanding the square, put

\[
\lambda_{d,e}
:=2K\sqrt Q\,(d^{-1/2}-e^{-1/2}).
\]

For `e=d+h` and `d~D`, define the reciprocal resolution

\[
H:=\frac{D^{3/2}}{K\sqrt Q}.
\]

Then for `|h|\lesssim H`,

\[
\lambda_{d,d+h}=O(1).
\]

This is the unresolved near cell.

## 2. Why the old `D^(1/3)` boundary appeared
For the sharp outer block, the kernel is

\[
S_Q(\lambda)
:=\sum_{Q<n\le2Q}e\!\left(\lambda\sqrt{n/Q}\right).
\]

A crude Euler estimate of the form

\[
S_Q(\lambda)=QF(\lambda)+O(1+|\lambda|)
\]

produces, after absolute summation over `O(DH)` near-diagonal pairs with reciprocal weight `~D^{-1/2}`, an error

\[
\ll HD^{1/2}.
\]

Comparing with the desired block scale `QD^(1/2)` forces

\[
H\lesssim Q.
\]

At `K~D`, where `H~sqrt(D/Q)`, this becomes

\[
Q\gtrsim D^{1/3}.
\]

Thus the previous Sector-A/Sector-B split came from the **chosen sharp-cutoff quadrature error**, not directly from the reciprocal phase.

## 3. Midpoint correction: sharp cutoff already reaches `D^(1/5)`
Define

\[
g_\lambda(x)=e\!\left(\lambda\sqrt{x/Q}\right).
\]

Use the composite midpoint rule on the unit cells centered at the integers `Q+1,...,2Q`:

\[
S_Q(\lambda)
=\int_{Q+1/2}^{2Q+1/2}g_\lambda(x)\,dx
+R_Q(\lambda).
\]

For `|\lambda|<=B` fixed,

\[
g_\lambda''(x)\ll_B Q^{-2}
\]

uniformly on the interval, so the composite midpoint error satisfies

\[
\boxed{R_Q(\lambda)\ll_B Q^{-1}.}
\]

Equivalently,

\[
S_Q(\lambda)
=QF_Q(\lambda)+O_B(Q^{-1}),
\]

where

\[
F_Q(\lambda)
:=\int_{1+1/(2Q)}^{2+1/(2Q)}e(\lambda\sqrt t)dt.
\]

Absolute aggregation over the near cell now costs only

\[
E_{\rm mid}
\ll D^{1/2}H/Q.
\]

For this to lie below the target `QD^(1/2)` it is enough that

\[
H\lesssim Q^2.
\]

At `K~D`,

\[
\sqrt{D/Q}\lesssim Q^2
\iff
\boxed{Q\gtrsim D^{1/5}.}
\]

Classification:

`SHARP_OUTER_MIDPOINT_BOUNDARY_D1_5`.

This alone proves that the earlier `D^(1/3)` boundary was not intrinsic.

## 4. Smooth majorant is legal
Choose a fixed nonnegative

\[
W\in C_c^\infty((a,b)),
\qquad 0<a<1<2<b,
\]

with

\[
W(t)\ge1\quad(1\le t\le2).
\]

Then, whenever the support remains inside the available Voronoi `n` range,

\[
\mathcal M(Q,K)
\le
\mathcal M_W(Q,K)
:=\sum_n W(n/Q)|V_n(K)|^2.
\]

Because every summand is nonnegative, this replacement requires no cancellation assumption.

For the genuinely low-`Q` range one may choose the support so that `bQ<=K`; the top dyadic ranges can be handled separately and are not the previous low-`Q` corner.

## 5. Poisson summation for the smooth outer kernel
After expanding the square, define

\[
S_{Q,W}(\lambda)
:=\sum_{n\in\mathbb Z}W(n/Q)e\!\left(\lambda\sqrt{n/Q}\right),
\]

with the square root evaluated only on the positive support of `W`.

Let

\[
g_\lambda(t)=W(t)e(\lambda\sqrt t).
\]

Poisson summation gives

\[
S_{Q,W}(\lambda)
=Q\sum_{k\in\mathbb Z}\widehat g_\lambda(kQ).
\]

The zero mode is

\[
QF_W(\lambda),
\qquad
F_W(\lambda):=\int W(t)e(\lambda\sqrt t)dt.
\]

For every fixed `B,A>0`, the derivatives of `g_lambda` are uniformly bounded for `|lambda|<=B`, and repeated integration by parts gives

\[
|\widehat g_\lambda(\xi)|
\ll_{A,B,W}(1+|\xi|)^{-A}.
\]

Hence

\[
\boxed{
S_{Q,W}(\lambda)
=QF_W(\lambda)
+O_{A,B,W}(Q^{1-A})
\qquad(|\lambda|\le B).
}
\]

Classification:

`SMOOTH_OUTER_POISSON_ARBITRARY_POWER_TRANSFER`.

## 6. Aggregate error in the reciprocal near cell
There are `O(DH)` pairs with `d~D` and `|d-e|\lesssim H`. The reciprocal amplitude is `~D^{-1/2}`. Therefore the Poisson remainder contributes

\[
E_{\rm Pois}
\ll_{A,B,W}
D^{1/2}H Q^{1-A}.
\]

Relative to the desired `QD^(1/2)` scale,

\[
\boxed{
\frac{E_{\rm Pois}}{QD^{1/2}}
\ll H Q^{-A}.
}
\]

At `K~D`, `H<=D^(1/2)`. Thus for every fixed `delta>0`, if

\[
Q\ge D^\delta,
\]

choosing

\[
A>\frac1{2\delta}
\]

makes the transfer error power-saving.

Therefore the entire polynomial low-`Q` range merges back into the smooth continuous-kernel problem.

Permanent correction:

`POLYNOMIAL_LOW_Q_NOT_A_DISTINCT_DISCRETE_SECTOR`.

## 7. Continuous smooth kernel remains a band-energy kernel
The smooth main kernel is

\[
F_W(y)=\int W(t)e(y\sqrt t)dt.
\]

With `u=sqrt(t)`,

\[
F_W(y)=2\int uW(u^2)e(yu)du.
\]

Thus `F_W` is a rapidly decaying Fourier transform because `W` is smooth and compactly supported away from zero.

If a local reciprocal block has been frozen to `lambda=alpha h`, and

\[
P(\beta)=\sum_m a_m e(\beta m),
\]

then its autocorrelation identity is

\[
\boxed{
A_0F_W(0)+2\operatorname{Re}\sum_{h\ge1}A_hF_W(\alpha h)
=
\int W(t)|P(\alpha\sqrt t)|^2dt.
}
\]

After `beta=alpha sqrt(t)`, the right side is a positive smoothly weighted Fourier energy on a band of frequencies

\[
\beta\asymp\alpha\asymp H^{-1}.
\]

So smoothing does not manufacture arithmetic cancellation. It only removes the artificial sharp-cutoff discretization loss.

## 8. Effect on the research map
The old map

`Sector A: Q>=D^(1/3)` / `Sector B: Q<D^(1/3)`

must be replaced by:

1. **polynomial `Q`**: smooth outer Poisson transfer reduces the discrete outer mean square to the same continuous reciprocal-band problem, with arbitrary-power discretization accuracy;
2. **subpolynomial / bounded `Q`**: still requires a separate endpoint treatment if it is needed at full strength;
3. the actual unresolved arithmetic obstruction is therefore not outer-`n` discreteness but Möbius energy in a shrinking reciprocal/Fourier band, together with the slowly varying exact `d^{-1/2}` geometry.

The previous low-Q linear-twist literature barrier remains relevant to the arithmetic part, but it is no longer evidence for a distinct discrete sector.

## 9. Next direct audit
Re-optimize the original Voronoi sufficiency argument so that very small `Q` blocks are weighted by their actual factor `tau(n)n^{-3/4}` rather than demanding the same mean-square theorem uniformly down to `Q=1`.

The next question is:

> after smooth Poisson removes all polynomial low-`Q` discretization loss, how strong a bound is really needed for the remaining subpolynomial `Q` blocks in order for the total Voronoi sum to stay at `K^(1/2+epsilon)` before the outer `K^(1/2)` factor?

If those smallest blocks admit a weaker sufficient estimate, the artificial Sector-B corner may disappear completely.