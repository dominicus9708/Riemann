# Riemann Hypothesis Audit Checkpoint — 2026-09-15

## Status

Riemann Hypothesis: `OPEN`.

This checkpoint records the end state of the current DSD / formation-information audit. It is not a proof claim.

---

## 1. Exact information chain retained

\[
\text{primes}
\leftrightarrow \Lambda(n)
\leftrightarrow \psi(x)
\leftrightarrow -\zeta'(s)/\zeta(s)
\leftrightarrow \text{zero/pole data}.
\]

The current program prioritizes information preservation and identifies where averaging, norms, quotienting, or symmetry erase prime-label/parity information.

---

## 2. Main exact structural results obtained in this audit

### A. Formation phase

\[
F(s,z)=\prod_p(1+zp^{-s}),\qquad F(s,-1)=1/\zeta(s).
\]

The exceptional phase `z=-1` is Möbius parity, not an independently discovered RH phase.

### B. Boolean / squarefree structure

Squarefree states form a Boolean prime-channel system and Möbius is the global parity character.

The arithmetic cutoff is a weighted Boolean halfspace

\[
\sum_{p\in S}\log p\le\log X.
\]

### C. K-wise parity invisibility

On a complete Boolean cube, global parity is orthogonal to every proper-subset observable. Even- and odd-parity distributions can share all marginals up to order `K` while having opposite top parity.

Thus fixed/low-order prime-label statistics cannot determine the Möbius parity endpoint in general.

### D. Visible-core exact GCD audit

For exact gcd label `d`, residual prime-label information is seen only through

\[
(\lfloor X/d\rfloor,V_X(d)),
\qquad
V_X(d)=\prod_{p\mid d,\ p\le X/d}p.
\]

In particular singleton labels `p>sqrt(X)` are exactly label-blind within that kernel.

### E. Connected visibility flux

Boolean connected differences remove lower-order masks exactly, but the resulting flux factors into restricted lower-scale Möbius kernels. The apparent half-log `1/2` is generic multiplicative balance geometry, not an RH-specific selection.

### F. Divisibility tensor barrier

Even all nonempty CRT-orthogonal prime-divisibility tensor orders, when used through normalized linear L^2 combinations, collapse to the classical sieve-density scale.

### G. Floor dilation

\[
T_aF_b=F_{a*b}.
\]

Fixed linear floor-dilation is exactly summatory Dirichlet convolution, not a new contraction mechanism.

### H. Scale curvature / Hankel determinants

Finite scale determinants remove individual exponential modes but act as spectral-mode selectors. Published dyadic Mertens curvature is reproduced to high correlation by the first known zeta zeros, so this class is spectral reencoding rather than an independent arithmetic proof mechanism.

### I. Reciprocal hierarchy false control

Formation phase cumulants generate thresholds

\[
1/2,1/3,1/4,\ldots
\]

as ordinary prime-power tail convergence boundaries. Hence appearance of `1/2` alone is not treated as RH evidence.

### J. Reflection-resolution guard

A reflected pair `1/2±delta` can look numerically like exponent `1/2` whenever

\[
|\delta|\log X\lesssim1.
\]

All finite `sigma≈1/2` diagnostics must report this resolution limit and reflected-pair false controls.

### K. Fixed-order parity moment barrier

\[
M(X)=\sum_{j\ge0}(-2)^jB_j(X),
\qquad
B_j=\sum_{n\le X}\mu(n)^2{\omega(n)\choose j}.
\]

Parity on `0,...,m` has exact and uniform sign-preserving polynomial degree `m`. Fixed-order `omega` moments therefore cannot recover full parity.

### L. Topological reencoding

The squarefree cutoff complex satisfies

\[
M(X)=-\widetilde\chi(\Delta_X),
\]

but Björner's shifted-complex theory gives a wedge-of-spheres model with linear total Betti mass. Static topology and natural quota persistence therefore reencode rather than remove the parity cancellation problem.

### M. Prime-boundary signed L^p barrier

For each prime `p`,

