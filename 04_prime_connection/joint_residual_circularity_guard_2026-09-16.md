# Joint square-shell residual circularity guard — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Chord-residual identity: EXACT.
- Canonical second integration-by-parts attempt: CLOSED_AS_CIRCULAR_REENCODING.

## 1. Setup

Let

\[
E(t)=\vartheta(t)-t,
\]

and for the square shell

\[
a=m^2,\qquad b=(m+1)^2,\qquad h_m=b-a=2m+1
\]

write

\[
E_m=E(a),\qquad E_{m+1}=E(b),
\]

\[
L_m=\vartheta(b)-\vartheta(a).
\]

Recall the signed placement moment

\[
Q_m=\sum_{a<p\le b}\left(p-\frac{a+b}{2}\right)\log p.
\]

## 2. Exact chord identity for Q_m

The theta chord on [a,b] is the sum of the identity line t and the linear interpolation of the endpoint errors.
Therefore the previously derived chord-area formula becomes

\[
\boxed{
Q_m
=
h_m\frac{E_m+E_{m+1}}2
-
\int_a^b E(t)\,dt.
}
\]

This is exact.

## 3. Original event energy is recovered immediately

Since

\[
E_{m+1}-E_m=L_m-h_m,
\]

we obtain

\[
\begin{aligned}
L_m\frac{E_m+E_{m+1}}2-Q_m
&=(L_m-h_m)\frac{E_m+E_{m+1}}2
+\int_a^bE(t)dt\\
&=\frac12(E_{m+1}^2-E_m^2)
+\int_a^bE(t)dt.
\end{aligned}
\]

Thus

\[
\boxed{
\Delta_mH
=\int_a^bE(t)dt
+\frac12(E_{m+1}^2-E_m^2),
}
\]

which is exactly the original definition of the Chebyshev event energy increment.

Therefore using the local chord residual to seek a second independent area reserve does not create new information; it reconstructs H identically.

## 4. The live joint residual is exactly H plus the known prime-power reserve

Write

\[
R_m=\psi(m^2)-m^2,
\qquad
P_m=\psi(m^2)-\vartheta(m^2),
\]

so

\[
R_m=E_m+P_m.
\]

Define the residual previously isolated for the live route,

\[
J_m:=L_m\frac{R_m+R_{m+1}}2-Q_m,
\]

and the explicit prime-power reserve

\[
A_m:=L_m\frac{P_m+P_{m+1}}2.
\]

Then exactly

\[
\boxed{
J_m-A_m=\Delta_mH.
}
\]

Equivalently,

\[
\boxed{
J_m=A_m+\Delta_mH.
}
\]

Hence the desired inequality

\[
J_m<A_m
\]

is not a weaker auxiliary estimate: it is precisely

\[
\Delta_mH<0.
\]

After summing shells, the same statement becomes

\[
\sum J_m-\sum A_m
=H(\text{final square})-H(\text{initial square}).
\]

## 5. Audit verdict

A purely algebraic second integration-by-parts/oriented-area decomposition of the joint residual cannot by itself solve the remaining problem. In the canonical shell variables it is exactly circular.

Classification:

`JOINT_RESIDUAL_CIRCULARITY_GUARD`.

This does not say that every possible new inequality involving J_m is circular. It says that any proposed progress must introduce genuinely new arithmetic information beyond:
- the definitions of theta, psi and the prime-power tail;
- endpoint/chord interpolation;
- algebraic integration by parts;
- the already known event-energy identity.

## 6. Consequence for the next route

The next candidate must constrain the correlation between two genuinely different scales or structures, rather than rearrange H.
The prime-square cross-scale flux

\[
W_m^{(2)}=\vartheta(m)\,L_m-\vartheta(m^2)\,[\vartheta(m+1)-\vartheta(m)]
\]

is one such exact cross-scale object because it couples prime information near m and m^2.

A viable continuation should therefore test whether the hard event-energy residual has a nontrivial correlation/inequality with this cross-scale flux (or a higher prime-power analogue) that is not an identity and does not require an RH-strength bound as an input.
