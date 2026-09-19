# j=2 double-refined-branch subset lemma and H^(1/8) frontier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: apply Vaughan/Heath--Brown structure to both H^3 prime variables after the strengthened low-Type-I closure.
- Every branch pair with a low-Type-I smooth cofactor on either side is already CLOSED at H^(6+epsilon).
- New result: if both surviving branches are central/high refined branches, their combined factor support always admits a two-product partition with H-exponent discrepancy at most 1/4.
- This gives a branchwise standard-DLS loss at most H^(1/8).
- The bound 1/4 is sharp for the factor-scale class.
- Classification: \`J2_DOUBLE_REFINED_BRANCH_H1_8_FRONTIER\`.

## 1. Abstract refined H^3 branch

A surviving central/high H^3 branch has the following factor-scale form:
\[
\boxed{
\mathcal B
=
\{z;\lambda_1,\ldots,\lambda_r\},
}
\]
where
\[
1\le z\le2,
\qquad
0<\lambda_j\le1,
\]
and
\[
\boxed{
z+\sum_j\lambda_j=3.
}
\]

Interpretation:
- high second-Type-I:
  \[
  z=3-(\beta+\gamma),
  \qquad
  \lambda_1=\beta,\quad\lambda_2=\gamma;
  \]
- support-aware Type-II:
  z is the large von-Mangoldt factor exponent and the \(\lambda_j\) are the H-smooth prime-factor exponents of the nonzero composite cofactor.

Prime-power / rough-prime exceptional pieces were already separated in the earlier support audit.

Let
\[
s:=\sum_j\lambda_j=3-z.
\]
Then
\[
1\le s\le2.
\]

## 2. Two-branch subset lemma

Take two refined branches
\[
\mathcal B_1,\qquad \mathcal B_2.
\]

Claim: among all atomic factors from the two branches there exists a subset with H-exponent t satisfying
\[
\boxed{
|t-2|\le\frac14.
}
\]

### Case 1: one branch already works by itself

For a branch, both
\[
z
\quad\text{and}\quad
s=3-z
\]
are legal subset sums.

If either belongs to
\[
[7/4,9/4],
\]
then the claim is immediate.

Since z,s<=2, the only hard case is therefore
\[
\boxed{
5/4<z<7/4,
\qquad
5/4<s<7/4
}
\]
for both branches.

### Case 2: a small atom is at least 3/4

Suppose branch 1 has
\[
\lambda\in[3/4,1].
\]

Take:
- the distinguished z-factor;
- every small factor except this lambda.

The subset exponent is
\[
z+(s-\lambda)
=
3-\lambda.
\]

Hence
\[
2\le3-\lambda\le9/4.
\]

So again
\[
|t-2|\le1/4.
\]

Thus in the remaining hard case **every small atom in both branches is <3/4**.

### Case 3: all small atoms are <3/4

Use branch 2.

Its small-factor total satisfies
\[
s_2>5/4.
\]

There exists a small-factor subset with exponent
\[
\boxed{
u\in[1/4,3/4].
}
\]

Proof:
- if some atom is at least 1/4, take that atom; it is <3/4;
- if every atom is <1/4, add atoms until the partial sum first reaches 1/4; the resulting sum is <1/2.

Now return to branch 1 and write
\[
s_1=3-z_1.
\]

To make \(s_1+u\) lie in [7/4,9/4], u must lie in
\[
I_s
=
[7/4-s_1,\ 9/4-s_1].
\]

To make \(z_1+u\) lie in the same interval, u must lie in
\[
I_z
=
[7/4-z_1,\ 9/4-z_1].
\]

Since
\[
z_1=3-s_1,
\]
we have
\[
I_z
=
[s_1-5/4,\ s_1-3/4].
\]

For
\[
5/4\le s_1\le7/4,
\]
the two intervals overlap and their union contains
\[
\boxed{[1/4,3/4].}
\]

Therefore the u found above belongs to at least one of \(I_s,I_z\).

Hence either
\[
s_1+u
\]
or
\[
z_1+u
\]
lies in
\[
[7/4,9/4].
\]

This proves the claim.

Classification:
\`TWO_REFINED_H3_BRANCHES_HAVE_QUARTER_BALANCE\`.

## 3. Include the outer d-factor

The original sharp j=2 sector has the outer factor
\[
d_0\asymp H^2.
\]

Adding its exponent 2 to the subset t from the lemma gives a product group of exponent
\[
2+t.
\]

Therefore
\[
\boxed{
\left|(2+t)-4\right|
\le
\frac14.
}
\]

Since the full exponent total is 8, the complementary group has the opposite discrepancy.

Thus the common two-product balance functional satisfies
\[
\boxed{
\Delta_H\le\frac14.
}
\]

## 4. Standard DLS consequence

After canonical divisor selection and dyadic localization, the selected subset may be collapsed into one product coefficient and the complement into the other.

All multiplicities are divisor-bounded and hence have diagonal L2 moments up to H^epsilon.

The standard two-product DLS bound therefore gives
\[
\boxed{
T_{\rm refined\times refined}
\ll_\varepsilon
H^{6+1/8+\varepsilon}.
}
\]

This improves the support-aware one-sided H^(1/6) residual.

In V-units,
\[
H=V^{1/2},
\]
so
\[
H^{1/8}=V^{1/16}.
\]

Classification:
\`J2_DOUBLE_REFINED_BRANCH_DLS_H1_8\`.

## 5. Sharp factor-scale configuration

Take each branch to have exponents
\[
\boxed{
\left\{
\frac32,\frac34,\frac34
\right\}.
}
\]

For the union of two such branches, the available subset sums nearest 2 are
\[
\frac32
\quad\text{and}\quad
\frac34+\frac34+\frac34
=
\frac94.
\]

There is no subset sum in
\[
(7/4,9/4).
\]

Hence
\[
\boxed{
\min|t-2|=\frac14.
}
\]

Thus the quarter-balance lemma is sharp for the abstract factor-scale class.

Consequently the DLS loss
\[
\boxed{H^{1/8}}
\]
cannot be improved uniformly by two-product regrouping alone within this class.

Permanent rule:
\`DOUBLE_REFINED_H1_8_PARTITION_BARRIER_SHARP\`.

## 6. Interaction with low-Type-I closure

The strengthened low-Type-I theorem says:

if **either** H^3 variable exposes a smooth cofactor of length at least H^2, then the entire mixed branch is already
\[
H^{6+\varepsilon}.
\]

Therefore, after decomposing both prime variables, the branch map becomes:

1. low-Type-I on either side:
   \[
   \boxed{H^{6+\varepsilon}\ \text{CLOSED}};
   \]

2. both sides central/high refined:
   \[
   \boxed{H^{6+1/8+\varepsilon}};
   \]

3. exceptional rough-prime / prime-power pieces:
   handled by the earlier inter-branch cancellation and sparsity audits.

Thus the current **branchwise double-decomposition frontier** is
\[
\boxed{H^{1/8}}.
\]

## 7. Important audit warning

The sharp H^(1/8) factor configuration may again live on composite Vaughan atoms which cancel after complete cross-scale recombination.

Therefore:
\[
\boxed{
H^{1/8}
}
\]
is an upper-bound deficit for the current double-refined branch architecture, not a lower bound for the true j=2 sum.

The same permanent rule remains active:
\[
\texttt{FACTOR_SCALE_SHARPNESS_NE_FULL_VAUGHAN_SHARPNESS}.
\]

## 8. Updated next target

The new question is substantially smaller:

\[
\boxed{
\text{Can one recover only }H^{-1/8}
\text{ beyond standard DLS on the double-refined central branch?}
}
\]

Potential resources:
- signed cross-scale recombination between the two prime decompositions;
- a second-generation B/A-process on the H^(3/2) distinguished factors;
- a genuinely multilinear spacing theorem using both refined branches simultaneously.

This replaces the older H^(1/2), H^(1/4), and H^(1/6) branchwise deficits as the smallest current double-decomposition frontier.
