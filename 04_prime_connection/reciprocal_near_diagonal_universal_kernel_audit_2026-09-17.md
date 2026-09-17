# Reciprocal near-diagonal universal-kernel audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Standard Vaughan coefficient-removal route: closed as an independent RH-scale mechanism.
- Original reciprocal-phase outer mean square: restored as the primary object.
- Near-diagonal resolution cell: admits a scale-free limiting kernel.
- Absolute averaged-Chowla input currently available in the literature: insufficient at the required polynomial resolution scale.

## 1. Dyadic reciprocal block
Write

\[
V_{n,D}
=
\sum_{d\asymp D}
\mu(d)d^{-1/4}
 e\!\left(2K\sqrt n\,d^{-1/2}\right),
\]

and for an outer dyadic block `n~Q` define

\[
\mathcal M(Q,D)
=
\sum_{n\asymp Q}|V_{n,D}|^2.
\]

The diagonal contribution is

\[
\mathcal M_{\rm diag}
\asymp
Q\sum_{d\asymp D}\mu(d)^2d^{-1/2}
\asymp QD^{1/2}
\]

up to the squarefree density and harmless logarithmic/constant factors.

Thus the desired RH-scale block estimate

\[
\boxed{
\mathcal M(Q,D)\ll_\varepsilon QD^{1/2+\varepsilon}
}
\]

is exactly diagonal scale.

## 2. Exact shift kernel
For a positive shift `h`,

\[
\Delta_d(h)
:=d^{-1/2}-(d+h)^{-1/2}
=
\frac{h}{\sqrt d\sqrt{d+h}(\sqrt d+\sqrt{d+h})}.
\]

The outer kernel is

\[
\mathcal K_{Q,K}(d,h)
:=
\sum_{n\asymp Q}
 e\!\left(2K\sqrt n\,\Delta_d(h)\right).
\]

The mean square expands as diagonal plus

\[
2\operatorname{Re}
\sum_{h\ge1}
\sum_{d\asymp D}
\mu(d)\mu(d+h)
[d(d+h)]^{-1/4}
\mathcal K_{Q,K}(d,h),
\]

with the obvious support restriction `d+h` in the dyadic block.

## 3. Resolution length
Define

\[
\boxed{
H:=\frac{D^{3/2}}{K\sqrt Q}.
}
\]

For `d~D`, the phase difference has size

\[
2K\sqrt Q\,\Delta_d(h)\asymp \frac hH.
\]

Thus `h~H` is precisely the first separation scale of adjacent reciprocal frequencies on the outer `n`-block.

## 4. Universal near-diagonal scaling
Put

\[
d=Dx,\qquad h=Hy,\qquad n=Qt,
\]

where `x,t` stay in fixed dyadic compact intervals and `y=O(1)`.

Using

\[
(1+u)^{-1/2}
=1-\frac12u+\frac38u^2+O(u^3),
\]

we obtain

\[
\begin{aligned}
2K\sqrt n\,[d^{-1/2}-(d+h)^{-1/2}]
&=K\sqrt n\,h d^{-3/2}
+O(K\sqrt n\,h^2d^{-5/2})\\
&=\sqrt t\,y x^{-3/2}
+O\!\left(\frac HD\right).
\end{aligned}
\]

The identity `K sqrt(Q) H=D^{3/2}` was used in the last line.

In the current unresolved range `H<=D^{1/2}`,

\[
\frac HD\le D^{-1/2}.
\]

Therefore the dangerous near-diagonal phase converges to the scale-free kernel

\[
\boxed{
\Phi_0(x,y,t)=\sqrt t\,y x^{-3/2}.
}
\]

Likewise

\[
[d(d+h)]^{-1/4}
=D^{-1/2}x^{-1/2}
\left(1+O(H/D)\right).
\]

Classification:

`RECIPROCAL_NEAR_DIAGONAL_UNIVERSAL_KERNEL`.

## 5. Consequence: no automatic asymptotic oscillation inside one resolution cell
The leading normalized phase `Phi_0` contains no growing power of `D`.

Hence increasing the global scale does **not** create an increasing number of deterministic phase oscillations inside `h=O(H)`.

