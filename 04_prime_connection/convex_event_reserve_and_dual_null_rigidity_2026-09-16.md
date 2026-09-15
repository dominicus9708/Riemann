# Convex event-reserve and dual-null rigidity audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Convex/Bregman master identity: EXACT.
- Johnston quadratic energy: exact derived RH-equivalent criterion (using Johnston's theorem plus explicit RH bounds).
- Landau primorial-budget slice: known structure in Deléglise–Nicolas; not novel.
- Regularly varying kernel expansion: DERIVED ASYMPTOTIC / requires standard explicit-formula hypotheses.
- Dual-null rigidity via Hamburger: EXACT within the standard Dirichlet-series finite-order class; do not extend automatically to arbitrary Beurling generalized Dirichlet series.

## 1. Convex event-reserve master identity
Let F be C^2 on [2,∞), and define

R_F(x) = sum_{p<=x} (log p) F'(p) - F(theta(x)).

Stieltjes integration by parts gives

R_F(x) - C_F
= - int_2^x (theta(t)-t) F''(t) dt
  - D_F(theta(x),x),

where

C_F = 2 F'(2) - F(2),

D_F(y,x) = F(y)-F(x)-F'(x)(y-x).

If F is convex, D_F>=0. Thus every such event reserve is a weighted Chebyshev bias minus a nonnegative endpoint Bregman penalty.

### Quadratic member
F(u)=u^2/2 gives

R_F(x)=sum_{p<=x} p log p - theta(x)^2/2.

Equivalently, the event energy

H(x)=theta(x)^2/2 - sum_{p<=x} p log p + 2

is the negative centered reserve. Between primes H is constant; at p,

Delta_p H = (log p)(theta(p)-p-(log p)/2).

Together with Johnston's criterion this yields the derived equivalence

RH iff H(x)<0 for all x>=3.

### Landau / h(n) member
F(u)=Li(u^2), so F'(u)=u/log u and

R_F(x)=sum_{p<=x} p - Li(theta(x)^2).

If pi_1(x)=sum_{p<=x}p, this is pi_1(x)-Li(theta(x)^2).
Deléglise–Nicolas explicitly use sigma_k=pi_1(p_k), log h(sigma_k)=theta(p_k), and prove under RH quantitative bounds with leading constants 2/3 ± c, where c=sum_rho 1/|rho(rho+1)|≈0.0461176.
Therefore the core Landau reserve is pre-existing; the contribution here is its exact placement in the same Bregman family as the Johnston energy.

## 2. Primorial-budget optimum
For prime x>=5, set A(x)=sum_{p<=x}p. Since log t/t decreases for t>e and every prime q>x has lower value/cost ratio log q/q than every included prime p<=x (including p=2 once x>=5), the 0-1 knapsack defining h(A(x)) is optimized by the full initial prime segment:

h(A(x)) = product_{p<=x} p,
log h(A(x)) = theta(x).

Hence the full Deléglise–Nicolas RH criterion implies on these champion budgets

A(x) > Li(theta(x)^2).

Do not claim the slice alone is RH-equivalent without a separate proof; intermediate budgets have non-initial-segment optimizers.

## 3. Regularly varying convex kernels
Suppose w(x)=F''(x) is positive and regularly varying,

w(x) ~ x^{-a} L(x),   a<3/2,

with sufficient smoothness for standard explicit-formula / Karamata manipulations. The leading theta error has prime-square bias -sqrt(x) plus the zeta zero wave. Under RH, after normalization,

R~_F(x)/(x^{3/2-a} L(x))
= 1/(3/2-a)
  + sum_rho x^{i gamma}/[rho(rho+1-a)]
  + o(1),

while the Bregman endpoint penalty is smaller by a factor x^{-1/2} up to logarithms.

For slowly varying w (a=0),

R~_F(x)/(x^{3/2}w(x))
= 2/3 + sum_rho x^{i gamma}/[rho(rho+1)] + o(1).

This explains structurally why the Johnston kernel w=1 and Landau kernel w~1/log x exhibit the same 2/3 deterministic buffer and the same zero coefficient family.

## 4. Kernel margin / detection delay duality
For power-index a,

B_a = 1/(3/2-a)

is the deterministic prime-square buffer coefficient. Sending a toward 3/2 from below increases the finite-range safety margin. But an off-critical zero beta>1/2 still gains relative factor x^{beta-1/2}; only the crossover constant is delayed. Therefore stronger smoothing or larger deterministic buffer cannot eliminate the RH obstruction; it can hide it longer.

Permanent audit rule:

KERNEL_MARGIN_DELAY_DUALITY:
Any kernel optimization claim must report both the critical-line safety margin and the resulting delay in sensitivity to beta>1/2 modes.

This refines SMOOTHING_DELAY_GUARD.

## 5. Critical Beurling false controls and integer rigidity
Perturb generalized primes q_p=p+O(sqrt(p)). Under the summable logarithmic-displacement condition, zeta_Q/zeta is analytic and nonzero in Re(s)>1/2, so the right-half zero divisor is preserved. Event energy, however, can shift at the same x^{3/2} scale as the prime-square buffer.

Even normalizing the generalized integer density to 1 (by adjusting finitely many small generalized primes so Res_{s=1} zeta_Q=1) does not restore event-energy sign. Thus:

same right-half zero divisor + generalized-integer density 1
is insufficient to force the ordinary-prime event-energy inequality.

Exact integer completeness N_Q(x)=floor(x) is much stronger: then the generalized Dirichlet series equals zeta(s) in Re(s)>1, and Euler-product uniqueness forces the ordinary prime multiset.

## 6. Dual-null rigidity: scope and theorem
Arithmetic/Beurling nulls preserve substantial multiplicative/Euler information and can preserve the Re(s)>1/2 zero divisor, but they generally lose the Riemann functional equation / additive-lattice self-duality.

Hamburger's converse theorem states, in the standard ordinary Dirichlet-series setting: if f and g are Dirichlet series absolutely convergent for sigma>1, (s-1)f(s) and (s-1)g(s) are entire of finite order, and they satisfy the Riemann functional equation with the standard Gamma factor, then

f(s)=g(s)=c zeta(s).

Therefore, within this standard class, an exact null preserving the full Riemann functional equation collapses to zeta up to scale. This must NOT be overextended to arbitrary generalized Dirichlet series / Beurling systems, whose exponents need not be the ordinary integers.

Methodological principle:

DUAL_NULL_RIGIDITY:
- multiplicative/Euler-preserving perturbations are useful arithmetic false controls but normally break additive/self-dual functional-equation structure;
- symmetry/functional-equation-preserving deformations can serve spectral false controls but typically lose Euler-product arithmetic;
- demanding both in the standard Dirichlet-series finite-order class leaves essentially no nontrivial null by Hamburger rigidity.

This is a limitation of null-model methodology, not a proof of RH.

## 7. Current live question
The surviving target is not another equivalent weighted integral. It is a deterministic mechanism that uses BOTH:
1. exact multiplicative prime/divisor structure, and
2. additive-lattice/self-dual structure behind the Riemann functional equation,

to force a sign/reserve inequality such as the quadratic event reserve without re-importing zero locations.

Any candidate must survive:
- RECIPROCAL_HIERARCHY_FALSE_CONTROL,
- REFLECTION_RESOLUTION_GUARD,
- SMOOTHING_DELAY_GUARD,
- KERNEL_MARGIN_DELAY_DUALITY,
- Beurling critical-relocation controls,
- known spectral/Weil re-encodings.
