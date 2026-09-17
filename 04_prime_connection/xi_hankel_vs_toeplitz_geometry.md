# Xi Hankel-vs-Toeplitz positivity geometry

Status: `EXACT STRUCTURAL BARRIER`.

## 1. Positive Xi kernel gives an unconditional Stieltjes moment sequence
The Riemann Xi Fourier kernel \(\Phi(u)\) is positive and rapidly decaying. Its raw even moments

\[
b_n:=\int_0^\infty u^{2n}\Phi(u)\,du
\]

can be written, after \(t=u^2\), as

\[
b_n=\int_0^\infty t^n\,d\mu(t)
\]

for a positive measure \(d\mu\) on \([0,\infty)\).

Hence \((b_n)\) is a Stieltjes moment sequence.

By the classical Stieltjes/Gantmacher–Krein characterization, the infinite Hankel matrix

\[
H(b)=(b_{i+j})_{i,j\ge0}
\]

is totally positive. Equivalently, all Hankel minors (and the shifted moment conditions) have the required nonnegative signs.

At the quadratic-form level,

\[
\sum_{i,j=0}^r c_ic_jb_{i+j}
=
\int_0^\infty\left(\sum_{i=0}^r c_it^i\right)^2d\mu(t)\ge0.
\]

Thus even all-order Hankel positivity of the raw Xi moments is unconditional and cannot by itself encode RH.

## 2. Jensen hyperbolicity is a different total-positivity geometry
For a finite polynomial with nonnegative coefficients,

\[
P(X)=\sum_{j=0}^d a_jX^j,
\]

real nonpositive zeros are equivalent (Aissen–Schoenberg–Whitney / Pólya-frequency theory) to total positivity of the associated Toeplitz coefficient matrix, i.e. the finite coefficient sequence is PF-infinity.

The Jensen polynomials use a factorial-normalized Taylor sequence and binomial weighting. Therefore the RH-relevant real-rootedness problem is not the raw-moment Hankel total positivity above; it belongs to the Jensen/PF/Toeplitz geometry.

Schematic distinction:

\[
\boxed{
\text{positive Xi kernel}
\Longrightarrow
\text{raw-moment Hankel-TP (unconditional)}
}
\]

whereas

\[
\boxed{
\text{Jensen hyperbolicity for the full family}
\Longleftrightarrow
\text{RH-relevant Laguerre–Pólya/PF structure}.
}
\]

## 3. False-control rule
`HANKEL_GEOMETRY_FALSE_CONTROL`:

Do not treat positivity of Gram matrices, moment Hankel determinants, shifted Hankel determinants, or even all-order Hankel total positivity of the raw Xi kernel moments as RH evidence. Those are consequences of the positive moment representation.

Every determinant-based Xi proposal must specify whether the matrix geometry is:

1. Hankel/moment geometry -- largely automatic from kernel positivity; or
2. Toeplitz/Jensen/Pólya-frequency geometry -- tied to real-rootedness.

The word `total positivity` alone is therefore insufficient.

## 4. Relation to fixed-order Jensen barrier
This barrier is complementary to `FIXED_JENSEN_DEGREE_FALSE_CONTROL`:

- fixed Jensen degree can become hyperbolic unconditionally at large shift;
- raw-moment Hankel positivity is stronger in order (all orders) but lives in the wrong matrix geometry.

Therefore neither `higher order` nor `all determinants positive` is meaningful without tracking the exact transformation that carries Stieltjes/Hankel structure into Jensen/Toeplitz real-rootedness.

## 5. Live question
The possible nontrivial bridge is now sharply stated:

\[
\boxed{
\text{Can the special theta/Poisson structure of }\Phi
\text{ promote unconditional Hankel-TP into the required Jensen/PF-TP?}
}
\]

Generic positive measures do not provide such a promotion, so any successful bridge must use additional modular/self-dual structure specific to the Riemann kernel.

Literature anchors: classical Stieltjes moment problem; Schoenberg total positivity; Aissen–Schoenberg–Whitney real-rootedness/PF theorem; Pólya–Jensen criterion for Xi.
