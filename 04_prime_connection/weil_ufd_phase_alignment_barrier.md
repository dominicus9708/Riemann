# Weil prime-comb UFD phase-alignment barrier

Status: exact torus-average structure + pointwise barrier + open finite-time recurrence problem.

## 1. Prime comb in a compact Weil window
For supp f subset [-L,L], the autocorrelation g=f*tilde(f) has support [-2L,2L]. The arithmetic Weil symbol contains the finite prime-power trigonometric comb
\[
P_L(t)=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n).
\]
Set
\[
A_L=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}.
\]
By the PNT and partial summation,
\[
\boxed{A_L\sim4e^L.}
\]

## 2. UFD forces exact pointwise alignment in the supremum
For distinct ordinary primes, the numbers log p are linearly independent over Q: a rational relation can be cleared to an integer relation and exponentiated, contradicting unique factorization.

Kronecker's simultaneous approximation theorem therefore implies that for every epsilon>0 there are arbitrarily large t for which
\[
t\log p\equiv0\pmod{2\pi}
\]
within epsilon for every prime p occurring in the finite comb. All harmonics k log p then align as well.

Hence
\[
\boxed{\sup_{t\in\mathbb R}P_L(t)=A_L,}
\]
and the supremum is approached at arbitrarily large t.

Thus exact unique factorization forbids any uniform pointwise cancellation estimate better than the trivial total mass.

Classification: `UFD_PHASE_ALIGNMENT_BARRIER`.

## 3. Doubly exponential pointwise-envelope scale
The archimedean part of the Weil symbol grows only logarithmically in |t|. A pointwise proof that waits until this term exceeds the worst possible prime comb must therefore reach
\[
\log |t|\gtrsim A_L\sim4e^L,
\]
so
\[
\boxed{|t|\gtrsim\exp(4e^L).}
\]
This reproduces the doubly-exponential scale appearing in recent compact-window certificate work. It is a limitation of uniform pointwise-envelope methods, not a statement that near-perfect phase alignment actually occurs before that height.

## 4. Infinite-time Haar statistics are completely different
Group the prime-power terms by prime:
\[
Y_p(\theta)=2\log p\sum_{k:p^k<e^{2L}}p^{-k/2}\cos(k\theta).
\]
By Kronecker-Weyl equidistribution, long-time averages of any continuous function of the finite phase vector equal Haar averages on the product torus. The variables Y_p are therefore independent under the Haar model.

Each has mean zero and, by trigonometric orthogonality,
\[
\mathbb E Y_p^2
=2(\log p)^2\sum_{k:p^k<e^{2L}}p^{-k}.
\]
Hence
\[
\boxed{
\operatorname{Var}_{\rm Haar}P_L
=2\sum_p(\log p)^2\sum_{k:p^k<e^{2L}}p^{-k}
\sim4L^2.
}
\]
Thus the typical Haar size is O(L), while the supremum is asymptotic to 4e^L.

The ratio between worst alignment and typical fluctuation is exponentially large in L.

## 5. Sub-Gaussian Haar tails
The prime-only part
\[
P_L^{(1)}(t)=\sum_{p<e^{2L}}a_p\cos(t\log p),
\qquad a_p=2\log p/\sqrt p,
\]
has Haar moment-generating function
\[
\prod_p I_0(\lambda a_p).
\]
Using I_0(z)<=exp(z^2/4) gives
\[
\mathbb P_{\rm Haar}(P_L^{(1)}\ge u)
\le
\exp\left(-\frac{u^2}{\sum_pa_p^2}\right),
\]
with
\[
\sum_pa_p^2\sim8L^2.
\]
The full prime-power comb also has sub-Gaussian concentration by applying Hoeffding's lemma prime-by-prime to the bounded Y_p.

Therefore near-maximal alignment has extremely small asymptotic density even though it occurs infinitely often.

## 6. The finite-time recurrence bottleneck
Weil positivity at fixed L cannot be proved from infinite-time density alone. A Paley-Wiener test F=hat(f) may be modulated to concentrate near an arbitrary target height t0 without changing the support of f. Consequently even a very rare bad phase recurrence can matter.

The live deterministic question is:
\[
\boxed{
\text{how early can a sufficiently strong simultaneous alignment of }(t\log p)_p\text{ occur?}
}
\]
One needs a finite-time quantitative recurrence bound, not merely Kronecker-Weyl equidistribution.

High-moment methods expose the difficulty. A 2k-th moment of a Dirichlet polynomial of length X=e^{2L} is cleanly diagonal only while roughly X^k is below the averaging height T. To convert average tails into a supremum bound over [0,T] one would like k comparable to log T, but diagonal control permits only k about log T/log X. The remaining factor T^{1/(2k)} is then of order sqrt(X)=e^L, losing the desired gain. This is another form of the high-dimensional recurrence bottleneck.

## 7. Relation to current compact-window work
A September 2026 preprint of Marcus Chuk proves finite-window Weil positivity at certain fixed L and identifies the exact supremum A_L of the prime comb, leading to the same doubly-exponential pointwise-envelope barrier. That work is recent and is treated here as literature alignment rather than a settled foundational theorem.

## 8. Project consequence
The exact ordinary-prime logarithms supply both:
- strong average phase decorrelation through torus equidistribution;
- arbitrarily accurate pointwise alignment through the same rational independence.

Thus UFD alone does not have a one-sided positivity effect. Any successful Weil-window route must combine finite-time Diophantine recurrence control with Paley-Wiener time-frequency concentration, rather than relying on either random-phase heuristics or pointwise prime-comb bounds alone.
