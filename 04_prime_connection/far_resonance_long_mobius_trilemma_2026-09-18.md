# Far-resonance long-Möbius trilemma audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Previous frontier: unbalanced Type-II box, long actual Möbius factor, far shifts `h \gtrsim H`.
- Hope audited here: use the integer resonances of the short smooth factor to convert the far-shift piece into a family of **linear Möbius twists** and then import Davenport/Baker–Harman type information.
- Result: that hope is false in the direct Cauchy/B-process architecture.
- If the Möbius factor is preserved, the arithmetic object after expansion is necessarily a **weighted binary Möbius correlation** `mu(w)mu(w+h)`, not a linear Möbius twist.
- If Cauchy is instead taken in the long Möbius factor, the Möbius signs disappear and one re-enters the generic spacing/DLS barrier.
- If the long Möbius factor is Vaughan-decomposed before Cauchy, one re-enters the recursive self-dual fixed-point barrier.
- Thus the far-resonant long-Möbius orientation has a three-way structural obstruction inside the currently audited toolkit.

## 1. Long-Möbius Type-II orientation
Write a dyadic Type-II block in the orientation

\[
T_n
=\sum_{d\asymp M} b_d
\sum_{w\asymp L}\mu(w)
 e\!\left(2K\sqrt n\,(dw)^{-1/2}\right),
\qquad ML=D,
\]

with

\[
L\gg M
\]

and the long factor `w` carrying the actual Möbius coefficient.

The reciprocal resolution is

\[
H=\frac{D^{3/2}}{K\sqrt Q}
\]

for `n\asymp Q`.

The near-shift range `|w-w'|\lesssim H` has already been bounded at the weight-adapted target scale by the first-derivative argument. The present audit concerns

\[
|h|:=|w'-w|\gtrsim H.
\]

## 2. Preserve Möbius: Cauchy in the short non-Möbius factor
Apply Cauchy in `d`:

\[
|T_n|^2
\le
\left(\sum_{d\asymp M}|b_d|^2\right)
\sum_{d\asymp M}
\left|
\sum_{w\asymp L}\mu(w)e(2K\sqrt n\,(dw)^{-1/2})
\right|^2.
\]

Using the divisor bound for `b_d`, the first factor is `M D^\varepsilon`.

After expanding the square in the long variable,

