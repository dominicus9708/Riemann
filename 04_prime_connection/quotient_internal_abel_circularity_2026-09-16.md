# Quotient-internal Abel circularity audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Internal summation-by-parts identity: EXACT.
- Linear/dyadic kernel-increment route: CLOSED AS RE-ENCODING.
- Nonlinear multi-scale interaction: still OPEN in principle.

## 1. Large-d quotient side

In the square-root/general hyperbola split, the large-d contribution has the form

\[
C(N;K)
=
\sum_{q\le Q}b(q)M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-M(K)B(Q),
\]

where

\[
B(q)=\sum_{r\le q}b(r),
\qquad
Q=\left\lfloor\frac{N}{K+1}\right\rfloor.
\]

Set

\[
A_q=M\!\left(\left\lfloor\frac Nq\right\rfloor\right).
\]

## 2. Exact Abel transform

Since `b(q)=B(q)-B(q-1)`, discrete summation by parts gives

\[
\boxed{
\sum_{q\le Q}b(q)A_q
=B(Q)A_Q+
\sum_{q=1}^{Q-1}B(q)(A_q-A_{q+1}).
}
\]

Therefore

\[
\boxed{
C(N;K)
=B(Q)(A_Q-M(K))
+
\sum_{q=1}^{Q-1}B(q)
\left[
M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-M\!\left(\left\lfloor\frac N{q+1}\right\rfloor\right)
\right].
}
\]

The bracket is exactly the previously audited quotient Mertens block increment.

The first boundary term is also just the Mertens mass in the final truncated quotient interval.

## 3. Consequence

Any argument that tries to exploit the summatory cancellation of `b(q)` by one more linear Abel transform returns exactly to the `B(q)`-weighted Mertens block representation.

Likewise, applying the same transform separately on dyadic q-bands produces only band-boundary terms plus the same block increments inside each band.

Thus there is no new linear reserve hidden in the passage

\[
b(q)\longleftrightarrow B(q).
\]

Classification:

`QUOTIENT_INTERNAL_ABEL_CIRCULARITY`.

## 4. Component convolution closure

The special kernel

\[
b=\log-\tau+2\gamma\mathbf1
\]

has components satisfying

\[
\mu*\log=\Lambda,
\qquad
\mu*\tau=\mathbf1,
\qquad
\mu*\mathbf1=\delta.
\]

Hence componentwise linear recombination also closes exactly to

\[
\mu*b=\Lambda-\mathbf1+2\gamma\delta.
\]

Therefore a cancellation discovered solely by splitting `b` into its three linear components is an exact convolution identity, not a new mechanism.

Classification:

`KERNEL_COMPONENT_CONVOLUTION_CLOSURE`.

## 5. Surviving scope

After this audit, a genuinely new quotient-side mechanism must be nonlinear or use additional arithmetic information not present in generic linear summation by parts.

Examples of admissible future questions include:
- scale-dependent nonlinear inequalities between several quotient bands;
- arithmetic constraints coupling divisor/Voronoi phases to Mertens block signs;
- stopping-time or energy structures not reducible to a fixed linear transform.

Any candidate that becomes a single linear Abel transform, dyadic telescoping identity, or componentwise convolution identity is closed by this audit.
