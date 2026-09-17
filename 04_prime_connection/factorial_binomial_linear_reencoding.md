# Factorial / binomial additive-lattice audit

Status: `EXACT REENCODING` for the linear valuation layer.

## Legendre valuation identity
For every integer n>=1,

\[
\log(n!)=\sum_p\sum_{k\ge1}\left\lfloor\frac{n}{p^k}\right\rfloor\log p.
\]

Taking the first difference in n gives

\[
\log n
=\sum_{p^k\mid n}\log p
=\sum_{d\mid n}\Lambda(d).
\]

Hence, as an arithmetic-function identity,

\[
\boxed{\log=\mathbf 1*\Lambda.}
\]

Möbius inversion recovers

\[
\Lambda=\mu*\log.
\]

Thus any linear manipulation of the factorial valuation table is information-equivalent to the standard von Mangoldt convolution chain.

## Binomial coefficients
Since

\[
\log {n\choose k}=\log(n!)-\log(k!)-\log((n-k)!),
\]

linear statistics of log-binomial coefficients remain in the same linear factorial/Mangoldt information class. They do not create an independent RH-scale observable.

## What is not closed
Nonlinear carry/residue information, such as Kummer/Lucas-type patterns in p-adic valuations of binomial coefficients, is not covered by this reduction. Such a route would have to use the residue/carry geometry essentially; otherwise it collapses back to the identity above.

Classification:

`LINEAR_FACTORIAL_BINOMIAL -> REENCODING_OF_LAMBDA`.
