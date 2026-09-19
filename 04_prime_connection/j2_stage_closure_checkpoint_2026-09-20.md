# j=2 stage closure checkpoint — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- j=2 Vaughan-edge sector: NOT CLOSED.
- Current smallest exact frontier:
  \[
  bh-ers=mp,\qquad m\neq0,\qquad |m|=O(1),
  \]
  with
  \[
  b\asymp p^{2/3},\quad
  h\asymp p^{1/3},\quad
  e\asymp p^{1/2},\quad
  r,s\asymp p^{1/4}.
  \]
- Required centered cross-correlation scale:
  \[
  \boxed{p^{2/3+o(1)}}.
  \]

## 1. Results now considered stable

### 1.1 Sector stratification
The central j=2 arithmetic has been localized from generic Vaughan Type-II geometry to a two-small-factor boundary layer.

For
\[
b_H(k)=\sum_{\substack{d\mid k\\d\le H}}\mu(d),
\]
all squarefree H-smooth support with at least three small prime factors and \(b_H(k)\ne0\) admits a subset discrepancy at most \(1/5\), hence
\[
\boxed{H^{6+1/10+\varepsilon}}.
\]

The same \(H^{1/10}\) bound applies to the corresponding cumulative second-Type-I components whose complementary \(b_H\)-cofactor has at least three prime factors.

The unresolved sharp boundary is therefore concentrated on
\[
\boxed{
k=rs,\qquad r,s\le H,\qquad rs>H,\qquad b_H(rs)=-1.
}
\]

### 1.2 Exact Vaughan tail algebra
With
\[
b_H=\mu_{\le H}*1,
\]
one has
\[
A_1=\Lambda*b_H,\qquad
A_2=\Lambda_{\le H}*b_H,
\]
and the Vaughan Type-II contribution is the negative \(k>H\) tail of
\[
\Lambda_{>H}*b_H.
\]

Hence on the tail
\[
\boxed{
-A_{2,\mathrm{tail}}+T_{II}
=
-(\Lambda*b_H)_{\mathrm{tail}}
=
-A_{1,\mathrm{tail}}.
}
\]

This is exact algebra.

However:
\[
\boxed{
\text{pointwise cancellation}
\ne
\text{restricted-subfamily analytic bound}.
}
\]

### 1.3 Generic approaches closed
The following automatic mechanisms have been audited and are insufficient:

1. generic 3D Robert--Sargos regrouping of the two-factor core;
2. recursive fixed-depth Vaughan/Heath--Brown decompositions;
3. outer-prime third decomposition;
4. one-variable B-process at the outer H^2 self-dual scale;
5. generic hyper-Kloosterman completion followed by fixed-modulus Mellin diagonalization;
6. generic outer additive/multiplicative Fourier transfer;
7. one-factor incidence plus Cauchy;
8. packet-slope averaging without coefficient-sensitive input.

### 1.4 Hyper-Kloosterman route
Simultaneous completion of
\[
e_p(A\overline{mn})
\]
in two smooth variables gives
\[
\mathrm{Kl}_3(Ah_1h_2;p).
\]

The fixed-modulus four-factor Mellin calculation reaches the natural raw variance scale but leaves exactly one factor H above the centered target.

Thus hyper-Kloosterman completion is structurally legal in appropriate one-sided settings, but it does not by itself close j=2.

### 1.5 Bourgain--Garaev correction
At square-root lengths,
\[
N_1=N_2=p^{1/2},
\]
Bourgain--Garaev gives an explicit reciprocal-product saving
\[
p^{-1/16}.
\]

But the inverse-product congruence lives on the variance/dispersion side.

The branchwise amplitude deficit
\[
H^{1/8}
\]
corresponds to variance deficit
\[
H^{1/4}=p^{1/12}.
\]

Therefore a lossless BG insertion leaves
\[
\boxed{
p^{1/12-1/16}
=
p^{1/48}
=
H^{1/16}.
}
\]

The obsolete statement that BG had a spare \(p^{-1/48}\) margin is withdrawn.

Permanent guard:
\[
\boxed{
\text{DO NOT compare modular variance saving directly to amplitude deficit.}
}
\]

## 2. Exact coefficient-preserving determinant form

For the nonzero determinant shell,
\[
bek\equiv-h\pmod p,
\]
with
\[
p\asymp H^3,\quad
b\asymp H^2,\quad
e,k\asymp H^{3/2},\quad
|h|\lesssim H.
\]

Because all variables are nonzero modulo p,
\[
\boxed{
\bar b\,\bar e\,\bar k\equiv-\bar h\pmod p.
}
\]

This inversion should be performed **before** transforming the outer Möbius coefficient.

Multiplicative character orthogonality gives
\[
\boxed{
\mathcal A_p
=
\frac1{p-1}
\sum_{\chi\ne\chi_0}
B(\chi)E(\chi)K(\chi)\overline{H(\chi)}.
}
\]

The Dirichlet-polynomial lengths are
\[
\boxed{
p^{2/3},\quad
p^{1/2},\quad
p^{1/2},\quad
p^{1/3}.
}
\]

Generic self-energy pairing gives
\[
\mathcal A_p\ll p^{1+o(1)},
\]
while the required centered scale is
\[
p^{2/3+o(1)}.
\]

Hence the exact missing generic character saving is
\[
\boxed{p^{-1/3}=H^{-1}}.
\]

## 3. Cross-factorization diagonal is empty

Expand
\[
k=rs,
\qquad
r,s\asymp p^{1/4}.
\]

