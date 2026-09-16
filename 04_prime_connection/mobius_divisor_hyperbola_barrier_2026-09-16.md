# Möbius–divisor hyperbola split barrier — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Square-root/general hyperbola split: EXACT.
- New cross-boundary reserve from the split: NONE; generic Dirichlet-hyperbola reorganization.
- Two-sided absolute exponent optimum: EXACT scale calculation.
- One-sided positivity of the divisor kernel: CLOSED by divisor-error sign changes.
- Surviving route: genuinely signed cross-boundary correlation only.

## 1. Exact general split

Recall

\[
T(N)=\sum_{d\le N}\mu(d)B\!\left(\left\lfloor\frac Nd\right\rfloor\right)
=\psi(N)-N+2\gamma,
\]

where

\[
b(q)=B(q)-B(q-1)=\log q-\tau(q)+2\gamma.
\]

Choose an integer cutoff `1<=K<N` and set

\[
Q=\left\lfloor\frac{N}{K+1}\right\rfloor.
\]

Splitting the original `d`-sum at `K` and interchanging the two finite sums in the `d>K` region gives exactly

\[
\boxed{
T(N)
=
\sum_{d\le K}\mu(d)B\!\left(\left\lfloor\frac Nd\right\rfloor\right)
+
\sum_{q\le Q}b(q)M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-
M(K)B(Q).
}
\]

For `K~sqrt(N)`, the first piece is the high-quotient / small-`d` divisor-kernel side and the second is the low-quotient / large-`d` Mertens side.

This is a standard Dirichlet-hyperbola partition of the same convolution. No additional reserve or positivity term is created at the boundary.

Classification:

`DIVISOR_MOBIUS_HYPERBOLA_REENCODING`.

## 2. General absolute exponents

Let

\[
K=N^\kappa,
\qquad 0<\kappa<1.
\]

Assume schematic power bounds

\[
B(y)=O(y^\alpha L_B(y)),
\qquad
M(y)=O(y^\beta L_M(y)),
\]

with subpower factors suppressed in the exponent calculation. Since

\[
b(q)=\log q-\tau(q)+2\gamma=q^{o(1)},
\]

termwise absolute control gives for the small-`d` side

\[
\left|
\sum_{d\le K}\mu(d)B(N/d)
\right|
\lesssim
N^\alpha K^{1-\alpha},
\]

with power exponent

\[
E_1=\alpha+\kappa(1-\alpha).
\]

For the large-`d` / low-quotient side,

\[
\sum_{q\le N/K}|b(q)|\,|M(N/q)|
\lesssim
N^\beta (N/K)^{1-\beta+o(1)},
\]

with exponent

\[
E_2=1-\kappa(1-\beta).
\]

The boundary term `M(K)B(N/K)` has exponent

\[
E_3=\kappa\beta+(1-\kappa)\alpha,
\]

and for `beta<1` it is below `E_1` at positive `kappa`.

## 3. Optimized absolute barrier

Balancing the two dominant exponents,

\[
E_1=E_2,
\]

gives

\[
\boxed{
\kappa_*=\frac{1-\alpha}{2-\alpha-\beta}.
}
\]

The optimized exponent is

\[
\boxed{
E_{\rm opt}
=\frac{1-\alpha\beta}{2-\alpha-\beta}.
}
\]

This formula makes the obstruction explicit.

If `alpha,beta>=0` and both are at most `1/2`, then

\[
E_{\rm opt}\ge\frac12,
\]

with equality only at the degenerate endpoint `alpha=beta=0`. Indeed

\[
E_{\rm opt}\le\frac12
\iff
\alpha+\beta\le2\alpha\beta,
\]

which fails for any nonzero `alpha,beta in [0,1/2]`.

Thus a termwise absolute hyperbola proof cannot reach square-root scale from any nontrivial positive power bounds on both components.

Classification:

`TWO_SIDED_HYPERBOLA_ABSOLUTE_BARRIER`.

## 4. Divisor-problem consequences

The current sharpest announced pointwise divisor bound is the Li–Yang exponent

\[
\alpha_*\approx0.3144831759741,
\]

improving Huxley's `131/416`; this remains a preprint result as of the present audit.

At the symmetric split `kappa=1/2`, the small-`d` piece alone has absolute exponent

\[
\frac{1+\alpha_*}{2}\approx0.6572416.
\]

Even granting the conjectural divisor exponent

\[
\alpha=\frac14,
\]

the same piece is only reduced to

\[
\boxed{N^{5/8+\varepsilon}},
\]

still above the RH square-root scale.

More strongly, even if one hypothetically had `M(x)=O(1)` (`beta=0`) while retaining the conjectural divisor exponent `alpha=1/4`, the optimized termwise-absolute split gives

\[
E_{\rm opt}=\frac{1}{2-1/4}=\frac47>\frac12.
\]

This is a limitation of this decomposition and absolute estimation, not a statement that such an unrealistically strong Mertens bound would be insufficient by other methods.

## 5. Positivity is unavailable

Since

\[
B(y)=S(y)-\Delta(y),
\qquad
S(y)=O(\log y),
\]

and the classical divisor error `Delta(y)` changes sign infinitely often with fluctuations of at least quarter-power scale, the kernel `B(y)` cannot have an eventual fixed sign.

Therefore neither half of the hyperbola split supplies a one-sided positive kernel that could replace signed cancellation.

Permanent guard:

`DIVISOR_KERNEL_SIGN_CHANGE_GUARD`.

## 6. Current consequence

The `sqrt(N)` split has now been fully audited:

- exact split: generic hyperbola identity;
- small-`d` absolute divisor control: exponent too large;
- large-`d` absolute Mertens control: exponent too large;
- boundary term: not a new reserve;
- kernel positivity: unavailable.

Hence the only surviving possibility inside this bridge is a **signed cross-boundary compensation** between the divisor/Voronoi and Mertens components.

Any proposed compensation must use the special arithmetic phase/order information of the two pieces; if it follows from triangle inequality, Cauchy–Schwarz without a new correlation input, or a second Abel/hyperbola rearrangement, close it as re-encoding.

Suggested tag:

`DIVISOR_MOBIUS_CROSS_BOUNDARY_SIGNED_OPEN`.
