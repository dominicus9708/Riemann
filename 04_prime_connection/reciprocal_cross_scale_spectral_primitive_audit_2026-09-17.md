# Reciprocal cross-scale spectral-primitive audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Reciprocal-phase outer mean square: primary live object.
- Gallagher diagonal short-interval L2 law: sufficient but now confirmed to be substantially stronger than necessary.
- Near-cell `h<=H` separate smallness: rejected as a necessary target.
- Cross-scale shift compensation: numerically strong, including for all-positive coefficients.
- Continuous outer kernel: admits an exact endpoint formula.
- New reduced object: a signed boundary functional of the first and second primitives of local Fourier energy.

## 1. Starting reciprocal block
For a dyadic arithmetic block write

\[
V_{n,D}=\sum_{D<d\le 2D} c_d d^{-1/4}e\!\left(2K\sqrt n\,d^{-1/2}\right),
\]

and

\[
\mathcal M(Q,D)=\sum_{Q<n\le2Q}|V_{n,D}|^2.
\]

For Möbius coefficients, `c_d=mu(d)`. The diagonal scale is

\[
\mathcal M_{\rm diag}\asymp QD^{1/2}.
\]

The reciprocal resolution length is

\[
H=\frac{D^{3/2}}{K\sqrt Q}.
\]

The unresolved range audited here has `1 << H <= D^(1/2)`.

## 2. Exact lag decomposition
Let

\[
z_{n,d}=c_d d^{-1/4}e\!\left(2K\sqrt n\,d^{-1/2}\right).
\]

Then

\[
\mathcal M(Q,D)
=\mathcal M_{\rm diag}
+2\operatorname{Re}\sum_{h\ge1}\mathcal C_h,
\]

where

\[
\mathcal C_h
=\sum_{Q<n\le2Q}
\sum_{\substack{D<d\le2D\\D<d+h\le2D}}
z_{n,d}\overline{z_{n,d+h}}.
\]

Define the partial-lag profile

\[
\mathcal M_{\le R}
:=\mathcal M_{\rm diag}
+2\operatorname{Re}\sum_{1\le h\le R}\mathcal C_h.
\]

`M_{<=R}` is not itself a square and may be negative. That is precisely why triangle-inequality separation by lag scale can destroy the compensation present in the full mean square.

## 3. Finite exact audit: Möbius / positive / random controls
The audit used

\[
K=D,
\qquad
D\in\{1024,2048,4096\},
\]

with `Q` chosen so that `H` is 4, 8, or 16. The full lag decomposition was computed by FFT autocorrelation and checked against the direct sum over `n`.

Representative normalized values are below. Each value is divided by the exact diagonal contribution of the same finite block.

| D | Q | H | coefficients | full / diag | h<=H / diag | h<=8H / diag |
|---:|---:|---:|---|---:|---:|---:|
| 1024 | 64 | 4 | Möbius | 0.8565 | 1.0819 | 0.8859 |
| 2048 | 128 | 4 | Möbius | 0.8067 | 0.9776 | 0.8456 |
| 4096 | 256 | 4 | Möbius | 1.0052 | 0.9780 | 1.0033 |
| 1024 | 16 | 8 | Möbius | 0.8391 | 1.1418 | 0.9922 |
| 2048 | 32 | 8 | Möbius | 1.0196 | 1.1324 | 1.1271 |
| 4096 | 64 | 8 | Möbius | 0.8277 | 1.0331 | 0.8791 |
| 1024 | 64 | 4 | positive | 0.00265 | -0.6253 | 0.0263 |
| 2048 | 128 | 4 | positive | 0.00133 | -0.6258 | 0.0263 |
| 4096 | 256 | 4 | positive | 0.00057 | -0.6260 | 0.0262 |
| 1024 | 16 | 8 | positive | 0.00887 | -1.1426 | 0.0497 |
| 2048 | 32 | 8 | positive | 0.00479 | -1.1372 | 0.0505 |
| 4096 | 64 | 8 | positive | 0.00249 | -1.1343 | 0.0494 |
| 1024 | 4 | 16 | positive | 0.0221 | -2.2303 | 0.0050 |
| 2048 | 8 | 16 | positive | 0.0167 | -2.1792 | 0.0851 |
| 4096 | 16 | 16 | positive | 0.00923 | -2.1462 | 0.0970 |

