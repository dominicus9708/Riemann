# Zero Structure Baseline

## 1. Regions

For \(s=\sigma+it\):

- \(\sigma>1\): \(\zeta(s)\ne0\) from the convergent Euler product.
- \(\sigma=1\): zero-free; this classical fact is part of the proof of the prime number theorem.
- \(0<\sigma<1\): the critical strip; infinitely many nontrivial zeros occur here.
- \(\sigma\le0\): apart from the trivial zeros at negative even integers, there are no zeros.

Status: `THEOREM_ESTABLISHED`.

Reference baseline: NIST DLMF §25.10.

## 2. Trivial zeros

The functional equation gives

\[
\zeta(-2n)=0,\qquad n=1,2,3,\ldots
\]

These are the trivial zeros.

Audit rule: trivial zeros are never counted as evidence for or against RH, which concerns the nontrivial zeros.

## 3. Nontrivial-zero symmetry

The nontrivial-zero set is symmetric about both

\[
\operatorname{Im}(s)=0
\]

and

\[
\operatorname{Re}(s)=\frac12.
\]

Thus a generic off-line zero generates the quartet

\[
\rho,\quad \bar\rho,\quad1-\rho,\quad1-\bar\rho.
\]

This structure is fully compatible with RH being false. Symmetry is therefore a constraint on counterexamples, not a proof of RH.

## 4. Critical-line zeros

Define

\[
Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right).
\]

For real \(t\), \(Z(t)\) is real and has the same zeros as \(\zeta(1/2+it)\). Sign changes can therefore isolate odd-multiplicity critical-line zeros.

DLMF states that \(Z(t)\) changes sign infinitely often, hence infinitely many zeta zeros lie on the critical line.

Status: `THEOREM_ESTABLISHED`, but this is strictly weaker than RH.

## 5. Multiplicity audit

A sign change detects an odd multiplicity zero, but absence of a sign change is not by itself proof that no zero occurs in an interval: an even-multiplicity zero need not change sign.

Therefore a complete zero-counting procedure must not equate `number of observed sign changes` with `number of all zeros` without an independent completeness/counting argument.

Audit label: `SIGN_CHANGE_COMPLETENESS_TRAP`.

## 6. Finite verification status

A peer-reviewed result by Platt and Trudgian (2021) reports a rigorous interval-arithmetic verification that every nontrivial zero with

\[
0<\gamma\le3\times10^{12}
\]

has \(\beta=1/2\), and reports these zeros as simple in that range.

Status in this repository: `NUMERICAL_RIGOROUS`, not `THEOREM_GLOBAL_RH`.

The logical distinction is essential:

\[
\forall \rho\;(0<\gamma\le T \Rightarrow \beta=1/2)
\]

for finite \(T\) does not imply

\[
\forall \rho\;(\beta=1/2).
\]

## 7. Source audit

### NIST DLMF §25.10
- accepted for standard zero-region and Z(t) facts;
- its historical numerical-record statements are not automatically treated as the 2026 latest record;
- useful because formulas are linked to classical sources and errata.

### Platt & Trudgian (2021)
- peer-reviewed research article;
- claim is explicitly finite-height and based on rigorous interval arithmetic;
- suitable as a modern finite-verification reference;
- not a global proof and must never be promoted to one by extrapolation.

## References

- NIST DLMF §25.10: https://dlmf.nist.gov/25.10
- D. Platt and T. Trudgian, “The Riemann hypothesis is true up to 3·10^12”, Bulletin of the London Mathematical Society 53 (2021), 792–797, DOI 10.1112/blms.12460.
