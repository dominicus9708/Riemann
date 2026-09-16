# Prime-power oriented-area reserve decomposition — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Discrete product/oriented-area identity: EXACT.
- Cumulative prime-power reserve asymptotic: UNCONDITIONAL from the prime number theorem.
- Cumulative oriented-area asymptotic: UNCONDITIONAL consequence of the exact identity + PNT.
- Pointwise sign of the oriented-area increment: FALSE as a universal monotonicity claim.

## 1. Square-endpoint state variables

Define

\[
\Theta_m:=\vartheta(m^2),
\qquad
P_m:=\psi(m^2)-\vartheta(m^2).
\]

The exact prime-power identity gives

\[
P_m=\vartheta(m)+\sum_{k\ge3}\vartheta(m^{2/k}).
\]

Hence, by the ordinary prime number theorem,

\[
\boxed{\Theta_m\sim m^2,\qquad P_m\sim m.}
\]

Let

\[
L_m:=\Theta_{m+1}-\Theta_m
\]

be the logarithmic prime mass in the square shell \((m^2,(m+1)^2]\).
The prime-power reserve appearing in the square-shell event-energy decomposition is

\[
A_m:=L_m\frac{P_m+P_{m+1}}2.
\]

## 2. Exact product + oriented-area identity

Define the discrete oriented-area/Wronskian term

\[
\boxed{
W_m:=\Theta_{m+1}P_m-\Theta_mP_{m+1}.
}
\]

A direct expansion gives

\[
(\Theta_{m+1}-\Theta_m)(P_m+P_{m+1})
=
(\Theta_{m+1}P_{m+1}-\Theta_mP_m)+W_m.
\]

Therefore

\[
\boxed{
A_m
=
\frac12\Delta(\Theta P)_m
+
\frac12W_m.
}
\]

Summing from a fixed lower index m0 to M-1 yields

\[
\boxed{
\sum_{m=m_0}^{M-1}A_m
=
\frac12\bigl(\Theta_MP_M-\Theta_{m_0}P_{m_0}\bigr)
+
\frac12\sum_{m=m_0}^{M-1}W_m.
}
\]

Thus the prime-power reserve separates exactly into:
1. an endpoint product term; and
2. a cumulative oriented area of the discrete trajectory \((\Theta_m,P_m)\).

## 3. Unconditional asymptotic of the full reserve

For a prime p in the square shell \((m^2,(m+1)^2]\), set

\[
a_m:=\frac{P_m+P_{m+1}}2.
\]

Since \(P_m\sim m\), uniformly across a shell

\[
\frac{a_m}{\sqrt p}\to1.
\]

Hence, up to a fixed initial range,

\[
\sum_{m<M}A_m
=
\sum_{p\le M^2}(\log p)\,a_{\lfloor\sqrt{p-0}\rfloor}
\sim
\sum_{p\le M^2}\sqrt p\log p.
\]

Using Stieltjes partial summation and \(\vartheta(x)\sim x\),

\[
\sum_{p\le X}\sqrt p\log p
=
\int_{2^-}^{X}t^{1/2}\,d\vartheta(t)
\]

\[
=
\sqrt X\,\vartheta(X)
-
\frac12\int_2^X\frac{\vartheta(t)}{\sqrt t}\,dt
\sim
X^{3/2}-\frac13X^{3/2}.
\]

Therefore

\[
\boxed{
\sum_{m<M}A_m\sim\frac23M^3.
}
\]

This is unconditional and uses only the ordinary PNT plus the exact prime-power decomposition.

## 4. Unconditional cumulative oriented area

The endpoint product satisfies

\[
\Theta_MP_M\sim M^3.
\]

Substituting the reserve asymptotic into the exact identity gives

\[
\sum_{m<M}W_m
=
2\sum_{m<M}A_m-\Theta_MP_M+O(1),
\]

and therefore

\[
\boxed{
\sum_{m<M}W_m\sim\frac13M^3.
}
\]

Consequently the familiar prime-square reserve coefficient decomposes as

\[
\boxed{
\frac23
=
\frac12+\frac16.
}
\]

Interpretation:
- \(\frac12M^3\) comes from half of the endpoint product \(\Theta_MP_M\);
- \(\frac16M^3\) comes from half of the positive cumulative oriented area.

This is a structural decomposition of the deterministic prime-power buffer. It is not an RH proof and does not control the remaining event-energy transport terms.

## 5. Local sign is not available

Because

\[
W_m
=
\Theta_m\Theta_{m+1}
\left(
\frac{P_m}{\Theta_m}-\frac{P_{m+1}}{\Theta_{m+1}}
\right),
\]

one would have \(W_m\ge0\) if \(P_m/\Theta_m\) were monotonically decreasing.
That monotonicity is false in finite data.

For the direct audit through \(5\times10^6\), corresponding to square endpoints through \(m=2236\):
- positive \(W_m\): 1,866 shells;
- negative \(W_m\): 368 shells;
- zero \(W_m\): 0.

Thus no shellwise positivity claim is retained.
The result is genuinely cumulative.

Classification:

`PRIMEPOWER_ORIENTED_AREA_DECOMPOSITION`.

Permanent guard:

`ORIENTED_AREA_POINTWISE_SIGN_GUARD` — the positive \(M^3/3\) cumulative oriented area must not be replaced by a false claim that every local Wronskian increment is nonnegative.

## 6. Numerical regression check

At finite cutoffs the convergence is slow but points toward the proved constants.
For example, with the direct prime computation through 5,000,000:

- M=500:
  - cumulative reserve / M^3 ~= 0.76674;
  - cumulative W / M^3 ~= 0.39240;
  - endpoint product / M^3 ~= 1.14108.
- M=1000:
  - cumulative reserve / M^3 ~= 0.74534;
  - cumulative W / M^3 ~= 0.38993;
  - endpoint product / M^3 ~= 1.10075.
- M=2236:
  - cumulative reserve / M^3 ~= 0.72829;
  - cumulative W / M^3 ~= 0.38352;
  - endpoint product / M^3 ~= 1.07306.

The target limits are respectively \(2/3\), \(1/3\), and 1.
These numerical values are regression checks only; the asymptotics above are derived independently from PNT.

## 7. Consequence for the live RH route

The square-shell event-energy sum is

\[
\mathcal B_{m,K}
=
\sum_j
\left[
L_j\frac{R_j+R_{j+1}}2
-
A_j
-
Q_j
\right],
\]

where \(R_j=\psi(j^2)-j^2\).
The deterministic negative part \(A_j\) now has an exact cumulative geometry rather than merely a heuristic \(2/3\) coefficient.

The remaining problem is therefore sharpened to the signed residual

\[
\boxed{
\sum_j
\left[
L_j\frac{R_j+R_{j+1}}2-Q_j
\right].
}
\]

A viable continuation must compare this joint residual with the endpoint-plus-oriented-area reserve without replacing either \(R_j\) or \(Q_j\) by absolute values, and without importing an RH-strength bound for \(\psi(x)-x\).

The next audit target is whether the joint residual itself has a discrete integration-by-parts decomposition that exposes a second oriented-area or boundary cancellation, rather than a Type-II/short-interval mean-square re-encoding.
