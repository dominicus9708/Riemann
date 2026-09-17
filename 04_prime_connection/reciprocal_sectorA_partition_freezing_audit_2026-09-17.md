# Reciprocal Sector-A partition / frequency-freezing audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Sector A: `K~D`, `Q>=D^(1/3)`, equivalently `H<=D^(1/3)`.
- Discrete-to-continuum transfer in the hard near cell: already controlled.
- New result: the remaining slow `d/D` dependence can be frozen on `J=sqrt(D)` blocks with a power-saving aggregate error.
- No block orthogonality assumption is needed: partition after expanding the mean square in the lag variable.
- Remaining Sector-A obstruction is arithmetic control of the resulting signed primitive boundary functional.

## 1. Why partition after the lag expansion
The reciprocal off-diagonal has the form

\[
\mathcal E
=2\operatorname{Re}
\sum_{h\ge1}\sum_{d\asymp D}
 b_{d,h}\,\mathcal K_{Q,K}(d,h),
\]

with

\[
b_{d,h}
=\mu(d)\mu(d+h)[d(d+h)]^{-1/4}.
\]

Introduce a smooth partition of unity only in the base variable `d`:

\[
\sum_j\chi_j(d)=1,
\qquad
\operatorname{supp}\chi_j\subset I_j,
\qquad |I_j|\asymp J.
\]

Then exactly

\[
\mathcal E
=2\operatorname{Re}\sum_j
\sum_h\sum_d
\chi_j(d)b_{d,h}\mathcal K_{Q,K}(d,h).
\]

This does **not** split the original exponential sum before squaring, so no artificial block orthogonality and no missing cross-block term is introduced.

Classification:

`LAG_SIDE_PARTITION_EXACT`.

## 2. Sector-A block length
At the symmetric scale `K~D`,

\[
H\asymp\sqrt{D/Q}.
\]

Sector A is

\[
Q\ge D^{1/3},
\]

hence

\[
H\le D^{1/3}.
\]

Choose

\[
\boxed{J=D^{1/2}.}
\]

Then

\[
H/J\le D^{-1/6},
\qquad
J/D=D^{-1/2}.
\]

So the block is much longer than the unresolved shift scale but still short compared with `D`.

It also lies below the previous curvature length

\[
J_{\rm curv}\asymp\sqrt{DH},
\]

because `H>=1` in the unresolved sector.

## 3. Freezing the exact reciprocal frequency
Recall

\[
\lambda_{d,h}
=2K\sqrt Q\,[d^{-1/2}-(d+h)^{-1/2}].
\]

For `h=O(H)` and `d~D`,

\[
\lambda_{d,h}
=\frac hH x^{-3/2}
+O\!\left(\frac{h^2}{HD}\right),
\qquad x=d/D.
\]

Let `d_j` be a reference point in `I_j`, with `x_j=d_j/D`. Across a block of length `J`,

\[
|x^{-3/2}-x_j^{-3/2}|
\ll J/D.
\]

Thus uniformly for `h<=cH`,

\[
\boxed{
\lambda_{d,h}
=\alpha_j h
+O_c\!\left(\frac JD+\frac HD\right),
}
\]

where

\[
\alpha_j
:=K\sqrt Q\,d_j^{-3/2}
\asymp H^{-1}.
\]

The harmless fixed factor convention in `alpha_j` is chosen to match the first-order expansion of the exact difference.

## 4. Kernel Lipschitz bound
For

\[
F(\lambda)=\int_1^2e(\lambda\sqrt t)dt,
\]

one has

\[
F'(\lambda)
=2\pi i\int_1^2\sqrt t\,e(\lambda\sqrt t)dt,
\]

so

\[
|F'(\lambda)|\ll1
\]

uniformly on the real line.

Therefore

\[
F(\lambda_{d,h})
=F(\alpha_jh)
+O_c\!\left(\frac JD+\frac HD\right).
\]

The same relative scale controls freezing

