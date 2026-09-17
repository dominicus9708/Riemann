# Stopping-branch equivalence / frame barrier audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Resolution-stopping branch decomposition: structurally useful localization, but **not a reduction in theorem strength by itself**.
- Individual stopped-branch band energies: deterministically at diagonal scale by periodicity/Parseval.
- Cross-interference upper bound at diagonal scale: exactly equivalent, up to the known branch-diagonal term, to the original mesoscopic Möbius band-energy target.
- Uniform coefficient-independent branch almost-orthogonality: numerically false at the required `O(1)` level; the normalized frame norm grows approximately like `H` in the tested cells.
- Near-lag cross term: for `0<h<H`, exactly re-enters ordinary Möbius shift correlations because same-branch pairs are impossible.
- Controlling the near-lag piece separately by absolute values would be stronger than necessary because farther lags may compensate it.

## 1. Band notation
Let

\[
I_H=[1/H,\sqrt2/H],
\qquad
P(\alpha)=\sum_{D<n\le2D}\mu(n)e(\alpha n).
\]

Partition the squarefree support by the resolution-stopping labels `B_q`, and put

\[
P_q(\alpha)=\sum_{n\in B_q}\mu(n)e(\alpha n).
\]

Define

\[
E_{\rm full}:=\int_{I_H}|P(\alpha)|^2\,d\alpha,
\]

\[
E_{\rm stop}:=\sum_q\int_{I_H}|P_q(\alpha)|^2\,d\alpha,
\]

and

\[
E_{\rm cross}:=
\sum_{q\ne r}
\int_{I_H}P_q(\alpha)\overline{P_r(\alpha)}\,d\alpha.
\]

Then exactly

\[
\boxed{E_{\rm full}=E_{\rm stop}+E_{\rm cross}.}
\]

The previous stopping-branch Parseval argument gives

\[
E_{\rm stop}\ll \frac1H\sum_{D<n\le2D}\mu(n)^2
\ll \frac DH.
\]

## 2. Exact equivalence of the remaining upper-bound problem
Because `E_stop>=0` and `E_stop=O(D/H)`, one has

\[
E_{\rm cross}\ll D/H
\quad\Longrightarrow\quad
E_{\rm full}\ll D/H.
\]

Conversely, if the original band target holds,

\[
E_{\rm full}\ll D/H,
\]

then

\[
E_{\rm cross}=E_{\rm full}-E_{\rm stop}\le E_{\rm full}\ll D/H.
\]

Hence, at the level of the required one-sided upper bound,

\[
\boxed{
E_{\rm full}\ll D/H
\iff
E_{\rm cross}\ll D/H
}
\]

once the deterministic stopped-branch diagonal estimate is inserted.

Classification:

`STOPPING_CROSS_EQUIVALENT_TO_MESOSCOPIC_BAND_TARGET`.

Therefore the stopping construction **localizes** the obstruction but does not weaken it automatically.

## 3. Near-lag re-entry into Chowla correlations
Write the full autocorrelation

\[
C_h(D)=\sum_{D<n\le 2D-h}\mu(n)\mu(n+h).
\]

For `0<h<H`, two integers in the same stopping branch would have difference divisible by the stopping divisor `q>=H`; hence this is impossible. Therefore every pair at such a shift is cross-branch and the near-lag part of `E_cross` is exactly

\[
2\sum_{1\le h<H}C_h(D)\,\operatorname{Re}K_H(h),
\]

where

\[
K_H(h)=\int_{1/H}^{\sqrt2/H}e(\alpha h)d\alpha.
\]

This gives an exact bridge to binary Möbius/Chowla shift correlations.

The Matomäki–Radziwiłł–Tao averaged Chowla theorem gives qualitative averaged cancellation over growing shift ranges, schematically

\[
\sum_{h\le H}|C_h(D)|=o(HD)
\]

for the corresponding long interval setting. Since `|K_H(h)|~1/H` for the unresolved near lags, inserting this after absolute values only gives `o(D)`, whereas the present target is `O(D/H)`. Thus existing averaged Chowla cancellation does not close the present polynomial band target by this route.

Literature boundary:
- Matomäki–Radziwiłł–Tao, *An averaged form of Chowla's conjecture*, Algebra & Number Theory 9 (2015), arXiv:1503.05121.

Permanent guard:

`AVERAGED_CHOWLA_ABSOLUTE_TRANSFER_H_LOSS`.

## 4. Near-lag smallness is still not necessary
The previous reciprocal cross-scale audit already showed that farther shifts can compensate the near cell. This remains true after the stopping decomposition.

Finite normalized near-lag contributions for Möbius include approximately

| D | H | near cross / diagonal baseline |
|---:|---:|---:|
| 4096 | 8 | -0.0169 |
| 4096 | 16 | -0.0930 |
| 8192 | 8 | +0.0337 |
| 8192 | 16 | -0.0294 |
| 16384 | 16 | +0.0602 |
| 16384 | 32 | -0.1116 |

For the squarefree-support control `mu^2`, the same near piece can be much larger and even positive, while the **full** cross term is strongly negative after farther shifts are restored.

Thus proving the near-lag Chowla piece separately at `D/H` scale is not a necessary condition for the full reciprocal band estimate.

Classification:

`STOPPING_NEAR_CHOWLA_SEPARATE_SMALLNESS_NOT_NECESSARY`.

