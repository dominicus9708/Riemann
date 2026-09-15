# Chow-Halfspace Scope Correction for the K-wise Parity Barrier

Date: 2026-09-15

## why this correction is necessary

Earlier information audits used the exact Boolean fact that on K+1 bits the even-parity and odd-parity distributions have identical marginals on every proper subset. This correctly shows that **arbitrary Boolean data** can hide global parity from all fixed-K local statistics.

However the arithmetic cutoff is not an arbitrary Boolean function.

For primes p<=Y with Y>=X, define y_p in {0,1} and

\[
f_X(y)=\mathbf1_{\{\sum_p y_p\log p\le\log X\}}.
\]

This is a linear threshold function (LTF / halfspace).

C. K. Chow's theorem says an LTF is uniquely determined, even among all bounded Boolean-cube functions, by its degree-0 and degree-1 Fourier coefficients (its Chow parameters).

Therefore the generic K-wise parity ambiguity **cannot be promoted to an information-theoretic impossibility theorem inside the LTF class**.

The earlier barrier remains valid only as:

- a null-model / unrestricted-Boolean guard;
- a warning that low-order statistics need the halfspace constraint to recover parity;
- not a proof that arithmetic degree-0/1 data fail to determine the cutoff.

## arithmetic Chow parameters

In 0/1 coordinates the unnormalized degree-0 count is simply the number of feasible squarefree states

\[
C_0(X)=Q(X)=\#\{n\le X:\mu(n)^2=1\}.
\]

For a prime p, the coordinate count for states containing p is

\[
C_p(X)
=\#\{n\le X:\mu(n)^2=1,\ p\mid n\}
=\#\{m\le X/p:\mu(m)^2=1,(m,p)=1\}.
\]

Thus the exact Chow vector is arithmetic and contains all singleton occupancy counts.

Chow uniqueness says this exact vector determines the entire threshold support and hence in principle also its top parity coefficient M(X).

This is an existence/identifiability statement, not a useful analytic bound by itself.

## tiny arithmetic margin

Because all feasible subset products are positive integers, replace the threshold log X by

\[
\theta_X=\log(X+1/2).
\]

This leaves the Boolean cutoff unchanged: product <=X iff log(product)<theta_X.

The minimum absolute margin is

\[
\gamma_X
=\min\left\{
\log\frac{X+1/2}{X},
\log\frac{X+1}{X+1/2}
\right\}
\sim\frac1{2X}.
\]

Let g be any bounded function [0,1] on the same cube. Pointwise,

\[
(f_X-g)(\theta_X-\sum_py_p\log p)
\ge \gamma_X|f_X-g|.
\]

Summing over the cube gives the quantitative form of Chow's elementary argument:

\[
\gamma_X\sum_y|f_X(y)-g(y)|
\le
\theta_X|\Delta C_0|
+\sum_{p\le Y}(\log p)|\Delta C_p|,
\]

where Delta C_0 and Delta C_p are the unnormalized degree-0 and coordinate-count discrepancies.

Hence

\[
\boxed{
\|f_X-g\|_{\ell^1}
\le
\gamma_X^{-1}
\left(
\theta_X|\Delta C_0|
+\sum_p(\log p)|\Delta C_p|
\right).
}
\]

Since gamma_X^{-1}~2X, Chow reconstruction is extremely ill-conditioned at the arithmetic threshold.

## consequence for parity control by Hamming reconstruction

The parity-sum discrepancy satisfies trivially

\[
\left|\sum_y(f_X-g)(y)(-1)^{|y|}\right|
\le\sum_y|f_X-g|.
\]

Therefore a strategy that first reconstructs the threshold support from approximate Chow data and then controls the top parity coefficient by Hamming/L1 distance would need

\[
\theta_X|\Delta C_0|+\sum_p(\log p)|\Delta C_p|
\lesssim \gamma_X X^{1/2}
\asymp X^{-1/2}
\]

to reach an O(sqrt(X)) parity bound.

For integer counting approximations this is essentially exact-data precision.

This does **not** rule out a more delicate signed functional of the Chow errors that uses cancellation. It rules out the straightforward robust-Chow + L1/Hamming route as an RH-scale mechanism.

## revised verdict

### retain

- generic K-wise parity invisibility as a null-model and unrestricted-Boolean information guard;
- fixed-K raw correlation failures found numerically.

### correct

- do not state that low-order prime-label data information-theoretically cannot determine the arithmetic cutoff: exact degree-0/1 data do determine any halfspace by Chow's theorem.

### close

- approximate Chow reconstruction followed by absolute Hamming/L1 control, because the arithmetic margin is only ~1/(2X).

### remaining possibility

A useful low-order route would have to exploit a **signed, arithmetic-specific functional of the exact Chow parameters** without converting first to support Hamming error. No such RH-scale inequality is presently established.

## literature

- C. K. Chow (1961), threshold functions uniquely determined by degree-0/1 Fourier data.
- Ryan O'Donnell and Rocco Servedio, *The Chow Parameters Problem*, SIAM J. Comput. 40 (2011).
- Anindya De, Ilias Diakonikolas, Vitaly Feldman, Rocco Servedio, *Nearly optimal solutions for the Chow Parameters Problem and low-weight approximation of halfspaces*, STOC 2012 / later journal version.