Then the two character-space product shapes are
\[
bh
\quad\text{and}\quad
ers.
\]

Their total scales are both p:
\[
p^{2/3}p^{1/3}=p,
\qquad
p^{1/2}p^{1/4}p^{1/4}=p.
\]

However the integer equality
\[
bh=ers
\]
has no solutions on the sharp separated support.

Indeed \(e\asymp p^{1/2}\) is prime and larger than \(h,r,s\), so \(e\mid b\). Writing \(b=ec\) gives
\[
c\asymp p^{1/6},
\qquad
ch=rs,
\]
which is impossible because \(r,s\asymp p^{1/4}>c\) are the two prime factors.

Therefore modular equality reduces to finitely many nonzero shells:
\[
\boxed{
bh-ers=mp,\qquad
m\neq0,\qquad |m|=O(1).
}
\]

This is the strongest current structural localization.

## 4. Interpretation of the remaining H-loss

Separate self-norms contain large positive diagonals.

The actual cross inner product does not.

Therefore the generic Cauchy loss is not expected to be sharp.

The missing factor
\[
H=p^{1/3}
\]
must come from the transversality between
\[
p^{2/3}\times p^{1/3}
\]
and
\[
p^{1/2}\times p^{1/4}\times p^{1/4}
\]
factorization shapes.

This is now called the
\[
\boxed{\text{cross-factorization wrap-shell dispersion problem}.}
\]

## 5. Exact current target

For each fixed bounded nonzero integer m, prove a centered estimate of the shape
\[
\boxed{
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
}
\]

Equivalent character target:
\[
\boxed{
\sum_{\chi\ne\chi_0}
B(\chi)E(\chi)R(\chi)S(\chi)\overline{H(\chi)}
\ll
p^{5/3+o(1)}.
}
\]

## 6. Literature status at closure checkpoint

Relevant accepted comparisons:

- Bourgain--Garaev: reciprocal-product bilinear/multilinear exponential sums;
- Korolev: Möbius-weighted reciprocal Kloosterman sums above square-root length;
- Banks--Shparlinski: interval/arbitrary-set multiplicative incidence;
- Petridis--Shparlinski: weighted trilinear finite-field exponential sums;
- Topacogullari and related work: shifted convolutions of generalized divisor functions with uniform power-saving errors.

No identified theorem has yet been verified to give the exact weighted prime-restricted wrap-shell target above as a black box.

## 7. Superseded statements

The following statements must not be restored as current claims:

- “BG reduces the H^(1/8) residual to H^(1/32).”
- “BG has an H^(-1/16) spare margin after paying the j=2 residual.”
- “pointwise Vaughan cancellation automatically removes the two-factor restricted subfamily.”
- “generic three-dimensional phase curvature alone closes the two-factor boundary.”
- “outer Möbius must be Fourier transformed before using reciprocal-product estimates.”

## 8. Next starting point

Do not restart from generic Type-II decomposition.

Resume from:
\[
\boxed{
bh-ers=mp,\qquad m\neq0,\quad |m|=O(1).
}
\]

The first next audit should compare this exact weighted shell with:
1. mixed \(d_2\)-\(d_3\) shifted-convolution asymptotics;
2. delta-method / Kuznetsov treatments with factor ranges fixed at
   \[
   p^{2/3},p^{1/3},p^{1/2},p^{1/4},p^{1/4};
   \]
3. a direct dispersion proof exploiting the absent integer diagonal.

This file is the canonical j=2 checkpoint for continuation after 2026-09-20.


# CANONICAL CORRECTION — 2026-09-20

The parts of this checkpoint that promote
\[
bh-ers=mP
\]
to the exact j=2 frontier are superseded.

The error arose from taking the legal Cauchy grouping
\[
|BH|\cdot|EK|
\]
and then treating it as if the original character moment were
\[
BH\,\overline{EK}.
\]
The original character orientations are instead
\[
B E K\overline H.
\]

Hence the exact orthogonality condition remains
\[
\boxed{b e k\equiv -h\pmod P},
\]
not \(bh\equiv ek\pmod P\).

With
\[
k=rs,
\]
the valid arithmetic frontier is
\[
\boxed{b e r s\equiv -h\pmod P},
\]
where
\[
b\asymp P^{2/3},\quad
e\asymp P^{1/2},\quad
r,s\asymp P^{1/4},\quad
h\asymp P^{1/3}.
\]

The valid character target is
\[
\boxed{
\sum_{\chi\ne\chi_0}
B(\chi)E(\chi)R(\chi)S(\chi)\overline{H(\chi)}
\ll P^{5/3+o(1)}.
}
\]

Generic Cauchy still gives a numerator of scale
\[
P^{2+o(1)},
\]
so the exact missing saving remains
\[
\boxed{P^{-1/3}=H^{-1}}.
\]

Withdrawn:
- bounded nonzero wrap-shell frontier;
- absent cross integer diagonal as a saving mechanism;
- shifted-divisor and determinant-theorem maps that relied on that artificial shell.

Still valid:
- two-small-factor support localization \(k=rs\);
- exact inverse congruence;
- structured four/five-factor character moment;
- generic H-deficit;
- all earlier Vaughan support, low-Type-I, H^(1/10), and H^(1/8) branchwise results.

New canonical starting point:
J2_STRUCTURED_FIVE_FACTOR_CHARACTER_MOMENT.

Permanent guard:
DO_NOT_APPLY_ORTHOGONALITY_AFTER_CHANGING_CONJUGATION_BY_CAUCHY.
