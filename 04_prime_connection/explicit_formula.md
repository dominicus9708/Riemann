# Prime Distribution and the Zeta-Zero Explicit Formula

## 1. Chebyshev psi function

Define

\[
\Lambda(n)=
\begin{cases}
\log p,&n=p^k\text{ for a prime }p\text{ and }k\ge1,\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
\psi(x)=\sum_{n\le x}\Lambda(n)
      =\sum_{p^m\le x}\log p.
\]

Status: `THEOREM_ESTABLISHED / STANDARD_DEFINITION`.

NIST DLMF §25.16 uses the equivalent prime-power definition.

## 2. Zeta connection

For \(\operatorname{Re}(s)>1\), logarithmic differentiation of the Euler product gives

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s}.
\]

This is one of the main structural bridges between primes and zeta.

Audit rule: as with the Euler product, this Dirichlet series must not be used outside its convergence region without a justified continuation/contour argument.

## 3. Explicit formula

A standard form, for \(x>1\) away from prime-power jump points, is

\[
\psi(x)
= x-\sum_{\rho}\frac{x^{\rho}}{\rho}
-\log(2\pi)
-\frac12\log(1-x^{-2}),
\]

where the sum runs over nontrivial zeros with the required symmetric limiting prescription.

DLMF records the asymptotic form

\[
\psi(x)=x-\frac{\zeta'(0)}{\zeta(0)}
-\sum_{\rho}\frac{x^\rho}{\rho}+o(1),
\]

and states the RH equivalence

\[
\boxed{\mathrm{RH}\iff
\psi(x)=x+O(x^{1/2+\varepsilon})
\text{ for every }\varepsilon>0.}
\]

Status: `THEOREM_ESTABLISHED`.

## 4. Why this matters for pattern analysis

A proposed pattern among \(\gamma_n\) should not be judged only by its fit to the zero table. The explicit formula gives a second domain in which consequences can be checked:

\[
\{\rho\}\longrightarrow\psi(x)-x.
\]

A claimed zero law that implies a prime-distribution behavior contradicting known bounds can therefore be rejected even if it numerically fits a limited zero sample.

## 5. Initial direct/truncated experiment

Direct \(\psi(x)\) values were computed from prime powers and compared with a naive symmetric truncation of the explicit zero sum using the first N positive critical-line zeros.

At \(x=100.5\):

- direct: \(94.04531122935739\ldots\)
- 10 zero pairs: \(95.77622089465242\ldots\)
- 50 zero pairs: \(94.90500701056198\ldots\)
- 200 zero pairs: \(93.90977856342219\ldots\)

At \(x=1000.5\):

- direct: \(996.68091224717524\ldots\)
- 10 zero pairs: \(997.76951239799401\ldots\)
- 50 zero pairs: \(994.73278148581294\ldots\)
- 200 zero pairs: \(996.04839861917285\ldots\)

Status: `NUMERICAL_EXPERIMENTAL / REGRESSION_ONLY`.

## 6. Audit result from the experiment

The truncation error does **not** decrease monotonically with the number of included zeros. This is expected because the zero sum is not an ordinary absolutely convergent positive-term approximation.

Therefore the following inference is prohibited:

`more zero terms -> monotone convergence -> observed residual is a rigorous bound`.

Any later use of the explicit formula for certified inequalities must use a theorem with an explicit truncation prescription and error term.

## 7. Further audit traps

- At a prime power, \(\psi(x)\) has a jump; endpoint conventions matter.
- The sum over zeros must specify the ordering/limiting convention.
- Replacing \(x^\rho\) by \(x^{1/2+i\gamma}\) assumes RH and therefore contaminates an attempted proof if RH has not already been established in the relevant step.
- A finite list of on-line zeros may be used for experiment but cannot replace the full zero sum in a theorem without a tail bound.

## References

- NIST DLMF §25.16: https://dlmf.nist.gov/25.16
- Encyclopedia of Mathematics, “Zeta-function” / “Distribution of prime numbers”, for standard explicit-formula formulations and historical context.
- Classical references cited by DLMF: Apostol and standard analytic-number-theory monographs.
