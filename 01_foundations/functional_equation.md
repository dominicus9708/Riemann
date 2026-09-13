# Xi Function and Functional Equation Audit

## 1. Definition

Define Riemann's xi function by

\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s).
\]

The standard functional equation is

\[
\xi(s)=\xi(1-s).
\]

Status: `THEOREM_ESTABLISHED`

Reference: NIST DLMF §25.4.

An equivalent reflection form for zeta is

\[
\zeta(s)=2(2\pi)^{s-1}\sin\!\left(\frac{\pi s}{2}\right)\Gamma(1-s)\zeta(1-s),
\]

with the usual exclusions/continuation interpretation at singular points.

## 2. Immediate structural consequences

Together with complex conjugation symmetry, the functional equation gives the familiar nontrivial-zero symmetry: if \(\rho\) is a nontrivial zero, the corresponding reflected/conjugated points occur according to

\[
\rho,\qquad 1-\rho,\qquad \overline\rho,\qquad 1-\overline\rho.
\]

Degeneracies occur when a zero already lies on a symmetry axis.

## 3. Critical audit: symmetry is not RH

The implication

\[
\text{zero set symmetric about }\operatorname{Re}(s)=\frac12
\]

is **not** equivalent to

\[
\text{every zero lies on }\operatorname{Re}(s)=\frac12.
\]

An off-line zero \(\beta+i\gamma\) with \(\beta\ne1/2\) is compatible with symmetry provided the reflected partners also occur. Therefore any proof candidate whose decisive step is merely `the zeros are symmetric, hence each zero is on the symmetry line` fails.

Audit label: `HARD_REJECTION_TEST: SYMMETRY_AXIS_FALLACY`.

## 4. Initial numerical regression

High-precision initialization tests evaluated

\[
\xi(s)-\xi(1-s)
\]

at several generic complex points. With 80-decimal-digit arithmetic, residual magnitudes were on the order of \(10^{-81}\) to \(10^{-82}\).

Status: `NUMERICAL_EXPERIMENTAL / IMPLEMENTATION_REGRESSION_ONLY`.

This is an implementation check, not evidence for RH.

## 5. Dependency audit

When using the functional equation later, record which representation is being used and whether gamma factors, poles, zeros of sine/cosine factors, and analytic continuation have been handled correctly. Formal cancellation at a singular point is not automatically valid.

## 6. References

- NIST DLMF §25.4, Reflection Formulas: https://dlmf.nist.gov/25.4
- NIST DLMF §25.10, Zeros: https://dlmf.nist.gov/25.10