Random Rademacher controls stay at order-one diagonal ratios, as expected.

### Interpretation
The all-positive sequence is a decisive false control against the strategy

> prove the `h<=H` cell is itself at diagonal size.

For positive coefficients the `h<=H` truncated profile can have magnitude exceeding the diagonal, and can even be negative, while the **full** reciprocal mean square is far below diagonal scale after farther shifts are restored.

Therefore:

`NEAR_CELL_SEPARATE_SMALLNESS_NOT_NECESSARY`.

This strengthens the previous `SHIFT_SCALE_COMPENSATION_GUARD` from a warning to an explicit finite counterexample against using near-cell smallness as a necessary structural property.

## 4. Smooth positive coefficients are phase-only false controls
For `c_d=1`, put

\[
f_n(d)=2K\sqrt n\,d^{-1/2}.
\]

On `d~D`, `n~Q`,

\[
|f_n'(d)|\asymp \frac1H.
\]

Away from the thin endpoint-resonance transition, the first-derivative/Kusmin–Landau estimate gives schematically

\[
\sum_{d\asymp D} e(f_n(d))\ll H.
\]

Partial summation with the weight `d^{-1/4}` then gives

\[
|V_{n,D}^{(+)}|\ll H D^{-1/4}.
\]

Hence

\[
\sum_{n\asymp Q}|V_{n,D}^{(+)}|^2
\ll QH^2D^{-1/2}
\le QD^{1/2}
\]

throughout `H<=sqrt(D)`.

Thus the reciprocal phase by itself can satisfy the target for a smooth positive coefficient sequence. Möbius randomness is **not necessary** for the full reciprocal sum to be small.

The proof problem is therefore not equivalent to showing that every local Fourier window of the coefficients is random-like.

## 5. Continuous outer kernel and its exact endpoint form
In the local near-diagonal scaling, freeze the slow `d/D` dependence and write the normalized kernel

\[
F(y):=\int_1^2 e(y\sqrt t)\,dt.
\]

With `u=sqrt(t)`,

\[
F(y)=2\int_1^{\sqrt2}u e(yu)\,du.
\]

For `y\ne0`, direct integration gives the exact identity

\[
\boxed{
F(y)
=
\frac{\sqrt2\,e(\sqrt2 y)-e(y)}{\pi i y}
+
\frac{e(\sqrt2 y)-e(y)}{2\pi^2 y^2}.
}
\]

Also `F(0)=1` by continuity.

Consequences:
1. the far-shift tail is an endpoint oscillation of order `1/y`;
2. the kernel is not positive and cannot be replaced by a monotone absolute envelope without losing cross-scale cancellation;
3. the two outer endpoints `n~Q` and `n~2Q` appear explicitly through the frequencies `1/H` and `sqrt(2)/H`.

Classification:

`RECIPROCAL_CONTINUOUS_KERNEL_ENDPOINT_IDENTITY`.

## 6. Spectral-primitive identity
Let a finite real coefficient block be `a_m`, and define the lag correlation

\[
A_h=\sum_m a_m a_{m+h}.
\]

Let

\[
P(\alpha)=\sum_m a_m e(\alpha m),
\qquad
A_0=\sum_m a_m^2.
\]

Then

\[
|P(\alpha)|^2-A_0
=2\sum_{h\ge1}A_h\cos(2\pi h\alpha).
\]

Define the first and second spectral primitives

\[
J(\alpha)
:=\int_0^\alpha\bigl(|P(u)|^2-A_0\bigr)\,du,
\]

\[
L(\alpha)
:=\int_0^\alpha J(v)\,dv.
\]

