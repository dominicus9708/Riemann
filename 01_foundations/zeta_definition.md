# Riemann Zeta Function — Definition and Domain Audit

## 1. Dirichlet-series definition

For

\[
\operatorname{Re}(s)>1,
\]

the Riemann zeta function is

\[
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}.
\]

Status: `THEOREM_ESTABLISHED / STANDARD_DEFINITION_ON_HALF-PLANE`

Primary standard reference used here: NIST DLMF §25.2.

## 2. Analytic continuation

Outside the half-plane \(\operatorname{Re}(s)>1\), the same Dirichlet series is not taken as the global definition. The zeta function is extended by analytic continuation and is meromorphic on \(\mathbb C\), with a unique simple pole at

\[
s=1
\]

with residue 1.

Status: `THEOREM_ESTABLISHED`

### Audit warning A — domain leakage

The identity

\[
\zeta(s)=\sum_{n=1}^{\infty}n^{-s}
\]

must not be used as an ordinarily convergent series when \(\operatorname{Re}(s)\le 1\). A derivation that substitutes a critical-strip value directly into this series without a valid continuation/summation argument is rejected.

## 3. Euler product

For

\[
\operatorname{Re}(s)>1,
\]

\[
\zeta(s)=\prod_{p}(1-p^{-s})^{-1},
\]

where the product is over all primes.

Status: `THEOREM_ESTABLISHED`

### Audit consequence

Because the Euler product converges in \(\operatorname{Re}(s)>1\), zeta has no zeros there. This statement is local to the product's valid domain; the product may not be formally extended into the critical strip without additional justification.

### Audit warning B — illegal product extension

A proof candidate is invalid if it argues that each Euler factor is nonzero and therefore \(\zeta(s)\ne0\) in a region where the Euler product is not known to converge in the required sense.

## 4. Computational cross-check target

The repository should independently verify at selected points with \(\operatorname{Re}(s)>1\):

1. Dirichlet partial sums → \(\zeta(s)\)
2. truncated Euler products → \(\zeta(s)\)
3. an analytic-continuation implementation → the same value

Agreement alone is not a proof of the global identities; it is a regression test for implementation errors.

## 5. Initial independently reproduced checks

Using high-precision arithmetic during repository initialization:

- at \(s=2\), \(\zeta(2)\approx1.6449340668482264\); an Euler product over primes \(p\le10000\) gives approximately \(1.6449179207462864\). The nonzero truncation error is expected and must not be mistaken for formula failure.
- at \(s=3+2i\), the same prime cutoff gives an absolute discrepancy of approximately \(3.64\times10^{-10}\) from the high-precision zeta evaluation.

Status: `NUMERICAL_EXPERIMENTAL / REGRESSION_ONLY`

These numbers are not used as mathematical evidence for RH.

## 6. References

- NIST DLMF §25.2, Definition and Expansions: https://dlmf.nist.gov/25.2
- DLMF cites Apostol (1976), Riemann (1859), Ivić (1985), and Titchmarsh for the corresponding classical formulas.
