# Selberg symmetry RH-scale barrier audit — 2026-09-16

## Status
- Selberg symmetry formula: classical theorem.
- Its use for the elementary PNT: classical.
- Direct Johnston/event-energy control from the standard formula: CLOSED_BY_SCALE_MISMATCH.
- Higher generalized von Mangoldt derivative-order escalation: FALSE CONTROL / margin-delay reencoding.

## 1. Classical symmetry formula
Define

Lambda_2(n)=mu*log^2(n)
           = Lambda(n) log n + sum_{d|n} Lambda(d)Lambda(n/d).

Then

sum_{n<=x} Lambda_2(n)=2x log x+O(x).

Equivalently,

sum_{n<=x} Lambda(n)log n
+ sum_{ab<=x}Lambda(a)Lambda(b)
=2x log x+O(x).

The Dirichlet series is

sum Lambda_2(n)n^{-s}=zeta''(s)/zeta(s).

At s=1 this has a double pole, while at a generic simple nontrivial zero rho it has only a simple pole. This explains why the main term is robust enough for the elementary PNT / P2 almost-prime theorem but does not itself locate zero real parts at 1/2.

## 2. Direct comparison with the event-energy target
Set X=y^2. By nonnegativity,

sum_{ab<=y^2} Lambda(a)Lambda(b)

contains the prime-prime submass with a,b<=y, namely theta(y)^2. However the Selberg main scale is

2X log X ~ 4 y^2 log y,

whereas the Johnston-derived event reserve distinguishes

sum_{p<=y} p log p - theta(y)^2/2

at natural deterministic scale y^{3/2}.

Thus the raw Selberg bound is much too coarse for the event-reserve sign. Weighted partial summation of the O(X) remainder produces O(y^2)-scale uncertainty, still larger than y^{3/2}.

Conclusion:
standard Selberg symmetry + positivity does not reach the RH-scale one-sided event reserve.

## 3. Relation to elementary PNT recurrence
The classical Erdős–Selberg proof converts the symmetry formula to recursive/averaged bounds for R(x)=psi(x)-x (or x-psi(x)), sufficient to obtain R=o(x). The standard mechanism is tailored to exclude zeros on Re(s)=1 / prove PNT. It supplies no polynomial x^{1/2+epsilon} error scale without additional RH-strength input.

## 4. Higher derivative-order false control
For k>=1 define generalized von Mangoldt

Lambda_k=mu*log^k.

Then

sum Lambda_k(n)n^{-s}=(-1)^k zeta^{(k)}(s)/zeta(s).

At s=1 the pole order becomes k, giving a large deterministic summatory main term approximately

k x (log x)^{k-1}.

But a generic simple zero rho remains a simple-pole obstruction. Therefore increasing k amplifies the finite-scale main term without improving the spectral-abscissa information.

Audit rule: SELBERG_DERIVATIVE_ORDER_FALSE_CONTROL.
A higher-k identity that appears more stable numerically must be tested for the same margin/detection-delay tradeoff as smoothing and convex-kernel escalation.

## 5. Current consequence
Selberg's quadratic divisor incidence is the correct kind of ordinary-integer arithmetic information, but the standard symmetry formula is quantitatively only PNT-scale for the present purpose. A viable continuation must introduce a nonlocal identity whose intrinsic remainder is already at or below x^{3/2} after mapping to the Johnston variable, rather than obtain that scale by integrating an O(x) Selberg remainder.
