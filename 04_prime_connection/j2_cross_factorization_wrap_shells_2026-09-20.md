# j=2 structured character moment: diagonal-free cross-factorization shells — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: exact four-factor character frontier, with the two-small-factor coefficient expanded again as \(k=rs\).
- New structural result: the two character-space product vectors correspond to incompatible integer factorization shapes
  \[
  bh
  \quad\text{and}\quad
  ers,
  \]
  and their exact integer diagonal \(bh=ers\) is empty in the sharp separated ranges.
- Therefore the generic Cauchy bound pays self-energy diagonals which are absent from the actual cross inner product.
- The cross correlation reduces to finitely many nonzero wrap shells
  \[
  bh-ers=mp,\qquad m\ne0,\quad |m|=O(1).
  \]
- Classification: J2_CROSS_FACTORIZATION_DIAGONAL_FREE_WRAP_SHELLS.

## 1. Sharp factor scales

Use the prime modulus normalization
\[
p\asymp H^3.
\]

The hard boundary has
\[
b\asymp p^{2/3},
\qquad
h\asymp p^{1/3},
\]
and
\[
e\asymp p^{1/2},
\qquad
r,s\asymp p^{1/4}.
\]

Thus both products have total scale p:
\[
bh\asymp p,
\qquad
ers\asymp p.
\]

The character moment is the correlation between these two multiplicative convolution shapes.

## 2. Exact equality is impossible

Assume
\[
bh=ers.
\]

The distinguished factor e is prime on the sharp Type-II component and satisfies
\[
e\asymp p^{1/2}.
\]

But
\[
h\asymp p^{1/3}<e,
\qquad
r,s\asymp p^{1/4}<e.
\]

Hence e cannot divide h, r, or s.

From
\[
e\mid bh
\]
it follows that
\[
e\mid b.
\]

Write
\[
b=e c.
\]

Then
\[
c\asymp p^{2/3-1/2}
=
p^{1/6}.
\]

The equality reduces to
\[
ch=rs.
\]

Now
\[
c\asymp p^{1/6},
\qquad
h\asymp p^{1/3},
\qquad
r,s\asymp p^{1/4}.
\]

Since r,s are the two prime factors in the sharp \(b_H(rs)=-1\) boundary, any prime divisor of c would have to equal r or s.

But
\[
c<r,s
\]
by a fixed power of p.

Thus no nontrivial prime divisor of c can divide rs.

Since
\[
c\asymp p^{1/6}>1,
\]
this is impossible.

Therefore
\[
\boxed{
bh=ers
\quad\text{has no solutions in the sharp separated support.}
}
\]

Permanent rule:
CROSS_FACTORIZATION_INTEGER_DIAGONAL_EMPTY.

## 3. Modular equality becomes finite wrap shells

Character orthogonality imposes
\[
bh\equiv ers\pmod p.
\]

Both integer products are contained in fixed dyadic multiples of p.

Therefore
\[
bh-ers=mp
\]
for one of only \(O(1)\) integers m.

The case
\[
m=0
\]
is impossible by the previous section.

Hence the entire cross correlation lies on
\[
\boxed{
bh-ers=mp,
\qquad
m\ne0,
\qquad
|m|=O(1).
}
\]

Classification:
J2_NONZERO_WRAP_SHELL_REDUCTION.

## 4. Why generic Cauchy loses H

The separate \(L^2\) norms
\[
\sum_\chi|B(\chi)H(\chi)|^2
\]
and
\[
\sum_\chi|E(\chi)R(\chi)S(\chi)|^2
\]
each contain their own positive diagonal product equalities.

Those diagonals force norms of order p and make Cauchy give a numerator of size
\[
p^2.
\]

But the actual cross product has no shared integer diagonal.

Thus the \(p^2\) bound is not geometrically sharp for the inner product.

The required numerator bound is
\[
p^{5/3+o(1)},
\]
a saving
\[
p^{-1/3}=H^{-1}
\]
from the generic Cauchy product.

This saving must come from **transversality between the two factorization shapes**, not from reducing either self-norm.

Permanent guard:
SEPARATE_GROUP_NORMS_CANNOT_SEE_CROSS_DIAGONAL_ABSENCE.

## 5. Exact shell equation

For fixed nonzero m,
\[
\boxed{
b h-e r s=m p.
}
\]

Given \(e,r,s,h\), the variable b is determined:
\[
b=\frac{ers+mp}{h}.
\]

The integrality condition is
\[
ers\equiv-mp\pmod h.
\]

Thus the shell may also be viewed as:
- moduli \(h\asymp p^{1/3}\);
- prime variable \(e\asymp p^{1/2}\);
- two prime factors \(r,s\asymp p^{1/4}\);
- residue
  \[
  e\equiv-mp\,\overline{rs}\pmod h;
  \]
- quotient \(b\asymp p^{2/3}\) carrying the inherited outer coefficient.

The modulus relative to the e-variable is
\[
h=e^{2/3},
\]
again the critical beyond-square-root AP scale previously seen in the project.

## 6. Unsigned count is not enough

There are schematically
\[
p^{1/2+1/4+1/4+1/3}
=
p^{4/3}
\]
quadruples \((e,r,s,h)\).

The divisibility condition by h has density
\[
p^{-1/3},
\]
so the unsigned shell naturally contains
\[
p^{1+o(1)}
\]
solutions.

But the centered target is only
\[
p^{2/3+o(1)}.
\]

Hence merely proving the expected unsigned density does not close the problem.

One still needs
\[
\boxed{p^{-1/3}}
\]
of signed/centered cancellation across the nonzero wrap shells.

## 7. New precise interpretation

The j=2 hard core can now be described without generic DLS language:

\[
\boxed{
\text{centered correlation between }
p^{2/3}\!\times p^{1/3}
\text{ and }
p^{1/2}\!\times p^{1/4}\!\times p^{1/4}
\text{ factorizations modulo }p,
}
\]
with the exact integer diagonal absent.

This is a more structured problem than arbitrary four-factor character moments.

It suggests that the next theorem should be a **cross-factorization dispersion estimate**, not another self-energy large sieve.

## 8. Next target

For every fixed nonzero bounded m, seek
\[
\sum_{\substack{
b\asymp p^{2/3},\ h\asymp p^{1/3}\\
e\asymp p^{1/2},\ r,s\asymp p^{1/4}\\
bh-ers=mp
}}
\alpha_b\eta_h\beta_e\rho_r\sigma_s
-
\mathfrak M_m
\ll
p^{2/3+o(1)}.
\]

A theorem of this form would supply exactly the missing \(H^{-1}\) variance saving for the two-factor boundary.

Permanent priority:
J2_CROSS_FACTORIZATION_WRAP_SHELL_DISPERSION.
