# Robert–Sargos Type-II mean-square audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Robert–Sargos (2006) three-dimensional real monomial theorem: DIRECTLY RELEVANT.
- Previous statement that no theorem-level real three-variable monomial source had been identified: CORRECTED.
- Direct use of Robert–Sargos Theorem 1 via L2 duality: INSUFFICIENT.
- A one-Cauchy-less adaptation of their double-large-sieve proof to the present outer mean square: DERIVED, but still INSUFFICIENT.
- Worst unresolved corner `D=K, N=1`: optimized classical spacing bound misses the target by a factor `K^(3/4+o(1))`.
- Therefore the remaining mechanism must exploit arithmetic coefficient structure and/or an ordered-phase transformation not present in the arbitrary-coefficient spacing theorem.

## 1. Present Type-II target

On a dyadic Voronoi block write the unweighted Type-II model as

\[
S_n(M,L)
=\sum_{a\asymp M}\alpha_a
 \sum_{b\asymp L}\beta_b
 e\!\left(2K\sqrt n\,a^{-1/2}b^{-1/2}\right),
\qquad ML\asymp D.
\]

The sufficient mean-square target is

\[
\boxed{
\sum_{N<n\le2N}|S_n(M,L)|^2
\ll_\varepsilon N D^{1+\varepsilon}.
}
\]

After restoring the Voronoi weight `D^(-1/4)` in the original `d`-sum, this corresponds to the required `N D^(1/2+epsilon)` scale.

The normalized oscillation parameter is

\[
\boxed{
X_0\asymp \frac{K\sqrt N}{\sqrt D}.
}
\]

## 2. Direct literature match

Robert and Sargos, *Three-dimensional exponential sums with monomials*, J. Reine Angew. Math. 591 (2006), study

\[
\sum_{h\asymp H}\sum_{n\asymp N}a(h,n)
\sum_{m\asymp M}b(m)
 e\!\left(
 X\frac{h^\beta n^\gamma m^\alpha}
 {H^\beta N^\gamma M^\alpha}
 \right),
\]

with bounded complex coefficients and fixed real exponents satisfying
`alpha(alpha-1) beta gamma != 0`.

The present phase fits formally with

\[
(\beta,\gamma,\alpha)
=\left(\frac12,-\frac12,-\frac12\right).
\]

Thus this is not merely an analogous functional class: it is a direct real three-variable monomial match.

Permanent correction:

`THREE_VARIABLE_MONOMIAL_LITERATURE_MATCH_CORRECTION` — do not state that no real three-variable monomial theorem has been identified. Robert–Sargos 2006 is a direct match at the phase-class level.

## 3. Robert–Sargos spacing theorem

Their Theorem 2 gives, for fixed `alpha != 0,1`, the optimal-up-to-epsilon spacing count

\[
\#\left\{m_i\asymp M:
|m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|
\le \delta M^\alpha\right\}
\ll_\varepsilon M^{2+\varepsilon}+\delta M^{4+\varepsilon}.
\]

For `alpha=-1/2`, this directly controls the four-point spacing that appears after Cauchy/differencing in one reciprocal-square-root factor.

Their proof of the three-dimensional theorem combines this four-variable estimate with the Bombieri–Iwaniec double large sieve.

## 4. Why Theorem 1 itself does not close the present mean square

The present target is an L2 norm over the outer variable `n`, whereas Robert–Sargos Theorem 1 controls one scalar three-dimensional linear sum.

By duality,

\[
\left(\sum_n|S_n|^2\right)^{1/2}
=\sup_{\|c\|_2=1}
\left|\sum_n c_n S_n\right|.
\]

Although `|c_n|<=1`, applying their arbitrary-coefficient linear theorem at this point loses the L2 normalization and is far too weak at the critical powers.

Therefore a direct theorem-1 import is classified

`ROBERT_SARGOS_LINEAR_TO_L2_DEFICIT`.

## 5. One-Cauchy-less adaptation of their proof

The proof structure can nevertheless be adapted more closely to the present norm.

Normalize

\[
u(n,a)=\left(\frac nN\right)^{1/2}
\left(\frac aM\right)^{-1/2},
\qquad
v(b)=\left(\frac bL\right)^{-1/2}.
\]

Then

\[
S_n=\sum_a\alpha_a\sum_b\beta_b e(X_0u(n,a)v(b)).
\]

Apply Cauchy only in the `a` variable, not in both outer variables as in the scalar three-dimensional sum:

\[
\sum_n|S_n|^2
\le
M\sum_{n,a}
\left|\sum_b\beta_b e(X_0u(n,a)v(b))\right|^2.
\]

After expansion in `b_1,b_2`, this is a double-large-sieve bilinear form between

\[
u(n,a)
\]

and

\[
v(b_1)-v(b_2).
\]

