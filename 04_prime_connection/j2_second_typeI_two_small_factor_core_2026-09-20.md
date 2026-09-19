# j=2 cumulative second-Type-I coefficient and two-small-factor core — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: after proving an H^(1/10) bound for nonzero Type-II H-smooth cofactors with at least three prime factors.
- New exact identity on the squarefree unique-large-prime stratum:
  \[
  C_2(k)
  =
  \sum_{\ell\mid k,\ \ell\ {\rm prime}}
  (\log\ell)\,b_H(k/\ell).
  \]
- Consequence: every nonzero cumulative second-Type-I component is a distinguished small prime times the same restricted-Möbius support \(b_H\).
- If the complementary \(b_H\)-cofactor has at least three prime factors, the component inherits the H^(1/10) product-balance bound.
- The only coefficient pattern not covered by this improvement is a distinguished small prime whose complementary \(b_H\)-cofactor has exactly two prime factors.
- Classification: \`J2_SECOND_TYPEI_TWO_SMALL_FACTOR_CORE\`.

## 1. Structural stratum

Consider a squarefree integer in the H^3 working range of the form
\[
q=e\,k,
\]
where
\[
e>H
\]
is the unique H-rough prime factor and
\[
k
\]
is H-smooth.

On the central/high second-Type-I range,
\[
H<k<H^2.
\]

All prime factors of k are <=H.

The second Type-I coefficient on q is
\[
C_2(k)
=
\sum_{\substack{
b c r=k\\
b\le H,\ c\le H
}}
\mu(b)\Lambda(c).
\]

The large prime e is forced into the unrestricted 1-variable and does not affect this coefficient.

## 2. Exact distinguished-prime expansion

Because k is squarefree, the von Mangoldt variable c must be one of its prime factors.

Let
\[
c=\ell,\qquad \ell\mid k.
\]

The remaining sum is
\[
\sum_{\substack{
b\mid k/\ell\\
b\le H
}}
\mu(b).
\]

This is exactly
\[
b_H(k/\ell).
\]

Therefore
\[
\boxed{
C_2(k)
=
\sum_{\substack{
\ell\mid k\\
\ell\ {\rm prime}
}}
(\log\ell)\,
b_H(k/\ell).
}
\]

Classification:
\`SECOND_TYPEI_CUMULATIVE_BH_REPRESENTATION\`.

## 3. Immediate support consequence

A term indexed by \(\ell\) is nonzero only if
\[
b_H(k/\ell)\ne0.
\]

Thus after choosing the distinguished Lambda-prime \(\ell\), the rest of the small-factor geometry is exactly the already-audited restricted-Möbius support problem.

Let
\[
\ell\asymp H^\gamma
\]
and write
\[
k/\ell=\prod_{i=1}^r p_i,
\qquad
p_i\asymp H^{\lambda_i}.
\]

Set
\[
s_c:=\sum_i\lambda_i.
\]

The actual large unrestricted/rough variable e has exponent
\[
z=3-\gamma-s_c.
\]

Now define the **virtual large exponent**
\[
z':=z+\gamma=3-s_c.
\]

Collapsing the product
\[
e\ell
\]
into one coefficient is legal at the DLS moment level: it is a convolution of two prime/divisor-bounded coefficients and has diagonal L2 size up to H^epsilon.

Hence the actual branch
\[
\{z,\gamma,\lambda_1,\dots,\lambda_r\}
\]
may be product-balanced using the virtual branch
\[
\boxed{
\{z',\lambda_1,\dots,\lambda_r\}.
}
\]

Any subset using z' is realized in the actual variables by taking both z and gamma.

## 4. Complementary cofactor with >=3 prime factors

Suppose
\[
r\ge3
\]
and
\[
b_H(k/\ell)\ne0.
\]

The previous support theorem
\`J2_TYPEII_GE3_FACTOR_H1_10\`
gives a subset of
\[
\{z',\lambda_1,\dots,\lambda_r\}
\]
whose H-exponent lies within 1/5 of 2.

Therefore the actual second-Type-I component has the same subset discrepancy:
\[
\boxed{\Delta_H\le1/5.}
\]

Including the outer H^2 factor and the opposite H^3 variable, standard DLS gives
\[
\boxed{
T_{I,2,\ r\ge3}
\ll_\varepsilon
H^{6+1/10+\varepsilon}.
}
\]

Thus the >=3-factor cumulative second-Type-I support is no longer part of the H^(1/8) sharp core.

Classification:
\`SECOND_TYPEI_GE3_COMPLEMENT_H1_10\`.

## 5. One-factor complement cannot occur in the high range

If
\[
k/\ell=p
\]
is a single prime <=H, then
\[
b_H(p)=1-1=0.
\]

Hence such a term vanishes.

The first possible nonzero complementary support has two prime factors.

## 6. Exactly-two-factor complement

Let
\[
k/\ell=rs,
\qquad
r,s\le H,
\qquad
rs>H.
\]

Then
\[
b_H(rs)=1-1-1=-1.
\]

The corresponding coefficient term is
\[
-(\log\ell).
\]

Its factor geometry is
\[
\{z,\gamma,\lambda_r,\lambda_s\},
\]
with
\[
z+\gamma=3-(\lambda_r+\lambda_s).
\]

Equivalently the virtual branch is
\[
\left\{
3-(\lambda_r+\lambda_s),
\lambda_r,\lambda_s
\right\}.
\]

This is exactly the old two-small-factor sharp geometry.

At
\[
\lambda_r=\lambda_s=3/4
\]
the virtual large exponent is 3/2 and the nearest branch subset to exponent 2 is still at distance 1/4.

A very small distinguished prime \(\ell\) does not remove this: z and gamma simply recombine to the same virtual 3/2 exponent.

Therefore this class remains genuinely unresolved by product regrouping.

Classification:
\`SECOND_TYPEI_TWO_FACTOR_COMPLEMENT_SHARP_CORE\`.

## 7. Unified residual picture

After cumulative coefficient recombination:

### Type-II
- nonzero H-smooth cofactor with >=3 factors:
  \[
  H^{6+1/10+\varepsilon};
  \]
- exactly-two-small-factor cofactor:
  cancellation-sensitive sharp core.

### Second Type-I
- distinguished Lambda-prime + nonzero b_H complement with >=3 factors:
  \[
  H^{6+1/10+\varepsilon};
  \]
- distinguished prime + exactly-two-factor b_H complement:
  the same sharp virtual geometry.

Thus the difficult j=2 central arithmetic is no longer a generic central/high multilinear family.

It is localized to the repeated pattern
\[
\boxed{
b_H(rs)=-1,
\qquad
r,s\le H,\quad rs>H.
}
\]

The remaining task is to preserve the signed relation between the Type-I and Type-II occurrences of this two-small-factor kernel.

Permanent priority:
\`J2_TWO_SMALL_FACTOR_SIGNED_CORE\`.
