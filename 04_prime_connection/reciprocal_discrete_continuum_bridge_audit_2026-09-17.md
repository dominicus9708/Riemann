# Reciprocal discrete–continuum bridge audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Continuous reciprocal kernel endpoint identity: EXACT.
- Discrete outer-`n` kernel to continuous kernel: uniform Euler-summation bridge derived.
- Hard near-cell `h=O(H)`: aggregate discretization error is harmless whenever `H<=Q`.
- For the symmetric scale `K~D`, this covers `Q >= D^(1/3)`.
- Remaining low-`Q` corner `Q<D^(1/3)`: still OPEN and must not be hidden by the continuum approximation.

## 1. Exact discrete kernel
For `d~D`, shift `h>=1`, and outer dyadic block `Q<n<=2Q`, define

\[
\mathcal K_{Q,K}(d,h)
:=\sum_{Q<n\le2Q}
 e\!\left(2K\sqrt n\,\Delta_d(h)\right),
\]

where

\[
\Delta_d(h)=d^{-1/2}-(d+h)^{-1/2}.
\]

Put the exact dimensionless frequency

\[
\boxed{
\lambda_{d,h}:=2K\sqrt Q\,\Delta_d(h).
}
\]

Then

\[
\mathcal K_{Q,K}(d,h)
=\sum_{Q<n\le2Q}
 e\!\left(\lambda_{d,h}\sqrt{n/Q}\right).
\]

No Taylor expansion in `h/d` has been used in this definition.

## 2. Euler summation
Let

\[
f_\lambda(t)=e(\lambda\sqrt t),\qquad 1\le t\le2.
\]

A standard first-order Euler/summation estimate gives

\[
\sum_{Q<n\le2Q} f_\lambda(n/Q)
=Q\int_1^2f_\lambda(t)\,dt
+O\!\left(\|f_\lambda\|_\infty+
\int_1^2|f_\lambda'(t)|\,dt\right).
\]

Since

\[
|f_\lambda'(t)|
=\pi|\lambda|t^{-1/2},
\]

we obtain uniformly in real `lambda`

\[
\boxed{
\mathcal K_{Q,K}(d,h)
=QF(\lambda_{d,h})+O(1+|\lambda_{d,h}|),
}
\]

where

\[
F(\lambda)=\int_1^2e(\lambda\sqrt t)\,dt.
\]

This is an exact discrete-to-continuum reduction up to the displayed deterministic error.

## 3. Near-cell frequency is bounded
Recall

\[
H=\frac{D^{3/2}}{K\sqrt Q}.
\]

For `d~D`, the exact difference satisfies

\[
\Delta_d(h)
=\frac{h}{\sqrt d\sqrt{d+h}(\sqrt d+\sqrt{d+h})}
\ll \frac{h}{D^{3/2}}.
\]

Hence

\[
|\lambda_{d,h}|
\ll \frac hH.
\]

Therefore, throughout any fixed hard cell

\[
1\le h\le cH,
\]

one has

\[
\boxed{
\mathcal K_{Q,K}(d,h)
=QF(\lambda_{d,h})+O_c(1).
}
\]

So the discrete outer kernel differs from its continuous endpoint kernel by only constant size per pair in the genuinely unresolved cell.

## 4. Aggregate weighted discretization error
The off-diagonal reciprocal mean square carries the weight

\[
[d(d+h)]^{-1/4}\asymp D^{-1/2}.
\]

There are `O(DH)` pairs `(d,h)` with `d~D` and `h<=cH`. Taking the `O_c(1)` Euler error absolutely therefore gives

\[
E_{\rm disc,near}
\ll_c D^{-1/2}\cdot DH
=H D^{1/2}.
\]

The desired dyadic mean-square target is

\[
Q D^{1/2+\varepsilon}.
\]

Thus the relative discretization cost is

\[
\boxed{
\frac{E_{\rm disc,near}}{QD^{1/2}}
\ll_c \frac HQ.
}
\]

Consequently, in the parameter region

\[
\boxed{H\le Q,}
\]

the continuous reciprocal kernel can be substituted into the hard near-cell without introducing a power-scale loss, even if the Euler error is summed absolutely.

Classification:

`RECIPROCAL_NEAR_CELL_DISCRETE_CONTINUUM_BRIDGE`.

## 5. Symmetric scale threshold
At the symmetric scale `K~D`,

\[
H\asymp\sqrt{\frac DQ}.
\]

Then `H<=Q` is equivalent, up to fixed constants, to

\[
\sqrt{D/Q}\le Q,
\]

hence

\[
\boxed{Q\ge D^{1/3}.}
\]

Therefore the unresolved block separates naturally into two sectors:

### Sector A — continuum-transfer sector
\[
Q\ge D^{1/3}.
\]

Here the hard near-cell may be analyzed through the continuous endpoint/spectral-primitive kernel with aggregate discretization error below the target scale.

### Sector B — low-outer-resolution corner
\[
Q<D^{1/3}.
\]

Here `H>Q`, so the naive absolute accumulation of the `O(1)` Euler errors is too expensive. A proof must retain cancellation in the discretization remainder, use a sharper discrete transform, or treat this corner by a different arithmetic argument.

Classification:

`LOW_Q_DISCRETE_CORNER_OPEN`.

## 6. Exact endpoint kernel retained in Sector A
For nonzero `lambda`,

\[
F(\lambda)
=
\frac{\sqrt2\,e(\sqrt2\lambda)-e(\lambda)}{\pi i\lambda}
+
\frac{e(\sqrt2\lambda)-e(\lambda)}{2\pi^2\lambda^2},
\]

with `F(0)=1` by continuity.

Thus Sector A inherits the endpoint-difference structure exactly at the continuum level. The remaining complication is not the outer `n` discretization but the fact that

\[
\lambda_{d,h}
=2K\sqrt Q\,[d^{-1/2}-(d+h)^{-1/2}]
\]

depends nonlinearly on both `d` and `h`.

The local linearization

\[
\lambda_{d,h}
=\frac hH x^{-3/2}
+O\!\left(\frac{h^2}{HD}\right),
\qquad d=Dx,
\]

is uniform for `h=O(H)`. Since `H<=D^(1/2)`, its error is `O(H/D)=O(D^(-1/2))` at the top of the near cell.

This supports a short-`d` block treatment in which the dilation frequencies are frozen only after a quantitative error audit.

## 7. Next live split
The previous global problem is now sharpened into two independent tasks.

1. **Sector A (`Q>=D^(1/3)`)**: restore the slowly varying `d/D` dependence in the spectral-primitive boundary identity and prove that a smooth short-`d` partition preserves cross-scale compensation.
2. **Sector B (`Q<D^(1/3)`)**: search for a genuinely discrete mechanism. The continuum replacement is not automatically cheap here, and the earlier outer B-process audit already showed that the near cell has no free oscillatory gain.

Permanent guard:

`CONTINUUM_TRANSFER_RANGE_GUARD` — do not use the continuous spectral-primitive identity over the entire unresolved parameter range without separately controlling the low-`Q` corner.
