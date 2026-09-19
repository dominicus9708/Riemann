# j=2 hyper-Kloosterman Mellin diagonalization and exact H-gap — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: one-sided prime-modulus route after simultaneous completion produced a rank-3 hyper-Kloosterman kernel.
- New exact calculation: retaining the numerator factorization \(c=nk\) and using the multiplicative Mellin transform of \(\mathrm{Kl}_3\) gives a per-modulus bound \(p^{4/3+o(1)}=H^{4+o(1)}\).
- Restoring the modulus sum and Poisson prefactor gives total scale H^6, while the connected determinant target is H^5.
- Therefore the route removes the generic completion overhead but leaves exactly the original one-factor-H centered-variance deficit.
- Important correction: the earlier numerical comparison between a Kloosterman saving and the branchwise H^(1/8) amplitude deficit mixed two different proof architectures and must not be interpreted as an H^(1/32) improvement.
- Classification:
  - \`KL3_MELLIN_DIAGONALIZATION_RAW_VARIANCE_SCALE\`;
  - \`H1_8_VS_KL_SAVING_CROSS_ARCHITECTURE_COMPARISON_GUARD\`.

## 1. Favorable completed model

Use the determinant false-control geometry only as a scale model:
\[
\frac{D}{P}
\sum_{p\asymp P}
\lambda_p
\sum_{|n|,|k|\lesssim H}
u_{n,k}
\sum_{m,r\asymp \sqrt p}
W_1(m/\sqrt p)W_2(r/\sqrt p)
e_p\!\left(nk\,\overline{mr}\right),
\]
with
\[
D=H^2,\qquad
P=H^3,\qquad
\frac DP=H^{-1}.
\]

The variables \(n,k\) are the two short numerator variables from the determinant completion.

The critical smooth factors have
\[
m,r\asymp H^{3/2}=\sqrt p.
\]

## 2. Double completion

Simultaneous completion in m,r gives, after cancellation of the Poisson normalization against the unnormalized complete sum,
\[
\sum_{h_1,h_2\asymp \sqrt p}
\alpha_{h_1}\beta_{h_2}
\mathrm{Kl}_3(nk h_1h_2;p),
\]
up to rapidly decaying tails and H^epsilon losses.

Thus the fixed-modulus arithmetic core is
\[
\mathcal S_p
=
\sum_{\substack{n,k\asymp p^{1/3}\\h_1,h_2\asymp p^{1/2}}}
a_n b_k c_{h_1}d_{h_2}
\mathrm{Kl}_3(nkh_1h_2;p).
\]

## 3. Exact multiplicative Mellin transform

Use the normalized convention
\[
\mathrm{Kl}_3(t;p)
=
p^{-1}
\sum_{\substack{xyz=t\\x,y,z\in\mathbf F_p^\times}}
e_p(x+y+z).
\]

For a multiplicative character \(\chi\bmod p\),
\[
\widehat K(\chi)
:=
\sum_{t\in\mathbf F_p^\times}
\mathrm{Kl}_3(t;p)\chi(t)
=
p^{-1}\tau(\chi)^3.
\]

For nonprincipal \(\chi\),
\[
|\tau(\chi)|=\sqrt p,
\]
hence
\[
\boxed{
|\widehat K(\chi)|=p^{1/2}.
}
\]

The principal character contributes only a negligible exceptional mode under this normalization.

Fourier inversion on \(\mathbf F_p^\times\) gives
\[
\mathcal S_p
=
\frac1{p-1}
\sum_{\chi\bmod p}
\widehat K(\chi)
A(\chi)B(\chi)C(\chi)D(\chi),
\]
where
\[
A(\chi)=\sum_{n\asymp p^{1/3}}a_n\overline{\chi(n)}
\]
and similarly for the other three variables.

Therefore
\[
|\mathcal S_p|
\ll
p^{-1/2}
\sum_\chi
|A(\chi)C(\chi)|
|B(\chi)D(\chi)|
+
p^{o(1)}.
\]

## 4. Mixed second moments

Apply Cauchy:
\[
|\mathcal S_p|
\ll
p^{-1/2}
\left(
\sum_\chi |A(\chi)C(\chi)|^2
\right)^{1/2}
\left(
\sum_\chi |B(\chi)D(\chi)|^2
\right)^{1/2}.
\]

Consider the first mixed moment.

Character orthogonality gives
\[
\sum_\chi |A(\chi)C(\chi)|^2
=
(p-1)
\sum_{\substack{
n_1h_1\equiv n_2h_2\pmod p
}}
a_{n_1}\bar a_{n_2}
c_{h_1}\bar c_{h_2}.
\]

But
\[
n_i\asymp p^{1/3},
\qquad
h_i\asymp p^{1/2},
\]
so
\[
n_i h_i\asymp p^{5/6}<p
\]
for sufficiently separated smooth dyadic supports.

Thus the congruence is an integer product equality:
\[
n_1h_1=n_2h_2.
\]

The multiplicative energy of two intervals at these lengths is divisor-diagonal:
\[
\#\{n_1h_1=n_2h_2\}
\ll_\varepsilon
p^{5/6+\varepsilon}.
\]

Hence
\[
\boxed{
\sum_\chi |A(\chi)C(\chi)|^2
\ll_\varepsilon
p^{11/6+\varepsilon}.
}
\]

The same bound holds for the other mixed pair.

## 5. Per-modulus bound

Therefore
\[
|\mathcal S_p|
\ll_\varepsilon
p^{-1/2}
p^{11/12}
p^{11/12}
=
\boxed{
p^{4/3+\varepsilon}.
}
\]

Since
\[
p\asymp H^3,
\]
this is
\[
\boxed{
|\mathcal S_p|
\ll_\varepsilon
H^{4+\varepsilon}.
}
\]

This is stronger than treating \(c=nk\) as one generic coefficient and then invoking a black-box bilinear \(\mathrm{Kl}_3\) estimate.

Classification:
\`KL3_FOUR_FACTOR_MELLIN_BOUND_P4_3\`.

## 6. Restore the outer modulus sum

There are
\[
\asymp H^3
\]
prime moduli on the power scale.

Restoring the determinant Poisson prefactor
\[
D/P=H^{-1}
\]
gives
\[
H^{-1}
\cdot
H^3
\cdot
H^4
=
\boxed{H^6}.
\]

The connected centered determinant target is
\[
\boxed{H^5}.
\]

Thus the remaining gap is exactly
\[
\boxed H.
\]

This is the same one-factor-H variance deficit already identified before completion.

Permanent interpretation:
\`HYPERKL_COMPLETION_RETURNS_TO_RAW_DETERMINANT_SCALE\`.

## 7. Why this is still useful

The generic Poisson + Kloosterman-fraction benchmark was polynomially worse than raw scale.

The \(\mathrm{Kl}_3\) Mellin calculation removes that additional generic-completion loss and returns to the natural H^6 shell mass.

Therefore it proves that:
- reciprocal double completion itself is not the source of a new polynomial obstruction;
- the unresolved saving is entirely the connected/modulus-average saving H^6 -> H^5.

This is a sharper localization of the problem.

## 8. Cross-architecture correction

The branchwise double-Vaughan estimate
\[
H^{6+1/8}
\]
belongs to the **original amplitude/DLS architecture**.

The hyper-Kloosterman calculation above belongs to the **squared centered determinant/variance architecture**, whose target is H^5 after normalization.

Therefore one must not write
\[
H^{1/8}\times H^{-3/32}=H^{1/32}
\]
as an actual improved bound.

That comparison mixes unmatched normalizations and different transformed objects.

Permanent guard:
\`DO_NOT_MULTIPLY_SAVINGS_ACROSS_AMPLITUDE_AND_VARIANCE_ARCHITECTURES\`.

## 9. Modulus-average target

Let
\[
\mathcal S_p
\]
denote the fixed-modulus four-factor hyper-Kloosterman form above.

A sufficient next theorem is
\[
\boxed{
\sum_{\substack{p\asymp H^3\\p\ {\rm prime}}}
\lambda_p\mathcal S_p
\ll_\varepsilon
H^{6+\varepsilon}.
}
\]

Combined with the outer \(H^{-1}\) factor this gives the connected target H^5.

The pointwise bound only gives
\[
H^3\cdot H^4=H^7.
\]

Thus one needs exactly
\[
\boxed{H^{-1}}
\]
of cancellation in the average over the prime moduli.

Classification:
\`KL3_PRIME_MODULUS_AVERAGE_H_SAVING_OPEN\`.

## 10. Standard character large sieve does not automatically supply H

After Mellin diagonalization, summing over varying prime moduli introduces independent character groups modulo each p.

The classical character large sieve over moduli up to
\[
P=H^3
\]
has conductor term
\[
P^2
\]
which dominates all present Dirichlet-polynomial lengths \(P^{1/2}\) and below.

Thus, at the power scale, it reproduces the trivial total number of modulus-character pairs and does not give the required extra H.

Hence the remaining H-saving must use more than:
- fixed-modulus Mellin diagonalization;
- absolute values in the character variable;
- the standard large sieve over varying moduli.

Permanent rule:
\`STANDARD_CHARACTER_LARGE_SIEVE_NO_PRIME_MODULUS_H_GAIN\`.

## 11. Current verdict

The legal one-sided hyper-Kloosterman route is now sharply classified:

\[
\boxed{
\text{double completion}
\to
\text{exact }\mathrm{Kl}_3
\to
\text{Mellin diagonalization}
\to
H^6
}
\]

and then stalls one factor H above the centered target.

A new theorem would have to control the prime-modulus average of these four-factor \(\mathrm{Kl}_3\) forms.

No such exact theorem has yet been identified.

Therefore the smaller official j=2 technical target remains the separate amplitude-side H^(1/8) residual.
