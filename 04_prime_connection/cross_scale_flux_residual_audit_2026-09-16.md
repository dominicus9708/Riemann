# Cross-scale flux versus hard residual audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Simple pointwise linear coupling between prime-square oriented flux and hard event residual: NUMERICALLY UNSUPPORTED.
- Fixed-length square-window domination: CLOSED as a universal strategy by the previously proved positive-run locality barrier.
- Scale-growing/adaptive nonlocal coupling: OPEN.

## 1. Leading square reserve and residual

Let

\[
A_m^{(2)}
=L_m\frac{\vartheta(m)+\vartheta(m+1)}2
\]

be the prime-square layer of the explicit prime-power reserve, and define

\[
F_m:=\Delta_mH+A_m^{(2)}.
\]

Thus F_m is what remains in one shell after the leading square reserve is added back.
The prime-square oriented flux is

\[
W_m^{(2)}
=\vartheta(m)L_m-\vartheta(m^2)\,[\vartheta(m+1)-\vartheta(m)].
\]

Both are naturally on the m^2 shell scale.

## 2. Finite local-correlation audit

Using exact primes through x<=5,000,000 and shells m=2,...,2235:

- F_m/m^2 > 0 in about 21.7% of shells;
- among root-prime activation steps (m+1 prime), the positive fraction is about 21.2%;
- among composite steps, the positive fraction is about 21.8%.

For m>=100, the Pearson correlation between

\[
F_m/m^2
\quad\text{and}\quad
W_m^{(2)}/m^2
\]

is approximately

\[
-0.0062.
\]

Thus the local sign/magnitude of the prime-square oriented flux does not visibly predict the sign/magnitude of the hard residual at this range.

Classification:

`CROSS_SCALE_LOCAL_LINEAR_NULL` — do not use a shellwise linear correlation between F_m and W_m^(2) as the next proof mechanism without genuinely new evidence.

This is a numerical negative result, not an impossibility theorem for nonlinear or long-range relations.

## 3. Why fixed-length window domination is a false control

In the same finite range, long moving sums of F_m become strongly negative; for example all tested overlapping windows of length 256 beyond the small initial range were negative.

This finite behavior cannot be promoted to an asymptotic rule.

From the previously established Littlewood positive-excursion argument, there are arbitrarily long runs of consecutive prime events with

\[
\Delta_pH>0.
\]

Those runs span an unbounded number of square shells. A shell lying wholly inside such a run has nonnegative event-energy increment, and any nonempty such shell has positive increment. Since

\[
A_m^{(2)}\ge0,
\]

its F_m is also nonnegative, and positive on nonempty event shells.

Therefore for every fixed integer K there are arbitrarily large locations where a K-shell window cannot be forced negative by a universal fixed-window theorem of this form.

Guard:

`FIXED_WINDOW_SQUARE_RESERVE_FALSE_CONTROL`.

The observed finite negativity of long fixed windows is another finite-range stability phenomenon, not an asymptotic mechanism.

## 4. Project consequence

The simplest cross-scale continuation has now been pruned twice:

1. pointwise/local linear correlation with W_m^(2) has no numerical support;
2. fixed-length moving-window domination is incompatible with the known unbounded positive event runs.

A surviving cross-scale inequality must therefore be both:
- genuinely nonlinear or structurally conditional; and
- scale-growing/adaptive rather than fixed-locality.

The next useful target is a stopping-time or cumulative-reserve formulation in which the recovery horizon grows with the size of the Chebyshev excursion, while remaining arithmetic and not merely restating H<0.
