# Vaughan-edge double-Möbius product-collapse audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Context: the worst unbalanced low-outer-index Type-II block, with the short Vaughan factor at its natural lower edge.
- New exact simplification: on `V<d<=2V`, the restricted Vaughan coefficient is exactly `b_d=mu(d)`.
- Consequence: the edge block carries two Möbius factors, but their product does not create independent factorization-sign cancellation because the phase depends only on the product.

## 1. Exact edge identity for the Vaughan coefficient
Recall

\[
b_d=\sum_{\substack{c\mid d\\c>V}}\mu(c).
\]

If

\[
V<d\le2V,
\]

then every proper divisor `c<d` satisfies

\[
c\le d/2\le V.
\]

Hence the only divisor of `d` exceeding `V` is `c=d`, and therefore

\[
\boxed{b_d=\mu(d)\qquad(V<d\le2V).}
\]

At the extreme `D=K`, outer index `n~1`, the natural symmetric Vaughan threshold is

\[
H\asymp K^{1/2},\qquad U=V\asymp K^{1/4}.
\]

Thus the shortest Type-II factor block `d~K^(1/4)` lies precisely in this double-Möbius edge geometry.

## 2. Edge Type-II sum
The block becomes schematically

\[
T_{\rm edge}
=\sum_{d\asymp V}\mu(d)
\sum_{w\asymp L}\mu(w)
 e\!\left(A(dw)^{-1/2}\right),
\]

with `VL~D`.

Since

\[
(dw)^{-1/2}
\]

depends only on the product `r=dw`, regrouping is exact:

\[
T_{\rm edge}
=\sum_r \Gamma_{V,L}(r)e(Ar^{-1/2}),
\]

where

\[
\Gamma_{V,L}(r)
=\sum_{\substack{dw=r\\d\asymp V,\ w\asymp L}}
\mu(d)\mu(w).
\]

## 3. Coprime/squarefree product sector
If `r` is squarefree, every factorization `r=dw` has `(d,w)=1`, and

\[
\mu(d)\mu(w)=\mu(r).
\]

Therefore

\[
\boxed{
\Gamma_{V,L}(r)
=\mu(r)\nu_{V,L}(r)
\qquad(r\text{ squarefree}),
}
\]

where `nu_{V,L}(r)>=0` is the number of allowed divisors in the short factor range.

Thus **all admissible factorizations of a fixed squarefree product carry the same sign**. There is no internal Möbius cancellation across factorization coordinates.

Classification:

`DOUBLE_MOBIUS_FACTORIZATION_SIGN_COHERENCE`.

## 4. Shared-prime correction
If `(d,w)=g>1` while both `d,w` are squarefree, write

\[
d=ga,\qquad w=gb,
\]

with `g,a,b` squarefree and pairwise coprime in the natural decomposition. Then

\[
r=g^2ab,
\]

and

\[
\mu(d)\mu(w)=\mu(g)^2\mu(a)\mu(b)=\mu(ab).
\]

Hence the non-squarefree product contribution is an explicit square-overlap sector, not an independent random-sign sector. It can be organized by the common square factor `g^2`.

## 5. Full-convolution comparison
Without dyadic restrictions, the coefficient convolution is

\[
(\mu*\mu)(n),
\]

whose Dirichlet series is

\[
\sum_{n\ge1}\frac{(\mu*\mu)(n)}{n^s}
=\frac1{\zeta(s)^2}.
\]

Thus doubling the Möbius factors does not spectrally desensitize the problem; the unrestricted comparison has a **squared reciprocal-zeta obstruction**.

The restricted edge convolution is not equal to the full convolution, but this comparison is a guard against treating the mere presence of two Möbius factors as an automatic source of additional cancellation.

## 6. Consequence for the live route
The candidate

`two Möbius factors -> independent sign cancellation in Type II -> close far resonance`

is false at the factorization level in the critical edge block.

A successful coefficient-sensitive estimate would have to use something beyond product-factor sign independence, for example:

1. reciprocal-phase curvature before exact product regrouping;
2. an average over outer Voronoi indices;
3. a weighted estimate for the one-variable restricted convolution `Gamma_{V,L}(r)`;
4. cancellation involving the square-overlap sectors.

Because the phase itself factors exactly through `r=dw`, any claimed bilinear gain that survives exact regrouping must be identifiable in the product coefficient `Gamma_{V,L}` rather than attributed to fictitious independent phase dimensions.

Permanent guards:
- `VAUGHAN_EDGE_BD_EQUALS_MU`.
- `DOUBLE_MOBIUS_FACTORIZATION_SIGN_COHERENCE`.
- `RESTRICTED_MU_CONVOLUTION_PRODUCT_COLLAPSE`.
