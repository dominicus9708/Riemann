# j=2 signed-tail smooth-cofactor self-dual barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: after proving that sharp Vaughan cutoffs may be smoothed at balanced cost and that a product-kernel signed Gram estimate collapses back to the prime operator.
- Candidate tested: use the smooth signed tail
  \[
  \Lambda_{>H}*\mu_W*1
  \]
  and apply a B-process in its unrestricted cofactor before product collapse.
- Result: every such smooth cofactor has length at most the reciprocal B-process self-dual scale H^2.
- Consequence: the signed-tail+B-process route does not create an automatic shorter dual variable; its generic scale geometry is self-dual or worse.
- Classification: \`J2_SIGNED_TAIL_SMOOTH_COFACTOR_SELFDUAL_BARRIER\`.

## 1. Tail factorization

After smoothing the Möbius cutoff, write a dyadic factorization
\[
q=e d r\asymp H^3,
\]
where
\[
d\asymp H^\alpha,
\qquad
0\le\alpha\le1,
\]
\[
e\asymp H^\beta,
\qquad
\beta\ge1,
\]
and
\[
r\asymp H^\gamma.
\]

The product constraint gives
\[
\boxed{
\alpha+\beta+\gamma=3.
}
\]

Therefore
\[
\gamma
=
3-\alpha-\beta
\le
2-\alpha
\le2.
\]

Hence
\[
\boxed{
R:=H^\gamma\le H^2.
}
\]

## 2. Reciprocal B-process scale

The sharp j=2 reciprocal phase has normalized amplitude
\[
X=H^4.
\]

For a reciprocal-square-root monomial in a variable of length R,
\[
f(r)=C r^{-1/2},
\]
the B-process dual length is
\[
R^*\asymp\frac XR.
\]

Thus
\[
RR^*\asymp X=H^4,
\]
and the self-dual length is
\[
\boxed{
R_{\rm sd}=H^2.
}
\]

Since every signed-tail smooth cofactor satisfies
\[
R\le H^2,
\]
we obtain
\[
\boxed{
R^*\ge H^2\ge R.
}
\]

A B-process in r never shortens the variable by a polynomial factor.

## 3. Boundary case

Equality
\[
R=H^2
\]
requires
\[
\gamma=2,
\]
hence
\[
\alpha=0,\qquad\beta=1.
\]

This is the limiting configuration
\[
d\asymp1,
\qquad
e\asymp H,
\qquad
r\asymp H^2.
\]

It lies exactly at B-process self-duality.

For every interior tail configuration with
\[
\alpha>0
\quad\text{or}\quad
\beta>1,
\]
one has
\[
R<H^2
\]
and the B-process lengthens the cofactor.

Classification:
\`SIGNED_TAIL_BPROCESS_ONLY_SELFDUAL_AT_BOUNDARY\`.

## 4. Stationary amplitude

On an r-block of length \(R=H^\gamma\),
\[
|f''(r)|
\asymp
\frac{H^4}{R^2}.
\]

Hence the stationary amplitude is
\[
|f''|^{-1/2}
\asymp
\frac R{H^2}
=
H^{\gamma-2}
\le1.
\]

The dual frequency count is
\[
R^*
=
\frac{H^4}{R}
=
H^{4-\gamma}.
\]

Thus the product
\[
(\text{stationary amplitude})\times(\text{dual length})
\asymp
H^{\gamma-2}H^{4-\gamma}
=
H^2
\]
is invariant.

There is no free polynomial saving from the transform.

## 5. Why this differs from the closed low-Type-I block

The earlier low-Type-I closure applied B-process to the **combined unrestricted variable**
\[
n\asymp H^{3-\theta},
\qquad
0\le\theta\le1,
\]
so
\[
n\ge H^2.
\]

That variable was the full cofactor before resolving
\[
L=\Lambda*1.
\]

After exact signed Vaughan recombination is rewritten as
\[
\Lambda_{>H}*\mu_{\le H}*1,
\]
the same cofactor is split into
\[
e r,
\qquad
e>H.
\]

This forces the remaining genuinely smooth factor r down to
\[
r\le H^2.
\]

Hence:
\[
\boxed{
\text{the long smooth B-process resource and the exact signed tail structure cannot both be exposed for free.}
}
\]

## 6. Consequence for the proposed signed Gram route

The route
\[
\text{smooth cutoff}
\to
\text{signed tail}
\to
\text{B-process in the smooth factor}
\to
\text{factor-sensitive signed Gram}
\]
does not by itself escape the self-dual fixed point.

To obtain new power saving one would need an ingredient beyond a one-variable B-process, for example:
- simultaneous transformation in more than one factor;
- a genuinely coefficient-sensitive multilinear spacing estimate;
- an outer-average mean square which supplies extra orthogonality;
- a transformation applied before splitting \(L=\Lambda*1\).

Classification:
\`SIGNED_TAIL_ONE_VARIABLE_BPROCESS_ROUTE_NOT_AUTOMATIC_ESCAPE\`.

## 7. Updated route comparison

Three facts now coexist:

1. **Before** splitting the logarithmic cofactor, low-Type-I has a long smooth variable and is closed by B-process+DLS.
2. **After** exact signed recombination, the smooth tail cofactor is at most self-dual.
3. Keeping only product-level signs collapses back to the original prime operator.

Therefore the remaining useful direction is not further manipulation of the signed tail in isolation.

The next candidates are:
\[
\boxed{
\text{outer-average / packetized prime reciprocal phase}
}
\]
or a genuinely multilinear transformation that changes the self-dual geometry.

Permanent priority:
\`RETURN_TO_PRIME_RECIPROCAL_OUTER_AVERAGE_AFTER_SIGNED_TAIL_BARRIER\`.