\[
[d(d+h)]^{-1/4}
=D_j^{-1/2}
\left(1+O_c\!\left(\frac JD+\frac HD\right)\right).
\]

## 5. Aggregate freezing error
There are `O(DH)` near-cell pairs. The frozen continuum kernel carries the outer factor `Q`, and the reciprocal weight is `~D^(-1/2)`.

Hence the absolute aggregate error from frequency and weight freezing is

\[
E_{\rm freeze}
\ll_c
Q\,D^{-1/2}\,(DH)
\left(\frac JD+\frac HD\right).
\]

Therefore

\[
\boxed{
E_{\rm freeze}
\ll_c
QD^{1/2}
\left(
\frac{HJ}{D}+
\frac{H^2}{D}
\right).
}
\]

With `J=sqrt(D)`,

\[
\frac{HJ}{D}=\frac H{\sqrt D}
\le D^{-1/6},
\]

and

\[
\frac{H^2}{D}
\le D^{-1/3}.
\]

Thus

\[
\boxed{
E_{\rm freeze}
\ll_c QD^{1/2}D^{-1/6}
}
\]

up to fixed constants and the smaller `D^(-1/3)` term.

Classification:

`SECTOR_A_FREQUENCY_FREEZING_POWER_SAVING`.

This is a bookkeeping/geometric reduction, not an RH estimate by itself.

## 6. Local signed primitive identity without block-orthogonality loss
Define the block-weighted lag correlations

\[
A_{j,h}
:=\sum_{d\asymp D}
\chi_j(d)\mu(d)\mu(d+h),
\]

or include the slowly varying amplitude before freezing if desired.

Because the partition is applied only to the base index,

\[
\sum_j A_{j,h}
=\sum_{d\asymp D}\mu(d)\mu(d+h)
\]

exactly.

For any real lag sequence `A_{j,h}`, define

\[
J_j(\alpha)
:=\sum_{h\ge1}A_{j,h}
\frac{\sin(2\pi h\alpha)}{\pi h},
\]

\[
L_j(\alpha)
:=\sum_{h\ge1}A_{j,h}
\frac{1-\cos(2\pi h\alpha)}{2\pi^2h^2}.
\]

The endpoint formula for `F` gives algebraically

\[
\boxed{
2\operatorname{Re}\sum_{h\ge1}A_{j,h}F(\alpha_jh)
=
\frac{2}{\alpha_j}
\left[
\sqrt2\,J_j(\sqrt2\alpha_j)-J_j(\alpha_j)
\right]
+
\frac{2}{\alpha_j^2}
\left[
L_j(\alpha_j)-L_j(\sqrt2\alpha_j)
\right].
}
\]

This identity does not require `A_{j,h}` to be an autocorrelation of a separately truncated block. Therefore the partition can preserve all original cross-block pairs while still exposing the primitive boundary structure locally.

Classification:

`LAG_PARTITION_PRIMITIVE_IDENTITY`.

## 7. What is now removed from Sector A
The following are no longer the primary difficulties in `Q>=D^(1/3)`:

1. outer-`n` discreteness in the hard near cell;
2. slow variation of `d/D` across a local block;
3. cross-block terms caused by splitting the original exponential sum before squaring.

All three can be handled without a power loss by working on the lag side.

## 8. Remaining Sector-A problem
After the controlled reductions, the hard contribution is reduced to a sum of local signed functionals of the form

\[
\frac{Q}{\alpha_j}
[\sqrt2 J_j(\sqrt2\alpha_j)-J_j(\alpha_j)]
+
\frac{Q}{\alpha_j^2}
[L_j(\alpha_j)-L_j(\sqrt2\alpha_j)],
\]

with

\[
\alpha_j\asymp H^{-1}.
\]

The remaining question is purely arithmetic:

> can these dilation differences be bounded at total diagonal scale using information weaker than a uniform square-root bound for Mertens increments or the full diagonal short-interval Möbius variance law?

A proof that answers this positively would remove the generic `H` loss in Sector A while preserving the reciprocal cross-scale compensation that is destroyed by absolute lag estimates.
