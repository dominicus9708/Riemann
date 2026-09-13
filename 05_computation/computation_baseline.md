# Computation Baseline: Z(t), Riemann–Siegel, Gram Points, Completeness

## 1. Hardy Z-function

For real t define

\[
Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right),
\]

with the Riemann–Siegel theta function chosen so that \(Z(t)\in\mathbb R\).

Then

\[
|Z(t)|=\left|\zeta\!\left(\frac12+it\right)\right|,
\]

so critical-line zeros can be sought as real zeros of Z.

Reference baseline: NIST DLMF §25.10.

## 2. Riemann–Siegel formula

DLMF gives the standard form

\[
Z(t)=2\sum_{n=1}^{m}\frac{\cos(\vartheta(t)-t\log n)}{\sqrt n}+R(t),
\qquad
m=\left\lfloor\sqrt{\frac{t}{2\pi}}\right\rfloor,
\]

with

\[
R(t)=O(t^{-1/4}).
\]

Status: `THEOREM_ESTABLISHED`.

Audit warning: the displayed big-O statement is not, by itself, a numerical interval bound with a known constant at a chosen finite t. Certified computation requires an explicit remainder enclosure.

## 3. Gram points

Gram points \(g_n\) satisfy

\[
\vartheta(g_n)=n\pi.
\]

A common empirical pattern is

\[
(-1)^n Z(g_n)>0,
\]

which is one version of Gram's law.

This is **not a theorem valid for all n** and must never be used as a completeness axiom.

## 4. Deliberate failure fixture

A direct high-precision scan of \(0\le n<300\) reproduced the following bad Gram points, where the expected sign fails:

\[
126,\ 134,\ 195,\ 211,\ 232,\ 254,\ 288.
\]

The first failure is

\[
g_{126}\approx282.45472082346217461084,
\]

with

\[
Z(g_{126})\approx-0.0276294988571999367,
\]

although \(126\) is even.

Status: `NUMERICAL_EXPERIMENTAL / AUDIT_FIXTURE`.

This is intentionally stored because a pattern that works for the first 126 cases and then fails is exactly the kind of false generalization the repository must detect.

## 5. Zero finding versus zero certification

These are different tasks.

### Finding
- sample Z(t),
- bracket sign changes,
- refine roots,
- obtain candidate ordinates \(\gamma_n\).

### Certification
- prove numerical enclosures,
- count *all* zeros in the strip up to T,
- compare the total count with critical-line zeros,
- rule out missed zeros and numerical ambiguity.

A root finder alone performs the first task, not the second.

## 6. Turing-type completeness logic

Modern rigorous computations use zero-counting/completeness machinery rather than relying solely on Gram's law. LMFDB states that its large zeta-zero dataset was computed by David Platt and that completeness was verified using a rigorous version of Turing's method.

Platt (2017) reports rigorous isolation of nontrivial zeros through height 30,610,046,000 to absolute precision ±2^-102. Platt & Trudgian (2021) later report a rigorous interval-arithmetic verification of RH up to height 3×10^12.

Repository classification:

- interval/Turing certified finite range → `NUMERICAL_RIGOROUS`
- ordinary high-precision root list → `NUMERICAL_EXPERIMENTAL`
- neither class → global RH proof

## 7. Source audit

### DLMF §§25.10, 25.18
Accepted for formulas and classical computational method references. Numerical-history sentences dated 2008 are not used as current records.

### Platt 2017
Peer-reviewed primary research source for a rigorous zero-isolation algorithm and a large certified range. Suitable for later implementation design. The repository still requires independent understanding of its error-enclosure and completeness steps before treating a reimplementation as certified.

### Platt & Trudgian 2021
Peer-reviewed finite-height verification using interval arithmetic. Strong current baseline for the distinction between rigorous finite verification and global proof.

### LMFDB
Useful external dataset/provenance layer, but its zeta-zero knowl pages visibly carry beta/awaiting-review status. We therefore trace important claims back to the primary Platt work where possible.

## 8. Minimum computation gate before proof-family comparison

The following must be implemented or explicitly sourced before major proof approaches are compared:

1. independent zeta evaluation at generic complex points;
2. Z(t) evaluation;
3. zero bracketing/refinement;
4. N(T) count comparison;
5. Gram-point scan including known failures;
6. numerical precision/error metadata;
7. external dataset cross-check;
8. a path toward rigorous interval/Turing certification for selected ranges.

## References

- NIST DLMF §25.10: https://dlmf.nist.gov/25.10
- NIST DLMF §25.18: https://dlmf.nist.gov/25.18
- D. J. Platt, “Isolating some non-trivial zeros of zeta”, Mathematics of Computation 86 (2017), 2449–2467, DOI 10.1090/mcom/3198.
- D. Platt and T. Trudgian, “The Riemann hypothesis is true up to 3·10^12”, Bulletin of the London Mathematical Society 53 (2021), 792–797, DOI 10.1112/blms.12460.
- LMFDB zeta-zero source/completeness notes.
