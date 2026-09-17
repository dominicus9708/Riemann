# Möbius short-interval variance literature barrier — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Context: the Mellin/Dirichlet-polynomial reformulation reduces the critical long-factor problem to diagonal-scale mean square for Möbius short sums of length `Y=L/X`, with critical `Y=L^(1/3)`.
- Literature audit: modern almost-all short-interval cancellation is much weaker than the required variance scale when converted by a worst-case exceptional-set estimate.
- Exact random-size variance over the integers is not available here as an unconditional closure theorem.

## 1. Required short-sum scale
The long Möbius polynomial target

\[
\int_{I_X}\left|\sum_{w\asymp L}\mu(w)w^{it}\right|^2dt
\ll XL^{1+\varepsilon}
\]

corresponds through Gallagher/long-polynomial duality to the short-sum mean-square target

\[
\boxed{
\int_L^{2L}
\left|\sum_{x<m\le x+Y}\mu(m)\right|^2dx
\ll_\varepsilon LY^{1+\varepsilon},
\qquad Y=\frac LX.
}
\]

At the worst reciprocal block,

\[
X=L^{2/3},\qquad Y=L^{1/3}.
\]

This is the random/diagonal variance scale.

## 2. Modern almost-all pointwise theorem is not enough
Recent short-interval results for Möbius give, for polynomially long intervals and outside a logarithmically small exceptional set, a bound of schematic form

\[
\left|\sum_{x<m\le x+Y}\mu(m)\right|
\le Y(\log L)^{-c}.
\]

If the exceptional set has measure

\[
\ll L(\log L)^{-c},
\]

then bounding the exceptional intervals trivially by `Y` yields only

\[
\int_L^{2L}|S_Y(x)|^2dx
\ll
LY^2(\log L)^{-c}
\]

(up to changing `c`).

Compared with the required `LY`, this misses by

\[
\frac{Y}{(\log L)^c}.
\]

At `Y=L^(1/3)` this is a polynomial deficit.

Classification:

`ALMOST_ALL_LOG_SAVING_DOES_NOT_IMPLY_RANDOM_VARIANCE_SCALE`.

## 3. Relation to Möbius correlation
Expanding the variance gives

\[
\int_L^{2L}|S_Y(x)|^2dx
\asymp
LY
+2\sum_{1\le h<Y}(Y-h)
\sum_{n\asymp L}\mu(n)\mu(n+h)
\]

up to endpoint smoothing.

Thus diagonal-scale variance requires the weighted sum of binary Möbius correlations to be at most `LY` in aggregate. This is weaker than proving square-root cancellation for every fixed shift, but substantially stronger than an `o(LY^2)` averaged-Chowla statement.

## 4. Literature interpretation
Goldston--Gonek long-Dirichlet-polynomial theory explains the same obstruction from the frequency side: when polynomial length exceeds the `t`-integration length, the off-diagonal coefficient correlations become essential input.

Modern Matomäki--Radziwill--Tao style almost-all theorems establish strong logarithmic or qualitative cancellation over almost all intervals, but their published exceptional-set/log-saving scales do not by themselves imply the `LY` second-moment target at `Y=L^(1/3)`.

Older distribution/variance work on Möbius short sums formulates the random-size variance in connection with Möbius tuple/correlation conjectures, reinforcing that this is not a routine consequence of PNT-level cancellation.

## 5. Consequence for the RH project
Do not mark the Mellin/short-interval branch closed positively using an almost-all `o(Y)` result.

Current classification:

`MOBIUS_SHORT_INTERVAL_RANDOM_VARIANCE_OPEN_AT_REQUIRED_POWER`.

The useful remaining distinction is that the project does **not** need arbitrary fixed-shift Chowla. It needs only a specific smooth weighted aggregate of shifts up to `Y=L^(1/3)`. A future theorem giving this aggregate at `O(LY L^epsilon)` would close the corresponding far-resonant module even if individual correlations remain inaccessible.

References retained:
- D. A. Goldston and S. M. Gonek, *Mean value theorems for long Dirichlet polynomials and tails of Dirichlet series*, Acta Arith. 84 (1998), 155–192.
- K. Matomäki and J. Teräväinen, *On the Möbius function in all short intervals* and subsequent almost-all short-interval work.
- Recent higher-uniformity/almost-all short-interval results for Möbius in Inventiones Mathematicae (2026).
