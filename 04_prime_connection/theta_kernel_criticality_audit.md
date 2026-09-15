# Theta / Xi kernel criticality audit

Status: literature audit + exact deformation identities; no RH proof.

## 1. Additive lattice route
Poisson summation for the integer lattice yields the Jacobi theta self-reciprocity and, by Mellin transform, the functional equation for the completed zeta function. On the critical line,
\[
\Xi(t)=\xi(1/2+it)
\]
is the Fourier transform of an even, positive, super-exponentially decaying theta kernel \(\Phi\).

Thus RH is equivalent to real-rootedness of this Fourier transform.

## 2. Low-order positivity is not enough
Classical work proves strong convexity/log-concavity properties of \(\Phi\), including that the associated translation kernel is Pólya-frequency of order 2 (PF2).

However a 2026 certified computation of W. Michalowski proves
\[
\boxed{\Phi(|u|)\notin PF_5}
\]
by an explicit 5x5 Toeplitz minor with negative interval enclosure. Hence the most direct route
\[
\text{PF}_2\to\text{PF}_3\to\cdots\to\text{PF}_\infty
\]
cannot establish RH for the actual kernel: total positivity already fails at finite order five. Global PF4 remains open, but even PF4 would not imply total positivity.

Classification: `TOTAL_POSITIVITY_ROUTE_CLOSED`.

## 3. Jensen-polynomial fixed-order false control
Pólya's Jensen criterion makes RH equivalent to hyperbolicity of all relevant Jensen polynomials. But Griffin--Ono--Rolen--Zagier and subsequent effective work show that for every fixed degree d, the Jensen polynomials are hyperbolic for all sufficiently large shifts, unconditionally.

Therefore fixed-degree or any finitely truncated Jensen-hyperbolicity computation cannot be RH evidence by itself.

New guard:
`FIXED_JENSEN_ORDER_FALSE_CONTROL` — require degree/scale growth or a genuinely all-order argument.

## 4. de Bruijn--Newman criticality guard
Let
\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du.
\]
There is a constant \(\Lambda\) such that all zeros of \(H_t\) are real iff \(t\ge\Lambda\). RH is equivalent to \(\Lambda\le0\). Rodgers--Tao proved
\[
\boxed{\Lambda\ge0}.
\]
Consequently, for every \(t<0\), \(H_t\) has at least one nonreal zero.

This gives a methodological obstruction. Suppose a kernel property P:
1. is sufficient for all Fourier zeros to be real;
2. holds for \(\Phi\) at t=0 with a uniform strict margin;
3. is open/continuous under the deformation \(e^{tu^2}\Phi(u)\).

Then P would persist for some t<0 and falsely imply real-rootedness there. Therefore no such robust open property can prove RH at t=0.

New guard:
\[
\boxed{\texttt{NEGATIVE_HEAT_ROBUSTNESS_GUARD}}
\]
A successful kernel criterion must be critical/non-open at t=0 or otherwise fail arbitrarily close on the negative-heat side.

## 5. Negative heat as multiplicativity defect
Dobner's proof of Newman's conjecture approximates negative-time deformations using
\[
\zeta_t(s)=\sum_{n\ge1}a_t(n)n^{-s},\qquad
a_t(n)=\exp\left(\frac t4(\log n)^2\right),\quad t<0.
\]
The coefficients satisfy the exact defect law
\[
\boxed{
\log\frac{a_t(mn)}{a_t(m)a_t(n)}
=\frac t2\log m\log n.
}
\]
Thus exact multiplicativity is restored precisely at t=0. In prime-channel language, nonzero heat introduces an all-to-all bilinear coupling between logarithmic factor coordinates.

This provides a useful synthesis:
- Poisson/theta self-duality encodes the additive integer lattice;
- t=0 restores exact multiplicativity of the Dirichlet coefficients;
- de Bruijn--Newman criticality asks whether this exact intersection already forces all Xi zeros real.

But multiplicativity at t=0 is not by itself a proof: positive t also breaks coefficient multiplicativity while sufficiently heated transforms have only real zeros.

## 6. Project verdict
The theta route gives a genuine joint additive/multiplicative critical point, but the obvious local positivity mechanisms are unavailable:
- PF-infinity is false;
- fixed Jensen degree is asymptotically hyperbolic without RH;
- any robust open sufficient condition is ruled out by Lambda >= 0.

A surviving route must identify a non-open all-order invariant that is exactly saturated at t=0 and is not merely another formulation of de Bruijn--Newman Lambda=0.
