# j=2 exact tail recombination and two-factor boundary layer — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: after support localization of Type-II and cumulative second-Type-I coefficients.
- New exact algebraic compression:
  \[
  A_1=\Lambda*b_H,\qquad
  A_2=\Lambda_{\le H}*b_H,
  \]
  and the Type-II term is the negative \(k>H\) tail of
  \[
  \Lambda_{>H}*b_H.
  \]
- Therefore on the tail,
  \[
  -A_{2,\rm tail}+T_{II}
  =
  -(\Lambda*b_H)_{\rm tail}
  =
  -A_{1,\rm tail}.
  \]
- Interpretation: the central signed problem is a single factorable convolution with an exact head-tail projection, not three unrelated Vaughan branches.
- After the new support lemmas, the hardest part of this tail is the exactly-two-small-factor boundary
  \[
  b_H(rs)=-1.
  \]
- Classification: \`J2_TWO_FACTOR_TAIL_BOUNDARY_LAYER\`.

## 1. Restricted Möbius convolution

Define
\[
b_H:=\mu_{\le H}*1.
\]

Thus
\[
b_H(k)
=
\sum_{\substack{d\mid k\\d\le H}}\mu(d).
\]

Since
\[
L=\Lambda*1,
\]
the first Type-I convolution is
\[
A_1
=
\mu_{\le H}*L
=
\mu_{\le H}*\Lambda*1
=
\boxed{\Lambda*b_H}.
\]

Similarly,
\[
A_2
=
\mu_{\le H}*\Lambda_{\le H}*1
=
\boxed{\Lambda_{\le H}*b_H}.
\]

Hence
\[
A_1-A_2
=
\boxed{\Lambda_{>H}*b_H}.
\]

## 2. Head-tail split

Split the convolution variable k in
\[
(\Lambda_{>H}*b_H)(q)
=
\sum_{ek=q}\Lambda_{>H}(e)b_H(k)
\]
according to
\[
k\le H
\quad\text{or}\quad
k>H.
\]

The Vaughan Type-II term is exactly
\[
\boxed{
T_{II}
=
-\bigl(\Lambda_{>H}*b_H\bigr)_{\rm tail}.
}
\]

Therefore
\[
A_1-A_2+T_{II}
=
\bigl(\Lambda_{>H}*b_H\bigr)_{\rm head}.
\]

But for k<=H,
\[
b_H(k)=\delta_{k,1}.
\]

Thus the head is exactly
\[
\Lambda_{>H},
\]
which equals \(\Lambda\) on the H^3 working range.

## 3. Exact tail recombination

Also split A_2 into head and tail.

On k>H,
\[
-A_{2,\rm tail}
+
T_{II}
=
-\bigl(\Lambda_{\le H}*b_H\bigr)_{\rm tail}
-
\bigl(\Lambda_{>H}*b_H\bigr)_{\rm tail}.
\]

Therefore
\[
\boxed{
-A_{2,\rm tail}
+
T_{II}
=
-\bigl(\Lambda*b_H\bigr)_{\rm tail}
=
-A_{1,\rm tail}.
}
\]

Hence the full identity may be viewed as
\[
\boxed{
A_{1,\rm head}
}
\]
after exact cancellation of the complete tail.

This is algebraically tautological but analytically important: all hard tail branches are different decompositions of one and the same convolutional boundary projection.

## 4. Why this does not itself close the sum

The head identity
\[
b_H(k)=\delta_{k,1}
\qquad(k\le H)
\]
collapses the factorization and returns directly to the prime sequence.

Conversely, estimating each tail component separately preserves factor geometry but loses the exact signed projection.

Thus the analytic problem remains:
\[
\boxed{
\text{retain enough factor coordinates to use DLS/dispersion
while preserving the tail subtraction.}
}
\]

This is the same product-kernel quotient obstruction identified earlier.

## 5. Support stratification inside the tail

The new support audits refine the tail.

### >=3 small prime factors

For squarefree H-smooth k with
\[
b_H(k)\ne0
\]
and at least three prime factors, the branch admits
\[
\Delta_H\le1/5,
\]
hence
\[
H^{6+1/10+\varepsilon}.
\]

### Cumulative second-Type-I complement

The exact representation
\[
C_2(k)
=
\sum_{\ell\mid k}
(\log\ell)b_H(k/\ell)
\]
shows that all components with a >=3-factor \(b_H\)-complement satisfy the same H^(1/10) bound after collapsing \(e\ell\).

### Exactly two factors

If
\[
k=rs,\qquad r,s\le H,\qquad rs>H,
\]
then
\[
\boxed{
b_H(rs)=-1.
}
\]

There is no internal restricted-Möbius cancellation.

This is the first tail layer immediately beyond the head cutoff which can retain the sharp product imbalance.

## 6. Boundary-layer interpretation

The remaining hard arithmetic kernel is therefore
\[
\boxed{
\sum_{\substack{r,s\le H\\rs>H}}
(\text{arithmetic weights})
}
\]
inserted into the reciprocal phase through a distinguished Lambda variable.

At the sharp factor scale,
\[
r,s\asymp H^{3/4},
\qquad
e\asymp H^{3/2},
\]
giving the familiar branch pattern
\[
\left\{
\frac32,\frac34,\frac34
\right\}.
\]

Thus the current H^(1/8) architecture is localized to a two-small-factor **boundary layer** of the truncated Möbius convolution.

Classification:
\`J2_H1_8_LOCALIZED_TO_TWO_FACTOR_BOUNDARY_LAYER\`.

## 7. Correct analytic target

The next norm should not attempt to improve all central Vaughan branches.

It only needs to control the signed head-tail projection on the kernel
\[
b_H(rs)=-1.
\]

Equivalent formulations include:
- a signed multiscale DLS for the two-factor boundary;
- a centered E2-type product variance for the \(rs\)-kernel;
- a coefficient-sensitive mixed-Hessian estimate which sees the two factors separately.

This is strictly narrower than a generic weighted 3D Hessian theorem.

Permanent priority:
\`J2_TWO_FACTOR_BOUNDARY_SIGNED_NORM_FIRST\`.
