# Reflection–primepower pinch and convex majorization — 2026-09-16

## Status
- RH remains OPEN.
- Reflection–primepower pinch: exact structural comparison + standard explicit-formula asymptotics.
- Convex inverse-quantile representation: exact.
- Universal convex positivity: CLOSED / too strong because theta(x)-x changes sign infinitely often.

## 1. Prime-power truncation hierarchy
For m>=2 define

Theta_{<m}(x) = sum_{k=1}^{m-1} theta(x^{1/k})
              = psi(x) - sum_{k>=m} theta(x^{1/k}).

The omitted prime-power tail has leading term theta(x^{1/m})~x^{1/m}. Hence

Theta_{<m}(x)-x
= (psi(x)-x) - x^{1/m} + lower prime-power layers.

After one integration the deterministic deficit is

- [m/(m+1)] x^{1+1/m}.

A zeta zero rho contributes at exponent x^{rho+1}. Thus the exponent competition is controlled by

Re(rho) - 1/m.

## 2. Reflection–primepower pinch
The zeta functional equation reflects rho to 1-rho, hence the spectral abscissa beta_* = sup Re(rho) satisfies beta_*>=1/2.

The first non-prime layer of the Euler prime-power hierarchy is the square layer m=2, with exponent 1/2.

Therefore m=2 is the unique prime-power truncation for which the deterministic prime-power correction can live at the same exponent as the smallest spectral abscissa permitted by reflection symmetry:

reflection fixed point: beta=1/2
prime-square exponent: 1/2.

For m=2 (Theta_{<2}=theta), the integrated deterministic buffer is -(2/3)x^{3/2}; under RH the zero wave also has x^{3/2} scale and coefficient family 1/[rho(rho+1)]. The known absolute coefficient mass c≈0.0461176 is much smaller than 2/3, explaining the robust sign in Johnston's criterion.

For m>=3, even under RH the zero-wave exponent 3/2 exceeds the buffer exponent 1+1/m, so no fixed-sign argument based only on that lower prime-power buffer can persist asymptotically.

This refines, but does not revoke, RECIPROCAL_HIERARCHY_FALSE_CONTROL: observing 1/2 from m=2 alone is not RH evidence; it becomes structurally distinguished only when coupled simultaneously to reflection symmetry and an actual dominance/sign criterion.

## 3. Finite-scale crossover guard
Let

c = sum_rho 1/|rho(rho+1)| ≈ 0.0461176444

under RH. For m>=3, a conservative scale where the deterministic buffer coefficient m/(m+1) still exceeds the worst absolute critical-line zero sum is given approximately by

x^(1/2-1/m) < [m/(m+1)]/c.

Corresponding rough crossover scales:
- m=3: ~1.85e7
- m=4: ~9.1e4
- m=5: ~1.55e4
- m=6: ~6.4e3

These are false-control scales, not sign-change predictions. Phase cancellation and lower-order terms can postpone actual crossings substantially.

Permanent rule: PRIMEPOWER_CROSSOVER_GUARD. A finite-range fixed sign in an m>=3 truncation must be compared against the deterministic buffer/critical-zero crossover before any spectral claim is made.

## 4. Convex event reserve as inverse-quantile majorization
Let cumulative prime-log mass be theta(x). Define its generalized inverse P_theta(u) by

P_theta(u)=p when theta(p^-)<u<=theta(p).

Then for any differentiable F and prime cutoff x,

sum_{p<=x} (log p) F'(p)
= integral_0^{theta(x)} F'(P_theta(u)) du.

After the harmless endpoint constant from F(0),

R_F(x)
= integral_0^{theta(x)} [F'(P_theta(u))-F'(u)] du.

For F(u)=u^2/2,

R_quad(x)=integral_0^{theta(x)} [P_theta(u)-u] du
= sum_{p<=x} p log p - theta(x)^2/2.

Thus the Johnston-derived event reserve is the signed area between the inverse prime-log quantile and the diagonal.

Equivalently, if U is uniform in prime-log mass u∈[0,theta(x)], then R_quad/theta is the difference between E[P_theta(U)] and E[U]=theta/2.

## 5. Why universal convex positivity is impossible
If the above reserve were nonnegative for every sufficiently rich class of increasing test functions F', this would amount to first-order stochastic dominance of P_theta(U) over U, which for monotone quantiles forces essentially P_theta(u)>=u almost everywhere, corresponding to theta(x)<=x-type pointwise dominance.

But theta(x)-x changes sign infinitely often (Littlewood). Therefore no proof can make all convex event reserves simultaneously positive. A viable RH-equivalent criterion must use a selected broad kernel whose long-range reserve survives local crossings.

## 6. Universal local threshold in the convex family
At a prime p, let ell=log p and t=theta(p^-). Then

Delta_p R_F
= ell F'(p) - [F(t+ell)-F(t)].

If F' is strictly increasing, there is xi_F∈(t,t+ell) with

[F(t+ell)-F(t)]/ell = F'(xi_F),

hence

Delta_p R_F>0 iff p>xi_F.

For smooth regular kernels,

xi_F = t + ell/2 + O(ell^2 F'''(t)/F''(t)).

Thus the local event threshold is universally close to

theta(p)-p = (1/2)log p.

The exact quadratic case has precisely this threshold. Since Littlewood oscillations create arbitrarily long large positive theta-p excursions, changing convex kernel cannot produce a fixed-K local monotonic proof.

## 7. Current interpretation
The 1/2 in the quadratic event completion itself remains generic sawtooth geometry (EVENT_ENERGY_HALF_FALSE_CONTROL). The nontrivial structural point is the simultaneous meeting of:
- reflection symmetry of zeta zeros at 1/2,
- the first omitted Euler prime-power layer at exponent 1/2,
- a sign criterion whose critical-line coefficient mass is strictly below the prime-square buffer.

This is an explanatory synthesis, not a proof of RH.
