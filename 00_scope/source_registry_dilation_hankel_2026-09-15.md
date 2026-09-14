# Audited Source Registry — Dilation / Hankel Supplement 2026-09-15

This supplement follows the same evidence rules as `00_scope/source_registry.md`.

## S039 — Tom M. Apostol, *Introduction to Analytic Number Theory*

- Type: `STANDARD_TEXTBOOK`.
- Role: Dirichlet convolution, Möbius inversion, summatory convolution and hyperbola-method baseline.
- Critical audit use: fixed floor-dilation sums are standard summatory representations of Dirichlet convolution, not a new operator family.
- Audit verdict: `ACCEPT_FOR_STANDARD_CONVOLUTION_BASELINE`.

## S040 — Jeffery Kline (2019), *A sparser matrix representation of the Mertens function*

- Type: `PRIMARY_RESEARCH`.
- Journal: Linear Algebra and its Applications 581 (2019), 354–366.
- DOI: 10.1016/j.laa.2019.07.021.
- Role: modern matrix representation of the Mertens function derived from a more general construction for multiplicative sequences and explicitly tied to Dirichlet convolution.
- Critical audit use: divisibility/matrix re-expression of Mertens is an established line and does not by itself change RH difficulty.
- Audit verdict: `ACCEPT_FOR_MERTENS_DIRICHLET_MATRIX_CONTEXT`.

## S041 — Gi-Sang Cheon & Hana Kim (2019), *Mertens equimodular matrices of Redheffer type*

- Type: `PRIMARY_RESEARCH`.
- Journal: Linear Algebra and its Applications 572 (2019), 252–272.
- DOI: 10.1016/j.laa.2019.03.009.
- Role: Redheffer-type matrices whose determinants reproduce Mertens behavior and spectral sufficient conditions related to RH.
- Critical audit use: matrix/divisibility spectral reformulations of Mertens are established and must be distinguished from independent cancellation estimates.
- Audit verdict: `ACCEPT_FOR_REDHEFFER_SPECTRAL_CONTEXT`.

## S042 — François Clément & Stefan Steinerberger (2025), *On the largest singular vector of the Redheffer matrix*

- Type: `PRIMARY_RESEARCH`.
- Journal: Linear Algebra and its Applications 725 (2025), 96–114.
- DOI: 10.1016/j.laa.2025.07.003.
- Role: recent study of Redheffer singular vectors and encoded factorization information.
- Critical audit use: current benchmark showing that divisibility-matrix spectral analysis remains active but the determinant/RH relation still ultimately encodes Mertens growth.
- Audit verdict: `ACCEPT_FOR_CURRENT_REDHEFFER_CONTEXT`.

## S043 — Alan Haynes & Wadim Zudilin (2015), *Hankel Determinants of Zeta Values*

- Type: `PRIMARY_RESEARCH`.
- Journal: SIGMA 11 (2015), 101.
- DOI: 10.3842/SIGMA.2015.101.
- Role: asymptotics of Hankel determinants constructed from zeta values at positive integers.
- Critical audit use: Hankel determinants and zeta are already linked in published work, though this object is different from the repository's `det[M(2^{k+i+j})]` scale sequence.
- Audit verdict: `ACCEPT_FOR_HANKEL_ZETA_METHOD_CONTEXT`.

## S044 — Nicholas G. Polson (2026), *Thorin, Levy and Mobius: Sign Structure in the Reciprocals of xi and zeta*

- Type: `UNREFEREED_PREPRINT / NOVELTY_CAUTION_ONLY`.
- Source: SSRN preprint, August 2026.
- Role: a different RH-related construction involving Hankel determinant positivity.
- Critical audit use: do not claim generic novelty for `Hankel determinant + RH` language.
- Limitation: not peer reviewed and not used as theorem-level evidence.
- Audit verdict: `NOVELTY_CAUTION_ONLY`.

## S045 — Wiener algebra of Dirichlet series context

- Type: `FUNCTION_SPACE_CONTEXT`.
- Role: absolutely convergent Dirichlet series form a Wiener-type Banach algebra; inverse-closed statements provide external context for the repository's elementary weighted-l1 invertibility audit.
- Critical audit use: stable coefficient-side invertibility should be treated as a Banach-algebra question, not as a hidden source of improved Mertens exponents.
- Audit verdict: `ACCEPT_FOR_INVERTIBILITY_CONTEXT_ONLY`.

## Supplement rule

- Standard convolution identities are not novelty claims.
- Matrix/Hankel representations are separated from actual arithmetic bounds.
- Unrefereed 2026 preprints are used only to prevent overclaiming novelty.
- No source in this supplement constitutes evidence that RH has been proved.