Termwise integration gives

\[
J(\alpha)
=\sum_{h\ge1}A_h\frac{\sin(2\pi h\alpha)}{\pi h},
\]

and

\[
L(\alpha)
=\sum_{h\ge1}A_h
\frac{1-\cos(2\pi h\alpha)}{2\pi^2h^2}.
\]

Insert the exact endpoint form of `F(h/H)`. The full signed off-diagonal functional of the continuous local model becomes

\[
\boxed{
2\operatorname{Re}\sum_{h\ge1}A_hF(h/H)
=
2H\left[\sqrt2\,J\!\left(\frac{\sqrt2}{H}\right)
-J\!\left(\frac1H\right)\right]
+2H^2\left[L\!\left(\frac1H\right)
-L\!\left(\frac{\sqrt2}{H}\right)\right].
}
\]

This is an exact algebraic identity for the continuous local kernel.

Classification:

`RECIPROCAL_SPECTRAL_PRIMITIVE_BOUNDARY_IDENTITY`.

## 7. Why this changes the immediate target
Gallagher reduction asks for a random-sign-size short-interval second moment, equivalently local Fourier flatness at scale `1/H`. That remains a valid sufficient condition.

The identity above shows it is not necessary.

The reciprocal kernel only asks for a **specific signed dilation boundary functional** of the spectral energy:

- first primitive at `1/H` and `sqrt(2)/H`;
- second primitive across the same dilation step.

Two very different spectral geometries can therefore give a small reciprocal mean square:

1. Möbius/random-like spectral flatness, where the off-diagonal correction is small;
2. smooth positive coefficients, where low-frequency energy is highly concentrated but the two primitive terms compensate strongly.

This explains the positive-coefficient false control without invoking Möbius cancellation.

Permanent correction:

`GALLAGHER_DIAGONAL_L2_SUFFICIENT_NOT_NECESSARY`.

Do not promote the diagonal short-interval Möbius variance law to the unique live proof target.

## 8. Literature boundary
For the integer Möbius function, the random-sign variance scale for all polynomially short intervals is not presently available as a general unconditional theorem.

- Classical and modern short-interval results give strong `o(H)` cancellation for almost all intervals in broad ranges and, in newer work, higher-uniformity against polynomial/nilsequence phases.
- Those statements do not by themselves imply the diagonal variance law `integral |sum mu|^2 ~ XH` uniformly in the ranges needed here.
- Conditional work of Nathan Ng models the short-interval Mertens increment with variance approximately `6H/pi^2` under a Möbius-adapted Hardy–Littlewood assumption.
- Function-field analogues do prove the corresponding variance scale in large-field limits, supporting the random model but not proving the integer statement.

Therefore making the diagonal short-interval variance law the sole next target would risk replacing RH by another deep unresolved cancellation statement.

## 9. New live problem
The next proof object should be the **discrete reciprocal spectral-boundary functional**, not an absolute lag norm and not local variance alone.

Required next steps:

1. replace the continuous `n`-integral by the discrete sum `Q<n<=2Q` and obtain a uniform Euler–Maclaurin / van-der-Corput error bound;
2. restore the slowly varying `x=d/D` dependence, so the boundary frequencies become `x^{-3/2}/H` and `sqrt(2)x^{-3/2}/H`;
3. determine whether the resulting `d`-dependent primitive functional can be controlled by arithmetic information weaker than square-root Mertens or diagonal short-interval variance;
4. test a smooth dyadic partition in `d` whose overlap terms preserve the primitive cancellation exactly;
5. keep positive and random coefficients as permanent false controls.

The decisive question is now:

> Can the exact reciprocal phase convert Möbius arithmetic information that is weaker than local square-root cancellation into a bounded **dilation difference of integrated spectral energy**?

If yes, this would bypass the `H` loss shared by generic large sieve, one-sided Type-II DLS, and the isolated Gallagher target without assuming RH-scale Mertens cancellation in advance.