Using the Fouvry–Iwaniec two-variable spacing estimate for the first family and Robert–Sargos Theorem 2 for the second gives, up to `K^epsilon`/divisor factors,

\[
B_1
\ll
NM+\frac{N^2M^2}{X_0},
\]

and

\[
B_2
\ll
L^2+\frac{L^4}{X_0}.
\]

Hence the resulting mean-square estimate is

\[
\boxed{
\mathcal Q_{N,M,L}
\ll_arepsilon
M X_0^{1/2}
\left(NM+\frac{N^2M^2}{X_0}\right)^{1/2}
\left(L^2+\frac{L^4}{X_0}\right)^{1/2}
K^\varepsilon.
}
\]

This is the natural outer-L2 analogue of the Robert–Sargos/Fouvry–Iwaniec spacing mechanism.

## 6. Worst unresolved corner

Take the extreme unresolved Voronoi block

\[
D=K,\qquad N=1,
\qquad X_0\asymp K^{1/2}.
\]

Write

\[
M=K^m,
\qquad
L=K^{1-m}.
\]

Optimizing the preceding bound over all factor splits `0<=m<=1` gives the minimum at the balanced transition range (including `m=1/2`) and yields

\[
\boxed{
\mathcal Q_{1,M,L}
\ll K^{7/4+o(1)}.
}
\]

But the required unweighted Type-II target is

\[
\boxed{
\mathcal Q_{1,M,L}
\ll K^{1+\varepsilon}.
}
\]

Thus the classical arbitrary-coefficient spacing mechanism misses by

\[
\boxed{K^{3/4-o(1)}}.
\]

This deficit remains after optimizing the factor split; it is not an artefact of choosing `M=L=sqrt(K)`.

## 7. Interpretation of the deficit

The failure has a useful structural meaning.

Robert–Sargos already gives essentially optimal four-point spacing for a single monomial factor. Therefore merely sharpening the same unsigned spacing count is unlikely to supply the missing `K^(3/4)`.

The present problem contains information absent from their arbitrary-coefficient theorem:

1. one Vaughan Type-II factor carries an actual Möbius coefficient `mu(w)`;
2. the second coefficient is a restricted divisor-Möbius sum `b_d`;
3. the reciprocal phase remains ordered across the dyadic product block;
4. the desired norm is only the outer `n` mean square, not a worst-case scalar triple sum.

Consequently the next proof mechanism must preserve at least one of these structures before absolute Cauchy/spacing destroys it.

## 8. Relation to the product-collapse / Chowla barrier

Expanding the outer mean square first collapses the phase to the product variable `r=ab`:

\[
\sum_n |S_n|^2
=
\sum_{r,r'}\gamma_r\overline{\gamma_{r'}}
\sum_n
 e\!\left(2K\sqrt n(r^{-1/2}-r'^{-1/2})\right),
\]

where

\[
\gamma_r
=\sum_{ab=r}\alpha_a\beta_b
\]

within the Type-II box.

Thus an arbitrary-coefficient treatment forgets the factorization after forming `gamma_r`, while an unphased short-interval reduction over-strengthens the problem into a Chowla-style correlation estimate.

The new audit locates the viable middle route:

> retain the factorization and at least one arithmetic coefficient while also retaining the reciprocal ordered phase.

## 9. Recent literature check

Javier Pliego (2024), *Estimates for a three-dimensional exponential sum with monomials*, gives newer estimates for specialized weighted three-dimensional monomial sums using mixed zeta moments and stationary phase.

However the main corollary is tied to a special non-dyadic region and exponent/weight relations; the paper explicitly notes that the domain prevents deriving analogous dyadic-interval estimates by simply removing the weight. It is therefore not a direct closure theorem for the present Type-II box.

Classification:

`PLIEGO_2024_RELEVANT_NOT_DIRECT_DYADIC_CLOSURE`.

## 10. Next direct frontier

The next audit should not repeat a generic three-variable monomial estimate. It should test one of the following coefficient-sensitive routes:

1. **Möbius-preserving B-process audit** — determine whether the reciprocal `b^{-1/2}` phase can be transformed on a Vaughan Type-II factor without replacing the Möbius coefficient by an arbitrary bounded sequence.
2. **Second decomposition of the non-Möbius coefficient** — expand `b_d=sum_{c|d,c>V} mu(c)` before Cauchy and test whether the resulting 3/4-linear form gains enough spacing to remove the `K^(3/4)` deficit.
3. **Coefficient-sensitive double large sieve** — replace unsigned `B_1,B_2` counts by weighted energies carrying `mu(w)` or restricted Möbius structure; any claimed gain must be compared against random-sign and all-positive false controls.
4. **Ordered Type-II mean value** — keep the outer `n` average and the factorization simultaneously, and derive a bound that is weaker than uniform Chowla but stronger than arbitrary-coefficient spacing.

The immediate next calculation should start with route 2 because it remains algebraic and exact before importing any new conjectural cancellation.