## 5. Uniform frame almost-orthogonality test
A tempting stronger target is a coefficient-independent inequality

\[
\left\|\sum_q z_qP_q\right\|_{L^2(I_H)}^2
\le C
\sum_q|z_q|^2\|P_q\|_{L^2(I_H)}^2
\]

with an absolute `C=O(1)`.

Equivalently, normalize each nonzero branch waveform

\[
v_q=P_q/\|P_q\|_{L^2(I_H)}
\]

and ask whether the Gram/frame operator has uniformly bounded top eigenvalue.

Finite midpoint-quadrature audits give:

| D | H | coefficients inside branches | top normalized frame eigenvalue | actual full / sum branch energy |
|---:|---:|---|---:|---:|
| 4096 | 8 | `mu` | 9.35 | 0.988 |
| 4096 | 8 | `mu^2` | 9.38 | 0.126 |
| 4096 | 16 | `mu` | 17.82 | 0.919 |
| 4096 | 16 | `mu^2` | 17.83 | 0.131 |
| 8192 | 8 | `mu` | 8.49 | 1.050 |
| 8192 | 8 | `mu^2` | 8.54 | 0.128 |
| 8192 | 16 | `mu` | 16.72 | 0.967 |
| 8192 | 16 | `mu^2` | 16.70 | 0.137 |

The extremal frame norm is essentially the same for `mu` and `mu^2` and is numerically of order `H`, not `O(1)`.

Therefore the desired Möbius behavior is **not** a coefficient-independent geometric almost-orthogonality property of the stopping branch supports.

Classification:

`STOPPING_BRANCH_UNIFORM_FRAME_BOUND_H_LOSS`.

This is a numerical barrier, not an asymptotic impossibility theorem. But it rules out treating a generic branch-frame estimate as the missing mechanism without additional Möbius-specific input.

## 6. Refinement-energy telescoping
Let `P_j` be the partition obtained by exposing the first `j` ordered prime factors, while freezing any branch as soon as its prefix product reaches `H`. Define

\[
E_j:=\sum_{B\in\mathcal P_j}\int_{I_H}|P_B(\alpha)|^2d\alpha.
\]

Then `E_0=E_full` and the final `E_J=E_stop`. If a parent `B` is split into children `B_1,...,B_m`,

\[
\sum_i\|P_{B_i}\|_2^2-\|P_B\|_2^2
=-2\operatorname{Re}\sum_{i<k}\langle P_{B_i},P_{B_k}\rangle_{I_H}.
\]

Hence exactly

\[
\boxed{
E_{\rm stop}-E_{\rm full}
=\sum_j(E_{j+1}-E_j),
}
\]

so the stopping cross problem is a cumulative signed energy defect across the ordered-factorization tree.

Representative normalized levels:

| D | H | coeff. | E0 | E1 | E2 | E3 | E4 |
|---:|---:|---|---:|---:|---:|---:|---:|
| 4096 | 16 | `mu` | 0.924 | 1.009 | 1.008 | 1.005 | — |
| 4096 | 16 | `mu^2` | 0.132 | 0.578 | 1.085 | 1.006 | — |
| 8192 | 16 | `mu` | 0.970 | 0.989 | 1.001 | 1.004 | — |
| 8192 | 16 | `mu^2` | 0.137 | 0.581 | 1.082 | 1.004 | — |
| 16384 | 32 | `mu` | 0.846 | 0.972 | 0.996 | 1.002 | 1.002 |
| 16384 | 32 | `mu^2` | 0.140 | 0.519 | 0.929 | 1.000 | 1.000 |
| 8192 | 8 | `mu` | 1.051 | 1.003 | 1.001 | 1.001 | — |

The Möbius defects are small but not monotone in sign. Therefore no tree-energy monotonicity is inferred.

Moreover, at every sibling split the common newly exposed Möbius signs square out, so a local parity sign cannot force the defect sign. The small Möbius defect must come from the unresolved tail parity/phase, not from a one-step martingale sign rule.

Classification:

`SIGNED_BUCHSTAB_ENERGY_TELESCOPING_WITHOUT_LOCAL_MONOTONICITY`.

## 7. Consequence
The following stopping-tree strategies are now closed as standalone mechanisms:

1. common-prefix contraction;
2. first-divergence local parity contraction;
3. coefficient-independent `O(1)` branch-frame almost orthogonality;
4. nodewise energy monotonicity generated solely by the local Möbius sign;
5. separate absolute control of all near-lag Chowla correlations.

The stopping decomposition remains useful as a diagnostic because it isolates where the unexplained Möbius-specific cancellation lives, but the unexplained object is still theorem-equivalent to the original mesoscopic band target.

## 8. Next live decision
Two routes remain logically distinct:

- **Sector A:** seek a genuinely Möbius-specific signed operator that acts on the unresolved tail parity *before* taking the branch Gram norm; it must not collapse to fixed prime-label tensors, ordinary Buchstab recursion, or averaged Chowla after absolute values.
- **Sector B (`Q<D^(1/3)`):** return to the original discrete reciprocal curvature, where the continuous band reduction itself is no longer cheap, and test whether the additional curvature can provide cancellation unavailable in the frozen Fourier model.

Given the equivalence/barriers above, Sector B is now the cleaner independent branch to audit next.