Any proof that treats this near-diagonal resolution cell in isolation therefore cannot expect a growing power saving from smooth phase oscillation alone.

The required improvement must come from at least one of:

1. arithmetic cancellation of the Möbius products `mu(d)mu(d+h)`;
2. cancellation between the near-diagonal cell and more distant shift ranges;
3. a transformation that reorganizes the full kernel before taking absolute values.

Permanent guard:

`RESOLUTION_CELL_NO_FREE_OSCILLATION_GUARD`.

## 6. Required near-cell arithmetic scale
For `h<=cH`, the normalized outer kernel is of size at most constant order times `Q`. In leading variables define

\[
\mathscr K_Q(x,y)
:=\frac1Q
\sum_{n\asymp Q}
 e\!\left(\sqrt{n/Q}\,y x^{-3/2}\right).
\]

Then the near-cell contribution has the schematic scale

\[
QD^{-1/2}
\sum_{h\lesssim H}
\sum_{d\asymp D}
\mu(d)\mu(d+h)
\mathscr K_Q(d/D,h/H).
\]

To place this part **individually** at the diagonal target `QD^{1/2+epsilon}`, a sufficient weighted condition is

\[
\boxed{
\sum_{h\lesssim H}
\sum_{d\asymp D}
\mu(d)\mu(d+h)
\mathscr K_Q(d/D,h/H)
\ll_\varepsilon D^{1+\varepsilon}.
}
\]

There are `~DH` raw pairs, so this corresponds to an average cancellation factor about `H` relative to absolute counting.

For random signs, a total fluctuation of order `sqrt(DH)` is already below `D` because `H<=D`; hence the required signed scale is compatible with the random model. The difficulty is proving it deterministically for Möbius with this structured kernel.

## 7. Comparison with averaged Chowla results
Matomäki–Radziwiłł–Tao and refinements prove strong forms of averaged Chowla cancellation, schematically of the type

\[
\sum_{h\le H}
\left|
\sum_{d\le D}\mu(d)\mu(d+h)
\right|
=o(DH)
\]

when `H->infinity`, with quantitative logarithmic savings in several regimes and later refinements.

If one discards the phase kernel and takes absolute values shift by shift, the present near-cell target would instead require roughly

\[
\sum_{h\le H}
\left|
\sum_{d\asymp D}\mu(d)\mu(d+h)
\right|
\ll_\varepsilon D^{1+\varepsilon},
\]

which is stronger by essentially a factor `H` when `H` is a polynomial scale.

Thus existing averaged-Chowla theorems do not directly close the required absolute-correlation route.

Classification:

`AVERAGED_CHOWLA_ABSOLUTE_SCALE_MISMATCH`.

This does not rule out using those theorems as one component of a phase-sensitive argument.

## 8. Important nonlocality warning
The near-cell contribution need not itself be small.

Even for smooth or positive coefficients, reciprocal-phase sums can exhibit cancellation between different shift scales. Therefore forcing the `h<=H` piece separately below diagonal scale may be a stronger condition than the original mean-square problem.

Permanent guard:

`SHIFT_SCALE_COMPENSATION_GUARD` — do not replace the full signed off-diagonal kernel by independently bounded absolute shift bands unless the resulting loss is proved harmless.

This guard is especially important after the positive-coefficient false-control numerics, where the full reciprocal sum can remain at the same power scale even though no Möbius cancellation is present.

## 9. Updated live problem
The next useful object is not the absolute Chowla norm and not a generic Type-II norm. It is the **full signed reciprocal correlation kernel**

\[
\boxed{
\sum_{h}
\sum_{d}
\mu(d)\mu(d+h)
[d(d+h)]^{-1/4}
\mathcal K_{Q,K}(d,h).
}
\]

The next audit should test transformations of this whole kernel that preserve cancellation between shift scales. Natural candidates are:

1. Poisson/van-der-Corput `B` transformation in the outer `n` variable before splitting in `h`;
2. an Abel/summation-by-parts transform in the shift variable that isolates derivatives of the smooth reciprocal kernel while retaining cumulative signed Möbius correlations;
3. a two-scale decomposition with explicit overlap terms, designed so that near/far compensation is algebraically preserved rather than destroyed by triangle inequalities.
