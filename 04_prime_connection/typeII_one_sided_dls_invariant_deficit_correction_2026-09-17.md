# Type-II one-sided DLS invariant-deficit correction — 2026-09-17

## Status
This note strengthens the earlier file
`typeII_outer_mean_square_cauchy_dls_barrier_2026-09-17.md`.

The earlier lower statement

\[
\text{derived-method deficit}\ge \min(M,L)
\]

is true but far from sharp for the particular standard double-large-sieve bound that was derived there.

The exact algebra exposes an **invariant dense-spacing term** independent of how the factor block is split.

## 1. Starting DLS bound
For

\[
ML=D,
\qquad
F=\frac DH,
\]

the one-sided Cauchy + Bombieri–Iwaniec double-large-sieve calculation gives

\[
\mathcal E
\ll_ε
M F^{1/2}
\left(QM+\frac{Q^2M^2}{F}\right)^{1/2}
\left(L^2+\frac{L^4}{F}\right)^{1/2}
D^ε.
\]

The target is

\[
\mathcal E\ll_ε QD^{1+ε}.
\]

Define the ratio of the displayed method bound to `QD` by `R_M`. Then

\[
R_M
=
\sqrt{\frac{FM}{Q}}
\sqrt{1+\frac{QM}{F}}
\sqrt{1+\frac{L^2}{F}}.
\]

## 2. Exact expansion
Squaring and expanding gives

\[
\begin{aligned}
R_M^2
&=\frac{FM}{Q}
\left(1+\frac{QM}{F}\right)
\left(1+\frac{L^2}{F}\right)\\
&=
M^2
+\frac{D^2}{F}
+\frac{FM}{Q}
+\frac{D^2}{MQ}.
\end{aligned}
\]

Since

\[
F=\frac DH,
\]

the second term is exactly

\[
\boxed{\frac{D^2}{F}=DH.}
\]

Therefore

\[
\boxed{R_M\ge\sqrt{DH}.}
\]

This lower floor is independent of the factor split `D=ML`.

Classification:

`TYPEII_ONE_SIDED_DLS_INVARIANT_DENSE_SPACING_BARRIER`.

## 3. Origin of the invariant loss
It comes from multiplying the dense parts of both spacing counts:

\[
\mathcal B_U
\supset \frac{Q^2M^2}{F},
\qquad
\mathcal B_V
\supset \frac{L^4}{F}.
\]

Inside the standard DLS bound these terms alone give

\[
M\sqrt F
\cdot\frac{QM}{\sqrt F}
\cdot\frac{L^2}{\sqrt F}
=
\frac{QD^2}{\sqrt F}.
\]

Relative to the target `QD`, this is

\[
\frac{D}{\sqrt F}
=\sqrt{DH}.
\]

Thus the obstruction is not merely the outer Cauchy factor and cannot be repaired by making one factor variable small.

## 4. Consequence for alternative factor decompositions
A higher-order Vaughan/Heath–Brown decomposition may expose smaller individual factors, but **if those factors are regrouped and then fed into the same one-sided Cauchy + generic DLS architecture**, the dense-spacing product above survives at the level of the total product `D`.

Therefore simply increasing the number of factor variables does not remove this obstruction.

A successful higher-order decomposition would have to change one of the following ingredients:

1. obtain a spacing count genuinely smaller than the generic dense term;
2. preserve arithmetic coefficient cancellation instead of replacing coefficients by modulus bounds;
3. avoid the one-sided Cauchy/DLS architecture altogether.

## 5. Relation to the product-collapse audit
The invariant `DH` term is consistent with the later observation that

\[
d^{-1/2}w^{-1/2}=(dw)^{-1/2}.
\]

The lifted factor coordinates do not create new independent phase information. Generic spacing counts still see a densely populated image of the original product-frequency geometry, and their dense terms recombine into a quantity depending only on the total product scale `D` and the reciprocal-resolution parameter `H`.

## 6. Permanent correction
The earlier label

`TYPEII_ONE_SIDED_CAUCHY_DLS_BARRIER`

remains valid, but its quantitative summary should be strengthened from

`deficit >= min(M,L)`

to

\[
\boxed{\text{standard derived DLS-bound ratio}\ge\sqrt{DH}.}
\]

This is a statement about the size of the **derived generic upper bound**, not a lower bound for the true Type-II mean square.
