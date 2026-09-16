# Square-shell event-energy audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Square-shell decomposition: EXACT.
- Prime-power separation at square endpoints: EXACT.
- Finite computation through x <= 5,000,000: NUMERICAL / all tested complete square shells have negative event-energy increment.
- Uniform one-shell or fixed-K square-shell negativity: CLOSED by Littlewood positive oscillations + Brun–Titchmarsh occupancy control.
- Scale-growing shell compensation: OPEN.

## 1. Exact square-shell decomposition

Let

\[
H(x)=\frac12\vartheta(x)^2-\sum_{p\le x}p\log p+2.
\]

For integer m>=2 define the square shell

\[
I_m=(m^2,(m+1)^2],
\]

its logarithmic prime mass

\[
L_m=\vartheta((m+1)^2)-\vartheta(m^2),
\]

and endpoint Chebyshev errors

\[
E_m=\vartheta(m^2)-m^2.
\]

Let the geometric midpoint be

\[
c_m=\frac{m^2+(m+1)^2}{2}=m^2+m+\frac12,
\]

and define the centered log-weighted prime first moment

\[
Q_m=\sum_{m^2<p\le(m+1)^2}(p-c_m)\log p.
\]

Then exactly

\[
\boxed{
H((m+1)^2)-H(m^2)
=L_m\frac{E_m+E_{m+1}}2-Q_m.
}
\]

Equivalently, if

\[
d_m=L_m-(2m+1)=E_{m+1}-E_m,
\]

then

\[
\boxed{
\Delta_mH=L_m\left(E_m+\frac{d_m}{2}\right)-Q_m.
}
\]

This is the exact version of the earlier approximate square-bin defect based on prime counts and the replacement log p ~= 2 log m. The present form keeps the true logarithmic weights and the within-shell prime placement moment Q_m.

## 2. Exact prime-power separation at square endpoints

Write

\[
R_m=\psi(m^2)-m^2,
\qquad
P_m=\psi(m^2)-\vartheta(m^2).
\]

Then

\[
E_m=R_m-P_m.
\]

Using

\[
\psi(x)=\sum_{k\ge1}\vartheta(x^{1/k}),
\]

we obtain at x=m^2

\[
\boxed{
P_m=\vartheta(m)+\sum_{k\ge3}\vartheta(m^{2/k}).
}
\]

Hence the square-shell energy increment has the exact split

\[
\boxed{
\Delta_mH
=
L_m\frac{R_m+R_{m+1}}2
-
L_m\frac{P_m+P_{m+1}}2
-Q_m.
}
\]

The leading term of P_m is the prime-square layer theta(m) ~ m. Since L_m ~ 2m, its shell reserve is naturally of order -m^2. Summing to M gives the familiar x^{3/2} scale with x=M^2.

This explains why square shells are the geometrically natural shell scale for the prime-square reserve. It does not prove the required sign because the R_m transport and Q_m placement terms remain.

## 3. Finite computation

The accompanying script `scripts/audit_square_shell_event_energy.py` computes L_m, E_m, Q_m and Delta_m H directly from the prime list.

For N=5,000,000, all complete shells

\[
2\le m\le2235,
\qquad (m+1)^2\le N,
\]

were tested.

Numerical summary:
- complete shells tested: 2234;
- shells with Delta_m H > 0: 0;
- largest observed Delta_m H: approximately -8.97798213 at m=2;
- range of Delta_m H / m^2: approximately [-3.77194,-0.95358].

Therefore one-shell negativity is an extremely strong finite-range pattern in this range.

It must not be promoted to an asymptotic conjectural mechanism without the obstruction below.

## 4. Why fixed square-shell locality must eventually fail

Littlewood's oscillation theorem gives

\[
\psi(x)-x=\Omega_+\!\left(\sqrt{x}\,\log\log\log x\right).
\]

Since

\[
\psi(x)-\vartheta(x)=O(\sqrt{x}),
\]

the same positive scale survives for theta:

\[
\vartheta(x)-x
=\Omega_+\!\left(\sqrt{x}\,\log\log\log x\right).
\]

Choose a sequence of prime cutoffs p_n with