\[
|T_n|^2
\ll
M D^\varepsilon
\sum_{w,w'\asymp L}
\mu(w)\mu(w')
\sum_{d\asymp M}
 e\!\left(C_{n;w,w'}d^{-1/2}\right),
\]

where

\[
\boxed{
C_{n;w,w'}
:=2K\sqrt n\,[w^{-1/2}-w'^{-1/2}].
}
\]

Writing `w'=w+h`, the arithmetic coefficient is exactly

\[
\boxed{\mu(w)\mu(w+h).}
\]

This is already a binary Chowla-type object before any resonance transformation is applied.

Classification:

`LONG_MOBIUS_CAUCHY_SHORT_FACTOR_BINARY_CORRELATION_REENTRY`.

## 3. B-process on the short smooth factor
For one pair `(w,w')`, consider

\[
\phi(d)=C d^{-1/2}.
\]

Assume first `C>0`; the opposite sign is symmetric. Then

\[
\phi'(d)=-\frac C2d^{-3/2},
\qquad
\phi''(d)=\frac{3C}{4}d^{-5/2}.
\]

In the far-resonant range the derivative interval contains nonzero integers. Let the resonance be `-r`, with `r\ge1`, and solve

\[
\phi'(d_r)=-r.
\]

Then

\[
\boxed{
 d_r=\left(\frac C{2r}\right)^{2/3}.
}
\]

The B-process / Legendre phase is

\[
\phi(d_r)+r d_r.
\]

A direct substitution gives

\[
\boxed{
\phi(d_r)+r d_r
=3\cdot2^{-2/3}C^{2/3}r^{1/3}.
}
\]

Also

\[
|\phi''(d_r)|^{-1/2}
\asymp
C^{1/3}r^{-5/6}.
\]

Thus, schematically and away from standard endpoint-transition corrections,

\[
\sum_{d\asymp M}e(Cd^{-1/2})
\rightsquigarrow
\sum_{r\in\mathcal R(C,M)}
C^{1/3}r^{-5/6}
 e\!\left(c\,C^{2/3}r^{1/3}\right),
\]

where `c=3\cdot2^{-2/3}` up to the convention in `e(t)` and the usual stationary-phase phase shift.

Classification:

`RECIPROCAL_MINUS_HALF_BPROCESS_TO_ONE_THIRD_PHASE`.

The negative half-power reciprocal phase is transformed into a positive one-third-power dual phase.

## 4. The arithmetic coefficient does not become linear Möbius
Substitute

\[
C=C_{n;w,w+h}
=2K\sqrt n\,[w^{-1/2}-(w+h)^{-1/2}].
\]

After B-process, the far-resonant contribution has schematic form

\[
\sum_h\sum_w
\mu(w)\mu(w+h)
\sum_r
A_{n,w,h,r}
 e\!\left(
 c\,|C_{n;w,w+h}|^{2/3}r^{1/3}
 \right).
\]

The Möbius information is still

\[
\boxed{\mu(w)\mu(w+h),}
\]

not `mu(w)` alone.

Moreover, because

\[
C_{n;w,w+h}
\]

depends on both `w` and `h`, the dual phase is not a fixed linear twist in `w` to which Davenport's theorem can simply be applied.

For `h\ll L`, the first expansion is

\[
C_{n;w,w+h}
\asymp
K\sqrt Q\,h\,w^{-3/2},
\]

so the dual phase is approximately

\[
\asymp
(K\sqrt Q)^{2/3}
 h^{2/3}w^{-1}r^{1/3}.
\]

Thus even locally the transformed `w` dependence is reciprocal, not linear.

Permanent correction:

`FAR_RESONANCE_DAVENPORT_LINEAR_TWIST_HOPE_FALSE`.

## 5. What averaged Chowla can and cannot do
The preserved-Möbius formulation naturally asks for weighted shift sums of the form

\[
\sum_{w\asymp L}
\mu(w)\mu(w+h)W_{h,r,n}(w),
\]

with an oscillatory smooth weight `W` inherited from the dual reciprocal phase.

This is at least as structurally close to binary Chowla as the unweighted correlation

\[
\sum_{w\asymp L}\mu(w)\mu(w+h).
\]

Known averaged Chowla results provide strong qualitative cancellation after averaging shifts, but the previous audit already showed that absolute transfer of those results loses the polynomial factor needed for the present shrinking-band target.

The B-process does not change that arithmetic order from one-point Möbius to a simpler object; it produces a **weighted two-point correlation**.

Classification:

`FAR_RESONANCE_WEIGHTED_CHOWLA_REENTRY`.

This is a structural classification, not a claim that no future weighted Chowla theorem could close the range.

## 6. Alternative 1: Cauchy in the long Möbius factor
Instead apply Cauchy in `w`. Then

\[
|T_n|^2
\le
L
\sum_{w\asymp L}
\left|
\sum_{d\asymp M}b_d
 e(2K\sqrt n\,(dw)^{-1/2})
\right|^2.
\]

The coefficient `mu(w)` has disappeared before the oscillatory estimate begins.

Expanding the remaining square produces an arbitrary/divisor-bounded coefficient spacing problem. This is precisely the architecture already shown to carry the invariant dense-spacing deficit

\[
R\ge\sqrt{DH}
\]

against the old target, or the residual `K^(1/4)` loss against the weight-adapted very-small-`Q` target.

Classification:

`LONG_MOBIUS_CAUCHY_REMOVAL_RETURNS_GENERIC_DLS_BARRIER`.

## 7. Alternative 2: decompose the long Möbius factor before Cauchy
The remaining natural attempt is to apply Vaughan/Heath--Brown type decomposition to the long `mu(w)` factor first.

This was audited in the recursive reciprocal Vaughan calculation. At the natural derivative threshold, a balanced daughter Type-II block and expansion of its non-Möbius coefficient expose a smooth cofactor exactly at the B-process self-dual length.

The 2026-09-18 asymmetric minimax audit further showed that

\[
R R^*=X
\]

and the worst of the primal/dual lengths is uniquely minimized by the symmetric threshold. Therefore simply changing Vaughan asymmetry cannot create an automatic scale saving.

Classification:

`LONG_MOBIUS_PREDECOMPOSITION_RETURNS_SELFDUAL_VAUGHAN_FIXED_POINT`.

## 8. Far-resonance trilemma
Inside the currently audited family of methods, the long-Möbius far-resonant block therefore has three direct choices:

### A. Preserve Möbius by Cauchy in the short factor
Result:

\[
\mu(w)\mu(w+h)
\]

weighted binary Chowla correlation after the resonance/B-process transform.

### B. Cauchy in the long Möbius factor
Result: Möbius information is removed and the generic DLS dense-spacing barrier returns.

### C. Decompose the long Möbius factor before Cauchy
Result: recursive Vaughan returns to the reciprocal self-dual fixed point; asymmetry only transfers the length between a variable and its B-dual.

Hence:

\[
\boxed{
\text{far-resonant long-Möbius block}
\to
\begin{cases}
\text{weighted Chowla},\\
\text{generic DLS barrier},\\
\text{self-dual Vaughan loop}.
\end{cases}
}
\]

Classification:

`FAR_RESONANCE_LONG_MOBIUS_TRILEMMA`.

## 9. Consequence for the proof search
This trilemma closes the hope that the **existing** Cauchy/B-process/Vaughan pieces, merely reordered, automatically turn the far-resonant block into a known linear Möbius exponential sum.

A genuine exit must retain more joint information before any of the three reductions destroys it. The remaining plausible architectures are narrower:

1. a **coefficient-sensitive bilinear/Gram estimate** that keeps `mu(w)` linearly rather than squaring it into `mu(w)mu(w+h)`;
2. a multilinear mean-value inequality using two Vaughan generations simultaneously, before regrouping to the self-dual daughter box;
3. an identity coupling the far resonance index `r` to factorization data so that the binary correlation receives an additional arithmetic sparsity absent from ordinary Chowla;
4. an external theorem specifically for weighted two-point Möbius correlations with reciprocal/fractional-power weights at the required polynomial scale.

The cleanest next direct audit is option 3: inspect the resonance condition

\[
r\asymp |C_{n;w,w+h}|M^{-3/2}
\]

and determine whether its integrality forces a nontrivial congruence or spacing restriction on `(w,h)` beyond the generic smooth relation. If no arithmetic restriction is created, the B-process resonance index is merely analytic bookkeeping and the route reduces fully to weighted Chowla.