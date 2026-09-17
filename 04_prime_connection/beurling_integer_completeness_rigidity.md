# Beurling integer-completeness rigidity audit

Status: `EXACT + BARRIER / OPEN-RIGIDITY CONNECTION`

## 1. Critical relocation setup
Let the ordinary primes be indexed as `p` and let a generalized-prime perturbation be

\[
q_p=p+\delta_p,
\]

with a pairing chosen so that

\[
\sum_p |\log(q_p/p)|p^{-\sigma}<\infty
\]

for every \(\sigma>1/2\). Then

\[
\zeta_{\mathcal Q}(s)=\zeta(s)e^{H(s)},
\qquad \Re s>1/2,
\]

where

\[
H(s)=\sum_p\sum_{k\ge1}\frac{q_p^{-ks}-p^{-ks}}{k}.
\]

Hence \(e^{H(s)}\) is analytic and nonzero in \(\Re s>1/2\); the zero/pole divisor in that half-plane is unchanged.

## 2. Generalized-integer density
At \(s=1\),

\[
\rho_{\mathcal Q}
:=\operatorname*{Res}_{s=1}\zeta_{\mathcal Q}(s)
=e^{H(1)}
=\prod_p\frac{1-p^{-1}}{1-q_p^{-1}}.
\]

Under the standard positive-coefficient Tauberian hypotheses this is the asymptotic generalized-integer density:

\[
N_{\mathcal Q}(x)\sim \rho_{\mathcal Q}x.
\]

Therefore a one-sided coherent relocation already destroys integer-completeness at the linear-density level. In particular, if \(q_p>p\) for all p and at least one inequality is strict then \(\rho_{\mathcal Q}<1\); if \(q_p<p\) for all p then \(\rho_{\mathcal Q}>1\).

For \(q_p=p+\alpha\sqrt p\) with small fixed \(\alpha\),

\[
\log\rho_{\mathcal Q}
=-\alpha\sum_p\frac{\sqrt p}{p(p-1)}+O(\alpha^2),
\]

so the density defect is already first-order in the coherent displacement.

## 3. Density one is only the first Mellin constraint
Define for real \(\sigma>1\)

\[
C_\sigma(\mathcal Q)
:=\log\frac{\zeta_{\mathcal Q}(\sigma)}{\zeta(\sigma)}
=\sum_p\log\frac{1-p^{-\sigma}}{1-q_p^{-\sigma}}.
\]

Then \(C_1=0\) (in the residue/limit sense) is merely the density-one condition.

Exact integer-completeness is much stronger. If the generalized-integer counting measure equals the ordinary integer counting measure, then

\[
\zeta_{\mathcal Q}(s)=\zeta(s)\qquad(\Re s>1),
\]

hence

\[
C_\sigma(\mathcal Q)=0\qquad\text{for every }\sigma>1.
\]

Conversely, equality of these Dirichlet/Laplace transforms on an interval \(\sigma>1\) determines the counting measure, so the full continuum of Mellin constraints recovers exact integer-completeness.

Thus:

\[
\boxed{
N_{\mathcal Q}(x)\equiv\lfloor x\rfloor
\iff
C_\sigma(\mathcal Q)=0\ \forall\sigma>1.
}
\]

After exact counting-measure recovery, unique factorization forces the generalized primes to be the ordinary primes.

## 4. Finite Mellin data are insufficient
Any finite list \(C_{\sigma_1},\dots,C_{\sigma_k}\) gives only finitely many smooth scalar constraints on infinitely many prime positions. For a generic choice of sufficiently separated large primes, the Jacobian of these constraints with respect to finitely many prime displacements has full rank (asymptotically it is a generalized exponential/Vandermonde matrix). The implicit-function theorem therefore leaves nontrivial local perturbation manifolds preserving those finitely many Mellin constraints.

Consequently a finite collection of density/Mellin checks cannot by itself force ordinary-prime placement or the Chebyshev event-energy sign. The full support constraint, or an infinite hierarchy strong enough to recover it, is required.

Classification:

`FINITE_COMPLETENESS_MOMENTS -> INSUFFICIENT`

## 5. Connection to an independent Beurling rigidity problem
A much stronger quantitative statement would say that a nonclassical generalized-prime system cannot satisfy

\[
N_{\mathcal Q}(x)-\lfloor x\rfloor=o(\log x).
\]

This is essentially a classical Beurling rigidity conjecture / open problem. Therefore the route

`critical relocation -> near-integer completeness rigidity -> RH event-energy sign`

cannot currently be treated as a routine lemma; the intermediate rigidity problem is itself nontrivial and open in general.

## 6. Consequence for the RH audit
The earlier observation that \(O(\sqrt p)\) prime relocation can preserve the zero divisor in \(\Re s>1/2\) while changing the Chebyshev event-energy by \(\asymp x^{3/2}\) remains important, but the missing bridge is now precise:

\[
\boxed{
\text{zero-divisor stability}
\not\Rightarrow
\text{integer-completeness}
\not\Rightarrow_{\text{known quantitatively}}
\text{event-energy sign}.
}
\]

The next viable route should therefore use an exact arithmetic identity that exploits ordinary integer structure directly, rather than assuming a near-completeness rigidity estimate that would amount to a separate Beurling problem.
