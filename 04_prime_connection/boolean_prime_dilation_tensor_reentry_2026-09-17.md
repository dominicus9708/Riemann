# Boolean prime-dilation tensor re-entry — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Two-prime / finite-prime Boolean dilation idea: EXACTLY REDUCED.
- Liouville case: centered prime-divisibility tensors become finite frequency-dilation stencils.
- Möbius case: the same expansion becomes restricted Möbius kernels with coprimality constraints.
- Independent novelty of the finite/all-order linear Boolean-dilation class: CLOSED by re-entry into the earlier CRT tensor / restricted-Möbius barriers.

## 1. Centered divisibility variables
For a prime `p` put

\[
Y_p(n)=p1_{p\mid n}-1.
\]

For a finite prime set `S`, write

\[
Q_T=\prod_{p\in T}p
\]

for each subset `T subset S` (with `Q_empty=1`). Then

\[
\prod_{p\in S}Y_p(n)
=
\sum_{T\subseteq S}
(-1)^{|S|-|T|}Q_T1_{Q_T\mid n}.
\]

## 2. Liouville hypercube dilation stencil
For Liouville,

\[
\sum_{\substack{D<n\le2D\\Q_T\mid n}}
\lambda(n)e(\alpha n)
=
(-1)^{|T|}P_{D/Q_T}^\lambda(Q_T\alpha).
\]

Therefore

\[
\boxed{
\sum_{D<n\le2D}
\lambda(n)
\prod_{p\in S}Y_p(n)e(\alpha n)
=
(-1)^{|S|}
\sum_{T\subseteq S}
Q_T P_{D/Q_T}^\lambda(Q_T\alpha).
}
\]

Classification:

`BOOLEAN_PRIME_DILATION_HYPERCUBE_IDENTITY`.

Thus a centered `|S|`-prime divisibility tensor is exactly a `2^|S|`-vertex frequency/scale dilation stencil.

## 3. Why this is not a new independent mechanism
On a complete CRT period, the variables `Y_p` are centered and mutually independent in the exact residue model, and the products

\[
Y_T=\prod_{p\in T}Y_p
\]

are exactly orthogonal with

\[
\operatorname{Var}(Y_T)=\prod_{p\in T}(p-1).
\]

These are precisely the prime-divisibility tensors already audited in

`all-order prime-divisibility tensor variance barrier`.

The frequency-dilation formula above does not add new information to that tensor: it is the Fourier/dilation representation of the same observable.

Consequently:

- fixed-order Boolean dilation inherits the fixed-order tensor barrier;
- normalized linear combinations over all subset orders inherit the earlier all-order optimum governed by sieve density;
- merely increasing `|S|` does not manufacture polynomial `H^{-1/2}` spectral flattening.

Classification:

`BOOLEAN_DILATION_TENSOR_REENTRY`.

## 4. Möbius version
For squarefree `Q_T`,

\[
\sum_{\substack{D<n\le2D\\Q_T\mid n}}
\mu(n)e(\alpha n)
=
(-1)^{|T|}
\sum_{\substack{D/Q_T<m\le2D/Q_T\\(m,Q_T)=1}}
\mu(m)e(Q_T\alpha m).
\]

Therefore the Boolean stencil is not a free Liouville stencil but a family of scaled **restricted Möbius sums**.

The coprimality restriction is exactly the structure that appeared earlier in connected visibility-boundary / restricted-Mertens recursions. Removing it by inclusion-exclusion returns to finite Euler factors and lower-scale restricted Möbius kernels.

Classification:

`MOBIUS_BOOLEAN_DILATION_RESTRICTED_KERNEL_REENTRY`.

## 5. Consequence for the next search
The candidate

> use two or more prime-dilation identities in a Boolean finite difference to cancel the additive prime-count fluctuation

does not produce an independent mechanism. It is another representation of already-audited prime-label tensors.

To escape the barrier, a new operator must use information not contained in a static divisibility mask. Possibilities still logically open are:

1. **ordered factorization dynamics** (which prime activates first / scale ordering), provided it does not collapse to ordinary Buchstab or Heath–Brown decomposition;
2. a nonlinear coupling of dilation depth with the reciprocal phase before label marginalization;
3. a genuinely global parity observable whose interaction order grows with scale and cannot be written as a normalized linear combination of CRT tensors.

The first of these must be audited immediately against the existing Buchstab/Heath–Brown literature before being treated as a new branch.
