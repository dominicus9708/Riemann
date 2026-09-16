# Square-shell event-energy audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Square-shell decomposition: EXACT.
- Prime-power separation at square endpoints: EXACT.
- Finite computation through x <= 5,000,000: NUMERICAL / all tested complete square shells have negative event-energy increment.
- Uniform one-shell or fixed-K square-shell negativity: CLOSED by Littlewood positive oscillations + Brun–Titchmarsh occupancy control.
- Absolute-value control of the within-shell centroid term: CLOSED at leading scale.
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

The leading term of P_m is the prime-square layer theta(m) ~ m. Its shell contribution is therefore naturally on the m^2 scale whenever the shell carries its expected logarithmic mass. Summing to M produces the x^{3/2} prime-square scale with x=M^2.

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

## 6. Exact chord-residual form of the placement term

Let

\[
h_m=(m+1)^2-m^2=2m+1,
\]

and on the shell define the linear chord joining the two theta endpoints,

\[
C_m(t)=\vartheta(m^2)+\frac{t-m^2}{h_m}L_m.
\]

Stieltjes integration by parts gives

\[
\sum_{m^2<p\le(m+1)^2}p\log p
=(m+1)^2L_m-
\int_{m^2}^{(m+1)^2}\bigl(\vartheta(t)-\vartheta(m^2)\bigr)dt.
\]

Therefore

\[
\boxed{
Q_m=-\int_{m^2}^{(m+1)^2}\bigl(\vartheta(t)-C_m(t)\bigr)dt.
}
\]

Thus Q_m is exactly the signed area between the local theta staircase and its endpoint chord. It is not an independent statistic: it is the within-shell shape information discarded by endpoint-only summaries.

## 7. Absolute centroid bound saturates the prime-square reserve scale

Because every p in I_m satisfies

\[
|p-c_m|\le\frac{h_m}{2},
\]

and all log p weights are positive,

\[
\boxed{
|Q_m|\le\frac{h_m}{2}L_m.
}
\]

The prime-power reserve term in the exact shell decomposition is

\[
L_m\frac{P_m+P_{m+1}}2.
\]

Whenever L_m>0, the ratio between the trivial support bound for |Q_m| and this reserve is

\[
\frac{(h_m/2)L_m}{L_m(P_m+P_{m+1})/2}
=
\frac{h_m}{P_m+P_{m+1}}.
\]

Now

\[
P_m=\vartheta(m)+O(m^{2/3})\sim m
\]

by the ordinary prime number theorem applied at the root scale. Hence

\[
P_m+P_{m+1}\sim2m+1=h_m,
\]

so

\[
\boxed{
\frac{(h_m/2)L_m}{L_m(P_m+P_{m+1})/2}\to1.
}
\]

Therefore triangle inequality / support-only control of Q_m is asymptotically coefficient-sharp against the leading prime-square reserve. It cannot leave a deterministic positive margin.

Classification:

`CENTROID_SUPPORT_BOUND_SATURATION`.

This closes any continuation that estimates Q_m only by |p-c_m|<=h_m/2, Holder, or an equivalent unsigned support norm. A surviving argument must use the sign/order of prime placement across shells, or a joint cancellation with the psi-transport term.

For the finite N=5,000,000 audit, the observed ratio

\[
\frac{|Q_m|}{(h_m/2)L_m}
\]

had maximum approximately 0.36794 (at m=10), median approximately 0.02231, and 99th percentile approximately 0.15068. This is useful numerical structure, but the exact support bound shows that such small finite ratios cannot be assumed uniformly.

## 8. Surviving scale-growing target

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

The middle term is the explicit prime-power reserve; its leading square contribution is visible without zero input. The first and third terms are the remaining psi-transport and signed within-shell placement terms.

The next viable question is therefore not `is every square shell negative?` and not `can |Q_m| be bounded absolutely?` but:

Can one prove a scale-growing, nonlocal inequality in which the JOINT signed quantity

\[
\sum_{j=m}^{m+K-1}\left[L_j\frac{R_j+R_{j+1}}2-Q_j\right]
\]

is dominated by the accumulated prime-power reserve, without importing an RH-equivalent bound for psi(x)-x or a Weil/Li explicit-formula positivity criterion?

Any proposed answer must be tested against:
- `FIXED_SQUARE_SHELL_LOCALITY_BARRIER`;
- `PRIME_SQUARE_RECOVERY_HORIZON_GUARD`;
- `CENTROID_SUPPORT_BOUND_SATURATION`;
- `SELBERG_HARDY_AVERAGING_BARRIER`;
- `HYPERBOLA_EXPONENT_INFLATION`;
- `KERNEL_MARGIN_DELAY_DUALITY`;
- `WEIL_SUPPORT_RESOLUTION_GUARD`.
