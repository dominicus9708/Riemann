# Critical prime transport and the boundary singularity law

Status: exact perturbative derivation / false-control framework.

## 1. Perturbation model
Let the ordinary prime \(p\) be moved to a generalized prime
\[
q_p=p+c p^\theta,
\qquad 0<\theta<1,
\]
for all sufficiently large primes, with finitely many control primes left available for normalization.

Set
\[
H(s)=\log\frac{\zeta_{\mathcal Q}(s)}{\zeta(s)}
=\sum_p\sum_{k\ge1}\frac{q_p^{-ks}-p^{-ks}}{k}.
\]
For every \(\sigma>\theta\), the perturbation series converges locally uniformly, so \(H\) is analytic there and \(e^{H(s)}\) is nonzero. Hence \(\zeta_{\mathcal Q}\) and \(\zeta\) have the same zero/pole divisor in \(\Re s>\theta\).

## 2. Boundary singularity law
The \(k=1\) term gives
\[
q_p^{-s}-p^{-s}
=-cs\,p^{-(s+1-\theta)}+O\bigl(p^{-(s+2-2\theta)}\bigr).
\]
Therefore near \(s=\theta\),
\[
H(s)=-cs\,P(s+1-\theta)+O(1),
\]
where \(P\) is the prime zeta function. Since
\[
P(1+u)=\log(1/u)+O(1),
\]
we obtain
\[
\boxed{H(s)=c\theta\log(s-\theta)+O(1)}.
\]
Thus
\[
\boxed{\frac{\zeta_{\mathcal Q}(s)}{\zeta(s)}\asymp (s-\theta)^{c\theta}}
\]
at the transport boundary.

Interpretation: a coherent \(p^\theta\) displacement preserves all zero information strictly to the right of \(\theta\), but inserts new analytic structure exactly on the boundary \(\Re s=\theta\).

## 3. Critical case theta=1/2
For
\[
q_p=p+c\sqrt p,
\]
all zero/pole data in the open half-plane \(\Re s>1/2\) are preserved, while the zeta ratio acquires a boundary singularity at \(1/2\).

This explains why square-root-scale transport is the critical Beurling null for RH-side information.

## 4. Density normalization does not remove the false control
At \(s=1\),
\[
H(1)=\sum_p\log\frac{1-p^{-1}}{1-q_p^{-1}}
\]
converges. If the transport begins only above a sufficiently large cutoff \(P\), its tail contribution to \(H(1)\) is arbitrarily small. A finite control prime can then be moved slightly in the opposite direction so that
\[
H(1)=0,
\]
thereby preserving the residue at \(s=1\), hence the leading generalized-integer density.

Using two distinct control primes one can simultaneously impose
\[
H(1)=H'(1)=0.
\]
At the unperturbed point, the Jacobian columns associated with a control prime \(r\) are
\[
A(r)=-\frac1{r(r-1)},
\]
\[
B(r)=-\frac1{r(r-1)}+\frac{\log r}{(r-1)^2}.
\]
Moreover
\[
\frac{B(r)}{A(r)}=1-\frac{r\log r}{r-1},
\]
and \(r\log r/(r-1)\) is strictly increasing for \(r>1\). Hence two distinct control primes give a nonzero Jacobian determinant, and the implicit-function theorem supplies the required local correction for sufficiently small tail data.

Therefore zero divisor, residue, and first Laurent jet can all be matched while the critical tail transport remains.

## 5. Chebyshev event-energy transport
For the event energy
\[
\mathcal H(x)=\frac12\vartheta(x)^2-\sum_{p\le x}p\log p+2,
\]
rank-matched transport gives
\[
\boxed{
\mathcal H_{\mathcal Q}(q_x)-\mathcal H_{\mathcal P}(x)
=-\frac{c}{1+\theta}x^{1+\theta}
+O\!\left(\frac{x^{1+\theta}}{\log x}\right).
}
\]
In particular, at \(\theta=1/2\),
\[
\boxed{
\Delta\mathcal H
=-\frac{2c}{3}x^{3/2}
+O\!\left(\frac{x^{3/2}}{\log x}\right).
}
\]
The finite control-prime corrections contribute only lower-order bounded terms.

## 6. Critical robustness trichotomy
The prime-square term behind the Johnston integral criterion has scale \(x^{3/2}\).

- \(\theta<1/2\): transport changes event energy by \(o(x^{3/2})\); the square-layer buffer dominates.
- \(\theta=1/2\): transport changes event energy on exactly the same \(x^{3/2}\) scale while preserving the whole open RH half-plane divisor.
- \(\theta>1/2\): transport can dominate the square-layer buffer, but no longer preserves all zero information in \(\Re s>1/2\).

This is a `CRITICAL_TRANSPORT_FALSE_CONTROL`: Johnston/event-energy sign is not an invariant of the RH zero divisor plus finitely many Laurent data. It depends on the exact ordinary-prime placement / integer lattice.

## 7. Relation to Beurling regularity
Hilberdink's universal bound \(\max\{\alpha,\beta\}\ge1/2\) places the same exponent at the prime/integer regularity boundary. The perturbation singularity law gives a concrete mechanism: coherent \(p^\theta\) transport creates new boundary structure exactly at \(s=\theta\).

This does not prove RH. It clarifies why exact integer-completeness is stronger than all finite coarse matching conditions and why the square-root scale is the natural critical transport scale.