\[
M(X)=\sum_{X/p<m\le X,\ p\nmid m}\mu(m).
\]

Any real signed linear combination with weights summing to one has coefficient vector `c_w`. Using the prime-prime boundary matrix and an exact dual certificate gives

\[
\|c_w\|_r
\ge
\frac{N_X}{(N_X+1)^{1/r'}},
\qquad
N_X=\pi(X)-\pi(X/2).
\]

Thus any direct Holder/norm-only certificate in this entire linear boundary-shell class has unavoidable scale at least

\[
\gtrsim \frac{X}{(\log X)^{1/r}},
\]

and cannot reach `X^{1/2+epsilon}`.

---

## 3. Branches closed as primary RH candidates

- mean gap / density alone;
- global Haar/Hardy L^p norms;
- random-sign or generic square-root null evidence;
- complement-midpoint `1/2` arguments;
- raw GCD overlap sectors;
- singleton and fully-visible two-prime raw label correlations;
- connected visibility flux without new residual structure;
- fixed-order and all-order linear divisibility tensors;
- fixed linear floor-dilation / quotient recurrences;
- finite scale-Hankel / curvature observables;
- height localization requiring contour-edge control;
- fixed-degree `omega` moment hierarchies;
- low-order/K-wise prime-label marginals;
- static simplicial topology and natural persistence;
- signed linear prime-boundary averaging followed by L^p/Hölder bounds.

These are not declared mathematically useless; they are removed from the current **independent proof-candidate** list because they are exact reencodings, known barriers, null-reproduced diagnostics, or insufficient information classes.

---

## 4. False-positive guards now mandatory

Any future candidate must be tested against:

1. `1/m` reciprocal hierarchy;
2. reflection-resolution `|delta| log X`;
3. random multiplicative / gap-permutation nulls where appropriate;
4. known-zero spectral reconstruction;
5. Dirichlet-convolution reduction;
6. restricted-Mertens recursion reduction;
7. low-order/K-wise parity invisibility;
8. sieve/parity literature overlap;
9. topological/Betti reencoding;
10. linear boundary-shell norm barrier.

A candidate failing any guard is downgraded before further computation.

---

## 5. Remaining live frontier

The formation-side live frontier is now deliberately narrow:

\[
\boxed{
\text{high-order, nonlinear, prime-weight-sensitive incomplete-boundary geometry}
}
\]

A viable candidate must simultaneously:

1. preserve the exact parity point `z=-1`;
2. depend on actual prime logarithmic weights, not only cardinality `omega`;
3. use information beyond fixed/K-wise marginals;
4. not reduce to ordinary sieve/Buchstab or Dirichlet convolution;
5. not become a finite spectral determinant / known-zero reencoding;
6. not rely only on L^p norm compression;
7. produce a deterministic arithmetic-side sign, monotonicity, contraction, or nonlinear cancellation mechanism.

The natural next primitive is boundary slack

\[
\mathcal S_X(S)
=
\log X-\sum_{p\in S}\log p,
\]

coupled to global parity `(-1)^{|S|}` and high-order prime-label geometry.

---

## 6. Next restart point

When this project resumes, do **not** restart from generic Mertens recurrences, low-order moments, topology, or linear boundary averaging.

Start with:

1. define a nonlinear slack--parity observable on incomplete boundary states;
2. test exact invariance/reduction under prime toggles;
3. search weighted-threshold Boolean Fourier / approximate-degree / knapsack-boundary literature;
4. derive an arithmetic-only identity or inequality before numerical scaling;
5. apply all false-positive guards above;
6. only then run prime-gap/null and cutoff-stability computations.

---

## 7. Evidence labels

- `EXACT`: algebraic/combinatorial identity proved directly.
- `STANDARD`: standard theorem or consequence used with citation.
- `NUMERICAL`: finite computation only.
- `REENCODING`: equivalent/repackaged known difficulty.
- `CLOSED`: closed only as a current independent proof route.
- `OPEN`: unresolved and not claimed.

Final status: **RH remains OPEN. The audit substantially narrows the admissible method class but does not establish RH.**