\[
u_n:=\vartheta(p_n)-p_n
\ge c\sqrt{p_n}\,\log\log\log p_n.
\]

For consecutive primes, with g_j=p_j-p_{j-1},

\[
u_{j-1}=u_j+g_j-\log p_j\ge u_j-\log p_n.
\]

Thus for

\[
R_n=\left\lfloor\frac{u_n}{4\log p_n}\right\rfloor
\]

all of the last R_n+1 prime events satisfy, for sufficiently large n,

\[
u_{n-r}\ge\frac34u_n\gg\log p_n,
\]

and therefore

\[
\Delta_{p_{n-r}}H
=
(\log p_{n-r})\left(u_{n-r}-\frac12\log p_{n-r}\right)>0.
\]

So there are arbitrarily long runs of consecutive positive event-energy injections, with

\[
R_n\gg\frac{\sqrt{p_n}\,\log\log\log p_n}{\log p_n}.
\]

By the prime number theorem these last R_n primes lie in [p_n/2,p_n] for sufficiently large n. A square shell there has length asymptotic to 2 sqrt(p_n), and Brun–Titchmarsh gives a uniform occupancy bound

\[
\#\{p\in(m^2,(m+1)^2]\}
=O\!\left(\frac{\sqrt{p_n}}{\log p_n}\right).
\]

Consequently the positive run necessarily spans

\[
\Omega(\log\log\log p_n)
\]

square shells along an unbounded sequence.

Every prime event inside the interior of that span is positive; empty shells contribute zero. Hence no rule using a uniformly bounded number K of consecutive square shells can make every grouped energy increment nonpositive.

Classification:

`FIXED_SQUARE_SHELL_LOCALITY_BARRIER`.

This is stronger than the earlier fixed-prime-count locality barrier because it closes the natural prime-square shell scale itself.

## 5. Positive-run energy mass

On the same sequence, each event in the retained run has

\[
\Delta_pH\gg (\log p_n)u_n.
\]

With R_n >> u_n/log p_n events, the total positive energy inserted by the run obeys

\[
\boxed{
\sum_{\text{run}}\Delta_pH
\gg u_n^2
\gg p_n(\log\log\log p_n)^2.
}
\]

The deterministic prime-square reserve contributed by one square shell is only on its natural O(p_n) scale. Therefore any compensation argument that relies only on accumulating this shellwise prime-square reserve may require a recovery horizon growing at least on a poly-log-log-log scale along these excursions; fixed recovery length is impossible.

Do not interpret this as a universal lower bound for every conceivable nonlocal proof. It applies to shell-reserve compensation mechanisms whose negative budget per shell remains O(p_n).

Audit tag:

`PRIME_SQUARE_RECOVERY_HORIZON_GUARD`.

## 6. Surviving scale-growing target

For K=K(m) define

\[
\mathcal B_{m,K}
=H((m+K)^2)-H(m^2).
\]

The exact shell sum is

\[
\boxed{
\mathcal B_{m,K}
=
\sum_{j=m}^{m+K-1}
\left[
L_j\frac{R_j+R_{j+1}}2
-
L_j\frac{P_j+P_{j+1}}2
-Q_j
\right].
}
\]

The middle term is the explicit prime-power reserve; its leading square contribution is visible without zero input. The first and third terms are the remaining psi-transport and within-shell placement terms.

The next viable question is therefore not `is every square shell negative?` but:

Can one prove a scale-growing, nonlocal inequality in which the combined R_j transport and Q_j placement terms are dominated by the accumulated P_j prime-power reserve, without importing an RH-equivalent bound for psi(x)-x or a Weil/Li explicit-formula positivity criterion?

Any proposed answer must be tested against:
- `FIXED_SQUARE_SHELL_LOCALITY_BARRIER`;
- `PRIME_SQUARE_RECOVERY_HORIZON_GUARD`;
- `SELBERG_HARDY_AVERAGING_BARRIER`;
- `HYPERBOLA_EXPONENT_INFLATION`;
- `KERNEL_MARGIN_DELAY_DUALITY`;
- `WEIL_SUPPORT_RESOLUTION_GUARD`.
